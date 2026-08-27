#!/usr/bin/env python3
"""Step 4 (F0): artifacts/bundles/<node>-node/provenance.yaml -> claims
(graph/DESIGN.md §8.4). Mirrors publish/adapter.py's build_claims() dim-
walking EXACTLY (read directly, not paraphrased): posture, capital.
{available,operating,deployed,in,out}, optionality, gravity -- only where
`sub.get("value")` is truthy, confidence = the first source whose
`confidence` is high/med/low. Only the 83 *-node bundles (glob-matched
identically to build_claims()) -- NOT the -axes or named-investigation
bundles, and NOT build_claims()'s pocket/sector AGGREGATE claims (those
are pure computation over claims that already exist here; a trivial
follow-on if ever wanted, out of this design's stated scope).

Refresh-aware like step 5: id includes asof, so a re-run with a changed
bundle produces a new claim + supersedes the old, rather than mutating
history in place.
"""
import glob, hashlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
ORIGIN = "graph/ingest/04_bundle_claims.py, 2026-08-27"

def slug(s): return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
def rel_id(s, p, t): return "rel-" + slug(f"{s}:{p}:{t}")
def rel_name(s, p, t):
    b = lambda r: r.split(":", 1)[1]
    return f"{b(s)}:{p}:{b(t)}"
def base(kind, idf, idv, name):
    return {"kind": kind, idf: idv, "version": VER, "name": name, "data_domain": DOMAIN, "sensitivity": SENS}
CONF_BAND = {"high": "strong", "med": "moderate", "low": "weak"}
CONF_WEIGHT = {"high": 0.85, "med": 0.6, "low": 0.35}

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
entity_by_slug = {a["meta"]["entity_slug"]: a for a in atoms
                  if a.get("atom_type") == "entity" and a.get("meta", {}).get("entity_slug")}

DIM_LABELS = {"posture": "Posture", "optionality": "Optionality", "gravity": "Gravity",
              "capital-available": "Capital · available", "capital-operating": "Capital · operating",
              "capital-deployed": "Capital · deployed", "capital-in": "Capital · in", "capital-out": "Capital · out"}

new_atoms, new_sources, new_rels = [], [], []
created, refreshed, noop, no_entity = 0, 0, 0, []

def make_source(s):
    url, label = s.get("url"), s.get("label")
    key = (url, label)
    if key in src_by_key:
        return src_by_key[key]
    # hash-suffixed, not truncated: bundles reuse generic labels ("DuckDuckGo
    # HTML search aggregation") across many different underlying URLs that
    # share a long common prefix -- a plain [:75] truncation collided 13
    # different (label,url) pairs onto a handful of ids on the first run.
    h = hashlib.sha1(f"{label}|{url}".encode()).hexdigest()[:10]
    sid = "src-bundle-" + slug(str(label))[:50] + "-" + h
    evidence_class = "testimony_disinterested" if (url and not url.startswith(("http://", "https://"))) else "published_document"
    src = base("source", "source_id", sid, label or "untitled")
    src.update({"source_type": "web_page" if str(url).startswith("http") else "other", "title": label,
                "locator": url, "published_at": str(s.get("as_of")) if s.get("as_of") else None,
                "evidence_class": evidence_class, "meta": {"figure_text": s.get("figure"), "origin": ORIGIN}})
    src = {k: v for k, v in src.items() if v is not None}
    new_sources.append(src); src_by_key[key] = sid
    return sid

def add_claim(node, dim, sub, asof, entity):
    global created, refreshed, noop
    if not sub or not sub.get("value"):
        return
    cid = f"kat-claim-bundle-{node}--{dim}--{asof}"
    if cid in atom_ids:
        noop += 1; return
    prior = [a for a in atoms + new_atoms if a.get("meta", {}).get("bundle_node") == node
             and a.get("meta", {}).get("dimension") == dim and a.get("lifecycle_status") == "active"
             and a["knowledge_atom_id"] != cid]
    value = " ".join(str(sub.get("value", "")).split())
    basis = " ".join(str(sub.get("basis", "")).split())
    c = base("knowledge_atom", "knowledge_atom_id", cid, f"{DIM_LABELS.get(dim, dim)}: {value[:100]}")
    c.update({"atom_type": "claim", "label": c["name"], "summary": basis or value, "body": value,
              "epistemic_status": "accepted", "source_process": "extraction", "valid_from": asof,
              "meta": {"bundle_node": node, "dimension": dim, "origin": ORIGIN},
              "formalization_stage": "S3", "lifecycle_status": "active", "sources": []})
    atom_ids.add(cid)
    cref = f"knowledge_atom:{cid}"

    if entity:
        eref = f"knowledge_atom:{entity['knowledge_atom_id']}"
        rid = rel_id(cref, "about", eref)
        if rid not in rel_ids:
            r = base("relationship", "relationship_id", rid, rel_name(cref, "about", eref))
            r.update({"source_ref": cref, "target_ref": eref, "predicate_id": "about",
                      "qualifiers": {"role": "subject"}, "review_status": "unreviewed"})
            new_rels.append(r); rel_ids.add(rid)
    else:
        no_entity.append(node)

    conf_seen = None
    for s in sub.get("sources") or []:
        conf = s.get("confidence")
        if conf in CONF_BAND and conf_seen is None:
            conf_seen = conf
        sid = make_source(s)
        c["sources"].append(sid)
        rid = rel_id(f"source:{sid}", "supports", cref)
        if rid not in rel_ids:
            r = base("relationship", "relationship_id", rid, rel_name(f"source:{sid}", "supports", cref))
            r.update({"source_ref": f"source:{sid}", "target_ref": cref, "predicate_id": "supports",
                      "evidence_class": next((ns["evidence_class"] for ns in new_sources if ns["source_id"] == sid),
                                              next((os_["evidence_class"] for os_ in sources if os_["source_id"] == sid), "published_document")),
                      "evidence_strength_band": CONF_BAND.get(conf), "evidence_weight": CONF_WEIGHT.get(conf),
                      "review_status": "unreviewed"})
            new_rels.append(r); rel_ids.add(rid)
    new_atoms.append(c)

    if prior:
        for p in prior:
            pref = f"knowledge_atom:{p['knowledge_atom_id']}"
            rid = rel_id(cref, "supersedes", pref)
            if rid not in rel_ids:
                r = base("relationship", "relationship_id", rid, rel_name(cref, "supersedes", pref))
                r.update({"source_ref": cref, "target_ref": pref, "predicate_id": "supersedes",
                          "review_status": "reviewed", "note": f"bundle refresh: {node}--{dim} updated to {asof}."})
                new_rels.append(r); rel_ids.add(rid)
            p["lifecycle_status"] = "deprecated"
        refreshed += 1
    else:
        created += 1

for f in sorted(glob.glob(os.path.join(REPO, "artifacts/bundles/*-node/provenance.yaml"))):
    d = yaml.safe_load(open(f)) or {}
    node = d.get("node")
    if not node:
        continue
    asof = str(d.get("asof", ""))
    entity = entity_by_slug.get(node)
    add_claim(node, "posture", d.get("posture"), asof, entity)
    for k, sub in (d.get("capital") or {}).items():
        add_claim(node, "capital-" + k, sub, asof, entity)
    for dim in ("optionality", "gravity"):
        add_claim(node, dim, d.get(dim), asof, entity)

write("atoms.jsonl", atoms + new_atoms)
write("sources.jsonl", sources + new_sources)
write("relationships.jsonl", rels + new_rels)
print(f"{created} new claim(s), {refreshed} refreshed, {noop} unchanged (no-op)")
print(f"{len(set(no_entity))} node(s) with no matching canonical entity: {sorted(set(no_entity))[:20]}")
