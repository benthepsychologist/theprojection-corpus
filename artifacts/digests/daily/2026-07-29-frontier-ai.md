---
lens: frontier-ai
date: 2026-07-29
status: final
window_start: 2026-07-29T05:00:00-04:00
as_of: 2026-07-30T06:30:00-04:00
coverage: done
---

# Frontier AI — 2026-07-29

*Curated from the 12-collector run (google-news + rss + gdelt + sec_edgar +
openalex + semantic_scholar + github + the tier-2 wave) plus 5 tier-2
cluster agents — extended overnight with the four-print earnings
gauntlet, 1 tier-2 agent (agentic-interim). Finalized with a coverage-
critic pass against sources/benchmarks.yaml — see coverage-log.md.*

## Today's throughline

The story moved from the selloff itself to what the selloff means. With
yesterday's Asian rout now scored to 07-28, today's development was the
framing hardening around it — a rotation *out* of chipmakers and *into*
hyperscalers on the fear that AI infrastructure capex is peaking sooner
than assumed. China's DUV tool gained a named maker, Shanghai Aishengna,
and a sceptical read from JPMorgan, but still no delivery to any named
fab — the event that would actually reset that thread.

**Then the four prints answered, and the thesis split in two.** Capex is
not peaking — Meta and Microsoft both guided it higher — but the rotation
away from chips is real, and it runs on monetization proof, not on the
hyperscaler/chipmaker line: Arm and Qualcomm fell on genuinely strong
AI-specific numbers, while Meta fell just as hard on an EPS miss and
near-zero free cash flow, and only Microsoft's 43% Azure growth bought it
relief. Microsoft's named "first" — an OpenAI-vs-own capex split — still
did not happen.

## Product & access

- **Grok Build Mode shipped for SuperGrok Heavy subscribers** — generate and publish apps directly from chat. The day's one real product release; corrects an earlier "nothing shipped" framing (coverage-critic catch, 07-30). ([TLDR AI](https://tldr.tech/ai))
  <!-- k: t=grok-frontier e=xai axis=product-and-access -->

## China

- **Shanghai Aishengna was named as the maker behind China's domestic immersion DUV tool** — founded August 2023, backed by Shanghai Electric Holding and Shanghai International Trust, staffed from SMEE and Yuliangsheng. ([Seoul Economic Daily](https://en.sedaily.com/international/2026/07/29/aishengna-revealed-as-chinese-duv-maker-behind-chip-stocks))
  <!-- k: t=china-duv-lithography,china-stack-independence e=smic axis=china -->
- **JPMorgan put the sceptical case plainly** — "producing a small quantity of DUV equipment and building a mass-production system are entirely different matters"; yield and precision at volume remain unproven. ([Seoul Economic Daily](https://en.sedaily.com/international/2026/07/29/aishengna-revealed-as-chinese-duv-maker-behind-chip-stocks))
  <!-- k: t=china-duv-lithography e= axis=china -->
- **No delivery to any named fab has been confirmed** — coverage still says "expected this year" for SMIC, Hua Hong and CXMT, unchanged from yesterday's announcement. Delivery, not announcement, is this thread's test.
  <!-- k: t=china-duv-lithography e=smic,hua-hong,cxmt axis=china -->
- **China's Commerce Ministry rejected the distillation allegation** as lacking "factual and legal basis" and accused Washington of "AI hegemonism"; no new US enforcement action followed. ([Technology.org](https://www.technology.org/2026/07/28/china-ai-hegemonism-us-distillation-sanctions/))
  <!-- k: t=kimi-distillation-fight,china-stack-independence e=moonshot-ai axis=china -->
- **The industry open letter defending open-weight models reached 132 signatories**, including Amazon, Google and OpenAI. ([Caixin Global](https://www.caixinglobal.com/2026-07-29/moonshot-open-sources-kimi-k3-as-us-china-ai-tensions-intensify-102468927.html))
  <!-- k: t=kimi-distillation-fight e=openai,google-deepmind axis=china -->
- **The US expanded China tech curbs with import bans on Chinese humanoid robots, robot dogs, and solar inverters**, on national-security grounds (coverage-critic catch, 07-30). ([Bloomberg Technology](https://www.bloomberg.com/technology))
  <!-- k: t=china-stack-independence e= axis=china -->

## Capital & corporate

- **The second Korean circuit-breaker session belongs to 07-28's digest, not today's** — it closed 02:30 ET, before the 5am boundary, and is already recorded there; today's 07-29-datelined coverage is reporting that session, not a third one.
  <!-- k: t=ai-memory-shortage,chips-equity-pivot e= axis=capital-and-corporate -->
- **Analysts are framing this as a rotation from chipmakers to hyperscalers** on fear that AI infrastructure capex is peaking faster than expected — Morgan Stanley, UBS and Forrester; BofA dissents and calls it mid-innings. ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/ai-investors-may-pivot-hyperscalers-133026207.html))
  <!-- k: t=chip-hyperscaler-rotation,ai-trade-bear-turn e= axis=capital-and-corporate -->
- **TSMC's Kumamoto fab is structurally intact and restarting in stages** after Tuesday's M7.1 quake, with no resumption date given; the site is under 3% of TSMC capacity. ([Taipei Times](https://www.taipeitimes.com/News/taiwan/archives/2026/07/29/2003861588))
  <!-- k: t=tsmc-capacity-race e=tsmc axis=capital-and-corporate -->

## 🌙 The overnight earnings gauntlet — the strategic read

- **Microsoft's Azure accelerated to 43% constant-currency growth, and
  its named "first" still did not happen** — no OpenAI-vs-own capex
  split disclosed, despite that being the specific thing this thread was
  watching for. FY27 capex guidance stayed qualitative. ([Microsoft IR](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast))
  <!-- k: t=microsoft-capex e=microsoft axis=capital-and-corporate -->
- **Meta's AMD 6GW commitment went unmentioned on the call** — the only
  new infrastructure item was a BlackRock 1GW Texas JV — while capex
  guidance rose again to $130-145B against a near-zero free-cash-flow
  quarter. ([Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-meta-misses-eps-in-q2-2026-as-stock-sinks-after-hours-93CH-4821910))
  <!-- k: t=meta-capex e=meta-ai axis=capital-and-corporate -->
- **Arm's AGI-CPU bookings doubled to more than $2B across FY27-FY28**,
  and data-center royalty revenue more than doubled year-over-year — the
  strongest AI-specific datapoint of the night, undercut by a smartphone-
  royalty guidance cut that still dominated the stock's reaction.
  ([Arm Newsroom](https://newsroom.arm.com/news/arm-q1-fye27-results))
  <!-- k: t=arm-royalty-regime e=arm axis=capital-and-corporate -->
- **Qualcomm's Dragonfly custom-silicon revenue does not start until
  December** — this quarter's guide moved on legacy handset weakness
  instead — but the company raised its FY2029 non-handset target to
  $40B, with more than $15B from data centers.
  ([GuruFocus](https://www.gurufocus.com/news/8988855/qualcomm-inc-qcom-q3-2026-earnings-call-highlights-record-automotive-revenue-and-data-center-ramp-offset-handset-headwinds))
  <!-- k: t=qualcomm-dragonfly e=qualcomm axis=capital-and-corporate -->

## ⏱ Release-watch & markets

- **Nvidia -2.1%** intraday, on the standing guarantee reports rather than new disclosure; CDS eased to ~78bp from Monday's record 82bp, with Oracle now wider.
- **Asian semis** — Kioxia -13.9%, Tokyo Electron -10.6%, SoftBank -7.0%; US after-hours followed with Intel -6%, AMD -8%, Micron -8%, Sandisk -14%.
- **DRAM/NAND contract pricing** — TrendForce still guides Q3 at +13-18% and +10-15% QoQ, a marked deceleration from Q1's 93-98%; no fresher print today.
- **Four prints, all in**: MSFT +8-9% AH, META -8/-11% AH, ARM -7/-8% AH, QCOM -8% AH.

## ⏳ Upcoming & expected

- ✅ **hit — `fomc-july-decision`**: held 3.50%-3.75%, 9-3, three dissents for a hike.
- ✅ **hit — `microsoft-q2-earnings`, `meta-q2-earnings`, `arm-q1fy27-earnings`, `qualcomm-q3fy26-earnings`** — all four reported overnight; see the section above for the verdict on each.
- **New:** `fomc-september-decision` (09-16).
- Next 7 days: `amazon-q2-earnings` and `samsung-q2-breakdown` (both 07-30), `gov-review-framework-announce` (08-01), `eo14409-deadlines` (08-01), `altman-washington-briefing` (07-31).

## 🔄 Map changes

- `~ upcoming/microsoft-q2-earnings` — due corrected **07-30 → 07-29** against two Microsoft primary sources; the 07-28 agent correction that introduced 07-30 was wrong (⟨daily 07-29⟩).
- `~ upcoming/fomc-july-decision` — pending → **hit** (⟨daily 07-29⟩).
- `~ upcoming/arm-q1fy27-earnings` — confidence **reported → confirmed** (⟨daily 07-29⟩).
- `~ upcoming/ca-sb903-assembly` — confidence **confirmed → reported**; the 08-14 date is not bill-specific (⟨daily 07-29⟩).
- `+ upcoming/fomc-september-decision`, `+ upcoming/mn-nudify-ban-effective` (curate-add 07-29).
- `~ threads/microsoft-capex` — watch prose reverted to 07-29 (07-29).
- `+ thread chip-hyperscaler-rotation` (money) — split from `chips-equity-pivot`, whose CHIPS-Act-equity scope didn't fit the rotation trade a tier-2 agent had written into it (ben-steer 07-29).
- `~ threads/chips-equity-pivot` — the 07-29 timeline entry above moved out; `last_seen` reverted to 07-28 (07-29).
- `~ upcoming/meta-q2-earnings`, `~ upcoming/microsoft-q2-earnings`, `~ upcoming/arm-q1fy27-earnings`, `~ upcoming/qualcomm-q3fy26-earnings` — all four pending → **hit**, resolved overnight (⟨daily 07-29⟩).
- `~ threads/meta-capex`, `~ threads/microsoft-capex`, `~ threads/arm-royalty-regime`, `~ threads/qualcomm-dragonfly`, `~ threads/chip-hyperscaler-rotation`, `~ threads/ai-trade-bear-turn` — overnight earnings blocks added (⟨daily 07-29⟩).
- `+ watchlist/Hims & Hers` (mental-health) — critic-add 07-30.
- `~ digest/Product & access` — "nothing shipped" line corrected (Grok Build Mode); China robot/inverter curbs added (critic-add 07-30).

## 🧵 Thread candidates

- **Promoted:** the chips-to-hyperscalers rotation → `chip-hyperscaler-rotation` (ben-steer 2026-07-29, same day it was offered).

## Appendix — Coverage check vs. benchmarks (2026-07-30)

Checked against The Rundown AI, TLDR AI, The Neuron, The AI Daily Brief.
One real miss auto-added (**Hims & Hers**, cross-lens with mental-health —
see that digest's appendix); two log-only items folded in above (China
robot/inverter import curbs, Grok Build Mode). One initial critic flag —
the OpenAI rogue-agent/pacing-letter story as a "new thread" miss — was
**corrected on inspection**: the thread (`openai-agent-security-incident`)
already existed and the story was first captured in 07-28's digest, not
missed on 07-29. Full detail: coverage-log.md, "2026-07-30 — /daily:
2026-07-29 finalized, coverage-critic pass."

---
China's DUV tool got a named maker and a sceptical read, still no
delivery to any named fab. Then four earnings reports answered the
capex-peaking question: capex kept rising at both hyperscalers, but only
Microsoft was rewarded, on visible Azure growth — Meta fell as hard as
the chip names it was supposedly rotating capital away from.
