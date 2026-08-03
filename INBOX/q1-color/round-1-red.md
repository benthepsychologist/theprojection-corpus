<!-- q1 color-team · round 1 · RED seat · 2026-08-03
     model: Claude (Fable-tier subagent, fresh context, single-family run)
     artifact: INBOX/2026-08-02-q1-skeleton-v2.md
     prompt: INBOX/q1-color/PROMPTS.md §RED, dispatched verbatim
     memo below is the seat's return, verbatim and unedited. -->

# RED memo — q1 decomposition skeleton v2

Read fresh, no workshop context. All dollar figures below marked *(illustrative)* are round numbers used to exhibit mechanics, not sourced claims.

---

## Findings

**R-1. SUBSTANTIVE. The design's two accounting principles classify its own flagship transaction both ways — the rollup cut is never defined.**

- **Demonstrated failure.** §1.5 rules that under consolidation, "intra-system sales… never add to system totals; only boundary crossings are system revenue or system cost." F3 rules that "an investment converts to build at the moment it is spent — Nvidia's $100B into OpenAI enters build when OpenAI buys something real with it." But the thing OpenAI buys is GPUs *from an in-system vendor* — an intra-system sale. The same transaction is simultaneously "enters build" (F3) and "a transfer that never adds to system totals" (§1.5). F1 has the same fracture internally: "totals come only from boundary crossings and category rollups." Read the rollup as *all purchase edges by category* and you chain-sum under a category disguise — Meta→Nvidia $50B *(illustrative)* tagged compute-silicon plus Nvidia→TSMC $18B *(illustrative)* tagged compute-silicon gives a $68B category total for ~$50B of final spend, violating F1's own first clause. Read the rollup as *boundary crossings only* and Meta→Nvidia — the main event of the entire question — is excluded from "what the money buys." Both readings fail; no third is defined. The §11 bar scaffold then denominates success in "final-buyer spend," a concept the schema nowhere defines.
- **Why it matters.** The category rollup is one of the two named instruments of the whole plan. As specified, its value is either double-counted or excludes GPU purchases — the sourcer cannot know which edges they are sourcing *for the headline* and which for resolution only.
- **Remedy.** Define two totals explicitly and name them: (a) **gross build at the final-buyer frontier** — purchase edges whose buyer node is a terminal asset owner/operator (the natural home of the category rollup and of "final-buyer spend"); (b) **consolidated boundary cost/revenue** — the net-vs-rest-of-economy view. Interior edges feed resolution and the optional value-added lens, never totals.

---

**R-2. SUBSTANTIVE. No membership predicate — so totals are a function of tracing depth, and the delta ledger cannot distinguish "the world moved" from "we traced further."**

- **Demonstrated failure.** §3 dissolves the roster: "inside/outside stops being a yes/no per company and becomes 'how far the money is traced.'" But consolidation (R-03, F3) *requires* a yes/no per counterparty to classify each edge as transfer vs boundary crossing. Walk it: in pass 1, Meta→EPC $10B *(illustrative)* is a boundary crossing (EPC untraced). In pass 5, the EPC becomes a node (dc-construction is a core activity) — the same edge silently reclassifies to intra-system, and the boundary crossings are now the EPC's steel, labor, and equipment purchases, at different magnitudes and different categories. **The headline total and category mix change with zero real-world change.** §6's delta pass "emits what changed in the system this period" with no typing, so this coverage artifact, an ordinary observation revision, and a ⚙ retune (moving a band cut changes every solid+hatched headline) are all indistinguishable from actual system movement — the exact signal R-08 exists to produce. Two more membership exhibits: "capital sources" and "tax incentives" are among the twenty live activities, so investors and government incentive flows are arguably *in-system* — making equity inflow never a boundary crossing and "how much external capital is entering" unaskable in boundary terms.
- **Why it matters.** The delta ledger is ruled "a first-class product surface, equal in rank to the map." As designed it will emit phantom deltas on every deepening or retuning pass, and its consumers cannot tell.
- **Remedy.** (a) A **versioned consolidation perimeter**: an explicit, criteria-based, dated membership list; tracing depth changes resolution, never classification. (b) **Typed deltas**: world-event · revision · coverage-extension · parameter-retune, with totals stamped by the parameter-set version they were computed under.

---

**R-3. SUBSTANTIVE. The observation schema omits the stage/basis axis that is the plan's own stated motivation — and reconciliation is arithmetically undefined without it.**

- **Demonstrated failure.** §1.5 diagnoses the 3× public ambiguity as press collapsing "four different stages of money — guidance, commitment, contract, delivered asset." The cure for stage-collapse is to *record the stage* — yet the observation tuple `{figure, as_of, period, source, provenance_class, capture_ref, reliability, rationale, method_note}` has no stage field, and `period` ("the quarter or finer") cannot even represent "up to $500B over four years, unscheduled." Consequence: §4's reconciliation — "an edge's magnitude is the weighted read across its observations" — is asked to average obs₁ = $500B (guidance, multi-year) with obs₂ = $18B *(illustrative)* (deployed, one quarter). That weighted read is not a number with meaning, and the "disagreement beyond tolerance" flag will fire on every commitment-bearing edge purely from stage mixing. A second facet: no accounting-basis field (cash vs accrual vs delivery) — Nvidia recognizes on delivery, Meta capitalizes on placement-in-service, cash moves on payment terms, so the two sides of one edge legitimately sit in different quarters and per-period reconciliation flags spurious conflicts.
- **Why it matters.** This touches the one thing the design says is non-recoverable: capture. Stage is re-derivable from captured excerpts, but only by re-reading every capture; and until it exists, F4 ("commitments enter at the deployed rate") is inoperable because nothing marks which observations speak to deployed vs committed. It also breaks the aim "news becomes model-delta": a megadeal announcement (the biggest news class) produces no queryable model state until deployment evidence arrives quarters later.
- **Remedy.** Add `stage` (guidance | commitment | contract | delivered) and `basis` to the observation; allow a commitment-shaped period (span + schedule-if-known); reconcile only within (stage, basis, period) cells; let the delta ledger report stage transitions as first-class events.

---

**R-4. SUBSTANTIVE. Conservation cannot fire where it matters and is trivially satisfied where it can — "localizes error to a specific actor" over-claims.**

- **Demonstrated failure.** The identity is money in = money out + **retained**. For the actors at the center of the circularity question — OpenAI, Anthropic, xAI, private neoclouds — retained is a free variable: no balance sheet, no cash disclosure. Any imbalance is absorbed into "retained," so the check never flags. At entity×activity subnodes (`samsung/foundry`), retained isn't even a defined quantity anywhere on earth. Where the check *can* run — public filers at whole-entity level — the filing balances by construction, so it detects nothing the filing didn't already say. Two additional spurious-imbalance sources: F8 attributable-share counting (a node carrying 30% of a substation's flows arithmetically cannot conserve against 100%-basis flows on its other edges) and the timing-basis mismatch from R-3.
- **Why it matters.** §1.5 sells conservation as the structural advantage over the strawman's residual ("localizes error to a specific actor instead of one system-wide residual"). As specified the diagnostic is silent precisely on the private, opaque actors it was wanted for.
- **Remedy.** Add a per-node **closure state** (conservation-testable: yes/no + why); treat `retained` as a claim requiring its own observation (cash-on-hand leaks, funding-round balance math) before conservation is asserted; declare whether conservation runs pre- or post-F8 attribution.

---

**R-5. SUBSTANTIVE. Per-edge origination tags assume traceable dollars; fungibility makes the "industry paying itself" number a function of an unstated convention.**

- **Demonstrated failure.** §3 requires every financing edge to carry one source-of-funds tag (operating cash · debt · equity · vendor · sovereign). But purchases are paid from a commingled pool. OpenAI in one period *(illustrative)*: $40B vendor/equity in, $10B debt, $10B revenue; pays Oracle $30B. Which tag does the Oracle edge carry? Specific tracing (Nvidia's dollars → Oracle) is unobservable; pro-rata, FIFO, and "earmarked-first" conventions give materially different answers, and nothing in the design picks one. Two sourcers tag the same edge differently and both comply. The flagship query this feature exists for — "how much of this is the industry paying itself" — moves by tens of billions depending on the convention.
- **Why it matters.** Origination is q1-native by ruling (R-10); this is the mechanism that was supposed to make it queryable "instead of a vibe." Unconventioned, it's a vibe with a schema field.
- **Remedy.** Record origination at the **(entity, period) funding-pool level** (sources in, uses out — observable from disclosures); derive per-edge attribution through an explicit ⚙ allocation convention; reserve direct edge tags for contractually earmarked financing (vendor financing tied to specific purchases, project finance).

---

**R-6. SUBSTANTIVE. F7 does not terminate — the activity list itself spans the supply chain, so the recursion re-enters through the door the ruling closed.**

- **Demonstrated failure.** F7 models any "direct purchase by an in-system activity" with no floor; the floor binds only one hop further. But the twenty in-system activities include the bottom of the physical chain (minerals & refined inputs, labor, water, land). Walk it: TSMC buys palladium → refiner is performing "minerals & refined inputs," an in-system activity → the refiner's ore purchase is a *direct purchase by an in-system activity*, modeled with no floor → the miner is also plausibly "minerals" → in-system → the miner's Caterpillar equipment purchase is a direct purchase, modeled → Caterpillar's steel suppliers are the +1 hop, and "steel purchased by equipment makers" as a system-wide edge-class plausibly clears ~$1B/yr. That is the tractor-bolts regress R-07 explicitly forbids, reached in four steps by following F7 as written. The termination R-07 wants exists only if activity *membership* is bounded — and no instantiation rule exists (this is the same missing predicate as R-2).
- **Why it matters.** F7 is what makes "physically complete but bounded" a claim rather than a wish; as written the effective bound is Tier priority, i.e., whatever sourcers happen not to get to — exactly the un-auditable darkness R-06/R-09 were built to abolish.
- **Remedy.** An **instantiation rule**: an entity×activity node comes live only when its AI-attributable flow clears the materiality floor; purchases by non-instantiated entities collapse to "other inputs" at the parent; the floor conditions *all* edges, not only the +1 hop.

---

**R-7. SUBSTANTIVE. Inference-class observations carry no dependency references — upstream revisions rot derived figures silently, in a system whose whole point is revision.**

- **Demonstrated failure.** §4 admits "inference from other claims in the map" as a provenance class, but the observation tuple has only free-text `method_note` — no structured pointer to the claims an inference derives from. Walk it: TSMC's AI-attributable revenue is inferred from a Nvidia order-volume observation; a later delta pass revises the Nvidia figure down 30%; the derived TSMC observation persists at its stale value, the edge stays "measured," and no flag fires — the discrepancy check only compares observations *on the same edge*. Nothing in the design can even enumerate which observations are downstream of a revised one.
- **Why it matters.** This is a capture-side gap, the one class the plan itself calls non-recoverable: once inferences accumulate unlinked, retrofitting lineage means re-deriving every inference by hand. A living model with unlinked inference is a model that quietly disagrees with itself more each pass.
- **Remedy.** Require `derived_from: [capture_refs / observation ids]` on every inference-class observation; the delta pass propagates invalidation (revised upstream → downstream observations flagged for re-derivation).

---

**R-8. SUBSTANTIVE. The forward intake channel structurally starves the independent-measurement class — the model will drift into exactly the deference R-05 was built to prevent.**

- **Demonstrated failure.** §6: the delta pass "rides the collection pipeline that already runs daily — collected items become candidate observations." That pipeline collects *news*. News supplies company statements and press — the two classes §4 labels incentive-laden. The class the project "actively cultivates" — customs manifests, satellite analysis, interconnection-queue filings, permits — does not arrive as news items and has no acquisition mechanism anywhere in the plan: Tier B probes ask *whether* a measurement path exists (one-shot), nothing converts a found path into a recurring collector, and Tier A — where independent measurement is supposed to counterweight guidance *now* — has no independent-source tasking at all. So the baseline may start balanced, but every forward pass adds company-provenance observations and almost nothing else; track-record weighting can only weigh observations that exist.
- **Why it matters.** R-05's headline feature — a crafted independent measurement outweighing company guidance — never gets exercised, not because of ranking (the thing that was fixed) but because of supply (the thing that wasn't). The model converges on the companies' own narrative by availability.
- **Remedy.** Probes must *output collectors*, not just verdicts: a positive probe result becomes a scheduled sweep (queue filings and permits are free and public) attached to the delta pass. The pass definition should name its intake channels plural: news promotion + independent-source sweeps.

---

**R-9. SUBSTANTIVE. The burn metric is named as a q1 aim that q1's own scope cannot compute.**

- **Demonstrated failure.** §1.5 lists two instruments that "fall out and are themselves aims": the category rollup and the **burn metric** ("external revenue vs. internal build spend"). But R-13's consequence puts inference selling and downstream revenue in q2, and §5 gives them only a Tier B reconnaissance probe in v1 — a probe answers "does a measurement path exist," it does not produce the revenue-side number. v1 as scoped delivers a burn metric with an empty numerator. (Separately, "external revenue vs internal build spend" mixes the consolidated-net view with the gross-build view — resolvable, but only once R-1's two totals exist to mix.)
- **Why it matters.** The burn metric is the "is any of this real" number — the single output a reader most wants. Shipping v1 without saying this aim is deferred invites the plan to be judged against a promise its scope already broke.
- **Remedy.** Either (a) strike the burn metric from q1's stated aims and mark it q2-delivered, or (b) add one bounded Tier A item: *boundary-aggregate* external AI revenue per final-seller node (a handful of disclosed/estimated totals, not the full q2 demand decomposition).

---

**R-10. SUBSTANTIVE. The looked-vs-didn't-look distinction is only recorded where probes run — Tier A's negative results have no home.**

- **Demonstrated failure.** §3's coverage table defines unmeasured as "looked, or not yet looked — the probe record (§7) says which." But §7 probe records exist only for Tier B activities, and are per-activity, not per-edge. A Tier A sourcer who hunts hard for, say, Broadcom's networking-attributable split and finds nothing produces no record at all — so a Tier A unmeasured edge is permanently ambiguous between "opaque" and "unattempted," which is precisely the distinction §1.5 claims is "auditable."
- **Why it matters.** The audit claim (§1.5, R-09's generalization) silently covers only half the model — and the half where most of the money is.
- **Remedy.** A negative-result log discipline for all sourcing, not just probes: any sourcing attempt that ends unmeasured writes what was tried and when, attached to the edge/node.

---

**R-11. LINE. F7 and §12 disagree on where the floor binds.** F7: one hop further "AND the flow clears the materiality floor." §12's restatement: "direct purchases + one further hop **trace fully**" — which reads as the +1 hop being unconditional. Two statements of the same rule, different binding condition; a sourcer following §12 traces edges F7 says to collapse. Remedy: make §12's cell quote F7's condition verbatim.

**R-12. LINE. The reconciliation tolerance is an unregistered tunable.** §4 and R-04 hang the entire flag surface — "a product surface," per §4 — on "disagreement beyond tolerance," and tolerance appears nowhere in §12, whose stated contract is "every tunable value… collected here so none of them hides in prose." The flag rule cannot run without a value, and the registry's completeness claim is currently false. Remedy: add a ⚙ tolerance row (even a crude starting rule, e.g., relative-spread threshold per edge magnitude band).

**R-13. LINE. Financing edges are required to carry a destination category that has no value for them.** §3: every edge carries "destination category — what kind of thing the money bought." Equity/debt/prepayment edges buy nothing; the eight-value list has no none/financing value. Sourcers will improvise inconsistently. Remedy: make destination category required on purchase edges only, or add an explicit `financing — n/a` value.

---

## (a) Overall read (~100 words)

Not ready to source against yet — but close, and the failures are concentrated, not diffuse. The evidence layer (observations, provenance/reliability split, capture discipline) is fundamentally sound; the accounting layer above it is underdefined at exactly the load-bearing joints: what totals mean (R-1), who is inside (R-2/R-6), and what an observation must carry to be reconcilable (R-3). By the plan's own asymmetry — you can rework anything except what you didn't capture — R-3 and R-7 must land *before* sourcing starts; R-1, R-2, R-5, R-6 must land before any total or delta is published; the rest can be fixed in flight.

## (b) Counts

**SUBSTANTIVE: 10** (R-1 through R-10) · **LINE: 3** (R-11 through R-13).

## (c) Survival prediction

**6 substantive survive adjudication.** Likely merges: R-1+R-2 (shared root: no defined cut/perimeter) and R-2+R-6 (shared root: no membership predicate) could consolidate to two findings; R-9 may be adjudicated as an aims-wording fix and R-10 downgraded to LINE. R-3, R-5, R-7, R-8 I expect to survive intact.
