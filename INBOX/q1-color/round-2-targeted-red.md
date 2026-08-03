<!-- q1 color-team · round 2 · targeted RED · 2026-08-03
     model: Claude (Fable-tier subagent, fresh context)
     inputs: q1 v3 + round-1-white.md + round-1-red.md (original constructions)
     bar: ZERO new/persisting substantive carries
     memo below is the seat's return, verbatim and unedited. -->

# RED memo — q1 skeleton v3 · round 2 (targeted pass on the 8 carries + 5 line carries)

Read fresh: v3, then the WHITE adjudication, then the original RED constructions (`round-1-red.md`) to test v3 against the failures as originally built, not against round 1's remedy text — per the R-16/R-17 instruction. Rulings R-01–R-18 treated as binding throughout; nothing below argues with a ruling.

> 🎯 **Verdict: 7 of 8 RESOLVED, 1 PARTIALLY RESOLVED — the revision misses the zero bar by exactly one carry, and the miss is two sentences wide.** The filter design (R-16) kills the membership-family failures more thoroughly than round 1's own perimeter remedy would have. The one residue is in the item-1 edge-typing rule, where the fix's wording re-admits the failure mode it exists to close, at one edge class.

---

## Per-carry statuses

**1. Two named totals + capacity-service-vs-build typing — PARTIALLY RESOLVED · SUBSTANTIVE.**
What's fixed is real: the two totals are named, and **"operator frontier" is now a predicate** ("operates the acquired asset rather than reselling it") where v2's "final-buyer spend" was a phrase — the $68B-for-$50B construction dies (Nvidia→TSMC fails the operator test under either typing), and the OpenAI→Oracle ambiguity dies (`capacity/service payment`, never build; a neocloud's own GPU purchase is the one counted build event). The remaining piece is the fix's own wording: *"a payment for compute capacity **or services** … is NEVER build."* Read narrowly ("compute capacity-or-services") it's correct; read broadly, **payments to an EPC for constructing a datacenter the buyer will operate are "payments for services" → NEVER build** — and datacenter construction, one of the largest physical components of the buildout, falls out of the flagship total. The two clauses of the rule collide on exactly this edge class (an EPC contract is simultaneously "a payment for services" and "asset acquisition"), so the type a sourcer picks once again silently decides what enters gross build — the round-1 mode recurring at a new site, introduced by the remedy's phrasing. Round 1's own W-1 lesson applies: a rule that a competent operator must interpret correctly is the defect, not a defense. Second, smaller piece: the §12 category **"purchased compute capacity (services)"** is unreachable by the category rollup as defined (the rollup "reads at" gross build = `asset purchase` edges only), yet it's the only carrier for R-17's "a surface that could not decompose past a reseller says so on its face." **Refined remedy (two sentences):** (i) type by what the payment procures — use of another party's capacity/services = `capacity/service payment`; creation or acquisition of an asset the buyer will operate = `asset purchase` regardless of contract form (EPC, construction, engineering); (ii) state the rollup's read set = operator-frontier asset purchases **plus** non-decomposed capacity/service crossings of the cut, rendered as purchased-compute-capacity per R-17.

**2. Membership/instantiation (merged R-2+R-6), now via R-16 filters — RESOLVED.**
I ran all three original constructions against the filter design and all three are dead. *Reclassification walk:* classification now lives in the filter's membership list, never in node existence — instantiation "never changes any filter classification," and when the Meta→EPC dollars do move from external-cost to transfer, that movement decomposes into a **coverage-extension delta** (typed) and/or a **filter-version bump** (typed retune), with every published total stamped (map version, filter version, ⚙ set) — the round-1 defect was never that totals move but that consumers *couldn't tell why*; now they can, mechanically. *Tractor bolts:* the instantiation predicate is **activity-independent** — the palladium refiner's "in-system activity" escape hatch is gone because activities no longer confer membership at all; below the ⚙ floor an entity never instantiates and its upstream is never traced, and F7 now conditions all tracing. *Capital-sources exhibit:* `cut:core-buildout` explicitly places capital providers and governments outside, so equity inflow is a boundary crossing again — the "unaskable" query is askable under a named cut. White's added requirement (perimeter version on the totals stamp) survives as the filter-version stamp. One prose nit, not a carry: §1.5's "totals can **never** wobble when tracing deepens" oversells — instantiating an already-listed filter member legitimately moves the boundary total (typed coverage-extension); the machinery is honest, the sentence should soften to match it.

**3. Stage/basis axis — RESOLVED.**
All five punch-list components are present and mutually wired: `stage` and `basis` on the tuple; the commitment-shaped period (so "$500B over four years, unscheduled" is representable without lying about a quarter); reconciliation confined to (stage, basis, period) cells with the cross-stage weighted read **undefined by rule** — which kills the guidance-averaged-with-delivered failure outright rather than tolerating it; the cross-stage consistency flag (delivered ≤ contracted ≤ committed) as its own flag class; and stage transitions as first-class typed delta events in §6. F4, inoperable in v2, now has an operating definition: deployed rate computed from `delivered`-stage observations joined via `commitment_ref`, face values barred from flow totals. The imported typed-value field (point/bounds/scope-qualified, bounds as constraints) strengthens the cell semantics further.

**4. Conservation/closure discipline — RESOLVED.**
Every element of the narrowed remedy is in: per-node **closure state** (testable yes/no + why), `retained` as a claim requiring its own observation before conservation is asserted, the check running on full-basis **pre-F8** flows per (basis, period) cell (killing both spurious-imbalance sources — share-basis mixing and timing-basis mixing), the public-filer check correctly framed as the map's assembled edge set against filed totals (a real coverage/double-count diagnostic), and opaque privates honestly marked non-closing rather than silently passing. The over-claiming §1.5 sales pitch ("localizes error to a specific actor") is gone entirely; the qualification now lives in the identity itself ("— where the node closes").

**5. Funding pool — RESOLVED.**
The two-level design lands exactly as adjudicated: per-edge origination tags confined to **discrete, disclosed financing events**; the push-through question routed through the **(entity, period) pool** (sources in, including operating cash — the self-funding-hyperscaler case that was the sharp end of the finding — and uses out), with per-edge attribution derived via the ⚙ pro-rata convention registered in §12; the paying-itself headline queryable convention-free at the financing-edge level under a named cut. One vocabulary trim worth making while the file is open: "operating cash" appears in the per-edge tag list, but an operating-cash draw is never a discrete disclosed financing event — it lives only in the pool; leaving it in the edge-tag vocabulary invites a sourcer to re-derive per-purchase funding attributions by hand, the exact convention problem the pool closes. Trim, don't redesign.

**6. Inference lineage (`derived_from`) — RESOLVED.**
Required on every inference-class observation **at intake**, holding observation ids/capture refs; "list everything downstream of X" is answerable from the field from observation one; invalidation propagation explicitly staged as a v1.x delta-pass feature. This is the punch-list text applied without loss, and it satisfies the capture-asymmetry doctrine that made it capture-class: the expensive part (the links) is captured from day one, the cheap part (the propagation job) is deferred.

**7. Intake plurality — RESOLVED.**
Both halves of the starvation loop are broken. Supply side: a positive probe **must register a recurring sweep** attached to the delta pass (queue filings, permits, customs — public and recurring), and intake is named plural: news promotion + independent-source sweeps. Detection side: the **single-class flag** fires on *absence* (an edge ≥ ⚙ $5B/yr with only company-provenance observations), not on disagreement — so the structural never-arrives problem (a second observation that the disagreement check needs but the pipeline never delivers) can no longer keep an edge silently deferent; the flag routes to independent-measurement tasking, which is a consumer, not a verdict.

**8. Attempt log — RESOLVED.**
The discipline is applied verbatim and at full scope: any sourcing attempt, **in any tier**, ending unmeasured writes a dated note of what was tried, attached to the edge or node — so a Tier A unmeasured edge is no longer permanently ambiguous between "opaque" and "unattempted," which was the whole finding. One line-level defect in the file, not the discipline: §4 points at "§3's coverage table," and v3's §3 contains no coverage table (it was a v2 surface). Restore the table to §3 or repoint the reference — as written, the log's promised rendering surface is a dangling cross-reference.

---

## Line carries — applied?

- **§12 quote-F7-verbatim (R-11)** — ✅ applied; the floor row quotes F7's binding condition word-for-word.
- **Tolerance row (R-12)** — ✅ applied; registered in §12, written in (stage, basis, period)-cell terms.
- **Destination-category fixes (R-13)** — ✅ applied (purchase-only; `n/a — financing`; `intended_category` excluded from totals); micro-nit: revenue edges taking a label that *reads* "financing."
- **Burn-metric aims rewording (R-9/R-18)** — ✅ applied; §1.5 defers delivery to q2 per R-18, and the R-13 annotation is corrected.
- **Labor-cost instrumentation note (W-2)** — ❌ **NOT applied**; no "instrument the first delta passes" note anywhere in v3 (§5, §6, §12 all checked).

---

## Status table

| # | carry | status | tag |
| --- | --- | --- | --- |
| 1 | two named totals + capacity/service typing | **PARTIALLY RESOLVED** | SUBSTANTIVE |
| 2 | membership/instantiation → R-16 filters | RESOLVED | — |
| 3 | stage/basis axis | RESOLVED | — |
| 4 | conservation/closure | RESOLVED | — |
| 5 | funding pool | RESOLVED | — |
| 6 | `derived_from` lineage | RESOLVED | — |
| 7 | intake plurality + single-class flag | RESOLVED | — |
| 8 | attempt log | RESOLVED | — |
| — | bonus | none claimed — nothing unrelated rose above nit level in the targeted lanes | — |

**Count of new/persisting substantive carries: 1** (item 1's typing-clause residue; the W-2 miss and the §3 coverage-table dangling reference are LINE). Targeted-pass bar is ZERO.

> **Pass prediction: NO — fails adjudication by exactly one carry.** The residue is the round-1 failure mode recurring at one edge class via the remedy's own wording; it changes what a sourcer types on construction-contract edges, so it can't honestly be tagged LINE — but the fix is two sentences, and a v3.1 carrying them (plus the W-2 note and the coverage-table repoint) should clear without another seat round.

Status: round-2 targeted RED pass complete — one substantive residue identified, remedy specified; no ruling argued with; recommend v3.1 by amendment rather than a further full round.
