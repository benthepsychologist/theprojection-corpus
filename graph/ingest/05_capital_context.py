#!/usr/bin/env python3
"""Step 5 (F0): attention/capital-context.yaml's 5 readings -> claims
(graph/DESIGN.md §8.5). Refresh-aware per §8 intro: same as_of on a
re-run is a no-op; a new as_of creates a new claim and supersedes the old
(deprecating it), rather than mutating history in place -- the reading's
own evolution stays visible, same discipline as the q1 revision findings.
`framing` (emphasis/deprioritize/notes) is steering, not ingested.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
ORIGIN = "graph/ingest/05_capital_context.py, 2026-08-27"

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

atoms = read("atoms.jsonl")
sources = read("sources.jsonl")
rels = read("relationships.jsonl")
atom_ids = {a["knowledge_atom_id"] for a in atoms}
rel_ids = {r["relationship_id"] for r in rels}
src_by_key = {(s.get("locator"), s.get("title")): s["source_id"] for s in sources}

cc = yaml.safe_load(open(os.path.join(REPO, "attention", "capital-context.yaml")))
new_atoms, new_sources, new_rels = [], [], []
created, noop, refreshed = 0, 0, 0

for key, reading in cc.get("readings", {}).items():
    as_of = str(reading.get("as_of", ""))
    cid = f"kat-claim-capctx-{key}-{as_of}"
    if cid in atom_ids:
        noop += 1
        continue
    # find any prior reading of this same key (different as_of) to supersede
    prior = [a for a in atoms if a.get("meta", {}).get("reading_key") == key
             and a.get("lifecycle_status") == "active" and a["knowledge_atom_id"] != cid]

    value = " ".join(str(reading.get("value", "")).split())
    basis = " ".join(str(reading.get("basis", "")).split())
    c = base("knowledge_atom", "knowledge_atom_id", cid, f"capital-context: {key} as of {as_of}")
    c.update({"atom_type": "claim", "label": c["name"], "summary": basis, "body": value,
              "epistemic_status": "accepted", "source_process": "extraction",
              "valid_from": as_of,
              "question": ["q7"],
              "meta": {"reading_key": key, "origin": ORIGIN},
              "formalization_stage": "S4", "lifecycle_status": "active", "sources": []})
    new_atoms.append(c); atom_ids.add(cid)
    cref = f"knowledge_atom:{cid}"

    for src in reading.get("sources", []) or []:
        skey = (src.get("url"), src.get("label"))
        sid = src_by_key.get(skey)
        if not sid:
            sid = "src-" + slug(f"capctx-{key}-{src.get('label','')}")[:80]
            s = base("source", "source_id", sid, src.get("label") or "untitled")
            s.update({"source_type": "web_page" if src.get("url") else "other", "title": src.get("label"),
                       "locator": src.get("url"), "published_at": str(src.get("as_of")) if src.get("as_of") else None,
                       "evidence_class": "published_document",
                       "meta": {"figure_text": src.get("figure"), "origin": ORIGIN}})
            s = {k: v for k, v in s.items() if v is not None}
            new_sources.append(s); src_by_key[skey] = sid
        c["sources"].append(sid)
        rid = rel_id(f"source:{sid}", "supports", cref)
        if rid not in rel_ids:
            r = base("relationship", "relationship_id", rid, rel_name(f"source:{sid}", "supports", cref))
            r.update({"source_ref": f"source:{sid}", "target_ref": cref, "predicate_id": "supports",
                       "evidence_class": "published_document", "review_status": "unreviewed"})
            new_rels.append(r); rel_ids.add(rid)

    if prior:
        for p in prior:
            pref = f"knowledge_atom:{p['knowledge_atom_id']}"
            rid = rel_id(cref, "supersedes", pref)
            if rid not in rel_ids:
                r = base("relationship", "relationship_id", rid, rel_name(cref, "supersedes", pref))
                r.update({"source_ref": cref, "target_ref": pref, "predicate_id": "supersedes",
                          "review_status": "reviewed", "note": f"capital-context refresh: {key} updated {p['valid_from']} -> {as_of}."})
                new_rels.append(r); rel_ids.add(rid)
            p["lifecycle_status"] = "deprecated"
        refreshed += 1
    else:
        created += 1

write("atoms.jsonl", atoms + new_atoms)
write("sources.jsonl", sources + new_sources)
write("relationships.jsonl", rels + new_rels)
print(f"{created} new reading(s), {refreshed} refreshed (superseded prior), {noop} unchanged (no-op)")
