#!/usr/bin/env python3
"""Step 3 (F0): the remaining attention/upcoming.yaml expectations -> hypothesis
claims. Same mapping port_hypotheses_q3.py proved on 16 financing items,
widened to all, with the slip-chain fix from graph/DESIGN.md §8.3 (found
during review, never actually built until now -- the 16 already ported had
zero slips, so nothing needed re-shaping retroactively; only 3 items in the
whole 70-item ledger have a `slips` field at all).

Slip chain: "X by D" is falsified the moment D passes without D confirming
it -- that's a REJECTED claim, not a mutated one. "X by D'" is a NEW
hypothesis that `supersedes` it. A due date with two prior slips is a
three-link chain. idempotent: guarded on kat-hyp-<id>[--slipN] existing.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"

def slug(s): return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
def rel_id(s, p, t): return "rel-" + slug(f"{s}:{p}:{t}")
def rel_name(s, p, t):
    b = lambda r: r.split(":", 1)[1]
    return f"{b(s)}:{p}:{b(t)}"
def base(kind, idf, idv, name):
    return {"kind": kind, idf: idv, "version": VER, "name": name, "data_domain": DOMAIN, "sensitivity": SENS}
def band(r):
    if r is None: return None
    return "strong" if r >= 0.8 else "moderate" if r >= 0.5 else "weak"

def read(fname):
    p = os.path.join(GRAPH, fname)
    return [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []
def write(fname, rows):
    with open(os.path.join(GRAPH, fname), "w") as f:
        for r in rows: f.write(json.dumps(r, sort_keys=True) + "\n")

STATUS = {"pending": "hypothesized", "hit": "accepted", "slipped": "hypothesized", "passed-silent": "rejected"}
CONF = {"confirmed": "high", "reported": "medium", "rumored": "low"}
ORIGIN = "graph/ingest/03_expectations.py, 2026-08-27"

atoms = read("atoms.jsonl")
sources = read("sources.jsonl")
rels = read("relationships.jsonl")
annos = read("annotations.jsonl")
passes = read("extraction_passes.jsonl")
atom_ids = {a["knowledge_atom_id"] for a in atoms}
rel_ids = {r["relationship_id"] for r in rels}
src_keys = {(s.get("locator"), s.get("title")) for s in sources}
ann_ids = {a["annotation_id"] for a in annos}
pass_ids = {p["extraction_pass_id"] for p in passes}

# entity lookup for `about`
entity_by_slug = {}
for a in atoms:
    if a.get("atom_type") == "entity":
        es = a.get("meta", {}).get("entity_slug")
        if es: entity_by_slug.setdefault(es, a)

up = yaml.safe_load(open(os.path.join(REPO, "attention", "upcoming.yaml")))
items = up[[k for k, v in up.items() if isinstance(v, list)][0]]
already = {a["meta"]["upcoming_id"] for a in atoms if a.get("meta", {}).get("upcoming_id")}

def get_or_make_source(url_or_list, label):
    urls = url_or_list if isinstance(url_or_list, list) else [url_or_list]
    refs = []
    for url in urls:
        key = (url, label)
        existing = next((s["source_id"] for s in sources if (s.get("locator"), s.get("title")) == key), None)
        if existing:
            refs.append(f"source:{existing}"); continue
        sid = "src-" + slug(f"{label}-{url}")[:80]
        s = base("source", "source_id", sid, label)
        s.update({"source_type": "web_page", "title": label, "locator": url,
                   "evidence_class": "published_document", "meta": {"origin": ORIGIN}})
        sources.append(s); refs.append(f"source:{sid}")
    return refs

new_count = 0
for it in items:
    if it["id"] in already:
        continue
    claim_text = " ".join(str(it["claim"]).split())
    slip_dates = sorted(it.get("slips") or [])
    due_dates = [str(d) for d in slip_dates] + [str(it["due"])]  # chain: each slip, then the current due
    prev_ref = None
    final_ref = None
    for i, due in enumerate(due_dates):
        is_final = i == len(due_dates) - 1
        hid = f"kat-hyp-{slug(it['id'])}" + (f"--slip{i}" if not is_final else "")
        if hid in atom_ids:
            prev_ref = f"knowledge_atom:{hid}"; final_ref = prev_ref; continue
        status = "rejected" if not is_final else STATUS.get(it.get("status"), "hypothesized")
        h = base("knowledge_atom", "knowledge_atom_id", hid, f"{claim_text[:140]} (by {due})")
        h.update({"atom_type": "claim", "label": h["name"], "summary": claim_text, "body": claim_text,
                  "epistemic_status": status,
                  "epistemic_confidence_band": CONF.get(it.get("confidence")),
                  "source_process": "inference",
                  "defeat_conditions": " ".join(str(it.get("what_confirms", "")).split()) or None,
                  "valid_to": due if status == "hypothesized" else None,
                  "meta": {k: v for k, v in {
                      "upcoming_id": it["id"] if is_final else None, "thread": it.get("thread"),
                      "due": due, "logged": str(it.get("logged")), "logged_by": it.get("logged_by"),
                      "entities": it.get("entities"), "origin": ORIGIN}.items() if v not in (None, [], "")},
                  "formalization_stage": "S4", "lifecycle_status": "active", "sources": []})
        h = {k: v for k, v in h.items() if v is not None}
        atoms.append(h); atom_ids.add(hid); new_count += 1
        href = f"knowledge_atom:{hid}"

        if it.get("source") and i == 0:  # the logging source attaches to the FIRST link in the chain
            refs = get_or_make_source(it["source"], f"logging source for {it['id']}")
            h["sources"] = [r.split(":", 1)[1] for r in refs]
            for r in refs:
                rid = rel_id(r, "supports", href)
                if rid not in rel_ids:
                    rr = base("relationship", "relationship_id", rid, rel_name(r, "supports", href))
                    rr.update({"source_ref": r, "target_ref": href, "predicate_id": "supports",
                               "evidence_class": "published_document", "evidence_strength_band": band(0.6),
                               "evidence_weight": 0.6, "review_status": "unreviewed"})
                    rels.append(rr); rel_ids.add(rid)

        for ent in it.get("entities") or []:
            e = entity_by_slug.get(slug(ent))
            if e:
                eref = f"knowledge_atom:{e['knowledge_atom_id']}"
                rid = rel_id(href, "about", eref)
                if rid not in rel_ids:
                    rr = base("relationship", "relationship_id", rid, rel_name(href, "about", eref))
                    rr.update({"source_ref": href, "target_ref": eref, "predicate_id": "about",
                               "qualifiers": {"role": "subject"}, "review_status": "unreviewed"})
                    rels.append(rr); rel_ids.add(rid)

        if prev_ref:
            rid = rel_id(href, "supersedes", prev_ref)
            if rid not in rel_ids:
                rr = base("relationship", "relationship_id", rid, rel_name(href, "supersedes", prev_ref))
                rr.update({"source_ref": href, "target_ref": prev_ref, "predicate_id": "supersedes",
                           "review_status": "reviewed",
                           "note": f"Original due date passed without confirming ({it['id']}, slip chain)."})
                rels.append(rr); rel_ids.add(rid)
            for atm in atoms:
                if atm["knowledge_atom_id"] == prev_ref.split(":", 1)[1]:
                    atm["lifecycle_status"] = "deprecated"

        # resolution annotation on the FINAL link only
        if is_final and it.get("status") in ("hit", "passed-silent") and (it.get("evidence") or it.get("outcome_note")):
            justification = it.get("evidence") if isinstance(it.get("evidence"), str) else \
                             ("; ".join(it["evidence"]) if isinstance(it.get("evidence"), list) else it.get("outcome_note"))
            pid = "ep-" + slug(f"resolve-{it['id']}")[:60]
            if pid not in pass_ids:
                p = base("extraction_pass", "extraction_pass_id", pid, f"resolution check for {it['id']}")
                p.update({"pass_type": "A5", "pass_iteration": 2, "pass_mode": "adjudication",
                          "agent_identity": "claude-session-theprojection-corpus-graph-step3",
                          "methodology_version": "attention-week-expectations-scorecard",
                          "source_target_refs": h.get("sources", ["unspecified-resolution-prose"]) and
                              [f"source:{s}" for s in h.get("sources", [])] or ["source:unspecified-resolution-prose"]})
                passes.append(p); pass_ids.add(pid)
            aid = "ann-" + slug(f"resolve-{it['id']}")[:70]
            if aid not in ann_ids:
                an = base("annotation", "annotation_id", aid, f"resolution of {it['id']}")
                an.update({"annotation_type": "extraction_review", "target_ref": href,
                           "generated_by_ref": f"extraction_pass:{pid}", "justification": justification,
                           "extraction_confidence": "high" if it.get("status") == "hit" else "medium"})
                annos.append(an); ann_ids.add(aid)

        prev_ref = href; final_ref = href

write("atoms.jsonl", atoms); write("sources.jsonl", sources); write("relationships.jsonl", rels)
write("annotations.jsonl", annos); write("extraction_passes.jsonl", passes)
print(f"{new_count} hypothesis claim(s) created across {len(items) - len(already)} remaining expectations "
      f"(including slip-chain links)")
