<!-- kit: attention/week@2026-08-21.4 — canonical: kestrel/library/skills/attention/week/SKILL.md.tmpl — provenance only. A local edit is fine; kit.py sync will flag drift. Route a wanted template change to the engine's issue tracker (dev) or its ops inbox (anything naming a live repo), never a direct edit. -->

---
name: week
description: The weekly pass — synthesis against the radar questions, near-miss audit, and the decay review that prunes the attention map. Run Saturday or when convenient.
---

# /week — synthesis + decay review

Once a week (Saturday by default; any convenient day works). **The week is
fixed Mon–Sun (5am ET boundaries)** — `week_of` is the Monday of the week
containing the run date, regardless of which day `/week` actually runs.
This is where the map *shrinks* and understanding *compounds*; the dailies
only ever grow it.

## Steps

1. **Weekly digest** — one per lens into `artifacts/digests/weekly/`,
   rendered against `templates/weekly-digest.md`. Written **against
   `attention/radar.md` questions**, not as a re-aggregation: what moved on
   each open Q this week, reading the week's dailies as pre-digested
   history plus one fresh 7-day sweep.
2. **Expectations scorecard** — resolve anything in
   `attention/upcoming.yaml` still pending-but-due from the week; write the
   week's hit/slipped/passed-silent scorecard into the weekly digest
   (⏳ section); prune resolved entries older than the closing week (the
   digest records them first — nothing is lost). **Also prune expired
   flashes** from `attention/flash.yaml` — expired means past
   `render_read.flash_last_day()` (the filing day; **not** the raw
   `expires` field, which since 2026-08-04 can only shorten a flash and is
   ignored when longer). This is now cosmetic tidying: the rail already
   refuses to render them regardless. Their substance already lives in the
   digests and timelines; nothing is lost. If the week logged
   **more than one or two flashes, say so in the digest** — a rail that
   fires often has a drifting bar and stops meaning anything
   (AGENTS discipline 10).
3. **Near-miss audit** — the week's `coverage-log.md` entries: what
   benchmarks led with that we missed, what was auto-added, whether a
   *pattern* implies a watchlist/source gap. Also flag: any entity with
   heavy item traffic but no thread (candidate signal) and any thread whose
   tags never appear (retire signal).
4. **Decay review — a staleness REPORT, not a retirement queue** (Ben,
   2026-08-14: "I don't understand why we would ever retire a thread...
   why would we decay retire anything?"). List threads whose `last_seen`
   is older than **10 days** (slug · stale since · a one-line note on
   why it's plausibly still quiet), plus **stale timelines** (thread
   active in yaml but no timeline entry in 14 days) and unresolved
   passed-silent expectations — purely as information. **Being stale is
   not itself grounds to resolve or retire anything.** Most real stories
   move on their own irregular cadence (a regulatory process, a budget
   cycle, a court date, a slow product cadence) — going quiet for a week
   or two says nothing about whether the story is over, and the 2026-08-14
   run's own numbers prove it: 27 stale threads reviewed, 26 came back
   "keep." **Only propose a resolve/retire when there's a concrete,
   evidence-based reason on the table** — the story demonstrably
   concluded elsewhere (resolve), or it's a confirmed dead end / a
   duplicate / explicitly abandoned (retire) — never staleness alone.
   State the reason plainly when proposing one; if there isn't a real
   reason, don't propose anything — just note the thread is quiet and
   move on. **Ben still answers any real proposal in the same read;
   never resolve or retire silently.**
   ⚠️ **Why this is a mechanical distinction, not just an editorial
   one**: `resolved`/`retired` threads drop out of `/daily`'s collector
   term sweep (AGENTS.md discipline 1 — "a thread that's done stops
   costing API calls"). An `open` thread keeps being watched regardless
   of how stale it looks; retiring is a decision to **stop watching**,
   not a decision to stop displaying. `/map`'s own freshness buckets
   (🟢🟡🔴, by `last_seen`) already carry the pure display-only
   staleness signal — that's the tool for "hasn't been active in a
   while." Treating every stale thread as a resolve/retire candidate by
   default quietly turns a display concern into a coverage-loss risk.
   **Board pass** (2026-07-24; axis model 2026-07-25): run the `/classify
   postures` logic — propose a posture for every org marked `# provisional`
   or whose posture no longer matches its open-thread genres, flag any actor
   whose structural kind (state↔kingdom) or axis estimate
   (capitalization/optionality/gravity) has drifted from the evidence, and
   surface board actors with no live thread this cycle as `dormant`
   candidates. Ben confirms in the same read;
   apply `classify`/`ben-steer`. **Then refresh the standing synthesis** — a
   full pass over `attention/actor-doing.yaml`, re-writing each major actor's
   "what are they doing now" roll-up from its current threads + posture (bump
   `asof`); this is the layer people read to know an actor's state without
   reading every thread. Then `/publish --push` so `/map/` reflects it all.
   Then `graph/ingest/04_bundle_claims.py` (added 2026-08-27, `graph/
   DESIGN.md` §8.4 — local extension, skip if `graph/` doesn't exist):
   the board pass just refreshed `artifacts/bundles/*-node/
   provenance.yaml`'s `asof`/figures, so this is the natural point to
   re-run it — idempotent, only creates a new claim (superseding the
   old) for a node whose bundle actually changed. `graph/validate.py`
   after.
4b. **Refresh the standing capital-context snapshot**
   (`attention/capital-context.yaml`, DESIGN.md Part 2 §11) — this is the
   `/week`-adjacent pass that artifact is built for; `/daily` never
   touches it. Re-run the Global Capital data stack's 5 collectors
   (`treasury_tic`, `bis_stats`, `imf_data`, `epfr_flows`,
   `fund_flow_reports` — `cloud-researcher collect --corpus . --lens global-capital
   --source <id>` per source, since these aren't part of the term-swept
   watchlist sweep), then re-write each `readings.*` entry from what
   actually came back — a real value, a real `basis`, real `sources[]`,
   bump `as_of`. Apply `framing.emphasis`/`framing.deprioritize`/
   `framing.notes` (whatever `/steer capital-context ...` has accumulated
   since the last refresh) to shape which readings get the closer look,
   same as any other steering input. A reading with genuinely nothing new
   since last week (the data hasn't moved — several of these sources lag
   weeks to months) keeps its prior value and `as_of` rather than being
   rewritten for the sake of it. Never hand-invent a reading — if a
   collector comes back empty (`fund_flow_reports` may well, both its
   sources are bot-gated as of 2026-07-30), say so in the reading's
   `value` rather than fabricating one. Then `graph/ingest/
   05_capital_context.py` (§8.5, same local-extension/skip-if-absent
   caveat as above) — refresh-aware, a reading with no new `as_of` is a
   no-op. `graph/validate.py` after.
4c. **Refresh the q1-flows money-graph** (`research/q1-flows/
   {nodes,edges,memberships}.yaml` — added 2026-08-27 as a **local
   extension specific to this instance**, not part of the canonical
   kestrel template and with no upstream equivalent; a repo-specific
   research program, see `research/README.md`). **As of 2026-08-27, this
   targets `graph/`, not the YAML files** —
   `nodes.yaml`/`edges.yaml`/`memberships.yaml` are frozen (safety net +
   archeology only, see their own headers). Scan the week's own daily
   digests (already-curated — no fresh sweep needed) for named financing
   events crossing the $100M materiality floor (Ruling 2 in
   `INBOX/2026-08-03-q1-skeleton-v3.md`): equity rounds, debt issuances/
   bond sales, M&A/asset purchases, anchor-lease/capacity deals, and
   guarantees. For each one, source it exactly as every prior pass has —
   a real WebSearch/WebFetch, a real URL, a hand-written reliability
   score and rationale (this is the manual stand-in for `cloud-researcher`'s
   verify tools, which aren't reachable from this repo yet — see
   `cloud-researcher/INBOX/2026-08-27-theprojection-corpus-verify-kit-not-
   reachable-from-consuming-repos.md`; nothing here changes when that
   lands, only how the source gets captured) — then call
   `graph/add.py`'s `add_financing(...)` with the
   result. Follow `research/PRINCIPLES.md` (P-01: cardinality-correct
   fields; P-02: a structured field records what a source explicitly
   says, never an inference) and `graph/schemas/
   q1-local-vocab.md` for `flow_type`/`destination_category` — real
   cited sources only, an honest link-only capture rather than a
   fabricated figure. This is a lighter, incremental top-up, not a full
   research pass: apply established principles/rulings directly; only a
   genuinely novel schema question gets flagged and held for Ben rather
   than decided unilaterally, the same discipline the dated passes in
   `research/README.md` already follow. After adding the week's
   financings, re-run `graph/export_q1.py` — **closed 2026-08-27**: the
   Q1 page (`theprojection-site/content/research/q1.md`) is now a live,
   clickable render of `graph/{atoms,relationships}.jsonl` (front matter
   `flowmap: q1_flows`, drawn by `layouts/research/single.html` +
   `static/js/q1-flowmap.js`), not hand-typed tables — no manual page
   edit needed, the export script is the only step. Validate every JSONL
   file still parses after editing, same discipline the frozen YAML
   always had.
5. **Radar upkeep** — update each worked question's Working notes; flag any
   question that looks answered or dead.
6. **Map deltas of the week** — the full add/drop ledger with provenance
   tags, so evolution stays visible.
7. ⛔ **RETIRED 2026-08-25** — this step used to run `theprojection
   render-read` and republish the private "internal read" Artifact page so
   a weekly-synthesis panel showed there. That page is retired in full
   (Ben: "kill it utterly" — see AGENTS.md discipline 8, ROADMAP.md
   §Delivery); `render_read.py`'s `load_weekly()`/`_parse_weekly_
   throughline()` (the code behind that panel) were dead-code-removed
   with it, since nothing else called them. There is no replacement
   weekly-synthesis surface on the public site — if one is wanted there,
   that's new work, not a restore of this step.
8. **Take steering** — same as `/daily`: reactions apply immediately.

## Interim mode

Until the pipeline lands, run the 7-day sweep agentically (subagent per
lens) and assemble against the template in-session.
