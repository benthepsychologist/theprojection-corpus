#!/usr/bin/env python3
"""add.py — append ONE new financing to the authoritative graph.

THE SEAM: this tool never fetches a URL and never classifies evidence itself.
It takes a compact description of a financing PLUS an already-captured,
already-classified source, and does only the AKM-shape structuring: entity/
event atoms (creating new ones if needed), a claim atom, about/funds
relationships, and a source/supports/annotation/extraction_pass set from the
source info handed to it.

Today, "already-captured, already-classified" means a research agent did a
real WebSearch/WebFetch and filled in the fields by hand -- the same practice
every q1-flows research pass has always used. Once
cloud-researcher/INBOX/2026-08-27-theprojection-corpus-verify-kit-not-reachable-
from-consuming-repos.md is answered, the same input shape should be
producible by calling cloud-researcher's fetch-one/capture-citations/
fill-provenance tools instead of a human filling in reliability by hand --
NOTHING in this script changes when that happens. That is the point of the
seam: swap what fills in the input dict, never touch the fan-out below it.

Per-source capture granularity (Ben, 2026-08-27): one extraction_pass per
CALL to this tool, covering exactly the one source it was given -- not a
session-level marker covering many. This is the discipline the frozen YAML
never had (see graph/README.md and the round-three brief on
extraction_pass.source_target_ref cardinality).

Usage: import and call add_financing(...), or run as a script with a JSON
input file: python3 add.py input.json
"""
import json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")

def atom_id(prefix, raw_id):
    return f"kat-{prefix}-{slug(raw_id)}"

def rel_id(source_ref, pred, target_ref):
    return "rel-" + slug(f"{source_ref}:{pred}:{target_ref}")

def rel_name(source_ref, pred, target_ref):
    def bare(ref): return ref.split(":", 1)[1]
    return f"{bare(source_ref)}:{pred}:{bare(target_ref)}"

def base_obj(kind, id_field, id_val, name):
    return {"kind": kind, id_field: id_val, "version": VER, "name": name,
            "data_domain": DOMAIN, "sensitivity": SENS}

def reliability_band(r):
    if r is None: return None
    if r >= 0.8: return "strong"
    if r >= 0.5: return "moderate"
    return "weak"

def append_jsonl(fname, row):
    with open(os.path.join(HERE, fname), "a") as f:
        f.write(json.dumps(row, sort_keys=True) + "\n")

def read_jsonl(fname):
    path = os.path.join(HERE, fname)
    if not os.path.exists(path):
        return []
    return [json.loads(l) for l in open(path) if l.strip()]

def find_entity_atom(entity_slug_or_q1_id):
    """Look up an existing entity/event atom by its meta.q1_node_id (preferred)
    or meta.entity_slug. Returns the atom dict or None."""
    for a in read_jsonl("atoms.jsonl"):
        if a.get("atom_type") not in ("entity", "event"):
            continue
        m = a.get("meta", {})
        if m.get("q1_node_id") == entity_slug_or_q1_id or m.get("entity_slug") == entity_slug_or_q1_id:
            return a
    return None

def make_entity_atom(q1_node_id, entity_name, activity=None):
    """Create a new entity atom if one doesn't already exist for this node id.
    Mirrors build_graph.py's label convention exactly (entity + activity) so
    the two never diverge."""
    existing = find_entity_atom(q1_node_id)
    if existing:
        return f"knowledge_atom:{existing['knowledge_atom_id']}"
    label = f"{entity_name} ({activity})" if activity else entity_name
    aid = atom_id("ent", q1_node_id)
    a = base_obj("knowledge_atom", "knowledge_atom_id", aid, label)
    a.update({
        "atom_type": "entity", "label": label, "aliases": [q1_node_id],
        "meta": {"q1_node_id": q1_node_id, "entity_slug": slug(entity_name),
                 "activity": activity, "coverage_state": "measured",
                 "origin": f"added via graph/add.py, {datetime.date.today().isoformat()}"},
        "formalization_stage": "S2", "lifecycle_status": "active", "sources": [],
    })
    a["meta"] = {k: v for k, v in a["meta"].items() if v is not None}
    append_jsonl("atoms.jsonl", a)
    return f"knowledge_atom:{aid}"

def add_financing(*, from_node, from_entity_name, from_activity,
                   to_node, to_entity_name, to_activity,
                   amount_usd, flow_type, destination_category, note,
                   valid_from=None, valid_to=None, quantity_basis="point",
                   quantity_lower=None, quantity_upper=None,
                   source_label, source_url, source_evidence_class,
                   source_reliability, source_rationale, source_as_of=None,
                   source_captured_text_path=None, source_capture_sha256=None,
                   edge_id=None):
    """Add one new financing claim to the graph. `edge_id` is a human-chosen
    slug (mirrors the YAML register's edge-id convention) used only for
    display/traceability -- the graph doesn't require it to be unique across
    kinds the way the frozen YAML did.

    `source_captured_text_path` / `source_capture_sha256`: fill these in once
    a real capture exists (today: fetched and hashed by hand, matching
    fetch-one.py's own stamp format; tomorrow: cloud-researcher's own output,
    same fields, same meaning). Leave both None for a link-only citation --
    honest under-capture, not a blocker.
    """
    from_ref = make_entity_atom(from_node, from_entity_name, from_activity)
    to_ref = make_entity_atom(to_node, to_entity_name, to_activity)

    eid = edge_id or slug(f"{from_node}--{to_node}--{datetime.date.today().isoformat()}")
    cid = atom_id("claim", f"{eid}--obs0")
    from_label = find_entity_atom(from_node)["label"] if find_entity_atom(from_node) else from_entity_name
    to_label = find_entity_atom(to_node)["label"] if find_entity_atom(to_node) else to_entity_name
    label = f"{from_label} → {to_label}: {note}"
    claim = base_obj("knowledge_atom", "knowledge_atom_id", cid, label[:160])
    claim.update({
        "atom_type": "claim", "label": label[:160], "summary": note, "body": note,
        "valid_from": valid_from, "valid_to": valid_to,
        # Quantity cluster is INLINE on the atom per reg-02's ruling (not a trait,
        # not meta): quantity / quantity_unit / quantity_lower / quantity_upper /
        # quantity_basis as ordinary top-level properties.
        "quantity": amount_usd, "quantity_lower": quantity_lower, "quantity_upper": quantity_upper,
        "quantity_unit": "USD" if (amount_usd is not None or quantity_lower is not None) else None,
        "quantity_basis": quantity_basis,
        "epistemic_status": "accepted", "source_process": "extraction",
        "meta": {"q1_edge_id": eid, "q1_from_node": from_node, "q1_to_node": to_node,
                 "flow_type": flow_type, "destination_category": destination_category,
                 "origin": f"added via graph/add.py, {datetime.date.today().isoformat()}"},
        "formalization_stage": "S3", "lifecycle_status": "active", "sources": [],
    })
    claim = {k: v for k, v in claim.items() if v is not None}
    claim["meta"] = {k: v for k, v in claim["meta"].items() if v is not None}

    sid = "src-" + slug(f"{eid}-{source_label}")[:80]
    src = base_obj("source", "source_id", sid, source_label)
    src.update({"source_type": "web_page", "title": source_label, "locator": source_url,
                "published_at": source_as_of, "evidence_class": source_evidence_class,
                "meta": {k: v for k, v in {
                    "capture_path": source_captured_text_path,
                    "capture_sha256": source_capture_sha256,
                }.items() if v is not None}})
    if not src["meta"]:
        del src["meta"]
    claim["sources"].append(sid)
    claim_ref, source_ref = f"knowledge_atom:{cid}", f"source:{sid}"
    append_jsonl("atoms.jsonl", claim)
    append_jsonl("sources.jsonl", src)

    for target_ref, tag in ((from_ref, "from"), (to_ref, "to")):
        r = base_obj("relationship", "relationship_id", rel_id(claim_ref, "about", target_ref),
                     rel_name(claim_ref, "about", target_ref))
        r.update({"source_ref": claim_ref, "target_ref": target_ref, "predicate_id": "about",
                  "qualifiers": {"role": tag}, "review_status": "unreviewed"})
        append_jsonl("relationships.jsonl", r)

    funds = base_obj("relationship", "relationship_id", rel_id(from_ref, "funds", to_ref),
                     rel_name(from_ref, "funds", to_ref))
    funds.update({"source_ref": from_ref, "target_ref": to_ref, "predicate_id": "funds",
                  "qualifiers": {"materialized_from_claim_ref": claim_ref, "q1_edge_id": eid},
                  "review_status": "unreviewed"})
    append_jsonl("relationships.jsonl", funds)

    sup = base_obj("relationship", "relationship_id", rel_id(source_ref, "supports", claim_ref),
                   rel_name(source_ref, "supports", claim_ref))
    sup.update({"source_ref": source_ref, "target_ref": claim_ref, "predicate_id": "supports",
                "evidence_class": source_evidence_class,
                "evidence_strength_band": reliability_band(source_reliability),
                "evidence_weight": source_reliability, "review_status": "unreviewed"})
    append_jsonl("relationships.jsonl", sup)

    # One extraction_pass PER CALL, covering exactly this one source -- the
    # per-source granularity ruling, honored from the first new entry rather
    # than inherited as a historical-seed exception.
    pid = "ep-" + slug(f"{eid}-{datetime.date.today().isoformat()}")[:60]
    ep = base_obj("extraction_pass", "extraction_pass_id", pid, f"capture for {eid}")
    ep.update({"pass_type": "A5", "pass_iteration": 1, "pass_mode": "blind",
               "agent_identity": "claude-session-theprojection-corpus-add-tool",
               "methodology_version": "q1-flows-graph-add-1.0",
               # extraction_pass@1.1.0 as RULED by cloud-governor reg-02 (2026-08-27):
               # source_target_refs is the required array; the singular field is
               # dropped. (Our round-three brief's anyOf shape was refused -- anyOf
               # is a forbidden keyword in the registrar profile.)
               "source_target_refs": [source_ref]})
    append_jsonl("extraction_passes.jsonl", ep)

    ann_id = "ann-" + slug(f"{eid}-obs0")[:70]
    ann = base_obj("annotation", "annotation_id", ann_id, f"extraction provenance for {cid}")
    ann.update({"annotation_type": "extraction_provenance", "target_ref": claim_ref,
                "generated_by_ref": f"extraction_pass:{pid}", "source_ref": source_ref,
                "justification": source_rationale})
    append_jsonl("annotations.jsonl", ann)

    print(f"Added: {claim_ref}  (edge {eid}, ${amount_usd:,} {flow_type})" if amount_usd
          else f"Added: {claim_ref}  (edge {eid}, {flow_type})")
    return claim_ref


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: add.py <input.json>  (see graph/README.md for the field shape)")
        sys.exit(2)
    with open(sys.argv[1]) as f:
        add_financing(**json.load(f))
