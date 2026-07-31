---
lens: global-capital
date: 2026-07-31
status: building
window_start: 2026-07-31T05:00:00-04:00
as_of: 2026-07-31T09:15:00-04:00
coverage: pending
---

# Global Capital — 2026-07-31

*Curated from the 18-collector run (`collect.py`) plus 2 tier-2 cluster
research agents covering Grok/xAI/SpaceX/SoftBank and AI financing/
capital markets, each WebSearch/WebFetch-verified against primary
sources. FRED returned no new series values this window; no fresh macro
strip beyond what's already on file.*

## Today's throughline

A broad Tokyo AI/semiconductor rally (Nikkei 225 +4.37%) sent SoftBank to
the exchange's daily limit-up (+12-15%) and Arm +9% overnight — a
one-session snapback from Arm's own guidance-cut selloff two nights
earlier, and independent of SoftBank's own results, which turn out to be
due 08-06, not 07-30 as the ledger had it (a wrong date, corrected, not a
slip). Separately, Google became the third hyperscaler this week to
guarantee a third-party developer's bank debt rather than fund AI
buildout directly — backing Anthropic's own Texas data-center campus,
the same structure Meta/BlackRock and Nvidia/OpenAI used days earlier.
WSJ reported Tesla is weighing a sale of its China business ahead of a
possible Tesla-SpaceX merger; Musk denied it same day. Oil held its range,
no clean new print.

## Capital in my markets — the Tokyo snapback

- **SoftBank shares hit the exchange's daily limit-up (+12-15%, to
  ~5,322 yen) and Arm rose 9% overnight**, part of a broad Tokyo
  AI/semiconductor rally (Nikkei 225 +4.37%, Advantest and Tokyo
  Electron also limit-up) triggered by strong US tech earnings —
  reversing, for one session, the "rotation away from chips" framing
  that closed out 07-29's Arm earnings coverage, and happening
  independent of SoftBank's own still-unreported results.
  ([Bloomberg Japan](https://www.bloomberg.com/jp/news/articles/2026-07-31/TJ0K57KJH6V400), [Nikkei](https://www.nikkei.com/article/DGXZQOFL3119J0R30C26A7000000/))
  <!-- k: t=softbank-all-in,arm-royalty-regime,chip-hyperscaler-rotation e=softbank,arm axis=capital-in-my-markets -->
- **SoftBank's Q1 FY26 earnings date was wrong, not slipped** —
  SoftBank's own IR page shows the briefing scheduled for **2026-08-06**
  (3:30pm JST disclosure, 4:30pm briefing); all Q1 materials still show
  placeholders. The prior 07-30 date traced to a single uncorroborated
  secondary source.
  ([SoftBank Group IR](https://group.softbank/en/event/earnings_2026q1))
  <!-- k: t=softbank-all-in e=softbank axis=capital-in-my-markets -->
- **Brent held its range, ~$90-92/bbl through this morning** — essentially
  continuing 07-30's noisy-but-elevated level, no fresh break in either
  direction; the market hasn't repriced off the new Saudi maritime
  alliance yet (see World News), consistent with how fresh that
  announcement still is.
  ([Fortune](https://fortune.com/article/price-of-oil-07-31-2026/))
  <!-- k: t=red-sea-oil-shock e= axis=capital-in-my-markets -->

## Deals & financing

- **Google guarantees a $15B bank loan backing Anthropic's Texas
  data-center buildout** — a Morgan Stanley-led consortium ($14B bridge
  loan + revolving credit) lending to Nexus Data Centers for a Hubbard,
  TX campus (1.6GW dedicated gas plant, four leases for Anthropic);
  Google takes ~20% project equity for the guarantee, not yet an
  official Google/Anthropic announcement. Third instance this week of a
  hyperscaler guaranteeing a third-party developer's debt rather than
  funding buildout directly — see the interpretation below.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-30/banks-line-up-15-billion-of-debt-for-anthropic-with-google-aid))
  <!-- k: t=google-capex,ai-power-buildout,where-the-capex-lands e=google,anthropic axis=deals-and-financing interp=yes -->
- **WSJ: Tesla weighing a sale/spinoff of its China business ahead of a
  possible Tesla-SpaceX merger — Musk denies it.** Tesla executives were
  reportedly told to prepare options (spinoff/sale/closure) for
  Gigafactory Shanghai; Musk called it "fake news... never even come up
  in a discussion ever" same day, though he's separately declined to
  rule out a Tesla-SpaceX merger this month. Reported-but-denied, not
  confirmed — a new structural narrative for `spacexai-public-megacap`
  regardless of which way it resolves.
  ([Bloomberg pickup of WSJ](https://www.bloomberg.com/news/articles/2026-07-31/tesla-weighs-china-unit-sale-ahead-of-spacex-deal-wsj-says))
  <!-- k: t=spacexai-public-megacap e=tesla,spacex axis=deals-and-financing -->
- **CoreWeave and Qualcomm: nothing new on the tracked threads today** —
  checked directly; every headline in today's sweep either restates an
  already-logged 07-29/07-30 fact (the $2.6B loan's repricing to 5.5pp
  over benchmark, 96-97 cents on the dollar) or is routine
  insider-selling/analyst chatter.
  <!-- k: t=coreweave-backlog-bet,qualcomm-dragonfly e= axis=deals-and-financing -->

## ⏳ Upcoming & expected

- ✅ **hit — `altman-washington-briefing`**: full detail on Frontier AI.
- 🚧 **corrected, not a flip — `softbank-q1-earnings`**: due date moves
  07-30 → 08-06 (was wrong, not a slip).
- 39 expectations on the ledger, 14 hit.

## 🔄 Map changes

- `~ upcoming/softbank-q1-earnings` — due-date corrected 07-30 → 08-06
  (⟨daily 07-31⟩).
- `~ threads/softbank-all-in`, `~ threads/arm-royalty-regime`,
  `~ threads/google-capex`, `~ threads/spacexai-public-megacap` —
  timeline blocks added (⟨daily 07-31⟩).
- `+ artifacts/digests/daily/2026-07-31-global-capital.interp.yaml` —
  first interpretation of the day, on the Google/Anthropic financing
  guarantee (mechanism: off-balance-sheet hyperscaler credit guarantees
  as a response to the elevated long-rate environment).

## 🧵 Thread candidates

- None new today — the CoreWeave/Qualcomm cluster returned nothing
  digest-worthy, and the day's one adjacent financing story (Nscale's
  $1.65B Anyscale acquisition) predates this window's cutoff and doesn't
  map to a tracked thread; not offered.

---
A broad Tokyo AI-chip rally sent SoftBank to limit-up and Arm +9%,
independent of SoftBank's own results — which turn out to be due 08-06,
not 07-30. Google became the third hyperscaler this week to guarantee a
third-party developer's debt rather than fund AI buildout directly,
backing Anthropic's Texas campus. WSJ reported Tesla is weighing a
China-business sale ahead of a possible SpaceX merger; Musk denied it.
