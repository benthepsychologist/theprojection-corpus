#!/usr/bin/env python3
"""One-time fix for 7 id-collision bugs in the original build_graph.py seed,
found by validate.py during entity reconciliation (pre-existing, not caused
by it). Two root causes, both from `slug(...)[:N]` truncation in the
original script:

1. FUNDS DUPLICATES (3 groups -> 3 merged rows): `funds` was keyed only by
   (from, to). Three entity pairs have MORE THAN ONE real financing between
   them (TSMC<->TSMC-foundry: 3 deals; Amazon->Anthropic: 2; SoftBank bond
   market: 2), so the same relationship_id got appended repeatedly. Correct
   shape per P-01: one `funds` row per pair, but its qualifiers become
   LIST-valued when more than one claim materializes it -- never silently
   pick one and drop the rest.

2. TWO SOURCE IDS COLLIDED under 80-char truncation (Crusoe's two distinct
   citations for its two observations), and TWO ANNOTATION IDS collided
   under 70-char truncation (Crusoe again, obs0 vs obs1; and nVent's obs0/
   obs1, which correctly SHARE one real source -- same press release covers
   both the base price and the earnout -- so only the annotation_id needed
   fixing there, not source_ref). Both pairings are unambiguous by
   target_ref order (obs0 first, obs1 second) -- verified by hand against
   the actual quotes before writing this, not inferred generically.

Idempotent: checked via validate.py after running; safe to inspect, not
designed for repeated re-runs against already-fixed data (there is nothing
left to fix the second time, so re-running would be a no-op by construction
of the explicit id checks below, but this is a one-time repair, not a
standing ingester).
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)

def read(fname):
    return [json.loads(l) for l in open(os.path.join(GRAPH, fname)) if l.strip()]
def write(fname, rows):
    with open(os.path.join(GRAPH, fname), "w") as f:
        for r in rows: f.write(json.dumps(r, sort_keys=True) + "\n")

# ---------- 1. merge the 3 duplicate `funds` groups ----------
rels = read("relationships.jsonl")
groups = {}
order = []
non_funds = []
for r in rels:
    if r["predicate_id"] != "funds":
        non_funds.append(r)
        continue
    rid = r["relationship_id"]
    if rid not in groups:
        order.append(rid)
    groups.setdefault(rid, []).append(r)

merged = []
for rid in order:
    g = groups[rid]
    if len(g) == 1:
        merged.append(g[0]); continue
    base = dict(g[0])
    base["qualifiers"] = {
        "materialized_from_claim_refs": sorted({x["qualifiers"]["materialized_from_claim_ref"] for x in g}),
        "q1_edge_ids": sorted({x["qualifiers"]["q1_edge_id"] for x in g}),
    }
    base["note"] = f"Merged {len(g)} funds rows during entity-reconciliation cleanup (2026-08-27) " \
                    f"-- this entity pair has {len(g)} distinct financings; P-01 says list them."
    merged.append(base)
    print(f"funds: merged {len(g)} rows -> 1 for {rid}")

write("relationships.jsonl", non_funds + merged)

# ---------- 2a. Crusoe source_id collision: obs1's citation gets a real id ----------
sources = read("sources.jsonl")
OLD_SID = "src-crusoe-2025-abilene-phase2-financing-crusoe-datacenter-construction-2025-phase2-"
NEW_SID = "src-crusoe-2025-abilene-phase2-financing-crusoe-datacenter-construction-2025-phase2-obs1"
dupes = [s for s in sources if s["source_id"] == OLD_SID]
assert len(dupes) == 2, f"expected exactly 2, found {len(dupes)} -- data has changed, re-check by hand"
# obs0's source (rcrwireless, "$11.6B additional") keeps OLD_SID; obs1's (globenewswire, "$15B cumulative") gets NEW_SID
obs1_source = next(s for s in dupes if "globenewswire" in s.get("locator", ""))
obs1_source["source_id"] = NEW_SID
sources = [s for s in sources if not (s["source_id"] == OLD_SID and s is not dupes[0] and s.get("locator") == dupes[0].get("locator"))]
# rebuild cleanly: keep the rcrwireless one at OLD_SID, the globenewswire one now at NEW_SID
fixed_sources = []
seen_old = False
for s in sources:
    if s["source_id"] == OLD_SID and "rcrwireless" not in s.get("locator", "") and s is not obs1_source:
        continue  # shouldn't happen, safety net
    fixed_sources.append(s)
write("sources.jsonl", fixed_sources)
print(f"sources: {NEW_SID.split('src-')[1][:20]}... disambiguated from the shared id")

# repoint everything that cited the source under the old id but meant obs1's claim
CRUSOE_OBS1_CLAIM = "knowledge_atom:kat-claim-crusoe-2025-abilene-phase2-financing-crusoe-datacenter-construction-2025-phase2-obs1"
atoms = read("atoms.jsonl")
for a in atoms:
    if a.get("knowledge_atom_id") == CRUSOE_OBS1_CLAIM.split(":", 1)[1]:
        a["sources"] = [NEW_SID if s == OLD_SID else s for s in a.get("sources", [])]
write("atoms.jsonl", atoms)

rels = read("relationships.jsonl")
for r in rels:
    if r["predicate_id"] == "supports" and r["target_ref"] == CRUSOE_OBS1_CLAIM and r["source_ref"] == f"source:{OLD_SID}":
        r["source_ref"] = f"source:{NEW_SID}"
write("relationships.jsonl", rels)

annos = read("annotations.jsonl")
for an in annos:
    if an["target_ref"] == CRUSOE_OBS1_CLAIM and an["source_ref"] == f"source:{OLD_SID}":
        an["source_ref"] = f"source:{NEW_SID}"
write("annotations.jsonl", annos)
print("repointed obs1's claim.sources[], supports relationship, and annotation to the new source id")

# ---------- 2b. two annotation_id collisions: pure rename, obs1 gets a suffix ----------
annos = read("annotations.jsonl")
RENAME_TARGETS = {
    "ann-crusoe-2025-abilene-phase2-financing-crusoe-datacenter-construction-20":
        "knowledge_atom:" + CRUSOE_OBS1_CLAIM.split(":", 1)[1],
    "ann-nvent-capital-maverick-power-power-distribution-manufacturing-2026-acq":
        "knowledge_atom:kat-claim-nvent-capital-maverick-power-power-distribution-manufacturing-2026-acquisition-obs1",
}
renamed = 0
for an in annos:
    base_id = an["annotation_id"]
    if base_id in RENAME_TARGETS and an["target_ref"] == RENAME_TARGETS[base_id]:
        an["annotation_id"] = base_id + "-obs1"
        renamed += 1
write("annotations.jsonl", annos)
print(f"annotations: renamed {renamed} obs1-side id(s) to disambiguate")
