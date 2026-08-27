#!/usr/bin/env python3
"""Step 1a (F0): extract every entity/person candidate slug+name from the four
sources that disagree, with provenance. Writes graph/schemas/entity-candidates.json
for the clustering step (01b) to consume. Reads only; writes nothing to graph/*.jsonl.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)

def slug(s): return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")

candidates = []  # {slug, name, source, kind, provenance}

# ---- 1. board.yaml orgs + houses ----
board = yaml.safe_load(open(os.path.join(REPO, "attention", "board.yaml")))
for o in board.get("orgs", []):
    candidates.append({"slug": o["slug"], "name": o["slug"].replace("-", " ").title(),
                        "source": "board.orgs", "kind": "org",
                        "provenance": f"board.yaml orgs, rank={o.get('rank')}, pocket={o.get('pocket')}"})
for h in board.get("houses", []):
    candidates.append({"slug": h["slug"], "name": h.get("name", h["slug"]),
                        "source": "board.houses", "kind": "person",
                        "provenance": "board.yaml houses"})

# ---- 2. watchlist.yaml orgs + people, all 3 lenses ----
wl = yaml.safe_load(open(os.path.join(REPO, "attention", "watchlist.yaml")))
for lens, cats in wl.get("lenses", {}).items():
    for kind_key, kind in (("orgs", "org"), ("people", "person")):
        for item in cats.get(kind_key, []) or []:
            if isinstance(item, str):
                candidates.append({"slug": slug(item), "name": item, "source": f"watchlist.{lens}.{kind_key}",
                                    "kind": kind, "provenance": f"watchlist.yaml lens={lens}"})
            else:
                candidates.append({"slug": item.get("entity", slug(item.get("term", ""))),
                                    "name": item.get("name", item.get("term")),
                                    "source": f"watchlist.{lens}.{kind_key}", "kind": kind,
                                    "provenance": f"watchlist.yaml lens={lens}, term={item.get('term')}"})

# ---- 3. q1 graph facet entities (already-migrated atoms) ----
for l in open(os.path.join(GRAPH, "atoms.jsonl")):
    a = json.loads(l)
    if a.get("atom_type") != "entity":
        continue
    m = a.get("meta", {})
    q1id = m.get("q1_node_id", "")
    if m.get("q3_facility"):
        continue  # facilities are not org/person entities -- out of scope for this reconciliation
    bare = q1id.split("/")[0] if "/" in q1id else q1id
    candidates.append({"slug": slug(bare), "name": a["label"].split(" (")[0],
                        "source": "graph.q1_facet", "kind": "org",
                        "provenance": f"graph atom {a['knowledge_atom_id']} (facet: {m.get('activity') or m.get('round_type')})",
                        "facet_atom_id": a["knowledge_atom_id"], "facet_q1_id": q1id})

# ---- dedupe within-source exact slug matches, keep all provenance ----
by_slug_source = {}
for c in candidates:
    key = (c["slug"], c["source"])
    by_slug_source.setdefault(key, c)
candidates = list(by_slug_source.values())

with open(os.path.join(GRAPH, "schemas", "entity-candidates.json"), "w") as f:
    json.dump(candidates, f, indent=1)

print(f"{len(candidates)} candidates extracted")
from collections import Counter
print(Counter(c["source"] for c in candidates))
