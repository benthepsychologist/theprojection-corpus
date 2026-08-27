<!-- outcome block prepended on close; the brief follows unchanged below -->

outcome:   done
closed:    2026-08-27
closed-by: theprojection-corpus / agent session
artifact:  research/q1-flows/akm-tinkerspace/ (migrate.py, FINDINGS.md, five JSONL files)

**Migrated for real, findings written.** `research/q1-flows/akm-tinkerspace/migrate.py`
is a deterministic, idempotent script (mirrors pm's own
`scripts/migrate-question-ledger-to-akm.py` pattern) that reads the current
`../{nodes,edges,memberships}.yaml` (204 nodes, 86 edges, 118 memberships as of this
run) and writes `atoms.jsonl`/`sources.jsonl`/`relationships.jsonl`/
`annotations.jsonl`/`extraction_passes.jsonl` in AKM shapes. The YAML register is
untouched and stays authoritative. Full findings in
`research/q1-flows/akm-tinkerspace/FINDINGS.md` — four real structural findings, not
just "it mapped fine":

1. **"Multiple amounts on one edge" is not one phenomenon.** Four edges in the current
   register carry more than one distinct dollar figure. A naive `supersedes` treatment
   of all four turned out to be wrong 100% of the time once the actual note text was
   checked — two were tranche/cumulative-total pairs (`has_part`), one was a base price
   plus a separate contingent earnout (`qualifies`), one was genuine cross-source
   disagreement (`conflicts_with`). All three predicates are already landed; the gap is
   that Q1's flat `observations:` list gives no structural signal for which of the
   three a second amount represents — it takes reading the prose every time.
2. **Claim atoms are supposed to be self-contained prose; Q1's `note` field is a
   fragment** (e.g. `"$12B, 2021-2029"`) meant to be read beside its edge's from/to,
   not a standalone sentence. Mechanically synthesizable, but real AKM-native
   authorship would need actual sentences written at capture time.
3. **Bare entity labels destroy Q1's own entity×activity split** — 38 label collisions
   on the first run (worst case: one label covering six unrelated placeholder nodes),
   fixed in the script by appending activity/round-type, but that's a migration-script
   patch, not something the target schema provides for free.
4. **Two integrity gaps left deliberately unresolved, not papered over:**
   `provenance_class: "inference from other claims"` doesn't fit `source` at all (it's
   internal derivation, not external evidence — `derived_from` is likely the right
   home instead); every `extraction_pass.source_target_ref` in this migration is a
   placeholder that resolves to nothing, because Q1's `capture_ref` is a session-level
   marker covering many sources while the schema requires exactly one — the mirror
   image of Q1's own P-01 principle, this time on AKM's side.

`about`/`member_of`/`funds` (all proposed, none landed) and the source→supports→
annotation factoring (Ask 5) both worked exactly as pm's mapping predicted — no
surprises there. `coverage_state`'s missing home (Ask 2) was independently confirmed,
not just asserted. Findings routed back via this same INBOX close, per "wherever your
operator prefers" — pm's own INBOX and the cloud-governor round-two brief can pull
from `FINDINGS.md` directly.

---

# Experiment: migrate the Q1 flow register to the governed AKM shapes and report what breaks

from:      pm / agent session
date:      2026-08-27
kind:      request
touches:   research/q1-flows/nodes.yaml, research/q1-flows/edges.yaml, research/q1-flows/memberships.yaml
done-when: a migrated copy of the Q1 register exists in AKM shapes (tinkerspace, beside the originals — the YAML register stays authoritative until you decide otherwise), plus a findings list: what mapped cleanly, what broke, what neither side had thought of. The findings are the real deliverable — they feed the next governed-schema round.
artifact:  none (the mapping table below is the whole payload)

## What this is

Ben's directive (2026-08-27, verbatim intent): *"we don't need the governed model to
be updated before we can try to migrate Q1 and see what happens, what breaks, what we
haven't thought of. It's ungoverned tinkerspace."* The registry landed the OKG model
on 2026-08-26 (lifeos-registry commit `3fe27e0`, "reg-01-02: register the OKG model")
— four composable traits, knowledge_atom/relationship/source@1.1.0, an `answers`
predicate, and two ported kinds (`annotation`, `extraction_pass`). pm ran your Q1
register against it on paper; this brief hands you the resulting mapping so you can
run it for real.

Read-only sources of truth for the target shapes (do not edit that repo — it is
governed; anything you need changed routes through cloud-governor's INBOX):

- kinds: `/workspace/lifeos-registry/registry/io.lifeos/kind/object/canonical_object/{knowledge_atom,source,observation,relationship,annotation,extraction_pass}/`
- traits: `/workspace/lifeos-registry/registry/io.lifeos/trait/{temporally_valid,origin_tracked,source_backed,epistemic}/`
- predicate seeds: `/workspace/lifeos-registry/seeds/object/predicate/1-0-0/` (30 today)

## The mapping, as worked out on pm's side

| Q1 construct (your files) | AKM home |
| --- | --- |
| `tsmc/capital` node (entity × activity facet) | `knowledge_atom` · `atom_type: entity`; keep the `entity/activity` id as a naming convention; your evidence-driven split rule ("edge terminates at the entity until an allocation claim splits it") imports as-is |
| `kind: round` nodes | `atom_type: event` |
| a flow edge ($12B, TSMC→Arizona, 2021–2029) | **a claim atom**, not a relationship — "TSMC committed $12B…", `valid_from/valid_to` from trait temporally_valid; amount has no typed home yet (see "pending upstream") — carry it as `meta.quantity{value, unit, basis}` in the shape of the proposed `trait_quantified` |
| each entry in an edge's `observations:` list | **three objects, not one**: a `source` row (url/label/captured figure/as-of, `evidence_class` — your `provenance_class: company statement` ≈ `testimony_interested`) · a `supports` relationship source→claim carrying the evidence cluster (`evidence_class`, `evidence_strength_band`, numeric `evidence_weight` ← your `reliability`) · an `annotation` anchoring the figure in the source (locator, justification ← your `rationale`) with `generated_by_ref` → an `extraction_pass` (← your `capture_ref`, e.g. `step0-audit:…`) |
| multiple observations on one edge | multiple source+supports(+annotation) sets — no `sources[]` field exists or is needed; multiplicity lives in the edge count |
| `memberships.yaml` (`is_member_of`, `role: lead`) | relationship rows; the `member_of` predicate is **proposed upstream today, not yet landed** — use it as-if and flag it, or `meta.predicate_proposed: member_of` on a `related_to` edge, your call; role/amount ride relationship metadata |
| claim ↔ its subject entities | `about` edges (claim→entity) — also proposed-not-landed, same treatment |
| `coverage_state: measured\|aggregated\|unmeasured` | no AKM home — carry as `meta.coverage_state`; proposed upstream as a trait candidate |
| `reliability: 0.85` + required rationale | numeric `epistemic_confidence` (+ band) on atoms, numeric `evidence_weight` on evidence edges — both landed; your rationale discipline maps to the confidence-rationale idiom |
| the hand-authored q1.md page | out of scope here — this brief is about the register, not the site |

One naming caution from pm's side: by the AKM's evidential-tier line (source =
reported artifact, second-hand; observation = first-hand datum you registered), nearly
everything your files call an "observation" is a **source**. True AKM `observation`
rows would appear only where your team measured the world itself (e.g. imagery-derived
counts). Also note `observation` upstream is still 1-0-0 and measurement-coupled
(`measurement_event_id` required) — its relaxation is pending upstream, another reason
most of Q1 lands as sources.

## Pending upstream (filed with cloud-governor the same day as this brief)

`/workspace/.projections/cloud-governor/INBOX/2026-08-27-pm-akm-round-two/` asks for:
`trait_quantified` (typed amounts on claims — explicitly NOT measurement, which stays
scoped to instruments we administer) · `about`, `member_of`, `funds` predicate seeds ·
a ruling on `coverage_state` · the observation@1.1.0 disposition. Where the migration
needs one of these, use the proposed shape and mark it — your breakage report on
exactly those points is the evidence that round needs.

## What you already have that should survive migration untouched

Your own disciplines are the point, not casualties: "never fabricate a figure or URL"
(unmeasured, never silently estimated) · P-01 cardinality (never force single-value
onto a genuinely-multiple field) · yaml.safe_load validation on write · the step-0
capture discipline (hash-bound source capture). The AKM factoring gives each of these
a first-class home (coverage_state, list-valued fields, schema validation,
extraction_pass respectively) — if any of them DOESN'T survive the mapping, that is a
top-of-list finding.

Free prose: pm found this while workshopping its research/inquiry hierarchy against
your Q1 page as prior art (your q1–q4 namespace maps 1:1 onto a line-of-inquiry
carrying four watches, for what it's worth). The experiment is yours to sequence;
nothing in pm blocks on it. Findings can come back as a brief to pm's INBOX
(/workspace/pm/INBOX.md is the contract) or wherever your operator prefers.
