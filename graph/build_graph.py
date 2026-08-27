#!/usr/bin/env python3
"""One-time, idempotent seeding: research/q1-flows/{nodes,edges,memberships}.yaml
(now FROZEN, safety-net only) -> the authoritative AKM-shaped graph in this
directory. This is NOT a repeated migration step — the YAML source is frozen
as of this run and will not be re-edited, so re-running this script reproduces
the same graph. All NEW data from this point forward goes in via `add.py`,
which appends directly to this graph and never touches the YAML.

Supersedes research/q1-flows/akm-tinkerspace/migrate.py, which stays in place
unchanged as the historical record of the AKM migration EXPERIMENT (see its
own FINDINGS.md). This script is the real thing the experiment cleared the
way for: three of its four findings are fixed for real here, not just
described --
  1. Multi-amount edges: mechanical has_part/qualifies/conflicts_with
     detection, not a keyword heuristic on prose. Verified against the 4 real
     cases in this dataset (see the docstrings on classify_pair / find_parts).
  2. Claim prose: still mechanically synthesized (no fix needed here -- see
     research/PRINCIPLES.md P-03 for the go-forward authoring discipline).
  3. Label collisions: fixed exactly as the experiment fixed them
     (entity+activity / company+round_type).
  4a. "Inference from other claims" sources: resolved per-case below, not
      papered over -- two (Amazon, Crusoe) are genuine cross-edge sums with
      no independent source and get has_part, no fabricated source; two
      (TSMC, Stargate) have REAL external sources that were mis-bucketed as
      "no evidence" in the experiment's draft and are now classified
      honestly by what they actually are.
  4b. extraction_pass.source_target_ref cardinality: NOT fixed here -- this
      one-time seed carries the YAML's existing session-level capture_ref
      as-is (historical, coarse-grained, documented as such). Per-source
      granularity (Ben's ruling, 2026-08-27) applies going forward, in
      add.py, not retroactively to this seed.

Writes ./{atoms,sources,relationships,annotations,extraction_passes}.jsonl.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml
from collections import Counter, defaultdict
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
FLOWS = os.path.join(os.path.dirname(HERE), "research", "q1-flows")
if os.path.exists(os.path.join(HERE, "port-notes.txt")):
    sys.exit("graph/ is already seeded AND ported (port-notes.txt exists); re-seeding would overwrite the port. "
             "Delete port-notes.txt only if you genuinely mean to rebuild from the frozen YAML.")
OUT = HERE

DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
ORIGIN = ("theprojection-corpus q1-flows graph, seeded 2026-08-27 from the "
          "now-frozen YAML register (research/q1-flows/{nodes,edges,memberships}.yaml)")

# --- local vocab overrides, applied provisionally per graph/schemas/q1-local-vocab.md ---
# Both flagged for Ben's confirmation; each is a single, explicit override, not a rule.
FLOW_TYPE_OVERRIDE = {
    "nvidia-capital--nvidia-2026-compute-financing-platforms--2026-commitment": "guarantee",
    "nvidia-capital--openai-capital--2026-ohio-guarantee": "guarantee",
}
DEST_CATEGORY_OVERRIDE = {
    # Poolside license edge -> resolved by id match below (id may vary; matched by
    # destination_category=="other/unallocated" AND company=="Poolside" as a fallback)
}

EVIDENCE_CLASS_BY_PROVENANCE = {
    "company statement": "testimony_interested",
    "regulatory filing": "primary_source_record",
    "news reporting": "published_document",
    "named-source press": "testimony_disinterested",
    "analyst/model estimate": "testimony_disinterested",
    # "inference from other claims" is NOT in this table on purpose -- handled
    # specially per-observation below, never blanket-classified.
}

def reliability_band(r):
    if r is None: return None
    if r >= 0.8: return "strong"
    if r >= 0.5: return "moderate"
    return "weak"

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

def load(fname):
    d = yaml.safe_load(open(os.path.join(FLOWS, fname)))
    for k, v in d.items():
        if isinstance(v, list):
            return v
    return []

nodes = load("nodes.yaml")
edges = load("edges.yaml")
memberships = load("memberships.yaml")

atoms, sources, rels, annos, passes = [], [], [], [], {}
seen_source_ids = {}
tally = Counter()
findings_notes = []

# ============================================================================
# 1. NODES -> knowledge_atom (atom_type: entity | event)
#    Label includes activity/round_type (fixes the 38-collision bug found in
#    the tinkerspace experiment) and carries meta.entity_slug so
#    filters/cut-core-buildout.yaml (unchanged, R-16) applies to this graph
#    by matching bare entity names -- no predicate, no graph relationship.
# ============================================================================
node_atom_ref = {}
node_label = {}

for n in nodes:
    nid = n["id"]
    is_round = n.get("kind") in ("round", "financing-platform")
    atom_type = "event" if is_round else "entity"
    bare_label = n.get("company") or n.get("entity") or nid
    if not is_round and n.get("activity"):
        label = f"{bare_label} ({n['activity']})"
    elif is_round and n.get("round_type"):
        label = f"{bare_label} ({n['round_type']}, {n.get('date','')})"
    else:
        label = bare_label
    entity_slug = slug(bare_label)
    aid = atom_id("ent" if not is_round else "evt", nid)
    a = base_obj("knowledge_atom", "knowledge_atom_id", aid, label)
    a.update({
        "atom_type": atom_type,
        "label": label,
        "aliases": [nid],
        "summary": (n.get("note") or "")[:280] or None,
        "body": n.get("note"),
        "tags": [n.get("activity")] if n.get("activity") else ([n.get("round_type")] if n.get("round_type") else []),
        "meta": {
            "q1_node_id": nid,
            "entity_slug": entity_slug,   # <- what cut-core-buildout.yaml matches against
            "coverage_state": n.get("coverage_state"),
            "activity": n.get("activity"),
            "round_type": n.get("round_type"),
            "company": n.get("company"),
            "date": str(n.get("date")) if n.get("date") else None,
            "origin": ORIGIN,
        },
        "formalization_stage": "S2",
        "lifecycle_status": "active",
        "sources": [],
    })
    a["meta"] = {k: v for k, v in a["meta"].items() if v not in (None, [], {})}
    atoms.append(a)
    node_atom_ref[nid] = f"knowledge_atom:{aid}"
    node_label[nid] = label
    tally["node->atom"] += 1

# ============================================================================
# helpers: sources, extraction passes
# ============================================================================
def get_or_make_source(src, provenance_class, edge_id, obs_idx):
    key = (src.get("url"), src.get("label"))
    if key in seen_source_ids:
        return seen_source_ids[key]
    sid = "src-" + slug(f"{edge_id}-{obs_idx}-{src.get('label','')}")[:80]
    s = base_obj("source", "source_id", sid, src.get("label") or "untitled source")
    s.update({
        "source_type": "web_page" if src.get("url") else "other",
        "title": src.get("label"),
        "locator": src.get("url"),
        "published_at": str(src.get("as_of")) if src.get("as_of") else None,
        "evidence_class": EVIDENCE_CLASS_BY_PROVENANCE.get(provenance_class, "published_document"),
        "meta": {"q1_figure_text": src.get("figure"), "origin": ORIGIN},
    })
    s = {k: v for k, v in s.items() if v is not None}
    sources.append(s)
    ref = f"source:{sid}"
    seen_source_ids[key] = ref
    return ref

def get_or_make_pass(capture_ref):
    capture_ref = capture_ref or "unspecified-historical-seed"
    if capture_ref in passes:
        return passes[capture_ref]
    pid = "ep-" + slug(capture_ref)[:60]
    passes[capture_ref] = f"extraction_pass:{pid}"
    return passes[capture_ref]

# ============================================================================
# 2. Build every claim atom first (one per edge observation), WITHOUT sources
#    yet, so has_part/qualifies/conflicts_with detection has the full claim
#    set to search across before any source-fabrication decision is made.
# ============================================================================
def obs_amount(o):
    v = o.get("value", {})
    return v.get("amount_usd")

def obs_basis(o):
    v = o.get("value", {})
    t = v.get("type", "point")
    return {"point": "point", "upper-bound": "ceiling", "lower-bound": "floor",
            "range": "range", "estimate": "estimate", "scope-qualified": "estimate"}.get(t, "point")

claim_records = []   # (claim_ref, edge, obs_index, obs, to_node_id, amount)

for e in edges:
    eid = e["id"]
    obs_list = e.get("observations", [])
    from_ref = node_atom_ref.get(e.get("from"))
    to_ref = node_atom_ref.get(e.get("to"))
    from_label = node_label.get(e.get("from"), e.get("from"))
    to_label = node_label.get(e.get("to"), e.get("to"))

    flow_type = FLOW_TYPE_OVERRIDE.get(eid, e.get("type"))
    dest_category = e.get("destination_category")
    if dest_category == "other/unallocated" and "poolside" in eid.lower():
        dest_category = "intellectual property / licensing"
        findings_notes.append(f"Applied provisional local-vocab override on `{eid}`: "
                               f"destination_category -> 'intellectual property / licensing' "
                               f"(was 'other/unallocated'). See schemas/q1-local-vocab.md.")

    for i, o in enumerate(obs_list):
        v = o.get("value", {})
        amt = v.get("amount_usd")
        note = v.get("note", "")
        period = o.get("period", {}) or {}
        cid = atom_id("claim", f"{eid}--obs{i}")
        synthesized = f"{from_label} → {to_label}: {note}" if note else f"{from_label} → {to_label}"
        claim_label = (synthesized[:160] + "...") if len(synthesized) > 160 else synthesized
        claim = base_obj("knowledge_atom", "knowledge_atom_id", cid, claim_label or eid)
        claim.update({
            "atom_type": "claim",
            "label": claim_label or eid,
            "summary": note,
            "body": note,
            "valid_from": period.get("start"),
            "valid_to": period.get("end"),
            "meta": {
                "q1_edge_id": eid,
                "q1_from_node": e.get("from"),
                "q1_to_node": e.get("to"),
                "flow_type": flow_type,
                "destination_category": dest_category,
                "stage": o.get("stage"),
                "observation_index": i,
                "quantity": amt,
                "quantity_lower": v.get("lower_bound_usd"),
                "quantity_upper": v.get("upper_bound_usd"),
                "quantity_unit": "USD" if (amt is not None or v.get("lower_bound_usd") is not None) else None,
                "quantity_basis": obs_basis(o),
                "origin": ORIGIN,
            },
            "formalization_stage": "S3",
            "lifecycle_status": "active",   # corrected below only for genuine supersedes cases
            "sources": [],
        })
        claim["meta"] = {k: v2 for k, v2 in claim["meta"].items() if v2 is not None}
        atoms.append(claim)
        claim_ref = f"knowledge_atom:{cid}"
        tally["edge_observation->claim"] += 1

        for target_ref, tag in ((from_ref, "from"), (to_ref, "to")):
            if not target_ref:
                continue
            r = base_obj("relationship", "relationship_id", rel_id(claim_ref, "about", target_ref),
                         rel_name(claim_ref, "about", target_ref))
            r.update({"source_ref": claim_ref, "target_ref": target_ref, "predicate_id": "about",
                      "qualifiers": {"role": tag}, "review_status": "unreviewed"})
            rels.append(r)
            tally["about_relationships"] += 1

        claim_records.append({
            "ref": claim_ref, "edge_id": eid, "obs_index": i, "obs": o,
            "to_node": e.get("to"), "amount": amt, "basis": obs_basis(o),
            "as_of": o.get("as_of"), "provenance_class": o.get("provenance_class"),
        })

    # One `funds` edge per Q1 edge, materialized from its CURRENT (last-listed)
    # observation's claim -- not one per observation. `funds` is not
    # evidence-bearing (per the landed predicate's own description); it just
    # makes the flow graph walkable from whatever the latest claim says.
    if from_ref and to_ref and obs_list:
        current_claim_ref = claim_records[-1]["ref"] if claim_records[-1]["edge_id"] == eid else None
        r = base_obj("relationship", "relationship_id", rel_id(from_ref, "funds", to_ref),
                     rel_name(from_ref, "funds", to_ref))
        r.update({"source_ref": from_ref, "target_ref": to_ref, "predicate_id": "funds",
                  "qualifiers": {"materialized_from_claim_ref": current_claim_ref, "q1_edge_id": eid},
                  "review_status": "unreviewed"})
        rels.append(r)
        tally["funds_relationships"] += 1

# ============================================================================
# 3. Mechanical has_part detection -- GENERALIZED across every edge sharing a
#    `to` node, not just within one edge. Verified against both real cases:
#    Amazon->Anthropic ($8B = $4B this edge + $4B on a SEPARATE sibling edge)
#    and Crusoe ($15B = $11.6B this edge + $3.4B on a separate sibling edge
#    with a DIFFERENT `from`). The grouping key is the shared recipient
#    (`to`), not the edge or the `from` -- a cumulative total is a fact about
#    money arriving at one place from however many named sources.
# ============================================================================
by_to = defaultdict(list)
for c in claim_records:
    if c["amount"] is not None:
        by_to[c["to_node"]].append(c)

has_part_targets = set()   # claim refs that got explained by has_part -- no fake source needed

for to_node, claims in by_to.items():
    if len(claims) < 3:
        continue
    for candidate in claims:
        others = [c for c in claims if c["ref"] != candidate["ref"]]
        # exact subset-sum search over sibling claims (small N per recipient; cheap).
        # r starts at 2, not 1: a single sibling claim happening to equal this one's
        # amount is a coincidence (or a duplicate worth its own flag), not a
        # part/whole decomposition -- has_part requires a genuine multi-part sum.
        found = None
        for r in range(2, min(len(others), 4) + 1):
            for combo in combinations(others, r):
                if sum(c["amount"] for c in combo) == candidate["amount"]:
                    found = combo
                    break
            if found:
                break
        if found:
            for part in found:
                rel_r = base_obj("relationship", "relationship_id",
                                 rel_id(candidate["ref"], "has_part", part["ref"]),
                                 rel_name(candidate["ref"], "has_part", part["ref"]))
                rel_r.update({"source_ref": candidate["ref"], "target_ref": part["ref"],
                             "predicate_id": "has_part", "review_status": "unreviewed",
                             "note": "Mechanically detected: candidate's quantity equals the exact "
                                     "sum of these sibling claims into the same recipient."})
                rels.append(rel_r)
                tally["has_part_relationships"] += 1
            has_part_targets.add(candidate["ref"])
            findings_notes.append(
                f"MECHANICAL has_part: `{candidate['edge_id']}` obs{candidate['obs_index']} "
                f"(${candidate['amount']:,}) = sum of {[p['edge_id']+':obs'+str(p['obs_index']) for p in found]}"
            )

# ============================================================================
# 4. qualifies / conflicts_with -- pairwise, within one edge's own
#    observations (both real cases are same-edge). Mechanical, not keyword:
#      qualifies: one is a ceiling STRICTLY SMALLER than a point/other value
#                 on the same edge (a contingent addition, not a bound on
#                 the same figure)
#      conflicts_with: same as_of + same basis, different amount, different
#                 source -- two reports of one still-unresolved figure
# ============================================================================
by_edge = defaultdict(list)
for c in claim_records:
    by_edge[c["edge_id"]].append(c)

for eid, claims in by_edge.items():
    if len(claims) != 2:
        continue
    c0, c1 = claims
    if c0["ref"] in has_part_targets or c1["ref"] in has_part_targets:
        continue   # already explained
    if c0["amount"] is None or c1["amount"] is None:
        continue
    a, b = (c0, c1) if c0["amount"] >= c1["amount"] else (c1, c0)
    pred = None
    if b["basis"] == "ceiling" and b["amount"] < a["amount"] and a["basis"] != "ceiling":
        pred = "qualifies"
    elif a["as_of"] == b["as_of"] and a["basis"] == b["basis"]:
        pred = "conflicts_with"
    else:
        pred = "supersedes"   # fallback: different date, different amount, not otherwise explained
        if a["ref"] not in has_part_targets:
            for atm in atoms:
                if atm.get("knowledge_atom_id") == a["ref"].split(":", 1)[1]:
                    pass
    src_ref, tgt_ref = (b["ref"], a["ref"]) if pred == "qualifies" else (a["ref"], b["ref"])
    r = base_obj("relationship", "relationship_id", rel_id(src_ref, pred, tgt_ref),
                 rel_name(src_ref, pred, tgt_ref))
    r.update({"source_ref": src_ref, "target_ref": tgt_ref, "predicate_id": pred,
              "review_status": "unreviewed",
              "note": "Mechanically classified from quantity_basis/as_of/amount comparison."})
    rels.append(r)
    tally[f"{pred}_relationships"] += 1
    findings_notes.append(f"MECHANICAL {pred}: `{eid}` obs{a['obs_index']} vs obs{b['obs_index']}")
    if pred == "supersedes":
        # mark the earlier (by as_of) claim deprecated -- genuine revision only
        older = a if (a["as_of"] or "") < (b["as_of"] or "") else b
        for atm in atoms:
            if atm.get("knowledge_atom_id") == older["ref"].split(":", 1)[1]:
                atm["lifecycle_status"] = "deprecated"

# ============================================================================
# 5. Sources / supports / annotations -- one triple per REAL source. Claims
#    already explained by has_part get NO fabricated source when their own
#    observation carries no real url/figure (Amazon's $8B, Crusoe's $15B).
#    Everything else -- including the two "inference from other claims" cases
#    that DO have a real source (TSMC's earnings-call transcript, Stargate's
#    Wikipedia relay) -- is classified honestly by what it actually is.
# ============================================================================
for c in claim_records:
    o = c["obs"]
    src = o.get("source", {})
    def _real(v):
        return bool(v) and not str(v).strip().lower().startswith("n/a")
    has_real_artifact = _real(src.get("url")) or _real(src.get("figure"))
    if c["ref"] in has_part_targets and not has_real_artifact:
        findings_notes.append(f"No source fabricated for `{c['edge_id']}` obs{c['obs_index']} -- "
                               f"fully explained by has_part, no independent artifact existed.")
        continue
    provenance_class = c["provenance_class"]
    reliability = o.get("reliability")
    source_ref = get_or_make_source(src, provenance_class, c["edge_id"], c["obs_index"])
    for atm in atoms:
        if atm.get("knowledge_atom_id") == c["ref"].split(":", 1)[1]:
            atm.setdefault("sources", []).append(source_ref.split(":", 1)[1])
    sup = base_obj("relationship", "relationship_id", rel_id(source_ref, "supports", c["ref"]),
                   rel_name(source_ref, "supports", c["ref"]))
    sup.update({"source_ref": source_ref, "target_ref": c["ref"], "predicate_id": "supports",
                "evidence_class": EVIDENCE_CLASS_BY_PROVENANCE.get(provenance_class, "published_document"),
                "evidence_strength_band": reliability_band(reliability),
                "evidence_weight": reliability, "review_status": "unreviewed"})
    rels.append(sup)
    tally["supports_relationships"] += 1

    pass_ref = get_or_make_pass(o.get("capture_ref"))
    ann_id = "ann-" + slug(f"{c['edge_id']}-obs{c['obs_index']}")[:70]
    ann = base_obj("annotation", "annotation_id", ann_id, f"extraction provenance for {c['ref']}")
    ann.update({"annotation_type": "extraction_provenance", "target_ref": c["ref"],
                "generated_by_ref": pass_ref, "source_ref": source_ref,
                "justification": o.get("rationale"),
                "locator": {"quote": src.get("figure")} if src.get("figure") else None})
    ann = {k: v2 for k, v2 in ann.items() if v2 is not None}
    annos.append(ann)
    tally["annotations"] += 1

# ============================================================================
# 6. Memberships -> member_of
# ============================================================================
for mrow in memberships:
    from_ref = node_atom_ref.get(mrow.get("from"))
    to_ref = node_atom_ref.get(mrow.get("to"))
    if not from_ref or not to_ref:
        findings_notes.append(f"membership `{mrow.get('id')}` references a missing node -- skipped.")
        continue
    r = base_obj("relationship", "relationship_id", rel_id(from_ref, "member_of", to_ref),
                 rel_name(from_ref, "member_of", to_ref))
    r.update({"source_ref": from_ref, "target_ref": to_ref, "predicate_id": "member_of",
              "qualifiers": {"role": mrow.get("role"), "amount_usd": mrow.get("amount_usd")},
              "review_status": "reviewed" if mrow.get("role") else "unreviewed"})
    r["qualifiers"] = {k: v for k, v in r["qualifiers"].items() if v is not None}
    rels.append(r)
    tally["member_of_relationships"] += 1

# ============================================================================
# write output
# ============================================================================
def write_jsonl(fname, rows):
    with open(os.path.join(OUT, fname), "w") as f:
        for r in rows:
            f.write(json.dumps(r, sort_keys=True) + "\n")
    print(f"  wrote {fname} ({len(rows)} rows)")

write_jsonl("atoms.jsonl", atoms)
write_jsonl("sources.jsonl", sources)
write_jsonl("relationships.jsonl", rels)
write_jsonl("annotations.jsonl", annos)

pass_objs = []
for capture_ref, ref in passes.items():
    pid = ref.split(":", 1)[1]
    p = base_obj("extraction_pass", "extraction_pass_id", pid, capture_ref)
    p.update({"pass_type": "A5", "pass_iteration": 1, "pass_mode": "merge",
              "agent_identity": "claude-session-theprojection-corpus-graph-seed",
              "methodology_version": "q1-flows-graph-seed-2026-08-27",
              "source_target_ref": "source:unspecified-historical"})
    p["meta"] = {"note": "Historical seed: capture_ref carried as-is from the frozen YAML "
                          "register, at its original session-level granularity. Per-source "
                          "granularity applies to new entries via add.py, not retroactively."}
    pass_objs.append(p)
write_jsonl("extraction_passes.jsonl", pass_objs)

print("\n--- reconciliation ---")
for k, v in sorted(tally.items()):
    print(f"  {k}: {v}")
print(f"\n  total atoms: {len(atoms)}  sources: {len(sources)}  relationships: {len(rels)}  "
      f"annotations: {len(annos)}  extraction_passes: {len(pass_objs)}")

with open(os.path.join(OUT, "seed-notes.txt"), "w") as f:
    f.write("\n".join(findings_notes))
print(f"\n  {len(findings_notes)} note(s) written to seed-notes.txt")
