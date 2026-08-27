#!/usr/bin/env python3
"""Exercises the holds/held_by predicate gap (graph/DESIGN.md §6, §12.2)
with real data before filing the round-four brief -- board.yaml's 14
`held_by` org->person fields, both already canonical entity atoms.
`holdings` (org -> internal product-brand strings like "gemini"/"azure",
not other tracked entities) is a different, bigger question -- not
ingested here, not this gap.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"

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
rel_ids = {r["relationship_id"] for r in rels}
entity_by_slug = {a["meta"]["entity_slug"]: a for a in atoms
                  if a.get("atom_type") == "entity" and a.get("meta", {}).get("entity_slug")}

board = yaml.safe_load(open(os.path.join(REPO, "attention", "board.yaml")))
new_rels, no_match = [], []
for o in board.get("orgs", []):
    held_by = o.get("held_by")
    if not held_by:
        continue
    org = entity_by_slug.get(o["slug"])
    person = entity_by_slug.get(held_by)
    if not org or not person:
        no_match.append((o["slug"], held_by))
        continue
    oref, pref = f"knowledge_atom:{org['knowledge_atom_id']}", f"knowledge_atom:{person['knowledge_atom_id']}"
    rid = rel_id(oref, "related_to", pref)
    if rid in rel_ids:
        continue
    r = base("relationship", "relationship_id", rid, rel_name(oref, "related_to", pref))
    r.update({"source_ref": oref, "target_ref": pref, "predicate_id": "related_to",
              "qualifiers": {"role": "held_by"}, "review_status": "unreviewed",
              "note": "GAP: no landed holds/held_by predicate; related_to+role is the least-wrong "
                      "landed shape, same stopgap as q3's operates/owns/leases (graph/DESIGN.md §6)."})
    new_rels.append(r); rel_ids.add(rid)

write("relationships.jsonl", rels + new_rels)
print(f"{len(new_rels)} held_by relationship(s) added; {len(no_match)} skipped (no matching entity): {no_match}")
