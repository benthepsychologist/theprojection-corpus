#!/usr/bin/env python3
"""One-time repair, not part of the steady-state pipeline (same posture as
00_fix_seed_dedup_bugs.py): 01_entity_apply.py's canonical-label derivation
missed publish/adapter.py's BOARD_ORG_NAMES override table -- the one place
this repo already resolves the "board slug doesn't title-case into its real
display name" problem (TSMC, not "Tsmc"; SpaceXAI, not "Spacex"; The Silk
Road, not "Silk Road"). Board pages have always shown these correctly
because adapter.py consults that table; the graph's own canonical entities
never did, so 19 of them carry a naive title-cased slug as their label.

BOARD_ORG_NAMES is copied here rather than imported -- publish/adapter.py
does `from publish import core`, a module that only exists inside kestrel's
own publish runner (see graph/parity_check.py's docstring for the same
issue), so it can't be imported standalone. Keep this copy in sync by hand
if that table changes; there's no way to make Python enforce it without
adapter.py becoming importable on its own.

Run once. Refuses (via the assert) to run against a graph that doesn't
have exactly the 19 known-bad labels, so it can't silently no-op on a
graph state it wasn't written against, or double-apply.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)

BOARD_ORG_NAMES = {
    "amazon-aws": "Amazon", "meta-ai": "Meta", "alibaba-qwen": "Alibaba",
    "spacex": "SpaceXAI", "microsoft-mai": "Microsoft MAI", "sk-hynix": "SK Hynix",
    "cxmt": "CXMT", "tsmc": "TSMC", "pif": "PIF", "mgx": "MGX", "nuhw": "NUHW",
    "silk-road": "The Silk Road", "united-states": "United States", "china": "China",
    "european-union": "European Union", "united-kingdom": "United Kingdom",
    "france": "France", "uae": "UAE", "saudi-arabia": "Saudi Arabia", "russia": "Russia",
    "us-state-legislatures": "US State Legislatures", "eu-ai-act": "EU AI Act",
    "proposed-sro": "Proposed SRO", "nsa-frontier-review": "NSA Frontier Review",
    "caisi": "CAISI", "fda": "FDA", "dmhc": "DMHC", "mhra": "MHRA",
    "kaiser-permanente": "Kaiser Permanente",
}

path = os.path.join(GRAPH, "atoms.jsonl")
atoms = [json.loads(l) for l in open(path) if l.strip()]

mismatches = [
    a for a in atoms
    if a.get("atom_type") == "entity" and a["knowledge_atom_id"].startswith("kat-canon-")
    and a.get("meta", {}).get("entity_slug") in BOARD_ORG_NAMES
    and a.get("label") != BOARD_ORG_NAMES[a["meta"]["entity_slug"]]
]
assert len(mismatches) == 19, (
    f"expected exactly 19 known-bad labels, found {len(mismatches)} -- "
    "this script has already run, or the graph changed underneath it; "
    "check by hand before re-running"
)

for a in mismatches:
    correct = BOARD_ORG_NAMES[a["meta"]["entity_slug"]]
    a["label"] = correct
    a["name"] = correct

with open(path, "w") as f:
    for a in atoms:
        f.write(json.dumps(a, sort_keys=True) + "\n")

print(f"fixed {len(mismatches)} canonical entity label(s): "
      + ", ".join(f"{a['meta']['entity_slug']}→{a['label']}" for a in mismatches))
