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

Unchanged from the YAML register. No AKM home exists for this today —
confirmed empirically by the AKM migration experiment
(`research/q1-flows/akm-tinkerspace/FINDINGS.md`) and is the live subject of
`cloud-governor/INBOX/2026-08-27-pm-akm-round-two/`'s Ask 2 (a ruling
request, not yet answered as of this file's writing). If that round lands a
`coverage_state`-equivalent trait, this file's convention retires in favor
of it.

## What does NOT live here

`cut:core-buildout` (the named consolidation roster) is **not** a local
vocabulary term and does not appear on any atom in this graph. R-16 rules
boundaries are filters over the map, never classification baked into it —
`filters/cut-core-buildout.yaml` stays exactly as it is, unchanged, and
applies to this graph by matching each atom's `meta.entity_slug` (see
`build_graph.py`) against its own bare-entity membership list. See
`research/q1-flows/graph/README.md` for how filter application works
against the graph.
