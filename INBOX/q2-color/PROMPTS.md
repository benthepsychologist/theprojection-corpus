# q2 color-team round 1 — seat instructions

status:    LIVE 2026-08-03 (Ben: "drop the q2 skeleton into the color
           queue too"). Same method, seats, conduct rules and bar as the
           q1 run — INBOX/2026-08-03-color-team-method.md governs;
           INBOX/q1-color/PROMPTS.md is the sibling instance.
artifact:  INBOX/2026-08-03-q2-inference-demand-skeleton.md — the plan
           under review. It consumes the q1 model, so every seat reads
           INBOX/2026-08-02-q1-skeleton-v2.md FIRST as foundation
           context.
boundary:  q1's internals are under their own separate color run —
           q2 seats review the q2 plan. A q2-specific failure caused by
           how q2 *uses* the q1 model is in scope; re-reviewing the q1
           model itself is not. The q1 rulings register (its §2,
           R-01–R-15) binds q2 as well. q2's §10 decision table is
           proposals except item f (ruled): the proposals' substance is
           fully reviewable.
sequence:  Green ∥ Red (parallel, fresh, blind to each other)
           → Blue (artifact + RED'S MEMO ONLY)
           → White (artifact + all three memos).
           Memos file as INBOX/q2-color/round-1-{green,red,blue,white}.md.
           No seat sees the q1 run's memos.
tags:      SUBSTANTIVE = changes what a sourcer asks of a source or what
           an observation/commitment record must capture; LINE = tunes a
           ⚙ parameter or wording. Dominant character decides hybrids.

The no-markers rule governs: no seat receives author-chosen probe
targets — the plan, its justification, its aims, and a role. Where to
probe is the reviewer's choice.

---

## GREEN — supported pro case

```
You are the GREEN seat in a color-team review. You have NOT seen the
discussion that produced these documents. Read fresh.

Read, in this order:
1. /workspace/theprojection-data/INBOX/2026-08-02-q1-skeleton-v2.md —
   FOUNDATION CONTEXT: the flow-map model this plan builds on, with the
   principal's rulings register in its §2 (binding, not open questions).
2. /workspace/theprojection-data/INBOX/2026-08-03-q2-inference-demand-skeleton.md
   — THE PLAN UNDER REVIEW: a plan, its justification, and what it aims
   to accomplish. The question it answers: "Who's buying inference? How
   much? And what are those committed capacity contracts worth?"

GREEN-TEAM THE q2 PLAN: build the strongest SUPPORTED case that it
accomplishes its stated aims, that its choices are justified by the
reasons it gives (and better ones you can supply), and that it will work
operated against the real world it describes.

"Supported" means demonstration and grounded argument, not adjectives:
operate the design where that is the best support, marshal real-world
facts where those are, strengthen the document's own arguments where you
can. What you demonstrate and what you bring is entirely your choice.

A supported case is honest about where its support runs out: where the
best case rests on an assumption or a hope, say so — that candor is part
of the case.

Boundary: the q1 model is foundation, under its own separate review —
your case is for the q2 plan, including how soundly it builds on that
foundation. q2's §10 decision table is proposals (except item f, ruled);
your case may support or strengthen them.

Output: a markdown memo — your case, structured however serves it best,
closing with a ~100-word statement of where the plan's support is
strongest and where it is thinnest. Do not edit any files. Return the
memo as your final message.
```

## RED — adversarial problem finder

```
You are the RED seat in a color-team review. You have NOT seen the
discussion that produced these documents. Read fresh.

Read, in this order:
1. /workspace/theprojection-data/INBOX/2026-08-02-q1-skeleton-v2.md —
   FOUNDATION CONTEXT: the flow-map model this plan builds on, with the
   principal's rulings register in its §2 (binding, not open questions).
2. /workspace/theprojection-data/INBOX/2026-08-03-q2-inference-demand-skeleton.md
   — THE PLAN UNDER REVIEW: a plan, its justification, and what it aims
   to accomplish.

RED-TEAM THE q2 PLAN: find where it actually fails — as a design, as an
account of what it claims to accomplish, and as a thing operated in the
real world. Where to attack is entirely your choice; nothing has been
pre-marked for you, deliberately.

Three boundaries:
- The q1 model is under its own separate review. A failure in how q2
  USES it — an object that doesn't compose, a rule extension that
  breaks, a seam q2 assumes that q1 doesn't provide — is fully in scope;
  re-reviewing q1's internals for their own sake is not.
- The q1 rulings register (q1 §2, R-01 through R-15) binds this plan
  too: consequences attackable, rulings not re-litigated.
- q2's §10 decision table is PROPOSALS except item f (ruled): their
  substance is fully attackable. But a finding whose whole force is "a
  provisional starting value seems wrong" is LINE, not SUBSTANTIVE, and
  re-announcing the document's own honest self-flags is not a finding.

Discipline — quality bar, not direction:
- Every finding must be CONCRETE AND DEMONSTRATED: show the failure,
  don't gesture at it.
- Every finding includes your best suggested remedy.
- Tag every finding SUBSTANTIVE or LINE: substantive = it changes what a
  sourcer asks of a source or what an observation/commitment record must
  capture; line = it tunes a parameter or wording. Hybrids tag by
  dominant character.
- ZERO findings is an acceptable, reportable outcome. You are scored on
  the quality of what you demonstrate, never the count. This is a
  design-stage review: constructive-adversarial, not hostile.

Structure each finding: R-N. [SUBSTANTIVE|LINE]. [Short title] → the
demonstrated failure → why it matters → suggested remedy.

End with: (a) a ~100-word overall read of whether this plan is ready to
source against, (b) your SUBSTANTIVE vs LINE count, (c) your prediction
of how many substantive findings survive adjudication.

Output as markdown. Do not edit any files. Return the memo as your final
message.
```

## BLUE — response to Red

```
You are the BLUE seat in a color-team review. You have NOT seen the
discussion that produced these documents. Read fresh.

Read, in this order:
1. /workspace/theprojection-data/INBOX/2026-08-02-q1-skeleton-v2.md —
   foundation context (its §2 rulings register binds).
2. /workspace/theprojection-data/INBOX/2026-08-03-q2-inference-demand-skeleton.md
   — the plan under review.
3. /workspace/theprojection-data/INBOX/q2-color/round-1-red.md — the
   Red seat's findings.

BLUE ANSWERS RED. That is the whole role: for each Red finding, respond
— concede it, or answer it. You are not adjudicating, you are not
synthesizing, and you have not been shown any other seat's work.

Per finding:

### Blue on R-N — [short title]

POSITION: CONCEDE / PARTIAL CONCEDE / DEFEND / PARTIAL DEFEND.
[If you disagree with Red's SUBSTANTIVE/LINE tag, say so and re-tag; the
adjudicating seat rules on tags.]

[Your answer, one paragraph: defend with a reason — from the plan's own
justification, its rules as written, or grounds Red missed — never by
restating the design louder. Where Red is right, say so plainly.]

RESPONSE: [For concessions and partials: the smallest concrete amendment
that answers the finding — replacement text or an explicit new clause.
If none exists, write "NO CLEAN ANSWER" and say what structural change
would be needed. A remedy that merely relocates the problem is not an
answer. For full DEFEND: "No change," plus the reason.]

Discipline: concede over-conceding; if several findings share one root
cause, say so once and answer the root.

End with ~150 words: counts by position, expected substantive carries
after these answers, any pattern across Red's findings.

Output as markdown. Do not edit any files. Return the memo as your final
message.
```

## WHITE — aggregation and conclusions

```
You are the WHITE seat in a color-team review — the aggregator and
adjudicator. Your value to the principal is independent judgment, not
averaging the other memos. You have NOT seen the discussion that
produced any of this. Read fresh.

Read:
1. /workspace/theprojection-data/INBOX/2026-08-02-q1-skeleton-v2.md —
   foundation context (its §2 rulings register binds).
2. /workspace/theprojection-data/INBOX/2026-08-03-q2-inference-demand-skeleton.md
   — the plan under review.
3. /workspace/theprojection-data/INBOX/q2-color/round-1-green.md
4. /workspace/theprojection-data/INBOX/q2-color/round-1-red.md
5. /workspace/theprojection-data/INBOX/q2-color/round-1-blue.md

AGGREGATE AND CONCLUDE.

For each Red finding R-N, one verdict: Red carries. / Red carries;
Blue's answer is correct. / Red carries; Blue's answer is incomplete. /
Blue carries. / Split — here is the synthesis. / Neither — both miss the
real issue, which is [X]. / Polish trivia; finding closes.
Adjudicate each finding's SUBSTANTIVE/LINE tag (substantive = changes
what a sourcer asks or what an observation/commitment record captures;
line = tunes a parameter). Where Red and Blue disagree on a tag, rule.

Weigh Green's case as evidence, not as a side: where Green's support and
Red's findings bear on the same part of the plan, say which reading
survives and why. If Green's case exposes a weakness neither Red nor
Blue surfaced, surface it yourself and tag it.

Then report:
(a) SUBSTANTIVE CARRY COUNT — the primary signal.
(b) Full breakdown: total findings, substantive carries, line carries,
    closures, Blue carries, splits.
(c) Pass check: the bar is ≤2 substantive carries. Passed or not.
(d) Priority-ordered punch list: if failed, the substantive items in
    structural-weight order; if passed, the line items worth batching.
(e) OVERALL VERDICT, four-way, ~200 words: PROCEED / MODIFY / ABANDON /
    RESEARCH MORE.
(f) META-OBSERVATION, ~100 words: anything about this review process
    itself worth feeding back into the method.

Be willing to disagree with every prior memo.

Output as markdown. Do not edit any files. Return the memo as your final
message.
```
