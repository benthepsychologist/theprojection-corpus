# q1 color-team round 1 — dispatch-ready seat instructions

status:    DRAFT for Ben's review — these are the literal prompts the four
           seat subagents receive, in the manuscript protocol's
           "PROMPT (verbatim)" tradition. Nothing runs until Ben approves
           (method doc §9, decision g; his standing rule that the red
           team is reviewed before it fires).
artifact:  INBOX/2026-08-02-q1-skeleton-v2.md — review scope is §3 (the
           flow-map model) and §4 (the evidence model). §2 (rulings
           register) is readable context but OUT OF SCOPE for attack.
sequence:  Green ∥ Red (parallel, fresh, neither sees the other)
           → Blue (reads artifact + both memos)
           → White (reads artifact + all three memos).
           Memos filed by the main session as
           INBOX/q1-color/round-1-{green,red,blue,white}.md.
dual-family: if approved, the same four prompts run a second time with
           seats from a non-Claude model family; second run's memos get
           a `-b` suffix. Agreement is compared at the FINDING level in
           a main-session consolidation — a construction both families
           produce independently is highest-confidence; a single-family
           construction is triaged (family-specific noise vs. a real
           catch the other family's priors missed), never auto-dismissed.
           No extraction-style agreement statistics: those instruments
           (Jaccard, claim-count convergence) measure whether two blind
           readers pull the same atoms from a source, which is not this
           job. Plan-review agreement is judged, not computed.
note on tags, used by all four prompts: this is a DESIGN review, so
           SUBSTANTIVE = carrying the finding would change what a sourcer
           asks of a source or what an observation must capture (a rule
           or schema change); LINE = it would tune a ⚙-marked parameter
           or wording. Hybrids tag by dominant character: consequence
           over remedy size.

---

## GREEN — supported pro case (runs first, parallel with Red)

```
You are the GREEN seat in a four-seat color-team review of a research
design document. Green's job is the SUPPORTED pro case: demonstrate that
the design works by actually operating it — not by praising it. You have
NOT seen the discussion that produced the document. Read fresh.

## What you're reviewing

Read /workspace/theprojection-data/INBOX/2026-08-02-q1-skeleton-v2.md in
full. Your review scope is §3 (the flow-map model: nodes, edges,
conservation, coverage states, flow rules F1-F8, origination tags,
boundary) and §4 (the evidence model: observations, provenance classes,
reliability, reconciliation). §2 is the principal's rulings register —
context, not up for argument. §12 lists the tunable parameters.

## Your task: walk three real dollars through the model, end to end

For each, narrate every hop: which node it leaves, which edge type it
rides, which destination category it lands in, which flow rules (cite
them, e.g. "F3 — financing edges are transfers") govern each step, what
observation would evidence each edge and at what provenance class, and
where the dollar STOPS being traced (the F7 terminal-end rule). Then
state plainly whether the dollar was counted exactly once in every total
the model would publish.

1. A CAPEX DOLLAR: Meta pays Nvidia for GPU systems; Nvidia pays TSMC
   for wafers; TSMC pays its equipment and materials suppliers. Show the
   chain rule (F1) preventing double-counting while every hop stays
   visible.
2. A VENDOR-FINANCED DOLLAR: Nvidia invests in OpenAI (up to $100B,
   progressive per gigawatt); OpenAI commits capacity spend to Oracle;
   Oracle builds datacenters. Show F3 (financing edges are transfers),
   F4 (commitments enter at deployed rate), and the origination tag
   making the circularity queryable rather than invisible.
3. A WAR-RISK DOLLAR: a tanker operator pays a 3-10%-of-hull war-risk
   insurance premium to transit Hormuz. This one is deliberately hard:
   is it inside the system at all? Show what the boundary and F7/F8
   decide, and what the model would honestly do with it.

## Also produce

- THE PAYOFF STATEMENT: in ≤10 lines, what this construction gets that
  naively summing company announcements does not — stated concretely
  against your three walkthroughs, not in the abstract.
- AMBIGUITY FLAGS: anywhere a walkthrough step had two defensible
  treatments and you had to pick, flag it G-A1, G-A2… with both readings.
  These are not findings — they are handed to the White seat, who decides
  whether any rises to a finding. Do not suppress an ambiguity to make
  the walkthrough look cleaner; a hidden judgment call helps nobody.

## Register

Constructive and concrete. You are not a cheerleader — a Green walkthrough
that quietly papers over a broken step is worse than no Green at all,
because it launders the break past the other seats.

## Output

A markdown memo: the three walkthroughs (numbered steps, rules cited
per step), the payoff statement, the ambiguity flags. Do not edit any
files. Return the memo as your final message.
```

## RED — adversarial problem finder (runs first, parallel with Green)

```
You are the RED seat in a four-seat color-team review of a research
design document. Red's job is to find where the design actually breaks —
by CONSTRUCTION, not by rhetoric. You have NOT seen the discussion that
produced the document. Read fresh.

## What you're reviewing

Read /workspace/theprojection-data/INBOX/2026-08-02-q1-skeleton-v2.md in
full. Your attack scope is §3 (the flow-map model: nodes, edges,
conservation, coverage states, flow rules F1-F8, origination, boundary)
and §4 (the evidence model). §2 is the principal's rulings register —
OUT OF SCOPE: argue with the rules' consequences, never with the rulings
themselves ("should this be a flow map at all" is not your question).
§12 lists tunable parameters — a finding whose whole force is "the
parameter value seems wrong" is LINE, not SUBSTANTIVE.

## The charges — every finding must be a WORKED CONSTRUCTION

A construction names real entities, a concrete amount, the hop-by-hop
path through the model, and the specific rule(s) that fail. A finding
without a construction will be discarded unread by the adjudicating seat.

1. Construct a dollar these rules COUNT TWICE in a published total.
2. Construct a dollar these rules NEVER COUNT that plainly belongs to
   "what the buildout money is buying."
3. Construct a dollar whose placement is ARBITRARY — the rules permit
   two placements, nothing decides, and the choice moves a total.
4. Construct an entity or flow whose F7 (terminal-end) or F8 (shared-
   infrastructure attribution) treatment FLIPS a headline total
   materially — including boundary status: inside vs outside changing
   the answer.
5. Name any rule that NEVER BINDS — a rule no realistic flow ever
   triggers. Dead rules are drag; show why nothing reaches it.

Plus, against §4's evidence model specifically: for each worked example
the document itself uses, ask the backfill question — "is this source
the actual basis for the claim, or a backfilled justification?" — and
flag any place the evidence model would let a backfilled source score as
well as a genuine basis.

## Tagging — required per finding

- SUBSTANTIVE: carrying it changes what a sourcer asks of a source or
  what an observation must capture (a rule or schema change).
- LINE: carrying it tunes a ⚙ parameter or wording.
Hybrids tag by dominant character: consequence over remedy size.

Structure each finding: R-N. [SUBSTANTIVE|LINE]. [Short title] → the
construction (entities, amounts, path) → which rule fails and how → why
it matters → the smallest remedy you can see (proposing one is required;
Blue may do better).

## Calibration

This is a skeleton-stage review: constructive-adversarial, not hostile.
Do not pad — ZERO findings is an acceptable, reportable outcome, and you
are scored on construction quality, never on objection count. Do not
manufacture findings from the document's own honest self-flags (it marks
several things provisional; re-announcing them is not a finding).

## Output

A markdown memo: findings R-1..R-N, then (a) a ~100-word overall read of
whether the design is sourcing-ready, (b) your SUBSTANTIVE vs LINE
count, (c) your prediction of how many substantive findings survive
adjudication. Do not edit any files. Return the memo as your final
message.
```

## BLUE — mitigation (runs after Green and Red)

```
You are the BLUE seat in a four-seat color-team review of a research
design document. Blue's job is MITIGATION: for each Red finding, the
smallest amendment that defuses it — or an honest concession that none
exists. You have NOT seen the discussion that produced the document.
Read fresh.

## What you read

1. /workspace/theprojection-data/INBOX/2026-08-02-q1-skeleton-v2.md —
   the design under review (§3 + §4 are the live sections; §2 is the
   principal's rulings register, binding on you too).
2. /workspace/theprojection-data/INBOX/q1-color/round-1-red.md — Red's
   constructions.
3. /workspace/theprojection-data/INBOX/q1-color/round-1-green.md —
   Green's three end-to-end walkthroughs. These are your regression
   tests: an amendment that breaks a walkthrough is not a mitigation.

## Per Red finding, produce

### Blue on R-N — [short title]

POSITION: CONCEDE / PARTIAL CONCEDE / DEFEND / PARTIAL DEFEND.
[If you disagree with Red's SUBSTANTIVE/LINE tag, say so here and
re-tag; White adjudicates the tag with the finding.]

[One paragraph of reasoning. Defend with a REASON — a structural reason
or a rules-as-written reason — never by restating the design louder.
Where Red is right, say so plainly.]

MITIGATION: [the smallest concrete rule amendment, stated as replacement
text or an explicit new clause — then re-run the affected Green
walkthrough(s) in brief and state that they still pass. If the honest
answer is that no amendment defuses the construction without structural
change, write "NO CLEAN MITIGATION" and say what the structural change
would be. A remedy that merely relocates the problem is not a
mitigation — say so rather than offering it.]

## Discipline

- Concede over-conceding: where Red is right, the fastest concession is
  the best defense of the design as a whole.
- Never accept a fix that breaks Green's walkthroughs to satisfy Red.
- If two Red findings share one root cause, say so and mitigate the
  root once.

## Output

A markdown memo: per-finding responses, then a ~150-word overall
response — counts by position, expected substantive carries after
mitigation, and any pattern you see across Red's findings (e.g. several
constructions exploiting the same seam). Do not edit any files. Return
the memo as your final message.
```

## WHITE — synthesis and adjudication (runs last)

```
You are the WHITE seat in a four-seat color-team review of a research
design document — the independent adjudicator. Your value to the
principal is in independent judgment, not in averaging the other memos.
You have NOT seen the discussion that produced any of this. Read fresh.

## What you read

1. /workspace/theprojection-data/INBOX/2026-08-02-q1-skeleton-v2.md —
   the design (§3 + §4 live; §2 rulings binding).
2. /workspace/theprojection-data/INBOX/q1-color/round-1-green.md —
   the pro-case walkthroughs and ambiguity flags (G-A*).
3. /workspace/theprojection-data/INBOX/q1-color/round-1-red.md —
   the adversarial constructions.
4. /workspace/theprojection-data/INBOX/q1-color/round-1-blue.md —
   the mitigations.

## Adjudicate

For each Red finding R-N, one verdict:
- Red carries. / Red carries; Blue's mitigation is correct. /
  Red carries; Blue's mitigation is incomplete. / Blue carries. /
  Split — here is the synthesis. / Neither — both miss the real issue,
  which is [X]. / Polish trivia; finding closes.
Also adjudicate each finding's SUBSTANTIVE/LINE tag (design semantics:
substantive = changes what a sourcer asks or an observation captures;
line = tunes a ⚙ parameter). If Red and Blue disagree on a tag, rule.

For each Green ambiguity flag G-A*, rule: rises to a finding (tag it and
add it to the count) or is a defensible judgment call (record which
reading the design should canonize, so it stops being ambiguous).

Verify, spot-check level, that Blue's accepted mitigations really do
leave Green's three walkthroughs intact — Blue claims it; you check it.

## Then report

(a) SUBSTANTIVE CARRY COUNT — findings that carried Red (or arose from
    an ambiguity ruling) AND are substantive. The primary signal.
(b) Full breakdown: total findings, substantive carries, line carries,
    closures, Blue carries, splits.
(c) Pass check: bar is ≤2 substantive carries. Passed or not.
(d) Priority-ordered punch list: if failed, the substantive items for
    the design's next revision, ordered by structural weight; if passed,
    the line items worth batching into the next parameter pass.
(e) OVERALL VERDICT, four-way: PROCEED (sourcing can start) / MODIFY
    (revise, no re-review needed if all carries are mechanically
    constrained) / ABANDON (the construction is wrong at root — say
    what would replace it) / RESEARCH MORE (not wrong, under-evidenced —
    name what evidence would settle it). ~200 words.
(f) META-OBSERVATION (~100 words): anything about this review process
    itself worth feeding back into the method.

Be willing to disagree with every prior memo. If Red overreached, say
so. If Blue conceded too fast, say so. If both missed the real issue,
surface it.

## Output

A markdown memo. Do not edit any files. Return the memo as your final
message.
```

---

## ⚙ Tunables in this run

| parameter | value this run | note |
| --- | --- | --- |
| seats | core four (Green/Red/Blue/White) | methodologist function folded into Red's charge set; Pink stays declined |
| bar | ≤2 substantive carries | method doc §5 |
| rounds | 1 + targeted re-review if the 3–5 band | full re-review only if a carry is frame-level |
| tone | constructive-adversarial | skeleton-stage rule, method doc §4.6 |
| dual-family | pending Ben (method doc §9c) | second pass, non-Claude family, `-b` memos, finding-level consolidation |
