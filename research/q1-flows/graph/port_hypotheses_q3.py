#!/usr/bin/env python3
"""One-time port (2026-08-27, Ben: "port everything you can"): everything in
this repo that already has a proposition-with-a-truth-state shape goes into
the graph. Run ONCE after build_graph.py; guards on existing ids so a re-run
is a no-op. Five things, in order:

1. Backfill epistemic fields build_graph.py omitted: every seeded claim gets
   epistemic_status=accepted / source_process=extraction (the composition
   design's "fact" posture, AGENTS.md discipline 1 + the 2026-08-27 ruling
   that the graph holds propositions only).
2. TSMC's advanced-packaging range ($6-12.8B) is derived as 10-20% of a
   $60-64B FY2026 capex guidance that lives ONLY inside its note. Add the
   guidance as its own claim, sourced to the same earnings-call transcript
   already in sources.jsonl, then link derived_from + inference_basis. This
   is the honest port: the input to a derivation must itself be a claim.
3. Amazon->Anthropic $8B cumulative: pure arithmetic, no artifact (has_part
   already links its parts). Mark source_process=inference, inference_basis
   = the two part claims. Crusoe's $15B is NOT marked inference -- it's
   company-stated (a real press release supports it) and merely also sums.
4. attention/upcoming.yaml: the 16 financing-relevant expectations become
   hypothesis claims. Mapping, all landed fields:
     claim            -> summary/body
     what_confirms    -> defeat_conditions   (trait_epistemic -- exactly this)
     confidence       -> epistemic_confidence_band (confirmed=high, reported=medium)
     status pending   -> epistemic_status=hypothesized
     status hit       -> accepted + an annotation(extraction_review) carrying
                         the resolution's evidence prose as justification --
                         NOT a fabricated source object; the evidence is the
                         reviewing agent's finding, citing outlets in prose
     passed-silent    -> rejected (the dated proposition was falsified)
     slipped          -> hypothesized, meta.slips carried
     source (url)     -> a real source + supports (the reporting that made
                         us log the expectation)
     entities         -> about relationships where the entity already exists
                         in the graph (matched on meta.entity_slug)
     thread/due/...   -> meta (threads aren't in the graph yet -- pointer only)
   upcoming.yaml itself is NOT modified -- it stays the operational ledger
   /daily and /week read. This is a copy-in, and the two will drift until
   the attention-corpus migration (separate design) retires the YAML.
5. research/q3-datacenter-census/attribution.yaml: 28 facilities become
   entity atoms (meta.q3_facility=true, epoch_current_mw, control_cut,
   coverage_state). Attribution roles (operator/propco/tenant/end_user/
   owner_of_record) become related_to relationships with qualifiers.role,
   facility -> entity, ONLY where the prose names an entity already in the
   graph (substring match on the graph's entity labels). Unmatched roles
   stay as meta.attribution.<role> prose on the facility atom -- structured
   where matchable, honest prose where not. ⚠️ GAP FLAGGED, not invented:
   no landed predicate says operates/owns/leases; related_to + role
   qualifier is the least-wrong landed shape. Filed for round three+ if a
   second consumer needs it.
"""
import json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
TODAY = datetime.date.today().isoformat()
ORIGIN = f"port_hypotheses_q3.py, {TODAY} (one-time port; Ben: 'port everything you can')"

def slug(s): return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
def rel_id(s, p, t): return "rel-" + slug(f"{s}:{p}:{t}")
def rel_name(s, p, t):
    b = lambda r: r.split(":", 1)[1]
    return f"{b(s)}:{p}:{b(t)}"
def base(kind, idf, idv, name):
    return {"kind": kind, idf: idv, "version": VER, "name": name, "data_domain": DOMAIN, "sensitivity": SENS}
def band(r):
    if r is None: return None
    return "strong" if r >= 0.8 else "moderate" if r >= 0.5 else "weak"

def read(fname):
    p = os.path.join(HERE, fname)
    return [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []
def write(fname, rows):
    with open(os.path.join(HERE, fname), "w") as f:
        for r in rows: f.write(json.dumps(r, sort_keys=True) + "\n")

atoms, sources, rels, annos, passes = (read(f) for f in
    ("atoms.jsonl", "sources.jsonl", "relationships.jsonl", "annotations.jsonl", "extraction_passes.jsonl"))
atom_ids = {a["knowledge_atom_id"] for a in atoms}
rel_ids = {r["relationship_id"] for r in rels}
src_ids = {s["source_id"] for s in sources}
ann_ids = {a["annotation_id"] for a in annos}
ep_ids = {p["extraction_pass_id"] for p in passes}
notes = []

def add_atom(a):
    if a["knowledge_atom_id"] in atom_ids: return False
    atoms.append(a); atom_ids.add(a["knowledge_atom_id"]); return True
def add_rel(r):
    if r["relationship_id"] in rel_ids: return False
    rels.append(r); rel_ids.add(r["relationship_id"]); return True
def add_src(s):
    if s["source_id"] in src_ids: return False
    sources.append(s); src_ids.add(s["source_id"]); return True
def add_ann(a):
    if a["annotation_id"] in ann_ids: return False
    annos.append(a); ann_ids.add(a["annotation_id"]); return True
def add_pass(p):
    if p["extraction_pass_id"] in ep_ids: return False
    passes.append(p); ep_ids.add(p["extraction_pass_id"]); return True

entity_by_slug = {}
entity_labels = []
for a in atoms:
    if a.get("atom_type") in ("entity", "event"):
        es = a.get("meta", {}).get("entity_slug")
        if es: entity_by_slug.setdefault(es, a)
        entity_labels.append((a["label"], a))

# ---------- 1. backfill epistemic posture on every seeded claim ----------
n = 0
for a in atoms:
    if a.get("atom_type") == "claim" and "epistemic_status" not in a:
        a["epistemic_status"] = "accepted"; a["source_process"] = "extraction"; n += 1
notes.append(f"backfilled epistemic_status=accepted/source_process=extraction on {n} seeded claims")

# ---------- 2. TSMC guidance claim + derived_from ----------
pkg_id = "kat-claim-tsmc-capital-tsmc-advanced-packaging-construction-2026-capex-share-obs0"
pkg = next((a for a in atoms if a["knowledge_atom_id"] == pkg_id), None)
if pkg:
    guide_src = next((s["source_id"] for s in sources if s["source_id"].startswith(
        "src-tsmc-capital-tsmc-advanced-packaging-construction-2026-capex-share")), None)
    gid = "kat-claim-tsmc-capital-tsmc-fy2026-capex-guidance"
    g_summary = "TSMC raised FY2026 capital-expenditure guidance to $60-64B; 70-80% advanced process, ~10% specialty, 10-20% advanced packaging/testing/mask-making/other."
    g = base("knowledge_atom", "knowledge_atom_id", gid, "TSMC guided FY2026 capex to $60-64B (Q2 2026 earnings call)")
    g.update({"atom_type": "claim", "label": g["name"],
              "summary": g_summary,
              "body": g_summary, "epistemic_status": "accepted", "source_process": "extraction",
              "meta": {"q1_from_node": "tsmc/capital", "q1_to_node": "tsmc/capital", "flow_type": "capex",
                       "destination_category": "n/a — financing", "quantity_lower": 60_000_000_000,
                       "quantity_upper": 64_000_000_000, "quantity_unit": "USD", "quantity_basis": "range",
                       "entity_slug": "tsmc", "origin": ORIGIN,
                       "note": "Added so the packaging-share derivation has a real input claim; the guidance was previously only inside that claim's note."},
              "formalization_stage": "S3", "lifecycle_status": "active",
              "sources": [guide_src] if guide_src else []})
    if add_atom(g):
        gref, pref = f"knowledge_atom:{gid}", f"knowledge_atom:{pkg_id}"
        if guide_src:
            sref = f"source:{guide_src}"
            r = base("relationship", "relationship_id", rel_id(sref, "supports", gref), rel_name(sref, "supports", gref))
            r.update({"source_ref": sref, "target_ref": gref, "predicate_id": "supports",
                      "evidence_class": "testimony_interested", "evidence_strength_band": "strong",
                      "evidence_weight": 0.85, "review_status": "unreviewed",
                      "note": "Company's own earnings-call statement of its guidance -- interested testimony, high reliability as a record of what was said."})
            add_rel(r)
        tsmc = entity_by_slug.get("tsmc")
        if tsmc:
            eref = f"knowledge_atom:{tsmc['knowledge_atom_id']}"
            r = base("relationship", "relationship_id", rel_id(gref, "about", eref), rel_name(gref, "about", eref))
            r.update({"source_ref": gref, "target_ref": eref, "predicate_id": "about", "qualifiers": {"role": "subject"}, "review_status": "unreviewed"})
            add_rel(r)
        r = base("relationship", "relationship_id", rel_id(pref, "derived_from", gref), rel_name(pref, "derived_from", gref))
        r.update({"source_ref": pref, "target_ref": gref, "predicate_id": "derived_from", "review_status": "reviewed",
                  "note": "10-20% of the guidance range, bucketed with testing/mask-making -- arithmetic on a stated percentage, not an isolated packaging figure."})
        add_rel(r)
        pkg["source_process"] = "inference"; pkg["inference_basis"] = [gid]
        notes.append(f"TSMC: added guidance claim {gid}; packaging range now derived_from it")

# ---------- 3. Amazon $8B: pure derivation ----------
amz = next((a for a in atoms if a["knowledge_atom_id"] == "kat-claim-amazon-capital-anthropic-capital-2024-11-additional-obs1"), None)
if amz:
    parts = [r["target_ref"].split(":", 1)[1] for r in rels
             if r["predicate_id"] == "has_part" and r["source_ref"].endswith(amz["knowledge_atom_id"])]
    amz["source_process"] = "inference"; amz["inference_basis"] = parts
    notes.append(f"Amazon $8B marked inference; basis={parts}")

# ---------- 4. financing expectations -> hypothesis claims ----------
up = yaml.safe_load(open(os.path.join(REPO, "attention", "upcoming.yaml")))
items = up[[k for k, v in up.items() if isinstance(v, list)][0]]
FIN = {'ai-circular-financing-risk','frontier-lab-ipos','nvidia-vendor-financing','softbank-all-in','fidelity-buys-ai-labs',
       'ai-compute-spend','anthropic-infrastructure-buildout','where-the-capex-lands','hyperscaler-capex-big-picture',
       'datacenter-backlash-capital-risk','ai-datacenter-sites','stargate-buildout','oracle-stargate-bet','coreweave-backlog-bet',
       'intel-rescue','chips-equity-pivot','pif-ai-buildout','custom-asic-tolls','nvidia-order-book','treasury-long-end-intervention'}
STATUS = {"pending": "hypothesized", "hit": "accepted", "slipped": "hypothesized", "passed-silent": "rejected"}
CONF = {"confirmed": "high", "reported": "medium"}
ported = 0
for it in items:
    if it.get("thread") not in FIN: continue
    hid = f"kat-hyp-{slug(it['id'])}"
    claim_text = " ".join(str(it["claim"]).split())
    h = base("knowledge_atom", "knowledge_atom_id", hid, claim_text[:160])
    h.update({"atom_type": "claim", "label": claim_text[:160], "summary": claim_text, "body": claim_text,
              "epistemic_status": STATUS.get(it.get("status"), "hypothesized"),
              "epistemic_confidence_band": CONF.get(it.get("confidence")),
              "source_process": "inference",
              "defeat_conditions": " ".join(str(it.get("what_confirms", "")).split()) or None,
              "valid_to": str(it.get("due")) if it.get("status") in ("pending", "slipped") else None,
              "meta": {k: v for k, v in {
                  "upcoming_id": it["id"], "thread": it.get("thread"), "due": str(it.get("due")),
                  "due_precision": it.get("due_precision"), "upcoming_status": it.get("status"),
                  "resolved": str(it.get("resolved")) if it.get("resolved") else None,
                  "slips": it.get("slips"), "logged": str(it.get("logged")), "logged_by": it.get("logged_by"),
                  "entities": it.get("entities"), "origin": ORIGIN}.items() if v not in (None, [], "")},
              "formalization_stage": "S4", "lifecycle_status": "active", "sources": []})
    h = {k: v for k, v in h.items() if v is not None}
    if not add_atom(h): continue
    href = f"knowledge_atom:{hid}"
    ported += 1
    # the reporting that made us log it
    if it.get("source"):
        sid = "src-" + slug(f"upcoming-{it['id']}")[:80]
        s = base("source", "source_id", sid, f"logging source for {it['id']}")
        s.update({"source_type": "web_page", "title": s["name"], "locator": str(it["source"]),
                  "evidence_class": "published_document", "meta": {"origin": ORIGIN}})
        add_src(s); h["sources"].append(sid)
        r = base("relationship", "relationship_id", rel_id(f"source:{sid}", "supports", href), rel_name(f"source:{sid}", "supports", href))
        r.update({"source_ref": f"source:{sid}", "target_ref": href, "predicate_id": "supports",
                  "evidence_class": "published_document", "evidence_strength_band": band(0.6), "evidence_weight": 0.6,
                  "review_status": "unreviewed", "note": "The reporting the expectation was logged from -- supports that the event is expected, not that it happened."})
        add_rel(r)
    # about -> existing entities
    for ent in it.get("entities") or []:
        e = entity_by_slug.get(slug(ent))
        if e:
            eref = f"knowledge_atom:{e['knowledge_atom_id']}"
            r = base("relationship", "relationship_id", rel_id(href, "about", eref), rel_name(href, "about", eref))
            r.update({"source_ref": href, "target_ref": eref, "predicate_id": "about", "qualifiers": {"role": "subject"}, "review_status": "unreviewed"})
            add_rel(r)
    # resolution -> extraction_review annotation (a reviewing agent's finding, not a source artifact)
    if it.get("status") in ("hit", "passed-silent") and it.get("evidence"):
        pid = "ep-" + slug(f"resolve-{it['id']}")[:60]
        p = base("extraction_pass", "extraction_pass_id", pid, f"resolution check for {it['id']}")
        p.update({"pass_type": "A5", "pass_iteration": 2, "pass_mode": "adjudication",
                  "agent_identity": "claude-session-theprojection-corpus-week-2026-08-27",
                  "methodology_version": "attention-week-expectations-scorecard",
                  "source_target_refs": [f"source:{h['sources'][0]}"] if h["sources"] else [],
                  "meta": {"note": "source_target_refs (list) used per round-three brief; no single artifact -- the resolution cited outlets in prose."}})
        if not p["source_target_refs"]:
            p["source_target_ref"] = "source:unspecified-resolution-prose"; del p["source_target_refs"]
        add_pass(p)
        a = base("annotation", "annotation_id", "ann-" + slug(f"resolve-{it['id']}")[:70], f"resolution of {it['id']}")
        a.update({"annotation_type": "extraction_review", "target_ref": href, "generated_by_ref": f"extraction_pass:{pid}",
                  "justification": " ".join(str(it["evidence"]).split()),
                  "extraction_confidence": "high" if it.get("status") == "hit" else "medium"})
        add_ann(a)
notes.append(f"ported {ported} financing expectations as hypothesis claims")

# ---------- 5. q3 facilities ----------
q3 = yaml.safe_load(open(os.path.join(REPO, "research", "q3-datacenter-census", "attribution.yaml")))["records"]
ROLE_PRED_GAP = "related_to"   # no landed operates/owns/leases predicate -- flagged
def match_entity(prose):
    if not prose: return None
    p = str(prose).lower()
    best = None
    for label, a in entity_labels:
        bare = label.split(" (")[0].lower()
        if len(bare) >= 4 and bare in p and (best is None or len(bare) > len(best[0])):
            best = (bare, a)
    return best[1] if best else None
fac_n = role_n = unmatched = 0
for rec in q3:
    fid = "kat-fac-" + slug(rec["facility"])
    f = base("knowledge_atom", "knowledge_atom_id", fid, rec["facility"])
    attr = rec.get("attribution") or {}
    f.update({"atom_type": "entity", "label": rec["facility"], "tags": ["datacenter-facility", rec.get("control_cut")],
              "body": rec.get("notes"),
              "meta": {k: v for k, v in {"q3_facility": True, "entity_slug": slug(rec["facility"]),
                       "epoch_current_mw": rec.get("epoch_current_mw"), "country": rec.get("country"),
                       "control_cut": rec.get("control_cut"), "coverage_state": rec.get("coverage_state"),
                       "attribution": attr, "origin": ORIGIN}.items() if v is not None},
              "formalization_stage": "S2", "lifecycle_status": "active", "sources": []})
    if not add_atom(f): continue
    fac_n += 1
    fref = f"knowledge_atom:{fid}"
    for i, s in enumerate(rec.get("sources") or []):
        sid = "src-" + slug(f"q3-{rec['facility']}-{i}-{s.get('label','')}")[:80]
        so = base("source", "source_id", sid, s.get("label") or "untitled")
        so.update({"source_type": "web_page" if s.get("url") else "other", "title": s.get("label"), "locator": s.get("url"),
                   "published_at": str(s.get("as_of")) if s.get("as_of") else None, "evidence_class": "published_document",
                   "meta": {"q3_figure_text": s.get("figure"), "origin": ORIGIN}})
        so = {k: v for k, v in so.items() if v is not None}
        add_src(so); f["sources"].append(sid)
        r = base("relationship", "relationship_id", rel_id(f"source:{sid}", "supports", fref), rel_name(f"source:{sid}", "supports", fref))
        r.update({"source_ref": f"source:{sid}", "target_ref": fref, "predicate_id": "supports",
                  "evidence_class": "published_document", "review_status": "unreviewed"})
        add_rel(r)
    for role, prose in attr.items():
        ent = match_entity(prose)
        if not ent: unmatched += 1; continue
        eref = f"knowledge_atom:{ent['knowledge_atom_id']}"
        r = base("relationship", "relationship_id", rel_id(fref, ROLE_PRED_GAP, eref) + "-" + slug(role),
                 rel_name(fref, ROLE_PRED_GAP, eref))
        r.update({"source_ref": fref, "target_ref": eref, "predicate_id": ROLE_PRED_GAP,
                  "qualifiers": {"role": role, "attribution_prose": " ".join(str(prose).split())[:300]},
                  "review_status": "unreviewed",
                  "note": "GAP: no landed operates/owns/leases predicate; related_to + qualifiers.role is the least-wrong landed shape. Entity matched by label substring -- review."})
        add_rel(r); role_n += 1
notes.append(f"q3: {fac_n} facilities ported; {role_n} attribution roles linked via related_to+role; {unmatched} roles left as prose (no matching entity in graph)")

write("atoms.jsonl", atoms); write("sources.jsonl", sources); write("relationships.jsonl", rels)
write("annotations.jsonl", annos); write("extraction_passes.jsonl", passes)
with open(os.path.join(HERE, "port-notes.txt"), "w") as fh: fh.write("\n".join(notes))
print("\n".join(notes))
print(f"\ntotals: atoms {len(atoms)} sources {len(sources)} rels {len(rels)} annos {len(annos)} passes {len(passes)}")
