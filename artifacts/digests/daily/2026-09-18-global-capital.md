---
lens: global-capital
date: 2026-09-18
status: final
window_start: 2026-09-18T05:00:00-04:00
as_of: 2026-09-19T10:30:00-04:00
coverage: done
---

# Global Capital — 2026-09-18

*Curated agentic-interim, 05:00 ET 09-18 → 05:00 ET 09-19 (final;
evening window swept 09-19). First pass (05:00-15:00 ET same day) rests
on WebSearch/WebFetch against `attention/watchlist.yaml`, open threads,
and `attention/capital-context.yaml` (asof 2026-08-25, read for
grounding on the rate-regime and cross-border framing, not treated as
current itself), and checked `buffer/2026-09-18-rss.jsonl` (104 rows).
This finalize pass swept the previously-uncovered 15:00 ET Friday → 05:00
ET Saturday window — the US close, oil settlements, and Friday-evening
filings — plus `buffer/2026-09-18-sec_edgar.jsonl` (229 rows) and
`buffer/2026-09-18-federal_register.jsonl` (47 rows), neither of which
carried anything relevant to this lens's watchlist names. CNBC's oil and
market pages, TheStreet, Reuters and MarketWatch all 403'd on both
`python3 urllib` (Googlebot UA) and WebFetch this pass — a new, broader
block than the single-page CNBC 403 logged 09-18 morning — so the
US-close and settlement figures below are triangulated across
`tradingeconomics.com` (its own par-yield-curve and commodity pages,
which state their Treasury/CME sourcing), the U.S. Treasury's own daily
par yield curve (mirrored live by stockmarketwatch.com/bonds, which
cites "official U.S. Treasury data"), and two independent same-day
recap sources (vittarthi.com's dated close snapshot and KBL
Destinations' Substack market report) that agree with each other and
reconcile arithmetically against Thursday 09-17's already-confirmed
close — not a single wire's own "settled at" sentence, which is a
transport gap worth flagging rather than a substitute for one.

## Today's throughline

Virginia's governor rolled out the most aggressive state data-center
regulatory framework in the country and launched a new state AI task
force, the same Friday Wall Street closed out a triple-witching session
still digesting Wednesday's Fed rate hike in a narrow, mixed band: the
S&P 500 finished essentially flat at 7,627.99 (-0.13%), the Dow fell
0.35% to 51,597.80 and the Nasdaq closed flat at 26,415.85 (-0.01%),
while the 10-year Treasury yield closed at 5.01% (+7bp) and the 30-year
at 5.34% (+5bp), both closing at their highest since 2007. Warren Buffett
stepped down as Berkshire Hathaway's chairman after 56 years, handing the
non-executive chair to his son Howard while Greg Abel keeps running the
company. Overnight Asia had carried forward both of Thursday's big
stories: the Bank of Japan's 25bp hike to 1.25% weakened the yen further
rather than strengthening it, and USD/JPY broke above 157 to a two-week
high near ¥157.90 intraday before settling back to close at ¥156.87
(+0.58%), on a split 7-2 board vote and a governor's press conference
that gave mixed signals on the pace of further hikes; Asian equities
extended Wall Street's Thursday rally rather than selling off on the
hike, with chipmakers leading on Nvidia CEO Jensen Huang's comments that
the company will double the number of chips it sells next year,
production capacity rather than customer demand now the binding
constraint. Oil, which had eased a fourth straight session to about
$102.57 in Asian trading and round-tripped intraday to roughly $104.34 as
Saudi Arabia and Yemen's Houthis traded fresh cross-border attacks
Thursday, resumed its slide into the close: Brent settled at $103.87
(-0.91%) and WTI at $100.30 (-1.58%), each lower on the day as markets weighted Saudi Arabia's pipeline-restart timeline over
the fresh border clash — a reminder that oil is currently pricing
conflict-escalation odds as much as physical barrels, in both directions
within the same session. SoftBank added a fourth financing lever this
week, after a dollar-bond roadshow that closed unpriced and loan talks
with Apollo against its second Vision Fund: Bloomberg reported SoftBank
increased its Arm-backed margin loan from $20bn to $25bn, renegotiated
with creditors this month, with lenders offering roughly $7bn of demand
against a $3-5bn target, and Tokyo shares closed the day up more than
2.5% on the news. Late Friday, Paramount and the 12 states suing to block
its $110bn Warner Bros. Discovery acquisition moved toward a possible
settlement — CNN content-monitoring and a theatrical-release commitment
among the terms — sending both companies' shares up sharply after hours.

## 📊 Macro strip

*vs. yesterday's 2026-09-17 finalized digest.*

| line | value (~10:00 ET) | vs. last read |
| --- | --- | --- |
| Brent | ~$102.57, -2.2% | fourth straight down session, extending Thursday's Saudi-restart drop |
| WTI | ~$100.05, -1.9% | tracking Brent lower |
| Yen (USD/JPY) | continuing to soften toward ¥157 | weakened 0.45% to ¥156.64 on the BOJ decision itself, softening further into this morning |
| Nikkei 225 | +1.5-2% (intraday) | first full session since the BOJ hike — rallying, not selling off, on the decision |
| Hang Seng / Shanghai Composite | +0.6% / +1% | broad Asian follow-through on Wall Street's Thursday close |
| SoftBank (9984.T) | +1.5% to ¥6,341 | extends the recovery from 09-14's OpenAI-IPO-doubt selloff |
| US equity futures | pointed to further gains | European futures set for a slightly weaker open by contrast |

### Afternoon update (~15:00 ET, provisional — markets close 16:00 ET)

*Levels below are intraday and will move again before the close; treat
as provisional, not a final read.*

| line | value (~14:30-15:00 ET) | vs. this morning's read |
| --- | --- | --- |
| S&P 500 | ~7,620, roughly flat / -0.1 to -0.2% on the day | choppy, not a continuation of Thursday's rally — over 350 constituents retreating even as the index itself holds near flat |
| Dow Jones | -0.1 to -0.3% intraday | tracking the broader index's chop |
| Nasdaq Composite | flat to +0.2% intraday | chipmakers (Broadcom, AMD, Intel) providing the lift that's keeping it positive |
| 10-year Treasury yield | ~5.0%, +5bp on the day | highest since July 2007; markets pricing continued Fed tightening after Wednesday's hike |
| Dollar index (DXY) | ~100.3 | on track for its best week since May |
| Brent | ~$104.34, -48c (~flat) | round-tripped off the ~$102.57 Asian-session low as fresh Saudi-Houthi border clashes revived the war-risk premium |
| WTI | ~$101.66, -25c | same round-trip; still up roughly 1% for the week |
| Yen (USD/JPY) | broke above 157, ~¥157.90 (two-week high) | extends this morning's softening; BOJ's 7-2 dissent reading as an unresolved internal split |
| SoftBank (9984.T) | closed +2.56% to ¥6,407 | Tokyo session closed before the NY open; extends this morning's +1.5% reaction to the Arm margin-loan increase |

Today is also a quarterly "triple witching" expiration (stock-index
futures, stock-index options and single-stock options expiring
simultaneously — single-stock futures do not currently trade in this
market, so the fourth leg some AI-generated market summaries add is
inaccurate), which market commentary is citing as a contributor to the
session's choppy, directionless trade and elevated volume; Citadel
Securities estimated roughly $7 trillion in options exposure expiring,
one of the largest expirations on record.

🔧 **Correction — this digest called today's expiration "quad witching"
in the morning and afternoon passes; every wire and market-report source
checked at finalize (TheStreet, Foreign Policy Journal, KBL Destinations,
Alain Guillot) calls it triple witching, the standard quarterly term for
stock-index futures/options plus single-stock options. Corrected above
and in the throughline; "quad witching" would require single-stock
futures, which are not a live US contract.**

### Final close (16:00 ET Friday, 2026-09-18)

*Reconciled against Thursday 09-17's already-confirmed close (S&P
7,637.72, Nasdaq 26,418.30, Dow 51,779.85) — each figure below checks out
arithmetically against that base, corroborated by two independent
same-day recap sources (vittarthi.com, KBL Destinations) that agree with
each other to the same basis point / cent.*

| line | close | change | vs. this morning's/afternoon's provisional read |
| --- | --- | --- | --- |
| S&P 500 | 7,627.99 | -0.13% | afternoon read (~7,620, "roughly flat") was directionally right but a touch low |
| Dow Jones | 51,597.80 | -0.35% | afternoon read (-0.1 to -0.3%) slightly understated the decline |
| Nasdaq Composite | 26,415.85 | -0.01% | afternoon read (flat to +0.2%) overstated it; chipmaker strength didn't hold the index positive into the close |
| 10-year Treasury yield | 5.01% | +7bp | afternoon's ~5.0%/+5bp was close; final move was a touch larger, per Treasury's own par yield curve |
| 30-year Treasury yield | 5.34% | +5bp | not read this morning/afternoon; highest close since 2007 alongside the 10-year |
| Dollar index (DXY) | ~100.22-100.23 | roughly flat | confirms the afternoon's "~100.3" read; best week since May holds |
| Brent | $103.87 | -0.91% | the afternoon's "~$104.34, ~flat" read did NOT hold into the close — oil resumed its decline in the final trading hours rather than staying flat |
| WTI | $100.30 | -1.58% | same correction — the afternoon's "~$101.66" read was a session high on the recovery, not the close |
| Yen (USD/JPY) | ¥156.87 | +0.58% on the day | the afternoon's "broke above 157, ~¥157.90" was the intraday high, not the close — yen gave back roughly half that move by 16:00 ET |
| Gold | $4,383.45/oz | +0.97% | one-week high, first weekly gain in four weeks, as falling oil eased inflation concerns |
| VIX | ~15.3 | roughly flat | consistent with the afternoon's calmer read despite triple-witching volume |

Sources: [tradingeconomics.com/commodity/brent-crude-oil](https://tradingeconomics.com/commodity/brent-crude-oil), [tradingeconomics.com/commodity/crude-oil](https://tradingeconomics.com/commodity/crude-oil), [tradingeconomics.com/commodity/gold](https://tradingeconomics.com/commodity/gold), [tradingeconomics.com/japan/currency](https://tradingeconomics.com/japan/currency), [stockmarketwatch.com/bonds](https://stockmarketwatch.com/bonds) (cites official US Treasury par-yield-curve data), [vittarthi.com/markets/us](https://vittarthi.com/markets/us), [KBL Destinations Daily Market Report 9-18-26](https://kbldestinations.substack.com/p/daily-market-report-9-18-26). ⚠️ CNBC, Reuters, MarketWatch and TheStreet all 403'd on both `python3 urllib` and WebFetch this pass — a genuine wire "settled at" sentence was not directly reachable; the figures above are cross-validated across independent secondary sources rather than sourced to one wire, and are reported as such rather than dressed up as a single primary citation.

## Capital in my markets

- **SoftBank increased its Arm-backed margin loan from $20bn to $25bn,
  renegotiated with creditors this month, without reducing its Arm
  stake** — SOFR plus roughly 225bp and a 25bp credit-adjustment spread,
  maturing September 2027. Lenders reportedly offered about $7bn of
  demand against SoftBank's $3-5bn target, a sign banks remain
  comfortable taking Arm shares as collateral at today's prices. This is
  a fourth simultaneous SoftBank financing lever active this same week —
  alongside the still-unpriced $10-20bn dollar-bond roadshow (now
  passed-silent per 09-17's finalize) and Apollo's talks to nearly double
  the Vision Fund 2 NAV loan to $9bn (also logged 09-17) — each pledging
  a different slice of the same concentrated AI bet, exactly the
  "everything collateralizes everything else" pattern this map's own
  `softbank-all-in` thread was opened to track. Tokyo shares closed the
  session up 2.56% to ¥6,407, extending this morning's +1.5% reaction —
  the market reading the loan increase as a sign of continued lender
  confidence rather than a distress signal.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-09-18/softbank-raises-arm-margin-loan-to-25-billion-as-ai-bets-grow), [Finimize](https://finimize.com/content/softbank-taps-arm-shares-for-a-bigger-margin-loan))
  <!-- k: t=softbank-all-in axis=capital-markets -->
- **Brent settled at $103.87 (-0.91%) and WTI at $100.30 (-1.58%) Friday, after swinging between an Asian-session low near $102.57 and a midday recovery as Saudi Arabia and Yemen's Houthis traded fresh cross-border attacks.**
  Midday Friday, CNBC quoted Brent at $104.34 (down 48 cents) and WTI at
  $101.66; the Asian-session low did not hold through the US session,
  and the close gave back most of the recovery. Saudi Arabia's East-West
  pipeline restart plan and its Oman ship-to-ship workaround remain the
  supply-side story removing the premium built since the 09-10 drone
  strike; Thursday's border clash is
  pulling the same barrel the other way, and one market strategist
  quoted by CNBC said prices are currently more sensitive to the pace
  of the pipeline restart and to fresh incidents than to conventional
  supply-and-demand data.
  ([CNBC](https://www.cnbc.com/2026/09/18/oil-prices-today-brent-wti-saudi-arabia-houthi.html), [Vantage Markets](https://www.vantagemarkets.com/market-analysis/why-crude-oil-prices-fell-saudi-pipeline-repair-september-18-2026/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-17/latest-oil-market-news-and-analysis-for-sept-18))
  <!-- k: t=red-sea-oil-shock axis=capital-markets interp=yes -->
- **Virginia Governor Abigail Spanberger signed an executive order
  banning by-right data-center approvals and non-disclosure agreements,
  requiring local approval for facilities over 25 megawatts, and
  shifting grid transmission and generation costs onto data centers
  and other large-load customers, while launching a new state
  Artificial Intelligence Task Force the same day.** Local coverage is
  calling it the most comprehensive and aggressive data-center
  accountability effort of any US state. Virginia's Loudoun County —
  "Data Center Alley" — hosts the largest concentration of data centers
  in the world, so this lands as the closest test yet of this map's own
  `datacenter-backlash-capital-risk` watch for whether opposition
  becomes a priced financial risk rather than a local siting fight: the
  state with the most capital already sunk into the physical AI
  buildout just made permitting, secrecy, and cost-allocation
  structurally harder for the industry, not merely proposed doing so —
  a step beyond the executive orders already logged from Massachusetts
  and the moratoriums from Oregon, New Hampshire and Connecticut.
  ([WTVR](https://www.wtvr.com/news/local-news/spanberger-data-centers-ai-sept-18-2026), [Virginia Business](https://virginiabusiness.com/spanberger-bans-by-right-approvals-ndas-for-data-centers/), [WDBJ7](https://www.wdbj7.com/2026/09/18/governor-spanberger-holds-news-conference-data-centers-ai/))
  <!-- k: t=datacenter-backlash-capital-risk axis=capital-markets sev=major interp=yes -->
- **The yen extended its slide against the dollar into Friday, USD/JPY
  breaking above 157 to a two-week high near ¥157.90, even though the
  Bank of Japan hiked its policy rate to a 31-year high of 1.25% on
  Thursday.** Governor Kazuo Ueda's press conference gave mixed signals
  on the pace of further hikes, and the decision's 7-2 dissent
  (Takaichi-appointed reflationists Toichiro Asada and Ayano Sato
  voting against) continues to read to currency markets as a less
  unified BOJ than the headline vote count suggests — the "sell the
  rumor" pattern this map's own `cross-border-rates` thread flagged on
  09-17 as its next open question is holding for a second session.
  ([XTB](https://www.xtb.com/en/market-analysis/chart-of-the-day-yen-in-a-trap-boj-hike-that-weakened-the-currency-18-09-2026), [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-18/yen-drops-against-dollar-after-boj-raises-rates-as-expected), [FX Leaders](https://www.fxleaders.com/news/2026/09/18/usd-jpy-forecast-15815-target-after-boj-hike/))
  <!-- k: t=cross-border-rates axis=fx -->
- **Intel shares kept climbing on unconfirmed reports of SK Hynix talks
  over US memory-chip production, which both companies say involve "no
  plans confirmed," and on a Barclays upgrade from
  "Underperform" to "Overweight," trading in a $106-112 range Friday.**
  No new deal terms, site confirmation, or company statement found —
  this is continued price momentum on an unconfirmed report, not a new
  fact.
  ([Investing.com](https://www.investing.com/news/stock-market-news/intel-stock-bullish-breakout-takes-place-should-you-chase-the-rally-93CH-4907170), [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-reportedly-discussing-us-memory-chip-manufacturing-with-intel-options-include-leasing-ohio-plant-or-forming-joint-venture-with-other-ai-hyperscalers))
  <!-- k: t=intel-rescue,chips-equity-pivot axis=capital-markets -->
- **Chipmakers led Asia's rally on Nvidia CEO Jensen Huang's comments
  that the company will double the number of chips it sells next year,
  attributing the demand surge to AI's spread across an expanding range
  of industries — and naming production capacity, not customer demand,
  as the actual constraint.** Samsung, SK Hynix and other regional
  chipmakers rallied on the comments; Nvidia's own shares rose roughly
  2.5% Thursday and continued trading higher. Worth holding against this
  map's own AI-buildout-debt-risk watch: a supply-constrained rather than
  demand-constrained framing, from Nvidia's own CEO, cuts against the
  bear case (this map's own Burry/shadow-credit-backstop entries) that
  the buildout is running ahead of real demand.
  ([Investing.com/Reuters](https://www.investing.com/news/stock-market-news/nvidia-rises-after-signaling-longer-ai-spending-runway-4878530), [Blockonomi](https://blockonomi.com/nvidia-nvda-stock-gains-2-as-ceo-huang-forecasts-doubled-chip-demand/))
  <!-- k: t=ai-buildout-debt-risk axis=capital-markets -->

- **Warren Buffett stepped down as chairman of Berkshire Hathaway, the
  post he has held since 1970, with his son Howard Buffett succeeding him
  as non-executive chairman under the company's long-standing succession
  plan; Greg Abel remains chief executive with full operational
  control.** Buffett becomes chairman emeritus; Berkshire framed Howard's
  role as guarding the company's culture rather than running it. For
  Berkshire's posture on AI-era capital — large cash pile, little direct
  AI exposure — the decision-maker was already Abel, so the capital
  allocation question is unchanged; what ends is Buffett's formal
  authority over the board.
  ([CNBC](https://www.cnbc.com/2026/09/18/buffett-stepping-down-as-berkshire-chairman.html))
  <!-- k: t=berkshire-ai-capital-stance e=berkshire-hathaway axis=investors-and-allocators -->

## Deals & filings

- **Paramount and the 12 states (led by California AG Bonta) suing to
  block its $110bn Warner Bros. Discovery acquisition are in advanced
  talks to settle as soon as this weekend, with independent content
  monitoring of CNN and a commitment on the number of theatrical film
  releases among the terms under discussion.** Reuters (via CNBC,
  published 09-19 but reporting on Friday-evening sourcing) and Bloomberg
  (09-18, on Paramount's own after-hours share reaction) both confirm the
  talks; Paramount shares rose nearly 7% and Warner Bros. Discovery
  roughly 8.4% in after-hours trading Friday on the report. The case is
  one of the last hurdles to Paramount's bid to become a Netflix/Disney
  rival, and Paramount is on the hook for a $7M-a-day "ticking fee" to
  Warner Bros. shareholders for every day after 09-30 the deal hasn't
  closed — a concrete, dated financial pressure toward settling now
  rather than litigating further. This doesn't fit any of this lens's 21
  assigned threads (a media-merger antitrust settlement, not AI capital
  or a chips/data-center/rates story); flagged as a thread candidate
  below.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-09-18/paramount-shares-climb-on-report-of-warner-deal-settlement-talks), [CNBC/Reuters](https://www.cnbc.com/2026/09/19/paramount-could-settle-with-states-over-warner-bros-this-weekend-reuters.html), [Variety](https://variety.com/2026/film/news/paramount-california-ag-bonta-advanced-talks-settle-antitrust-suit-1236867326/))
  <!-- k: axis=deals interp=yes -->

*Otherwise swept again this pass (10:00→15:00 ET window, then again at
finalize for the evening window); nothing new beyond what's already
logged on 09-17 (CoreWeave's convertible-note pricing, the Apollo/
SoftBank NAV loan talks) or above (the Arm margin loan) on this lens's
own 21 threads. Checked specifically and came back quiet: Nvidia's $500B
compute-financing platform (no named deal from Apollo/BlackRock/
Blackstone/Brookfield/Goldman/KKR converting the 08-10 MOUs into an
actual transaction — re-checked again at finalize via a fresh WebSearch
for any deal dated after 08-10; `nvidia-500b-financing-first-close` in
`attention/upcoming.yaml` was due 09-15 on month-level precision and
stays pending, no flip warranted), general AI-debt/private-credit
issuance (no new dated-09-18 deal found beyond the already-logged
Oracle/Blue Owl and Meta/Blue Owl facilities), Intel/SK Hynix (still no
confirmed deal beyond both companies' "no plans finalized" statements,
Intel shares continuing to trade on the speculation alone), and Oracle/
Stargate/CoreWeave (no evening-window news).*

## ⏳ Upcoming & expected

**No flips this pass.** `attention/upcoming.yaml` swept again for
anything due in the next 7 days within this lens's tracked threads:
`france-draft-finance-bill-0930` (due 09-30, no fresh development) and
`iran-hormuz-restricted-zone-boundaries` (due 09-21, thread
`red-sea-oil-shock`, no boundaries or enforcement action found this
pass) are the only two in range beyond the Nvidia item noted above.
Separately — outside this lens's own threads but flagged since the
brief asked for it by name — `ofac-gl-cc-winddown-0919` (thread
`iran-conflict-widening`, a world-news thread, not one of this lens's
21) is due tonight: OFAC General Licence CC's wind-down authorization
for transactions with Golden Global Yatirim Bankasi and two affiliated
Turkish entities expires at 12:01 a.m. EDT 09-19 by operation of law;
no news of an extension, a further designation, or a Turkish
government response was found this pass. Worth a same-day check by
whichever agent owns `iran-conflict-widening` once the deadline has
passed.

## 🔄 Map changes

- Two new dated timeline entries written this pass: `red-sea-oil-shock`
  (oil's round trip) and `cross-border-rates` (the yen's break above
  ¥157) each got a new `## 2026-09-18` block, and
  `datacenter-backlash-capital-risk` got a new `## 2026-09-18` block for
  Virginia's framework (`sev=major` on the digest bullet — a
  first-of-kind state-level regulatory framework, not just another
  local fight, landing in the single state with the most physical AI
  capital already deployed). `softbank-all-in`, `intel-rescue`, and
  `chips-equity-pivot` got ambient digest-bullet coverage only (`axis=`
  tags), no new timeline block, since neither the SoftBank close-price
  reaction nor the Intel/SK Hynix price momentum constitutes a new
  dated fact beyond what's already on those threads' most recent
  entries.
- The morning pass's WebSearch-budget exhaustion did not recur this
  pass; this afternoon sweep ran within budget on WebSearch plus
  `python3 urllib` for pages that 403 WebFetch (CNBC's oil page, in
  particular — confirmed the 403 is Cloudflare, not a dead page, by
  fetching it successfully via urllib with a browser user-agent).

## 🧵 Thread candidates

**Two, proposed to the main session, not opened here (out of this
agent's write scope):**
- **Manus (Chinese AI agent startup)** is raising $500M at a $4B
  valuation — its first round since Beijing's National Development and
  Reform Commission blocked a Meta acquisition on national-security
  grounds in April, with IDG Capital, Boyu Capital, CATL, Tencent and
  others reportedly in the round, and Manus said to be weighing a Hong
  Kong IPO. Doesn't cleanly fit any of this lens's 21 assigned
  threads (adjacent to `frontier-lab-ipos` and `china-stack-
  independence`, world-news lens, but distinct from both — a Chinese
  AI *agent* startup's financing, not a frontier-model lab's). ([TechCrunch](https://techcrunch.com/2026/09/18/manus-seeks-4b-valuation-in-new-500m-fundraise-as-it-resumes-independent-ops/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-17/manus-eyes-4-billion-value-in-first-round-since-meta-breakup))
- **Family-office AI investment demand** — TechCrunch (09-18, in the
  day's RSS buffer) reports family offices "clamoring" for direct AI
  investments, a capital-source category distinct from `asset-managers-
  build-ai`'s institutional/SWF focus. Not chased further this pass
  (outside the 10:00-15:00 window's priority list) but flagged as a
  possible sub-thread or a widened watch on the existing thread. ([TechCrunch](https://techcrunch.com/2026/09/18/family-offices-are-clamoring-for-ai-investments/))

---

Virginia's governor signed the country's most aggressive state
data-center regulatory framework and launched a new AI task force, on a
triple-witching Friday where US equities closed little-changed (S&P
7,627.99, -0.13%) still digesting Wednesday's Fed hike, with the 10-year
and 30-year Treasury yields both closing at their highest since 2007
(5.01% and 5.34%). The Bank of Japan's overnight hike to 1.25% weakened
the yen further rather than strengthening it, USD/JPY breaking above 157
to a two-week high intraday before settling back to close at ¥156.87, on
a split 7-2 board vote, without spooking Asian equities — the Nikkei
rallied 1.5-2% and chipmakers led on Nvidia's Jensen Huang forecasting a
doubling of chip sales next year. Oil resumed its slide into the close
after an intraday round trip: a fourth straight down session in Asian
trading (Brent to about $102.57) recovered to roughly $104.34 during the
US session as Saudi Arabia and Yemen's Houthis traded fresh cross-border
attacks Thursday, then fell back again to settle at $103.87. SoftBank
added a fourth simultaneous financing lever to the pile this map has
tracked all week, increasing its Arm-backed margin loan from $20bn to
$25bn on oversubscribed demand and closing its Tokyo session up 2.56% —
one more slice of the same concentrated AI bet pledged a different way.
Late Friday, Paramount and the 12 states suing to block its $110bn
Warner Bros. Discovery acquisition moved toward a possible settlement,
sending both companies' shares up sharply after hours.

## Appendix — Coverage check vs. benchmarks

**They led with → we missed:** No confirmed miss. Money Stuff carries no
Friday edition (confirmed against its own author-page RSS history — a
consistent Mon-Thu publishing pattern going back to early August, not a
one-off gap), so 09-18 is not applicable to check against it. FT
Unhedged's 09-18 edition ("The QT endgame at the BoE," pubDate Fri 18 Sep
2026 05:30 GMT) confirmed to exist via RSS; its subject (Bank of England
QT) is outside what this lens's US/Asia-focused 09-18 coverage would have
carried regardless, and the body is paywalled past the dek with no
reader-proxy access this pass — logged checked-not-a-miss. Axios Pro
Rata and Bloomberg Technology were not checkable at all this pass — both
direct-URL and `r.jina.ai` reader-proxy access 403'd on every attempt, a
harder block than either's prior same-day-only or stale-cache failure
mode. A wire backstop (WebSearch for Reuters/Bloomberg 09-18 roundups)
surfaced nothing beyond what's already in this digest.
**Both covered:** N/A — no benchmark comparison was reachable beyond FT
Unhedged's existence check above.
**We had → they didn't:** Virginia's data-center framework, the SoftBank
Arm-margin-loan increase, the Nvidia/Huang chip-doubling comments,
Berkshire's chairman succession, Friday's final US close (added at this
finalize pass, correcting this digest's own earlier provisional reads),
and the Paramount/Warner Bros. Discovery settlement-talks story — none
checkable against any of the four named benchmarks this pass. Full
transport detail in `coverage-log.md`'s 2026-09-19 entry.
