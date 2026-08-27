#!/usr/bin/env python3
"""graph/validate.py -- referential integrity, not schema conformance (per
graph/DESIGN.md §8 intro: "we're copiers without the registrar"). Checks:
  - every JSONL file parses
  - no duplicate ids within a kind
  - every relationship's source_ref/target_ref resolves to an atom or source
    that actually exists
  - every annotation's target_ref/generated_by_ref/source_ref resolves
  - every claim's `sources` list entries exist in sources.jsonl
Exit 0 and silent on success; exit 1 with every violation listed on failure.
Run after any ingester; wire into CI/pre-commit later if it earns it.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def read(fname):
    path = os.path.join(HERE, fname)
    rows = []
    for i, line in enumerate(open(path)):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as e:
            errors.append(f"{fname}:{i+1} invalid JSON: {e}")
    return rows

errors = []
atoms = read("atoms.jsonl")
sources = read("sources.jsonl")
rels = read("relationships.jsonl")
annos = read("annotations.jsonl")
passes = read("extraction_passes.jsonl")

atom_ids = {a["knowledge_atom_id"] for a in atoms if "knowledge_atom_id" in a}
source_ids = {s["source_id"] for s in sources if "source_id" in s}
rel_ids_seen = {}
ann_ids_seen = {}
pass_ids_seen = {}

def ref_exists(ref):
    if not isinstance(ref, str) or ":" not in ref:
        return False
    kind, rid = ref.split(":", 1)
    return (kind == "knowledge_atom" and rid in atom_ids) or (kind == "source" and rid in source_ids)

for a in atoms:
    aid = a.get("knowledge_atom_id")
    if aid in [x for x in atom_ids if False]:  # placeholder, real dup check below
        pass
seen_atom = set()
for a in atoms:
    aid = a.get("knowledge_atom_id")
    if aid in seen_atom:
        errors.append(f"atoms.jsonl: duplicate knowledge_atom_id {aid}")
    seen_atom.add(aid)
    for sid in a.get("sources", []):
        if sid not in source_ids:
            errors.append(f"atom {aid}: sources[] references missing source_id {sid}")

seen_src = set()
for s in sources:
    sid = s.get("source_id")
    if sid in seen_src:
        errors.append(f"sources.jsonl: duplicate source_id {sid}")
    seen_src.add(sid)

for r in rels:
    rid = r.get("relationship_id")
    if rid in rel_ids_seen:
        errors.append(f"relationships.jsonl: duplicate relationship_id {rid}")
    rel_ids_seen[rid] = True
    if not ref_exists(r.get("source_ref")):
        errors.append(f"relationship {rid}: source_ref {r.get('source_ref')} does not resolve")
    if not ref_exists(r.get("target_ref")):
        errors.append(f"relationship {rid}: target_ref {r.get('target_ref')} does not resolve")

pass_ids = {p.get("extraction_pass_id") for p in passes}
for a in annos:
    aid = a.get("annotation_id")
    if aid in ann_ids_seen:
        errors.append(f"annotations.jsonl: duplicate annotation_id {aid}")
    ann_ids_seen[aid] = True
    if not ref_exists(a.get("target_ref")):
        errors.append(f"annotation {aid}: target_ref {a.get('target_ref')} does not resolve")
    gen = a.get("generated_by_ref", "")
    if gen and gen.split(":", 1)[-1] not in pass_ids:
        errors.append(f"annotation {aid}: generated_by_ref {gen} does not resolve to an extraction_pass")
    if a.get("source_ref") and not ref_exists(a["source_ref"]):
        errors.append(f"annotation {aid}: source_ref {a['source_ref']} does not resolve")

for p in passes:
    pid = p.get("extraction_pass_id")
    if pid in pass_ids_seen:
        errors.append(f"extraction_passes.jsonl: duplicate extraction_pass_id {pid}")
    pass_ids_seen[pid] = True
    refs = p.get("source_target_refs") or ([p["source_target_ref"]] if p.get("source_target_ref") else [])
    for ref in refs:
        if ref not in ("source:unspecified-historical", "source:unspecified-resolution-prose") and not ref_exists(ref):
            errors.append(f"extraction_pass {pid}: source_target_refs entry {ref} does not resolve")

if errors:
    print(f"FAIL: {len(errors)} referential-integrity violation(s)")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK: {len(atoms)} atoms, {len(sources)} sources, {len(rels)} relationships, "
      f"{len(annos)} annotations, {len(passes)} extraction_passes -- all references resolve, no duplicate ids.")
