#!/usr/bin/env python3
"""Step 1b (F0): cluster entity-candidates.json into proposed canonical entities.
Precedence per graph/DESIGN.md §8.1: board slug (on the board) > watchlist slug >
q1 bare-entity slug. Confident clusters (exact or suffix-stripped match, single
source-of-truth per cluster) are written straight to entity-crosswalk.yaml.
Ambiguous clusters (a q1 facet slug with no board/watchlist match at all -- i.e.
genuinely new to the canonical layer, not a collision) still get a canonical
entity, just via q1 precedence -- true AMBIGUITY only means: two candidates
normalize to the same key but disagree on which is authoritative, or a name
looks like it might refer to two different real-world things. Writes both files;
prints the ambiguous set for review.
"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)

SUFFIXES = ["-aws", "-ai", "-inc", "-corp", "-corporation", "-group", "-systems",
            "-technologies", "-energy", "-capital", "-holdings"]

def normalize(slug):
    s = slug
    for suf in SUFFIXES:
        if s.endswith(suf) and s != suf.lstrip("-"):
            s = s[: -len(suf)]
    return s

candidates = json.load(open(os.path.join(GRAPH, "schemas", "entity-candidates.json")))

PRECEDENCE = {"board.orgs": 0, "board.houses": 0, "watchlist.ai.orgs": 1, "watchlist.global-capital.orgs": 1,
              "watchlist.mental-health.orgs": 1, "watchlist.ai.people": 1, "watchlist.global-capital.people": 1,
              "watchlist.mental-health.people": 1, "graph.q1_facet": 2}

clusters = {}  # normalized key -> list of candidates
for c in candidates:
    key = normalize(c["slug"])
    clusters.setdefault(key, []).append(c)

crosswalk = {}
review = []
KNOWN_DISTINCT = {
    # normalized keys that collide but are genuinely different real-world entities --
    # ruled here rather than left for a slow F4 review, because the distinction is
    # unambiguous from the data itself (different kind, or a documented board note).
    ("openai",): None,  # placeholder pattern, unused -- see loop below for real logic
}

for key, members in sorted(clusters.items()):
    slugs = sorted(set(m["slug"] for m in members))
    kinds = set(m["kind"] for m in members)
    sources = sorted(set(m["source"] for m in members))
    if len(slugs) == 1:
        # one true slug across every source that mentions it -- confident, no review needed
        canonical = slugs[0]
        aliases = [canonical]
    else:
        # multiple distinct slugs normalized to the same key -- apply precedence
        best_src = min((PRECEDENCE.get(m["source"], 9), m["slug"]) for m in members)
        canonical = best_src[1]
        aliases = slugs
        # Genuine ambiguity test: do the colliding slugs actually look like the SAME
        # entity (a facet split, a naming variant) or could plausibly be different
        # entities that happen to normalize together? Flag for review whenever more
        # than one *board or watchlist* (precedence 0/1) slug exists -- that's two
        # curated, human-authored names disagreeing, not a mechanical facet split.
        curated_slugs = set(m["slug"] for m in members if PRECEDENCE.get(m["source"], 9) <= 1)
        if len(curated_slugs) > 1:
            review.append({"key": key, "members": [{"slug": m["slug"], "source": m["source"],
                                                       "name": m["name"], "provenance": m["provenance"]}
                                                      for m in members]})
            continue
    crosswalk[canonical] = {
        "aliases": aliases,
        "kind": list(kinds)[0] if len(kinds) == 1 else sorted(kinds),
        "sources": sources,
        "facet_atoms": [m["facet_atom_id"] for m in members if "facet_atom_id" in m],
    }

import yaml
with open(os.path.join(GRAPH, "schemas", "entity-crosswalk.yaml"), "w") as f:
    yaml.safe_dump({"canonical": crosswalk}, f, sort_keys=True, allow_unicode=True, width=100)

print(f"{len(crosswalk)} confident canonical entities written to entity-crosswalk.yaml")
print(f"{len(review)} clusters need review (curated-vs-curated slug disagreement):\n")
for r in review:
    print(f"  KEY: {r['key']}")
    for m in r["members"]:
        print(f"    {m['slug']:30} [{m['source']:28}] {m['name']!r}  <- {m['provenance']}")
    print()

with open(os.path.join(GRAPH, "schemas", "entity-review-needed.json"), "w") as f:
    json.dump(review, f, indent=1)
