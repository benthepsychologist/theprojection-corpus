# The digest-bullet extractor silently truncates mid-word to 80 chars when a bullet doesn't match the expected lead-phrase convention

from:      kestrel / engine session
date:      2026-08-21
kind:      bug
touches:   theprojection_pipeline/render_read.py:296-304 (`parse_digest`'s
           bullet-to-title extraction; the `title` field it produces is
           then read as `i["title"]` — the pack's `text` — by
           theprojection_pipeline/readouts.py:318-322)
done-when: A bullet that doesn't match the expected lead-phrase convention
           either parses correctly or produces a visible warning. It must
           not silently emit a mid-word 80-character fragment to a
           reader-facing surface.
artifact:  none

## Path note

Originally kestrel GitHub issue #14, filed against `tools/readouts.py`.
The actual truncation happens one file over: it's in
`render_read.py`'s `parse_digest()`, which `readouts.py` imports and
consumes (`from theprojection_pipeline.render_read import (... parse_digest ...)`,
readouts.py:67). Both files now live in this repo under
`theprojection_pipeline/`, confirmed by reading them directly today
(2026-08-21). Line numbers below are current.

## The bug, as it stands today

```python
# render_read.py:296-304
for b in re.finditer(
        r"^- ((?:(?!^- )(?!^#).)+?)\n  <!-- k: ([^>]*?) -->",
        src, re.S | re.M):
    text = " ".join(l.strip() for l in b.group(1).strip().split("\n"))
    ann = b.group(2).strip()
    tags = dict(kv.split("=", 1) for kv in ann.split() if "=" in kv)
    lm = re.search(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", text)
    tm = re.match(r"\*\*([^*]+)\*\*", text)
    title = tm.group(1).strip() if tm else text[:80]
```

`tm` looks for a bold lead phrase (`**...**`) at the very start of the
bullet. When it doesn't match — anything that deviates even slightly from
the `- **Bold lead phrase** — sentence.` convention — the fallback is a
raw `text[:80]` slice: a fixed 80-character cut with no word boundary
awareness, and nothing logs that the fallback fired. This `title` value
is then read straight through as the pack's bullet `text`
(`readouts.py:318-322`: `rec = {"text": i["title"], ...}`), so a
truncated fragment reaches the briefing model — and, if a careless
briefing agent runs with it rather than dropping it, the reader — with no
signal anywhere that it's a fragment rather than a genuinely short bullet.

## What happened, from the original report (2026-08-11 `/daily` run)

Three of four briefing-writing agents independently reported pack items
arriving truncated mid-word and dropped the affected facts rather than
guess at the missing content. Between them they discarded seven distinct
items, including a $567M court judgment against Meta, an OpenAI-APA
teen-safety partnership, and a data-center-opposition midterm story a
coverage critic had just caught as a recall miss the same day. The
digests themselves were fine in `artifacts/digests/daily/` — the loss was
entirely in extraction.

Every failing bullet deviated from the bold-lead-phrase convention in one
of these observed shapes:

- an emoji before the bold marker, plus a colon *inside* the bold:
  `- ⚠️ **Critic-caught, added 2026-08-11:** AI data-center opposition has…`
- bold closed, then a colon instead of an em dash:
  `- 💡 **Also circulating, not verified as a discrete deal**: SemiAnalysis…`
- nested single-asterisk italics inside the bold span:
  `…published in *Science* that their Evo 1/Evo 2 models…**`
- a bold lead that is a *label* rather than a fact, so even a successful
  match carries no content: `- **Late catch, true event date
  2026-08-07:** the Financial Times reported…` extracts as the 39-char
  string `"Late catch, true event date 2026-08-07:"`.

Confirmed by regenerating packs after normalizing all seven bullets to the
documented convention: broken extractions went from 7 to 0, no other
change. The instance's own workaround was to hand-normalize those seven
bullets in `artifacts/digests/daily/`; nothing in the extractor was
touched.

## Why it's worse than an ordinary bug

The failure is silent in both directions. Nothing in `--pack`, `--apply`,
or `--export` warns that a bullet failed to parse — a truncated fragment
is indistinguishable from a genuinely short bullet. A careful briefing
agent drops the fact (silent under-coverage, what happened here); a
careless one publishes a sentence reconstructed from a fragment (silent
fabrication). Both are worse than a loud parse error.

## Two directions for the fix, not mutually exclusive

1. **Parse more tolerantly** — accept an emoji prefix, a colon
   terminator, and nested emphasis inside the bold span; treat the first
   sentence after the lead as the body regardless of separator.
2. **Fail loudly** — if the lead-phrase pattern doesn't match, emit a
   warning naming the digest file and line rather than falling through to
   a fixed slice. Even keeping today's strict parse, a warning would have
   surfaced this the first time it happened rather than on the day three
   agents happened to notice independently.

A note in the digest template that the `** — ` separator is load-bearing
for extraction (not merely stylistic) would also help — curating agents
have no way to know that today.
