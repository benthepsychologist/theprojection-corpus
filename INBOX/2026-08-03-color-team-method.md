# Color-team review — the cohesive method

status:     DRAFT for Ben's ruling — this document is also the material
            for the q1 red-team edit he owes: once ruled, it SUPERSEDES
            §10 of INBOX/2026-08-02-q1-skeleton-v2.md (the single-seat
            red-team brief becomes the Red seat of a full color run).
assembled:  2026-08-03, from every color-team trace in the workspace —
            provenance table in §2. Nothing here is invented; where the
            found material disagrees with itself, the disagreement is
            shown, not smoothed.
convention: ⚙ marks a tunable starting value (the q1 register's R-14
            rule — starting points are never hardcoded); the operative
            bar, seat set, and round count are all ⚙.

---

## 1. One method, three tellings

Three versions of "color team" exist in the record, and they are the same
method at different maturities:

- **Ben's operative minimum** (stated 2026-08-03, commissioning this doc):
  **green** = supported pro case · **red** = adversarial problem finder ·
  **blue** = mitigation of red where possible · **white** = synthesis.
  Fancy mode: run the whole thing twice with different model families and
  compare agreement.
- **The manuscript protocol** (`the-evidence-gap-src/color-team-protocol.md`,
  522 lines, versions 1→9): the most battle-tested instance — every
  chapter of the book went through it ("draft → multi-round adversarial
  color-team review until almost nothing's left to argue about," per the
  pm hub). v1.0 ran three seats (Red/Blue/White); v2.0 runs five
  (Red/Blue/Green/Pink/White) with author response moved into a
  consolidation phase.
- **The research architecture** (`kestrel/ROADMAP/RESEARCH.md`, PROPOSED):
  adopts the protocol as **stage 7 of a ten-stage investigation process**
  and proposes a parameterized `/color-team` library skill
  (lenses · rounds · bar). Its stage 1 — adversarially reviewing the
  skeleton *before sourcing* — is exactly what q1 is waiting on.

Ben's own testimony adds a fourth, earlier life the sweep could not reach
by file: *"color team showed up more in the claim extraction work i was
doing to model scientific and philosophic articles. We would color team a
inference on top of a body of evidence and let the models do a back and
forth… running it until agents converged on number of claims as a
completeness and accuracy check."* The book's protocol reviews **prose**;
the article work reviewed **inferences over evidence** — which is the
shape q1 needs.

## 2. Where the pieces came from

| source | contributed |
| --- | --- |
| `the-evidence-gap-src/color-team-protocol.md` (v1→v9) | seats, workflow, substantive/line tagging, ≤2-carry pass bar, decision bands, targeted re-review, verbatim seat prompts, nine versions of mechanization discipline |
| ~100 run memos under `the-evidence-gap-src/chapter-*/` | the run artifacts behind every empirical claim here |
| fleet-ontology register (cloud-governor INBOX, kestrel entry, `done/`) | convergence trajectories (22→15→13→0 · 15→8→11→2→0 · 14→0) · three-bars-for-three-jobs · the same-model ceiling · "cross-model agreement: never run" · fresh-context failure data pointer |
| `kestrel/ROADMAP/RESEARCH.md` §§7.7–8, 11–12 | granularity ruling (the unit is a layer/section, never a claim) · the separation rule · Red's backfill test · four-way verdict · drop-Pink-for-v1 · the `/color-team` skill proposal |
| `kestrel/INBOX/2026-07-31-…three-instances-one-species.md` | "verification is a dial" — color team as a parameterized engine skill; Ben: "color teaming a summary or write up of a thread in either of our news and info feeds is on the way" |
| `kestrel/INBOX/2026-08-02-…buildout-research-open-questions.md` | Ben's article-work testimony · layer-granularity options · the checking-the-checker gap · cross-model dual-pass recommendation |
| `research-template/METHODOLOGY.md` §13 (verified directly) | the sustained-context failure record: 279 raw findings → 169 substantive → 105 unique → **zero of six acts converged**, plus fabrication failure modes |
| pm hub, the manuscript OVERVIEW | the one-line frame: "the gauntlet… until almost nothing's left to argue about" |

## 3. The seats — a function registry, because the colors collide

⚠️ **The color names have been overloaded across versions**, and this doc
refuses to smooth that silently. The stable thing is the FUNCTION; a
color is a label pinned to a function per loadout:

| function | Ben's minimum (operative) | manuscript v1.0 | manuscript v2.0 |
| --- | --- | --- | --- |
| adversarial problem finder | **Red** | Red | Red (adversarial reader) |
| supported pro case / steelman | **Green** | — | — (v2.0's Green is a *methodologist*: evidence-claim fit, description-vs-artifact) |
| mitigation / defense of the artifact | **Blue** | Blue — but as the *author's* response (CONCEDE / PARTIAL CONCEDE / DEFEND / PARTIAL DEFEND) | — (v2.0's Blue is a *friendly reader*: comprehension, flow) |
| synthesis / independent adjudication | **White** | White | White (plus structural architecture) |
| editorial / prose quality | — | — | Pink — **already declined for research v1**: "No prose to edit until Stage 9" |

**The collisions, named:** Ben's Blue (mitigation) is v1.0's Blue minus
authorship, and is NOT v2.0's Blue (friendly reader). Ben's Green
(steelman) is NOT v2.0's Green (methodologist). White is compatible
across all three — with the manuscript's sharpest line carried forward
verbatim: *"your value to the author is in independent judgment, not in
averaging the two prior memos."*

**Operative ruling proposed:** Ben's four functions ARE the core loadout,
under his color assignments. The manuscript's methodologist and
friendly-reader functions become optional extension seats (new labels
when used, to avoid the collision); Pink stays declined until there is
prose. ⚙ Seat sets are per-loadout choices, not schema.

**Information flow between seats (Ben, 2026-08-03):** Green and Red run
blind to each other. **Blue reads the artifact and Red's memo only** —
it answers Red's concerns, that is all; it is not a dispute-settler and
never sees Green. **White is the only seat that reads everything**, and
aggregation is its exclusive job.

**One genuine gap the sweep proved:** nothing anywhere tests the
*reviewer*. A dedicated grep of the manuscript repo for any
checking-the-checker mechanism (`double agent`, `mole`, `collusion`,
`meta-review`, `test reliability`) returned **zero hits** — every
adversarial mechanism targets the prose, the claim, or a remedy, never
the reviewer. Ben's article work reportedly had convergence-on-claim-count
as a completeness check; that mechanism is not recoverable from any repo
in this sweep. Logged as an open seat concept, not invented into canon.

## 4. The non-negotiables — each with its receipts

1. **Fresh context per seat, per unit. Not a preference.** The recorded
   violation: drafting/reviewing across units in one sustained context
   produced **279 raw findings → 169 substantive → 105 unique after
   dedup → zero of six acts converged** — with fabrication appearing in
   later units (invented institutional reviews, a fabricated enforcement
   action). Healthy fresh-context trajectories for comparison:
   **22→15→13→0 · 15→8→11→2→0 · 14→0.** Never carry a reviewer across
   two units "to save setup."
2. **Separate the attacks from the decision.** Verbatim, from
   `agentic-research-patterns` via the research architecture: *"The red
   team pass produces attacks. The synthesis pass produces the verdict.
   Don't let the attacks and the decision happen in the same breath."*
   This is why White exists as a seat and not a paragraph.
3. **Every finding is tagged SUBSTANTIVE or LINE, by dominant
   character.** Substantive = carrying it changes what the artifact
   argues, includes, connects, or frames; line = wording/polish. Hybrids
   tag by consequence, not remedy size — the protocol's worked example
   is a two-number calendar fix tagged SUBSTANTIVE because the numbers
   anchored the thesis snapshot's credibility. In the q1 design context:
   substantive = changes what the sourcer asks or captures; line =
   parameter tuning.
4. **The diagnostic is the substantive carry count, never a win rate.**
   The recorded trap: a round carried red on 12 of 15 findings — 80%
   count-based — but only 3 were substantive. Win percentages conflate
   classes; the substantive-only count is the clean signal.
5. **Worked examples or the finding is discarded.** (q1's addition,
   answering Ben's "red teams are often set up to produce arbitrary
   opposition.") Every finding names entities, an amount, and the rule
   that fails; **zero findings is an acceptable, stated outcome**; the
   reviewer is scored on construction quality, not objection count. The
   manuscript's Red rubric already leans this way ("sharply but
   CONSTRUCTIVELY… every finding includes a suggested remedy").
6. **Tone matches the stage.** Empirical, from the protocol's pre-prose
   reviews: *"adversarial framing produces shallower findings;
   soft-collaborative framing elicits constructive additions"* — on a
   SKELETON. Full-adversarial tone is for finished artifacts; spec-stage
   reviews run soft-collaborative. q1's Stage-1 review is a skeleton
   review: constructive-adversarial, not hostile.
7. **Red's single most transferable question**, verbatim: *"Is this
   source the actual basis for the claim, or a backfilled
   justification?"* Aimed at every citation and every hypothesis.
8. **The plan's authors never write the test points** (Ben, 2026-08-03:
   *"by writing in specific concerns for red to go after you're usurping
   part of its role without the independence"*). A seat receives the
   plan, its justification, its aims, and a description of what an agent
   of its color tries to do — never a charge sheet, marker list, or
   author-chosen scenario. An author-written charge sheet performs Red's
   role with the least independent judgment available: the plan's own
   authors. Where a reviewer chooses to probe is itself part of the
   signal. Quality-bar constraints (findings must be demonstrated; zero
   findings acceptable) are conduct rules, not direction, and survive.
9. **The artifact must carry its own justification.** Reviewers are
   fresh-context by rule 1; if the plan's philosophy, reasoning, and
   aims live in a conversation the reviewers never see, they review a
   skeleton without its why and White concludes from ignorance. Before a
   color run, lay the justification into the document itself (q1's
   §1.5 is the instance) — it is part of the plan, not commentary, and
   it is the pro-case's raw material without being the pro-case.

## 5. The loop

```
seats run in parallel (fresh context each) → per-seat memos
  → CONSOLIDATION: cross-seat-confirmed items ranked above single-seat;
    substantive vs line split; author/principal position per item —
    CONCEDE / PARTIAL CONCEDE / DEFEND / PARTIAL DEFEND
  → PRINCIPAL DIRECTION: Ben rules where judgment is required
  → revision applies the punch list
  → next round, all seats fresh → convergence check
```

- **Pass bar ⚙: ≤2 substantive carries in a round.** Rationale kept
  verbatim: *"the signal we want is structural-problem rarity, not
  zero-finding perfection."*
- **Decision bands ⚙:** ≤2 → **pass** (line findings batch to polish) ·
  3–5 → **revise**, then *full* re-review if any carry is frame-level,
  or *targeted* re-review if all carries are mechanically constrained ·
  6+ → **step back** — the artifact may need an outline-level rethink,
  not a revision.
- **Targeted re-review** checks exactly one prior finding against four
  statuses: RESOLVED · PARTIALLY RESOLVED · NOT RESOLVED (recursive —
  the same failure mode re-introduced in a new form) · NEW PROBLEM IN
  THE REMEDY. Targeted pass bar: zero new substantive carries.
- **Verdicts are four-way**, not three: **proceed / modify / abandon /
  research more.** "Research more" is a real state — the artifact isn't
  wrong, it's under-evidenced.
- **Granularity: the unit is a section or a layer, never a claim.** Five
  reviewers per section is affordable; per-claim over hundreds is not.
  (Per-hypothesis stays available as an escalation for a hypothesis that
  matters enough.)
- **Bars are per-job, never universal:** color-team ≤2 carries ·
  source-verification **ZERO** (*"a cited claim that doesn't match its
  source is a publication-grade error, not a style point"*) · chronology
  sweeps <15% new entries. Convergence to iteration, not a fixed round
  count — most units converge in 2–3 rounds.

## 6. The dual-family mode — Ben's "fancy," specified against what's actually known

**The spec:** run the full color cycle twice, with the seat agents drawn
from **disjoint model families**, then compare at the finding level.

**What the record actually says, and it says it hard:**

- *"Same-model dual-pass measures session variance, not true methodology
  variance."* Every recorded agreement number in the fleet came from
  same-model runs and is therefore **a floor**.
- **Raw agreement understates true agreement ~3×** unless disagreements
  are triaged mechanical-vs-substantive first — the recorded run: raw
  Jaccard 0.57 → 0.713 slug-normalized; 130 mechanical vs 18 substantive
  disagreements. The triage is mandatory or the metric is worthless.
- ⚠️ **Cross-model agreement has NEVER been run.** The fleet register
  lists it under "what genuinely does not exist anywhere." Running q1
  dual-family would be the fleet's first actual execution of the thing
  Ben remembers as the fancy mode.
- ⚠️ **Environment reality (2026-08-03):** this workstation has Claude
  models only — no other provider's credentials exist anywhere on it
  (checked). So dual-family is not runnable as automation here. It
  remains reachable **manually**: the seat prompts are self-contained by
  design, so pasting them into another vendor's own interface and
  returning the memos is a legitimate second-family pass. Mixing Claude
  *tiers* across passes is tier-variance, not family-variance, and is
  never to be recorded as dual-family.

**Agreement semantics ⚙:** a finding surfaced by both families =
highest-confidence, goes to the top of consolidation. A single-family
finding is *triaged, not dismissed* — it is either family-specific noise
or a real catch the other family's priors missed, and the consolidation
decides which, explicitly, per finding.

⚠️ **Scope caution (Ben, 2026-08-03): most of the recorded
convergence/reliability instrumentation is EXTRACTION machinery, not
review machinery.** Jaccard agreement, claim-count convergence as a
completeness check, dual-pass blind extraction — those measure whether
two blind readers pull the same atoms out of a source, and none of it
applies to evaluating a plan. What transfers to a plan review is exactly
two things: the same-model-variance warning above, and the *habit* of
splitting disagreements into mechanical-vs-substantive before reading
the agreement level — applied qualitatively at consolidation, never
computed as a statistic. The review-side machinery (substantive/line
tags, carry counts, the ≤2 bar) is what governs a plan review; the
extraction instruments stay with extraction.

## 7. Rigor is a dial

From the three-instances brief, adopted as frame: adversarial
verification *"is not [the manuscript]'s identity, it's the max setting
of a dial every instance turns."*

| setting ⚙ | what runs | when |
| --- | --- | --- |
| **low** | one Red pass, worked-example discipline, no consolidation | a thread writeup before publish ("on the way," per Ben) |
| **standard** | the core four seats, one round + targeted re-review as needed | a design doc, a layer's hypothesis set |
| **max** | five+ seats · multi-round to convergence · dual-family | a chapter; a load-bearing model the public will see |

The future `/color-team` engine skill (proposed in the research
architecture: parameterized by lenses · rounds · bar) wraps exactly this
dial; this document is the content that skill would encode.

## 8. First run — q1 Stage 1, instantiated

⚠️ **Corrected 2026-08-03 after Ben's second ruling on seat conduct.**
The first draft of this section gave Green three author-chosen
walkthrough dollars and Red a five-charge sheet. That violated the
method's own independence principle (now §4.8): *"by writing in specific
concerns for red to go after you're usurping part of its role without
the independence."* The superseded charge-sheet survives only as
historical record at q1-skeleton-v2 §10.

- **Artifact under review:** q1-skeleton-v2 in full — a plan, its
  justification (§1.5, laid in for this purpose), and its aims. The
  rulings register (§2) is decisions, not open questions: consequences
  are reviewable, rulings are not re-litigated.
- **Seats (core four ⚙), fresh context each, none sees this
  discussion — and no seat receives author-chosen probe targets:**
  - **Green** — *green-team it*: the strongest supported case that the
    plan accomplishes its stated aims. What to demonstrate or argue is
    Green's choice.
  - **Red** — *red-team it*: find where the plan actually fails. Where
    to attack is Red's choice; the only constraints are quality-bar
    (findings concrete and demonstrated, remedy suggested, tagged
    substantive/line, zero findings acceptable), never direction.
  - **Blue** — answers Red. Reads the artifact and Red's memo ONLY —
    not Green's. Per finding: position (CONCEDE / PARTIAL CONCEDE /
    DEFEND / PARTIAL DEFEND) and the smallest honest answer, with NO
    CLEAN ANSWER as an allowed state. Blue is not a dispute-settler.
  - **White** — the only seat that reads everything. Aggregates,
    adjudicates each Red/Blue exchange, weighs Green's case as evidence,
    reports the substantive carry count against the ≤2 bar, and returns
    the four-way verdict (proceed / modify / abandon / research more).
    Independent judgment, not averaging.
- **Tone:** constructive-adversarial (it is a design-stage review — §4.6).
- **Memos ⚙:** `INBOX/q1-color/round-1-{green,red,blue,white}.md`, with
  `-b` suffixed copies if the dual-family mode runs.
- **The dispatch-ready seat prompts are written:**
  `INBOX/q1-color/PROMPTS.md` — verbatim instructions for all four
  seats in the manuscript protocol's PROMPT tradition, sequenced
  Green ∥ Red → Blue → White, with the design-context tag semantics and
  the anti-theater clauses embedded. Nothing runs until Ben approves
  them.
- **Dual-family:** recommended — one full pass with Claude-family seats,
  one with a non-Claude family, consolidation compares. It would be the
  fleet's first real cross-model run.

## 9. Decision points for Ben

| # | decision | proposed ⚙ |
| --- | --- | --- |
| a | **seat semantics** — adopt your four-function minimum as canon, with the v2.0 collisions (Blue, Green) resolved by relabeling extension seats | yes as written in §3 |
| b | **q1 loadout** | core four; no charge sheets — seats choose their own probe points (§4.8); Pink stays declined |
| c | **dual-family on q1** | not automatable here (Claude-only environment); optional manual second pass via another vendor's UI, memos filed as `-b` — the Claude run proceeds either way |
| d | **pass bar for q1** | ≤2 substantive carries, one round expected, targeted re-review if 3–5 band |
| e | **memo location** | `INBOX/q1-color/` as in §8 |
| f | **this doc's routing** | routes to kestrel with the q1/q2 bundle; it is also the seed of the proposed `/color-team` library skill |
