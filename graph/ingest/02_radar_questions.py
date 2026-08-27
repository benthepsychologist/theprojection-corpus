#!/usr/bin/env python3
"""Step 2 (F0): radar Q1-Q7 -> question atoms (graph/DESIGN.md §8.2), plus the
q3 claim-lifting fix (§10.5) this same step owns. `question` facet is a list,
never `loi` (withdrawn, §1 -- one line, no partition).

Radar mode -> tier-2 shape is documentation (§3's table), not enforced here;
this step only creates the 7 question atoms and back-fills `question` onto
every existing claim that already resolves to one obviously (q1 flows -> q2;
the newly-lifted q3 claims -> q1+q2, since they're about who's building what
AND where capex physically lands).
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
QUESTION_BY_LENS = {"ai": ["q1", "q5"], "global-capital": ["q2", "q7"],
                     "mental-health": ["q3", "q4", "q6"], "world-news": []}
_threads = yaml.safe_load(open(os.path.join(REPO, "attention", "threads.yaml")))
LENS_BY_THREAD = {t["slug"]: t["lens"] for t in _threads["threads"]}

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

QUESTIONS = [
    ("q1", "Who are the players, and what are they DOING?", "monitor", ["ai", "mental-health"]),
    ("q2", "Where is the money going?", "answer", ["ai", "global-capital"]),
    ("q3", "Is mental-health tech getting more rigorous, or is hype winning?", "monitor", ["mental-health"]),
    ("q4", "How is AI showing up in mental health — and is it safe and governed?", "monitor", ["ai", "mental-health"]),
    ("q5", "Where is frontier AI heading overall?", "monitor", ["ai"]),
    ("q6", "What's moving in the market around my work?", "monitor", ["mental-health", "global-capital"]),
    ("q7", "Where is capital and economic power concentrating — in my markets and above them?", "monitor", ["global-capital"]),
]

atoms = read("atoms.jsonl")
atom_ids = {a.get("knowledge_atom_id") for a in atoms}
new_atoms = []
for qid, label, mode, lenses in QUESTIONS:
    aid = f"kat-q-{qid}"
    if aid in atom_ids:
        continue
    q = base("knowledge_atom", "knowledge_atom_id", aid, label)
    q.update({"atom_type": "question", "label": label, "epistemic_status": "undecided",
              "meta": {"mode": mode, "lens": lenses, "radar_slug": qid, "origin": "graph/ingest/02_radar_questions.py, 2026-08-27"},
              "formalization_stage": "S2", "lifecycle_status": "active"})
    new_atoms.append(q)
print(f"{len(new_atoms)} question atom(s) created")

# ---- backfill `question` on existing claims where it's unambiguous from content ----
# FIXED (found by a full-pipeline idempotency smoke test, 2026-08-27): the
# original upcoming_id branch was `"financ" in ... or True`, which is always
# True regardless of the check -- every hypothesis claim silently got
# question:[q2] ("where is the money going"), including ones with nothing to
# do with money (Lisa Cook's Fed removal, Ukraine's coalition meeting, an FDA
# psychedelic hearing). Correct derivation: look up the hypothesis's own
# `thread` in threads.yaml for its lens, then the same lens->question map
# digest bullets use (§12.1's stated interim). This OVERWRITES any
# `question` already set on an upcoming-sourced claim, since the prior value
# may be the bug's output, not a real assignment -- q1-flow claims (already
# correctly [q2], no thread lookup needed) are left untouched.
backfilled, corrected = 0, 0
for a in atoms:
    if a.get("atom_type") != "claim":
        continue
    m = a.get("meta", {})
    if ("q1_edge_id" in m or "q1_from_node" in m) and "question" not in a:
        a["question"] = ["q2"]
        backfilled += 1
        continue
    if m.get("upcoming_id"):
        threads = m.get("thread") or []
        threads = threads if isinstance(threads, list) else [threads]
        qs = sorted({q for t in threads for q in QUESTION_BY_LENS.get(LENS_BY_THREAD.get(t), [])})
        if a.get("question") != qs:
            corrected += 1 if "question" in a else 0
            backfilled += 1 if "question" not in a else 0
            a["question"] = qs
            a["meta"]["question_derived"] = True
print(f"{backfilled} claim(s) backfilled with `question`, {corrected} corrected "
      f"(had a wrong prior value from the `or True` bug)")

write("atoms.jsonl", atoms + new_atoms)

# ---- §10.5: lift q3 facility propositions out of entity meta into claim atoms ----
rels = read("relationships.jsonl")
sources = read("sources.jsonl")
annos = read("annotations.jsonl")
rel_ids = {r["relationship_id"] for r in rels}
atoms = read("atoms.jsonl")
atom_ids = {a.get("knowledge_atom_id") for a in atoms}

q3_facilities = [a for a in atoms if a.get("meta", {}).get("q3_facility")]
lifted_claims, lifted_rels, repointed_supports = [], [], 0
for fac in q3_facilities:
    fid = fac["knowledge_atom_id"]
    fref = f"knowledge_atom:{fid}"
    mw = fac["meta"].get("epoch_current_mw")
    if mw is not None:
        cid = f"kat-claim-{fid[len('kat-fac-'):]}-mw"
        if cid not in atom_ids:
            c = base("knowledge_atom", "knowledge_atom_id", cid, f"{fac['label']} draws {mw} MW (Epoch AI census)")
            c.update({"atom_type": "claim", "label": c["name"], "summary": c["name"],
                      "quantity": mw, "quantity_unit": "MW", "quantity_basis": "point",
                      "epistemic_status": "accepted", "source_process": "extraction",
                      "question": ["q1", "q2"],
                      "meta": {"about_facility": fid, "origin": "graph/ingest/02_radar_questions.py §10.5 lift, 2026-08-27"},
                      "formalization_stage": "S3", "lifecycle_status": "active",
                      "sources": list(fac.get("sources", []))})
            lifted_claims.append(c)
            atom_ids.add(cid)
            cref = f"knowledge_atom:{cid}"
            r = base("relationship", "relationship_id", rel_id(cref, "about", fref), rel_name(cref, "about", fref))
            r.update({"source_ref": cref, "target_ref": fref, "predicate_id": "about",
                      "qualifiers": {"role": "subject"}, "review_status": "unreviewed"})
            if r["relationship_id"] not in rel_ids:
                lifted_rels.append(r); rel_ids.add(r["relationship_id"])
            # re-point existing supports edges that targeted the facility entity -> the new claim
            for rr in rels:
                if rr["predicate_id"] == "supports" and rr["target_ref"] == fref:
                    rr["target_ref"] = cref
                    repointed_supports += 1
    # drop the MW figure from entity meta now that it's a claim (identity + facets only remain)
    fac["meta"].pop("epoch_current_mw", None)

print(f"§10.5: lifted {len(lifted_claims)} MW claim(s) out of facility entity meta; "
      f"repointed {repointed_supports} supports edge(s) from entity to claim")

write("atoms.jsonl", atoms + lifted_claims)
write("relationships.jsonl", rels + lifted_rels)
