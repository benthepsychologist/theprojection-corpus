#!/usr/bin/env python3
"""Step 1c (F0): apply entity-crosswalk.yaml. Additive, not destructive --
facet atoms keep their own meta.entity_slug UNCHANGED (that's the key
filters/cut-core-buildout.yaml already matches against; rewriting it would
silently drop members whose canonical differs from their facet slug, e.g.
amazon -> amazon-aws). Creates one new canonical entity atom per crosswalk
entry, links every existing facet atom to its canonical via part_of.
Idempotent: guarded on canonical atom ids existing already.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
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

crosswalk = yaml.safe_load(open(os.path.join(GRAPH, "schemas", "entity-crosswalk.yaml")))["canonical"]
atoms = read("atoms.jsonl")
rels = read("relationships.jsonl")
atom_ids = {a.get("knowledge_atom_id") for a in atoms}
rel_ids = {r["relationship_id"] for r in rels}

# facet atoms by their OWN (unchanged) entity_slug, for part_of linking
facet_by_slug = {}
for a in atoms:
    if a.get("atom_type") == "entity" and a.get("meta", {}).get("entity_slug") and not a["meta"].get("q3_facility"):
        facet_by_slug.setdefault(a["meta"]["entity_slug"], []).append(a)

new_atoms, new_rels = [], []
for canon_slug, info in crosswalk.items():
    cid = "kat-canon-" + canon_slug
    if cid not in atom_ids:
        # Prefer a real facet's own brand capitalization ("CoreWeave") over naively
        # title-casing the slug ("Coreweave") -- found by audit: the first run of
        # this script did the latter for every canonical, producing 25 cosmetically
        # wrong labels the interp-scenario entity-matcher then double-counted as
        # distinct entities. Facets carry q1's original, correctly-cased name.
        brand = canon_slug.replace("-", " ").title()
        for alias in info["aliases"]:
            for facet in facet_by_slug.get(alias, []):
                fb = facet["label"].split(" (")[0]
                if fb.lower() == brand.lower():
                    brand = fb; break
        c = base("knowledge_atom", "knowledge_atom_id", cid, brand)
        c.update({"atom_type": "entity", "label": c["name"], "aliases": sorted(set(info["aliases"])),
                  "meta": {"entity_slug": canon_slug, "canonical": True,
                           "reconciled_from": info["sources"], "origin": "graph/ingest/01_entity_apply.py, 2026-08-27"},
                  "formalization_stage": "S2", "lifecycle_status": "active", "sources": []})
        new_atoms.append(c)
        atom_ids.add(cid)
    cref = f"knowledge_atom:{cid}"
    # link every facet atom that carries any alias of this canonical
    for alias in info["aliases"]:
        for facet in facet_by_slug.get(alias, []):
            fref = f"knowledge_atom:{facet['knowledge_atom_id']}"
            if fref == cref:
                continue
            rid = rel_id(fref, "part_of", cref)
            if rid not in rel_ids:
                r = base("relationship", "relationship_id", rid, rel_name(fref, "part_of", cref))
                r.update({"source_ref": fref, "target_ref": cref, "predicate_id": "part_of",
                          "review_status": "reviewed",
                          "note": "q1 activity facet -> canonical entity, entity reconciliation step 1."})
                new_rels.append(r); rel_ids.add(rid)

write("atoms.jsonl", atoms + new_atoms)
write("relationships.jsonl", rels + new_rels)
print(f"{len(new_atoms)} canonical entity atoms created; {len(new_rels)} part_of links added")
