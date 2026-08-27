#!/usr/bin/env python3
"""Parity check: does the graph assert the same facts as the current, live
site output at theprojection-site/data/claims.json (bundle-direct, written
by `kestrel publish --instance .` calling publish/adapter.py::build_claims())?
Read-only, writes nothing. Run any time -- not gated on /daily or /week,
just on both data sources being present. Re-run `kestrel publish --instance .`
first if you want this checked against a fresher bundle-direct snapshot;
this script only reads whatever claims.json already contains.

PARITY, DEFINED (so the comparison logic below isn't ad hoc):
For every (subject, dimension) pair claims.json carries as a NON-aggregate
claim, the graph's ACTIVE (lifecycle_status != deprecated) claim for that
same pair must carry the same value, the same basis, the same confidence
band, and the same set of source URLs. A mismatch on any of those four is
a real bug. Everything else is expected structural divergence, not a
failure:
  - subject shape (bare board slug vs. graph's canonical entity id)
  - source SHAPE (bundle: flat sources[] list; graph: exploded into
    separate source atoms + supports relationships) -- only the URL SET
    is compared, not the container shape, and a GitHub blob URL vs. the
    same file's repo-relative path is normalized to one form first
  - basis vs. body/summary duplication: the bundle leaves `basis` empty
    for every non-posture dimension (its narrative lives in `value`
    alone); 04_bundle_claims.py mirrors that single narrative into both
    the graph claim's body and summary, so an empty bundle basis is
    never compared against the graph's summary
  - history: the graph may hold deprecated predecessors via `supersedes`;
    only the active claim is compared
  - aggregate claims (pocket/sector rollups): claims.json computes these
    by counting members; the graph has no equivalent yet (a deliberate
    step-4 scope decision, not a gap found here) -- excluded from
    comparison entirely, reported separately as "not yet covered."
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SITE_CLAIMS = os.path.join(os.path.dirname(REPO), "theprojection-site", "data", "claims.json")

CONF_BAND = {"high": "strong", "med": "moderate", "low": "weak"}

def read(fname):
    p = os.path.join(HERE, fname)
    return [json.loads(l) for l in open(p) if l.strip()]

atoms = read("atoms.jsonl")
sources = read("sources.jsonl")
rels = read("relationships.jsonl")
source_by_id = {s["source_id"]: s for s in sources}

# ---- side A: the real, already-published site output (bundle-direct) ----
if not os.path.exists(SITE_CLAIMS):
    sys.exit(f"missing {SITE_CLAIMS} -- run `kestrel publish --instance .` from {REPO} first")
site_claims_all = json.load(open(SITE_CLAIMS))
bundle_claims = {(c["subject"], c["dimension"]): c for c in site_claims_all if not c.get("aggregate")}
aggregate_count = sum(1 for c in site_claims_all if c.get("aggregate"))

# ---- side B: the graph's active bundle-sourced claims ----
graph_claims = {}
for a in atoms:
    if a.get("atom_type") != "claim" or "bundle_node" not in a.get("meta", {}):
        continue
    if a.get("lifecycle_status") == "deprecated":
        continue
    key = (a["meta"]["bundle_node"], a["meta"]["dimension"])
    graph_claims[key] = a

# reconstruct each graph claim's source URL set via its own `sources` list
GITHUB_BLOB_PREFIX = "https://github.com/benthepsychologist/theprojection-corpus/blob/main/"

def normalize_url(u):
    # in-repo file citations render as full GitHub blob URLs on the bundle
    # side but as repo-relative paths in the graph's source locator -- same
    # underlying file, different rendering, not a real divergence.
    return u[len(GITHUB_BLOB_PREFIX):] if u.startswith(GITHUB_BLOB_PREFIX) else u

def graph_source_urls(claim):
    urls = set()
    for sid in claim.get("sources", []):
        s = source_by_id.get(sid)
        if s and s.get("locator"):
            urls.add(normalize_url(s["locator"]))
    return urls

def bundle_source_urls(claim):
    return {normalize_url(s["url"]) for s in claim.get("sources", []) if s.get("url")}

both_keys = set(bundle_claims) & set(graph_claims)
only_bundle = set(bundle_claims) - set(graph_claims)
only_graph = set(graph_claims) - set(bundle_claims)

mismatches = []
matched = 0
for key in sorted(both_keys):
    b, g = bundle_claims[key], graph_claims[key]
    b_val = " ".join(str(b.get("value", "")).split())
    g_val = " ".join(str(g.get("body", "")).split())
    b_basis = " ".join(str(b.get("basis", "")).split())
    g_basis = " ".join(str(g.get("summary", "")).split())
    b_conf = b.get("confidence") or None
    g_conf_band = None
    # graph doesn't store the bundle's own high/med/low; derive from evidence_weight bands seen on its supports edges
    my_supports_bands = {r.get("evidence_strength_band") for r in rels
                          if r["predicate_id"] == "supports" and r["target_ref"] == f"knowledge_atom:{g['knowledge_atom_id']}"}
    b_conf_band = CONF_BAND.get(b_conf)
    b_urls, g_urls = bundle_source_urls(b), graph_source_urls(g)

    problems = []
    if b_val != g_val:
        problems.append(f"value differs:\n      bundle: {b_val[:150]}\n      graph:  {g_val[:150]}")
    # 04_bundle_claims.py duplicates the bundle's `value` into both the
    # graph's body and summary when the bundle itself leaves `basis` empty
    # (true for every non-posture dimension) -- not a divergence to flag.
    if b_basis and b_basis != g_basis:
        problems.append(f"basis differs:\n      bundle: {b_basis[:150]}\n      graph:  {g_basis[:150]}")
    if b_conf_band and b_conf_band not in my_supports_bands:
        problems.append(f"confidence band mismatch: bundle top confidence={b_conf}->{b_conf_band}, "
                         f"graph supports bands={my_supports_bands}")
    if b_urls != g_urls:
        problems.append(f"source URL set differs: bundle-only={b_urls - g_urls}, graph-only={g_urls - b_urls}")

    if problems:
        mismatches.append((key, problems))
    else:
        matched += 1

print(f"PARITY CHECK — build_claims() (bundle-direct) vs graph (step 4)\n")
print(f"  {len(bundle_claims)} non-aggregate bundle claims, {aggregate_count} aggregate claims "
      f"(excluded from comparison — no graph equivalent yet, by design)")
print(f"  {len(graph_claims)} active graph bundle-claims")
print(f"  {len(both_keys)} pairs present in both — {matched} match, {len(mismatches)} mismatch")
print(f"  {len(only_bundle)} pair(s) in bundle-direct only (missing from graph): {sorted(only_bundle)[:10]}")
print(f"  {len(only_graph)} pair(s) in graph only (no longer in bundle-direct — stale?): {sorted(only_graph)[:10]}")

if mismatches:
    print(f"\n--- {len(mismatches)} MISMATCH(ES) ---")
    for key, problems in mismatches:
        print(f"\n{key[0]}--{key[1]}:")
        for p in problems:
            print(f"    {p}")
    sys.exit(1)
else:
    print("\nNo mismatches. Parity holds for every claim present in both.")
