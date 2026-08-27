# Q1's local vocabulary — divergent from AKM, explicitly marked

Mirrors pm's `schemas/akm-proposed/` convention: this repo is ungoverned and
a *copier* of `lifeos-registry`'s shapes, not a subject of them. Where Q1
needs a classification AKM has no home for, it gets one here, versioned and
marked local, retired the moment an equivalent lands upstream. Nothing in
this file is a relationship or a predicate — see `research/README.md` and
R-16 (`filters/cut-core-buildout.yaml`'s own header) for why: **the map
stays classification-free.** These are `meta` fields on claim/entity atoms,
never graph edges.

## `meta.flow_type` — carried over from the YAML register's `type` field unchanged

`equity` · `debt` · `asset purchase` · `capex` · `capacity/service payment` ·
`grant / subsidy` · `prepayment` · `non-cash consideration`

**Proposed addition — `guarantee`, pending Ben's confirmation.** Two edges
(Nvidia's $500B compute-financing-platforms commitment, Nvidia's $105B
OpenAI/Ohio residual-value guarantee) are currently typed `equity`, which
they are not — a guarantee is a contingent liability, not a capital
contribution. Applied provisionally in this migration (both edges' claim
atoms carry `meta.flow_type: guarantee` going forward) so the pipeline isn't
blocked on a ruling; flagged here exactly as the research pass flagged it
inline in the YAML. Revert both to `equity` if the ruling goes the other way.

**Open, not resolved provisionally — `asset purchase`'s scope.** Originally
meant for EPC/construction contracts (e.g. TSMC's fab buildout), now also
carrying two whole-company M&A deals (nVent/Maverick Power,
Infineon/C2i Semiconductors). Left as `asset purchase` in this migration,
unchanged from the YAML — this one needs an actual decision (does M&A get
its own `flow_type`, e.g. `acquisition`?) rather than a default I can pick
for you the way `guarantee` was a clean, obvious gap-fill.

## `meta.destination_category` — carried over from the YAML register unchanged

`land, shell & materials` · `financing itself` · `memory & storage` ·
`compute silicon & systems` · `power infrastructure` ·
`purchased compute capacity (services)` · `networking & optics` ·
`n/a — financing`

**Proposed addition — `intellectual property / licensing`, pending Ben's
confirmation.** Poolside's Model Factory training-pipeline license (Nvidia's
$6B deal) has no destination category that fits — it landed in
`other/unallocated` in the YAML. Applied provisionally here as its own
category (`intellectual property / licensing`) rather than left unallocated,
since it's a real, nameable kind of spend distinct from every existing
category and a second IP/license deal would need the same home. Revert to
`n/a — financing` (or fold into another category) if the ruling goes
differently.

## `meta.coverage_state` — measured / aggregated / unmeasured

Unchanged from the YAML register. **Ruled 2026-08-27 by cloud-governor's
`reg-02` draft (`akm-extension-design.md` §7): stays in `meta`, never a
trait** — one kind, nothing to repeat across kinds, so the §5.2 trait test
fails. What this file already had is the ruled shape. Closed.

## Quantities — NOT local vocab; ruled inline on `knowledge_atom` (reg-02 §3)

`quantity` / `quantity_unit` / `quantity_lower` / `quantity_upper` /
`quantity_basis` are **top-level properties on claim atoms**, per reg-02 —
not a trait (refused: at one kind there's no cross-kind repetition to avoid)
and not `meta`. `align_reg02.py` hoisted them out of `meta` on 2026-08-27;
`add.py` writes them top-level. Listed here only so nobody puts them back in
`meta` — they are governed shape, not local vocabulary.

## `extraction_pass.source_target_refs` — the ruled shape, adopted (reg-02 §5)

Our round-three brief proposed keeping `source_target_ref` optional beside a
new `source_target_refs` with `anyOf` requiring one. **Refused as shaped:
`anyOf` is a forbidden keyword in the registrar profile.** The ruled 1.1.0 is
simpler — `source_target_refs` is the required array, the singular field is
dropped, and side-by-side versioning keeps 1.0.0 records valid. Adopted
in place: every pass in this graph carries the list (`align_reg02.py`),
`add.py` writes only the list.

**Formally landed, confirmed 2026-08-27** (cloud-governor's disposition,
`INBOX/2026-08-27-cloud-governor-akm-round-three-disposition.md`, now
`INBOX/done/`): `extraction_pass@1.1.0` registered exactly as described
above — no local divergence remains on this field. One thing the
disposition flagged worth carrying here: `relationship.predicate_id` is a
declared foreign key **never resolved at validation time** upstream — a
relationship naming an unregistered predicate would validate cleanly
there. `graph/validate.py` now checks this locally (a `KNOWN_PREDICATES`
whitelist), since nothing else does.

## What does NOT live here

`cut:core-buildout` (the named consolidation roster) is **not** a local
vocabulary term and does not appear on any atom in this graph. R-16 rules
boundaries are filters over the map, never classification baked into it —
`filters/cut-core-buildout.yaml` stays exactly as it is, unchanged, and
applies to this graph by matching each atom's `meta.entity_slug` (see
`build_graph.py`) against its own bare-entity membership list. See
`graph/README.md` for how filter application works
against the graph.
