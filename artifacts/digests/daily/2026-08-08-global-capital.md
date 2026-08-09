---
lens: global-capital
date: 2026-08-08
status: final
window_start: 2026-08-08T05:00:00-04:00
as_of: 2026-08-08T23:59:00-04:00
coverage: done
---

# Global Capital — 2026-08-08

*RECONSTRUCTED 2026-08-09 — no `/daily` ran on 2026-08-08 at all; this
digest did not exist until now. Built from scratch against
`buffer/2026-08-09-*.jsonl`'s wide catch-up sweep (`--since
2026-08-07T15:08:00Z`, filtered to lens=global-capital and bucketed to
this digest-day by real timestamp, 5am→5am ET), cross-checked with
WebSearch/WebFetch against primary and reputable secondary outlets
(CNBC, Fortune, Forbes, Reuters, Al Jazeera, USNews, NPR, CNBC, Yahoo
Finance, TradingEconomics). Because this is a same-pass finalize on a
reconstructed day, sourcing is held to the same bar as a live-day
digest — no bullet below runs on a single low-tier aggregator alone
where a better source existed.*

## Today's throughline

**Berkshire Hathaway's Q2 earnings were the day's real event — Greg
Abel ended a 14-quarter net-selling streak, deploying $10B into Alphabet
(pointedly, an AI-infrastructure-linked stake) and $4.5B into buybacks,
while net profit doubled to $25.7B.** It landed the same week Alphabet
itself went to raise up to $25B more in debt for AI capex — Berkshire's
"smart money" equity bet and Alphabet's own balance-sheet lever pulling
in the same direction, on the same stock, in the same week. Underneath
it: Kevin Warsh's forward-guidance-removal framework kept dominating Fed
coverage (FT: he'd still hike in September on hot inflation, but
September-hike odds slipped from ~68% to ~58% priced); Iran's IRGC hit a
16th ADNOC tanker with a missile in the Strait of Hormuz, a real
escalation but one inside the five-month war capital-context.yaml
already tracks, not a new one; and South Korea's SK Hynix-led selloff,
which had triggered a brief pre-market flash crash, began easing as
leveraged trades unwound.

---

## Capital in my markets

- **Berkshire Hathaway's Q2 2026 earnings marked the clearest break yet from Warren Buffett's cash-hoarding era: net profit doubled to $25.7B (from $12.4B), operating earnings rose to $13.0B, and CEO Greg Abel became a net buyer of stocks for the first time in 15 quarters — purchasing $23.5B of equities against $3.7B sold.** The single largest move: a $10B stake build in Alphabet, which surged 224% in Berkshire's portfolio in one quarter to become its 5th-largest holding, explicitly tied to Alphabet's AI-infrastructure investment rather than a generic value bet. Buybacks resumed at $4.5B for the quarter (more than $3.3B continuing into July). Cash and T-bills actually ticked down only modestly — $344.1B at June 30 vs. $347.7B at March 31 — meaning the ~$500B headline cash-pile framing several outlets used overstates how much was actually deployed; Abel spent real money, but the pile is still enormous.
  ([CNBC](https://www.cnbc.com/2026/08/08/berkshire-hathaway-earnings-q2-2026.html), [Fortune](https://fortune.com/2026/08/08/berkshire-hathaway-cash-pile-10-billion-alphabet-stock-brk-repurchasei-greg-abel-warren-buffett/), [Forbes](https://www.forbes.com/sites/bill_stone/2026/08/08/berkshire-hathaway-earnings-beat-as-abel-deploys-buffetts-cash-hoard/))
  <!-- k: t=berkshire-ai-capital-stance axis=capital-in-my-markets interp=yes -->

- **Kevin Warsh's own position on the September meeting hardened even as markets priced a lower hike probability: FT reports he's sticking with his lean-messaging approach but would still raise rates in September if the coming inflation readings run hot.** Market pricing moved the other way — odds of a September hike eased from ~68% to ~58% over the week, per rate-futures pricing — meaning the market is betting against exactly the outcome Warsh says he's still willing to deliver. The 10Y yield reflected the tension: ~4.64% at Friday's (08-07) midday jobs-reaction low, drifting back up toward ~4.68-4.69% by 08-08 as the "no forward guidance" regime left investors re-pricing continuously rather than off a single signal.
  ([TradingEconomics](https://tradingeconomics.com/united-states/government-bond-yield))
  <!-- k: t= e=kevin-warsh axis=capital-in-my-markets -->

- **Iran's Revolutionary Guard hit a UAE state-oil tanker with a missile in the Strait of Hormuz — the 16th attack on an ADNOC vessel since the war began, not a new front.** UAE state media (WAM/ADNOC) confirmed the strike, no injuries; the UAE foreign ministry called it "piracy" and a violation of UN Security Council Resolution 2817, and Qatar joined the condemnation. ADNOC's own running count: 15 of its vessels attacked by missiles/drones transiting the strait since the war began, three of them this week alone, one crew member killed and 20 injured across the campaign. This extends the standing conflict `capital-context.yaml`'s `conflict_risk_premium` reading already prices — a real, sourced escalation, but inside the five-month war, not a new theatre or combatant per the flash-rail bar (assessed below in this report, not applied to `attention/flash.yaml`).
  ([Al Jazeera](https://www.aljazeera.com/news/2026/8/8/uae-says-iran-targeted-adnoc-tanker-in-hormuz-no-casualties-2), [The National](https://www.thenationalnews.com/news/mena/2026/08/08/uae-and-qatar-condemn-iranian-strike-on-adnoc-oil-tanker/))
  <!-- k: t=red-sea-oil-shock axis=capital-in-my-markets -->

- **South Korea's SK Hynix-led selloff began easing as roughly $1.4B in leveraged trades unwound, a day after a brief pre-market "flash crash" (a 30%-limit-down print on an alternative exchange that lasted under an hour) rattled the KOSPI.** The rout traces to Wall Street spillover — SanDisk's strong earnings but soft guidance sparked broader memory-sector jitters — layered onto South Korea's own leveraged-ETF exposure to AI/semiconductor names. This is the market-structure cousin of the CXMT/DRAM-pricing story (above, 08-07): the same memory-shortage dynamics that give CXMT pricing power are also what's making SK Hynix/Samsung swing hardest on every AI-sentiment wobble.
  ([CNBC](https://www.cnbc.com/2026/08/06/asia-tech-selloff-wall-street-samsung-sk-hynix.html))
  <!-- k: t=chip-hyperscaler-rotation axis=capital-in-my-markets -->

## Deals & filings / Power & lobbying

- **Alphabet is raising up to $25B in fresh debt for AI infrastructure — its third major bond sale of 2026, taking total 2026 debt raised toward $70B on top of nearly $85B in equity issuance earlier in the year — in the same week Berkshire bought a $10B AI-infrastructure-linked equity stake in the company (above).** Maturities reportedly span two to 40 years. Alphabet's AI capex is tracking toward ~$190B for the year. Two "smart money" signals pointing opposite directions on the same balance sheet: Berkshire's equity purchase reads as a bet the AI buildout pays off; Alphabet's own accelerating reliance on debt (rather than its own enormous cash generation) to fund that buildout is exactly the financing-structure question `ai-circular-financing-risk` and `ai-trade-bear-turn` have been asking about every other AI capex name.
  ([Yahoo Finance/Quiver Quantitative](https://www.quiverquant.com/news/Alphabet+Targets+Up+to+$25+Billion+Bond+Sale+Amid+Rising+AI+Infrastructure+Spending), [Globe and Mail](https://www.theglobeandmail.com/investing/article-alphabet-25-billion-bond-sale-ai-build-out/))
  <!-- k: t=berkshire-ai-capital-stance,ai-circular-financing-risk axis=deals-and-filings interp=yes -->

- **CoreWeave expanded its AI-cloud partnership with quant trading firm IMC to a materially larger capacity commitment, three days ahead of its 08-11 Q2 earnings — the second confirmation this week that quantitative-finance demand, not just AI-lab demand, is a real leg of CoreWeave's backlog.** Flow Traders has already standardized on CoreWeave; Jane Street's existing $6B platform commitment plus its $1B equity stake and a planned $11B refinance were already on this thread's record. Financial-sector customers diversify the backlog away from the OpenAI/Meta concentration this thread has flagged as the real risk — worth weighing directly against Tuesday's earnings print.
  ([Yahoo Finance UK](https://uk.finance.yahoo.com/news/coreweave-crwv-wins-bigger-ai-011203516.html))
  <!-- k: t=coreweave-backlog-bet axis=deals-and-filings -->

## 📊 Macro strip

- **10Y yield: ~4.68-4.69%**, up from Friday's ~4.64% midday jobs-reaction
  low as the relief rally partly faded and Warsh's still-open-to-a-hike
  stance (above) re-entered pricing.
- **September rate-hike odds: ~58% priced**, down from ~68% earlier in
  the week — moving opposite to Warsh's own stated openness to hiking if
  inflation runs hot, the gap this digest is watching into 09-16.
- **10Y-2Y spread: 0.44** (FRED, 2026-08-06 — no newer FRED read
  surfaced this pass either; still the standing figure, now three real
  data points stale — the jobs print, Warsh's guidance framework, and
  today's Berkshire/Alphabet AI-financing news all postdate it).
- **Brent crude:** no new EOD close independently confirmed for 08-08 in
  this pass (see 08-07's revised $83.48 close); the UAE tanker strike
  (above) is the session's clearest upward pressure point in the absence
  of a confirmed print — flagged rather than guessed.

## ⏳ Upcoming & expected

- No `upcoming.yaml` entries hit their `due` date on 08-08 for this lens.
- 💡 **`berkshire-q2-2026-13f` (due 2026-08-14) — substantively
  pre-answered today, not yet formally hit.** The claim asks whether
  "the Alphabet position kept growing and whether any other AI-adjacent
  equity appears" — today's earnings release already discloses exactly
  that (Alphabet up 224% to the 5th-largest holding, explicitly
  AI-infrastructure-tied). The 13F itself (the actual regulatory filing
  this expectation is keyed to) hasn't been filed yet. Recommend: leave
  `pending` until the 13F files, but this is effectively confirmed in
  substance — a genuine case of the underlying fact landing before its
  tracked instrument does.
- Next 7 days: `coreweave-q2-earnings` 08-11 (context above) ·
  `iran-oman-hormuz-deal-signing` ~08-12 · `berkshire-q2-2026-13f` 08-14
  (see above).

## 🔄 Map changes

- `~ threads/berkshire-ai-capital-stance` — real, major development (Q2
  earnings, Alphabet stake build, buyback resumption); timeline entry
  written.
- `~ threads/coreweave-backlog-bet` — real development (IMC capacity
  expansion ahead of 08-11 earnings); timeline entry written.
- `~ threads/red-sea-oil-shock` — real development (UAE ADNOC missile
  strike, 16th attack on an ADNOC vessel); timeline entry written.
- `~ threads/chip-hyperscaler-rotation` — real development (SK Hynix
  selloff easing, leveraged-trade unwind); timeline entry written.
- `~ ai-circular-financing-risk` — ambient bump (Alphabet debt raise is
  relevant context, folded into the berkshire-ai-capital-stance bullet
  above rather than carrying its own entry).
- `~ softbank-all-in` · `oracle-stargate-bet` · `nvidia-vendor-financing`
  — ambient bump only; SoftBank's Q1 FY27 earnings coverage (profit
  drop) and Oracle's recycled AI-spending-concern coverage didn't clear
  the bar for a dedicated bullet (nothing beyond what's already on
  record for either thread).

## 🧵 Thread candidates

- None new. Yesterday's `Fed independence fight` candidate (Trump vs.
  Lisa Cook) stands unanswered from the 08-07 digest — carrying forward
  rather than re-offering.

---
Berkshire Hathaway's Q2 earnings were the headline: Greg Abel ended a
14-quarter selling streak, put $10B into Alphabet as an explicit
AI-infrastructure bet, and doubled net profit to $25.7B — landing the
same week Alphabet itself went to borrow up to $25B more for AI capex.
Underneath it, Kevin Warsh said he'd still hike in September on hot
inflation even as the market priced lower odds of exactly that, Iran hit
a 16th ADNOC tanker in the Strait of Hormuz without opening a new front,
and South Korea's chip-selloff scare began unwinding.

## Appendix — Coverage check vs. benchmarks

*Critic pass run 2026-08-09, checking Money Stuff (Matt Levine), Axios
Pro Rata, FT Unhedged, and Bloomberg Technology for 2026-08-08 coverage.
Same access picture as 08-07's appendix: Money Stuff, Axios Pro Rata and
FT Unhedged are paywalled and not independently fetchable for this
specific date in this environment. Berkshire's earnings, however, were
covered so broadly across reputable outlets (CNBC, Fortune, Forbes,
Reuters via multiple wires) that this critic pass treats that broad
convergence as a reasonable proxy for "did the major financial press
lead with this" even without direct access to the three named
newsletters.*

**They led with → we missed:** nothing identified — Berkshire's earnings
were the dominant story across every reachable outlet, and this digest's
lead bullet covers it in comparable or greater depth (the $344.1B actual
cash figure, not just the "~$500B pile" headline several secondary
aggregators repeated uncorrected).

**Both covered:** Berkshire/Abel's Alphabet bet and buyback resumption;
the broader "AI capex funded by debt" financing-structure question
(Alphabet's bond raise landing the same week is the kind of juxtaposition
Money Stuff's structure-focused beat would very plausibly have flagged,
but that can't be confirmed without access).

**We had → they didn't (per what's checkable):** the CoreWeave/IMC
capacity-expansion detail and the UAE ADNOC missile-strike figure (16th
attack, 15 vessels, one death) are more specialized than general
market-earnings coverage — genuinely additive, not just duplicative.