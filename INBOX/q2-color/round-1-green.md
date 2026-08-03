<!-- q2 color-team · round 1 · GREEN seat · 2026-08-03
     model: Claude (Fable-tier subagent, fresh context, single-family run; wave 2 after 529s)
     artifact: INBOX/2026-08-03-q2-inference-demand-skeleton.md
     foundation context: INBOX/2026-08-02-q1-skeleton-v2.md
     prompt: INBOX/q2-color/PROMPTS.md §GREEN, dispatched verbatim
     memo below is the seat's return, verbatim and unedited. -->

# GREEN memo — the case for the q2 inference-demand skeleton

**Seat:** GREEN (fresh context; q1 read as foundation only)
**Under review:** `INBOX/2026-08-03-q2-inference-demand-skeleton.md`
**Date:** 2026-08-03

> **Verdict: the q2 plan is the rare skeleton that has already partially demonstrated itself.** Its register seeds were assembled as a byproduct of q1 operation before q2 existed as a plan — the strongest possible evidence for its central claim that q2 is "mostly a view of the map q1 already defines." Its decomposition into WHO / HOW MUCH / WORTH matches, one-for-one, the documented failure mode of the real-world information environment it will operate in.

---

## 1. The three-way decomposition is not taxonomy for its own sake — it names the real world's actual failure

The plan's premise is that press smears buyer identity, realized revenue, and forward obligation into one number. This is not a hypothetical. The canonical episode is on the public record:

- **September 2025, Oracle's Q1 FY26 print.** RPO jumped to ~$455B (+359% YoY), driven overwhelmingly by the OpenAI ~$300B commitment. The market priced the *obligation* as if it were near-certain *revenue*: the stock rose ~36% in a day, adding on the order of a quarter-trillion in market cap — for a contract whose counterparty's annual revenue was then roughly two orders of magnitude below its total committed obligations.
- **October 2025, the OpenAI–Microsoft restructuring.** The $250B Azure commitment was *created* in the same restructuring that *removed* Azure exclusivity and the right of first refusal. Face value went up while the structural lock-in went down — a single event demonstrating that face without structure is not worth, which is exactly the §5 design (face + term + structure + termination clauses + linkage).

A design whose three measurement objects each correspond to a documented, dated, dollar-denominated confusion in the wild is a design justified by evidence, not preference. And this repo's own record independently generated the same diagnosis before the plan was written: the 07-27 capex crawl's cross-cutting finding #2 — *"The payoff layer is the weakest — backlogs and run-rates are press-corroborated; primary filings were unreachable or the mappings (e.g. $250B OpenAI → capex) simply don't exist publicly"* (`artifacts/threads/hyperscaler-capex-big-picture.md:87-89`; also `attention/threads.yaml:761`). The plan's §2 quotes this finding accurately. q2 is a gap the operation *hit*, worked as a question — not a question invented to have one.

---

## 2. The build-on-q1 claim is demonstrated, not asserted

I verified the plan's grounding claims against the repo record. Nine of the ten register seeds exist, with the exact caveats the plan attributes to them:

| seed (plan §5) | verified at | flag as recorded |
| --- | --- | --- |
| AWS backlog "$496B" | `artifacts/threads/aws-capex.md:25` | single-source, exactly as plan states |
| AWS $364B backlog *excluding* Anthropic $100B/decade | `aws-capex.md:85-87`, `threads.yaml:723` | exclusion noted at capture |
| OpenAI→Amazon $50B + $100B/8yr | `threads.yaml:726` | "CONFIRMED (02-27)" |
| CoreWeave backlog conversion | `coreweave-backlog-bet.md` ($66.8B → $99.4B while losses double) | literally the thread's standing question |
| Anthropic→Azure $30B | `ai-circular-financing-risk.md:54` | recorded *tied to* the Microsoft/Nvidia investment — the funding-linkage field already has a live instance |
| AMD warrant deals | `ai-circular-financing-risk.md:120` | recorded as warrant-structured, distinct from straight equity |
| $250B OpenAI→Microsoft | `hyperscaler-capex-big-picture.md:78` | "unmapped" to capex |
| Google backlog $514B | same table, line 77 | "(press-only)" |
| Anthropic TPU/Trainium scale | cross-cutting finding #1 | labs leak what hyperscalers won't |

Two consequences, both strongly in the plan's favor:

- **The seed table self-assembled.** Every one of these observations was captured during *spend-side* (q1-shaped) crawling, with no q2-dedicated sourcing pass. That is a live demonstration of the q1 ruling that the schema carries revenue-type edges before scope reaches them: the "schema stays ready" bet has already paid out. The plan's claim that Tier A can "build the contract register from the seed table" is therefore not a hope — the raw material demonstrably exists, pre-flagged, awaiting the audit step the plan itself mandates.
- **The record already practices the plan's discipline.** The $496B figure was captured *as* single-source; the $364B was captured *with* its exclusion; the $30B was captured *with* its funding linkage. The plan is not asking the operation to acquire a new habit — it is formalizing a habit the operation observably has.

**The "one object promoted, zero schema changes" claim survives scrutiny — and is actually stronger than stated.** q1's F4 rule ("commitments enter at the deployed rate, per period") requires *state* that q1's unit of record — the flow edge — has nowhere to keep: something must hold "up to $500B over four years" alongside deployed-to-date, or F4 cannot be computed. The commitment object's `amortized_to_date` field is precisely that missing ledger. q2's single addition doesn't merely avoid disturbing the foundation; it supplies a piece the foundation's own amortization rule tacitly needed. That is the soundest possible way to build on it.

Two further compatibility facts the plan could claim more loudly:

- **q2 makes q1's headline product computable.** The burn metric (external revenue vs. build spend) is named in q1's own aims as "the 'is any of this real' number." q1 alone delivers a denominator. q2 is the numerator. This is not adjacency — it is completion.
- **The revenue ladder is isomorphic to q1's spend ladder** (claimed run-rate → booked → recognized → collected ↔ guidance → commitment → contract → delivered). One earnings call yields observations for both ladders in a single capture, which is exactly the rework-asymmetry economics ("you can rework anything except what you didn't capture") that justified q1's unit-of-record choice. Sourcers learn one craft, not two.

---

## 3. Operating the design against real dollars — four demonstrations

**(a) The chain rule (§6) bans a number the market is currently mispricing.** Take the real backlog prints: Oracle RPO ~$455B, Microsoft RPO with the $250B inside it, AWS $364B, Google $514B (press-only), CoreWeave $99.4B. A naive "industry AI backlog" sum lands around $1.8T. But the chain is documented: OpenAI commits to Microsoft; Microsoft was historically CoreWeave's dominant customer (~62% of 2024 revenue), procuring neocloud capacity substantially to serve OpenAI workloads. The same future dollar sits in OpenAI's obligation, Microsoft's RPO, and CoreWeave's backlog — three hops, one dollar, precisely the plan's own worked example. The design makes the $1.8T headline *unconstructible*: totals only from boundary-committed or per-node registers. No competing framework I'm aware of in public analyst practice enforces this; it is the q1 F1 rule earning its keep a second time.

**(b) The boundary cut decides the ambiguous cases mechanically.** Is Azure's "$37B AI run-rate, +123%" external revenue? Under the taxonomy: its largest single driver is OpenAI consumption — an in-system node — so that portion is a transfer, never burn-metric numerator. The classification requires no judgment call beyond consulting q1's node roster. The plan's claim that "the load-bearing cut is not sector — it is boundary" is validated by this case: getting OpenAI-inside-Azure wrong would distort the headline metric by tens of billions; getting an enterprise buyer's *sector* wrong moves nothing that matters.

**(c) The commitment object's fields map one-to-one onto the hardest real contract.** The OpenAI↔AMD deal (Oct 2025): 6GW of Instinct purchases against warrants for up to 160M AMD shares (~10%), vesting in tranches tied to deployment and share-price milestones. Run it through the object: parties ✓; face (unpriced in dollars — flagged, per the Anthropic-TPU precedent the register already handles) ✓; term ✓; structure = milestone-vested warrants ✓; funding_linkage = seller-financed via equity upside ✓; amortized_to_date = 0 ✓. Nothing about the deal falls outside the schema, and the linkage field surfaces on the contract's face the exact fact — *the seller is subsidizing the demand* — that a face-value register would bury. Same for Nvidia→OpenAI "up to $100B, progressive per gigawatt": the structure field captures the tranching, the linkage field captures the circle. The design's worth-relevant fields are exactly the fields these real contracts turn on.

**(d) The ladder resolves a standing confusion this repo already owns.** CoreWeave: $99.4B booked backlog, roughly $1B/quarter-scale recognized revenue, deepening losses. The register + ladder turns "is the backlog real?" from a thread's open worry into a queryable ratio (booked vs. recognized vs. collected, per period). The plan converts the operation's own hardest standing question into routine output.

---

## 4. The §10 proposals are the right defaults, for reasons beyond those given

- **(a) The overlay.** The plan undersells its own case: strict-inference is not merely harder — it is *unmeasurable from disclosures*, because no seller splits inference from training revenue and capacity contracts are fungible across both. The real choice is overlay-or-nothing. And the overlay's inputs exist in the wild: public token price cards, aggregator throughput data (OpenRouter), occasional primary disclosures (Google's mid-2025 "980T tokens/month" statement), subscriber counts × price cards. The Tier B requirement to *grade the method's reliability ceiling before using its outputs* is the honest harness for it.
- **(c) Face + structure + flags, no EV modeling.** Sharper justification than "manufactured precision": the discriminating variable for realization is structure (take-or-pay vs. best-efforts), which is *the* undisclosed field. Any v1 expected-value model would therefore collapse to face × assumed-haircut — the press's error with extra steps. Deferral is not caution; it is refusing to launder an assumption into a number.
- **(d) Recognized-only period totals.** Correctly understood, this is a labeling rule, not a collection filter — stage-1 ARR leaks are still captured, still on the record, just never mixed into totals. Nothing is lost; only contamination is prevented.
- **(b) The taxonomy is cheap to be wrong about** — sector misclassification never moves the boundary cut, and the boundary is decidable from the node roster. Exactly what a ⚙ starting list should look like: revisable where revision is cheap.
- **The government seam (§3) is real, and worth more than its dollars.** USAspending, SAM.gov, FedRAMP, and the July 2025 CDAO awards ($200M ceilings each to OpenAI, Anthropic, Google, xAI) are named-buyer, named-amount, primary-source records. But the magnitudes are small against $300B contracts — so the sweep's chief value is as a **calibration set**: a domain where ground truth exists, against which the estimate-driven methods (overlay, surveys) can be graded before they carry weight elsewhere. The GSA $1-per-agency deals even demonstrate face≠worth *inside* the sourceable domain — loss-leader structure visible in primary records. The plan should claim this calibration role explicitly; it strengthens the Tier A case.

**The §7 hypothesis is a genuinely good instrument.** Rough-cutting the verified seeds: intra-system committed face on the order of $1T (OpenAI's ~$650B+ across Microsoft/Oracle/Amazon, Anthropic's ~$130B+, AMD/Nvidia structures, Stargate overlap handled carefully) against realized external inference revenue plausibly in the tens of billions per year. The order-of-magnitude claim survives even the unfavorable unit convention — annualize face over contract terms (~$200B/yr) and the gap is still ~5–10×. A hypothesis robust to its own unit ambiguity is well-formed. One strengthening: **pin the unit convention (total face vs. annualized face) before grading**, so the grade is arithmetic rather than argument.

---

## 5. Where the support runs out — stated plainly

- **The numerator's biggest class is its least observable.** Enterprise direct is predicted low-sourceability *by the plan itself*, and it is likely the largest genuinely-external class. The burn metric's numerator will ship as a reliability-banded range, heavily hatched, for the foreseeable future. The machinery handles this honestly; it does not make the number solid. That the band narrows over time is a hope, not a demonstrated path.
- **Private-lab recognized revenue may be permanently unobservable.** OpenAI, Anthropic, and xAI publish no audited recognized revenue. Decision (d)'s recognized-only totals leave the largest sellers' rows sparse indefinitely; totals will lean on lower ladder stages carried as labeled observations.
- **WORTH ships as annotated face, not worth.** Structure is "usually the undisclosed part" — the plan's own words — so v1's register answers "what are the contracts' faces and what do we know about their reality" rather than "what are they worth." Right call, honestly limited.
- **One boundary placement materially moves the headline and isn't yet flagged as tunable:** the application/reseller layer. If an aggregator (buys in-system API, sells external subscriptions) is drawn in-system, the external crossing happens at its customers; drawn outside, at its API purchases. The reseller class keeps the seam visible, but the placement itself deserves an explicit ⚙ entry.
- **The overlay's reliability ceiling is ungraded.** Until the Tier B probe grades it, "who's buying inference" is operationally "who's buying AI capacity" — the plan knows this; the reader should too.

---

## Closing statement (~100 words)

The plan's support is strongest where it is demonstrated rather than argued: the register seeds self-assembled from q1 operation with their caveats already attached, proving both the schema-readiness claim and the operation's fitness to execute; the commitment object supplies state q1's own amortization rule already required; and the chain rule bans, by construction, a trillion-dollar-scale double-count the market demonstrably commits. Support is thinnest exactly where the world withholds data: enterprise-direct revenue and contract structure are the least observable inputs, yet they dominate the burn metric's numerator and the register's worth column — there the plan offers honest bands and flags, not numbers, and its candor about that is its remaining strength.
