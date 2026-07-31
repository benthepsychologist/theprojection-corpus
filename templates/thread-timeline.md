---
thread: {slug}                 # must match threads.yaml slug
title: "{title}"
lens: {lens}
entities: [{entity slugs — mirror threads.yaml}]
opened: {YYYY-MM-DD}
crawled: {YYYY-MM-DD}          # last /crawl backfill pass; omit until one runs
---

# {Title} — timeline

*Watch:* {mirror of threads.yaml watch:, refreshed when it changes}

<!--
  RULES (reframe Phase 0, 2026-07-22):
  - Newest-first dated blocks. /daily REBUILDS today's block at the top
    (rebuild-in-place; re-runs never duplicate). /crawl APPENDS backstory
    at the bottom under the "## ← Backstory" divider. Two writers, two
    zones, no collision.
  - Every entry line ends with a provenance marker: ⟨daily YYYY-MM-DD⟩
    (chain = that day's digest + sidecar) · ⟨crawl YYYY-MM-DD⟩ (chain =
    finding + bundle) · ⟨seed YYYY-MM-DD⟩ (migration) · ⟨steer YYYY-MM-DD⟩
    (Ben dictated). No entry without a marker.
  - Entries are CURATED DEVELOPMENTS, not item mirrors — ambient matches
    update last_seen in threads.yaml but don't earn an entry.
  - Multi-thread items appear in each relevant timeline with prose fit to
    that thread's narrative. The render layer dedupes items by URL;
    timeline entries are prose and never deduped.
  - Bullet format matches the digest rubric: bold lead phrase, one
    sentence, one source link.
  - Resolution closes the file with a "## YYYY-MM-DD — Resolved" entry;
    the file is kept forever.
  - Renames: slugs are immutable; a rename adds `was: old-slug` to
    frontmatter via /steer only.
-->

## {YYYY-MM-DD} — {development headline}

- **{Bold lead}** — {one sentence}.
  ([{Source}]({url})) ⟨daily {YYYY-MM-DD}⟩

## ← Backstory

<!-- /crawl appends below; finding pointer goes in the heading line -->
