---
lens: global-capital
week_of: 2026-07-27
status: final
coverage: done
---

# Global Capital — week of 2026-07-27

*Synthesized from 7 dailies (Mon–Sun — the first full week since the lens
renamed from "money") + a fresh 7-day sweep. This was the heaviest
global-capital week on record: a full board-model rewrite, six capex-tree
crawls, a seven-event Wednesday earnings gauntlet, a hedge-fund blowup, and
a two-week-old gap in Fed coverage that closed on the record.*

## The week's throughline

The vendor-financing structure that defined last week — Nvidia guaranteeing
$250B of OpenAI's debt, AMD backing Anthropic, Meta/BlackRock's off-balance-
sheet joint venture — met its first real credit-market skepticism this
week, and then met a second, harder test. Nvidia's five-year CDS widened a
record 82bp in a single day (07-27, the largest move since the contract
began trading) as "circular financing" became the dominant frame across
Axios, Breakingviews and short-seller Jim Chanos; it eased to 78bp by 07-29
as Oracle overtook Nvidia as the widest-trading hyperscaler credit, meaning
the worry migrated from the lender to the largest lessee rather than
resolving. Then, on 07-30, the trade broke an actual fund: Leopold
Aschenbrenner's Situational Awareness — up ~439% through June on ~4x-
leveraged AI-infrastructure bets — lost about 67% in July, drew margin
calls from Goldman, JPMorgan and Bank of America, and was forced to sell
its entire public-equity book to Citadel at distressed prices from a ~$45B
peak NAV. It is the first AI-thesis fund broken by the AI trade itself, and
this map had nothing on it the day it happened. Underneath that, a seven-
event Wednesday earnings gauntlet (Meta, Microsoft, Arm, Qualcomm and SK
Hynix reporting 07-29, Samsung and Amazon following 07-30) drew a different
line than expected: not hyperscaler-vs-chipmaker but monetization-proven
vs. monetization-unproven. Microsoft (+8-9% after-hours on 43% Azure
growth), Amazon (AWS +37%, fastest in 18 quarters) and Samsung (record chip
profit) were rewarded; Meta fell -8.5% premarket on an EPS miss and near-
zero free cash flow, and Arm and Qualcomm fell just as hard despite beating
and raising, because their numbers didn't show revenue conversion the way
the hyperscalers' did. All of that landed against a semiconductor complex
having its worst month since December 2002 (SOXX -22.1% in July, against a
essentially-flat Nvidia) even as the same four hyperscalers guided a
combined $720-745B of 2026 capex — demand guidance and chip equities
pointing in opposite directions, unresolved at week's end. And running
underneath the whole week was a structural gap this map closed only on
08-02: it had covered the Fed's 07-29 hold — the 9-3 vote, all three
dissenters named — in exhaustive detail for two straight weeks without ever
naming the sitting chair. He is Kevin Warsh, confirmed 54-45 on 05-13 (the
narrowest confirmation in the office's history) and in the seat since
05-22, a hawk who opposed the Fed's own quantitative easing from inside the
building in 2008-2011. The vote counts this map recorded were accurate the
whole time; the thing they were a fact about was missing.

Structurally, the board also took its biggest step yet this week: a
four-axis measurement model (commanded_capital / thrust / gravity /
optionality, each grounded in an established formalization — Damodaran
reinvestment rates for thrust, G-SIB substitutability for gravity) went
live 07-27, and by week's end 53 orgs carried full numeric values across
labs, chipmakers, memory names, capital pools, insurers and — new this
week — seven US health payers and a full government/agency layer (12
agencies, Canada as a state node). The board grew from 77 to 92 organizations
this week; the thread map grew from 43 to roughly 63.

## By radar question

### Q7 — Where is capital and economic power concentrating — in my markets and above them?

**What moved, in order.** The vendor-financing structure that was last
week's finding (Nvidia's $250B guarantee, AMD-Anthropic, the Apollo/
Broadcom SPV) got its first credit-market pushback this week, in two
stages. First, Nvidia's own CDS: record 82bp widening 07-27, easing to 78bp
by 07-29 as **Oracle overtook Nvidia as the widest-trading hyperscaler
credit** — a genuine structural shift (the circular-financing worry moving
from the vendor doing the guaranteeing to the largest customer leasing the
capacity) that this map flagged as a thread candidate twice (07-29, 07-30)
and left unanswered both times; it stands as a standing signal rather than
a tracked thread. Second, and harder: **Situational Awareness's forced
liquidation to Citadel (07-30)** is the first instance of the AI trade
breaking a fund built to bet on it, not just repricing one. A third
structure joined the vendor-guarantee pattern this week — **Google
guaranteed a $15B bank loan for Anthropic's Texas campus (07-30)**, the
same off-balance-sheet logic Meta/BlackRock and Nvidia/OpenAI used days
earlier, making three hyperscaler-guarantees-third-party-debt deals inside
one week. **Deal-level debt demand — the leading indicator the 07-20
digest asked to start tracking — supplied two real numbers this week**:
CoreWeave's $2.6B Anthropic-tied loan repriced to 5.5 percentage points
over benchmark, pricing at 96-97 cents on the dollar amid investor caution
over its debt load, and the Oracle CDS move above. Then the earnings
gauntlet drew the week's actual concentration line: capital keeps
rewarding *demonstrated* monetization (Microsoft's Azure, Amazon's AWS,
Samsung's chip margins) over guided or promised monetization (Meta's raised
capex without matching cash flow; Arm's and Qualcomm's beat-and-raise
quarters that fell anyway). And the week's structural correction was the
Fed-chair discovery itself: power was concentrated in a specific person
this whole time — a hawk confirmed by one vote's margin, running a
committee that went from a unanimous 12-0 hold in June to 9-3 with three
dissents *for a hike* in six weeks — and this map priced his committee's
votes without ever naming him.

**Working-note candidate, updated:** the 07-27 note (capital concentrating
at sovereign scale into a few names, funding the bottleneck not the models,
macro risk framed as ">$800B circular financing loops") is **superseded by
something more specific**, not dead. The mechanism this week clarified is
not a generic financing loop — it's hyperscalers extending off-balance-
sheet credit *guarantees* to third-party developers (three instances in
seven days: Meta/BlackRock, Nvidia/OpenAI, Google/Anthropic), which lowers
the guaranteed party's borrowing cost without the guarantor issuing debt or
carrying the asset — cheaper capital for the buildout, but contingent
credit risk that stays largely undisclosed until something breaks, which is
exactly what happened one lever down the chain when Situational Awareness's
leveraged bet snapped. Track the guarantee count and the CDS/loan-spread
level, not survey sentiment.

### Q2 — Where is the money going?

**The 07-27 working note (capital concentrating into a few names at
sovereign scale, funding compute/energy/memory bottlenecks not models) is
now largely confirmed, not superseded** — but this week filled in the
destination layer with real structure instead of a general claim. The W1-W6
capex-tree crawls (TSMC, Arm, Intel, CoreWeave, the memory trio, and the
hyperscaler capex synthesis) resolved the "what are they doing with the
capex" question that had been genuinely untracked: power is being solved
three separate ways (nuclear restarts on a 2027→2039 horizon, Meta exiting
its RE100 clean-power pledge for a 7.5GW gas pivot, and a second former DOE
Cold War nuclear site — Paducah, KY, this time, after Portsmouth/Piketon,
OH — becoming a $100B AI power build with NextEra and Brookfield); capex is
migrating off balance sheets via the same guarantee/JV/bond structures Q7
tracks; and the own-silicon-vs-Nvidia split is undisclosed at all four
major hyperscalers even as the labs themselves leak it (Anthropic alone is
on both 1M TPUs and 1M Trainium chips). The clearest concrete link this
week: **Amazon quietly raised its FY2026 capex guidance to ~$220B from
~$200B on the 07-30 earnings call, explicitly citing higher memory
costs** — the first hard evidence that the memory-price shock
(`ai-memory-shortage`) is now large enough to move a hyperscaler's own
capex line, not just its cost line. Four hyperscalers now guide a combined
$720-745B for 2026.

## Threads

**Moved:** `nvidia-vendor-financing` / `ai-circular-financing-risk` (CDS
record 82bp → 78bp, Oracle overtakes Nvidia, Google/Anthropic guarantee
adds a third instance) · `ai-trade-bear-turn` (Korea's double circuit-
breaker, the Fed hold, SOXX -22.1% July) · `chip-hyperscaler-rotation`
(split from `chips-equity-pivot` 07-29; carries the full monetization-line
verdict across all seven earnings) · `red-sea-oil-shock` (five-month
Hormuz-closure correction, IRGC tanker strikes, Treasury insurance-
extortion sanctions; conflict-narrative content split out to the new
world-news thread `iran-conflict-widening`) · `softbank-all-in` (Tokyo
limit-up rally, Q1 earnings date corrected 07-30→08-06) · `cxmt-memory-ipo`
(Alibaba's pre-IPO stake up ~20x to ~$20.9B) · `hyperscaler-capex-big-
picture` / `aws-capex` (Amazon's $220B capex raise) · `frontier-lab-ipos`
(SpaceX's SPCX round-trip to -49% from its ATH and -20% below issue;
Anthropic IPO chatter firming toward $1T, and the two-month recall gap on
its S-1 filing corrected) · `custom-asic-tolls` (Broadcom-Samsung ~$200B
MOU re-dated; MediaTek's $5B AI-ASIC budget) · `asset-managers-build-ai`
and `genesis-mission` (both extended with timeline detail).

**Resolved this week:** none formally closed; `openai-custom-silicon`
retired and folded into `inhouse-silicon` on 07-27 (ben-steer, capex-tree
crawl made the two threads redundant).

## ⏳ Expectations scorecard

| id | outcome |
| --- | --- |
| `cxmt-star-listing` | ✅ **hit** 07-27 — STAR debut +466-472%, mainland China's most valuable listed company on day one |
| `fomc-july-decision` | ✅ **hit** 07-29 — held 3.50-3.75% on a 9-3 vote, three dissents *for a hike* (Hammack, Kashkari, Logan) after a unanimous 12-0 in June |
| `meta-q2-earnings` | ✅ **hit** 07-29 — beat revenue, missed EPS ~14-15%, FCF near zero ($784M), capex raised to $130-145B; -8.5% premarket |
| `microsoft-q2-earnings` | ✅ **hit** 07-29 — beat across the board, Azure +43% cc; churned twice mid-week (07-29→07-30 via a wrong tier-2 correction, then reverted) before a primary-source check settled it back at 07-29 — only Microsoft's own IR page actually resolved it, not the ledger and not recollection |
| `arm-q1fy27-earnings` | ✅ **hit** 07-29 — beat-and-raise, AGI-CPU bookings doubled to $2B+; fell -4.95% anyway on a smartphone-royalty guidance cut |
| `qualcomm-q3fy26-earnings` | ✅ **hit** 07-29 — guide missed on legacy handset weakness, not Dragonfly (starts December); FY2029 non-handset target raised to $40B |
| `sk-hynix-q2-earnings` | ✅ **hit** 07-29 — record op profit (+557% YoY) but missed consensus; round-tripped intraday in Seoul |
| `amazon-q2-earnings` | ✅ **hit** 07-30 — AWS +37% YoY (fastest in 18 quarters), net sales +20%; capex raise to $220B surfaced two days later on 08-01 |
| `samsung-q2-breakdown` | ✅ **hit** 07-30 — record chip profit (~70% DS margin, first time above 70%), first-ever mobile-division operating loss; faded despite the beat |
| `gdp-pce-2026-07-30` | ✅ **hit** 07-30 — Q2 GDP +1.5% annualized, June PCE 3.7%/3.3% headline/core, both at consensus — a stagflation-adjacent print |
| `eu-ai-act-code-of-practice` | ✅ **hit** 08-02 — cross-lens with frontier-ai, full detail there |
| `anthropic-ipo-filing` | ✅ **hit** 08-02, and the claim itself was **rewritten**: logged 07-27 as thin/rumored, but Anthropic's own newsroom announced the confidential S-1 on 2026-06-01 — this map picked up well-covered eight-week-old news and filed it as fresh |

Zero slips, zero passed-silent — a clean 16-for-16 resolution week across
the whole map, of which the twelve above are global-capital's. The full
ledger stood at 44 expectations by 08-02's close (17 hit total, 2 passed-
silent — both outside this week's resolution batch, elsewhere on the
record). **New expectations logged this week, global-capital-relevant:**
`coreweave-q2-earnings` (due 08-11) · `fomc-september-decision` (09-16) ·
`softbank-q1-earnings` (08-06 — corrected from an initially wrong 07-30
date, not a slip) · `fy2027-appropriations` (09-30) ·
`softbank-openai-bridge-matures` (2027-03-25, a hard clock on OpenAI's
liquidity story that sits before the 2027 IPO window analysts are
converging on).

## 🍂 Decay review

The map is clean — zero threads past the 10-day staleness threshold among open/developing status. One bookkeeping fix applied during this run: `ai-compute-spend` (a meta-thread) had a real 2026-07-30 timeline entry (Samsung HBM/DRAM pricing) but its `last_seen` field had never been synced to match — corrected to 2026-07-30. Nothing to retire, nothing for Ben to decide this week.

## 🔍 Near-miss audit

- **The week's real miss: Situational Awareness's forced liquidation to
  Citadel (07-30) was entirely absent day-of.** Money Stuff led with it,
  6+ outlets corroborated the sale, lenders, leverage and buyer — this map
  had nothing until the 08-01 finalize pass added it with `sev=major`.
  First AI-thesis fund broken by the trade it was betting on; the specific
  holdings and stake valuation stayed unconfirmed even after the add
  (two independent sweeps returned different position lists).
- **Couche-Tard's ~$8.7B acquisition of Poland's Żabka Group (07-31)** was
  Axios Pro Rata's actual lead story that day and never entered
  deals-and-filings — a clean, confirmed recall miss, though ruled a
  deliberate non-add (general retail M&A, outside this lens's AI-capital
  focus) rather than a gap to fix.
- **The Broadcom-Samsung ~$200B collaboration was mis-dated by five days,
  and had actually been wrong three separate times.** Filed as a 07-30
  development; the thread file separately claimed it "broke 07-28"; the
  true date, per Samsung's own newsroom release, is 07-25 — and it's a
  non-binding MOU, not the signed contract this map had recorded. Same
  failure family as the SpaceX pricing misdate two weeks ago: aggregation
  re-indexing a story into a later news cycle reads as a fresh event.
- **The Fed-chair gap is arguably the week's most structural finding**,
  as much a near-miss as a throughline item: two straight weeks of
  detailed FOMC vote coverage (the 9-3 hold, all three dissenters named)
  with no record anywhere of who chairs the committee. Found 08-02 via
  cross-sweep *agreement* — two independent sweeps sharing no sources
  landed on the same fact the same day, which this pipeline had previously
  only used contradiction-detection for. Kevin Warsh and Jerome Powell are
  now watchlist entities; a "Fed chair" theme was added.
- **Also worth naming, a self-caught data-integrity error rather than a
  benchmark miss:** both this lens's and the AI lens's 07-28 digests
  originally headlined "Nvidia -5%" as a same-day event; price history
  showed it was 07-27's move, and 07-28 was actually a credit/equity
  divergence (CDS wide, equity flat) — a more useful signal than the
  synchronized break originally reported. Caught by cross-sweep
  contradiction, corrected same-week.
- **DeepSeek's 1GW Inner Mongolia campus plus IPO prep, and Xsight Labs'
  $300M raise at a $2.8B valuation**, both benchmark leads on 07-30 this
  map missed and added at finalize — minor next to Situational Awareness
  but real.

## 🔄 Map deltas of the week

**07-27 — the board's structural rewrite, plus the week's first two new
threads.** Four-axis measurement model went live (`capitalization` renamed
schema-wide to `commanded_capital`; thrust promoted to a first-class axis;
gravity's method un-deferred to a structural/attributable formula;
optionality confirmed as a measured band, never derived) — `axes_num`
written for 21 pilot actors (agent-derive). `openai-custom-silicon`
retired → folded into `inhouse-silicon` (ben-steer). New meta thread
`frontier-lab-ipos` opened with three children including a new
`anthropic-ipo-timing` (ben-steer). `nvidia-vendor-financing` and
`ai-trade-bear-turn` opened (ben-steer — Ben's explicit call that the
index-direction story is "its own thing," not circular financing).
Thread count 43→45→47. W1 capex crawl completed (Google/Microsoft/AWS/Meta,
167 sources) — the destination layer's first real depth.

**07-28 — the zero-thread chokepoints closed, and the board went fully
numeric.** W2 crawl (TSMC/Arm/Intel/CoreWeave, 172 sources) plus
`meta-gas-pivot` threaded; threads 47→52. `asset-managers-build-ai` and
`softbank-all-in` opened (W5, ben-steer). xAI classified as an L2 subnode
under SpaceX — money consolidates at the parent, identity stays separate
(ben-steer). `custom-asic-tolls` and `qualcomm-dragonfly` opened
(ben-steer); threads 54→56. W4 memory-trio crawl landed mid–"Black
Tuesday" (SK Hynix -14.65%, KOSPI -10.84%, explicitly CXMT-triggered).
Row 24 assembled: **53 orgs now carry full `axes_num`** (was 22) — labs,
the Musk pair (SpaceX consolidated, Tesla's first axes), memory/chips,
capital pools, insurers, and seven US health payers for the first time.
`payer-ai-claim-denial` and `mhpaea-parity-limbo` opened (ben-steer);
threads 56→58. Row 23 applied: `gov-pool` pocket plus 12 agency nodes (7
US, 5 Canada) plus a Canada state node — board 79→92 orgs. Four new
threads: `genesis-mission`, `chips-equity-pivot`, `dod-ai-consolidation`,
`canada-ai-vs-care`; threads 58→62. Rows 7-8 (the collectors pipeline)
built same day — 7 live collector modules, `/daily` flipped to
collectors-first.

**07-29 — a split, and a critic-added thread.** `chip-hyperscaler-rotation`
split out of `chips-equity-pivot` (ben-steer: "give it its own thread for
the rotation") to carry the earnings-gauntlet monetization verdict; the
tier-2 agent that first drafted it into the wrong thread flagged its own
mismatch rather than forcing the fit. `openai-agent-security-incident`
opened critic-add (frontier-ai lens, cross-referenced here since the
capital-markets misses shared the same benchmark-recall pass). Microsoft's
earnings date churned 07-29→07-30→07-29 before a primary-source check
settled it (see scorecard above).

**07-30 — the earnings verdict, the war-widening flash, and World News
built same day.** Meta/Microsoft/Arm/Qualcomm's overnight results folded
into the still-open 07-29 digest (calls landed before the 5am boundary).
`red-sea-oil-shock`'s flash updated in place (not duplicated) as the
Iran-Iraq conflict widened to direct US strikes inside Iran, Saudi Arabia
joining as a combatant, and Treasury sanctioning the Hormuz insurance-
extortion scheme. `tools/world_news.py` and `attention/world-news.yaml`
shipped and backfill-validated same day (Ben: "I don't want to wait a
week"); `red-sea-oil-shock` trimmed to oil/shipping/underwriting content
only, with conflict-narrative content split to the new `iran-conflict-
widening` thread. Finalize pass (run 08-01) added Situational Awareness's
liquidation (`sev=major`), DeepSeek's Inner Mongolia campus, Xsight Labs'
round, and corrected Broadcom-Samsung's date; one `sev=major` demoted
(chip-hyperscaler-rotation's "pattern held" line) to keep the flag
discriminating on an unusually heavy day.

**07-31/08-01/08-02 — the redating and the Fed-chair discovery.** A
systematic day-assignment bug found and documented: four 07-30 items
(Anthropic's Claude self-breach disclosure, the Google/Anthropic $15B
guarantee, Apple's Q3 print, OpenAI's Luna price cut) had been bucketed
into 07-31 because a morning sweep attributed overnight news to the
current day rather than the 5am boundary — left in place with
`DAY-ASSIGNMENT NOTE` cross-references rather than moved, since both days
sit inside this same week. Iran conflict redated: the war began 02-28, not
07-23 (a price-move date had silently become a war's start date when
`iran-conflict-widening` was split from `red-sea-oil-shock`). Hormuz
redated: shut five months, not one week — transits ~10/day against a
60-140/day norm, all four major container lines rerouting via the Cape,
war-risk insurance at 3-10% of hull value against ~0.25% pre-war
(`sev=major`). **Kevin Warsh and Jerome Powell added to the global-capital
watchlist, plus a "Fed chair" theme (critic auto-add, 08-02)** — the
week's single biggest structural correction, detailed above.
`anthropic-ipo-filing`'s claim rewritten with the corrected 06-01 source.
EU AI Act mechanism fix applied (cross-lens with frontier-ai).

---
The vendor-financing structure that defined last week got its first real
test this week and didn't hold cleanly: Nvidia's credit swaps hit a record
high, and a leveraged AI-thesis hedge fund was forced to sell its whole
book to Citadel. A seven-event Wednesday earnings gauntlet then drew a
sharp line between hyperscalers proving their AI spend converts to revenue
and everyone else, even as the chip sector had its worst month since 2002.
And underneath two weeks of detailed Fed coverage, this map discovered it
had never named the man running the Federal Reserve — Kevin Warsh, a hawk
confirmed by the narrowest margin in the job's history. Coming week: SpaceX's
first post-IPO earnings against a $123B insider unlock, SoftBank's delayed
Q1 print, and whether Oracle's widening credit becomes the next thing this
market breaks.
