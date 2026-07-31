---
lens: global-capital
date: 2026-07-29
status: final
window_start: 2026-07-29T05:00:00-04:00
as_of: 2026-07-30T06:30:00-04:00
coverage: done
---

# Global Capital — 2026-07-29

*Curated from the 12-collector run (google-news + rss + gdelt + sec_edgar +
federal_register + fred + the tier-2 wave) plus 5 tier-2 cluster agents —
extended overnight with the four-print earnings gauntlet, 1 tier-2 agent
(agentic-interim). Day closed; coverage pending (finalizable from ~10:00
ET 07-30).*

## Today's throughline

The Fed held and the committee split three ways doing it. Rates stayed at
3.50%-3.75% on a 9-3 vote with three dissents *for a hike* — after a
unanimous 12-0 in June — and the statement language barely moved, so the
disagreement is entirely in the vote, not the prose. It landed into a tape
still absorbing yesterday's Asian chip rout, with the Dow down some 800
points into a close that four of the biggest capex spenders report after.
The AI trade's credit leg moderated rather than broke: Nvidia's swaps eased
off Monday's record and Oracle took over as the widest-trading hyperscaler,
which moves the circular-financing question from the lender to the largest
lessee.

**Then the four-print gauntlet answered, and split the "capex peaking"
thesis in two.** Capex is not peaking — Meta raised its guide again to
$130-145B and Microsoft guided FY27 to "grow year-over-year" — but the
rotation away from chips is real, and it ran on a different axis than
assumed. Arm and Qualcomm both fell on genuinely strong AI-specific
numbers; Meta, a hyperscaler, fell just as hard as they did, on an EPS
miss and near-zero free cash flow. Microsoft alone was rewarded, on 43%
Azure growth that bought tolerance for its spend. The dividing line
tonight was monetization-proven vs. monetization-unproven, not
hyperscaler vs. chipmaker.

## Capital in my markets

- **The Fed held at 3.50%-3.75% on a 9-3 vote, with three dissents for a quarter-point hike** — Hammack, Kashkari and Logan; June's decision was unanimous. ([Federal Reserve](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm))
  <!-- k: t= e= axis=capital-in-my-markets sev=major -->
- **The statement's descriptive language is essentially unchanged from June** — same lines on growth "despite elevated uncertainty" and on energy supply shocks; the committee split, the text did not. ([Federal Reserve](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm))
  <!-- k: t= e= axis=capital-in-my-markets -->
- **The Asian chip rout is scored to 07-28, not today** — Korea's second circuit-breaker session closed 02:30 ET, before the 5am digest boundary, so it sits in yesterday's digest where it is already recorded. Today's 07-29-datelined coverage, including the "$1T off Asian chip stocks" tally, is reporting *that* session. ([CNBC](https://www.cnbc.com/2026/07/29/chip-selloff-sk-hynix-samsung-softbank.html))
  <!-- k: t=ai-trade-bear-turn,ai-memory-shortage e= axis=capital-in-my-markets -->
- **South Korea called an emergency market meeting** and moved to tighten curbs on leveraged and inverse ETFs after the rout — the regulatory response, which is new. ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-29/south-korea-to-hold-emergency-market-meeting-after-kospi-turmoil))
  <!-- k: t=ai-trade-bear-turn e= axis=capital-in-my-markets -->
- **Nvidia's credit-default swaps eased to roughly 78bp from Monday's record 82bp, and Oracle overtook it** as the widest-trading hyperscaler — the widening moderated rather than continued. ([Seeking Alpha](https://seekingalpha.com/news/4620575-oracle-leads-record-widening-in-hyperscaler-cds-spreads))
  <!-- k: t=ai-circular-financing-risk,nvidia-vendor-financing e=nvidia,oracle axis=capital-in-my-markets -->
- **Nvidia fell about 2.1% intraday**, still trading the standing $250B OpenAI-guarantee reports rather than any new disclosure. ([TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-29-2026stock-market-today-july-29-2026))
  <!-- k: t=ai-trade-bear-turn,nvidia-vendor-financing e=nvidia axis=capital-in-my-markets -->
- **Brent sits around $89.5-90.4 and WTI around $82.3-84.4**, holding the gains from Tuesday's strike on the US base in Jordan; sources disagree sharply on the day's percentage move even as levels agree. ([Fortune](https://fortune.com/article/price-of-oil-07-29-2026/))
  <!-- k: t=red-sea-oil-shock e= axis=capital-in-my-markets -->

## Deals & filings

- **Four of the largest AI capex spenders report after today's close** — Microsoft FY26 Q4, Meta Q2, Arm Q1 FY27 and Qualcomm Q3 FY26, all confirmed from company IR. ([Microsoft](https://news.microsoft.com/source/2026/07/08/microsoft-announces-quarterly-earnings-release-date-68/))
  <!-- k: t=microsoft-capex,meta-capex,hyperscaler-capex-big-picture e=microsoft,meta-ai axis=deals-and-filings -->
- **A separate Nvidia-to-OpenAI chip-financing negotiation of roughly $350B sits alongside the $250B lease-and-construction guarantee** — two distinct instruments, which together are what could carry the Ohio project past $500B. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/nvidia-weighs-250-billion-guarantee-so-openai-can-lease-softbanks-10-gigawatt-ohio-campus))
  <!-- k: t=nvidia-vendor-financing,ai-circular-financing-risk,stargate-buildout e=nvidia,openai axis=deals-and-filings -->
- **No company has confirmed the $250B guarantee** — terms remain explicitly unfinalized and "could fall apart"; the figure is press consensus across WSJ, Bloomberg and Reuters, not a signed deal. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/nvidia-weighs-250-billion-guarantee-so-openai-can-lease-softbanks-10-gigawatt-ohio-campus))
  <!-- k: t=nvidia-vendor-financing,ai-circular-financing-risk e=nvidia,openai axis=deals-and-filings -->

## 🌙 The overnight earnings gauntlet — the verdict

- **Meta beat revenue but missed EPS by ~14-15%, with free cash flow near
  zero ($784M) against a ~$12B/quarter trailing average** — capex was
  raised again, to $130-145B, the second raise this year. Stock -8.5%
  premarket. ([StockTitan](https://www.stocktitan.net/news/META/meta-reports-second-quarter-2026-hkjfhayj8l0v.html))
  <!-- k: t=meta-capex,hyperscaler-capex-big-picture,chip-hyperscaler-rotation e=meta-ai axis=deals-and-filings -->
- **Microsoft beat on revenue, EPS and Azure growth (43% cc, above a
  39-40% guide)**, though the EPS figure carries a ~$3.2B unrealized gain
  on its Anthropic stake. FY27 capex guidance stayed qualitative — the
  named OpenAI-vs-own capex split did NOT happen. Stock +8-9% after-hours.
  ([Microsoft IR](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast))
  <!-- k: t=microsoft-capex,hyperscaler-capex-big-picture e=microsoft axis=deals-and-filings -->
- **Arm beat and raised on every metric, including AGI-CPU bookings
  doubling to $2B+ — and the stock fell anyway**, -4.95% premarket,
  extending its pre-earnings -28% run. What moved it: a full-year royalty
  growth guidance cut to "high teens" from ~20%, on smartphone weakness.
  ([Arm Newsroom](https://newsroom.arm.com/news/arm-q1-fye27-results))
  <!-- k: t=arm-royalty-regime,chip-hyperscaler-rotation e=arm axis=deals-and-filings -->
- **Qualcomm's guide missed on legacy handset weakness, not on
  Dragonfly** — its custom-silicon revenue starts in December, one
  quarter out. The FY2029 non-handset target was raised to $40B from
  $22B. Stock -4.8% premarket.
  ([CNBC](https://www.cnbc.com/2026/07/29/qualcomm-qcom-earnings-report-q3-2026-.html))
  <!-- k: t=qualcomm-dragonfly e=qualcomm axis=deals-and-filings -->
- **New detail on Microsoft's own quarter: $130B in new data-center
  leases signed this quarter alone**, pushing total not-yet-commenced
  lease commitments to $329.1B from $196.6B the prior quarter — and the
  first disclosed break-out of its AI-lab stakes: the Anthropic position
  marked UP $3.2B (+33¢ EPS), the OpenAI position marked DOWN $600M
  (-7¢ EPS), in the same quarter.
  ([Bloomberg](https://www.bloomberg.com/) via [Irish Times](https://www.irishtimes.com/); [TechCrunch](https://techcrunch.com/))
  <!-- k: t=microsoft-capex e=microsoft axis=deals-and-filings -->
- **Samsung joined the same pattern overnight: a record beat, and the
  stock still faded.** Total operating profit +1,814% YoY on a record
  chip quarter (~70% DS margin, first time above 70%) — but mobile (MX)
  posted its first-ever operating loss on the same memory prices that
  made the chip side record. Stock jumped +7-8% intraday, then closed
  down ~1-1.2%; Kospi fell >1%, SK Hynix >5% same session.
  ([Samsung Newsroom](https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results))
  <!-- k: t=ai-memory-shortage,chip-hyperscaler-rotation e=samsung axis=deals-and-filings -->
- **The dividing line across all four was monetization-proven vs.
  monetization-unproven, not hyperscaler vs. chipmaker** — Microsoft
  bought tolerance for its capex with visible Azure acceleration; Meta,
  a hyperscaler, did not, and fell as hard as Arm and Qualcomm did.
  <!-- k: t=chip-hyperscaler-rotation,ai-trade-bear-turn e= axis=deals-and-filings sev=major -->

## 🌍 The war widened, and so did its price

- **The Iran-US conflict escalated well past the Jordan strike overnight:
  the US struck targets inside Iran directly (Bandar Abbas, Kish Island,
  Khuzestan's oil belt), killing civilians on Qeshm Island; Saudi Arabia
  joined US airstrikes against Iran-backed militias in Iraq — its first
  direct military action of this kind; Iran killed a worker in Kuwait and
  a drone hit vessels at Egypt's Damietta port, both new countries in this
  conflict.** ([NPR](https://www.npr.org/2026/07/30/nx-s1-5913077) · [Al Jazeera](https://www.aljazeera.com/where/iraq/))
  <!-- k: t=red-sea-oil-shock e= axis=capital-in-my-markets sev=major -->
- **US Treasury sanctioned 10 firms and 8 tankers, including Persian Gulf
  Marine Insurance Co. and HormuzSafe Marine Services, over an Iranian
  scheme extorting insurance payments for Strait of Hormuz passage** — a
  direct, dated instance of the underwriting layer this thread is meant
  to price, not oil moving as a proxy for it. ([Bloomberg — headline/date
  confirmed via search, not directly fetched](https://www.bloomberg.com/) · [Iran International](https://www.iranintl.com/))
  <!-- k: t=red-sea-oil-shock e= axis=capital-in-my-markets -->
- **Brent is now ~$92.10 (+1.5%) and WTI ~$85.23 (+0.9%) this morning**,
  continuing yesterday's +7.9%/+6.6% surge rather than reversing it.
  Houthis are reportedly weighing a toll on Red Sea transit near
  Bab-el-Mandeb — a second supply-risk vector distinct from Hormuz.
  ([Washington Post](https://www.washingtonpost.com/)) ⟨sourced this morning⟩
  <!-- k: t=red-sea-oil-shock e= axis=capital-in-my-markets -->
- **This is not "oil went up" — it is a live case of conflict being
  priced twice: once through the commodity (Brent/WTI), once through the
  underwriting layer (Treasury's insurance-extortion sanctions, and by
  implication the war-risk premiums insurers now attach to Hormuz and Red
  Sea transit).** Worth a standing watch, not a one-day mention — see the
  map-changes note below on a possible dedicated tracking approach.
  <!-- k: t=red-sea-oil-shock e= axis=capital-in-my-markets -->

## 📊 Macro strip

- **Fed funds target — 3.50%-3.75%**, unchanged; third consecutive hold, now with three hawkish dissents (prior read: unanimous hold, 06-17).
- **Brent — ~$92.10**, up again from ~$89.5-90.4 yesterday, continuing rather than reversing the surge.
- **WTI — ~$85.23**, up from ~$82.3-84.4.
- **Nvidia 5y CDS — ~78bp**, off the record 82bp set 07-27; Oracle now wider.
- **Hormuz transits — 78 for 07-13/20**, against 174 the prior week; still suppressed, no fresher print.
- **30Y Treasury yield — ~5.24%**, highest since 2007, extending the post-FOMC bond selloff.
- **New this morning: Q2 GDP advance estimate + June PCE**, 8:30am ET — consensus core PCE 3.3% YoY, headline 3.7%. First real catalyst after the hawkish hold.

## ⏳ Upcoming & expected

- ✅ **hit — `fomc-july-decision`**: held at 3.50%-3.75%, 9-3, three dissents for a hike. The ~24% hike odds carried since 07-21 did not fire, but the hawkish read was not wrong — the committee went from 12-0 to 9-3 in six weeks.
- ✅ **hit — `meta-q2-earnings`**: beat on revenue, missed on EPS, capex raised again to $130-145B.
- ✅ **hit — `microsoft-q2-earnings`**: beat across the board, Azure to 43%; the OpenAI-vs-own capex split did not disclose.
- ✅ **hit — `arm-q1fy27-earnings`**: beat-and-raise, stock fell anyway on a smartphone-royalty guidance cut.
- ✅ **hit — `qualcomm-q3fy26-earnings`**: guide missed on legacy handset weakness; Dragonfly's contribution starts in December.
- ✅ **hit — `samsung-q2-breakdown`**: record chip profit, first-ever MX mobile loss, faded on the same "priced-in" pattern.
- **New:** `fomc-september-decision` due 09-16 — does the three-dissent bloc grow, hold or fold.
- **New:** `mn-nudify-ban-effective` due 08-01.
- **New:** `gdp-pce-2026-07-30` — 8:30am ET today.
- Next 7 days: `amazon-q2-earnings` due today (07-30, after close); `gov-review-framework-announce` and `eo14409-deadlines` both 08-01.

## 🔄 Map changes

- `~ upcoming/microsoft-q2-earnings` — due 07-30 → **07-29**, verified against two Microsoft primary sources. A tier-2 agent's 07-28 "correction" to 07-30 was wrong and had been trusted because the ledger normally outranks thread prose (⟨daily 07-29⟩).
- `~ upcoming/fomc-july-decision` — pending → **hit** (⟨daily 07-29⟩).
- `~ upcoming/arm-q1fy27-earnings` — confidence reported → **confirmed**, Arm's own release-date announcement (⟨daily 07-29⟩).
- `~ upcoming/ca-sb903-assembly` — confidence confirmed → **reported**; 08-14 is not SB 903-specific on the Assembly calendar and a second source puts the deadline at 08-29 (⟨daily 07-29⟩).
- `+ upcoming/fomc-september-decision` — 09-16 (curate-add 07-29).
- `+ upcoming/mn-nudify-ban-effective` — 08-01 (curate-add 07-29).
- `~ threads/microsoft-capex` — watch prose reverted to 07-29 after the ledger correction above (ben-steer → primary-source override, 07-29).
- `~ upcoming/meta-q2-earnings`, `~ upcoming/microsoft-q2-earnings`, `~ upcoming/arm-q1fy27-earnings`, `~ upcoming/qualcomm-q3fy26-earnings` — all four pending → **hit**, resolved overnight (⟨daily 07-29⟩).
- `~ threads/meta-capex`, `~ threads/microsoft-capex`, `~ threads/arm-royalty-regime`, `~ threads/qualcomm-dragonfly`, `~ threads/chip-hyperscaler-rotation`, `~ threads/ai-trade-bear-turn` — overnight earnings blocks added (⟨daily 07-29⟩).
- `~ upcoming/samsung-q2-breakdown` — pending → **hit**, resolved in this window despite a 07-30 due date; the release landed ~19:00-21:00 ET on 07-29, before the 5am boundary (⟨daily 07-29⟩).
- `+ upcoming/gdp-pce-2026-07-30` — 8:30am ET (curate-add 07-29).
- `~ flash/iran-strikes-us-base-jordan` — updated in place (not a second flash): the conflict widened to direct US strikes on Iran, Saudi Arabia joining as a combatant, Kuwait and Egypt hit; `expires` extended to 08-02 (ben-steer, 07-30 — ongoing severity confirmed by a dedicated verification pass, see coverage-log.md).
- `~ threads/red-sea-oil-shock` — extended with the Treasury Hormuz-insurance sanctions and the widened conflict (⟨daily 07-29⟩).

## 🧵 Thread candidates

- **candidate:** Oracle has quietly overtaken Nvidia as the widest-trading hyperscaler credit — the circular-financing worry migrating from the lender to the largest lessee. Track it? ([Seeking Alpha](https://seekingalpha.com/news/4620575-oracle-leads-record-widening-in-hyperscaler-cds-spreads))
- **candidate:** Korea's emergency market meeting and leveraged-ETF curbs — a national regulator responding to an AI-driven equity rout. Track it? ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-29/south-korea-to-hold-emergency-market-meeting-after-kospi-turmoil))
- **resolved, not a candidate anymore:** the standing "conflict pricing" watch above is now World News + Global Capital (built/specced 2026-07-30 — see ROADMAP §World News, §Global Capital).

## Appendix — Coverage check vs. benchmarks (2026-07-30)

Checked against Money Stuff, Axios Pro Rata, FT Unhedged, Bloomberg
Technology. Coverage held up well — the Fed-vote, four-print gauntlet,
CDS-spread, and Iran-war-oil sections were more thorough than any single
benchmark. One cross-lens gap found (SpaceX's post-IPO turmoil, flagged
independently by Money Stuff and Axios Pro Rata) is **not backfilled
here** — the same-run tier-2 dispatch found a materially fresher, more
precise version of the story dated 07-30 (SPCX closed $114.87, -49.1%
from its 06-16 ATH, ~15% below its $135 IPO price, ~$26B short interest);
that carries the story forward in today's digest instead. Full detail:
coverage-log.md.

---
The Fed held rates but split three ways doing it, with three dissents for a
hike after a unanimous June. That night four of the AI trade's biggest
spenders reported: capex kept rising at both hyperscalers, but Wall Street
punished Meta as hard as it punished the chip names, rewarding only
Microsoft's visible monetization. The rotation is real; it just isn't the
axis anyone assumed. Overnight the Iran war widened well past its
triggering strike — direct US action inside Iran, Saudi Arabia in as a
combatant, two new countries hit — and Treasury sanctioned the actual
underwriting layer that war-risk premiums run through, not just the oil
price everyone already watches.
