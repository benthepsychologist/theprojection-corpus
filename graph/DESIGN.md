# graph/ — the corpus-wide knowledge graph

**Status:** design, ruled 2026-08-27, read-before-impl. **Rulings this rests on** (Ben, same day): one corpus-wide graph with news as a different cut, not a different graph · digest bullets enter at S1 · `interp.yaml` scenarios are propositions · entity reconciliation is step one · `graph/` lives at repo root now. **Upstream it aligns to:** pm's inquiry ladder (ratified 2026-08-26, `pm/docs/design.md` §37g and the beat proposal Part 3/4) and cloud-governor's `reg-02` draft (`akm-extension-design.md`, 2026-08-27). This repo is a copier of both; where they haven't landed we use the ruled shape as-if and mark it.

What's already here: the Q1 money-flow graph (86 flows, 204 entity/event atoms), 16 financing hypotheses, 28 q3 facilities — seeded and ported 2026-08-27, `README.md` and `schemas/q1-local-vocab.md` in this directory. This document is what turns that into the whole corpus.

---

## 1. One graph, one register, `loi` as a facet

The ratification rules it directly: *"Each line of inquiry has ONE graph… not nested under any tier… one register with an `loi` facet — axes are facets, not separate graph files per line."* The news layer is not a second migration into a second graph. It is the same graph, where the atoms carry `loi` = which radar question, `lens` = which beat, `thread` = which watch — and the evidence differs in kind (published items are sources; our own coverage findings are observations).

Why it holds for this repo in particular, beyond the ruling: research **q1** ("Where is the money going?") and radar **Q2** ("Where is the money going?") are the same question — the site page says so. The research graph and the attention layer were never two corpora; they are one line's investigation arm and its watch arm, and the ladder says those share one graph by construction.

The honest caveat: one graph, **nine migrations**. The attention layer is nine distinct source shapes, each needing its own F0 parser. §8 specifies each.

## 2. Two planes: spine and graph

| plane | holds | truth-state? | lives in |
| --- | --- | --- | --- |
| **spine** | lines, watches, investigations, deliverables, work items — the work | no | `attention/threads.yaml`, `attention/radar.md` (structure), skills, runs |
| **graph** | propositions and evidence — questions, claims (accepted / derived / hypothesized), sources, observations, and the relationships between them | yes (or pending) | `graph/*.jsonl` |
| **composition** | the read: digest narratives, radar working-note syntheses, `actor-doing.yaml`, `interp.yaml` mechanisms | no — frames, not propositions | where they are today; they cite *into* the graph and never write atoms |

The 2026-08-27 composition ruling: **the graph holds propositions only** (a proposition has a truth-state — settled, computed, or pending). Interpretations are frames and stay out, carrying a bibliography of atom ids. The mechanization discipline (`AGENTS.md` §6.1) is why this line is load-bearing: a graph of propositions is F0-maintainable end to end; one atom that only a model can judge makes it a mixed-trust store.

## 3. The ladder, on this repo's existing objects

Ben's own fit-test (2026-08-26): *"theprojection-site's `thread_kind: meta|project|story` with `resolved` vs `retired` terminals IS the ladder; the radar's `mode: answer|monitor|both` is the tier-2 fork latent."* So:

| ladder tier | this repo's object | plane | note |
| --- | --- | --- | --- |
| `line_of_inquiry` (work_stream; never finishes) | radar Q1–Q7 | spine; root is a `question` atom | `loi` facet value = the Q slug (`q1`…`q7`) |
| `watch` (ops_stream; completes-or-continues; retired by the line) | `kind: story` thread · `status: open → retired` | spine | `threads.yaml` row + `artifacts/threads/<slug>.md` timeline; radar `mode: monitor` |
| `investigation` (project; bounded; closes) | `kind: project` thread · `→ resolved`; research passes q1–q4 | spine | radar `mode: answer` |
| sub-line container | `kind: meta` thread with `parent` children | spine | grouping, not a tier of its own |
| `deliverable` (the answer) | `capital-context` readings · `actor-doing` · radar syntheses · site pages | **split** — readings are claims (graph); prose syntheses are composition | |
| `work_item: evidence_collect` | `/daily` sweep · critic pass · research pass | spine → each run is an `extraction_pass` | |
| `work_item: experiment` | an expectation's `due` + `what_confirms` | spine (the check) → graph (the hypothesis, its `extraction_review`) | already built |

**Threads are spine, not atoms.** A thread has no truth-state ("Power Buildout" isn't true or false). `threads.yaml` stays the watch ledger, unchanged; graph atoms carry `meta.thread`. `radar.md` stays as spine (the seven questions) plus composition (the working notes); only the seven `question` atoms enter the graph.

## 4. Atom types and what produces each

| `atom_type` | produced from | count (est.) | posture |
| --- | --- | --- | --- |
| `entity` | reconciled union of `board.yaml` orgs+houses, `watchlist.yaml` orgs+people, q1 entities, q3 facilities | ~350 | — |
| `concept` | `watchlist.yaml` themes + conditions | ~40 | — |
| `event` | q1 rounds; resolved `hit` expectations (the thing happened) | ~45 | — |
| `question` | radar Q1–Q7 | 7 | `epistemic_status: undecided` for life (pm's pattern) |
| `claim` — accepted | q1 flows · bundle `provenance.yaml` dims · `capital-context` readings · timeline entries (S2) · digest bullets (S1) | ~4,500 in 60 days, most S1 | `accepted` / `extraction` |
| `claim` — derived | arithmetic over other claims | few | `accepted` / `inference` / `inference_basis` |
| `claim` — hypothesized | `upcoming.yaml` (70) · `interp.yaml` scenarios | ~100 | `hypothesized` → `accepted`/`rejected`; `defeat_conditions` required |
| `source` | every cited URL, deduped on (url, label) | ~2,000 | `evidence_class` from `outlet-credibility.yaml` band (§10.2) |
| `observation` | critic-log misses; page-diff hits (later, via cloud-researcher) | ~50 | `observation_type: absence`, `evidence_class: absence_of_evidence` — `observation@1.1.0` as ruled in reg-02 §6 |

## 5. Facets — meta, never parents

Everything cross-cutting is a facet (the ratification's own lesson, "learned twice"). All in `meta`, none a relationship, none an atom:

`loi` (q1–q7) · `lens` (ai / global-capital / mental-health / world-news) · `thread` (slug list — a bullet can carry several) · `axis` (the digest's display section) · `genre` · `pocket` · `sphere` · `weight` · `digest` (source file, for S1 claims) · `entity_slug` (canonical, §8.1) · `coverage_state` · `flow_type` / `destination_category` (q1's own, `schemas/q1-local-vocab.md`).

`cut:core-buildout` is a filter over `entity_slug`, unchanged (R-16).

## 6. Predicates

**In use, all landed or ruled-landing:** `about` (claim→entity/event/concept) · `supports` (source→claim, carries the evidence cluster) · `member_of` (entity→round) · `funds` (entity→entity, materialized) · `has_part` (cumulative totals) · `qualifies` (contingent additions) · `conflicts_with` (source disagreement) · `supersedes` (genuine revision) · `derived_from` (arithmetic) · `answers` (claim→question; landed) · `related_to` + `qualifiers.role` (the stopgap below).

**Gaps — round-four brief, filed alongside implementation, `related_to`+role used as-if until then:**
- `holds` / `held_by` — board houses↔orgs (`held_by: andy-jassy`, `holdings: [...]`)
- `operates` / `owns` / `leases` — q3 facility roles (already flagged in the q3 port)
- a claim→claim aboutness — `interp` scenarios are *about* the S1 claim they interpret; `about`'s allowed targets are entity/event/concept. Carried as `meta.interprets` until ruled.

**Explicitly not used:** `informed_by` (the judgment edge — composition-layer behaviour), `encompasses` (a learning-practice predicate; irrelevant here), `synthesis`/`plausible` epistemic values.

## 7. The curation funnel is `formalization_stage`

AKM's ladder, verbatim from the atom schema: S0 unprocessed · S1 titled/tagged, enough to re-find · S2 key claim identified, linked · S3 typed, provenance explicit · S4 epistemic status assessed, maintained — *"most material should NOT advance past S1."* This repo's pipeline already is that funnel:

| stage | this repo | enters graph? |
| --- | --- | --- |
| S0 | `world-news.yaml` candidate (126/day) | **no** — buffer; enters only on promotion |
| S1 | digest bullet with `<!-- k: t= e= axis= -->` | yes (ruled) |
| S2 | thread timeline entry (`artifacts/threads/*.md`) | yes — the *same atom*, stage bumped |
| S3 | q1 flow claim · bundle claim with `sources[]` + reliability | yes |
| S4 | resolved expectation · radar working note's subject claim | yes (the claim); the note itself is composition |

A bullet that gets promoted to a timeline is one atom at S2, not two atoms. Dedupe key: `slugify(bold-lead[:50])` + date + lens — the key `interp.yaml` already uses, so the convention is load-bearing today, not invented here.

## 8. Migration spec — per source, implementable

Every ingester: its own script in `graph/ingest/`, F0, idempotent (guards on ids; re-run is a byte-identical no-op — proven by md5 diff, the standard set by `port_hypotheses_q3.py`), one `extraction_pass` per run with `source_target_refs` (list, per reg-02 §5), validates every JSONL file on write. None fetches or classifies a source — that's the `add.py` seam and stays cloud-researcher's (`cloud-researcher/INBOX/2026-08-27-…verify-kit…`).

### 8.1 Entity reconciliation — step one, F4 once, then F0

**Problem.** Three slug vocabularies overlap and disagree: `board.yaml` (`amazon-aws`, `andy-jassy`), `watchlist.yaml` (`amazon`, `elon-musk`), q1 (`amazon/capital`, bare `Amazon`), q3 (facility names). **Everything else depends on one entity layer.**

**Method.**
1. F0: extract every slug/name from all four sources into a candidate table with provenance.
2. F0: exact-match and normalized-match (lowercase, strip `-aws`/`-inc`/facet suffixes) to propose clusters.
3. F4, one sitting: Ben reviews the proposed clusters — is `amazon-aws` (a board kingdom with a house) the same entity as watchlist `amazon`? Rule each ambiguous one. Output: `graph/schemas/entity-crosswalk.yaml` — `canonical_slug: [every old slug]`.
4. F0: rewrite every existing atom's `meta.entity_slug` and every `about`/`funds`/`member_of`/`related_to` target through the crosswalk; `aliases` on each entity atom carries every old slug so nothing is lost.

**Canonical slug precedence:** `board.yaml` slug where the entity is on the board (it's the curated actor layer) → else `watchlist.yaml` slug → else q1 bare-entity slug → else facility name slug. `houses` are person entities; `holdings`/`held_by` become `related_to`+role until `holds` lands.

**Done when:** one `entity_slug` per real-world entity across the whole graph; `cut:core-buildout` still applies by slug and yields the same member set it did before.

### 8.2 Radar questions → 7 `question` atoms

`radar.md` headers → `kat-q-q1`…`kat-q-q7`. Fields: `label` (the question), `meta.mode`, `meta.lens`, `meta.loi = q<n>`, `epistemic_status: undecided`, `formalization_stage: S2`. Working notes are composition — not ingested. `answers` edges arrive later from investigation deliverables (mode `answer`/`both` questions); monitor-mode questions stay un-answered by design, which is correct.

### 8.3 Remaining expectations → 54 hypothesis claims

`port_hypotheses_q3.py`'s mapping, filter widened from financing threads to all. Two normalizations on the way (§10.3): `evidence` as a URL list (1 case) → real `source` rows + `supports`; `outcome_note` where `evidence` is absent → the annotation's `justification`. `passed-silent` → `rejected` with the `extraction_review` carrying the grace-sweep record.

### 8.4 Bundle claims → ~800 claims (124 nodes × ~7 dims)

`artifacts/bundles/<node>-node/provenance.yaml` is what `build_claims()` actually reads and is already claim-shaped: per dim (`posture`, `capital.{available,operating,deployed,in,out}`, `optionality`, `gravity`) a `{value, basis, sources[]}` block. Per dim → one claim: `label` = dim, `body` = value prose, `summary` = basis, `about` → the entity, one `source` + `supports` per `sources[]` entry (`confidence: high/med/low` → band; `evidence_class` from §10.2), `meta.dimension`, `meta.bundle_asof`. **Quantities stay prose** ("~$263B commandable") — typed-number extraction from these is an F1 step later, not promised here. `board.yaml`'s inlined axis prose is the same data denormalized; after this step it is redundant and retires from `board.yaml` in a follow-up, not now.

**Site consequence, noted not built:** `build_claims()` can read these atoms instead of the bundles — the clickability proposal's data source, unchanged in shape.

### 8.5 `capital-context.yaml` readings → 5 claims

`readings.<key>` → one claim each: `body` = value, `summary` = basis, `meta.loi = q7`, `meta.reading_key`, one `source`+`supports` per `sources[]` row. `framing` is steering (governance plane) — not ingested. `/week` 4b keeps rewriting the YAML; the ingester re-runs after it and the claim's `supersedes` chain records each refresh.

### 8.6 Thread timelines → S2 claims (103 files)

Shape is regular: `## <date> — <headline>` sections, each bullet `- **<bold lead>** <prose> ([Outlet](url), …) ⟨<verb> <date>⟩`. Parser: section date + bold lead + trailing links + the `⟨verb date⟩` tag. Per bullet → find the S1 atom by the §7 dedupe key; if found, bump `formalization_stage` to S2 and add `meta.timeline = <thread>`; else create at S2 (steer-authored or pre-digest entries). Links → sources + `supports`. `⟨verb date⟩` → the `extraction_pass` (one per distinct verb+date, `source_target_refs` = that run's sources). 💡/⚠️ prefixes → `meta.marker`.

### 8.7 Digest bullets → S1 claims (ruled in)

Parser exists: `render_read.py:305` (`parse_digest()`) yields bullet text + the `k:` tag dict. Per bullet → one claim: `label`/`body` = bullet text minus the link parenthetical (already a sentence — bold lead + support; P-03 satisfied by construction), `formalization_stage: S1`, `meta.thread` = `t=` list, `meta.axis`, `meta.digest` = file, `meta.lens`, `meta.loi` via thread→radar mapping (§12.1), `about` → each `e=` entity, links → sources + `supports` with `evidence_class` from the outlet band. Id = the §7 key. Volume ≈ 15 × 4 lenses/day; JSONL until it isn't, SQLite then. The digest *file* is untouched — it's the read; the graph holds its facts.

### 8.8 `interp.yaml` scenarios → hypothesis claims (ruled propositions)

Per entry, per `scenarios[i]`: a claim with `body` = `direction`, `defeat_conditions` = `why`, `meta.precedent`, `epistemic_status: hypothesized`, `meta.interprets` = the parent S1 claim id (same key — the file is keyed on it already), `about` → the parent's entities, `meta.loi = q7`. `mechanism` and `context_note` are frames — **not ingested**; they remain in the file, which becomes composition with a bibliography (the parent id it already carries). Fix the unenforced length caps on the way (§10.4).

### 8.9 Critic-log misses → observations

`coverage-log.md` entries → per `**Missed:**` item, one `observation`: `observation_type: absence`, `evidence_class: absence_of_evidence` (we looked and it wasn't there) or `own_experiment` (a re-fetch we ran), `occurred_at` = the finalized date, `meta.lens`, `meta.benchmark`, `meta.disposition` (filed-to-thread / unverifiable). The **Map effect** line names the claim it produced — link `supports` from the observation to that claim where the claim exists. Uses `observation@1.1.0` as ruled (reg-02 §6).

## 9. What stays out, and why

| stays | why |
| --- | --- |
| `threads.yaml`, `radar.md` structure | spine — work objects, no truth-state |
| digest narratives, radar working notes, `actor-doing.yaml`, `interp` mechanisms, `coverage-log` prose | composition — frames; cite into the graph via the `k:` tags and bullet keys that already exist |
| `world-news.yaml` | S0 buffer; the graph holds curated propositions, not the sweep (same rule q1 already follows) |
| `watchlist.yaml` `terms`, `sources/*.yaml`, `flash.yaml` | sweep and rail config |
| `board.yaml` ranks/axes/postures/genres definitions | facet vocabulary; the *values* ride atoms as facets, the *definitions* stay here |

## 10. Defects to fix on the way — all this repo's, all F0

1. **Genre drift.** Five thread genres in use (`policy-fight`, `trade-war`, `product-race`, `political-risk`, `market-intervention`) are undefined in `board.yaml`'s 14. Define or remap before `genre` becomes a facet.
2. **`sources/outlet-credibility.yaml` is 83 % dead bytes.** Six duplicate top-level `domains:` keys; `yaml.safe_load` keeps only the last. Append-instead-of-regenerate in whatever builds it. Regenerate once, fix the builder. This file is the `reliability_tier`/`evidence_class` table every news `source` atom needs, so it's on the critical path.
3. **`upcoming.yaml` `evidence` is untyped** (string ×14, URL list ×1, `outcome_note` ×1). Normalize in the 8.3 ingester; propose one shape for the YAML itself.
4. **`interp.yaml` length caps** are documented as enforced and visibly aren't (`mechanism` at ~230 chars against a 200 cap). Enforce or amend the doc.

## 11. Sequence and done-when

| # | step | F-rung | done when |
| --- | --- | --- | --- |
| 1 | entity reconciliation (§8.1) | F0 propose · **F4 review once** · F0 apply | one canonical slug per entity; crosswalk file exists; `cut:core-buildout` yields the same members |
| 2 | radar questions (§8.2) | F0 | 7 `question` atoms; every existing atom's `meta.loi` resolves to one |
| 3 | remaining expectations (§8.3) | F0 | 70/70 in graph; 0 with untyped evidence |
| 4 | bundle claims (§8.4) | F0 | 124 nodes × dims; `build_claims()` output reproducible from atoms (parity check, not cutover) |
| 5 | `capital-context` (§8.5) | F0 | 5 claims, wired into `/week` 4b |
| 6 | timelines (§8.6) | F0 | 103 files parsed; every `⟨verb date⟩` is an `extraction_pass` |
| 7 | digest bullets (§8.7) | F0 | every `k:`-tagged bullet since the earliest digest is an S1 atom; timeline-promoted ones are S2, not duplicated |
| 8 | interp scenarios (§8.8) | F0 | every scenario is a hypothesis with a defeat condition |
| 9 | critic observations (§8.9) | F0 | every `**Missed:**` is an observation |
| — | §10 defects | F0 | interleaved where each blocks a step (10.2 before 7) |

Steps 2–9 are independent of each other once 1 lands; run in order for reviewability, not dependency. **Nothing here cuts a YAML over.** `threads.yaml`, `upcoming.yaml`, `board.yaml`, `capital-context.yaml` all remain the operational files `/daily` and `/week` read; the graph is fed *from* them. Retiring any of them as source-of-truth is a later, separate decision, after the graph has proven itself as `build_claims()`'s input (step 4's parity check is the evidence for that call).

## 12. Open items and upstream asks

1. **thread → `loi` mapping.** `threads.yaml` has `lens`, not a radar-question pointer. Needed for `meta.loi` on S1/S2 claims. Proposal: a `loi:` field on each thread (F4 once, 103 rows, mostly obvious from `lens` + `genre`); until then `loi` derives from lens (ai→q1/q5, global-capital→q7, mental-health→q3/q4/q6, world-news→none) and is marked derived.
2. **Round-four brief** to cloud-governor: `holds`/`held_by`, `operates`/`owns`/`leases`, and a claim→claim aboutness for interpretation-of. Filed when step 1 gives the first real `held_by` rows to cite.
3. **`board.yaml` axis-prose retirement** after step 4 — a follow-up ruling, not this design.
4. **cloud-researcher verify seam** — unchanged; every ingester consumes already-cited material. When the verify kit lands, only what fills `evidence_class`/reliability changes.
5. **SQLite threshold** — no number set; JSONL until a `/week` run's ingest or the site build is measurably slow.
