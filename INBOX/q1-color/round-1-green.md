<!-- q1 color-team · round 1 · GREEN seat · 2026-08-03
     model: Claude (Fable-tier subagent, fresh context, single-family run)
     artifact: INBOX/2026-08-02-q1-skeleton-v2.md
     prompt: INBOX/q1-color/PROMPTS.md §GREEN, dispatched verbatim
     memo below is the seat's return, verbatim and unedited. -->

# GREEN memo — the supported case for q1 skeleton v2

> 🎯 **Verdict: the design accomplishes its stated aims, and the support is unusually concrete** — its rules survive worked operation against the real 2025–26 events it must model, its central bets are vindicated by documented real-world precedent, and two of its riskiest claims (schema extensibility, on-demand pass semantics) have already been tested outside this document and passed.

**Method note.** I did not take the plan's claims on faith. I operated the flow rules against real events (§A), checked the plan's external premises against the world (§B), and verified its internal cross-references against the repo (§C). Where the case rests on a hope rather than a demonstration, §E says so.

---

## A. Operating the design — five real dollars through the rules

The strongest support for a set of rules is running them. Each example below is a real event from the period the model must cover, processed by the rules as written. In every case the rules produce a determinate, defensible answer where the naive alternative (sum the headlines) demonstrably fails.

**A1 — The circular dollar: Nvidia → OpenAI → Oracle → Nvidia.**
The defining contested question of the entire buildout discourse. Nvidia commits up to $100B into OpenAI progressive per gigawatt; OpenAI commits >$300B to Oracle; Oracle buys Nvidia GPUs to serve it. Press treatment produces three headline numbers that sum the same underlying dollars two or three times, with the circularity invisible.

- **F3** classifies Nvidia→OpenAI as a financing edge (type: equity, origination: *vendor*) — a transfer, not build.
- **F4** amortizes the Oracle commitment at the deployed rate per quarter.
- The dollar enters **build exactly once** — at the purchase edge where Oracle acquires real silicon (destination category: compute silicon & systems).
- The **origination tag** makes "how much of OpenAI's compute is funded by its own suppliers" a *query*, not an investigation. This is §1.5's promise ("queryable view instead of a vibe") cashed on the single most argued-about structure in the market.
- **Conservation** at the OpenAI node localizes any imbalance to OpenAI — precisely the actor whose in/out/retained picture the public record garbles most.

No rule needed interpretation; no two rules collided. That is what "the design works" looks like at the object level.

**A2 — The four-stage ambiguity, quantified on Stargate.**
One project produces four different public numbers: "up to $500B over four years" (frame), ">$300B over five" (commitment), quarterly RPO additions (contract), datacenters actually energized (delivered asset). The plan's diagnosis — press collapses these for a ~3× ambiguity — is if anything **conservative**: by late 2025 the sum of OpenAI-attributed announcements ran on the order of $1.4T against in-period deployment plausibly in the low tens of billions. Treating commitments as spend is an order-of-magnitude error, not a 3× one. F4 plus the observation model (face value recorded as a company-statement observation; edge magnitude from reconciling filings, delivered-capacity math, and credible press) is the *minimum* machinery that can hold these four numbers apart. Anything simpler re-collapses them.

**A3 — F5 sorts look-alike headlines mechanically.**
Same news cycle, two multibillion "AI deal" stories: AMD's 160M-share warrants against 6GW of purchases, and Amazon's $53.4B Anthropic revaluation. F5's substance test — do real resources or claims on capacity change hands? — puts the first on the map as a real edge at disclosed issue value (payment form sets *type*, never existence) and keeps the second off it entirely (a mark moves nothing; at most it annotates ownership). A scoreboard design would either count both or adjudicate each case ad hoc. The rule decides both correctly with zero judgment spent.

**A4 — F1/F2 against the nesting chain, and why the strawman's alternative was impossible.**
Big-four calendar-2025 capex (~$380–400B) contains most of Nvidia's data-center revenue (~$115B+), which contains a large slice of TSMC's revenue (~$90B, majority HPC), which contains ASML's. One dollar, visible at three or four hops; summing announcements counts it at every hop. F1 (totals only from boundary crossings and category rollups) kills the error by construction. And F2's dissolution of the strawman's margin-assignment rule is not a stylistic preference — it is forced by the world: per-hop margin by customer and node is **not disclosed** (Nvidia does not break out margin by customer; TSMC does not by customer-node). The value-added method requires data that does not exist; the flow map requires only the hops, which *are* disclosed (revenue lines, COGS, capex). The design chose the construction the actual disclosure regime can feed.

**A5 — The aggregated state matches how disclosure actually looks.**
Samsung reports one capex total spanning memory, foundry, display, and appliances; OpenAI discloses almost no internal split at all. R-02/F6's answer — edge terminates at the entity, node carries `aggregated` honestly, allocation claims split it later with their own observations and reliability — is the only one of the three possible designs that neither fakes precision nor drops the node. The three-state coverage model (`measured / aggregated / unmeasured`) is the disclosure world's real texture, encoded.

**A6 — F8 matches how grid analysts already work.**
Attributing shared grid buildout by interconnection-queue share, flagged as an estimate with its method, is the standard practice of the analysts who actually forecast datacenter power (queue filings at ERCOT/PJM are the working instrument of that field). F8 is not an invention; it is an adoption of the proven method, with the honesty flag added.

---

## B. External grounding — the plan's bets are already vindicated in the world

**R-05 (independent measurement can outweigh company statements) has a named proof.** In February 2025, channel-check work (TD Cowen) surfaced Microsoft datacenter lease cancellations before and against the company's public posture — and was vindicated. SemiAnalysis's satellite-plus-permits-plus-queues datacenter model is a running demonstration that the independent-measurement class is cultivatable and frequently *ahead* of disclosure. The strawman's rank-by-source-type ladder would have permanently subordinated both to company guidance. R-05 is the ruling the recent history of this exact field demands.

**R-03 (consolidation, not suspicion) encodes the telecom lesson.** In 1999–2001, vendor financing (Lucent, Nortel) and capacity swaps (Global Crossing, WorldCom) generated "revenue" that was intra-system transfer; no consolidation-style discipline existed, headline demand was overstated, and the discovery arrived as a collapse. The plan applies a proven accounting mechanic — intra-group elimination — to a system that is not legally one firm but economically behaves like one for this question. It also converts the loudest current controversy (the fall-2025 circular-financing debate) from a moral argument into a mechanical adjustment, which is exactly what a *model* should do with a controversy.

**The burn metric formalizes the field's best prior analysis.** The most influential public treatment of "is any of this real" (Sequoia's "$600B question," 2024) was a one-off, hand-built external-revenue-versus-build-cost gap analysis. The burn metric is that analysis as a continuously computed instrument with receipts — same logic, upgraded from essay to system.

**The question's scale premise is real.** Hyperscaler capex alone ran ~$380–400B in calendar 2025 with 2026 guidance stepping well beyond it; "largest mobilization of resources, raw," is not rhetoric, and a flows model with conservation is the standard instrument (national accounts, input-output tables) that economics reaches for at exactly this scale of question. R-01's choice has a century of methodological precedent behind it that the document doesn't even bother to claim.

---

## C. Verified internal evidence — claims I checked against the repo, not took on faith

- ✅ **The extensibility claim has already been tested — and passed.**
  R-13 claims bringing q2 online "requires no redesign." The sibling file
  (`/workspace/theprojection-data/INBOX/2026-08-03-q2-inference-demand-skeleton.md`)
  exists and confirms it operationally: "no new schema, one object promoted" —
  the commitment object, whose `amortized_to_date` field is exactly the seam
  F4 already consumes. Better: q2's §6 extends F1's chain rule to *backlogs*
  unchanged, banning "industry backlog" headline sums by construction. The
  schema survived its first real extension before this review even convened.
  That is the rework-economics argument (§1.5) cashed once, in public.
- ✅ **R-15's precedent is real and includes the failure-recovery case.**
  Git history in this repo: `/daily 08-01` recovered a missing 20-hour window
  two days late; `/daily 08-02` recovered a missing 22-hour window. The
  "pass brings the model up to now, whenever invoked" semantics the delta
  pass imports is not an analogy to something hoped-for — it is the observed
  behavior of the pipeline it will ride, demonstrated twice in the three days
  before this review, *including* the late-invocation catch-up case that a
  heartbeat-floor design most needs to work.
- ✅ **The pipeline the delta pass rides exists** — `sources/feeds.yaml`,
  `artifacts/digests/`, the operating `/daily` skill, and a live commit
  stream. §6's "rides the collection pipeline that already runs daily" is a
  statement of fact, not intent.
- ✅ **The document practices its own discipline.** Every ⚙ in the body
  (F7 floor, §4 band cuts, §3 categories, §5 tier cut, §6 heartbeat) resolves
  to a row in §12, exactly as R-14 requires. A plan that already obeys its
  own conventions before implementation is weak evidence, but it is evidence
  — the convention costs something, and it was paid.

---

## D. Arguments the plan undersells

- **The rework asymmetry is a coherent decision principle, not a slogan.**
  The design front-loads *only* the irreversible (source capture with dates,
  excerpts, hashes; coverage predictions written before sourcing) and defers
  *everything* reversible (every parameter is ⚙-data). Operate it: move the
  materiality floor from $1B to $500M — no observation is invalidated, only
  which edges collapse into "other inputs" changes. Re-cut the destination
  categories — observations carry source language and re-tag. Re-band
  reliability — the 0–1 numbers stand, rendering re-cuts. The one
  non-recoverable act, capturing a source before it rots, is the one act the
  design refuses to defer. This is textbook irreversibility-weighted
  sequencing, applied consistently across the whole plan.
- **Flags are the product, and the design is the only shape that produces
  them.** §4's line — flags "mark where the system is lying to itself or to
  us" — deserves more weight than it gets. For Ben's actual question, the
  *disagreements* between a company's guidance and independent measurement
  may be the highest-value output the model emits. Any single-authority
  design (R-04's rejected alternative) resolves that signal away at ingest;
  this one preserves it as a first-class surface.
- **§7 is a calibration loop, not bookkeeping.** Writing sourceability
  predictions before sourcing and grading them after is forecasting
  discipline applied to the sourcing operation itself: misses generalize
  into method ("predicted-dark but found — record how"), and the strawman's
  half-sourceable hypothesis becomes a scoreable claim instead of a vibe.
  The sourcing operation improves itself as a side effect of being audited.

---

## E. Where the support runs out — stated, not papered over

1. **Coverage will be thinnest where the question is hottest.** F6
   allocation and conservation both bite hardest at private core nodes
   (OpenAI, Anthropic, xAI) whose disclosure is weakest. The design handles
   this *honestly* (aggregated state, flags) — but honest low coverage is
   still low coverage. The mitigation is the independent-measurement class:
   proven in the field (§B), **not yet proven by this operation at this
   scale**. That is a capability bet, and the plan should be read as making
   it.
2. **The delta pass's labor cost is unmeasured.** The pipeline proves
   *collection*; promotion to observations — each with an assigned
   reliability and a written rationale — is analyst work per item. Nothing
   yet demonstrates that a weekly heartbeat is affordable at the evidence
   bar §4 sets. The heartbeat floor guards against drift, not against cost.
3. **Conservation's diagnostic power phases in.** It needs both sides of a
   node measured; early on, most nodes won't balance-check at all. It is a
   maturing instrument, not a day-one error detector, and the case for it
   should be read that way.
4. **The ⚙ starting values are guesses** — the ~$1B floor, the 0.7/0.35
   band cuts. The design's own answer is that they are *structurally cheap*
   guesses (editable data, labelled on every surface that depends on them),
   which is true and is the right defense — but it is a defense of the
   convention, not of the values.
5. **The bar is open** (§11 item 8, deliberately). Until Ben writes it,
   "will it succeed" can only be judged against §1.5's stated aims — which
   this memo has done — not against a finish line.

---

## Closing statement

The plan's support is strongest exactly where a plan most needs it: at the unit of record and the flow rules, which survive worked operation against the real events they must model, are forced by the actual disclosure regime (the rejected margin method needs undisclosed data), and have already passed one live extension test (q2: zero schema changes); and at the evidence model, whose central bet — independent measurement can beat company statements — the field vindicated in 2025. Support is thinnest on operating cost: the per-pass labor of the evidence discipline is unmeasured, coverage will be weakest at the private nodes where the question burns hottest, and the finish line itself awaits Ben's words.
