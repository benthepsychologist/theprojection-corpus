# Preserve per-story source multiplicity — the pipeline holds hundreds of articles per story and discards all but one link

from:      kestrel / engine session
date:      2026-08-21
kind:      gap
touches:   theprojection_pipeline/render_read.py:302-304 (parse_digest's
           link/title extraction) · theprojection_pipeline/build_world_news.py
           ~430-437 (rss-side item dict) and ~461-469 (gdelt-side item
           dict) · theprojection_pipeline/world_news.py:134-147 (rank(),
           which already computes `urls_sample`) · readouts.py bullet
           schema (optional, lower priority)
done-when: (1) every citation link a curator writes on a digest bullet
           survives into the payload item (a `urls: [{label, url}, ...]`
           list; keep scalar `url` = first link for compatibility);
           (2) attention/world-news.yaml items carry clickable URLs, not
           just outlet counts — at minimum the `urls_sample` that
           `world_news.rank()` already computes; (3) payload items for
           stories with real buffer multiplicity carry a compact
           source-cluster object — `coverage: {outlet_count, articles:
           [{outlet, url, ts}, ...]}` — so a site renderer can show "N
           outlets" with an expandable full link list on demand.
artifact:  none

## Path note

Originally kestrel GitHub issue #6, filed against `tools/render_read.py`,
`tools/build_world_news.py`, `tools/world_news.py`, `tools/readouts.py`.
All four now live under `theprojection_pipeline/` in this repo, not
`tools/`. Verified today (2026-08-21) by reading the current files —
line numbers below are current, not the original issue's.

## Fix 1 — parse_digest keeps only the first link (still present, confirmed today)

`theprojection_pipeline/render_read.py:302`:

```python
lm = re.search(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", text)
```

`re.search` returns only the first match; everything after the first
citation link in a bullet is discarded before it ever reaches `w["items"]`,
the readouts source packs, or the site payload. Curators deliberately
write 2-3 links on big bullets (the original report cites the 08-06
frontier-ai digest's Hassabis bullet, which cited both CNBC and Semafor).
Switch to `re.finditer`/`findall` and emit `urls: [{label, url}, ...]` per
item (readouts.py's `bl()` and the `items.append({...})` block at
render_read.py ~308-329), keeping the existing scalar `url` as the first
entry so nothing downstream breaks.

## Fix 2 — build_world_news drops the URL sample its own ranker computes (still present, confirmed today)

`theprojection_pipeline/world_news.py:134-147`'s `rank()` already builds
`urls_sample` (3 URLs per cluster) at line 147. But
`theprojection_pipeline/build_world_news.py` never copies it into the
written item:

- rss-side item dict, ~lines 430-437: carries `headline`,
  `distinct_outlets`, `outlets_sample` — no `urls_sample`.
- gdelt-side item dict, ~lines 461-469: no url field of any kind.

Net effect in the live artifact: an item can say "63 distinct outlets"
with zero clickable links anywhere in the file. Carry `urls_sample`
through on the rss side; on the gdelt side carry whatever representative
link the event rows can support, or state explicitly in a comment that
gdelt clusters are link-less by construction.

## Fix 3 — the new piece: a per-item source cluster (`coverage`)

At render/payload time, for each curated item, attach a compact cluster
of the buffered articles that match the same story:

```yaml
coverage:
  outlet_count: 63
  articles:            # capped sample, not all matches — say 10-15
    - {outlet: axios.com, url: ..., ts: ...}
    - {outlet: semafor.com, url: ..., ts: ...}
```

Design is open; notes carried over from the original report:

- Clustering already exists — `world_news.py`'s `cluster()` (title-keyword
  + Jaccard-similarity approach, see the function above `rank()`) is
  probably reusable scoped to the item's day + lens. Exact-URL +
  title-keyword grouping is fine for a first pass.
- Normalize `outlet` to a bare domain — the instance plans a
  domain-keyed outlet-credibility table as instance data and will join it
  at render time; a domain-keyed schema makes that join trivial.
- Cap the stored sample (10-15 articles) but keep the true
  `outlet_count` as the headline fact. Note `google_news_rss` URLs are
  Google redirect links, not publisher URLs — prefer gdelt/rss records
  (direct publisher URLs) as sample members where both exist.
- Cross-day dup caveat: buffer dedup is scoped to one (day, source_id)
  file, so the same redirect URL can legitimately reappear across day
  files. A distinct-URL set across the cluster window is needed or
  counts will inflate.

## Scale, from the original measurement (2026-08-07)

Collectors emit one record per article per source with no cross-source
clustering, so the buffer genuinely holds the field: a DeepMind/Hassabis
transition story had 296 raw records / 198 distinct URLs; an
Anthropic-OpenAI Hugging Face breach story had 68 records / 51 distinct
URLs; world-news.yaml's biggest cluster that week had 204 distinct
outlets (Russia-Ukraine). All of it collapses to exactly one link per
rendered card today.

## Optional, lower priority

`readouts.py`'s briefing bullet is `{emoji, text, url}` with a scalar
url. A `urls[]` sibling would let brief bullets carry multiple citations
too — the site mostly needs the item-level `coverage` object from Fix 3,
so this is optional.

## Explicitly NOT engine work (recorded so scope stays clean)

- The outlet bias/lean ratings table — instance data, instance decision
  (licensing questions live there).
- Per-source "what this outlet adds" blurbs — LLM curation duty, scoped
  to major stories at curate time, never auto-generated by the renderer.
- Thumbnails for the source list — the instance's publish adapter already
  fetches og:images per URL and will cap the sample it decorates.

## Why it matters

Found while chasing "are we only getting one article for each story, and
how do we even know we got the best one?" These three fixes are the
gating dependency for a ground.news-style story-page/coverage-list
feature the instance wants to build on the site side.
