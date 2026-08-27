#!/usr/bin/env python3
"""Align the graph to cloud-governor's reg-02 rulings (akm-extension-design.md,
DRAFT 2026-08-27). Idempotent; run once, safe to re-run.

Two rulings change shapes already in this graph:
1. Quantities are an INLINE cluster on knowledge_atom, not a trait and not
   meta -- move meta.quantity{,_unit,_lower,_upper,_basis} to top-level.
2. extraction_pass@1.1.0 carries source_target_refs (required array) and
   DROPS source_target_ref -- convert every singular ref to a one-item list.
   (Our own round-three anyOf shape was refused: anyOf is a forbidden keyword
   in the registrar profile. Versioning handles 1.0.0 compatibility instead.)

One ruling confirms what we had: coverage_state stays in meta. No change.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
Q = ("quantity", "quantity_unit", "quantity_lower", "quantity_upper", "quantity_basis")

def rw(fname, fn):
    p = os.path.join(HERE, fname); rows = [json.loads(l) for l in open(p) if l.strip()]
    n = sum(fn(r) for r in rows)
    with open(p, "w") as f:
        for r in rows: f.write(json.dumps(r, sort_keys=True) + "\n")
    return n

def hoist_quantity(a):
    m = a.get("meta", {}); moved = False
    for k in Q:
        if k in m: a[k] = m.pop(k); moved = True
    return moved

def listify_target(p):
    if "source_target_ref" in p:
        p["source_target_refs"] = [p.pop("source_target_ref")]; return True
    return False

print(f"quantity hoisted on {rw('atoms.jsonl', hoist_quantity)} atoms")
print(f"source_target_ref -> refs on {rw('extraction_passes.jsonl', listify_target)} passes")
