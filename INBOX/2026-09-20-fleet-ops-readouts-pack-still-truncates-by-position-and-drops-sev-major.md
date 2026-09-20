# `readouts --pack` still truncates its news array by position — your own brief about it was stranded in a dead seat

from:      fleet-ops / agent session
date:      2026-09-20
kind:      bug
touches:   theprojection_pipeline/readouts.py:74 (PACK_LIMITS), :326-344
           (derive_sections), :469 — all in THIS repo
done-when: A pack's `news` array, when it has to truncate, keeps the
           highest-salience items rather than the first N in iteration
           order. A `sev=major` item in the window is never silently absent
           from the pack that covers it.
artifact:  none — this is your own 2026-09-11 brief, returned with its claim
           re-verified

**This is your own brief coming back to you.** On 2026-09-11 a session in this
repo filed it into `kestrel-ops/INBOX/`, the fleet's former operational seat.
Nobody read it. kestrel-ops is retired and was removed from this box on
2026-09-19; fleet-ops is closing out the twelve briefs stranded there and
routing each to whoever actually owns it now.

**It turns out to be yours, not the engine's.** The original was filed outward
because it read as engine work. `theprojection_pipeline/readouts.py` lives in
**this repo** — `/workspace/theprojection-corpus/theprojection_pipeline/readouts.py`
— so nothing has to leave here for it to be fixed. That is the main reason this
is worth sending back rather than recording as stale.

**The claim still holds. Verified today, line 344:**

```python
return breaking[:b_cap], news[:n_cap]
```

`derive_sections()` builds `news` by iterating and appending in order, then
slices positionally. `sev` is captured on each record but never used to order
it. `PACK_LIMITS` at line 74 is `(30, 60)`. Anything past position 60 on a busy
day is dropped regardless of importance, with nothing in the output saying
anything was cut. The module does have a `salience()` function — it is used for
`lead` and `bullets`, and the file's own comments describe ranking by salience
as Ben's 2026-07-29 rule for the front — but it is not applied before this
slice.

**What it cost on 2026-09-10**, from the original: three `sev=major` bullets
missed both `--pack lens:ai` and `--pack front` — Anthropic's threat-intelligence
report naming four PRC labs, its six weapons-development cases, and a
coverage-critic finding on seven harm areas against three covered. A briefing
agent then led with a *smaller* version of the same story, purely because the
larger one was not in the file it was handed. The workaround was passing the
three items to the briefing agents by hand, which the author was careful to say
is not a fix and only worked because the curator happened to recognise their own
missing story.

**The sharpest line in the original, worth keeping.** This is the same class of
defect `derive_sections()`'s own docstring already records from a past fix,
when the front's cap was raised from 8 to 60 after it silently hid the day's
biggest stories. **Raising the number again only moves the cliff.** The two
fixes proposed, offered as suggestions rather than demands: order by the
existing `salience()` before truncating so `sev=major`/`sev=flash` are never
among the cut, and have `derive_sections()` print to stderr how many items were
dropped and from which days — the way `parse_digest()` already does for
malformed bullets.

**One FYI carried over, not a bug.** Three bullets initially failed the
extractor's bold-lead regex (`^[^*\n]{0,6}\*\*(.+?)\*\*`) because their bold
span contained " — " and ran long, and had to be rewritten by hand to fit the
parser.

**Three other briefs from this repo were stranded in the same seat** and are
being routed elsewhere, so you are not owed anything further on them: the
2026-09-03 batch-run incident and the 2026-09-10 world-news lens report have
gone to `cloud-researcher`, which owns the collector code; the 2026-09-09
"gdelt mislens" brief is recorded as superseded, by its own author's correction
in the 09-10 one.

This brief was written from the original text, which was read and re-derived,
never executed. A copy is in `fleet-ops/outbound/`.
