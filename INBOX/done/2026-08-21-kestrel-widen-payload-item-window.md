<!-- outcome block prepended on close; the brief follows unchanged below -->

outcome:   fixed, per the shape of the fix the brief itself suggested
closed:    2026-08-25
closed-by: theprojection-corpus / agent session
commit:    2db4051

**Fixed as suggested**: the calendar-week walk at
`render_read.py`'s old ~347 is now a fixed `ITEM_WINDOW_DAYS = 14`
lookback ending at `today`; `week_start`/`today` are untouched so
calendar-week framing still works for a client that wants it. Verified
live: a real run now ships 13 days of items (2026-08-12 through
2026-08-24) instead of whatever the current calendar week alone would
have held.

**One display-layer consequence found and fixed while verifying this**,
since it wasn't obviously covered by "the instance owns the display
layer": `templates/read-shell.html`'s masthead hardcoded
`P.days.length+"/7 days in"` — with `days[]` now spanning 14 days
instead of a calendar week, that stat would have shown nonsense like
"13/7 days in". Fixed to filter `days` back down to the current calendar
week before computing that one stat, so it keeps its original meaning.

⚠️ **Real cost, not hidden**: the live payload jumped from ~1132 KB
(per STATUS.md, the last real run) to ~1920 KB on this widened window —
well past the existing 600 KB soft cap, which the file already warns
about on every run. The degradation rule the brief flagged as
"probably wants to land together" (dropping item html >3 days old) is
still NOT implemented — same unimplemented gap as before this fix, just
now hit at a bigger number. Worth deciding whether that lands before or
shortly after this ships to a real `/daily` run.

---

# Widen the payload's item window so the display layer can offer time-window views, instead of the renderer deciding

from:      kestrel / engine session
date:      2026-08-21
kind:      gap
touches:   theprojection_pipeline/render_read.py:347 (`week_start = today -
           timedelta(days=today.weekday())`) and the `for i in range(7)`
           loop just below it (~352-355)
done-when: The payload carries enough item history that a client can
           render "this week", "last 7 days", or any narrower cut WITHOUT
           a re-render. The instance owns which view is default; the
           engine just ships the data.
artifact:  none

## Path note

Originally kestrel GitHub issue #17, filed against `tools/render_read.py`.
Now lives at `theprojection_pipeline/render_read.py` in this repo. Read
the current file directly today (2026-08-21) — the bug is unchanged,
line 347 exact match to the original report:

```python
week_start = today - timedelta(days=today.weekday())   # back up to Monday
for i in range(7):
    d = week_start + timedelta(days=i)
    if d > today: break
```

## The ask, in one line

Stop deciding the window in the renderer. Ship ~14 days of items and let
the view choose. The instance owner's framing: "why don't we just provide
button-views like the feed lenses? Let me decide on the fly what I want
to see, with a default view alongside any other cuts."

## What the code does now, and why it bites

It walks from the Monday of the current calendar week to today. On a
Monday, `today.weekday()` is 0, so `week_start == today`, the loop runs
exactly once, and the payload can contain only Monday's own content.

From the original report's measurements: on Monday 2026-08-10 a `/daily`
run closed a ~23-hour backlog whose content was almost entirely dated
08-09 (a Sunday) — the payload rendered with ~0 items immediately after
the largest catch-up in weeks. Same again 2026-08-11: the payload held 3
items while the briefing layer was working from ~40 bullets, which
separately broke a link-resolution feature built on `payload.items` as a
lookup table. Nothing is lost — digest archives and thread timelines stay
intact, and briefing pages use a different, non-week-gated path — but it
recurs on every Monday that follows a catch-up run, which is most of
them, since weekends are exactly when backlog accumulates.

## Why "just switch to rolling 7" is the wrong ask

That was the original reporter's first instinct and the instance owner
rejected it, correctly: a calendar week is not only a lookback, it's also
how the reporting cycle is framed, and a plain rolling-7 throws that
framing away to fix a Monday bug. The better shape: **the payload carries
a superset, the client cuts it** — roughly 14 days of items, plus the
`week_start`/`today` fields already in the payload, so a view can still
draw the calendar-week boundary when it wants to.

## Half the work is already done — `upcoming` needs no change

`upcoming` is already unwindowed: `render_read.py:396` reads the whole
expectations ledger (`yaml.safe_load(...)["expectations"]`, confirmed
still exact at line 396 today) and ships all of it — at filing time, 61
entries with due dates running from 2026-08-10 out to 2027-12-31. So the
forward half of any "N back / N forward" view needs no engine change; it
is a display-layer filter, done on the instance side
(`templates/read-shell.html` hardcoded a 0-1 day forward horizon at
~line 260 — instance's to widen).

**So the only engine-side change is the backward item window** — the loop
at render_read.py ~352-355.

## Shape of the fix (yours to judge)

Replace the calendar-week walk with a fixed lookback — `today - 13 days`
through `today`, iterating days that actually have digests — and leave
`week_start`/`today` in the payload untouched so calendar framing stays
available to the client. If a configurable value is preferable to a
constant, `kestrel.yaml` would be the natural home, since instances may
reasonably differ.

## One consequence worth pricing in — confirmed still true today

The rendered artifact was already 786-795 KB against the 600 KB soft cap
at filing time, and the degradation rule the warning points at ("drop
item html >3 days old") was never built. Confirmed still true today: the
warning still fires unconditionally —

```python
# render_read.py ~435-436
print(f"⚠ over {PAYLOAD_SOFT_CAP//1024} KB soft cap — apply the "
      "degradation rule (drop item html >3 days old)", file=sys.stderr)
```

— with no code implementing that degradation rule anywhere in the file. A
14-day window makes the payload larger mid-week than a calendar week
does, so this change and that unimplemented degradation rule probably
want to land together rather than separately.

## What the instance is doing regardless

Building view toggles against whatever the payload contains, widening its
own forward horizon, and adding a Monday-specific "what happened over the
weekend" module. Those work today; they just have less to show on the
backward side until this lands.
