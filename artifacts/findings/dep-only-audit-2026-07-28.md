# Finding — dep-only thrust audit (rollout wave H)

**Thread:** dep-only-audit · **Crawled:** 2026-07-28

The pilot's `axes_num.thrust` figures were built with a blended **capex −
D&A** netting term. Per [`content/metric/thrust.md`](../../../theprojection/content/metric/thrust.md)
("Depreciation, never amortization"), the netting term should be
**depreciation only** — amortization of acquisition intangibles must never
be subtracted, since it measures a past deal's goodwill writedown, not
machine wear. Broadcom was already corrected this way (capex $0.9B −
depreciation-only ≈ $0.9B → thrust ≈ $0, up from the absurd −$8B that
resulted from netting VMware amortization). This audit checks the rest of
the 21-actor pilot using the same rule.

**Method:** five parallel WebFetch sweeps against SEC EDGAR 10-K/10-Q
filings (primary source; company CIKs looked up directly) for the actors
with the largest acquisition-amortization books — the ones most likely to
have blended amortization into their "D&A" netting term. The remaining
corporates were checked against the M&A profile already on record in
`board.yaml`/prior bundles rather than re-fetched, since none carry a
large-intangible-amortization acquisition; funds/labs were skipped per
brief (non-capex recipes structurally can't have this pollution). No
figure was fabricated; where a filing genuinely doesn't split the two, the
finding says so explicitly (Qualcomm).

---

## Priority suspects — WebFetch-verified against primary filings

### Oracle — CORRECTION, thrust $46B → **$48B/yr** (small, upward)

FY26 10-K (fiscal year ended 2026-05-31, filed 2026-06-22, CIK 0001341439).
Oracle discloses amortization of intangible assets as its **own
income-statement line**, separate from depreciation — both also appear
distinctly on the face of the cash-flow statement.

| line | FY26 value | source |
|---|---|---|
| Depreciation (cash flow) | **$7,623M** | [R8.htm](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/R8.htm) |
| Amortization of intangible assets | $1,671M | [R4.htm](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/R4.htm) |
| D+A combined (≈ what the board's "$9B" is) | $9,294M | derived |
| Capex | $55,663M | [R8.htm](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/R8.htm) |

The board's "$9B" is the **blended D+A total** ($9.294B), not
depreciation-only as labeled. Corrected: capex $55.663B − depreciation
$7.623B = **$48.04B/yr**. Direction is upward, not downward — because
amortization ($1.7B) is the *smaller* of the two components here, removing
it from the subtraction means subtracting less overall, raising thrust.
The Cerner/NetSuite intangible-amortization hypothesis in the brief
doesn't overturn this: even if all $1.671B is acquisition-related, it's a
minority share of the $9.3B blend. No Cerner-specific breakout is
disclosed (only an aggregate future-amortization schedule,
[R53.htm](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/R53.htm)),
but the aggregate is all the correction needs.

Confidence: **high** (primary 10-K, both lines confirmed on two statement
faces).

---

### Microsoft — CORRECTION, thrust $57B → **~$71B/yr** (large, upward)

FY2025 10-K + Q3 FY2026 10-Q (period ended 2026-03-31, CIK 0000789019).
Microsoft separately discloses **depreciation (PP&E + finance leases)**
and **amortization of acquired intangibles** in dedicated notes, but its
cash-flow statement line is "**Depreciation, amortization, and other**" —
a *three-part* blend, not just D&A; "other" is a further ~$6B/yr of
non-cash items that also aren't depreciation.

| line | TTM (to 2026-03-31) | source |
|---|---|---|
| Depreciation (PP&E + finance leases) | **≈$30.3B** | [FY25 10-K R61.htm](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/R61.htm) + [Q3 FY26 10-Q R56.htm](https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/R56.htm) |
| Amortization of acquired intangibles | ≈$5.2B | [FY25 10-K R70.htm](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/R70.htm) + [Q3 FY26 10-Q R59.htm](https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/R59.htm) |
| Cash-flow "Depreciation, amortization, and other" (≈ what the board's "$44B" is) | ≈$41.5B | derived from the same filings |

No Activision-specific breakout is disclosed (Microsoft only reports
category totals — technology-based, marketing-related, customer-related,
contract-based — not by deal), but technology-based net intangibles fell
$7.6B (2025-06-30) → $5.3B (2026-03-31), consistent with continued
Activision game-IP/tech amortization running through the blend.

Corrected: capex $97B − depreciation $30.3B + M&A add-back (board's
implied ~$4B: $57B = $97B − $44B + $4B) = **≈$70.7B/yr**, vs. the board's
$57B. This is the largest correction found — the board figure understated
thrust by roughly $14B because the "D&A" label was actually netting a
broader three-part non-cash blend, not depreciation alone.

Confidence: **high** for the depreciation/amortization figures (primary
10-K/10-Q); **medium** on the exact M&A add-back component, since it's
back-derived from the board's own prior arithmetic rather than re-verified
this session.

---

### Amazon — NO CHANGE, thrust stays **$81B/yr**

FY2025 10-K + Q1 2026 10-Q (CIK 0001018724). Amazon's cash-flow D&A line
is scoped, by its own wording, to **"Depreciation and amortization of
property and equipment and capitalized content costs, operating lease
assets, and other"** — it already excludes acquired-intangible
amortization by construction, not by luck.

| line | value | source |
|---|---|---|
| Cash-flow D&A line (FY2025) | $65,756M | [10-K R3.htm](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/R3.htm) |
| Cash-flow D&A line (Q1 2026, quarterly) | $18,945M | [10-Q R2.htm](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/R2.htm) |
| Amortization of acquired intangibles (separately disclosed) | $817M (FY2025) | [10-K R64.htm](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/R64.htm) |

The board's $70B figure is a reasonable TTM read of the same (already
depreciation-scoped) line. Even if the $817M of acquired-intangible
amortization had been folded in by mistake somewhere, it's ~1.2% of the
$65.8B line — not material. **No correction needed.**

Confidence: **high**.

---

### Google (Alphabet) — NO CHANGE to thrust, but one figure needs fixing

10-K (FY2025) + Q2 2026 10-Q (period ended 2026-06-30, CIK 0001652044).
Alphabet doesn't split D&A on the face of the cash-flow statement, but
does disclose amortization of intangible assets separately in the
goodwill/intangibles note.

| line | TTM (to 2026-06-30) | source |
|---|---|---|
| Depreciation of PP&E (cash flow) | **$25.2B** ($21,136M FY25 − $9,485M H1-25 + $13,586M H1-26) | [Q2 26 10-Q R9.htm](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/R9.htm) + [FY25 10-K R10.htm](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R10.htm) |
| Amortization of intangible assets | ≈$0.8B TTM, rising toward ≈$1.4–1.5B/yr forward run-rate as Wiz layers in | [Q2 26 10-Q R74.htm](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/R74.htm) |

The board's "$25B" already matches pure TTM depreciation almost exactly
($25.2B) — amortization is a small, separate add-on that was **not**
blended into the board's figure. Whether by design or luck, no dep-only
correction is needed here.

**Separate data-quality flag (not a dep-only issue, worth fixing
anyway):** the board's Wiz add-back is stated as $32B; the actual
purchase-price consideration per the FY26 Q2 10-Q purchase-price-allocation
note is **$29.5B**
([R71.htm](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/R71.htm)),
with $8.3B of acquired intangibles (patents/tech $3.6B/7yr, customer
relationships $4.5B/10yr, trade names $0.2B/7yr) and ~$25B goodwill. Wiz
closed 2026-03-11. Using the corrected $29.5B figure: capex $132B −
depreciation $25.2B + Wiz $29.5B ≈ **$136.3B**, vs. the board's stated
$142B — a ~$6B gap driven by the Wiz-figure correction, not by
amortization pollution. Flagging for Ben; not applying it here since it's
outside this audit's specific mandate (dep-only rule, not general figure
accuracy).

Confidence: **high** on the depreciation/amortization split; **high** on
the corrected Wiz figure (primary purchase-price-allocation note).

---

### Qualcomm — split UNAVAILABLE; no dep-only correction; other flags

Q2 FY2026 10-Q (period ended 2026-03-29, filed 2026-04-29, CIK
0000804328). Checked the cash-flow statement and Note 2 ("Composition of
Certain Financial Statement Items") — **Qualcomm does not disclose a
depreciation-only figure separate from amortization anywhere in this
filing.** Combined D&A for the six months ended 2026-03-29 was $806M
(down slightly YoY from $833M) against capex of $1,082M (more than double
the prior-year period).
([10-Q primary document](https://www.sec.gov/Archives/edgar/data/804328/000080432826000061/qcom-20260329.htm))

Alphawave's acquired intangibles are disclosed in Note 8 (Acquisitions):
$239M subject to amortization, 5-year weighted-average life → ≈$48M/yr —
immaterial (2–6% of total D&A), so even if a split were derivable, it
wouldn't move the needle much.

**Per the audit brief's own instruction — genuinely unavailable, reported
as such rather than guessed.** No dep-only correction applied; thrust
stays at the board's $2.6B pending future disclosure.

**Other data-quality flags surfaced incidentally (not dep-only issues):**
- Alphawave closed 2025-12-18 for **$2.3B total** (mostly stock — $1.8B /
  11M shares — plus $301M cash), not "$2.4B cash" as the board's gloss
  implies.
- Modular ($3.9B, announced 2026-06-24) is **not closed** — expected H2
  2026, subject to regulatory approval. It should not be counted as
  deployed thrust yet; the board's $2.6B figure appears to already exclude
  it (consistent with Alphawave's $2.3B alone), so no value correction
  follows from this, but the "Alphawave/Modular" phrasing in the gloss
  reads as if both are counted, which is misleading and worth a wording
  fix independent of this audit.

Confidence: split **unavailable**; Alphawave price/structure and Modular
status **high** (primary sources).

---

## Remaining pilot actors — checked against existing record, not re-fetched

None of these carry a large-intangible-amortization acquisition on record,
so none were flagged as priority suspects in the brief. Checked against
`board.yaml`'s existing stated recipe and gloss; no new WebFetch performed
this session (out of the audit's stated scope). **No change** for all:

| actor | current thrust | why no change (basis already on board) |
|---|---|---|
| meta-ai | $74B/yr | recipe already separates organic capex−D&A ($55B) from the Scale AI *stake* ($14B, correctly a stake not an M&A-intangible book); Meta's legacy acquisitions (Instagram/WhatsApp) are old enough that amortization is immaterial. Not re-fetched — low priority, flag for a future pass if Ben wants primary confirmation. |
| tsmc | $18B/yr | organic fab capex−dep, no material M&A book. |
| intel | $0.1B/yr | capex ≈ D&A already prints ≈$0; Altera/Mobileye legacy intangibles could shift this slightly if the split were pulled, but the base is already near-zero either way — flag for future pass, not urgent. |
| apple | $0.1B/yr | no meaningful M&A book; capex ≈ D&A. |
| nvidia | $30B/yr | dominated by ecosystem *stakes* ($27B of $30B); organic capex−D&A component ($3.3B) is too small for amortization pollution to matter even if present. |
| arm | $0.3B/yr | capital-light licensor, no capex−D&A recipe in play. |
| coreweave | $13B/yr | young company, no acquisition-amortization book; capex $17B − D&A $3B. |
| cxmt | $4B/yr | state-funded fab buildout estimate, no M&A. |
| asml | $2B/yr | board's own recipe already labels the netting term "dep" (not D&A) — €1.4B capex − €1.0B depreciation — already compliant with the rule as stated. |
| samsung | n/a | owned by wave C, out of this audit's scope. |

**Funds/labs — skipped per brief** (structurally can't have this
pollution; recipe is net-new-deployment or commitment run-rate, not
capex−D&A): blackrock, vanguard, state-street, fidelity, china-life,
openai, anthropic.

---

## Notes

- No commits made, no `board.yaml` edits — this is a findings-only pass
  per the brief. Whoever applies these should also update `axes_asof` /
  add an `agent-derive` provenance comment on each changed line, per the
  repo's existing convention.
- Two corrections (Oracle, Microsoft) both moved thrust **up**, not down —
  worth noting since "removing amortization" is intuitively expected to
  lower thrust (undoing an artificial *negative* like Broadcom's). It only
  lowers thrust when amortization is the *larger* share of a blended
  figure; when depreciation is larger (both cases here), stripping out the
  smaller amortization component means subtracting less overall, so
  thrust rises. Broadcom was the outlier case where amortization
  dominated.
