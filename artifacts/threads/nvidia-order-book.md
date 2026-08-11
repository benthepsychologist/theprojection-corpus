---
thread: nvidia-order-book
title: "Nvidia's Order Book"
lens: ai
entities: [nvidia, openai, meta-ai]
opened: 2026-07-24
crawled: 2026-07-24
---

# Nvidia's Order Book — timeline

*Watch:* The demand side of the chip spend — the reported ~$1T Blackwell+Rubin
book (a management aggregate, not audited backlog), who's buying, and where the
constraint has shifted (supply/HBM4, not demand). The circular-financing angle.

## 2026-08-10 — Nvidia recruits Wall Street to finance $500B of demand-side buildout

- **Nvidia partnered with six asset managers — Apollo, BlackRock,
  Blackstone, Brookfield, Goldman Sachs and KKR — on financing
  platforms designed to raise over $500B in third-party capital for AI
  infrastructure, with Jensen Huang saying Nvidia itself can backstop
  up to $125B (25%) of the resulting deals — MOUs, not final
  agreements yet.** Not a chip order, but the demand-side counterpart
  to this thread's whole story: outside capital now being recruited at
  Wall Street scale specifically to fund the infrastructure that
  generates Nvidia's order book, treating compute as a lend-against
  asset class rather than one-off vendor financing. Nvidia shares fell
  on the announcement. Full detail on `ai-circular-financing-risk`
  (`sev=major` there).
  ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital), [CNBC](https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html)) ⟨daily 2026-08-10⟩

## 2026-08-07 — Nvidia takes a $3B stake in the power layer under Stargate

- **Nvidia will invest up to $3B in Lancium, the Blackstone-backed power
  developer behind Stargate's Abilene, Texas campus** — $2B initial for a
  ~20% stake, up to $1B more on grid milestones, valuing Lancium at
  roughly $10B. Not a chip order, but the same customer-financing logic
  one layer down: Nvidia now holds equity in the power infrastructure its
  own GPU customers depend on. Cross-refs `ai-circular-financing-risk`,
  `ai-power-buildout`.
  ([The Information](https://www.theinformation.com/articles/nvidia-invest-3-billion-blackstone-backed-power-firm-behind-stargate)) ⟨daily 2026-08-07⟩

## 2026-08-05 — A new demand category: SpaceX commits exclusively to Nvidia for AI compute in orbit

- **SpaceX unveiled Starmind AI1, an exclusive deal to run Nvidia Rubin
  GPUs and Vera CPUs as orbital AI compute** — each satellite carries a
  full Rubin NVL72 rack (72 GPUs), stands ~20m tall with a 75m solar
  wingspan, draws ~210kW average/~250kW peak power, targets a 2027
  launch, and SpaceX has floated a constellation scaling toward 1M
  satellites as a "distributed AI supercomputer in space." AMD shares
  fell on the exclusivity news.
  ([Interesting Engineering](https://interestingengineering.com/space/nvidia-spacex-starmind-ai1-satellite); multiple outlets 08-04/08-05) ⟨daily 2026-08-05⟩
- 💡 **A genuinely new category on this thread's demand side** — every
  prior entry here is terrestrial hyperscaler/lab demand; this is the
  first orbital compute customer, at satellite counts that dwarf any
  single datacenter campus if the constellation plan holds. Cost and
  firm order size are not yet disclosed — treat the "1M satellites"
  figure as a stated ambition, not a backlog number. ⟨daily 2026-08-05⟩

## 2026-07-24 — Opened + crawled

- **Thread opened** (ben-steer). ⟨steer 2026-07-24⟩
- **Verdict: the strongest demand book ever reported — ~$1T in Blackwell+
  Rubin orders through 2027 — but it's Huang's own aggregate figure, not an
  audited backlog, and the flashiest pillar (the $100B OpenAI deal)
  COLLAPSED in early 2026.** The binding constraint has shifted from demand
  to supply (an HBM4 drought). ⚠ WebSearch budget was exhausted (9-crawl
  fan-out) — built from targeted fetches; a few figures are soft. ⟨crawl 2026-07-24⟩

## ← Backstory (crawl 2026-07-24 → artifacts/findings/nvidia-order-book-2026-07-24.md)

## 2026-05-13 — First-ever $5.5T

- **Nvidia hit $5.5T market cap** — the first company ever — on news Huang
  would join Trump's China trip (~$5T as of late July).
  ([Forbes](https://www.forbes.com/sites/antoniopequenoiv/2026/05/13/nvidia-hits-record-55-trillion-value-first-company-to-ever-reach-mark/)) ⟨crawl 2026-07-24⟩

## 2026-04-09 — The constraint flips to supply

- **A Rubin supply squeeze** — HBM4 shortage pushed SK Hynix's ramp to
  Q3'26; TrendForce cut its 2026 Rubin shipment share 29%→22%. Demand isn't
  the bottleneck anymore; memory is. ⚠ reported (TrendForce).
  ([SDxCentral](https://www.sdxcentral.com/news/nvidias-rubin-gpus-hit-the-brakes-as-hbm4-memory-drought-threatens-jensens-supply-chain-magic-report/)) ⟨crawl 2026-07-24⟩

## 2026-03-16 — The $1T claim

- **GTC: Huang says ~$1T in Blackwell+Rubin orders through 2027** — up from
  the $500B-through-2026 figure a year prior. It's a demand/visibility
  number, NOT audited RPO/backlog — no public per-customer breakdown exists.
  ([TechCrunch](https://techcrunch.com/2026/03/16/jensen-just-put-nvidias-blackwell-and-vera-rubin-sales-projections-into-the-1-trillion-stratosphere/)) ⟨crawl 2026-07-24⟩

## 2026-03-04 — The $100B OpenAI deal dies

- **The OpenAI–Nvidia $100B / 10GW partnership is dead** — Huang confirms
  it's not proceeding (citing OpenAI's IPO plans); FT reported the
  abandonment in Feb. Corrects the circular-financing picture: Nvidia's
  actual OpenAI exposure is the ~$30B equity stake from the $110B round,
  not the $100B LOI. Cross-refs `ai-circular-financing-risk`.
  ([Gizmodo](https://gizmodo.com/the-100-billion-openai-nvidia-deal-is-not-happening-2000729749)) ⟨crawl 2026-07-24⟩

## 2025-12 — The backlog + the circular stakes

- **~3.6M-unit Blackwell backlog** from cloud providers; B200/GB200 sold out
  through mid-2026 (Microsoft the lead buyer, Meta >$100B 2026 capex). ⚠
  trade/analyst-sourced.
  ([FinancialContent](https://markets.financialcontent.com/stocks/article/tokenring-2025-12-29-nvidias-blackwell-dynasty-b200-and-gb200-sold-out-through-mid-2026-as-backlog-hits-36-million-units)) ⟨crawl 2026-07-24⟩
- **Nvidia's own 10-Q lists customer investments** — OpenAI up to $100B,
  Anthropic $10B, Intel $5B — Nvidia putting capital into its own buyers,
  the circular-financing critique made concrete (CFO: no definitive OpenAI
  agreement).
  ([Fortune](https://fortune.com/2025/12/02/nvidia-openai-deal-not-signed-yet-100-billion-rally-colette-kress/)) ⟨crawl 2026-07-24⟩
