#!/usr/bin/env python3
"""Answers Ben's "what's everything we know about where this money went"
for the 11 Q1 flow claims flagged `vendor_unspecified` (2026-08-27's fix):
company capex whose own source names no external recipient. Real, sourced
public reporting DOES name contractors, equipment vendors, and land
sellers for most of these projects -- this script encodes each finding as
a real graph citizen: a new vendor/contractor entity, a `funds`
relationship from the paying company's facet to it, and a claim with
`epistemic_status: "hypothesized"` (never "accepted" -- we are inferring
"this company likely received some of the tracked spend" from separate
reporting, not reading it off the original capex claim's own source).

Hypothesis claims are NOT summed into any aggregate total (would
double-count against the parent claim's already-tracked figure) and are
NOT treated as `members` of the parent (that mechanism means "these sum to
the total", which isn't true here -- a land purchase is one slice of a
capex figure, not a decomposition of the whole). Instead each hypothesis
claim carries `meta.explains_claim` pointing at the original claim it's
evidence about; graph/export_q1_claims.py surfaces this as a distinct
"hypothesized recipients" list on the original claim's page, separate from
its point-figure total.

Sourcing discipline: only findings with a specific, checkable citation are
included. Several real leads reported by the research pass were dropped
here on purpose -- generic "TSMC is a major customer of X" claims with no
project-specific tie, and a handful of contractor names sourced only from
an aggregator site with no primary corroboration (flagged as such in the
research, e.g. Amkor/TSMC subcontractor lists from blackridgeresearch.com/
getfods.com) -- these are gaps, not filled with a guess.

Run once (idempotent via id-based dedup checks below); no upstream data
depends on re-running it, but re-running is safe.
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
                 "origin": "graph/ingest/11_q1_vendor_hypotheses.py, 2026-08-28 -- "
                           "Ben: \"What's everything we know about where this money went?\""},
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
        "meta": {"origin": "graph/ingest/11_q1_vendor_hypotheses.py, 2026-08-28"},
    })
    source_ids.add(src_id)


def add_finding(company_facet, explains_claim, vendor_id, vendor_label, vendor_activity,
                 body, source_title, source_url, source_published, evidence_class,
                 amount=None, amount_basis="point", flow_type=None, destination=None,
                 part_of_canon=None):
    ensure_vendor_entity(vendor_id, vendor_label, vendor_activity, part_of_canon)
    src_id = "src-hyp-" + slug(vendor_id + "-" + source_url)[-70:]
    ensure_source(src_id, source_title, source_url, source_published, evidence_class)

    hyp_id = "kat-hyp-q1-" + slug(f"{company_facet}-{vendor_id}")[:80]
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
                     "origin": "graph/ingest/11_q1_vendor_hypotheses.py, 2026-08-28"},
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
            "note": "Hypothesized recipient, not the original claim's own source -- "
                    "see the claim's own citation. Not summed into any total.",
        })
        rel_ids.add(rid)


# ---- TSMC (Arizona / US expansion / CoWoS / 2026 capex) ----
TSMC_AZ_INTENT = "kat-claim-tsmc-capital-tsmc-foundry-construction-2020-az-intent-obs0"
TSMC_US_EXPANSION = "kat-claim-tsmc-capital-tsmc-foundry-construction-2025-us-expansion-obs0"

add_finding("kat-ent-tsmc-foundry-construction", TSMC_AZ_INTENT,
            "kat-ent-vendor-yates-construction", "Yates Construction", "general contractor (EPC)",
            "General contractor on TSMC's Arizona Fab 21 (broke ground 2022, targeted 2024 completion).",
            "Tom's Hardware — TSMC Fab 21 Arizona", "https://www.tomshardware.com/news/tsmc-fab-21-arizona",
            "2022", "published_document")

add_finding("kat-ent-tsmc-foundry-construction", TSMC_AZ_INTENT,
            "kat-ent-vendor-united-integrated-services", "United Integrated Services (UIS)",
            "MEP/cleanroom construction contractor",
            "Delivers mechanical/electrical/plumbing and cleanroom construction services at TSMC's "
            "Arizona Fab 21; reported to derive 50-60% of total revenue from TSMC's US fabs.",
            "Taipei Times", "https://www.taipeitimes.com/News/biz/archives/2025/03/06/2003832936",
            "2025-03-06", "published_document")

add_finding("kat-ent-tsmc-foundry-construction", TSMC_AZ_INTENT,
            "kat-ent-vendor-ctci-americas", "CTCI Americas", "EPC contractor",
            "Taiwanese EPC firm; opened an Arizona subsidiary specifically to provide "
            "engineering-procurement-construction services for TSMC's Arizona buildout.",
            "CTCI e-newsletter", "https://www.ctci.com/e-newsletter/EN/467/hot-news/article-01.html",
            None, "testimony_interested")

add_finding("kat-ent-tsmc-foundry-construction", TSMC_AZ_INTENT,
            "kat-ent-vendor-marketech-international", "Marketech International",
            "cleanroom/facility integration contractor",
            "Turnkey cleanroom/facility integration (MEP, DI water, gas/chemical supply, wastewater) "
            "for TSMC's Arizona fabs; reported to derive 20-30% of revenue from TSMC's US fabs.",
            "Taipei Times", "https://www.taipeitimes.com/News/biz/archives/2025/03/06/2003832936",
            "2025-03-06", "published_document")

add_finding("kat-ent-tsmc-foundry-construction", TSMC_US_EXPANSION,
            "kat-ent-vendor-arizona-state-land-department", "Arizona State Land Department",
            "land seller (state trust land auction)",
            "TSMC won a January 2026 Arizona State Land Department auction for 900 acres "
            "(part of the NorthPark development adjacent to its existing campus) for $197.25M.",
            "AZ Big Media", "https://azbigmedia.com/real-estate/tsmc-buys-900-acres-of-land-in-north-phoenix-for-197-million/",
            "2026-01", "published_document",
            amount=197250000, amount_basis="point", flow_type="asset purchase", destination="land, shell & materials")

# ---- SK hynix (Yongin / Cheongju) ----
SK_HYNIX_YONGIN = "kat-claim-sk-hynix-capital-sk-hynix-memory-fab-construction-2026-yongin-cheongju-obs0"

add_finding("kat-ent-sk-hynix-memory-fab-construction", SK_HYNIX_YONGIN,
            "kat-ent-vendor-sk-ecoplant", "SK ecoplant", "EPC contractor (affiliate)",
            "EPC affiliate handling engineering-procurement-construction work on the Yongin "
            "semiconductor cluster and its support facilities (cogeneration plant, industrial-complex development).",
            "Korea business press (via en.sedaily.com)",
            "https://en.sedaily.com/business/2026/05/25/korean-builders-ride-samsung-sk-hynix-chip-investment-boom",
            "2026-05-25", "published_document")

add_finding("kat-ent-sk-hynix-memory-fab-construction", SK_HYNIX_YONGIN,
            "kat-ent-vendor-techcross-water-energy", "Techcross Water & Energy",
            "wastewater-treatment EPC contractor",
            "Letter of intent worth approximately 50 billion won (~$35M) for Phase 2 "
            "wastewater-treatment EPC work at the Yongin fab -- an LOI, not yet a signed contract.",
            "TheLEC", "https://www.thelec.net/news/articleView.html?idxno=11815", "2026", "published_document",
            amount=35000000, amount_basis="estimate", flow_type="asset purchase", destination="land, shell & materials")

add_finding("kat-ent-sk-hynix-memory-fab-construction", SK_HYNIX_YONGIN,
            "kat-ent-vendor-temc-cns", "TEMC CNS", "chemical supply system contractor",
            "Confirmed KRW 25.25B (~$18.7M) contract, signed June 26 2026, to supply/install the "
            "Central Chemical Supply System (CCSS) for the Yongin fab.",
            "TheLEC", "https://www.thelec.net/news/articleView.html?idxno=11743", "2026-06-26", "published_document",
            amount=18700000, amount_basis="point", flow_type="asset purchase", destination="land, shell & materials")

add_finding("kat-ent-sk-hynix-memory-fab-construction", SK_HYNIX_YONGIN,
            "kat-ent-asml-equipment-sales", "ASML", "EUV lithography equipment supplier",
            "Record order: SK hynix committed KRW 11.9 trillion (~$7.9B) for approximately 30 ASML "
            "EUV lithography scanners through end-2027, split between the Cheongju M15X fab (HBM) "
            "and the Yongin cluster (advanced DRAM) -- this may overlap with rather than sit fully "
            "on top of the already-tracked $38.1B Yongin/Cheongju combined investment.",
            "Tom's Hardware",
            "https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-places-record-8-billion-order-for-asml-euv-lithography-machines",
            "2026", "published_document",
            amount=7900000000, amount_basis="point", flow_type="asset purchase", destination="compute silicon & systems",
            part_of_canon="kat-canon-asml")

# ---- Samsung (Taylor, TX) ----
SAMSUNG_TAYLOR = "kat-claim-samsung-capital-samsung-foundry-construction-2021-taylor-tx-obs0"

add_finding("kat-ent-samsung-foundry-construction", SAMSUNG_TAYLOR,
            "kat-ent-vendor-yates-construction", "Yates Construction", "general contractor (EPC)",
            "General contractor for Samsung's $17B (later $25B) Taylor, Texas foundry.",
            "Construction Dive",
            "https://www.constructiondive.com/news/samsung-picks-builder-yates-construction-17b-chip-plant-taylor-texas/625884/",
            None, "published_document")

add_finding("kat-ent-samsung-foundry-construction", SAMSUNG_TAYLOR,
            "kat-ent-vendor-epcor-utilities", "EPCOR Utilities", "water infrastructure contractor/operator",
            "Selected to design, build, and operate industrial water supply and reclamation "
            "infrastructure (Sandow Water Project, Blue Sky Water Reclamation Facility) for the "
            "Taylor site; $300M initial equity investment by EPCOR.",
            "EPCOR press release",
            "https://www.epcor.com/us/en/news/media-releases/2023-07-13-epcor-tapped-water-partner-central-texas.html",
            "2023-07-13", "published_document",
            amount=300000000, amount_basis="point", flow_type="asset purchase", destination="land, shell & materials")

# ---- Micron (Idaho) ----
MICRON_IDAHO = "kat-claim-micron-capital-micron-memory-fab-construction-2022-idaho-obs0"

add_finding("kat-ent-micron-memory-fab-construction", MICRON_IDAHO,
            "kat-ent-vendor-exyte", "Exyte", "general contractor (cleanroom construction; role later reduced)",
            "Hired as general contractor for Micron's Boise, Idaho fab after the 2022 announcement; "
            "Micron terminated Exyte's GC contract effective Sept 2, 2025 (per an Idaho Department "
            "of Labor filing), retaining Exyte afterward only as lead architect/engineer for Phase 1 design.",
            "Yahoo Finance", "https://finance.yahoo.com/news/micron-dropped-general-contractor-building-110000454.html",
            "2025-09", "published_document")

add_finding("kat-ent-micron-memory-fab-construction", MICRON_IDAHO,
            "kat-ent-vendor-yates-layton-jv", "Yates/Layton Joint Venture", "construction manager-at-risk",
            "Construction manager-at-risk (a Yates/Layton joint venture, a separate entity from "
            "Yates Construction alone) under a guaranteed-maximum-price contract for Micron's Boise "
            "fab; approximately 6,000 trades workers on site at peak.",
            "Construction Exchange", "https://exchange.construction/projects/industrial/micron-boise-fab-id1/",
            None, "testimony_interested")

# ---- ASE Technology (LEAP program, Kaohsiung) ----
ASE_LEAP = "kat-claim-ase-capital-ase-packaging-construction-2026-capex-obs0"

add_finding("kat-ent-ase-packaging-construction", ASE_LEAP,
            "kat-ent-vendor-hung-ching-construction", "Hung Ching Construction",
            "joint-venture construction partner / landlord",
            "Hung Ching Construction sold ASE the existing K18 facility for approximately NT$5.26B "
            "(~$163.4M); Hung Ching also holds a 77.76% stake in the K28 plant joint venture versus "
            "ASE's 22.24% (ASE contributed the land, Hung Ching funds the construction).",
            "Taipei Times / DIGITIMES",
            "https://www.taipeitimes.com/News/biz/archives/2024/08/10/2003822006",
            "2024-08-10", "published_document",
            amount=163400000, amount_basis="point", flow_type="asset purchase", destination="land, shell & materials")

add_finding("kat-ent-ase-packaging-construction", ASE_LEAP,
            "kat-ent-vendor-wus-printed-circuit", "WUS Printed Circuit", "substrate supplier / JV partner",
            "Joint facility announced with WUS Printed Circuit in Nanzih Park (~113,000 sqm, "
            "completion targeted September 2029) for FOCoS/FC BGA substrate production -- a "
            "co-investment partnership; no dollar figure attributed to WUS specifically.",
            "MarketScreener",
            "https://www.marketscreener.com/news/ase-technology-and-wus-announce-strategic-collaboration-to-build-advanced-ai-packaging-hub-in-kaoh-ce7f5bdbd98ef321",
            None, "testimony_interested")

# ---- Amkor Technology (Peoria, Arizona) ----
AMKOR_ARIZONA = "kat-claim-amkor-capital-amkor-packaging-construction-2025-arizona-obs0"

add_finding("kat-ent-amkor-packaging-construction", AMKOR_ARIZONA,
            "kat-ent-vendor-okland-construction", "Okland Construction", "general contractor",
            "Contractor for Amkor's Peoria, Arizona OSAT facility (per ENR's 2026 Top Owners "
            "coverage); first-phase construction cost reported at $1B project-wide -- not confirmed "
            "as Okland's own contract value specifically.",
            "ENR", "https://www.enr.com/articles/62804-enr-2026-top-owners-byte-down-on-ai-boom",
            "2026", "published_document")

add_finding("kat-ent-amkor-packaging-construction", AMKOR_ARIZONA,
            "kat-ent-vendor-ssoe-group", "SSOE Group", "engineering firm",
            "Engineering firm for Amkor's Peoria, Arizona facility.",
            "ENR", "https://www.enr.com/articles/62804-enr-2026-top-owners-byte-down-on-ai-boom",
            "2026", "published_document")

add_finding("kat-ent-amkor-packaging-construction", AMKOR_ARIZONA,
            "kat-ent-vendor-vistancia-development", "Vistancia Development LLC", "land seller",
            "Amkor purchased 67 acres from Vistancia Development LLC for $32,475,278.",
            "City of Peoria", "https://www.peoriaaz.gov/Home/Components/News/News/7705/439",
            None, "published_document",
            amount=32475278, amount_basis="point", flow_type="asset purchase", destination="land, shell & materials")

# ---- Core Scientific (Denton, TX) ----
CORE_SCIENTIFIC_DENTON = "kat-claim-core-scientific-capital-core-scientific-datacenter-construction-2024-denton-investment-obs0"

add_finding("kat-ent-core-scientific-datacenter-construction", CORE_SCIENTIFIC_DENTON,
            "kat-ent-vendor-evans-general-contractors", "Evans General Contractors", "general contractor",
            "General contractor for Core Scientific's Denton, Texas data center expansion.",
            "Moss Utilities project page", "https://mossutilities.com/projects/core-scientific/",
            None, "testimony_interested")

add_finding("kat-ent-core-scientific-datacenter-construction", CORE_SCIENTIFIC_DENTON,
            "kat-ent-vendor-moss-utilities", "Moss Utilities", "underground utility contractor",
            "Delivered the underground utility package for Core Scientific's Denton, Texas data center.",
            "Moss Utilities project page", "https://mossutilities.com/projects/core-scientific/",
            None, "testimony_interested")

write("atoms.jsonl", atoms + new_atoms)
write("sources.jsonl", sources + new_sources)
write("relationships.jsonl", rels + new_rels)
print(f"{len(new_atoms)} new atom(s), {len(new_sources)} new source(s), {len(new_rels)} new relationship(s)")
