#!/usr/bin/env python3
"""Export the Q1 money-flow map (graph/DESIGN.md's "worked graduation" case)
into a Hugo data file the site can actually render, replacing the hand-typed
prose that used to live at theprojection-site/content/research/q1.md.

Scope: every entity atom carrying `meta.q1_node_id` (the q1-flows facets --
e.g. "tsmc/capital") plus every `funds` relationship where at least one end
is in that set. This is a graph EXPORT, not a re-derivation: every number
here already exists in graph/atoms.jsonl, written by graph/ingest/01 and
graph/ingest/04 (and predecessors) from the frozen research/q1-flows YAML.

Layout: a simple layered (Sugiyama-style) DAG placement computed here in
Python and written as fixed x/y into the JSON, so the client only ever
draws what it's given -- no physics simulation, no client-side layout
library, consistent with this site's existing hand-rolled-SVG pattern
(static/js/map.js, layouts/map/list.html's board plate). Layer = longest
path from a source node (an entity with no incoming `funds` edge in scope);
a `funds` edge that would close a cycle is dropped from layering only (kept
in the data) and noted in `dropped_for_layering`.

Run any time; writes only theprojection-site/data/q1-flows.json. Re-run
after any graph ingest step that touches q1 entities/funds edges, or wire
into /week alongside the other graph refresh steps once this earns a place
in the standing cadence (see graph/DESIGN.md ROADMAP -- not decided yet).
"""
import json, os, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SITE = os.path.join(os.path.dirname(REPO), "theprojection-site")
# underscore, not hyphen: Hugo data files become .Site.Data.<name> by dot
# access, and a hyphen isn't a valid bare identifier in that path.
OUT = os.path.join(SITE, "data", "q1_flows.json")

LAYER_DX, ROW_DY = 280, 30


def read(fname):
    p = os.path.join(HERE, fname)
    return [json.loads(l) for l in open(p) if l.strip()]


atoms = read("atoms.jsonl")
rels = read("relationships.jsonl")
sources = read("sources.jsonl")
atom_by_id = {a["knowledge_atom_id"]: a for a in atoms if "knowledge_atom_id" in a}
source_by_id = {s["source_id"]: s for s in sources}

cut = yaml.safe_load(open(os.path.join(REPO, "research/q1-flows/filters/cut-core-buildout.yaml")))
CORE_BUILDOUT = set(cut["members"])


def strip(ref):
    return ref.split(":", 1)[1] if isinstance(ref, str) and ":" in ref else ref


# ---- nodes: every entity carrying a q1_node_id ----
q1_entities = {a["knowledge_atom_id"]: a for a in atoms
               if a.get("atom_type") == "entity" and "q1_node_id" in a.get("meta", {})}

part_of = {r["source_ref"]: r["target_ref"] for r in rels if r["predicate_id"] == "part_of"}


def canonical_label(aid):
    canon_ref = part_of.get(f"knowledge_atom:{aid}")
    if canon_ref:
        canon = atom_by_id.get(strip(canon_ref))
        if canon:
            return canon.get("label", canon.get("name"))
    return q1_entities[aid].get("label", q1_entities[aid].get("name"))


nodes = {}
for aid, a in q1_entities.items():
    meta = a.get("meta", {})
    slug = meta.get("entity_slug", "")
    nodes[aid] = {
        "id": aid,
        "q1_node_id": meta.get("q1_node_id"),
        "entity_slug": slug,
        "activity": meta.get("activity", ""),
        "canonical_label": canonical_label(aid),
        "core_buildout": slug in CORE_BUILDOUT,
        "atom_type": "entity",
    }

# ---- edges: funds relationships with at least one end in scope ----
def claim_refs(qualifiers):
    if "materialized_from_claim_refs" in qualifiers:
        return qualifiers["materialized_from_claim_refs"]
    if "materialized_from_claim_ref" in qualifiers:
        return [qualifiers["materialized_from_claim_ref"]]
    return []


def flow_from_claim(claim_ref):
    c = atom_by_id.get(strip(claim_ref))
    if not c:
        return None
    urls = []
    for sid in c.get("sources", []):
        s = source_by_id.get(sid)
        if s and s.get("locator"):
            urls.append(s["locator"])
    return {
        "claim_id": c["knowledge_atom_id"],
        "amount": c.get("quantity"),
        "unit": c.get("quantity_unit"),
        "basis": c.get("quantity_basis"),
        "flow_type": c.get("meta", {}).get("flow_type"),
        "destination_category": c.get("meta", {}).get("destination_category"),
        "date": c.get("valid_from"),
        "summary": c.get("summary", c.get("body", "")),
        "source_urls": urls,
    }


edges = []
added_external = {}  # id -> node dict, for funds endpoints outside the q1_node_id set

def ensure_node(aid):
    if aid in nodes or aid in added_external:
        return
    a = atom_by_id.get(aid)
    if not a:
        return
    meta = a.get("meta", {})
    added_external[aid] = {
        "id": aid,
        "q1_node_id": None,
        "entity_slug": meta.get("entity_slug", ""),
        "activity": meta.get("activity", ""),
        "canonical_label": a.get("label", a.get("name")),
        "core_buildout": meta.get("entity_slug", "") in CORE_BUILDOUT,
        "atom_type": a.get("atom_type"),
        "external": True,
    }

event_ids = {a["knowledge_atom_id"] for a in atoms if a.get("atom_type") == "event"}

# a financing round has no per-investor dollar split of its own -- the
# round's total lives on the event->company `funds` claim below. A
# member_of edge into an event is still a real money-flow leg (investor
# money into the round), just one whose amount isn't broken out here.
for r in rels:
    is_funds = r["predicate_id"] == "funds"
    is_round_membership = r["predicate_id"] == "member_of" and strip(r["target_ref"]) in event_ids
    if not (is_funds or is_round_membership):
        continue
    src, tgt = strip(r["source_ref"]), strip(r["target_ref"])
    if src not in q1_entities and tgt not in q1_entities and src not in event_ids and tgt not in event_ids:
        continue
    ensure_node(src)
    ensure_node(tgt)
    flows = [f for f in (flow_from_claim(cr) for cr in claim_refs(r.get("qualifiers", {}))) if f]
    total = sum(f["amount"] for f in flows if f.get("amount") and f.get("basis") == "point")
    edges.append({
        "id": r["relationship_id"],
        "source": src,
        "target": tgt,
        "role": r.get("qualifiers", {}).get("role") if is_round_membership else None,
        "total_amount": total or None,
        "unit": next((f["unit"] for f in flows if f.get("unit")), "USD"),
        "flows": flows,
        "note": r.get("note"),
    })

nodes.update(added_external)

# ---- layered layout (longest-path-from-source; cycle back-edges dropped) ----
adj = {aid: [] for aid in nodes}
indeg = {aid: 0 for aid in nodes}
for e in edges:
    adj[e["source"]].append(e["target"])
    indeg[e["target"]] += 1

layer = {aid: 0 for aid in nodes}
dropped = []

# DFS topo sort; a back-edge into an in-progress node means a funding cycle
# -- ignore it for topo order (nodes still get SOME layer), drop it from
# layering below, but keep it in `edges` untouched.
temp_mark, perm_mark, topo = set(), set(), []


def visit(n):
    if n in perm_mark or n in temp_mark:
        return
    temp_mark.add(n)
    for m in adj.get(n, []):
        visit(m)
    temp_mark.discard(n)
    perm_mark.add(n)
    topo.append(n)


for n in nodes:
    visit(n)
topo.reverse()  # sources first
topo_rank = {n: i for i, n in enumerate(topo)}

safe_edges = []
for e in edges:
    if topo_rank[e["source"]] < topo_rank[e["target"]]:
        safe_edges.append(e)
    else:
        dropped.append((e["source"], e["target"]))

for n in topo:
    for e in safe_edges:
        if e["source"] == n:
            layer[e["target"]] = max(layer[e["target"]], layer[n] + 1)

by_layer = {}
for aid, l in layer.items():
    by_layer.setdefault(l, []).append(aid)
for l, ids in by_layer.items():
    ids.sort(key=lambda a: nodes[a]["canonical_label"] or "")
    for i, aid in enumerate(ids):
        nodes[aid]["layer"] = l
        nodes[aid]["x"] = l * LAYER_DX
        nodes[aid]["y"] = i * ROW_DY

out = {
    "generated_by": "graph/export_q1.py",
    "node_count": len(nodes),
    "edge_count": len(edges),
    "layer_count": (max(by_layer) + 1) if by_layer else 0,
    "cut_core_buildout_version": cut["version"],
    "dropped_for_layering": [{"from": a, "to": b} for a, b in dropped],
    "nodes": list(nodes.values()),
    "edges": edges,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(out, f, indent=1, sort_keys=True)
print(f"{len(nodes)} nodes, {len(edges)} edges, {out['layer_count']} layers, "
      f"{len(dropped)} edge(s) dropped for layering (cycle back-edges) -> {OUT}")
