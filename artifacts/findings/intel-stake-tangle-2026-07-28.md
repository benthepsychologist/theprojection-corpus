---
finding: intel-stake-tangle
date: 2026-07-28
threads: [intel-rescue, chips-equity-pivot]
trigger: "ben-steer 2026-07-28 — crawl the three irreconcilable stake figures"
bundle: artifacts/bundles/intel-stake-tangle-2026-07-28/provenance.yaml
---

# The Intel-stake tangle — three figures, one position

**The question:** the US government's Intel stake carried three
irreconcilable public values in the same news week — "$36-42B",
"~$56.5B implied" (a $47.6B gain), and Trump's "$70B". Which is real?

**The answer:** one position, one fixed cost basis, three different
measurements — two of them defensible snapshots, one unsupported by any
price Intel traded at this year. And a fourth, filing-accurate number
that nobody in public uses.

## The fixed facts (all SEC-filing-verified)

- **The deal (8-K, 2025-08-22; closed 08-27):** 433,323,000 shares at a
  blended **$20.469** ≈ **$8.87B** — $5.695B Accelerated Direct Funding
  (274.583M sh) + $3.175B Secure Enclave escrow (158.740M sh) — billed
  as 9.9%. Consideration: converted CHIPS grants + Secure Enclave funds.
  [8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/50863/000005086325000129/a08222025form8-kex991.htm) ·
  [Ex-10.1](https://www.sec.gov/Archives/edgar/data/50863/000005086325000129/a08222025formex101stockand.htm)
- **The warrant:** 240,516,150 shares @ $20.00, 5-year, exercisable
  **only if Intel's foundry ownership falls below 51%** — Intel's Q2 FY26
  10-Q: "neither currently nor expected to become exercisable."
  [10-Q](https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm)
- **Actually issued as of 2026-06-27: 290.3M shares** (274.583M +
  15.74M released from escrow); 143M still escrowed, half of those
  genuinely contingent on further Secure Enclave disbursements. (10-Q)
- **Dilution:** shares outstanding 5,044M (10-Q cover, 2026-07-17) after
  the SoftBank ($2.0B @ $23, Aug 2025) and Nvidia ($5.0B @ $23.28,
  closed **Dec 2025**) raises — the headline stake is now **8.6%**, not
  9.9% (5.8% counting only issued shares).
- **Disclosure gap:** no SC 13D/13G exists for the position — 8-Ks and
  press releases only, unusual for a >5% holder. Pairs with Fortune's
  finding that the position appears in **no federal budget document**;
  Treasury says agencies report equity "in different ways."
- **The price path that scrambled everything:** INTC $105.45 (07-21) →
  $100.23 pre-print (07-23) → post-earnings after-hours pop past $112 →
  **reversed** to $92.32 (07-24) → $86.30 (07-28), ~30% off the Jul-6
  peak, on capex-guidance concern. Any figure quoted 07-20/22 vs
  07-24/28 rests on materially different prices.

## The reconciliation

| public figure | what it actually is | arithmetic | verdict |
|---|---|---|---|
| **$36B** (Bloomberg, 04-24) | stock-only, April price (~$83) | 433.3M × ~$83 | ✅ defensible snapshot, stale |
| **$42B** (Fortune, 07-26) | stock-only, July price (~$97) | 433.3M × ~$96.9 | ✅ the best reporting-grade current figure |
| **$47.6B gain / ~$56.5B** (Yahoo/Kobeissi, 05-08) | stock-only at the May price **peak** (~$129 intraday, Apple-deal day) | 433.3M × ~$129 − $8.87B | ✅ real but a local-maximum snapshot; analyst attribution, not government |
| **"$70B"** (Trump, CNBC 07-26) | explicitly a *gain* claim | stock-only would need ~$182/sh — never traded. Only route: 673.8M shares (warrant counted at full spot, strike ignored, non-exercisability ignored) × $97-105 (pre-selloff prices) ≈ $65-71B | ⛔ unsupported as stated; reachable only by double-counting the warrant at stale prices. His own April claim ("$30B in 90 days") tracked reality almost exactly — the July figure outruns the price path |
| **(unused by anyone)** | shares actually issued today | 290.3M × $86.30-91.67 = **$25-28B**; basis ≈ $6.0B; gain ≈ **$19-21B** | 🎯 the literally-accurate "what the government owns right now" |

*Note: stock+warrant-intrinsic at ~$90-92 also lands ≈$56.9B — a
coincidental arithmetic match to the May figure. The Yahoo piece's own
date and price peg (05-08, ~$129) is the anchored reading.*

## What it settles

The "tangle" wasn't fraud or confusion between outlets — it's **an
appreciating position quoted without as-of discipline** (three dates,
one methodology) plus **one claim that no price supports**. The
governance finding is sharper than the arithmetic one: a position worth
~$40B **has no official consolidated valuation anywhere** — no 13D, no
budget line, no Treasury number. The gain the administration cites in
interviews is not a figure any document defends.

## Open questions

- Escrow cadence: what triggers the remaining 143M shares' release, and
  will any filing mark it? (contingent, undated — watch the 10-Qs)
- Does any oversight body force consolidated reporting of the ~30-deal
  federal equity portfolio? (chips-equity-pivot's live question)
