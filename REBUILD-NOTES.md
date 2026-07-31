# REBUILD-NOTES — functional requirements distilled from the reference implementation

*Extracted 2026-07-20 by a read-only crawl of bizdev's digest machinery, so
kestrel never has to consult that repo again. These are the conventions and
hard-won lessons a fresh build must replicate or consciously drop. Where
kestrel deviates, deviate on purpose and note it here.*

## Pipeline shape (proven)

collect → curate → coverage-critic → commit → deliver, with a per-digest-day
**state machine in the digest file's own frontmatter**:
`status: building | final` · `window_start` · `as_of` · `coverage: na | pending | done`.

- **Day boundary: 5am ET → 5am ET**, DST-aware. (Use `zoneinfo`, don't
  hand-roll DST like the reference did.)
- **Building digests are rebuilt in place** (full regenerate over the growing
  window), not appended.
- **Freeze-then-critique ordering:** each daily run first finalizes any prior
  building day (re-collect with the *precise final window* — not the partial
  building collection), then runs deferred coverage checks, then rebuilds
  today-so-far.
- **Coverage check waits for ~10am ET** (`COVERAGE_HOUR_ET`) so the benchmark
  newsletters have actually published; earlier finalization sets
  `coverage: pending` and a later run completes it.
- **Weekly** reads the 7 daily digests as pre-digested history + one fresh
  7-day collection pass + threads state; runs Saturdays.

## Curation (the judgment layer, as implemented)

- Headless `claude -p` (model via env `DIGEST_MODEL`, default opus),
  `--permission-mode acceptEdits`, file tools only — **curation runs with NO
  web access**; it works strictly from collected files on disk.
- Prompt rules that did the real work: frame-neutral · signal-over-noise ·
  drop Reddit/PR-newswire · trim GDELT finance-bleed · trim arXiv to a
  handful · **prioritize watchlist entities** · de-dupe vs. prior digest (by
  judgment, no hash dedup exists) · if an input is empty say so and carry
  threads forward · end with a 3-line summary · digest opens with a
  **throughline** line, axis-grouped sections, one link per bullet, bold
  lead phrase.
- Format was taught by "match the two most recent digests exactly" — seed
  kestrel with a fixed template instead (less fragile than by-example).

## Coverage critic (the recall guarantee, as implemented)

- Headless claude **with** WebSearch/WebFetch, at finalize + weekly only.
- **Baseline = named curated newsletters** (ai lens): The Rundown AI, TLDR
  AI, The Neuron, The AI Daily Brief; weekly adds Import AI, Last Week in AI.
- Output: appendix section — *they led with → we missed* / *both covered* /
  *we had → they didn't* — plus a dated entry in a coverage log.
- **Auto-grows watchlist/threads** from misses (with `# auto-added` reason
  comments). ⚠ Reference only did this for the **ai lens** — mh had no
  critic and no auto-grow at all; kestrel must pick baselines per lens
  (money + mh need benchmark publications chosen).
- **YAML guardrail:** after any LLM edit to watchlist/threads, re-parse with
  `yaml.safe_load`; on failure, `git checkout --` the file. Keep this — it's
  the safety net for LLM-mutated state files.

## Collector lessons (per source)

| source | carry into fresh code |
| --- | --- |
| GDELT | 1 req/~5.5s pacing · 429 retry ×3 linear backoff · OR-batch terms in 6s · dynamic timespan to window · English filter client-side |
| OpenAlex | key effectively **required** (since 2026-02) + real `mailto` (mint a kestrel address — do NOT reuse the reference's) · must bound BOTH from/to publication dates or future-dated placeholders (2050) poison the sort |
| CourtListener | `type=r` (RECAP) not `type=o` · window client-side on `dateFiled` (server `filed_after` drops ongoing suits) · 1.5s pacing · heaviest throttle |
| SEC EDGAR | declared-contact User-Agent required · forms 8-K,10-K,S-1 · URL rebuilt from `_id` + CIK, raw-search fallback |
| Manifold | ai-lens release_watch terms only · never windowed (live snapshot) · dedup by market id |
| HN Algolia | `search_by_date` + numericFilters window · dedup by objectID AND normalized title |
| Federal Register | themes-only terms · dedup by URL |
| ClinicalTrials | v2, `LastUpdatePostDate:desc` sort is trustworthy · conditions-only |

Cross-cutting: every source degrades gracefully (one failing API never kills
the run) · per-source dedupe by normalized-title-prefix (80 chars) · precise
`(window_start, window_end)` override threaded into every source ·
**loudly log every skipped source** (silent drops read as coverage) · global
socket timeout before feedparser (no per-feed timeout exists) · browser-like
UA for RSS (Cloudflare 403s bot UAs) · keep `probe` (API connectivity) and
`audit` (feed-manifest validation) utilities.

## Delivery + feedback (as implemented)

- Auth: `authctl get gdrive:<alias>` (OAuth refresh-token, full `drive`
  scope). Reference account was a personal account — **confirm which
  account kestrel's folder lives on before wiring.**
- **Stable Doc per day**, upserted by exact title in one folder; re-push is
  a no-op unless `--replace` (destructive: deletes Doc + all comments —
  keep opt-in only). Upload = markdown with Docs mimeType (Drive's native
  md→Docs conversion; no Docs-API formatting calls).
- Comment pull: Drive comments API, resolved excluded by default, quoted
  anchor text + replies preserved → dated feedback file per digest day.
- ⚠ Reference used **UTC "yesterday"** in the sync script vs. ET digest-days
  everywhere else — kestrel should use the ET digest-day consistently.
- Nothing auto-acts on feedback; the loop closes by a human/agent reading
  the feedback file and resolving comments in the Doc.

## Scheduling (history)

The reference's cloud routine died on **blocked egress** (0 items from every
source) and was never revived; everything ran manually-local after that.
Requirement, not implementation: daily run ≥1×/day (after ~10am ET for the
coverage check), weekly on Saturday. Kestrel's runner: this container has
verified egress (2026-07-20) and authctl — run it here.

## Env vars the reference consumed

`DIGEST_MODEL` · `COVERAGE_HOUR_ET` · `OPENALEX_API_KEY` · `OPENALEX_MAILTO`
· `COURTLISTENER_TOKEN` (+ unused-but-provisioned `DATA_GOV_KEY`, `LDA_KEY`,
`OPENSECRETS_KEY`). Hand-rolled `.env` loader — kestrel can just use
python-dotenv or keep it simple.
