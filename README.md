# theprojection-corpus

**Ben's personal intelligence layer — instance #1** of the kestrel engine.
Hovers over external sources, watches, and dives only when something
matters — it **buffers and extracts, never owns the source data** (its
own artifacts and bundles it owns durably). Not a datastore.

Lenses: **ai · global-capital · mental-health**, plus **world-news**
(2026-07-30) — a fourth, deliberately narrow lens for threads that are
genuinely irreducible to the other three (a conflict/geopolitical
narrative for its own sake), with no watchlist sweep or coverage-critic
benchmarks of its own — not a peer of the primary three.
**global-capital** (renamed from `money` 2026-07-30, full rename — "'finance'
is boring 'Global Capital' is interesting to me") is itself an
*interpretive* lens: every relevant item can carry a generated,
confidence-tagged interpretation alongside its sourced bullet, read
against a standing macro-context snapshot — see DESIGN.md Part 2. Goal:
Ben knowledgeable and ultra-current — "this feeds me, not a dataset."
Daily and weekly digests are where insight surfaces; backward crawl fills
in backstory on demand.

Design of record: `pm` hub →
`streams/research-and-writing/projects/mh-tech-record/intelligence-feed-pivot.md`
(the 2026-07-20 pivot doc — frame, API candidates, stack manifest, this
repo's design in its §6).

## The engine/instance split (2026-07-31)

This repo is **instance #1** of the kestrel engine — it holds the DATA
(the attention map, artifacts, sources config, provenance, templates,
buffer) plus the operating skills (`.claude/skills/`) and these docs. The
CODE (collectors, the diff→changelog engine, the publish core, the kit
library) lives in kestrel (`/workspace/kestrel`), which tends this repo
and its siblings (currently also `therapybulletin-data`). `kestrel.yaml`
at this root is the instance manifest kestrel's tools read to know how to
operate here — the layout keys in it mirror what the tools actually read.

**Every engine tool needs `KESTREL_INSTANCE` pointed at this repo:**

```
KESTREL_INSTANCE=/workspace/theprojection-corpus python3 /workspace/kestrel/tools/collect.py
```

Full rule + rationale: `CLAUDE.md`. Without the env var, an engine tool
falls back to looking for instance data inside kestrel, where it no
longer lives, and fails loudly rather than silently reading stale paths.
This repo's own history before 2026-07-31 lives in kestrel's git history
(tag `pre-engine-split` and earlier).

**Publish is generic-core-plus-adapter, as of 2026-07-31:** kestrel's
`tools/publish.py` is a generic CLI with no per-site code of its own —
each instance declares its own adapter via `kestrel.yaml`'s
`outputs.adapter`. This instance's adapter lives HERE, at
`publish/adapter.py` (relocated out of the kestrel checkout the same
day), and its site-checkout path + Cloudflare deploy-hook config are read
from this repo's own `.env` (see `.env.example`).

## The principle (settled 2026-07-20)

External public datasets (GDELT, OpenAlex, EDGAR, FRED, …) are the **source
of truth** — durable, free, better-maintained than any copy we'd keep. No
ingestion/canonicalization pipeline. Locally we generate:

- **Buffer** — raw pull results with *cache* semantics: disposable,
  regenerable, short retention. Never canon.
- **Artifacts** — digests, findings, thread updates, syntheses. The durable
  output.
- **Bundles + provenance** — every artifact ships with a manifest of *how to
  re-fetch* its inputs (source · query · timestamp · stable ids). Never the
  data itself.
- **Source map** — where things are and how to get them (`sources/`).

**Perishability rule:** a real capture pipeline is justified only where the
observation is gone if not captured at that moment. That set lives *outside*
this repo (today: kalshi-scanner). `diffable` sources (Epoch CSVs, Forbes
lists) keep one prior snapshot for deltas; everything else is fetch-on-demand.

## The working day

```
/start            session open, read-only: continuation briefing + live
                  pipeline state (digests, expectations, flash, freshness,
                  push safety across repos, doc drift) → the next move
/daily            any time, any frequency — catch up to now: yesterday
                  finalized, expectations checked, today curated + tagged,
                  timelines updated, weekly page re-rendered, take steering
/steer <words>    "track X" · "drop Y" · "weight Z 3" · "expect C by D" —
                  the map moves, logged
/crawl <thread>   backstory on demand → finding + bundle + timeline backfill
/map              read-only status card, any time
/week             Saturday: synthesis by radar question + expectations
                  scorecard + decay review (weeks are fixed Mon–Sun)
/publish          push public-flagged threads to theprojection.org —
                  separate from /daily, not auto-chained; --push goes live
/classify <actor> place an actor on the board (attention/board.yaml) —
                  propose node kind (person/house/corp/state/agency/group)
                  + level + posture + axis estimate, apply on confirm
/health           read-only: is this repo in the state its docs claim?
                  kit drift, whether STATUS.md still matches reality, git
                  uncommitted/unpushed, inbox depth. Any time.
/wrap             checkpoint the session (any time, several times a day):
                  STATUS refresh, log.md, commits w/ receipts, verified
                  push on both zone repos — LOCAL skill, not kit-rendered
```

**The read is thread-centric** (Ben, 2026-07-22): a rolling Mon–Sun weekly
dashboard — active threads ranked by weight × move size, each wrapping its
evidence and dated expectations; entities (== the watchlist) clickable
above them. The map grows through reading (steering + critic auto-adds)
and shrinks through `/week`'s decay review — never by batch rewrites
(AGENTS.md §steering loop, disciplines 7–8).

## Layout

| path | what |
| --- | --- |
| `attention/` | **the product** — `watchlist.yaml` (entities: who/what, per lens; slug rules in header) · `threads.yaml` (the narratives, with `entities:` + `weight:`) · `upcoming.yaml` (dated-expectations ledger) · `radar.md` (the big questions Q1–Q7) · `board.yaml` (the power-structure layer: every actor a **node** with `kind` (person/house/corp/state/agency/group) + `level` (L1/L2) + group nodes for pockets/sectors, on the four measured axes (commanded_capital · thrust · gravity · optionality) — see [`DESIGN.md`](DESIGN.md)) · `actor-doing.yaml` (per-actor standing "what they're doing now" synthesis) · `flash.yaml` (the editorial, `critical`-only general-news rail) · `world-news.yaml` (the mechanical, cross-spectrum attention signal — GDELT + google_news_rss merged, matched against threads) · `capital-context.yaml` (the global-capital lens's standing macro snapshot — sourced readings, refreshed weekly, `/steer`-adjustable framing only) |
| `sources/` | `sources.yaml` (machine-readable source map) · `benchmarks.yaml` (coverage-critic baselines per lens) · `feeds.yaml` (RSS set) · `API-SIGNUP.md` (key-signup boilerplate + status) |
| `INBOX/` | inbound handoff hopper (the cross-repo protocol in the global CLAUDE.md) — briefs dropped by other repos' sessions, plus workshop drafts replying to them. Holds the frozen, no-longer-edited design record for kestrel's q1-q4 buildout-research program (skeletons + rulings register R-01–R-20) — the program itself is now under active build in `research/` (below), not here. |
| `research/` | kestrel's buildout-research program (q1 money-flows, q2 inference-demand, q3 datacenter census, q4 governance — unstarted), actually built as of 2026-08-10: `q1-flows/` (`nodes.yaml` incl. `round`-kind financing-event nodes, `edges.yaml` cited dollar flows, `memberships.yaml` `is_member_of` investor/lender↔round edges, `filters/` named boundary cuts over the same flow map) · `q3-datacenter-census/` (an attribution layer over the Epoch AI dataset) · `PRINCIPLES.md` (durable schema-design principles, P-01/P-02…, distinct from `INBOX/`'s frozen per-decision rulings register). Standalone — does not yet feed `/publish`, the site, or `attention/`; the claims-layer merge direction is logged in `ROADMAP.md`'s Queue, not built. |
| `templates/` | fixed render templates: `daily-digest.md` · `weekly-digest.md` · `thread-timeline.md` · `read-shell.html` (the one-time page shell — its HTML/JS is hand-authored, never edited by `/daily`) |
| `.claude/skills/` | this instance's commands: `/start` `/daily` `/week` `/steer` `/crawl` `/map` `/publish` `/classify` `/health` `/wrap` — all kit-installed as of the 2026-08-21.3 sync (`/health` arrived with that sweep and went undocumented here until the 08-21 publish staleness check caught it) (`/wrap` was local and un-kit-tracked from 2026-08-07 until then, when it was adopted into the library verbatim) — installed/synced from kestrel's kit library (`.agents/kit.yaml` tracks the installed stamp, one hash per rendered file). **These are kit-rendered, and kestrel is outside this session's write zone** (Ben, 2026-08-04) — so to change one, drop a brief into `/workspace/kestrel-ops/INBOX/` rather than editing the canonical copy. Editing a file here is allowed but will show as `dirty` in `kit.py sync`, which is the intended signal. ⚠️ Each file's line-1 header still says "edit the canonical copy… run `/sync-kits`" — superseded, and `/sync-kits` does not exist here; ignore it. |
| `buffer/` | git-ignored dated JSONL — pure cache, 30-day retention |
| `artifacts/` | `digests/daily/` (canonical archive, `<!-- k: -->`-tagged) · `digests/weekly/` · `threads/` (per-thread timelines) · `read/` (derived page — a view, not an artifact) · `readouts/` · `findings/` · `bundles/` |
| `provenance/` | per-run fetch manifests + `publish-*.yaml` public-export manifests (git-tracked, one per `/publish` run) |
| `publish/adapter.py` | **this instance's** publish adapter (relocated here from the kestrel checkout 2026-07-31) — declared via `kestrel.yaml`'s `outputs.adapter`, loaded by kestrel's generic `tools/publish.py`; no per-site code lives in the engine repo |
| `kestrel.yaml` | the instance manifest — `kind: attention`, layout keys, `outputs` (site path + adapter path) |
| `.env` / `.env.example` | this instance's own env config (site checkout path, Cloudflare deploy-hook URL) — read by `publish/adapter.py`; gitignored, never commit real values |
| docs | `AGENTS.md` (disciplines + operating rhythm) · `STATUS.md` (live state) · `ROADMAP.md` (decisions + sequence) · `BOOTSTRAP.md` (build gates) · `DESIGN.md` (board/claims schema + pipeline) · `REBUILD-NOTES.md` · `log.md` (session-close ledger) · `coverage-log.md` (critic + steering log) |

The engine side (for reference, lives in `/workspace/kestrel`, not here):
`collectors/` (source modules), `tools/` (the CLI scripts — `collect.py`,
`render_read.py`, `readouts.py`, `publish.py`, `world_news.py`,
`gdelt_dedup.py`, `build_world_news.py`, `probe.py`, `pdf_text.py`,
`thumbnails.py`, and more), `library/` (the kit that installs
`.claude/skills/` here).

## Public site

**theprojection.org** ([repo](https://github.com/benthepsychologist/theprojection-site),
Hugo + Cloudflare Pages) is a separate public repo — Ben's non-clinical
publication, built around the psychological-projection lens ("the surface is
never the system"). Kestrel feeds it, never the reverse: kestrel's generic
`tools/publish.py`, running this instance's own `publish/adapter.py`,
publishes every thread by default (Ben, 2026-07-22 — no hand-gating; hold
one back with `public: false`) through a hardcoded field allowlist and a
secret-scan pass, then stages `content/threads/*.md` + `data/payload.json` in
the site repo's working tree — commits and pushes with `--push`. See
AGENTS.md discipline 9. Each of the three primary lenses is a **lens page
under `/news/`** (`/news/ai/` · `/news/global-capital/` ·
`/news/mental-health/` — nested under the `/news/` dashboard since the
2026-08-03 restructure, when the front page became a projects hub and the
news feed moved to `/news/`) carrying its own **morning briefing** — `gist`
· salience-ranked `lead` · themed `sections` · `watch` — with the fuller
cross-lens briefing on the **`/news/` dashboard** (AGENTS.md discipline 12).
Since 2026-08-07 the dashboard links the three feeds visibly (a Feeds
row; the filter chips stay filters) and every feed page carries a
**Methodology** crumb to **`/methodology/`** — one page: the common
pipeline told once, per-feed sections (questions · sources with named
critic benchmarks · threads · cadence · honest gaps), plus a
coverage-check appendix mapping a working clinical team's source list
against this feed's mechanisms, every verdict live-verified. The site also carries the **`/map/`
board section** — a node page per actor plus **pocket and sector pages**, with
every posture/axis value linking to its **`/claim/<id>/` receipt** (cited
sources) — and its own hand-authored `content/about.md` and `README.md`, the
latter kept fact-synced with this repo's actual publish behavior as part of
`/publish`'s routine, not just written once. (Costume vocabularies are
projected via `data/labels.yaml`; the default is plain, metaphors deferred.)

## Contracts

- **Collector:** stateless `collect(watch, since) -> items + provenance`;
  read-only against the world; writes only to `buffer/`.
- **Provenance record:** `{source_id, params, fetched_at, items:[{id,url,ts}]}`
  — sufficient to re-fetch, deliberately nothing more.
- **Evidence lives in bundles:** when an artifact's claim needs durable
  evidence (the cited page could vanish), the capture goes in that artifact's
  bundle — evidence of *our citations*, never a general archive. On disk:
  `provenance/` holds **per-run** fetch manifests; a **bundle** is
  **per-artifact** (`artifacts/bundles/<slug>/` with `provenance.yaml` +
  optional `captures/`; daily digests use a lightweight sidecar
  `<digest>.provenance.yaml`). The board uses the same shape **per node**:
  `artifacts/bundles/<slug>-node/provenance.yaml` holds the sourced posture +
  capital-flow + optionality + gravity behind every claim page — see
  [`DESIGN.md`](DESIGN.md) §3.
- **Zero bizdev coupling** (Ben, 2026-07-20): never import, call, or write
  to bizdev after the one-time seed. Shared workstation infra
  (`authctl`/`gorch` for Drive) and one-time seed reads elsewhere are fine —
  they're platform, not bizdev. See BOOTSTRAP.md §Scope.
- **Lens declared once** in `attention/`; collectors, digests, and the
  coverage critic all key off it. **`world-news` is the exception on
  purpose** (2026-07-30): a thread can carry it, but there's no
  watchlist sweep or coverage-critic benchmark set for it — new threads
  arrive only via `attention/world-news.yaml`'s own candidate mechanism,
  never a term sweep.

## Status

Live state, dated narrative of what shipped and when, and what's still
open: **[`STATUS.md`](STATUS.md)**. Decisions + build sequence:
**[`ROADMAP.md`](ROADMAP.md)**. Board/claims architecture:
**[`DESIGN.md`](DESIGN.md)**. This file describes structure and
contracts, which change rarely — current counts (threads, collectors,
claims) live in STATUS.md and drift too often to duplicate here.
