<!-- status note added 2026-08-25 — reviewed, deliberately deferred, not touched -->

status:    reviewed 2026-08-25, deliberately NOT attempted in the same
           pass as the four mechanical INBOX fixes landed that day
           (commit 2db4051). This is a genuine design task, not a bug
           fix: `build_pack()`'s own `breaking`/`news` items already
           carry `{text, url}` as a bound pair, but the model is asked
           to WRITE a bullet in its own words and then separately choose
           which pack item's url belongs to it — closing that gap for
           real means changing what shape the model returns (e.g. a
           `ref` pointing back to a specific pack item, resolved to a
           url in code afterward, never trusted from the model directly)
           and bumping SUMMARY_SHAPE_VERSION/BRIEFING_SHAPE_VERSION
           again so soon after the 2026-08-25 bump. That is a real
           change to the model contract across the whole site and
           deserves its own sitting with time to get the schema and
           validator right together, not a rushed addition alongside
           unrelated regex fixes. Left open.

---

# readouts.py's pack still hands the briefing model a bag of facts and a bag of urls, so it can attach the wrong url to the right fact

from:      kestrel / engine session
date:      2026-08-21
kind:      gap
touches:   theprojection_pipeline/readouts.py — `build_pack()` (~line 789),
           `derive_sections()` (~line 301) which fills `breaking`/`news`,
           and `_check_url_provenance()` (~line 494)
done-when: `build_pack()` emits each candidate fact with its url already
           bound as a pair (e.g. `{text_hint, url}`), so a briefing model
           selects a pre-bound pair instead of assembling
           fact-text + url itself — removing the *opportunity* for a
           correct-fact/wrong-url mismatch rather than merely detecting one.
artifact:  none

## Path note

This was originally filed against kestrel's own `tools/readouts.py`
(GitHub issue #4 on benthepsychologist/kestrel) before that file moved to
theprojection-corpus. It now lives at
`theprojection_pipeline/readouts.py` in this repo — confirmed by reading
the file directly today (2026-08-21). Line numbers below are current as
of that read, not the original issue text.

## What the original issue reported (three gaps, one instance-day: 2026-08-04)

Running `/daily` step 6a's briefing generation surfaced three problems in
the same pipeline: (1) the `watch` field's shape was documented as prose
("1-3 sentences...") but validated as a JSON array, so every briefing
agent returned a string and got rejected — a wasted round every run;
(2) `--apply` never checked that a bullet's `url` actually came from that
scope's own source pack, so a fabricated-but-plausible URL passed
silently; (3) even when a url *is* from the pack, nothing stops it being
attached to the wrong fact — a real "Maine bans AI therapy" bullet
shipped with a real CNBC link about an unrelated xAI lawsuit, because
both were true facts drawn from the same pack and simply paired wrong by
the model. That one reproduced twice, independently, same day.

## What's already fixed — verified today, so don't re-do this

**Gap 1 (watch shape) is fixed.** `normalize_briefing()` (readouts.py
~423-444) now sentence-splits a bare string via `_split_sentences()`
rather than crashing/rejecting, and the shape text handed to the model
now explicitly reads: *"ARRAY of N-M strings, NOT a single string... Do
not open with the word 'Watch'"* (~line 882). The code comment at line
433 cites this exact bug ("INBOX 2026-08-04, gap 1") as the reason the
coercion exists.

**Gap 2 (fabricated URL) is fixed.** `_check_url_provenance()`
(~line 494) rejects any bullet `url` that isn't a set member of
`_scope_source_urls()` (~line 478 — every url in that scope's
`breaking`/`news`, plus each of the scope's own `/threads/<slug>/`
paths). The docstring cites "INBOX 2026-08-04 gap 2" directly. A
fabricated URL like the original ISM press-release example is no longer
possible to get past validation.

## What's still open — this brief is only about this part

**Gap 3, the mismatched-url case, is NOT fixed**, and the original issue
said as much: gap 2's membership test can't catch it, because the url
*is* legitimately in the pack — just attached to the wrong fact. Today's
`build_pack()` still ships `breaking`/`news` as parallel lists of items
(each with its own real `url`), and the shape instructions
(~lines 826-837) tell the model to pick "the source link from
`breaking`/`news` for that fact" — i.e. the model still does the
fact-to-url binding itself, which is exactly the step that broke twice on
2026-08-04.

**Suggested fix, unchanged from the original report:** have `build_pack()`
emit each candidate as an already-bound pair — `{text_hint, url}` — so
selecting a fact and getting its correct url are the same action, not two
independent choices a model can cross. This is a `--pack`/`build_pack()`
schema change, not a validation change, and is a design call left to
whoever picks this up. A model-based coherence checker (bullet vs url) was
also considered and explicitly deprioritized in the original report as
probably not worth it for ~20 bullets/run.

## Why it matters

These render as clickable citations on a public site whose premise is
that every claim carries a receipt. A wrong-but-real receipt (real fact,
real url, wrong pairing) is worse than a missing one, and reads as more
credible than an obviously-fabricated link would.
