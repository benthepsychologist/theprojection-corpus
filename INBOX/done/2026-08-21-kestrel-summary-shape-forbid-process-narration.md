<!-- outcome block prepended on close; the brief follows unchanged below -->

outcome:   fixed, both the rule text and mechanical enforcement
closed:    2026-08-25
closed-by: theprojection-corpus / agent session
commit:    2db4051

**Rule text added to both `shape["rules"]` arrays** (summary and
briefing), using the brief's own suggested wording near-verbatim: no
crawl/sweep/pass/batch/agent/buffer/digest/digest-day/backfill/re-index/
"our record"/"this run"; corrections stay in as facts about the world,
not about the lookup; dates are event dates, never look dates.

**Mechanical enforcement added too** (`_check_no_apparatus`), wired into
`validate_summary` (gist, every bullet, watch, each front beat) and
`validate_briefing` (gist, every lead/section bullet, every watch line) —
in the same family as `_check_link_floor`/`_check_url_provenance`, per
the brief's "if it's worth it" suggestion. **Deliberately narrower than
the rule text's own vocabulary**, taking the brief's own "sweep" false-
positive caveat and generalizing it: excluded `sweep`/`pass`/`batch`/
`agent`/`buffer`/`digest` from the mechanical check because each has an
ordinary, frequent, non-apparatus meaning in this corpus's real domains
(a tariff batch, a spy agent, a buffer zone, a bill that passes, a
market that digests news, an election sweep) — flagging those would be
false-positive-prone exactly as the brief warned "sweep" would be. The
mechanical check catches the unambiguous subset (`crawl`, `digest-day`,
`backfill`, `re-index`/`reindex`, `this run`, `our record`, `our
lookup`); the rule text still carries the fuller vocabulary for the
model itself to avoid.

**`SUMMARY_SHAPE_VERSION` 2→3, `BRIEFING_SHAPE_VERSION` 1→2** — bumped so
every cached readout (227 scopes at time of fix: 64 entity + 63 node +
96 thread + 3 lens + 1 front) regenerates against the new rule on the
next `--pack`/`--apply` pass, not just newly-changed ones. This is a
real cost worth knowing about before the next `/daily` run: it's a full
regeneration, not incremental.

---

# The summary shape lets a model narrate the pipeline to the reader — nothing in shape.rules forbids it

from:      kestrel / engine session
date:      2026-08-21
kind:      gap
touches:   theprojection_pipeline/readouts.py — the `shape["rules"]`
           arrays in `build_pack()`, currently at ~lines 844-849 (summary
           scopes) and ~lines 889-898 (briefing scopes)
done-when: A generated summary cannot describe the apparatus that
           produced it. The rule is stated in the shape the model is
           given, and ideally enforced in validation the way
           `_check_link_floor` and `_check_url_provenance` already
           enforce their invariants.
artifact:  none

## Path note

Originally kestrel GitHub issue #16, filed against `tools/readouts.py`.
Now lives at `theprojection_pipeline/readouts.py` in this repo. Read the
current `shape["rules"]` blocks directly today (2026-08-21) to confirm
this gap is still open — it is. Neither rules array mentions process
narration:

```python
# summary scopes, ~844-849
"rules": [
    "Every fact must trace to `breaking`, `news`, or `recent_timeline`.",
    "Never carry a figure forward from an older item as if current.",
    "`watch` (thread field) is a STANDING question, not today's news.",
    "No emoji outside the typed set; never let an emoji carry a fact.",
],

# briefing scopes, ~889-898
"rules": [
    "A fact may appear in `lead` AND in its section...",
    "Every fact must trace to `breaking`, `news`, or `recent_timeline`.",
    "Never carry a figure forward from an older item as current.",
    "`watch` (thread field) is a STANDING question, not news.",
    "No emoji outside the typed set.",
],
```

All of these constrain sourcing and structure — provenance and form.
Nothing says the summary is about the world rather than about the process
that observed it.

## What is (or was, as of the original report) live on theprojection.org

Real reader-facing summary bullets, generated through this exact pack
shape:

> "A July 24 crawl surveyed Big Tech's health pushes together, covering
> Amazon alongside Microsoft, Google, and Apple in the same batch."

> "Two independent crawl agents flagged Meta's gas pivot as significant in
> the same research pass."

> "A July 27 crawl mapped the AI power buildout across four actor types in
> a single pass."

> "Whether a dedicated crawl turns up a Humana-specific AI-denial finding,
> rather than exposure only through industry-wide litigation." (a `watch`)

The instance owner's verdict, verbatim: *"some of our summaries in
various places are clearly methodology and crawl summaries (what the
agent did) rather than summaries of the news and/or what it means.
Yuck."* A reader doesn't know what a crawl is, how many agents ran, or
what a "pass"/"batch" means — none of it is a fact about the world.

## Scale, from the original scan

A scan of the export at filing time found 15 scopes carrying apparatus
language in a reader-facing summary, mostly `thread:`/`entity:`/`node:`
scopes. Breaking it down: ~11 are genuine process narration; 3 are
*corrections* to the record (a claim once reported that turned out
false) — which ARE reader-relevant and should survive, just rewritten as
claims about the world rather than about the pipeline's own lookup; 2 are
internal jargon rather than process ("the digest-day is about two hours
old" means nothing to a reader).

## Why the shape permits it

`recent_timeline` entries carry provenance markers (`⟨crawl
2026-07-27⟩`) that do their job as internal bookkeeping inside the
timeline — and then leak one layer up when a model handed that timeline
reasonably treats "the crawl" as part of the story, because nothing tells
it otherwise.

## Suggested rule text (adapt freely)

> The pipeline is invisible to the reader. Never mention how a fact was
> obtained: no crawl, sweep, pass, batch, agent, buffer, digest,
> digest-day, backfill, re-index, "our record", "this run". Provenance
> markers in `recent_timeline` are internal bookkeeping, not content.
> Where the record contains a CORRECTION, keep it — but state it as a
> fact about the world ("Reports of X in late July were incorrect")
> rather than about our lookup ("a July 27 crawl traced X to a stale
> re-index"). Dates in a summary are the dates events happened, never the
> dates we looked.

## Enforcement, if it's worth it

A validator check in the same family as `_check_link_floor` /
`_check_url_provenance` (readouts.py ~457, ~494) would catch this
mechanically — a token blocklist over `gist`/`bullets[].text`/`watch`,
rejecting rather than warning, since the existing checks reject. The
banned vocabulary is small, stable, and unlikely to appear innocently in
this domain's actual news. One caveat from the original author's own
scan: "sweep" produces false positives ("a 42/42 sweep on IMO-class
tasks" is a benchmark result, not a crawl) — either drop that token or
require it adjacent to a first-person/process context.

## What the instance did as a workaround (not a fix)

Regenerated all 15 offending scopes with an explicit no-apparatus
instruction in the prompt, and fixed two digest throughlines whose own
opening sentences leaked "digest-day" onto the public front page via the
curated-gist path. That fixed that day's output; it does not stop the
next generation from doing it again, which is why this is filed rather
than treated as resolved.
