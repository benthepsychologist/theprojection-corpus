<!-- q2 color-team · round 2 · targeted verification (RED) · 2026-08-03
     model: Claude (Fable-tier subagent, fresh context)
     inputs: q1 v3 (foundation) + q2 v3 (artifact) + q1... q2 round-1-white.md
     prompt: dispatched per the targeted re-review protocol; bar = ZERO new/persisting substantive carries
     memo below is the seat's return, verbatim and unedited. -->

# RED memo — q2 skeleton v3 · round-2 targeted verification

**Seat:** RED (targeted pass; fresh context — q1 v3 foundation, q2 v3 artifact, round-1 WHITE adjudication only)
**Under review:** `/workspace/theprojection-data/INBOX/2026-08-03-q2-skeleton-v3.md`
**Checklist:** WHITE §4(d) punch list, itemized as carries (1)–(11) + W-1 + line batch
**Binding:** q1 v3 §2 rulings register (R-01–R-18). Nothing below argues with a ruling; carry (1) verifies the *application* of R-16/R-17, as instructed.
**Date:** 2026-08-03

> **Verdict: 11 of 12 substantive carries RESOLVED; one NEW PROBLEM IN THE REMEDY (the revenue ladder's stage vocabulary) — v3 misses the zero bar by exactly one, and the fix is a stated mapping, writable today.**

---

## 1. Substantive carries, verified one by one

**(1) The boundary predicate → named cuts + reseller collection + named ambiguity (R-17 applied).**
**RESOLVED.** The original failure was the burn metric and §7 hypothesis being a family of numbers indexed by an unstated classification. v3 closes that in the ruling's own shape: the map stays classification-free; two named ⚙ revenue-side cuts ship (`cut:cloud-frontier` computable now; `cut:retail-inference` computable-where-decomposed, with the non-decomposition stated on the surface's face — R-17's "name the ambiguity" applied literally); reseller-level flow collection is a Tier A item (§8), so the cut has data to operate on; buyer classification is a claim with observations/reliability, the resale-vs-embeds gray zone is flagged rather than legislated, and cut-stamped totals inherit the flag (§3); the §7 hypothesis names its cut inline, making it single-valued per cut; §2 declares the burn metric cut-stamped under q1's stamp rules; decision (h) records the F9 rejection so the rejected rule cannot silently return. The index variable is now an explicit, versioned stamp — the failure mode cannot recur unnoticed. One non-carry observation: q2 never states which cut the burn *headline* defaults to, nor says outright that numerator and denominator run under one cut; the stamp discipline covers it mechanically, but one sentence at metric-delivery time would foreclose a mixed-cut rendering.

**(2) `commitment_ref` joining flows to commitments.**
**RESOLVED.** The field is on the q1 edge schema from day one (q1 §3), nullable, with the design rationale ("no flow needs re-attribution later") stated; F4 explicitly computes deployed rate from stage-marked observations *joined via `commitment_ref`*; q2 §5 makes `amortized_to_date` derived-only — the sum of flows carrying the ref — with a single source of truth. The R-2 proof case (multiple concurrent OpenAI–Microsoft money relationships defeating pair+period attribution) is handled: each flow points at its commitment individually.

**(3) `serves_ref` / `part_of_ref` / `side` on commitments.**
**RESOLVED.** All three are in the §5 object with correct semantics (pass-through chains; frame⊃constituent containment; supply-build vs demand-capacity). WHITE 2.2's correction is incorporated, not just accommodated: aggregate (a) dedupes via `part_of_ref` with the external-side containment argument (government frame + per-agency commitments) written into §6 verbatim. The seed table exercises the relations (Stargate as supply-build frame; Oracle attaching via `part_of_ref` on evidence). Cross-side containment (demand-capacity constituent under a supply-build frame) does not double-count in side-filtered aggregate (c) because the frame is excluded by the side filter — coherent.

**(4) The hypothesis restated in gradeable units.**
**PARTIALLY RESOLVED — LINE.** The axes round 1 attacked are fixed: both windows pinned (next-12-mo LHS, trailing-12-mo RHS), cut named in the statement itself, dedup relations named, burn-metric window pinned alongside per WHITE 2.3, and aggregate (c) sanctioned with method-on-face so the internal-vs-published dodge is gone. Residual: the LHS — "committed face amortizing into the next 12 months (per F4 mechanics)" — is not single-valued for **unscheduled** commitments. F4 bans face values from flow totals and computes from stage-marked observations; read strictly, Stargate ("up to $500B/4yr, unscheduled") contributes **zero** forward amortization until schedule evidence lands; read loosely ("committed face amortizing"), a grader pro-rates face over the span — a swing of up to ~$125B/yr on that one row. That is the R-4 family-of-numbers shape at one remove, though far narrower. The phrase "committed face amortizing" also collides with F4's own "face values never enter flow totals." **Remedy:** one ⚙ line pinning the forward-amortization convention for unscheduled commitments (zero-until-scheduled or pro-rata-over-remaining-span — pick one, stamp it), and reword the LHS to "commitment drawdown amortizing per F4." Tag LINE: no capture change and no new sourcer ask — records already hold span + schedule-if-known + typed faces.

**(5) The recognized-or-derived amendment.**
**RESOLVED.** Decision (d) as amended is in §4 with every element of the WHITE 2.4 synthesis: derived recognized-revenue estimates (annualization unwound, haircut applied, method noted, provenance `inference from other claims`, low reliability) wherever a seller discloses no recognized figure; the mechanism framing preserved ("gates raw claims by measurand; never ranks sources by type"); solid+hatched split on headlines. §7's RHS reads "recognized-or-derived," so the one-sided emptiness that was biasing the grade is structurally gone.

**(6) The stage carrier + corrected stage-1 placement.**
**NEW PROBLEM IN THE REMEDY — SUBSTANTIVE.** The placement half is exact: stage-2 → commitment, stage-3/4 → revenue edges joined by `commitment_ref`, and stage-1 homed on the seller's aggregated revenue edge to `ext/*` (unallocated) — no counterparty, no contract, stage-marked, excluded from period totals, eligible to spawn derived estimates — WHITE 2.5 verbatim. But the carrier doesn't fit the load: q2 §4 asserts the ladder (claimed run-rate → booked → recognized → collected) is "carried by the observation's `stage` field (q1 v3 §4)" and thereby machine-enforceable, while q1's stage enum is **guidance | commitment | contract | delivered** — a spend-side vocabulary. **Recognized and collected have no distinct legal value**; the plausible encoding (stage=`delivered` × basis=`accrual` vs `cash`) appears in neither file; "commitment" has no ladder meaning and "booked" has no enum value. Consequences: the machine-enforceability claim is unfounded as written; the cross-stage consistency flag (delivered ≤ contracted ≤ committed) has no runnable revenue analogue (collected ≤ recognized ≤ booked); and a sourcer recording any revenue observation must improvise the field value — R-6's original failure mode (a rule whose vocabulary doesn't cover the record in front of the sourcer), reintroduced one level down: vocabulary instead of placement. **Remedy:** state the mapping in the artifact — claimed-run-rate→`guidance` · booked→`contract` · recognized→`delivered`+accrual basis · collected→`delivered`+cash basis — or extend q1 §4's enum with the revenue rungs; and write the revenue-side cross-stage inequality next to the spend-side one. Tag SUBSTANTIVE: it determines the value written on every revenue observation.

**(7) The government sweep respec.**
**RESOLVED.** All five elements are in §3 as spec, not aspiration: task-order-level actions and outlays with IDIQ ceilings excluded *and correctly stage-classified* (guidance/commitment — a nice coherence bonus, though note it leans on the same spend-side enum flagged in (6)); `contract_vehicle` captured per record; the vehicle→OEM unwinding map (Carahsoft, CSP consumption vehicles) as a named Tier A deliverable, repeated in §8; nominal-price awards as adoption-evidence-never-revenue; and Green's calibration-set role written into the seam's stated purpose with the grading-before-weight ordering intact.

**(8) The `ext/*` node class.**
**RESOLVED.** Sanctioned in §3 (`ext/consumer` · `ext/enterprise-<sector>` · `ext/gov-<jurisdiction>`), explicitly mirroring F6 — inbound allocation to a population node is a claim with observations and reliability — giving survey observations a legal endpoint. The class is load-bearing elsewhere and consistently used: stage-1 placement (§4) and the aggregated-revenue-edge home both depend on it, and q2 §2 correctly lists it among the additive schema items per the amended R-13 annotation.

**(9) Worth-bearing fields as dated observation sequences.**
**RESOLVED.** §5 states it as a rule ("a commitment's term history is a sequence, never a mutable scalar"), puts structure, clauses, and linkage states under the one evidence model as dated, sourced, superseding observations, and demonstrates it against the canonical case — face reiterated at $250B while exclusivity and refusal rights transformed — now representable as "a worth event at constant face," which is precisely the record R-9 showed the old shape recorded as "nothing happened."

**(10) Three-way register split + backlog reconciliation.**
**RESOLVED.** The split is exact and exercised by the seeds: commitment entries with parties/side/face; node-level backlog observations quarantined ("never register rows, never summed" — CoreWeave, AWS $496B, AWS $364B); financing components routed to q1 financing edges surfacing only as `funding_linkage`, with the R-10/2.7 proof case (OpenAI→Amazon $50B investment leg vs $100B/8yr capacity) split correctly. Backlog reconciliation lands as specified: per node, Σ active register faces vs disclosed backlog, gap read as unregistered committed inbound, a first-class cut-stamped coverage surface.

**(11) The revenue-space overlay respec.**
**RESOLVED.** §4 defines the overlay's output as a revenue share = utilization mix × price mix; an overlay lacking the price term is demoted to a labelled *capacity share* and banned from multiplying into dollars; the Tier B probe grades the method's reliability ceiling before any output is used (§8), and the government calibration set (§3) is what it grades against — the R-11 measurand fix plus the WHITE 2.6 linkage, both present.

**(W-1) Typed observation values with point/bound/scope semantics.**
**RESOLVED.** The enum landed in q1 v3 §4 (point · upper-bound · lower-bound · scope-qualified, scope stated, bounds as constraints never averageable, credited to this round's W-1), and q2 *uses* it where the finding demanded: the $364B excluding-Anthropic figure is explicitly recorded as a scope-qualified value (§5, item 2), commitment `face` is declared a typed value, and §2 names the bound semantics among the foundation fields it consumes.

---

## 2. Line batch

- **Capacity destination category** — ✅ landed: q1 §12 lists "purchased compute capacity (services)," coherent with the buyer-side typing rule (capacity payments are never build).
- **Per-field prediction split** — ✅ landed: §7's table predicts face (high) / structure (low) / termination clauses (low) separately, plus the seam rows.
- **Paying-conversion chase** — ✅ landed in §4 as a named chase (paying-subscriber counts + conversion rate, each a sourced claim); one nit: WHITE homed it in Tier A and §8's Tier A list omits it (Tier B's app-store/subscriber path is adjacent) — one-line tier placement fix.

---

## 3. Bonus finding (the one allowed) — LINE

**Bound-typed faces do not propagate through the sanctioned aggregates.** W-1's semantics land at observation level and `face` is a typed value — but §6's aggregates **sum** faces, and the seed table already contains both an upper-bound face (Stargate "up to $500B") and a lower-bound face (Oracle ">$300B/5yr"). A sum containing bound-typed terms is itself an interval, not a point, and no §6 rule says so; "rendered with its dedup method and cut on its face" covers dedup and cut but not bound propagation. Remedy is one rendering rule: aggregates over typed values propagate bound-type (render as a range, or state the point-convention used). LINE — capture is unchanged; this is computation/rendering discipline.

---

## 4. Status table

| # | carry | status | tag |
| --- | --- | --- | --- |
| 1 | boundary → cuts/collection/ambiguity (R-17) | RESOLVED | — |
| 2 | `commitment_ref` join | RESOLVED | — |
| 3 | `serves_ref`/`part_of_ref`/`side` | RESOLVED | — |
| 4 | gradeable hypothesis | PARTIALLY RESOLVED | LINE |
| 5 | recognized-or-derived | RESOLVED | — |
| 6 | stage carrier + stage-1 home | NEW PROBLEM IN THE REMEDY | **SUBSTANTIVE** |
| 7 | government sweep respec | RESOLVED | — |
| 8 | `ext/*` node class | RESOLVED | — |
| 9 | worth-bearing sequences | RESOLVED | — |
| 10 | register split + reconciliation | RESOLVED | — |
| 11 | revenue-space overlay | RESOLVED | — |
| W-1 | typed values, used in q2 | RESOLVED | — |
| bonus | bound propagation in aggregates | NEW (bonus) | LINE |

---

## 5. Count and prediction

**New/persisting substantive carries: 1** (carry 6 — the ladder-to-enum vocabulary gap). Pass bar is zero → **this pass is not met**, by exactly one. Line-class residue: carry 4's amortization convention, the bonus bound-propagation rule, the Tier A placement nit — none blocking under the bar's own definition.

> **Prediction: fails by one, fixable in one stated mapping plus two ⚙ lines with no re-sourcing implications — a same-day recheck after the §4 vocabulary amendment lands should pass clean, and the file routes with q1 immediately after.**
