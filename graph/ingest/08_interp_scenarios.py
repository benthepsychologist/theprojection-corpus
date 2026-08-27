#!/usr/bin/env python3
"""Step 8 (F0): *.interp.yaml scenarios -> hypothesis claims (graph/DESIGN.md
§8.8). Ruled propositions (Ben, 2026-08-27): direction=body, why=defeat
conditions, precedent=meta. mechanism/context_note are frames -- NOT
ingested; the file stays composition, already keyed on the bibliography
entry (its own top-level key = the parent S1 claim's dedupe id).

RUN BEFORE STEP 7 (out of the design's own stated order, by necessity of
scheduling): `about` still links to real entities matched by name (already
possible -- entities predate digests). `meta.interprets` is a forward
reference (a plain string, not a graph relationship) to the parent claim's
id, which step 7 hasn't created yet -- validate.py doesn't check meta
strings, only graph refs, so this is safe and gets a real target the
moment step 7 runs with matching ids. Flagged, not silently assumed.
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
ORIGIN = "graph/ingest/08_interp_scenarios.py, 2026-08-27"

def slug(s): return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
def rel_id(s, p, t): return "rel-" + slug(f"{s}:{p}:{t}")
def rel_name(s, p, t):
    b = lambda r: r.split(":", 1)[1]
    return f"{b(s)}:{p}:{b(t)}"
def base(kind, idf, idv, name):
    return {"kind": kind, idf: idv, "version": VER, "name": name, "data_domain": DOMAIN, "sensitivity": SENS}

def read(fname):
    p = os.path.join(GRAPH, fname)
    return [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []
def write(fname, rows):
    with open(os.path.join(GRAPH, fname), "w") as f:
        for r in rows: f.write(json.dumps(r, sort_keys=True) + "\n")

atoms = read("atoms.jsonl")
rels = read("relationships.jsonl")
atom_ids = {a["knowledge_atom_id"] for a in atoms}
rel_ids = {r["relationship_id"] for r in rels}
entity_labels = [(a["label"].split(" (")[0], a) for a in atoms if a.get("atom_type") == "entity"]

def match_entities(*texts):
    p = " ".join(str(t) for t in texts if t).lower()
    hits = []
    for label, a in entity_labels:
        bare = label.lower()
        # word-boundary match, not raw substring -- "balance" must not match "Alan".
        # Found by audit: raw `bare in p` matched "Alan" (a watchlist person) inside
        # "balance sheet" 30 times across the corpus before this fix.
        if len(bare) >= 4 and re.search(r"\b" + re.escape(bare) + r"\b", p):
            hits.append(a)
    by_id = {a["knowledge_atom_id"]: a for a in hits}
    return list(by_id.values())

new_atoms, new_rels = [], []
unmatched_no_entity = 0
for path in sorted(glob.glob(os.path.join(REPO, "artifacts", "digests", "daily", "*.interp.yaml"))):
    day = os.path.basename(path).split("-global-capital")[0]
    entries = yaml.safe_load(open(path)) or {}
    for key, entry in entries.items():
        entities_for_entry = match_entities(entry.get("mechanism"), entry.get("context_note"), key.replace("-", " "))
        for i, sc in enumerate(entry.get("scenarios") or []):
            hid = f"kat-hyp-interp-{slug(key)}-{i}"
            if hid in atom_ids:
                continue
            direction = " ".join(str(sc.get("direction", "")).split())
            why = " ".join(str(sc.get("why", "")).split())
            h = base("knowledge_atom", "knowledge_atom_id", hid, direction[:160])
            h.update({"atom_type": "claim", "label": direction[:160], "summary": direction, "body": direction,
                      "epistemic_status": "hypothesized", "source_process": "inference",
                      "defeat_conditions": why or None,
                      "meta": {k: v for k, v in {
                          "precedent": " ".join(str(sc.get("precedent", "")).split()) or None,
                          "interprets": key,  # forward reference -- resolved once step 7 creates this S1 claim id
                          "interp_file": os.path.basename(path), "digest_day": day,
                          "confidence_label": entry.get("confidence"), "origin": ORIGIN}.items() if v},
                      "formalization_stage": "S4", "lifecycle_status": "active", "sources": []})
            h = {k: v for k, v in h.items() if v is not None}
            new_atoms.append(h); atom_ids.add(hid)
            href = f"knowledge_atom:{hid}"
            if not entities_for_entry:
                unmatched_no_entity += 1
            for e in entities_for_entry:
                eref = f"knowledge_atom:{e['knowledge_atom_id']}"
                rid = rel_id(href, "about", eref)
                if rid not in rel_ids:
                    r = base("relationship", "relationship_id", rid, rel_name(href, "about", eref))
                    r.update({"source_ref": href, "target_ref": eref, "predicate_id": "about",
                              "qualifiers": {"role": "subject"}, "review_status": "unreviewed"})
                    new_rels.append(r); rel_ids.add(rid)

write("atoms.jsonl", atoms + new_atoms)
write("relationships.jsonl", rels + new_rels)
print(f"{len(new_atoms)} interp-scenario hypothesis claim(s) created; "
      f"{len(new_rels)} about-relationships; {unmatched_no_entity} scenario(s) with no matched entity "
      f"(kept as prose-only claims, not blocked)")
