# kestrel

**Ben's personal intelligence layer.** Hovers over the external sources,
watches, and dives only when something matters — it **buffers and extracts,
never owns the source data** (its own artifacts and bundles it owns
durably). The kestrel is not a datastore.

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
                  push safety on both repos, doc drift) → the next move
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
| `attention/` | **the product** — `watchlist.yaml` (entities: who/what, per lens; slug rules in header) · `threads.yaml` (the narratives, with `entities:` + `weight:`) · `upcoming.yaml` (dated-expectations ledger) · `radar.md` (the big questions Q1–Q7) · `board.yaml` (the power-structure layer: every actor a **node** with `kind` (person/house/corp/state/agency/group) + `level` (L1/L2) + group nodes for pockets/sectors, on the four measured axes (commanded_capital · thrust · gravity · optionality) — see [`DESIGN.md`](DESIGN.md)) · `actor-doing.yaml` (per-actor standing "what they're doing now" synthesis) · `flash.yaml` (the editorial, `critical`-only general-news rail) · `world-news.yaml` (the mechanical, cross-spectrum attention signal — GDELT + google_news_rss merged, matched against threads) · `capital-context.yaml` (the global-capital lens's standing macro snapshot — 5 sourced readings, refreshed weekly, `/steer`-adjustable framing only) |
| `sources/` | `sources.yaml` (machine-readable source map) · `benchmarks.yaml` (coverage-critic baselines per lens) · `feeds.yaml` (RSS set — seed pending) |
| `collectors/` | python package, one module per source — **17 built**: `google_news_rss` · `rss` · `gdelt` · `sec_edgar` · `federal_register` · `openalex` · `clinicaltrials` · `fred` · `semantic_scholar` · `github` · `lda` · `fec` · `treasury_tic` · `bis_stats` · `imf_data` · `epfr_flows` · `fund_flow_reports` (the last two: global-capital's data stack, added 2026-07-30 — 4 return real live data, `fund_flow_reports` an honest empty result, both its sources bot-walled) — one shared contract (`base.py`) |
| `templates/` | fixed render templates: `daily-digest.md` · `weekly-digest.md` · `thread-timeline.md` · `read-shell.html` (the one-time page shell) |
| `.claude/skills/` | the commands: `/start` `/daily` `/week` `/steer` `/crawl` `/map` `/publish` `/classify` |
| `buffer/` | git-ignored dated JSONL — pure cache, 30-day retention |
| `artifacts/` | `digests/daily/` (canonical archive, `<!-- k: -->`-tagged) · `digests/weekly/` · `threads/` (per-thread timelines) · `read/` (derived page — a view, not an artifact) · `findings/` · `bundles/` |
| `provenance/` | per-run fetch manifests + `publish-*.yaml` public-export manifests (git-tracked, one per `/publish` run) |
| `tools/` | `collect.py` (collectors runner CLI — built) · `probe.py` (collector connectivity smoke test — built) · `pdf_text.py` (PDF → plain-text extraction — built) · `render_read.py` (deterministic page renderer — built) · `publish_projection.py` (public export — built) · `readouts.py` (per-page executive readouts — BREAKING/NEWS mechanical, SUMMARY model-written — built) · `thumbnails.py` (og:image capture w/ `buffer/`-cached results, called by publish — built) · `world_news.py` (google_news_rss clustering — built) · `gdelt_dedup.py` (GDELT Events dedup + syndicate collapse — built) · `build_world_news.py` (merges both into `attention/world-news.yaml`, matched against threads — built) · generate-digest · coverage-critic · deliver (to build) |

## Public site

**theprojection.org** ([repo](https://github.com/benthepsychologist/theprojection),
Hugo + Cloudflare Pages) is a separate public repo — Ben's non-clinical
publication, built around the psychological-projection lens ("the surface is
never the system"). Kestrel feeds it, never the reverse: `tools/publish_projection.py`
publishes every thread by default (Ben, 2026-07-22 — no hand-gating; hold
one back with `public: false`) through a hardcoded field allowlist and a
secret-scan pass, then stages `content/threads/*.md` + `data/payload.json` in
the site repo's working tree — commits and pushes with `--push`. See
AGENTS.md discipline 9. **Live since 2026-07-23**: 67 threads publishing,
`/publish` wraps the script. Each of the three lenses is a **beat page**
(`/beat/ai/` · `/beat/global-capital/` · `/beat/mental-health/`, leading the nav)
carrying its own **morning briefing** — `gist` · salience-ranked `lead` ·
themed `sections` · `watch` — with the fuller cross-lens briefing on the
homepage (AGENTS.md discipline 12). The site also carries the **`/map/`
board section** — a node page per actor plus **pocket and sector pages**, with
every posture/axis value linking to its **`/claim/<id>/` receipt** (cited
sources) — and its own hand-authored `content/about.md` and `README.md`, the
latter kept fact-synced with this repo's actual publish behavior as part of
`/publish`'s routine, not just written once. (Costume vocabularies are
projected via `data/labels.yaml`; the default is now plain, metaphors
deferred.)

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
  capital-flow + optionality + gravity behind every claim page (72 of them;
  see [`DESIGN.md`](DESIGN.md) §3).
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

## Status — daily rhythm live; public site live; collectors built

As of 2026-07-30: the **attention map is seeded and steered** (67 threads,
8 of them `kind: meta` — the capex destination tree and Big-Tech-into-health
among them — grown/corrected across several `/daily` runs). A
**power-structure board** (`attention/board.yaml`: 77 orgs + 19 Houses +
11 group nodes) shipped 07-24 and publishes to the site's `/map/` section.
Its feudal rank ladder collapsed to axes on 07-25; on 07-26 the board became
a **node + claim graph** (every actor a node, every metric a clickable
**`/claim/<id>/` page** backed by cited per-node bundles — 664 claims); and
on 07-27 the model completed as **four measured axes** (commanded_capital ·
thrust · gravity · optionality, each grounded in named prior art) with
numeric `axes_num` on a 21-actor pilot — rendered as **the plate** (the
power view: optionality columns × weight, size = gravity, heat = burn)
atop `/map/`, with per-metric methodology pages at
`/metric/` (see [`DESIGN.md`](DESIGN.md)). The **daily rhythm is real**: `/daily` #1
finalized 07-20
(reconstructed the missed 07-21); `/daily` #2 finalized 07-22 and opened
07-23. The **thread-centric weekly reframe (Phase 0)** shipped 07-22:
timelines, entity layer, expectations ledger, tagged digests, weekly
dashboard (`tools/render_read.py`, stable artifact URL, ROADMAP §Delivery).
All promoted threads carry crawled backstories. **The public site went
live 07-23** and iterated through direct usage feedback the same day:
`/publish --push` ships real threads to theprojection.org; a
mobile-usability pass (collapsible cards, a highlights strip); "copy for
AI chat"; meta-threads; then a second feedback round — bigger feed-card
layout, real per-article thumbnails (`tools/thumbnails.py`, og:image
capture, cached in `buffer/`) with a favicon-tile fallback, whole-row
click-through. **Collectors are BUILT** (2026-07-28: 12 live sources —
google_news_rss · rss · gdelt · sec_edgar · federal_register · openalex ·
clinicaltrials · fred, plus the same-day tier-2 wave semantic_scholar ·
github · lda · fec — + `tools/collect.py`/`probe.py`/`pdf_text.py`;
/daily runs collectors-first). **07-29 shipped the read's ranking and
readouts**: threads now rank by salience (`weight × (V + I) + M` — volume,
imminence off `attention/upcoming.yaml`, and item magnitude via `sev=`,
not raw volume alone), a **flash rail** (`attention/flash.yaml`) puts
general-news-scale events on every page, and **`tools/readouts.py`** adds
BREAKING/NEWS (mechanical) + SUMMARY (model-written) executive readouts
atop every page. **07-30 shipped World News and specced Global Capital.**
World News (`attention/world-news.yaml`) is a mechanical, restrained,
cross-spectrum signal — distinct from the editorial flash rail — merging
google_news_rss clustering with a deduped GDELT feed
(`tools/build_world_news.py`), matched against `threads.yaml`; first real
run: 142 items, 54 confirmed, 88 held as candidates, now folded into
`/daily`'s thread-candidate offering. **The money lens is now
`global-capital`** — a full rename, not cosmetic (Ben: "'finance' is
boring 'Global Capital' is interesting to me"), and an interpretive one:
every relevant item can carry a generated, confidence-tagged
`interpretation` (`{mechanism, confidence, scenarios[], context_note}`,
enforced by `tools/readouts.py`'s `validate_interpretation()`) alongside
its sourced bullet, read against a standing macro-context snapshot
(`attention/capital-context.yaml`, refreshed weekly). Receipt pages live
at `/interpretation/<slug>/`. The data stack behind the snapshot —
Treasury TIC, BIS, IMF, EPFR, and fund-flow reports — is 5 real
collectors, 4 returning live data and one (fund-flow reports) an honest,
evidenced empty result (both its sources bot-wall this environment). Full
build: `DESIGN.md` Part 2. Still to build: P3 judgment tools (curate ·
coverage critic · state machine), remaining tier-2 keys; Drive comment
loop HELD. **Zero bizdev coupling** stands (BOOTSTRAP §Scope). Live state:
[`STATUS.md`](STATUS.md); architecture (nodes + claims):
[`DESIGN.md`](DESIGN.md); build checklist + gates:
[`BOOTSTRAP.md`](BOOTSTRAP.md).
