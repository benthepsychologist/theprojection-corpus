#!/usr/bin/env python3
"""One-shot, idempotent: research/q1-flows/{nodes,edges,memberships}.yaml -> AKM-shaped
graph, per the mapping in INBOX/2026-08-27-pm-q1-akm-migration-experiment.md.

Reads  ../nodes.yaml, ../edges.yaml, ../memberships.yaml (the current, authoritative Q1
       register -- this script never writes back to those files)
Writes ./{atoms,sources,relationships,annotations,extraction_passes}.jsonl (AKM shapes:
       knowledge_atom@1.1.0 / source@1.1.0 / relationship@1.1.0 / annotation@1.0.0 /
       extraction_pass@1.0.0)

This is an UNGOVERNED TINKERSPACE EXPERIMENT (Ben, 2026-08-27: "we don't need the
governed model to be updated before we can try to migrate Q1 and see what happens").
The YAML register stays authoritative; nothing here is read by /daily, /week, or
publish/adapter.py. Three predicates used below (`about`, `member_of`, `funds`) and one
trait-shaped field cluster (`quantity`/`quantity_unit`/`quantity_lower`/`quantity_upper`/
`quantity_basis`, the proposed trait_quantified) are NOT YET LANDED in lifeos-registry as
of this run -- used as-if per pm's own brief ("use it as-if and flag it, your call"),
each flagged inline below and in FINDINGS.md.

Deterministic: ids are computed slugs from the source YAML's own ids, never random, so
a re-run reproduces the same bytes given the same input. Safe to re-run after the q1-flows
fourth research pass lands more data -- it will just pick up the new nodes/edges/memberships.
Run from this directory or the repo root; paths are relative to this file.
"""
import json, os, re, sys, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yaml
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
FLOWS = os.path.dirname(HERE)
OUT = HERE

DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
ORIGIN = "theprojection-corpus q1-flows AKM migration experiment, 2026-08-27 (pm brief INBOX/2026-08-27-pm-q1-akm-migration-experiment.md)"

# --- evidence_class mapping: q1's provenance_class -> AKM source.evidence_class -----
# pm's brief gave one example ("company statement" ~= testimony_interested); the rest
# is this script's own judgment call, flagged as such in FINDINGS.md.
EVIDENCE_CLASS = {
    "company statement": "testimony_interested",       # the entity describing its own deal
    "regulatory filing": "primary_source_record",       # SEC/EDGAR etc: the legal record itself
    "news reporting": "published_document",             # a wire/outlet's own reporting
    "named-source press": "testimony_disinterested",    # a named source quoted BY a reporter, not the entity itself
    "analyst/model estimate": "testimony_disinterested", # a third party's modeled figure -- not the entity, not raw fact
    "inference from other claims": "absence_of_evidence",# this map's OWN inference, not an external source at all --
                                                          # see FINDINGS.md: this is arguably not a `source` at all
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
seen_source_ids = {}   # (url, label) -> source_id, so re-cited sources aren't duplicated
tally = Counter()
findings_notes = []

# ============================================================================
# 1. NODES -> knowledge_atom (atom_type: entity | event)
#    q1's own coverage_state has no AKM home (round-two brief, Ask 2) -- carried
#    as meta.coverage_state, exactly as pm's brief prescribes.
# ============================================================================
node_atom_ref = {}   # q1 node id -> knowledge_atom ref, for edge/membership lookups

for n in nodes:
    nid = n["id"]
    is_round = n.get("kind") == "round" or n.get("kind") == "financing-platform"
    atom_type = "event" if is_round else "entity"
    bare_label = n.get("company") or n.get("entity") or nid
    # FINDING: bare entity name collides across every activity facet of that entity
    # (204 nodes -> 38 shared labels once flattened -- e.g. "CoreWeave" alone covers 5
    # distinct entity/activity nodes, "ext (population)" covers 6 UNRELATED undisclosed-
    # investor placeholders). AKM's knowledge_atom has no first-class "activity" field the
    # way Q1's own entity/activity node-splitting principle assumes -- appending the
    # activity here is this script's fix, not something the target schema does for free.
    if not is_round and n.get("activity"):
        label = f"{bare_label} ({n['activity']})"
    elif is_round and n.get("round_type"):
        label = f"{bare_label} ({n['round_type']}, {n.get('date','')})"
    else:
        label = bare_label
    aid = atom_id("ent" if not is_round else "evt", nid)
    a = base_obj("knowledge_atom", "knowledge_atom_id", aid, label)
    a.update({
        "atom_type": atom_type,
        "label": label,
        "aliases": [nid],
        "summary": n.get("note", "")[:280] if n.get("note") else None,
        "body": n.get("note"),
        "tags": [n.get("activity")] if n.get("activity") else ([n.get("round_type")] if n.get("round_type") else []),
        "meta": {
            "q1_node_id": nid,
            "coverage_state": n.get("coverage_state"),   # meta convention per Ask 2 -- no trait home yet
            "activity": n.get("activity"),
            "round_type": n.get("round_type"),
            "company": n.get("company"),
            "date": str(n.get("date")) if n.get("date") else None,
            "origin": ORIGIN,
        },
        "formalization_stage": "S2",
        "lifecycle_status": "active",
        "sources": [],   # trait_source_backed -- populated below once we know which sources cite this node directly (rare; most citations are edge-level)
    })
    a["meta"] = {k: v for k, v in a["meta"].items() if v not in (None, [], {})}
    atoms.append(a)
    node_atom_ref[nid] = f"knowledge_atom:{aid}"
    tally["node->atom"] += 1

# ============================================================================
# helper: register a source (dedup by url+label), return its ref
# ============================================================================
def get_or_make_source(src, provenance_class, capture_ref, edge_id, obs_idx):
    key = (src.get("url"), src.get("label"))
    if key in seen_source_ids:
        return seen_source_ids[key]
    sid = "src-" + slug(f"{edge_id}-{obs_idx}-{src.get('label','')}")[:80]
    s = base_obj("source", "source_id", sid, src.get("label") or "untitled source")
    s.update({
        "source_type": "web_page" if src.get("url") else "other",
        "title": src.get("label"),
        "locator": src.get("url"),
        "reliability_tier": None,   # q1 has no reliability_tier-shaped field; reliability lives on the SUPPORTS relationship instead (evidence_weight), not here -- see FINDINGS.md
        "captured_at": None,
        "published_at": str(src.get("as_of")) if src.get("as_of") else None,
        "evidence_class": EVIDENCE_CLASS.get(provenance_class, "published_document"),
        "meta": {"q1_figure_text": src.get("figure"), "origin": ORIGIN},
    })
    s = {k: v for k, v in s.items() if v is not None}
    sources.append(s)
    ref = f"source:{sid}"
    seen_source_ids[key] = ref
    return ref

def get_or_make_pass(capture_ref):
    if not capture_ref:
        capture_ref = "unspecified"
    if capture_ref in passes:
        return passes[capture_ref]
    pid = "ep-" + slug(capture_ref)[:60]
    p = base_obj("extraction_pass", "extraction_pass_id", pid, capture_ref)
    p.update({
        "pass_type": "A5",   # A5 = claims, per methodology enum -- q1's own pass granularity (dated,
                              # whole-file "First/Second/Third/Fourth pass") does not map cleanly onto
                              # AKM's per-atom-type pass_type enum; A5 is this script's best approximation,
                              # flagged as a genuine mismatch in FINDINGS.md, not a resolved mapping.
        "pass_iteration": 1,
        "pass_mode": "blind",
        "agent_identity": "claude-session-theprojection-corpus-q1-akm-migration",
        "methodology_version": "q1-flows-pass-4 (theprojection-corpus, not the LifeOS extraction-methodology.md)",
        "source_target_ref": "source:unspecified",  # placeholder -- an extraction_pass's source_target_ref
                                                      # schema-requires ONE source, but q1's capture_ref (e.g.
                                                      # "session-webfetch:2026-08-12") is a session marker that
                                                      # covers MANY sources fetched that day, not one. Left as a
                                                      # placeholder; real fix flagged in FINDINGS.md.
    })
    passes[capture_ref] = f"extraction_pass:{pid}"
    return passes[capture_ref]

# ============================================================================
# 2. EDGES -> a claim atom (NOT a relationship) + about + funds
#    Each edge's observations[] -> three objects each: source, supports-relationship,
#    annotation (per the round-two brief's Ask 5 factoring table).
#
#    KEY FINDING handled here: where an edge's observations carry MATERIALLY
#    DIFFERENT amounts over time (a revised/updated figure, e.g. a guarantee that
#    shrank from $250B to $105B across four disclosures), this is NOT one claim
#    with multiple corroborating sources -- it is a SEQUENCE of claims, each
#    superseding the last, linked with the landed `supersedes` predicate. Detected
#    by: >1 distinct amount_usd across observations differing by >5%.
# ============================================================================
def obs_amount(o):
    v = o.get("value", {})
    return v.get("amount_usd")

def obs_basis(o):
    v = o.get("value", {})
    t = v.get("type", "point")
    return {"point": "point", "upper-bound": "ceiling", "lower-bound": "floor",
            "range": "range", "estimate": "estimate"}.get(t, "point")

def classify_multi_amount(obs_list):
    """Multiple distinct amounts on one edge is NOT a single phenomenon -- verified by
    reading every actual case in this dataset (see FINDINGS.md 'zero for four'). Three
    real, distinct relations hide behind the same surface signal, and Q1's flat
    observations[] list cannot tell them apart without reading the prose:
      - genuine revision over time (a figure that changed)   -> supersedes
      - a tranche + its running cumulative total              -> has_part / part_of
      - a base figure + a separate contingent/additional sum  -> qualifies
    This classifier is a heuristic on the `note` text, not a solved parser -- every
    case it labels should be read as "held for human review," same discipline as any
    other q1-flows judgment call. It exists to make the FINDING concrete with real
    numbers, not to claim the ambiguity is resolved.
    """
    notes = " | ".join((o.get("value", {}).get("note") or "").lower() for o in obs_list)
    if "cumulative total" in notes or "cumulative" in notes:
        return "has_part"
    if "earnout" in notes or "contingent" in notes or "additional consideration" in notes or "performance metric" in notes:
        return "qualifies"
    return "conflicts_with"   # default: genuine unresolved disagreement between sources on one fact

for e in edges:
    eid = e["id"]
    obs_list = e.get("observations", [])
    if not obs_list:
        continue
    amounts = [obs_amount(o) for o in obs_list if obs_amount(o) is not None]
    distinct_amounts = sorted(set(amounts))
    has_multi_amount = len(distinct_amounts) > 1 and (
        max(distinct_amounts) > min(distinct_amounts) * 1.05
    )
    multi_amount_relation = classify_multi_amount(obs_list) if has_multi_amount else None
    if has_multi_amount:
        findings_notes.append(
            f"MULTI-AMOUNT edge `{eid}`: {len(distinct_amounts)} distinct reported "
            f"amounts ({distinct_amounts}) -- classified as `{multi_amount_relation}` "
            f"(not `supersedes`; read the actual notes, see FINDINGS.md), linked "
            f"accordingly rather than marking either claim deprecated."
        )
        tally[f"multi_amount__{multi_amount_relation}"] += 1

    from_ref = node_atom_ref.get(e.get("from"))
    to_ref = node_atom_ref.get(e.get("to"))
    from_label = next((a["label"] for a in atoms if a.get("meta", {}).get("q1_node_id") == e.get("from")), e.get("from"))
    to_label = next((a["label"] for a in atoms if a.get("meta", {}).get("q1_node_id") == e.get("to")), e.get("to"))
    prev_claim_ref = None
    claim_refs_this_edge = []

    for i, o in enumerate(obs_list):
        v = o.get("value", {})
        amt = v.get("amount_usd")
        note = v.get("note", "")
        period = o.get("period", {}) or {}
        cid = atom_id("claim", f"{eid}--obs{i}")
        # FINDING: q1's `note` field is a terse fragment authored to be read beside the
        # edge's from/to (e.g. "$12B, 2021-2029"), never a self-contained sentence -- but
        # an AKM claim atom is supposed to stand alone as prose. Synthesizing a minimal
        # subject-verb-object sentence here is a stopgap, not a fix -- see FINDINGS.md.
        synthesized = f"{from_label} → {to_label}: {note}" if note else f"{from_label} → {to_label}"
        claim_label = (synthesized[:160] + "...") if len(synthesized) > 160 else synthesized
        claim = base_obj("knowledge_atom", "knowledge_atom_id", cid, claim_label or eid)
        claim.update({
            "atom_type": "claim",
            "label": claim_label or eid,
            "summary": note,
            "body": note,
            "valid_from": period.get("start"),   # trait_temporally_valid
            "valid_to": period.get("end"),
            "meta": {
                "q1_edge_id": eid,
                "q1_edge_type": e.get("type"),
                "q1_destination_category": e.get("destination_category"),
                "q1_stage": o.get("stage"),
                "q1_observation_index": i,
                # --- proposed trait_quantified (Ask 1, NOT LANDED -- used as-if) ---
                "quantity": amt,
                "quantity_unit": "USD" if amt is not None else None,
                "quantity_basis": obs_basis(o),
                "origin": ORIGIN,
            },
            "formalization_stage": "S3",
            # Only genuinely superseded claims (multi_amount_relation == "supersedes")
            # get deprecated; has_part/qualifies/conflicts_with claims all remain
            # ACTIVE, because none of those relations means the earlier claim stopped
            # being true -- see classify_multi_amount() above.
            "lifecycle_status": "deprecated" if (multi_amount_relation == "supersedes" and i < len(obs_list) - 1) else "active",
            "sources": [],
        })
        claim["meta"] = {k: v2 for k, v2 in claim["meta"].items() if v2 is not None}
        atoms.append(claim)
        claim_ref = f"knowledge_atom:{cid}"
        claim_refs_this_edge.append(claim_ref)
        tally["edge_observation->claim"] += 1

        # --- about: claim -> from/to entities (proposed predicate, NOT LANDED -- used as-if) ---
        for target_ref, tag in ((from_ref, "from"), (to_ref, "to")):
            if not target_ref:
                continue
            r = base_obj("relationship", "relationship_id",
                         rel_id(claim_ref, "about", target_ref),
                         rel_name(claim_ref, "about", target_ref))
            r.update({"source_ref": claim_ref, "target_ref": target_ref, "predicate_id": "about",
                      "qualifiers": {"role": tag}, "review_status": "unreviewed"})
            rels.append(r)
            tally["about_relationships"] += 1

        # --- link this claim to the prior observation's claim on THIS edge, using the
        #     relation classify_multi_amount() actually found -- supersedes only when
        #     it's a genuine revision; has_part when this is a cumulative-total pair;
        #     qualifies for a base+contingent-addition pair; conflicts_with when two
        #     sources simply disagree on one unresolved figure. All four are LANDED
        #     predicates already -- no proposal needed for this part of the mapping.
        if prev_claim_ref and multi_amount_relation:
            pred = multi_amount_relation
            # has_part points from the WHOLE to the PART: the later, larger (cumulative)
            # claim has_part the earlier, smaller (tranche) claim.
            src_ref, tgt_ref = (claim_ref, prev_claim_ref) if pred != "has_part" else (
                (claim_ref, prev_claim_ref) if amt and obs_amount(obs_list[i - 1]) and amt > obs_amount(obs_list[i - 1])
                else (prev_claim_ref, claim_ref)
            )
            r = base_obj("relationship", "relationship_id",
                         rel_id(src_ref, pred, tgt_ref),
                         rel_name(src_ref, pred, tgt_ref))
            r.update({"source_ref": src_ref, "target_ref": tgt_ref, "predicate_id": pred,
                      "review_status": "unreviewed",
                      "note": "Classified by migrate.py's classify_multi_amount() heuristic -- held for human review, not a solved parse."})
            rels.append(r)
            tally[f"{pred}_relationships"] += 1
        prev_claim_ref = claim_ref

        # --- the observation's source/supports/annotation triple (Ask 5 factoring) ---
        src = o.get("source", {})
        provenance_class = o.get("provenance_class")
        capture_ref = o.get("capture_ref")
        reliability = o.get("reliability")
        source_ref = get_or_make_source(src, provenance_class, capture_ref, eid, i)
        claim["sources"].append(source_ref.split(":", 1)[1])   # trait_source_backed index

        sup = base_obj("relationship", "relationship_id",
                       rel_id(source_ref, "supports", claim_ref),
                       rel_name(source_ref, "supports", claim_ref))
        sup.update({
            "source_ref": source_ref, "target_ref": claim_ref, "predicate_id": "supports",
            "evidence_class": EVIDENCE_CLASS.get(provenance_class, "published_document"),
            "evidence_strength_band": reliability_band(reliability),
            "evidence_weight": reliability,
            "review_status": "unreviewed",
        })
        rels.append(sup)
        tally["supports_relationships"] += 1

        pass_ref = get_or_make_pass(capture_ref)
        ann_id = "ann-" + slug(f"{eid}-obs{i}")[:70]
        ann = base_obj("annotation", "annotation_id", ann_id, f"extraction provenance for {cid}")
        ann.update({
            "annotation_type": "extraction_provenance",
            "target_ref": claim_ref,
            "generated_by_ref": pass_ref,
            "source_ref": source_ref,
            "justification": o.get("rationale"),
            "locator": {"quote": src.get("figure")} if src.get("figure") else None,
        })
        ann = {k: v2 for k, v2 in ann.items() if v2 is not None}
        annos.append(ann)
        tally["annotations"] += 1

    # --- funds: from-entity -> to-entity, materialized from the LATEST (current) claim ---
    if from_ref and to_ref and claim_refs_this_edge:
        latest_claim = claim_refs_this_edge[-1]
        r = base_obj("relationship", "relationship_id",
                     rel_id(from_ref, "funds", to_ref),
                     rel_name(from_ref, "funds", to_ref))
        r.update({
            "source_ref": from_ref, "target_ref": to_ref, "predicate_id": "funds",
            "qualifiers": {"materialized_from_claim_ref": latest_claim, "q1_edge_id": eid},
            "review_status": "unreviewed",
            # not evidence-bearing per the round-two brief -- no evidence_class/weight here
        })
        rels.append(r)
        tally["funds_relationships"] += 1

# ============================================================================
# 3. MEMBERSHIPS -> member_of relationships (proposed predicate, NOT LANDED -- used as-if)
# ============================================================================
for mrow in memberships:
    from_node = mrow.get("from")
    to_node = mrow.get("to")
    from_ref = node_atom_ref.get(from_node)
    to_ref = node_atom_ref.get(to_node)
    if not from_ref or not to_ref:
        findings_notes.append(f"membership `{mrow.get('id')}` references a node not found in nodes.yaml "
                               f"({from_node!r} -> {to_node!r}) -- skipped.")
        continue
    r = base_obj("relationship", "relationship_id",
                 rel_id(from_ref, "member_of", to_ref),
                 rel_name(from_ref, "member_of", to_ref))
    r.update({
        "source_ref": from_ref, "target_ref": to_ref, "predicate_id": "member_of",
        "qualifiers": {"role": mrow.get("role"), "amount_usd": mrow.get("amount_usd"),
                       "q1_source_ref": mrow.get("source_ref")},
        "review_status": "reviewed" if mrow.get("role") else "unreviewed",  # role:lead only ever set per P-02 (source explicitly says so)
    })
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

# extraction_passes needs its own list since `passes` dict maps capture_ref->ref, not the objects
pass_objs = []
seen_pass_ids = set()
for capture_ref, ref in passes.items():
    pid = ref.split(":", 1)[1]
    if pid in seen_pass_ids:
        continue
    seen_pass_ids.add(pid)
    p = base_obj("extraction_pass", "extraction_pass_id", pid, capture_ref)
    p.update({
        "pass_type": "A5", "pass_iteration": 1, "pass_mode": "blind",
        "agent_identity": "claude-session-theprojection-corpus-q1-akm-migration",
        "methodology_version": "q1-flows-pass-4 (theprojection-corpus, not the LifeOS extraction-methodology.md)",
        "source_target_ref": "source:unspecified",
    })
    pass_objs.append(p)
write_jsonl("extraction_passes.jsonl", pass_objs)

print("\n--- reconciliation ---")
for k, v in sorted(tally.items()):
    print(f"  {k}: {v}")
print(f"\n  total atoms: {len(atoms)}  sources: {len(sources)}  relationships: {len(rels)}  "
      f"annotations: {len(annos)}  extraction_passes: {len(pass_objs)}")

with open(os.path.join(OUT, "findings-notes.txt"), "w") as f:
    f.write("\n".join(findings_notes))
print(f"\n  {len(findings_notes)} structural finding(s) written to findings-notes.txt")
