---
lens: global-capital
date: 2026-08-07
status: final
window_start: 2026-08-07T05:00:00-04:00
as_of: 2026-08-07T23:59:00-04:00
coverage: done
---

# Global Capital — 2026-08-07

*Finalized 2026-08-09 (two days late — no `/daily` ran 08-08; this is the
catch-up run). Original morning draft was a tier-2 agentic-interim sweep
against BLS primary + Google News RSS. This finalize pass re-curates
against the full day: `buffer/2026-08-09-*.jsonl`'s wide catch-up sweep
(covering back to 08-07T15:08 UTC) filtered to lens=global-capital and
bucketed to this digest-day, cross-checked with WebSearch against primary
outlets (NPR, Washington Post, EA/PIF official releases, Yahoo/AP,
techjuice/macdailynews, TechCrunch/Seeking Alpha). Jobs figures remain
BLS-primary; the market-reaction and Fed-independence items below are the
day's full-day additions.*

## Today's throughline

**The July jobs report landed as the day's real capstone, and it broke
the wrong way for anyone reading Warsh's Fed as settled into its hawkish
hold — and by day's end it wasn't even the only pressure on that
committee.** Nonfarm payrolls fell 23,000 — not a soft beat but an
outright decline, against a market expecting +83-85k — and May/June were
revised down a combined 103,000 on top of it. Layered onto a committee
that just went from a unanimous hold in June to a 9-3 vote with three
dissents *for a hike* in July, on an already stagflation-adjacent Q2
(GDP +1.5%, PCE 3.7%/3.3%), this is the single data point most likely to
reopen the FOMC's internal argument before 09-16. Then, separately,
Trump revived his effort to remove Fed Governor Lisa Cook on a hard
three-week deadline — pressure on the committee's composition, not just
its messaging, and a fight this map had never tracked before today.
Underneath both: SpaceX moved to formally close its $60B Cursor
acquisition on top of its insider-unlock story, Saudi PIF's $55B
Electronic Arts buyout closed at a concentrated 93.4% direct ownership
(with Jared Kushner's Affinity Partners a small co-investor), the
government's chipmaker equity portfolio grew to 30 companies, and the
CXMT-probe-letter this map waited on since 07-28 never arrived and has
now flipped passed-silent.

---

## Capital in my markets

- **July nonfarm payrolls fell 23,000 — a genuine decline, not a soft
  beat — against consensus of roughly +83-85k, alongside a combined
  103,000-job downward revision to May and June.** Unemployment held at
  4.1% (6.9M unemployed). May was revised from +129,000 to +63,000;
  June from +57,000 to +20,000 — two consecutive months of what looked
  like moderate hiring turn out to have been much weaker. Average hourly
  earnings rose 2 cents to $37.62 (+3.2% YoY). Weakness concentrated in
  local-government education (-50,000), retail trade (-19,000), and
  financial activities (-14,000); health care still added 22,000 but at
  half its prior 12-month pace. **Reaction was too fresh to be indexed
  at this item's 08:44 ET check — see the midday-extension item below
  for the market's first verdict.** This is the print the standing `rate_regime` reading gets
  reweighed against: a committee that moved from unanimous (June) to
  9-3-with-3-hawkish-dissents (July) now has a negative payrolls print
  with a triple-digit-thousand revision in front of it before 09-16.
  ([BLS](https://www.bls.gov/news.release/empsit.nr0.htm))
  <!-- k: t= e=kevin-warsh axis=capital-in-my-markets sev=major interp=yes -->

- **Markets read the payrolls shock as hike-relief, not recession — a
  broad rally led by the Nasdaq (+1.03%), with the Dow briefly touching
  an all-time high, on "quells rate-hike fears" framing (midday
  extension, ~10:51 ET).** S&P 500 +0.49% (7,747.67), Dow +0.20%
  (53,992.41, off an earlier >400-point spike), 10Y yield down ~3bp to
  ~4.64% (single-source figure, direction consistent). The distinction
  that matters: coverage attributes the rally by name to reduced odds
  the 9-3 committee HIKES ("US stocks gain as surprise payrolls fall
  quells rate-hike fears" — Reuters; rate futures "cut chances of
  September rate hike"), not to a fresh September-cut bet — hike-relief
  and cut-pricing are related but distinct claims, and today's sourcing
  supports only the former. **Zero on-the-record Fed-official or
  administration reaction to this print existed as of the check** — the
  three July hawkish dissenters' only dated statements remain their
  pre-print dissent justifications (07-30/31). Re-check next run.
  ([Reuters via Google News](https://news.google.com/rss/search?q=stocks+payrolls+rate+hike+fears), [BLS](https://www.bls.gov/news.release/empsit.nr0.htm))
  <!-- k: t= e=kevin-warsh axis=capital-in-my-markets -->

- **SpaceX's insider lockup closed its first trading day up, not down —
  and no Form 4s or other insider-sale filings have surfaced as of this
  morning's check.** SPCX dipped to a new post-IPO low of $105.11
  intraday yesterday before recovering to close +2.6% at $111.17 (the
  08-06 close, checked this morning); the most recent listed insider
  transaction remains Musk's April 2026 sale. This extends rather than
  changes yesterday's read: the 911.5M-share tranche that unlocked 08-06
  is eligible to sell, but the absence of any actual filing keeps this a
  ceiling-not-evidence story for a second day. The larger 455.8M tranche
  stays locked (needs SPCX above $135; it closed under $112).
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-06/spacex-shares-steady-after-100-billion-insider-lockup-expires), [MarketBeat insider-trades](https://www.marketbeat.com/stocks/NASDAQ/SPCX/insider-trades/))
  <!-- k: t=spacexai-public-megacap e=spacex axis=capital-in-my-markets -->

- **The Iran-Oman Hormuz deal moved from "agreed in principle" to "joint
  statement in final drafting," per Iran's own framing — still not a
  signed deal.** CBS News (08-07) has Tehran saying the deal is "getting
  close"; Bloomberg (08-05/06) already had Iran calling it "agreed in
  principle." Brent traded $81.69/bbl at this morning's check, before
  closing the day at $83.48 (macro strip below) as Houthi strikes widened
  through the session. Genuine incremental movement, not the signing —
  the ledger expectation (due ~08-12) stays pending.
  ([CBS News via Google News](https://news.google.com/rss/search?q=Iran+Hormuz+deal), [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-06/iran-says-deal-with-oman-on-strait-of-hormuz-agreed-in-principle))
  <!-- k: t=red-sea-oil-shock axis=capital-in-my-markets -->

- **SpaceX formalized its $60B all-stock acquisition of AI coding startup
  Cursor in a merger agreement now on file, with Cursor telling staff a
  close could land within days — the deal itself dates to a June
  announcement, but this week is the first firm move toward actually
  closing it.** Cursor crossed $1B in annualized revenue in November and
  will fold directly into SpaceXAI's structure rather than run
  independently; some of its tools may end up carrying the Grok brand.
  The mechanism is the same one funding the rest of this thread: SpaceX's
  own post-IPO stock, still trading below its $135 IPO price, is the
  acquisition currency — a second AI-lab-sized bet bought with paper from
  a company whose market cap is itself an AI story.
  ([TechCrunch](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/), [Seeking Alpha](https://seekingalpha.com/news/4629527-cursor-says-spacex-deal-could-be-done-by-end-of-next-week---report))
  <!-- k: t=spacexai-public-megacap e=spacex axis=capital-in-my-markets -->

## Deals & filings / Power & lobbying

- **The CXMT-national-security-probe letter this map has been waiting
  on since 07-28 still hasn't materialized — the only letter that
  actually landed went to Apple instead, over a week ago.** A bipartisan
  Senate group (Banks R-IN, Schumer D-NY, plus Kim, Shaheen, Crapo,
  Ricketts) sent Tim Cook a letter dated 07-29/30 demanding Apple commit
  to never using CXMT or YMTC memory chips in any product worldwide,
  citing both companies' presence on an updated Pentagon list of
  China-military-linked entities; reply due 08-21. Different target (a
  buyer, not the administration) and a different ask — it doesn't
  satisfy the tracked claim, which stays pending inside its
  week-precision window. Separately, the CXMT Entity List addition
  remains the June-dated postponement already on record (trade-talks
  context); no new movement found today.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-29/senators-warn-apple-not-to-buy-memory-chips-from-chinese-firms), [Sen. Schumer](https://www.schumer.senate.gov/newsroom/press-releases/citing-core-national-security-and-economic-reasons-schumer-demands-apple-reject-chinese-military-linked-chips))
  <!-- k: t=cxmt-memory-ipo e=cxmt axis=deals-and-filings interp=yes -->

- **The DRAM-price story this thread flagged 08-05 (then only PANews/Digital-Daily sourced, no tier-1 wire pickup) got real corroboration this week — MacDailyNews and TechJuice independently confirm CXMT rejected Apple's bid for a discounted price, quoting the same rates Samsung and SK Hynix already charge.** Apple had spent months trying to qualify CXMT as a fourth LPDDR5X supplier (clearing Pentagon-list complications along the way); CXMT walked away because Huawei, Xiaomi and other Chinese OEMs had already locked its output into long-term deals at market rates, leaving no spare capacity and no reason to discount. Two fronts, one company, one week: Congress (above) wants Apple to swear off CXMT/YMTC entirely, while Apple's own procurement team was independently negotiating with CXMT and lost on price, not principle. New this pass: TSMC is reportedly sitting on ~$1B of finished A20 Pro chips it can't complete without matching DRAM — the iPhone 18 Pro supply risk this thread has tracked since 07-22 is now a live mechanism, not a hypothetical.
  ([MacDailyNews](https://macdailynews.com/2026/08/06/chinas-cxmt-rejects-apples-price-cut-demands-for-dram-boosting-samsung-and-sk-hynixs-pricing-power-amid-global-shortage/), [TechJuice](https://www.techjuice.pk/apple-and-cxmt-reportedly-fail-to-agree-on-dram-pricing/))
  <!-- k: t=cxmt-memory-ipo e=cxmt axis=deals-and-filings -->

- **Saudi Arabia's PIF-led consortium's $55B buyout of Electronic Arts is now fully closed, and this week's coverage sharpened a detail the September announcement didn't emphasize: PIF alone holds 93.4% of the company outright, not a diversified three-way split.** Silver Lake holds 5.5%; Jared Kushner's Affinity Partners — a small but direct co-investor — holds 1.1%. The deal (closed 2026-08-04 at $210/share cash) is the largest private-capital-funded buyout on record; EA is now delisted from Nasdaq and fully private. Both facts matter for how this map reads PIF: this is concentrated sovereign ownership, not a passive LP stake, and it sits in the same capital stack as a sitting US President's son-in-law's fund.
  ([EA official](https://www.ea.com/news/ea-announces-completion-of-acquisition), [Gulf News](https://gulfnews.com/business/markets/saudi-arabias-pif-led-consortium-buys-electronic-arts-ea-for-55-billion-1.500287836))
  <!-- k: t= e=pif axis=deals-and-filings -->

- **The federal government's chipmaker equity-stake program grew again — six more semiconductor firms signed letters of intent for CHIPS Act funding in exchange for "minority, non-controlling" equity, taking the government's total stock portfolio to 30 companies.** The new tranche (GlobalFoundries plus five smaller/earlier-stage firms — Kepler, Multibeam, Extropic, Thintronics, Obsidia Semiconductors, Aeluma) draws on up to $874M from the 2022 CHIPS Act. The government's cumulative position across all 30 deals is now ~$26.7B, still headlined by the Intel stake (9.9% at announce, now worth ~$42B on paper) this map already tracks on `intel-rescue`/`chips-equity-pivot`. GlobalFoundries — already on the expectations ledger for its 2026-11-04 earnings — is now also a direct government equity holder going into that print.
  ([Yahoo Finance/AP](https://finance.yahoo.com/markets/article/trump-administration-adds-6-chipmakers-to-the-governments-stock-portfolio-which-now-spans-30-companies-140535555.html))
  <!-- k: t=chips-equity-pivot axis=deals-and-filings -->

- **Trump revived his effort to remove Fed Governor Lisa Cook, a month after the Supreme Court blocked the first attempt — this time built to survive the Court's own procedural test.** The June ruling (5-4) held Trump couldn't remove a sitting Fed governor without due process; this week's White House letter revives the same unproven 2025 mortgage-fraud allegations but explicitly gives Cook 21 days (to August 26) to submit evidence or argument before any action — the notice-and-response step the Court required. Cook's attorney called the allegations "as baseless now as they were a year ago." **Not currently tracked on any thread or watchlist entity — Lisa Cook has never appeared in `attention/` before this.** This lands three days after the jobs shock reopened the FOMC's internal argument and inside Warsh's own low-guidance framework (below): a fresh push on the Fed's board composition, not just its messaging, with a hard 08-26 deadline this map should now watch.
  ([NPR](https://www.npr.org/2026/08/07/nx-s1-5925167/trump-lisa-cook-federal-reserve), [Washington Post](https://www.washingtonpost.com/business/2026/08/07/white-house-revives-bid-remove-fed-lisa-cook-over-mortgage-claims/))
  <!-- k: t= axis=deals-and-filings interp=yes -->

## 📊 Macro strip

- **Brent crude: $83.48/bbl EOD close (+1.2%)** — revised at finalize
  from the $81.69 morning-check figure; the full day's Houthi strikes on
  Saudi-backed forces in Marib/Hadramout plus Hormuz-transit uncertainty
  pushed it higher through the session. IEA separately called this "the
  largest-ever oil supply disruption" tied to the Middle East war.
- **10Y-2Y spread: 0.44** (FRED, 2026-08-06 — still the freshest FRED
  read as of this finalize; FRED's own update lag means 08-07's spread,
  which would reflect the jobs print directly, isn't in yet).
- **10Y yield: ~4.64% midday** (down ~3bp on the jobs shock), separately
  reported drifting back up toward ~4.68-4.69% into 08-08 as September
  rate-hike odds eased only partway (from ~68% to ~58% priced).
- **July payrolls: -23,000; unemployment 4.1%.** Full-day reaction: relief
  rally held (Nasdaq +1.03%, Dow briefly at an all-time high), "quells
  rate-hike fears" framing stuck — still no on-the-record Fed-official
  reaction to the print itself by end of day.

## ⏳ Upcoming & expected

- ✅ **`jobs-report-july-0807` — hit.** BLS released on schedule 08:30
  ET; -23,000 payrolls, 4.1% unemployment, -103k combined revisions.
- ⚠️ **`cxmt-congress-letters` — passed-silent (flipped since the morning
  draft).** Due 08-07 (week-precision); no administration-facing letter
  ever materialized — only the Apple letter (a different target, a
  different ask) and the commercial DRAM-pricing collapse (above), which
  don't satisfy the tracked claim. Status already flipped in
  `upcoming.yaml`; this finalize just reflects it correctly (the morning
  draft still read "held pending," which was already stale by the time
  this ran).
- Next 7 days: `qwen38-max-open-weights` ~08-10 · `coreweave-q2-earnings`
  08-11 · `berkshire-q2-2026-13f` 08-14 (partially pre-answered by the
  08-08 earnings release — see 08-08's digest) · `iran-oman-hormuz-deal-signing`
  ~08-12 (incremental movement today, above).

## 🔄 Map changes

- `~ threads/spacexai-public-megacap` — real developments (SpaceX lockup
  extension + Cursor merger-agreement formalization); timeline entry
  written.
- `~ threads/red-sea-oil-shock` — real development (Iran-Oman drafting
  update, Houthi Marib strikes, IEA disruption framing); timeline entry
  written.
- `~ threads/cxmt-memory-ipo` — real development (Apple DRAM-pricing
  collapse on top of the Congress-letter miss); timeline entry written.
- `~ threads/chips-equity-pivot` — real development (chipmaker portfolio
  to 30 companies, ~$26.7B cumulative); timeline entry written.
- `~ softbank-all-in` · `nvidia-vendor-financing` · `oracle-stargate-bet`
  · `coreweave-backlog-bet` · `ai-circular-financing-risk` — ambient bump
  only; targeted checks found nothing new beyond what's already tracked
  (Oracle/Nvidia financing: no coverage newer than 07-27).
- `upcoming/jobs-report-july-0807` → **hit** (ben-ledger discipline,
  evidence above).
- `upcoming/cxmt-congress-letters` → **passed-silent** (already reflected
  in `upcoming.yaml`; digest text corrected to match).
- + `board/pif` — Electronic Arts closing detail (93.4% direct PIF
  ownership, not a diversified split) sharpens this actor's holdings
  picture; proposed for main session, not applied here.
- ⚠ Flagged for the next `capital-context.yaml` refresh (`/week` step
  4b, not edited from `/daily`): the `rate_regime` reading is now two
  real data points stale — it predates both the -23k print/103k revision
  AND Warsh's forward-guidance-removal framework, which is now the
  dominant story about how the committee will actually communicate
  between meetings.

## 🧵 Thread candidates

- **candidate: Fed independence fight (Trump vs. sitting Fed governors)**
  — Trump's renewed effort to remove Governor Lisa Cook (above) is the
  second attempt at removing a sitting governor this cycle, now on a
  hard 08-26 deadline, and sits alongside Warsh's own low-guidance
  regime change as a second, distinct pressure on how the Fed actually
  operates. Neither Cook nor "Fed independence" has ever been a
  watchlist entity or thread here despite two weeks of detailed FOMC
  vote-count coverage. Track it? (source: NPR, above)
- SoftBank's Trump-library/Ohio-lease timing story remains folded into
  `softbank-all-in` (no change from the 08-06 call — same actor, same
  campus, not a new thread).

---
July payrolls fell 23,000 against a market expecting a roughly 84,000
gain, with May and June revised down a combined 103,000 — a real miss
landing on a Fed committee that just went from unanimous to three
hawkish dissents in one meeting, and the relief rally held through the
full day. Underneath it: SpaceX moved to formally close its $60B Cursor
acquisition, Saudi PIF's $55B Electronic Arts buyout closed at 93.4%
direct ownership, the government's chipmaker equity portfolio grew to 30
companies, and Trump revived his effort to fire Fed Governor Lisa Cook on
a hard three-week deadline — a governance fight this map had never
tracked before today.

## Appendix — Coverage check vs. benchmarks

*Critic pass run 2026-08-09, checking Money Stuff (Matt Levine), Axios Pro
Rata, FT Unhedged, and Bloomberg Technology for 2026-08-07 coverage.
Access was the same mixed picture prior appendices have logged: Money
Stuff and Axios Pro Rata are Bloomberg/Axios-paywalled and not
search-indexed for this specific date in this environment — genuinely
unreachable, not a clean-sweep claim. FT Unhedged likewise didn't surface
a fetchable 08-07 issue. Bloomberg Technology's TV segment and published
articles for 08-07 WERE reachable (video description + linked articles),
so that benchmark got a real check.*

**They led with → we missed:** Bloomberg Technology's own 08-07 framing —
["Big Tech Stocks Storm Back as AI Fears Fade and Euphoria
Resumes"](https://www.bloomberg.com/news/articles/2026-08-07/big-tech-stocks-storm-back-as-ai-fears-fade-and-euphoria-resumes) —
was its lead tech-markets piece for the day, crediting accelerating
AI-revenue growth at Microsoft and Amazon as the trigger. This digest's
jobs-report/market-reaction bullets cover the SAME rally but attribute it
to hike-relief, not the Big Tech earnings-acceleration framing Bloomberg
led with — a genuine framing gap, not a missing fact (the rally itself is
covered). Also on Bloomberg Tech's radar and outside this digest
entirely: OpenAI's first consumer hardware device, DeepMind's power
shift, ByteDance's 10-trillion-parameter model — all real, all
`frontier-ai` lens territory, not global-capital's.

**Both covered:** the July jobs report and its Fed-rate-path
implications (Bloomberg Tech's Ed Ludlow segment led with this too);
AI-capex financing pressure generally.

**We had → they didn't (per what's checkable):** the EA/PIF 93.4%
ownership breakdown and Kushner co-investment detail, the chipmaker
portfolio-to-30 figure, and the Lisa Cook renewed-removal deadline are
policy/deal-desk specifics a general tech-markets video segment wouldn't
carry — plausibly Axios Pro Rata or Money Stuff territory if either had
been reachable, but that can't be confirmed either way this run.
