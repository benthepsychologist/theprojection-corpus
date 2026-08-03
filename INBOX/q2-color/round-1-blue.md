<!-- q2 color-team · round 1 · BLUE seat · 2026-08-03
     model: Claude (Fable-tier subagent, fresh context, single-family run)
     inputs: q1 skeleton (foundation) + q2 artifact + round-1-red.md ONLY
     prompt: INBOX/q2-color/PROMPTS.md §BLUE, dispatched verbatim
     memo below is the seat's return, verbatim and unedited. -->

# BLUE memo — q2 inference-demand skeleton (round 1, answering RED)

Seat: BLUE, fresh context. Documents read: q1 skeleton v2 (foundation, §2 register binding), q2 skeleton (under review), Red's round-1 memo. Positions below answer R-1…R-14 in order.

**One root cause, declared once (per discipline):** R-2, R-3, R-6, R-8, and R-9 share a single root — the commitment was *named* as a promoted object but not *specified*: it got a shape without its joins (to flows, to other commitments), without observation staging, without endpoints for external buyers, and without temporal semantics. Blue answers that root once, as the **seam package**, stated under R-2 and referenced thereafter:

1. nullable `commitment_ref` on flow edges;
2. `serves_ref` + `part_of_ref` + a `side` discriminator (supply-build / demand-capacity) on commitments;
3. a `measurand`/`stage` field on observations, with the placement rule (stages 1–2 attach to commitments, stages 3–4 to revenue edges), and `figure` generalized to a typed value so structure/clause states are dated, sourced, superseding observations under the one existing evidence model;
4. a sanctioned external-population node class (`ext/consumer`, `ext/enterprise-<sector>`, `ext/gov-<jurisdiction>`) with inbound allocation as claims, mirroring F6.

Plus one sentence-level correction upstream: the q1 R-13 *annotation* ("zero schema changes") is amended to "no redesign: one promoted object plus a handful of additive fields, cheap before sourcing." The R-13 *ruling* (scope) is untouched — Red's own separation of ruling from annotation is correct and Blue adopts it.

---

### Blue on R-1 — the external/intra boundary predicate

POSITION: PARTIAL CONCEDE.

One sliver of defense: q2 §3's own first bullet already separates the two axes — "the load-bearing cut is not sector — it is boundary" — so the taxonomy row "resellers/aggregators" is a WHO bucket, not a boundary verdict; the doc does not commit to counting them as external, and Red's "both readings are available" is slightly generous to the wrong reading. But that defense only shrinks the charge from *contradiction* to *undefined* — and undefined is Red's actual finding: the predicate the burn metric and the §7 hypothesis hang on does not exist, and the resale regress has no terminal rule. Red is also right that q1 dissolved the boundary as a *depth* question while q2 needs a *membership* predicate — a genuinely new requirement, not covered by F7. The fix falls out of the plan's own consolidation logic (an entity consolidates when its product is materially resold system capacity), so it is congruent, not a redesign — but it must be written before sourcing, and it cannot wait on the Tier B reseller probe, because Tier A surfaces depend on it.

RESPONSE: Add a revenue-side boundary rule (F9): a buyer is **external** when its AI-resale share of purchased capacity falls below a ⚙ threshold (starting value to the §12-style table); above it, the buyer is in-system and measurement moves one hop outward, capped by F7's materiality machinery (the anti-regress terminal). Boundary classification is a claim — recorded per buyer with observations, rationale, and reliability per q1 R-04/F6, never a silent sourcer judgment. Annotate §3's reseller row: "boundary status per F9, per entity."

### Blue on R-2 — `commitment_ref` and the "zero schema changes" claim

POSITION: CONCEDE.

Red is right, and right in the way that matters most to this design: the missing linkage is exactly the rework-economics class q1 §1.5 says must land before data accumulates. OpenAI→Microsoft demonstrably carries multiple concurrent money relationships, so a bare pair-plus-period cannot attribute a flow to a commitment; `amortized_to_date` is otherwise either a drifting second source of truth or a derivation over a field that doesn't exist. Blue notes the pointer's *direction* (edge-side field vs commitment-side drawdown list) is an implementation detail — but arguing direction would merely relocate the problem, so Blue accepts Red's form: the sourcer stands at the flow when recording, and the edge-side nullable field is the minimal honest spec. The seam-package root cause is declared here; R-3, R-6, R-8, R-9 draw on it.

RESPONSE: Seam package item 1 — nullable `commitment_ref` on flow edges, added before any sourcing pass. Amend the q1 R-13 annotation as stated in the preamble.

### Blue on R-3 — chain and containment relations on the commitment

POSITION: PARTIAL DEFEND.

Red's headline — "§6's sanctioned aggregate, 'boundary-committed,' is uncomputable as specified" — overstates. Boundary-committed needs no chain relations, for the same reason F1 needs none: the boundary filter *is* the dedup. Every hop downstream of an external buyer's commitment (Microsoft procuring neocloud capacity to serve it) is intra-system by construction and never enters the sum; the aggregate awaits only R-1's classification predicate, which is a different finding. What Red gets right is aggregate (b) and everything downstream of it: a per-node register genuinely cannot represent frame⊃constituent overlap — Stargate and the Oracle contract sit on the *same* OpenAI register, so even the sanctioned per-node view double-counts without `part_of_ref` — and `serves_ref` becomes necessary the moment anything sums intra-system faces (the restated §7 hypothesis, R-10's reconciliation). Both relations are cheap now and unpayable later; conceded on those grounds, which are narrower than Red's.

RESPONSE: Seam package item 2 — `serves_ref`, `part_of_ref`, and the `side` discriminator on the commitment object. No change to §6's definition of aggregate (a), which stands as computable.

### Blue on R-4 — the hypothesis is ungradeable as stated

POSITION: CONCEDE.

The window argument is decisive and Blue will not defend against arithmetic: "roughly an order of magnitude" cannot absorb a free parameter that swings the ratio by *two* orders of magnitude (trailing-quarter vs full-term), and gradeability is not optional — q2 inherits R-09, so a hypothesis that cannot be graded violates the register it claims to inherit. One narrowing note, which changes the amendment's character rather than its content: §6's ban is on *published headline totals*; a deduped intra-system sum computed internally to grade a hypothesis is legitimate once R-3's relations exist. So the remedy is a restatement of the hypothesis in gradeable units, not a retraction of it — the hypothesis itself remains the right bet to write down before sourcing.

RESPONSE: Restate §7: "**Demand-side** intra-system committed face **amortizing into the next 12 months** (per F4 mechanics, deduped via `serves_ref`/`part_of_ref`) exceeds **trailing-12-month recognized-or-derived external inference revenue** by ≥10×." The `side` discriminator (seam package) supplies the filter; the register's supply-build rows (Stargate) fall out of the LHS.

### Blue on R-5 — recognized-only makes the RHS near-empty

POSITION: PARTIAL DEFEND.

The ladder is measurand hygiene, not rank-by-type resurrected: an annualized instantaneous run-rate is a *different quantity* from a quarter's recognized revenue, and barring the raw claim from a period total is unit discipline, not deference to source class. Nothing in q2 bars a **derived** recognized-revenue estimate: q1 §4's "analyst/model estimate" and "inference from other claims" classes are first-class, inherited in full, and q2 itself recommends exactly this move for the overlay — so the machinery Red prescribes as the fix is already in the plan, which is why this is a defense and not a redesign. The rendering bands then give graduated inclusion (a well-crafted derivation sits hatched, and headline totals quote solid+hatched with the split stated). What Blue concedes: decision (d)'s compressed wording "recognized only" invites the null reading, a sourcer operating it as written would zero out the two largest external sellers, and a one-sided emptiness in the denominator of §7's grade is a real confirmation bias. The gap is one clause, not a structure.

RESPONSE: Amend decision (d): "'Recognized' includes **derived recognized-revenue estimates** (annualization unwound, haircut, method note; provenance and reliability per q1 §4) where a seller discloses no recognized figure. The ladder gates raw claims by measurand; it never ranks sources by type."

### Blue on R-6 — the ladder has no carrier in the observation record

POSITION: CONCEDE.

Red is right and anticipated the only defense: `method_note` is prose and cannot drive a hard "never mixed" rule, and an ARR claim genuinely has no honest `period` — whatever a sourcer writes there, the weighted read will consume it. The Oracle-RPO worked case (one figure that is simultaneously a stage-2 revenue observation and a face-value observation, recorded twice and reconciled never) demonstrates that the stage field alone is insufficient without a placement rule, and Red supplied the right one. This is the seam root; the amendment also carries half of R-9 via the typed-value generalization.

RESPONSE: Seam package item 3 — `stage`/`measurand` on observations; placement ruled: stages 1–2 attach to the commitment object, stages 3–4 to revenue edges, joined by `commitment_ref`.

### Blue on R-7 — the government seam sources ceilings and middlemen

POSITION: PARTIAL CONCEDE.

Defended in part: the disclosure regime is not oversold, only under-specified — the same records contain task-order actions and outlays, so "government: high" survives *for the specced sweep*; and decision (d)'s ladder already blocks the worst failure Red describes, since a $9B IDIQ ceiling is stage-2 and cannot enter a period total as written. But everything operational in the finding is conceded, and it is the strongest field-knowledge in Red's memo: the sweep as designed would harvest ceilings and middlemen, the vehicle-of-record problem (Carahsoft, CSP consumption vehicles) makes the "named" seller the wrong counterparty, the OneGov $1-per-agency deals post approximately zero dollars at exactly the largest adoption events, and the prediction table would therefore grade a win on the wrong measurand. Red's remedy is accepted wholesale as the Tier A spec the plan should have carried.

RESPONSE: Spec the Tier A sweep to task-order-level actions and outlays, never award ceilings; capture `contract_vehicle` per record; name the vehicle→OEM unwinding map as an explicit Tier A deliverable; flag nominal-price awards as adoption evidence, not revenue.

### Blue on R-8 — external buyers have no node type

POSITION: CONCEDE.

Correct, and Red's own framing — "a small, honest schema addition, better named now than improvised per-sourcer" — is the right disposition. q1 never needed anonymous counterparties because its externals were identifiable suppliers; q2's external buyers are populations, and a sector-share survey observation has no attachable endpoint in an entity×activity graph. Blue adds one supporting ground Red missed: the population node class is the revenue-side mirror of q1's own "other inputs" collapse edge (F7) and of F6's allocation-as-claim — so the addition extends existing design moves rather than inventing a new kind of thing, which is why it is cheap.

RESPONSE: Seam package item 4 — the `ext/*` node class, with inbound allocation recorded as claims with observations and reliability.

### Blue on R-9 — term movement is uncapturable

POSITION: CONCEDE.

Red catches the plan violating its own named principle at its own named canonical case, which is the least defensible position available: q2 cites the OpenAI–Microsoft restructuring as "the canonical warning that terms move," then specifies scalar current-state fields that would record that exact event as "still $250B" and lose it. Under the capture asymmetry ("you can rework anything except what you didn't capture"), an undated clause state is the one non-recoverable error class. Blue's only refinement is to the remedy's mechanism: rather than bolting a parallel history apparatus onto the commitment, generalize the observation's `figure` to a typed value so structure, clauses, and linkage states are ordinary dated, sourced, superseding observations — one evidence model, with provenance, reliability, and capture discipline applying unchanged.

RESPONSE: Seam package item 3 (typed-value generalization): every worth-bearing field is observation-bearing; a commitment's term history is the observation sequence, never a mutable scalar.

### Blue on R-10 — backlogs in the register vs against it

POSITION: CONCEDE.

The strongest constructive finding in the memo, and Blue declines the available lawyering (that "seeds" are audit leads rather than register rows) because decision (e) says plainly "v1 register roster — the ten seeds in §5," which makes the two party-less RPO aggregates register rows as written. Red's reframe is better than a fix: sum-of-node-faces vs disclosed-backlog reconciliation is the demand-side analog of q1's conservation check — the per-node diagnostic q2 currently lacks entirely — and the doc proving the point by holding the perfect fact (Anthropic→Amazon *excluded* from AWS's stated backlog) with nowhere structural to put it is conclusive.

RESPONSE: Split the seed table: eight commitment entries; CoreWeave and AWS backlog rows become node-level backlog observations. Define per-node backlog reconciliation (Σ active register faces vs disclosed backlog; gap = unregistered committed inbound) as a first-class coverage surface. Amend decision (e) accordingly.

### Blue on R-11 — the overlay estimates capacity share, not revenue share

POSITION: PARTIAL CONCEDE.

Defended in part: §8's probe brief already gates the overlay — "design it, grade its reliability ceiling **before using its outputs**" — so the mis-split is not yet baked into any surface; there is a designed checkpoint between the method and a published dollar. But the estimand error in decision (a)'s proposed position is real and conceded: token economics and traffic measure physical utilization mix, the question is revenue mix, and the price differential between discounted committed training capacity and retail API inference means the two diverge most at exactly the heterogeneous sellers the plan cares about. A probe briefed to grade the reliability ceiling of the *wrong measurand* could pass its gate and still mis-split — so the units requirement belongs in the brief now, where it costs a sentence.

RESPONSE: Respec decision (a): the overlay's output is a **revenue** share — utilization mix (tokens, traffic, subscriber math) × price mix (price cards, disclosed contract rates). An overlay lacking the price term is a capacity share, labelled as such, and banned from multiplying into dollars. Tier B probe brief inherits the same language.

### Blue on R-12 — no destination category for purchased capacity

POSITION: CONCEDE (LINE tag affirmed).

Right, and cheap by the plan's own design: the category list is ⚙ and ruled re-cuttable (q1 R-14), which exists precisely so this class of gap is a data edit rather than a design flaw. Since q2's largest new flow class is known *in advance*, waiting for other/unallocated to bloat before re-cutting would waste the convention.

RESPONSE: Add "purchased compute capacity (services)" to the ⚙ destination-category list in q1 §12 as part of q2's landing.

### Blue on R-13 — face-sourceability vs worth-sourceability

POSITION: CONCEDE (LINE tag affirmed).

Right, with the plan's own text as witness: §5 says structure is "usually the undisclosed part" while §7 predicts "in-system contracts: high" undifferentiated — the table compresses away the distinction the same document draws. Since worth hangs on structure, the grade as written would score a win on the wrong measurand, which is exactly what the grading discipline (R-09) exists to prevent.

RESPONSE: Split the in-system row per worth-bearing field: face — high; structure — low; termination clauses — low. Apply the same per-field split anywhere worth (not just face) is the measurand.

### Blue on R-14 — the consumer seed vs the stated method

POSITION: PARTIAL DEFEND.

The seed table never claims the ~1B weekly-actives figure feeds the subscriber math — §4 introduces it as "seeds already in this map's record," i.e., an inventory of what is already held (flagged single-benchmark at that), not the method's input spec. "Doesn't serve the stated method" is literally true and establishes no error in the plan. The useful remainder is conceded: the method's dominating input — paying conversion — appears on no list anywhere in the document, and an input that dominates the estimate deserves a named chase rather than discovery mid-sourcing.

RESPONSE: Add to Tier A consumer sourcing: paying-subscriber counts and paying-conversion rate, each recorded as its own sourced, estimated claim. The WAU seed stays as what it is — a recorded benchmark.

---

## Closing (~150 words)

**Counts:** 8 CONCEDE (R-2, R-4, R-6, R-8, R-9, R-10, R-12, R-13) · 3 PARTIAL CONCEDE (R-1, R-7, R-11) · 3 PARTIAL DEFEND (R-3, R-5, R-14) · 0 full DEFEND. All of Red's tags affirmed.

**Expected substantive carries:** all eleven draw amendments, but they compress to four design changes — the F9 boundary rule (R-1); the commitment-seam package (R-2/3/6/8/9); the hypothesis restatement plus derived-revenue clause (R-4/5); and operational specs (R-7/10/11). None retracts a q2 position; nothing touches the rulings register.

**Pattern:** Red's substantive findings are internal-consistency attacks — the plan's own principles (rework economics, capture asymmetry, gradeability, the rank-by-type ban) turned on its gaps — which is why most must be conceded. Red's one recurring overreach is reading "unspecified as written" as "impossible as designed" where existing machinery (the boundary filter for aggregate (a), the inherited evidence model, the probe gate) already holds the fix; all three partial defends narrow on exactly that ground.
