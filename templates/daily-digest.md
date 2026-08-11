---
lens: {frontier-ai | mental-health | global-capital}
date: {YYYY-MM-DD}            # the ET digest-day (5am→5am)
status: {building | final}
window_start: {ISO timestamp}
as_of: {ISO timestamp}        # building only
coverage: {na | pending | done}
---

# {Lens label} — {date}

*Curated from ~{N} items ({collection mode: pipeline | agentic-interim};
sources: {source list}).*

## Today's throughline

{One short paragraph: the single thread that ties the day together. If the
day is thin, say so plainly and carry the open threads forward.}

## {Axis sections — per lens:}

<!--
  frontier-ai:    Product & access · Policy & governance · China · People &
                  accountability · Capital & corporate · Research & safety
  mental-health:  Product & market · Policy, regulation & legal · Research &
                  evidence · Capital & corporate · Clinical safety & harm
  global-capital: Capital in my markets · Deals & filings · Power & lobbying
  Omit an axis with nothing real. Every bullet: **bold lead phrase**, one
  sentence, frame-neutral — AND an invisible annotation line (reframe
  2026-07-22) making the digest the durable tagged item record:
    - **Bold lead** — sentence. ([Primary source](url), [Corroborating](url))
      <!-- k: t=thread-slug,thread-slug e=entity-slug axis=section-slug - ->
  t= 0–3 threads.yaml slugs · e= watchlist-derived entity slugs ONLY (a new
  entity = a map add through the loop first) · at least one of t=/e= unless
  the item is deliberately ambient. tools/render_read.py parses these.

  SOURCES — CITE EVERY SOURCE YOU ACTUALLY USED, not just one (ben-steer
  2026-08-11). This line previously read "exactly one source link", and that
  rule was destroying work: curators already consult two to four sources per
  bullet to verify an event against a primary source, then threw all but one
  away. Those discarded links are exactly what a reader wants. The site now
  publishes a STORY page per timeline entry — headline, summary, and its
  sources with credibility badges (publish/adapter.py `build_stories`) — and
  a story is only ever as well-sourced as the bullet it came from.

  Order them PRIMARY FIRST (the filing, the company newsroom, the paper, the
  government page), then the corroborating coverage that made you confident.
  Two to four is the useful range. One is right when only one exists; a long
  tail of aggregator restatements is noise, not sourcing.

  NEVER cite a `news.google.com` link — it is a redirect, not a publisher, so
  it can be neither attributed nor credibility-rated. Resolve it to the real
  article first. 45 such links reached the timelines before this was written
  down; story pages now render them as explicitly unattributable, which is
  the honest treatment but not one worth adding to.

  The BOLD LEAD is load-bearing beyond style: readouts.py's pack extractor
  keys on `**Bold lead** — sentence.` and falls back to an 80-character slice
  when it cannot match, which silently truncated seven bullets mid-word
  before it was caught on 2026-08-11. Keep the bold phrase a self-contained
  FACT (not a label like "Late catch:"), keep the ` — ` separator, and do not
  nest *italics* inside the bold span.
-->

## ⏱ Release-watch & markets   <!-- frontier-ai only -->
## 🧪 Clinical trials           <!-- mental-health only -->
## 📊 Macro strip               <!-- global-capital only: 3-6 indicator lines (FRED/BoC), delta vs last read -->

## ⏳ Upcoming & expected

{Today's expectation flips from `attention/upcoming.yaml` (✅ hit ·
🚧 slipped · ⚠️ passed-silent — the loud one), then anything due in the
next 7 days. "No flips; N pending" is a valid entry — never omit.}

## 🔄 Map changes

{Every attention-map edit since the last daily, one line each:
`+ thread ai/foo — <why> (ben-steer 07-21)` · `− org "Pear Therapeutics"
(decay-review 07-19)`. "None" is a valid entry — never omit the section.}

## 🧵 Thread candidates

{0–3 offers: `**candidate:** <one-line story> — track it? (source)`. Promoted
by a word from Ben; unanswered candidates may reappear once, then drop.}

---
{Three-line summary: the day in three sentences, written to be heard.}

<!-- At finalize, the coverage critic appends:
## Appendix — Coverage check vs. benchmarks
**They led with → we missed:** …
**Both covered:** …
**We had → they didn't:** …
-->
