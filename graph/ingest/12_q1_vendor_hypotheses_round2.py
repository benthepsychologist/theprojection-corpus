#!/usr/bin/env python3
"""Round 2 of "what's everything we know about where this money went" (see
graph/ingest/11_q1_vendor_hypotheses.py for round 1 and its rationale).

Ben, scaling up the ask after round 1 landed: "those are board edges...
What's everything we can find about where the $800B is going out today."
Round 1 only covered the 9 claims where the SAME company sat on both ends
of a `funds` edge (the "vendor_unspecified" bug). This round covers the
next tier by dollar size regardless of that bug -- the big equity/debt
raises (Meta's $30B bond, Oracle's $25B bond + $5B preferred, Google's
$25B bond, Intel's $20B equity, Vantage's $22B loan, Crusoe's $18.4B JV,
CoreWeave's ~$14B combined debt, Stargate LLC's $52B JV formation) where
the FIRST hop (investor -> company) was already correctly modeled, but
the SECOND hop (company -> whoever it then paid to actually build
something) was not researched at all.

Same discipline as round 1: `epistemic_status: "hypothesized"`, not
"accepted" -- these are inferences from separate reporting about a slice
of an already-tracked figure, linked via `meta.explains_claim`, never
summed into flow-type/destination totals (graph/export_q1_claims.py
already excludes epistemic_status=="hypothesized" from those, no export
script change needed for this round).

Two exceptions, both accepted-status, both because they're NOT a slice of
an existing figure -- they're a distinct, complete, well-sourced financing
fact in their own right, following the exact structural pattern already
used for the sibling fact already in the graph as "accepted":
  - Crusoe's second JPMorgan loan ($7.1B, phase 2) mirrors the existing
    accepted $2.3B JPMorgan claim (kat-claim-jpmorgan-chase-capital-...)
    exactly -- same lender entity, same predicate, same direction.
  - Five more lenders (BNP Paribas, Goldman Sachs, Societe Generale,
    Sumitomo Mitsui, Wells Fargo) joining Vantage's $22B loan syndicate
    are added as `member_of` participants on the SAME already-modeled
    lending event JPMorgan/MUFG already belong to -- a plain structural
    extension, not a new claim.

Sourcing discipline unchanged: dropped on purpose this round -- Blackstone's
reported $500M stake in Lancium (unverified single source), a "$148k/acre"
Intel land figure that didn't surface on re-search, Nvidia's $6.3B CoreWeave
capacity-backstop deal (wrong direction -- Nvidia guarantees CoreWeave's
revenue, it isn't a vendor CoreWeave pays), NextEra's $1.6B Duane Arnold
restart cost (NextEra's own capex, not a Google payment), and Meta's
Indiana LEAP District / New Albany Ohio projects (real findings, but would
need a new $10B/undisclosed accepted claim created first -- out of scope
for a vendor-hypothesis pass, flagged for a future round instead).

Run once (idempotent via id-based dedup, same pattern as round 1).
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def read(fname):
    p = os.path.join(GRAPH, fname)
    return [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []


def write(fname, rows):
    with open(os.path.join(GRAPH, fname), "w") as f:
        for r in rows:
            f.write(json.dumps(r, sort_keys=True) + "\n")


atoms = read("atoms.jsonl")
sources = read("sources.jsonl")
rels = read("relationships.jsonl")
atom_ids = {a["knowledge_atom_id"] for a in atoms if "knowledge_atom_id" in a}
source_ids = {s["source_id"] for s in sources}
rel_ids = {r["relationship_id"] for r in rels}

new_atoms, new_sources, new_rels = [], [], []


def ensure_vendor_entity(vendor_id, label, activity, part_of_canon=None):
    if vendor_id in atom_ids:
        return
    a = {
        "kind": "knowledge_atom", "atom_type": "entity", "knowledge_atom_id": vendor_id,
        "version": VER, "data_domain": DOMAIN, "sensitivity": SENS,
        "label": label, "name": label,
        "meta": {"entity_slug": slug(label), "activity": activity,
                 "origin": "graph/ingest/12_q1_vendor_hypotheses_round2.py, 2026-08-28"},
    }
    new_atoms.append(a)
    atom_ids.add(vendor_id)
    if part_of_canon:
        rid = "rel-" + slug(f"{vendor_id}:part_of:{part_of_canon}")
        if rid not in rel_ids:
            new_rels.append({
                "kind": "relationship", "relationship_id": rid, "version": VER,
                "data_domain": DOMAIN, "sensitivity": SENS,
                "name": f"{label}:part_of:{part_of_canon}",
                "predicate_id": "part_of", "review_status": "reviewed",
                "source_ref": f"knowledge_atom:{vendor_id}", "target_ref": f"knowledge_atom:{part_of_canon}",
            })
            rel_ids.add(rid)


def ensure_source(src_id, title, url, published, evidence_class):
    if src_id in source_ids:
        return
    new_sources.append({
        "kind": "source", "source_id": src_id, "version": VER,
        "data_domain": DOMAIN, "sensitivity": SENS,
        "title": title, "name": title, "locator": url,
        "published_at": published, "evidence_class": evidence_class, "source_type": "web_page",
        "meta": {"origin": "graph/ingest/12_q1_vendor_hypotheses_round2.py, 2026-08-28"},
    })
    source_ids.add(src_id)


def add_finding(company_facet, explains_claim, vendor_id, vendor_label, vendor_activity,
                 body, source_title, source_url, source_published, evidence_class,
                 amount=None, amount_basis="point", flow_type=None, destination=None,
                 part_of_canon=None):
    ensure_vendor_entity(vendor_id, vendor_label, vendor_activity, part_of_canon)
    src_id = "src-hyp2-" + slug(vendor_id + "-" + source_url)[-65:]
    ensure_source(src_id, source_title, source_url, source_published, evidence_class)

    hyp_id = "kat-hyp2-q1-" + slug(f"{company_facet}-{vendor_id}")[:75]
    if hyp_id not in atom_ids:
        claim = {
            "kind": "knowledge_atom", "atom_type": "claim", "knowledge_atom_id": hyp_id,
            "version": VER, "data_domain": DOMAIN, "sensitivity": SENS,
            "label": f"Hypothesized: {vendor_label} — {body[:80]}",
            "name": f"Hypothesized: {vendor_label} — {body[:80]}",
            "body": body, "summary": body,
            "epistemic_status": "hypothesized", "lifecycle_status": "active",
            "formalization_stage": "S3", "source_process": "inference",
            "sources": [src_id],
            "meta": {"explains_claim": explains_claim,
                     "origin": "graph/ingest/12_q1_vendor_hypotheses_round2.py, 2026-08-28"},
        }
        if amount is not None:
            claim.update({"quantity": amount, "quantity_unit": "USD", "quantity_basis": amount_basis})
            claim["meta"]["flow_type"] = flow_type
            claim["meta"]["destination_category"] = destination
        new_atoms.append(claim)
        atom_ids.add(hyp_id)

    rid = "rel-" + slug(f"{company_facet}:funds:{vendor_id}")[:90]
    if rid not in rel_ids:
        new_rels.append({
            "kind": "relationship", "relationship_id": rid, "version": VER,
            "data_domain": DOMAIN, "sensitivity": SENS,
            "name": f"{company_facet}:funds:{vendor_id}",
            "predicate_id": "funds", "review_status": "unreviewed",
            "source_ref": f"knowledge_atom:{company_facet}", "target_ref": f"knowledge_atom:{vendor_id}",
            "qualifiers": {"materialized_from_claim_ref": f"knowledge_atom:{hyp_id}"},
            "note": "Hypothesized recipient (round 2), not the original claim's own source. Not summed into any total.",
        })
        rel_ids.add(rid)


STARGATE = "kat-claim-stargate-2025-jv-financing-stargate-datacenter-construction-2025-formation-obs0"
CRUSOE_PHASE2 = "kat-claim-crusoe-2025-abilene-phase2-financing-crusoe-datacenter-construction-2025-phase2-obs1"
META_BOND = "kat-claim-ext-bond-market-meta-capital-2025-senior-notes-obs0"
ORACLE_BOND = "kat-claim-ext-bond-market-oracle-capital-2026-senior-notes-obs0"
GOOGLE_BOND = "kat-claim-ext-bond-market-google-capital-2026-25b-bond-obs0"
INTEL_EQUITY = "kat-claim-ext-public-equity-market-intel-capital-2026-stock-offering-obs0"
VANTAGE_LOAN = "kat-claim-vantage-data-centers-2025-mufg-jpmorgan-facility-vantage-data-centers-datacenter-construction-2025-debt-obs0"
COREWEAVE_ANCHOR = "kat-claim-coreweave-2026-q2-ddtl-facility-coreweave-capital-2026-debt-obs0"

TURNER = "kat-ent-turner-construction-epc-services"  # reuse -- same real company as the existing Ohio/Meta finding

# ---- Stargate LLC ($52.0B JV) ----
add_finding("kat-ent-stargate-datacenter-construction", STARGATE,
            "kat-ent-vendor-foxconn", "Foxconn", "seller of Lordstown, OH facility",
            "Foxconn sold its 6.2M sq ft former Lordstown Assembly plant to a SoftBank-affiliated "
            "buyer ('Crescent Dune LLC') for $375M, then leases it back to manufacture Stargate "
            "data center equipment; Shimizu North America LLC is the contractor starting "
            "construction there.",
            "TechCrunch", "https://techcrunch.com/2025/08/08/softbank-reportedly-bought-foxconns-ohio-factory-for-the-stargate-ai-project/",
            "2025-08-08", "published_document",
            amount=375000000, amount_basis="point", flow_type="asset purchase", destination="land, shell & materials")

add_finding("kat-ent-stargate-datacenter-construction", STARGATE,
            "kat-ent-vendor-shimizu-north-america", "Shimizu North America LLC", "general contractor",
            "Contractor starting construction at the Lordstown, Ohio Stargate equipment-manufacturing site.",
            "DataCenterDynamics",
            "https://www.datacenterdynamics.com/en/news/foxconn-and-softbank-to-manufacture-stargate-data-center-equipment-at-lordstown-ohio-facility/",
            "2025-08", "published_document")

add_finding("kat-ent-stargate-datacenter-construction", STARGATE,
            "kat-ent-vendor-bloom-energy", "Bloom Energy", "fuel-cell power equipment supplier",
            "Oracle agreed to purchase up to 2.45GW of Bloom solid-oxide fuel cells for the New "
            "Mexico Stargate/Project Jupiter site; no dollar figure disclosed, and the project is "
            "reportedly stalled after New Mexico's State Land Office denied a needed gas-pipeline application.",
            "Enverus", "https://www.enverus.com/blog/cracks-pipe-pipeline-bloom-energy-fuel-cell-data-center/",
            None, "published_document")

# ---- Crusoe Abilene JV phase 2 ($15.0B) ----
# ACCEPTED, not hypothesized -- mirrors the existing $2.3B JPMorgan claim's exact structure.
JPM_PHASE2_ID = "kat-claim-jpmorgan-chase-capital-crusoe-datacenter-construction-2026-phase2-loan-obs0"
if JPM_PHASE2_ID not in atom_ids:
    new_atoms.append({
        "kind": "knowledge_atom", "atom_type": "claim", "knowledge_atom_id": JPM_PHASE2_ID,
        "version": VER, "data_domain": DOMAIN, "sensitivity": SENS,
        "label": "JPMorgan Chase (capital (lending facet)) → Crusoe Energy Systems (datacenter "
                 "construction (Abilene, TX campus phase 2)): $7.1B construction loan",
        "name": "JPMorgan Chase -> Crusoe Energy Systems phase 2 construction loan",
        "body": "$7.1B construction loan, arranged by Newmark, for phase 2 (6 additional buildings) "
                "of the Abilene, TX Stargate campus JV (Blue Owl Capital, Crusoe, Primary Digital "
                "Infrastructure) -- a second, separate loan from JPMorgan's existing $2.3B phase 1 facility.",
        "summary": "$7.1B second JPMorgan construction loan for Crusoe's Abilene phase 2.",
        "epistemic_status": "accepted", "lifecycle_status": "active",
        "formalization_stage": "S3", "source_process": "extraction",
        "quantity": 7100000000, "quantity_unit": "USD", "quantity_basis": "point",
        "sources": ["src-hyp2-jpmorgan-crusoe-phase2-costar"],
        "meta": {"flow_type": "debt", "destination_category": "land, shell & materials",
                 "origin": "graph/ingest/12_q1_vendor_hypotheses_round2.py, 2026-08-28"},
    })
    atom_ids.add(JPM_PHASE2_ID)
ensure_source("src-hyp2-jpmorgan-crusoe-phase2-costar", "CoStar — Stargate Abilene $7.1B construction loan",
              "https://www.costar.com/article/1387166843/first-stargate-data-center-project-lands-7-1-billion-construction-loan",
              "2025-05-22", "published_document")
JPM_PHASE2_REL = "rel-jpmorgan-chase-capital-funds-crusoe-datacenter-construction-2026-phase2-loan"
if JPM_PHASE2_REL not in rel_ids:
    new_rels.append({
        "kind": "relationship", "relationship_id": JPM_PHASE2_REL, "version": VER,
        "data_domain": DOMAIN, "sensitivity": SENS,
        "name": "kat-ent-jpmorgan-chase-capital:funds:kat-ent-crusoe-datacenter-construction",
        "predicate_id": "funds", "review_status": "unreviewed",
        "source_ref": "knowledge_atom:kat-ent-jpmorgan-chase-capital",
        "target_ref": "knowledge_atom:kat-ent-crusoe-datacenter-construction",
        "qualifiers": {"materialized_from_claim_ref": f"knowledge_atom:{JPM_PHASE2_ID}"},
        "note": "Second, separate loan from the existing accepted $2.3B JPMorgan claim -- same lender, same borrower facet, different facility.",
    })
    rel_ids.add(JPM_PHASE2_REL)

add_finding("kat-ent-crusoe-datacenter-construction", CRUSOE_PHASE2,
            "kat-ent-vendor-blue-owl-crusoe-phase2-equity", "Blue Owl Capital & Crusoe (phase 2 equity)",
            "JV equity co-investors",
            "Blue Owl Capital and Crusoe reportedly contributed approximately $5B in equity for "
            "phase 2, alongside the $7.1B JPMorgan debt -- a secondary source's estimate, not an "
            "official disclosure; exact split not confirmed.",
            "Electron Economics", "https://electroneconomics.substack.com/p/hyperion-abilene-matador-portsmouth",
            None, "testimony_interested",
            amount=5000000000, amount_basis="estimate", flow_type="asset purchase", destination="land, shell & materials")

add_finding("kat-ent-crusoe-datacenter-construction", CRUSOE_PHASE2,
            "kat-ent-vendor-form-energy", "Form Energy", "battery storage equipment supplier",
            "Signed to supply 12 GWh of iron-air battery storage for the Abilene campus, deliveries "
            "starting 2027; no dollar figure disclosed.",
            "Lanin Substack (secondary; verify directly if used further)",
            "https://lanin.substack.com/", "2026-03", "testimony_interested")

# ---- Meta ($30.0B bond) ----
add_finding("kat-ent-meta-datacenter-construction", META_BOND,
            TURNER, "Turner Construction Company", "general contractor (EPC)",
            "General contractor (scope: the four primary AI data center buildings) at Meta's "
            "Hyperion campus, Richland Parish, Louisiana.",
            "Turner Construction", "https://www.turnerconstruction.com/pages/richland-parish-data-center-resource-page",
            None, "testimony_interested")

add_finding("kat-ent-meta-datacenter-construction", META_BOND,
            "kat-ent-vendor-dpr-construction", "DPR Construction", "general contractor",
            "Named general contractor at Meta's Hyperion campus, Richland Parish, Louisiana.",
            "DPR Construction", "https://www.dpr.com/projects/meta-richland-parish-data-center",
            None, "testimony_interested")

add_finding("kat-ent-meta-datacenter-construction", META_BOND,
            "kat-ent-vendor-mortenson", "Mortenson Construction", "general contractor",
            "Named general contractor at Meta's Hyperion campus, Richland Parish, Louisiana.",
            "Wikipedia — Hyperion Data Center", "https://en.wikipedia.org/wiki/Hyperion_Data_Center",
            None, "testimony_interested")

add_finding("kat-ent-meta-datacenter-construction", META_BOND,
            "kat-ent-vendor-louisiana-hyperion-vendors", "Louisiana local vendors (Meta Hyperion contractors)",
            "aggregate local contractor spend",
            "Meta states it has contracted more than $875M with roughly 160 Louisiana vendors "
            "(84% local to Northeast Louisiana) for the Hyperion campus, including named "
            "subcontractors Copeland Electric Co. (electrical) and 1LEMOINE (paving/utilities) -- "
            "an aggregate figure, not itemized per vendor.",
            "Meta Newsroom", "https://about.fb.com/news/2025/12/metas-richland-parish-data-center-supports-louisiana-economy-875-million-in-contracts/",
            "2025-12", "published_document",
            amount=875000000, amount_basis="point", flow_type="asset purchase", destination="land, shell & materials")

add_finding("kat-ent-meta-datacenter-construction", META_BOND,
            "kat-ent-vendor-entergy-louisiana-generation", "Entergy Louisiana (power generation buildout)",
            "power generation utility",
            "Entergy Louisiana is building 10 gas-fired power plants (7+ GW total, expanded from an "
            "initial 3-plant ~2,260MW plan) to power Hyperion; Meta funds the full 15-year revenue "
            "requirement. Estimated systemwide cost of the 10 plants: approximately $11B -- an "
            "estimate, not a confirmed invoice. Turbine OEM (GE Vernova/Siemens Energy/Mitsubishi "
            "Power) not publicly confirmed.",
            "Entergy / Tom's Hardware / Forbes",
            "https://www.entergy.com/news/entergy-louisiana-power-meta-s-data-center-in-richland-parish",
            "2026-03", "published_document",
            amount=11000000000, amount_basis="estimate", flow_type="asset purchase", destination="power infrastructure")

add_finding("kat-ent-meta-datacenter-construction", META_BOND,
            "kat-ent-vendor-williams-will-power", "Williams Companies (Will-Power subsidiary)",
            "power generation utility",
            "Williams' Will-Power subsidiary is building a ~200MW gas-fired 'Socrates South' plant "
            "to power Meta's New Albany, Ohio ('Prometheus') data center; no dollar figure disclosed.",
            "DataCenterDynamics",
            "https://www.datacenterdynamics.com/en/news/ohio-regulators-approve-construction-of-200mw-gas-power-plant-to-serve-meta-data-center-in-new-albany-ohio/",
            None, "published_document")

# ---- Oracle ($25.0B bond + $5.0B preferred) ----
add_finding("kat-ent-oracle-capital", ORACLE_BOND,
            "kat-ent-vendor-nvidia-oracle-gpu-order", "Nvidia (GPU sale to Oracle)",
            "GPU/compute hardware supplier",
            "Oracle reportedly ordered approximately $40B of Nvidia GB200 GPUs (~400,000 units) "
            "specifically for the Abilene, TX Stargate facility it leases to OpenAI under a "
            "15-year deal -- distinct from the broader $100B Nvidia-OpenAI investment tracked elsewhere.",
            "Network World / Tom's Hardware",
            "https://www.networkworld.com/article/3995015/oracle-to-spend-40b-on-nvidia-chips-for-openai-data-center-in-texas.html",
            None, "published_document",
            amount=40000000000, amount_basis="point", flow_type="asset purchase", destination="compute silicon & systems")

add_finding("kat-ent-oracle-capital", ORACLE_BOND,
            "kat-ent-vendor-walbridge", "Walbridge", "general contractor",
            "General contractor on the Oracle/OpenAI/Related Digital Stargate campus ('The Barn') "
            "in Saline Township, Michigan -- reported as a $16B project overall (not Walbridge's "
            "specific contract value), Walbridge's largest project in its 110-year history.",
            "Oracle newsroom / Michigan Contractor & Builder",
            "https://www.oracle.com/news/announcement/related-digital-oracle-openai-walbridge-and-governor-whitmer-celebrate-construction-of-stargate-campus-in-saline-township-2026-06-01/",
            "2026-06-01", "published_document")

# ---- Google ($25.0B bond) ----
add_finding("kat-ent-google-capital", GOOGLE_BOND,
            "kat-ent-vendor-ryan-companies", "Ryan Companies", "general contractor",
            "General contractor on Google's 'Project Skyway' data center, Pine Island, Minnesota.",
            "Equipment World", "https://www.equipmentworld.com/market-pulse/article/15816534/data-center-construction-boom-to-grow-in-2026",
            None, "testimony_interested")

add_finding("kat-ent-google-capital", GOOGLE_BOND,
            "kat-ent-vendor-whiting-turner", "Whiting-Turner Contracting Company", "general contractor",
            "Reported as a contractor for Google on hyperscale data center projects generally; no "
            "single named site or dollar figure surfaced.",
            "Buildermuse", "https://buildermuse.com/commercial/the-top-20-data-center-construction-contractors/",
            None, "testimony_interested")

add_finding("kat-ent-google-capital", GOOGLE_BOND,
            "kat-ent-vendor-monroe-county-ga", "Monroe County, Georgia (land seller)", "land seller",
            "Google bought 950 acres in Monroe County, Georgia for $58.5M (Sept 2025), near "
            "Cloverleaf's Rumble Technology Campus, for a potential data center.",
            "DataCenterDynamics", "https://www.datacenterdynamics.com/en/news/google-purchases-950-acres-for-potential-data-center-in-monroe-county-georgia/",
            "2025-09-26", "published_document",
            amount=58500000, amount_basis="point", flow_type="asset purchase", destination="land, shell & materials")

add_finding("kat-ent-google-capital", GOOGLE_BOND,
            "kat-ent-vendor-botetourt-county-va", "Botetourt County, Virginia (land seller)", "land seller",
            "Google bought approximately 312 acres from Botetourt County, Virginia for "
            "$14,055,406.37, plus a $4M contribution to county projects (June 2025).",
            "Botetourt County government", "https://www.botetourtva.gov/1021/Google-Data-Center",
            "2025-06", "published_document",
            amount=14055406, amount_basis="point", flow_type="asset purchase", destination="land, shell & materials")

add_finding("kat-ent-google-capital", GOOGLE_BOND,
            "kat-ent-vendor-kairos-power", "Kairos Power", "SMR nuclear power supplier",
            "Google backing 6-7 small modular reactors (up to 500MW total) via a US-only power "
            "purchase agreement; first unit targeted 2030; no dollar figure disclosed.",
            "DataCenterDynamics", "https://www.datacenterdynamics.com/en/news/google-signs-nuclear-smr-deal-with-kairos-for-data-center-power/",
            None, "published_document")

add_finding("kat-ent-google-capital", GOOGLE_BOND,
            "kat-ent-vendor-vertiv-google", "Vertiv", "liquid cooling equipment supplier",
            "Supplies liquid-cooling technology (coolant distribution units) used in Google's "
            "'Project Deschutes' open-standard liquid cooling design; no dollar figure disclosed.",
            "Vertiv", "https://www.vertiv.com/en-emea/solutions/ai-hub/vertiv-and-the-open-compute-project-ocp/",
            None, "testimony_interested")

# ---- Intel ($20.0B equity) ----
add_finding("kat-ent-intel-foundry-construction", INTEL_EQUITY,
            "kat-ent-vendor-bechtel", "Bechtel Corp.", "general contractor (EPC)",
            "General contractor for Phase 1 of Intel's New Albany, Ohio fab -- 2.5M sq ft "
            "including 600,000 sq ft of cleanrooms; no dollar figure disclosed for Bechtel's own contract.",
            "ENR", "https://www.enr.com/articles/55464-bechtel-wins-phase-1-contract-for-20b-intel-chip-plant-project",
            None, "published_document")

add_finding("kat-ent-intel-foundry-construction", INTEL_EQUITY,
            "kat-ent-vendor-hoffman-construction", "Hoffman Construction Co.", "general contractor",
            "General contractor for Intel's Fab 52 and Fab 62 in Chandler, Arizona; Fab 52 (~$5B, "
            "2.9M sq ft, project total not Hoffman-specific) was ENR's 2025 Project of the Year. "
            "Jacobs Engineering is the project designer.",
            "ENR", "https://www.enr.com/articles/58334-intels-20b-arizona-chip-plant-project-poised-to-make-national-impact",
            None, "published_document")

add_finding("kat-ent-intel-foundry-construction", INTEL_EQUITY,
            "kat-ent-vendor-aep-ohio-substation", "AEP Ohio (Green Chapel Station substation)",
            "power utility infrastructure",
            "AEP Ohio built a $95M, 500-megawatt substation ('Green Chapel Station') specifically "
            "for Intel's New Albany, Ohio fab; now sitting idle due to Intel's construction delay, "
            "with Meta separately seeking to draw power from it instead.",
            "WOSU / Tom's Hardware", "https://www.wosu.org/politics-government/2024-08-02/electric-build-up-for-intel-will-cost-95-million-all-of-aep-ohios-customers-could-be-on-the-hook",
            "2024-08-02", "published_document",
            amount=95000000, amount_basis="point", flow_type="asset purchase", destination="power infrastructure")

# ---- Vantage Data Centers ($22.0B loan, "Frontier" Texas megacampus) ----
add_finding("kat-ent-vantage-data-centers-datacenter-construction", VANTAGE_LOAN,
            "kat-ent-vendor-kiewit", "Kiewit Corporation", "design firm of record",
            "Named design firm of record for Vantage's 'Frontier' megacampus (Shackelford County, "
            "TX, 1,200 acres, 10 buildings, 1.4GW, ~$25B total project cost) per a Texas Department "
            "of Licensing and Regulation filing; no dollar figure attached to Kiewit's scope. No "
            "general contractor has been publicly named for Frontier as a whole.",
            "Kiewit (LinkedIn)", "https://www.linkedin.com/posts/kiewit_proud-to-partner-with-vantage-as-the-frontier-activity-7405305161444810752-aw5C",
            None, "testimony_interested")

add_finding("kat-ent-vantage-data-centers-datacenter-construction", VANTAGE_LOAN,
            TURNER, "Turner Construction Company", "general contractor (EPC)",
            "Turner Construction, together with McCarthy Building Companies (as a joint venture), "
            "plus Whiting-Turner Contracting and The Weitz Company, are named contractors on "
            "Vantage's separate 'Lighthouse' Stargate campus in Port Washington, Wisconsin ($15B "
            "project, $8B first phase) -- a different Vantage project from the Texas Frontier megacampus.",
            "ENR / Data Center Knowledge",
            "https://www.enr.com/articles/61793-construction-team-chosen-for-first-phase-of-15b-wisconsin-data-center-campus",
            None, "published_document")

# Structural addition (accepted, not a claim): five more lenders join the
# SAME already-modeled Vantage loan syndicate event JPMorgan/MUFG belong to.
VANTAGE_EVENT = "kat-evt-vantage-data-centers-2025-mufg-jpmorgan-facility"
_syndicate_source = ("src-hyp2-vantage-syndicate-bloomberg",
                      "Bloomberg — JPMorgan, MUFG to lead $22B Vantage financing",
                      "https://www.bloomberg.com/news/articles/2025-08-20/jpmorgan-mufg-to-lead-22-billion-loan-for-vantage-data-centers",
                      "2025-08-20", "published_document")
ensure_source(*_syndicate_source)
for lender_slug, lender_label in [
    ("bnp-paribas", "BNP Paribas"), ("goldman-sachs", "Goldman Sachs"),
    ("societe-generale", "Societe Generale"), ("sumitomo-mitsui-banking-corp", "Sumitomo Mitsui Banking Corp"),
    ("wells-fargo", "Wells Fargo"),
]:
    lender_id = f"kat-ent-vendor-{lender_slug}-capital"
    ensure_vendor_entity(lender_id, lender_label, "capital (lending facet)")
    rid = "rel-" + slug(f"{lender_id}:member_of:{VANTAGE_EVENT}")
    if rid not in rel_ids:
        new_rels.append({
            "kind": "relationship", "relationship_id": rid, "version": VER,
            "data_domain": DOMAIN, "sensitivity": SENS,
            "name": f"{lender_id}:member_of:{VANTAGE_EVENT}",
            "predicate_id": "member_of", "review_status": "reviewed",
            "source_ref": f"knowledge_atom:{lender_id}", "target_ref": f"knowledge_atom:{VANTAGE_EVENT}",
            "qualifiers": {"role": "participant"},
            "note": "Syndicate member alongside JPMorgan/MUFG, per Bloomberg -- individual dollar allocation not disclosed.",
        })
        rel_ids.add(rid)

# ---- CoreWeave (~$14B combined debt facilities; anchored on the largest single facility) ----
add_finding("kat-ent-coreweave-capital", COREWEAVE_ANCHOR,
            "kat-ent-vendor-dell-coreweave", "Dell", "GPU server systems integrator",
            "CoreWeave buys GPU-equipped server racks from Dell (a systems integrator, not "
            "directly from Nvidia): a $2.3B order of Dell-built GB200 NVL72 systems (PowerEdge "
            "XE9712, liquid-cooled) for 2025 delivery. Not tied to this specific $3.1B facility -- "
            "public reporting describes CoreWeave's aggregate debt/capex, not facility-by-facility use.",
            "Dell", "https://www.dell.com/en-us/blog/dell-delivers-market-s-first-nvidia-gb300-nvl72-to-coreweave/",
            None, "published_document",
            amount=2300000000, amount_basis="point", flow_type="asset purchase", destination="compute silicon & systems")

add_finding("kat-ent-coreweave-capital", COREWEAVE_ANCHOR,
            "kat-ent-vendor-supermicro-coreweave", "Supermicro", "GPU server systems integrator",
            "CoreWeave was reported as Supermicro's largest customer, approximately 22% of "
            "Supermicro's revenue (~$2.6B) across Q3 2023-Q3 2024 -- an analyst-derived revenue "
            "attribution, not a disclosed contract value.",
            "Analyst commentary (X/Twitter, Beth Kindig)", "https://x.com/Beth_Kindig/status/1832407478748778950",
            None, "testimony_interested",
            amount=2600000000, amount_basis="estimate", flow_type="asset purchase", destination="compute silicon & systems")

add_finding("kat-ent-coreweave-capital", COREWEAVE_ANCHOR,
            "kat-ent-vendor-applied-digital", "Applied Digital Corp", "datacenter landlord",
            "CoreWeave leases capacity from Applied Digital's Ellendale, ND (Polaris Forge 1) "
            "campus under two ~15-year leases, initially 250MW/~$7B projected revenue, expanded "
            "by 150MW in Aug 2025 to roughly $11B combined, amended again April 2026.",
            "Applied Digital / SEC filing", "https://ir.applieddigital.com/news-events/press-releases/detail/123/applied-digital-announces-250mw-ai-data-center-lease-with",
            "2025-08", "published_document",
            amount=11000000000, amount_basis="estimate", flow_type="capacity/service payment", destination="purchased compute capacity (services)")

add_finding("kat-ent-coreweave-capital", COREWEAVE_ANCHOR,
            "kat-ent-vendor-blue-owl-chirisa-lancaster", "Blue Owl Capital / Chirisa Technology Parks (Lancaster PA JV)",
            "datacenter landlord JV",
            "Blue Owl Capital, Chirisa Technology Parks, and Machine Investment Group closed a $4B "
            "JV funding a 100MW Lancaster, Pennsylvania campus with CoreWeave as sole tenant -- the "
            "JV's own funding total, a proxy for but not necessarily equal to CoreWeave's specific "
            "lease payments.",
            "MarketScreener", "https://www.marketscreener.com/news/blue-owl-chirisa-technology-parks-close-4-billion-funding-for-coreweave-data-center-ce7c50d8d98ff424",
            None, "published_document",
            amount=4000000000, amount_basis="estimate", flow_type="capacity/service payment", destination="purchased compute capacity (services)")

add_finding("kat-ent-coreweave-capital", COREWEAVE_ANCHOR,
            TURNER, "Turner Construction Company", "general contractor (EPC)",
            "Turner Construction and Wohlsen Construction (joint venture) are building the $6B, "
            "~100MW-expandable-to-300MW Lancaster, PA data center for CoreWeave -- may substantially "
            "overlap with the $4B Blue Owl/Chirisa JV funding total above, since both describe the "
            "same site; not additive.",
            "Turner Construction / ENR", "https://www.turnerconstruction.com/insights/coreweave-announces-multi-billion-dollar-commitment-to-ai-infrastructure-in-pennsylvania",
            None, "published_document",
            amount=6000000000, amount_basis="estimate", flow_type="asset purchase", destination="land, shell & materials")

add_finding("kat-ent-coreweave-capital", COREWEAVE_ANCHOR,
            "kat-ent-vendor-societe-generale-va-loan", "Societe Generale-led syndicate (Virginia CTP-01 loan)",
            "construction lender",
            "A Societe Generale-led syndicate provided a $600M construction loan for a separate "
            "50MW-then-120MW CoreWeave campus (CTP-01) in Chester/Chesterfield, Virginia, financed "
            "by Blue Owl Real Estate, Chirisa, and PowerHouse Data Centers.",
            "Commercial Observer", "https://commercialobserver.com/2024/12/societe-generale-600m-virginia-data-center/",
            "2024-12", "published_document",
            amount=600000000, amount_basis="point", flow_type="debt", destination="land, shell & materials")

add_finding("kat-ent-coreweave-capital", COREWEAVE_ANCHOR,
            "kat-ent-vendor-vertiv-coreweave", "Vertiv", "liquid cooling equipment supplier",
            "Supplies liquid cooling infrastructure for CoreWeave racks running Nvidia GB200 NVL72 "
            "at up to 250kW/rack; no dollar figure disclosed.",
            "Vertiv (via industry coverage)", "https://enkiai.com/ai-market-intelligence/data-center-liquid-cooling-companies/",
            None, "testimony_interested")

write("atoms.jsonl", atoms + new_atoms)
write("sources.jsonl", sources + new_sources)
write("relationships.jsonl", rels + new_rels)
print(f"{len(new_atoms)} new atom(s), {len(new_sources)} new source(s), {len(new_rels)} new relationship(s)")
