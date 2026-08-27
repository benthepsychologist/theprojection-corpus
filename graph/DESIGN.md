# graph/ — the corpus-wide knowledge graph

**Status:** design, ruled 2026-08-27, **revised same day after a fine-toothed review** (revisions marked ✎), read-before-impl. **Rulings this rests on** (Ben): one corpus-wide graph with news as a different cut, not a different graph · digest bullets enter at S1 · `interp.yaml` scenarios are propositions · entity reconciliation is step one · `graph/` lives at repo root. **Upstream it aligns to:** pm's inquiry ladder (ratified 2026-08-26, `pm/docs/design.md` §37g and the beat proposal Part 3/4) and cloud-governor's `reg-02` draft (`akm-extension-design.md`, 2026-08-27). This repo is a copier of both; where they haven't landed we use the ruled shape as-if and mark it.

What's already here: the Q1 money-flow graph (86 flows, 204 entity/event atoms), 16 financing hypotheses, 28 q3 facilities — seeded and ported 2026-08-27, `README.md` and `schemas/q1-local-vocab.md` in this directory. This document turns that into the whole corpus. **Appendix A lists everything that leaves this repo for cloud-researcher.**

---

## 1. One graph, one register, `loi` as a facet

The ratification rules it directly: *"Each line of inquiry has ONE graph… not nested under any tier… one register with an `loi` facet — axes are facets, not separate graph files per line."* The news layer is not a second migration into a second graph. It is the same graph, where the atoms carry `loi` = which radar question, `lens` = which beat, `thread` = which watch — and the evidence differs in kind.

Why it holds for this repo in particular: research **q1** ("Where is the money going?") and radar **Q2** ("Where is the money going?") are the same question — the site page says so. The research graph and the attention layer were never two corpora; they are one line's investigation arm and its watch arm, and the ladder says those share one graph by construction.

✎ **A naming trap, stated once so it isn't stepped on:** research `q1`–`q4` and radar `Q1`–`Q7` are different namespaces. The `loi` facet value is always the **radar** slug. Every existing q1-flows claim gets `loi: q2`, not `q1`.

The honest caveat: one graph, **nine migrations**. The attention layer is nine source shapes, each needing its own F0 parser. §8 specifies each.

## 2. Two planes: spine and graph

| plane | holds | truth-state? | lives in |
| --- | --- | --- | --- |
| **spine** | lines, watches, investigations, deliverables, work items — the work | no | `attention/threads.yaml`, `attention/radar.md` (structure), skills, runs |
| **graph** | propositions and evidence — questions, claims (accepted / derived / hypothesized), sources, and the relationships between them | yes (or pending) | `graph/*.jsonl` |
| **composition** | the read: digest narratives, radar working-note syntheses, `actor-doing.yaml`, `interp.yaml` mechanisms | no — frames, not propositions | where they are today; they cite *into* the graph and never write atoms |

The 2026-08-27 composition ruling: **the graph holds propositions only** (a proposition has a truth-state — settled, computed, or pending). Interpretations are frames and stay out, carrying a bibliography of atom ids. The mechanization discipline (`AGENTS.md` §6.1) is why this line is load-bearing: a graph of propositions is F0-maintainable end to end; one atom only a model can judge makes it a mixed-trust store.

## 3. The ladder, on this repo's existing objects

Ben's own fit-test (2026-08-26): *"theprojection-site's `thread_kind: meta|project|story` with `resolved` vs `retired` terminals IS the ladder; the radar's `mode: answer|monitor|both` is the tier-2 fork latent."*

| ladder tier | this repo's object | plane | note |
| --- | --- | --- | --- |
| `line_of_inquiry` (work_stream; never finishes) | radar Q1–Q7 | spine; root is a `question` atom | `loi` = the Q slug |
| `watch` (ops_stream; completes-or-continues; retired by the line) | `kind: story` thread · `open → retired` | spine | `threads.yaml` row + `artifacts/threads/<slug>.md`; radar `mode: monitor` |
| `investigation` (project; bounded; closes) | `kind: project` thread · `→ resolved`; research passes | spine | radar `mode: answer` |
| ✎ nesting within tier 2 | `kind: meta` thread with `parent` children | spine | **not a tier.** The ratification allows nesting *within* a tier ("nestable with sub-steps"); a meta thread is a watch that contains watches. `parent` stays a spine field. If a meta thread turns out to behave like a line (it never retires, it spawns investigations), that's a promotion to tier 1 — a `/week` steer call, not schema. |
| `deliverable` (the answer) | `capital-context` readings · `actor-doing` · radar syntheses · site pages | **split** — readings are claims (graph); prose syntheses are composition | |
| `work_item: evidence_collect` | `/daily` sweep · critic pass · research pass | spine → each run is an `extraction_pass` | |
| `work_item: experiment` | an expectation's `due` + `what_confirms` | spine (the check) → graph (the hypothesis, its `extraction_review`) | built |

**Threads are spine, not atoms.** A thread has no truth-state. `threads.yaml` stays the watch ledger, unchanged; graph atoms carry `meta.thread`. `radar.md` stays as spine plus composition; only the seven `question` atoms enter the graph.

## 4. Atom types and what produces each

| `atom_type` | produced from | count (est.) | posture |
| --- | --- | --- | --- |
| `entity` | reconciled union of `board.yaml` orgs+houses, `watchlist.yaml` orgs+people, q1 entities (§8.1 — canonical + facet atoms), q3 facilities | ~350 | — |
| ✎ `concept` | **none in this design.** Watchlist `themes`/`conditions` are sweep terms (config), board `genres`/`pockets`/`spheres` are facets. A concept atom earns existence only when a claim needs to be `about` it and no entity fits — none identified yet | 0 | — |
| ✎ `event` | q1 rounds and financing platforms **only**. A resolved expectation is an accepted claim ("X happened on D"), not a second event atom — one object per fact | ~30 | — |
| `question` | radar Q1–Q7 | 7 | `undecided` for life (pm's pattern) |
| `claim` — accepted | q1 flows · bundle dims · `capital-context` readings · timeline entries (S2) · digest bullets (S1) | ~4,500 / 60 days, most S1 | `accepted` / `extraction` |
| `claim` — derived | arithmetic over other claims | few | `accepted` / `inference` / `inference_basis` |
| `claim` — hypothesized | `upcoming.yaml` (70) · `interp.yaml` scenarios | ~100 | `hypothesized` → `accepted`/`rejected`; `defeat_conditions` required; `inference_basis` = what it extrapolates from |
| ✎ `source` | every cited URL, deduped on URL | **~8,000** (≈2 links/bullet × 3,600 bullets + bundles + q1) — dedupe on URL is load-bearing, not a nicety | `evidence_class` from the outlet band (§10.2, Appendix A) |
| ✎ `observation` | **none in this design.** Critic-log misses are process facts about *our* coverage, not first-hand data about the world — they are `extraction_review` annotations (§8.9), not observations. Real observations (page-diff hits, first-hand facility measurement) arrive via cloud-researcher — Appendix A | 0 today | — |

## 5. Facets — meta, never parents ✎ split by carrier

Everything cross-cutting is a facet (the ratification's own lesson, "learned twice"). All in `meta`, none a relationship, none an atom. **Which object carries which:**

| carrier | facets |
| --- | --- |
| claim atoms | `loi` (list — a thread can serve Q1 *and* Q5) · `lens` (list — a cross-posted bullet is one atom) · `thread` (list) · `axis` · `digest` · `stage` (via `formalization_stage`) · `coverage_state` · `flow_type` / `destination_category` (q1's own) |
| entity atoms | `entity_slug` (canonical) · `pocket` · `sphere` · `rank` · `coverage_state` · `control_cut` (q3) |
| spine (threads.yaml) — **not** copied onto atoms | `genre` · `weight` · `parent` · `terms` |

`cut:core-buildout` is a filter over `entity_slug`, unchanged (R-16).

## 6. Predicates

**In use, all landed or ruled-landing:** `about` (claim→entity/event) · `supports` (source→claim; the evidence cluster) · `member_of` (entity→round) · `funds` (entity→entity, materialized) · `has_part` / `part_of` (cumulative totals; ✎ and canonical-entity → facet-entity, §8.1) · `qualifies` · `conflicts_with` · `supersedes` · `derived_from` · `answers` (claim→question; landed) · `related_to` + `qualifiers.role` (stopgap).

✎ **Hypothesis ancestry needs no predicate.** A scenario that extrapolates from a fact, or an expectation logged from a report, records its ancestry in `inference_basis` — the `epistemic` trait's own field for exactly this ("its inferential ancestry"). The earlier draft's "claim→claim aboutness" gap is withdrawn; `informed_by` stays unused.

**Gaps — round-four brief, `related_to`+role as-if until then:** `holds` / `held_by` (board houses↔orgs) · `operates` / `owns` / `leases` (q3).

**Explicitly not used:** `informed_by`, `encompasses`, `synthesis`/`plausible`.

## 7. The curation funnel is `formalization_stage`

AKM's ladder, from the atom schema: S0 unprocessed · S1 titled/tagged · S2 key claim identified, linked · S3 typed, provenance explicit · S4 epistemic status assessed, maintained — *"most material should NOT advance past S1."* This repo already runs that funnel:

| stage | this repo | enters graph? |
| --- | --- | --- |
| S0 | `world-news.yaml` candidate | **no** — buffer; enters on promotion |
| S1 | digest bullet with `<!-- k: t= e= axis= -->` | yes (ruled) |
| S2 | thread timeline entry | yes — the *same atom*, stage bumped |
| S3 | q1 flow · bundle claim with `sources[]` + reliability | yes |
| ✎ S4 | a claim under active maintenance with an assessed status: resolved expectations, `capital-context` readings (weekly refresh), bundle claims (`/week` step 4) | yes |

✎ **Dedupe key = `slugify(bold-lead[:50])` + `date`.** Lens is *not* in the key: a bullet cross-posted to two lens digests with identical lead is one atom with `lens: [a, b]`; two lenses writing different leads about one event are two S1 claims, honestly. The key is what `interp.yaml` already uses, so the convention is load-bearing today. The lead is taken after stripping the ≤6-char emoji prefix `render_read.py`'s regex already allows.

## 8. Migration spec — per source, implementable

Every ingester: its own script in `graph/ingest/`, F0, idempotent — keyed on content ids so a re-run is a byte-identical no-op (proven by md5 diff, the standard `port_hypotheses_q3.py` set) **except** where a source has a refresh cadence (§8.4, §8.5): there, same `as_of` → no-op, new `as_of` → new atom + `supersedes`, old atom `deprecated`. One `extraction_pass` per run, `source_target_refs` (list, reg-02 §5). ✎ **Ingesters may look up a pre-computed classification (the outlet band table); they never fetch, score, or classify** — that's Appendix A.

✎ **Validation.** There is no schema validator here (the registrar validates; we're copiers without it). `graph/validate.py` (F0, to build in step 1) checks what it *can*: required fields per kind, every `about`/`supports`/`member_of`/`funds`/`related_to` ref resolves to an existing id, no duplicate ids, JSONL parses. Referential integrity, not schema conformance — said plainly.

✎ **Steady state — who runs what, after the backfill.** Ingesters are F0 scripts called from F3 skills: `/daily` (finalize step) → §8.7 digests (only `status: final`), §8.3 expectations · `/week` → §8.6 timelines, §8.4 bundles (after step 4's board pass), §8.5 capital-context (after 4b), §8.9 critic, §8.8 interp. Each is one line in the skill; the skill's own text names it.

### 8.1 Entity reconciliation — step one, F4 once, then F0

**Problem.** Three slug vocabularies overlap and disagree: `board.yaml` (`amazon-aws`, `andy-jassy`), `watchlist.yaml` (`amazon`, `elon-musk`), q1 (`amazon/capital`, bare `Amazon`), q3 (facility names). Everything else depends on one entity layer.

✎ **The facet question, settled.** q1's foundational rule — a company's capital-raising facet is a different node from its construction facet, because money and buildout are different questions — is kept. So the entity layer has two levels: **one canonical entity atom** per real-world entity (from board/watchlist), and **facet atoms** (q1's `amazon (capital)`, `amazon (ai-compute-procurement)`) linked `part_of` the canonical. `about` from an attention-layer claim targets the canonical; `about` from a q1 flow targets the facet. `has_part` is transitive and landed, so "every claim about Amazon" traverses both. The 204 existing q1 atoms are the facet level; step 1 creates the canonical level above them.

**Method.**
1. F0: extract every slug/name from all four sources into a candidate table with provenance.
2. F0: exact and normalized match (lowercase; strip `-aws`/`-inc`/facet suffixes) to propose clusters.
3. **F4, one sitting:** Ben rules each ambiguous cluster — is `amazon-aws` (a board kingdom with a house) the same entity as watchlist `amazon`? Output: `graph/schemas/entity-crosswalk.yaml` — `canonical_slug: [every old slug]`.
4. F0: rewrite every atom's `meta.entity_slug` and every relationship target through the crosswalk; `aliases` on each canonical atom carries every old slug.

**Canonical precedence:** `board.yaml` slug where on the board → `watchlist.yaml` → q1 bare entity → facility name. `houses` are person entities; `holdings`/`held_by` → `related_to`+role until `holds` lands.

**Done when:** one canonical slug per entity; crosswalk file exists; `cut:core-buildout` yields the same member set as before; `validate.py` passes.

### 8.2 Radar questions → 7 `question` atoms

`radar.md` headers → `kat-q-q1`…`kat-q-q7`: `label`, `meta.mode`, `meta.lens`, `epistemic_status: undecided`, S2. Working notes are composition — not ingested. `answers` edges come later from investigation deliverables; monitor-mode questions stay un-answered by design. ✎ This step also sets `loi` on every existing atom (q1 flows → `q2`; q3 facilities → `q3`'s radar counterpart, which is **Q1** ("players… DOING") or none — Ben's call in the same sitting as §8.1).

### 8.3 Remaining expectations → 54 hypothesis claims ✎ and a slip fix on the 16

`port_hypotheses_q3.py`'s mapping, filter widened. Normalizations: `evidence` as a URL list (1 case) → real `source` rows + `supports`; `outcome_note` where `evidence` is absent → the annotation's `justification`; `passed-silent` → `rejected`. ✎ **Slips are supersedes chains, not a `meta.slips` list**: "X by D" was falsified when D passed; "X by D′" is a new hypothesis that `supersedes` it, the old one `deprecated`. The 5 already-ported slipped items get re-shaped. `inference_basis` = the logging source's id (the earlier port left it empty — fix).

### 8.4 Bundle claims → per `-node` bundle × dim

`artifacts/bundles/<node>-node/provenance.yaml` (✎ count = the `-node`-suffixed subset of 124, established by the ingester, not assumed) is what `build_claims()` reads and is already claim-shaped. Per dim (`posture`, `capital.{available,operating,deployed,in,out}`, `optionality`, `gravity`) → one claim: `body` = value, `summary` = basis, `about` → canonical entity, one `source`+`supports` per `sources[]` row (`confidence` → band; `evidence_class` via the outlet band), `meta.dimension`, ✎ `valid_from` = the bundle's `asof`, refresh → `supersedes` chain per §8 intro. **Quantities stay prose** — typed extraction is a later F1 step, not promised. `board.yaml`'s inlined axis prose becomes redundant and retires in a follow-up ruling (§12).

**Site consequence, noted not built:** `build_claims()` can read these atoms — the clickability proposal's data source.

### 8.5 `capital-context.yaml` readings → 5 claims

`readings.<key>` → one claim: `body` = value, `summary` = basis, `loi: q7`, `meta.reading_key`, `valid_from` = `as_of`, sources → `supports`. `framing` is steering — not ingested. Refresh cadence per §8 intro.

### 8.6 Thread timelines → S2 claims (103 files) — ✎ runs *after* §8.7

Shape: `## <date> — <headline>` sections, bullets `- **<lead>** <prose> ([Outlet](url), …) ⟨<verb> <date>⟩`. Per bullet: find the S1 atom by the §7 key → bump to S2, add `meta.timeline`; else create at S2. ✎ **Skip spine actions** — `⟨steer⟩` bullets whose lead is `Thread opened` / `Promoted` / `Retired` / `Merged` are watch history, live in `threads.yaml` `notes`, not propositions. ✎ **`## ← Backstory` entries are propositions** (past facts) — ingest at S2 with `meta.backstory: true`. `⟨verb date⟩` → the `extraction_pass`. 💡/⚠️ → `meta.marker`.

### 8.7 Digest bullets → S1 claims (ruled in) — ✎ runs *before* §8.6

Parser exists: `render_read.py:305`. Per bullet → one claim: `body` = text minus link parenthetical (a sentence by construction — P-03 satisfied), S1, `meta.thread` (list), `meta.axis`, `meta.digest`, `lens` (list), `loi` (list, §12.1), `about` → each `e=` entity (canonical), links → sources + `supports`. Id = §7 key. ✎ **Only `status: final` digests** — a `building` digest's text can change, and a changed lead means a duplicate atom. ✎ **Skip `*-front.md` and `weekly/`** — both are composition over the lens digests, and the front's bullets are duplicates. ✎ **Check world-news digests carry `k:` tags before assuming** — the inventory confirmed tags on ai and global-capital only.

### 8.8 `interp.yaml` scenarios → hypothesis claims

Per `scenarios[i]`: `body` = `direction`, `defeat_conditions` = `why`, `meta.precedent`, `hypothesized`, ✎ `inference_basis` = [the parent S1 claim id] (same key the file is keyed on), `about` → the parent's entities, `loi: q7`. `mechanism`/`context_note` are frames — not ingested; the file becomes composition with a bibliography it already carries. Enforce the length caps on the way (§10.4).

### 8.9 Critic-log misses → `extraction_review` annotations ✎ (was: observations)

A `**Missed:**` item is a finding about our sweep, not first-hand data about the world. Per item: an `extraction_review` annotation on the claim the **Map effect** line produced (`justification` = the finding, `extraction_confidence` from the verdict), `generated_by_ref` = that critic pass. Where no claim resulted (`**Unverifiable:**`), the finding goes in the critic pass's `meta` — it's a process outcome with nothing to annotate.

## 9. What stays out, and why

| stays | why |
| --- | --- |
| `threads.yaml`, `radar.md` structure | spine |
| digest narratives, weekly digests, `*-front.md`, radar working notes, `actor-doing.yaml`, `interp` mechanisms, `coverage-log` prose | composition — cite in via the `k:` tags and bullet keys that already exist |
| `world-news.yaml` | S0 buffer |
| `watchlist.yaml` `terms`/`themes`/`conditions`, `sources/*.yaml`, `flash.yaml` | sweep and rail config |
| `board.yaml` vocab definitions | facet *definitions*; the *values* ride atoms |

## 10. Defects to fix on the way

1. **Genre drift** — five thread genres undefined in `board.yaml`'s 14. Define or remap. This repo, F0.
2. ✎ **`sources/outlet-credibility.yaml` is 83 % dead bytes** — six duplicate top-level `domains:` keys; only the last survives `safe_load`. **The builder is cloud-researcher's `credibility.py`** (in its installed package), so this is *their* append-instead-of-regenerate bug — brief filed, Appendix A. On our critical path (every news `source` needs its band), so step 7 waits on it or reads the last block knowingly.
3. `upcoming.yaml` `evidence` untyped — normalize in §8.3; propose one shape for the YAML.
4. `interp.yaml` length caps documented as enforced, aren't. Enforce or amend.

## 11. Sequence and done-when ✎ reordered

| # | step | F-rung | done when |
| --- | --- | --- | --- |
| 1 | entity reconciliation (§8.1) + `validate.py` | F0 · **F4 once** · F0 | canonical slugs; crosswalk exists; `cut:core-buildout` unchanged; validator passes |
| 2 | radar questions + `loi` on all existing atoms (§8.2) | F0 (+ one F4 call on q3's Q) | 7 atoms; every atom's `loi` resolves |
| 3 | expectations, incl. slip re-shape (§8.3) | F0 | 70/70; slips are `supersedes` chains |
| 4 | bundle claims (§8.4) | F0 | `build_claims()` output reproducible from atoms — **parity check, not cutover** |
| 5 | `capital-context` (§8.5) | F0 | 5 claims; wired into `/week` 4b |
| 6 | **digest bullets** (§8.7) — after 10.2 | F0 | every `k:`-tagged final bullet is an S1 atom |
| 7 | **timelines** (§8.6) | F0 | promoted bullets are S2 not duplicated; spine actions skipped; backstory in |
| 8 | interp scenarios (§8.8) | F0 | every scenario a hypothesis with a defeat condition |
| 9 | critic annotations (§8.9) | F0 | every `**Missed:**` with a Map effect is an annotation |
| 10 | steady state (§8 intro) | F0 in F3 | `/daily` and `/week` call the ingesters; a fresh digest produces atoms without a human step |

Steps 2–9 are independent once 1 lands, except 7 needs 6. **Nothing cuts a YAML over.** The operational files stay authoritative; step 4's parity check is the evidence for any later cutover ruling.

## 12. Open items and upstream asks

1. **thread → `loi`.** Threads carry `lens`, not a radar pointer. Proposal: a `loi:` list on each `threads.yaml` row (F4 once, 103 rows, mostly obvious). Until then `loi` derives from lens and is marked `loi_derived: true`.
2. **Round-four brief** (cloud-governor): `holds`/`held_by`, `operates`/`owns`/`leases`. Filed when step 1 yields the first real rows to cite.
3. **`board.yaml` axis-prose retirement** — after step 4's parity check.
4. **SQLite threshold** — none set; JSONL until a `/week` ingest or the site build is measurably slow.
5. ✎ **q3 facilities' `loi`** — Q1 or none; one call, step 2.

---

## Appendix A — what migrates to cloud-researcher

Everything below is a capability this repo either does by hand today, does badly with a stopgap, or has hard-coded in a place it doesn't belong. All of it is cloud-researcher's by charter (`kestrel/ROADMAP/CLOUD-RESEARCHER.md` D13: *gathering and verification*). **This graph is built with a seam at each one**: the ingesters consume already-fetched, already-classified material and do only structuring, so when a row below lands, what changes here is what fills an input field — never an ingester.

| # | capability | today, here | migrates as | what changes here when it lands | filed? |
| --- | --- | --- | --- | --- | --- |
| A1 | **Source capture** — fetch a URL, save verbatim text, hash-stamp it | not done; `source` atoms carry the URL only (link-only, honestly) | `fetch-one.py` / `capture-citations.py`, corpus-parametrized | `source.meta.capture_path` + `capture_sha256` populated; `add.py` already has the fields | ✅ `cloud-researcher/INBOX/2026-08-27-…verify-kit-not-reachable…` |
| A2 | **Evidence classification** — host → `evidence_class` + `reliability_tier` | a hand-written 6-line table in `build_graph.py`; band lookup in `outlet-credibility.yaml` | `fill-provenance.py`'s maintained host-class table | `supports.evidence_class` and `source.reliability_tier` come from the kit; the local table is deleted | ✅ same brief |
| A3 | **`outlet-credibility.yaml` builder** | `credibility.py` (cloud-researcher's own package) writes it — with the duplicate-key bug (§10.2) | already theirs; the bug is theirs | file regenerated clean; §10.2 closes | 📋 **to file** — a second brief, distinct from A1/A2 |
| A4 | **Run ledger** — machine-written record of every store-mutating run | `extraction_pass` rows reconstructed *after the fact* by ingesters from `⟨verb date⟩` tags and `capture_ref` markers | `runlog.py` — the collector run *emits* its own pass record as a side effect | ingesters stop reconstructing passes; they read the ledger | ✅ A1 brief names it |
| A5 | **Expectation resolution** — "did `what_confirms` happen by `due`?" | F2 subagents doing WebSearch + judgment (4 this session) | a verify verb: bounded fetch + one bounded question, per §8.3's shape | the `extraction_review` annotation is emitted by the verb; `/week` step 2 calls it | 📋 to file after A1 lands |
| A6 | **Research-pass sourcing** — find and cite a new financing | agent WebSearch/WebFetch + hand-written reliability (all four q1 passes) | A1 + A2 together, driven by a claim needing a source | `add.py`'s input dict is filled by the kit, not by hand | ✅ A1 brief |
| A7 | **S0 buffer** — the world-news candidate pool | `build_world_news` / `gdelt_dedup` — already moved to cloud-researcher 2026-08-21 | already theirs | none; stays out of the graph (§7). Optional later: the kit emits the S1 candidate on `confirmed_thread` | — |
| A8 | **Capital-context collectors** | `treasury_tic`, `bis_stats`, `imf_data`, `epfr_flows`, `fund_flow_reports` — already theirs | already theirs | §8.5 ingests their output; unchanged | — |
| A9 | **Coverage-critic benchmark fetch** | the critic pass fetches benchmark outlets through reader proxies with per-outlet workarounds in `sources/benchmarks.yaml` | sweep-side collector with the access-note logic | §8.9 consumes the finding; the fetching leaves | 📋 to file — after `collect --corpus` bug (already in their inbox) closes |
| A10 | **Observations** — first-hand data about the world | none exist here | `page_diff.py` hits ("this page changed") emitted as `observation` atoms; q3 first-hand measurement if ever | a new ingester (§4's observation row reopens) | 📋 after reg-02 lands `observation@1.1.0` |
| A11 | **`collect --corpus` targeting** | flag silently inert; env-var workaround | bug fix | `/week` 4b's documented command works as written | ✅ `cloud-researcher/INBOX/2026-08-21-theprojection-collect-ignores-corpus-flag.md` |

**Stays here, explicitly:** the graph and its JSONL · every ingester (F0 structuring is this repo's) · the entity crosswalk · `validate.py` · the spine (`threads.yaml`, `radar.md`) · the composition layer · `cut:core-buildout` and the local vocab. D13 in both directions: the researcher doesn't structure our graph; we don't gather.
