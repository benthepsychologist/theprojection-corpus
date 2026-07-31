---
thread: china-stack-independence
kind: crawl-finding
date: 2026-07-22
bundle: artifacts/bundles/china-stack-independence-2026-07-22/
method: >
  GDELT DOC API (partial — sustained 429s from concurrent crawls) +
  ~30 targeted fetches. Two of our prior digest claims flagged
  uncorroborated below.
---

# China's stack decoupling — backstory finding

**The throughline:** what looked like a July story is an eighteen-month
build: since the January-2025 "DeepSeek moment," China has assembled
models (DeepSeek V4, Qwen, GLM, Kimi), silicon (Huawei Ascend, Alibaba
Zhenwu + the SAIL stack open-sourced against CUDA), a state-run token
economy, and now capital-markets exits (Moonshot → HKEX, DeepSeek → IPO
talk, CXMT's listing) — while both governments converge on treating
frontier AI as an export-controlled national asset. July's selloff and the
$8.9B state intervention are the capital market pricing the transition.

## The arc (condensed; full event list in the bundle)

**2025-01 — the reference shock.** DeepSeek R1 wipes ~$600B off Nvidia
temporarily; every 2026 episode is measured against it.
([Forbes](https://www.forbes.com/sites/jonmarkman/2026/04/28/chinas-deepseek-v4-and-qwen-reshape-the-open-source-ai-race/))

**2026-04 — models arrive in force.** DeepSeek V4-Pro/Flash (MIT-licensed
1.6T MoE; V4-Pro reportedly trained on ~50k H100s acquired via Singapore
shells, V4-Flash on Huawei Ascend); Qwen passes 1B cumulative HF
downloads (>50% of global open-source downloads in Feb).
([Forbes](https://www.forbes.com/sites/jonmarkman/2026/04/28/chinas-deepseek-v4-and-qwen-reshape-the-open-source-ai-race/))

**2026-05 — silicon and signaling.** Hours after Trump's Beijing state
visit (Huang in the delegation), China bans Nvidia's RTX 5090D V2.
Alibaba unveils the Zhenwu M890 (144GB on-chip, ~3× predecessor; vs
H100-generation) with a 380B-yuan (~$53B) buildout pledge — while
admitting only ~560k Zhenwu units shipped ever, vs ~1M GPUs AWS racks in
a year: "Chinese fabs can't yet match TSMC."
([Yahoo](https://finance.yahoo.com/sectors/technology/articles/alibaba-baba-unveils-zhenwu-m890-120131341.html) ·
[The Register](https://www.theregister.com/systems/2026/05/22/alibaba-just-admitted-its-struggling-to-keep-up-with-rival-chipmakers-and-ai-shops/5244665) ·
[Nagaland Post](https://nagalandpost.com/china-bans-nvidia-gaming-chip-hours-after-trumps-visit/))

**2026-06 — institutionalization.** Beijing certifies 9 domestic AI chips
for government procurement (headline-verified only); the NDA's
token-economy plan makes tokens tradable settlement units (state telecoms
sell retail token plans from ¥9.9/mo); Amodei accuses Alibaba of
distilling Claude into Qwen.
([Jamestown](https://jamestown.org/the-prcs-token-economy-takes-shape/) ·
[The Register](https://www.theregister.com/ai-and-ml/2026/07/22/the-truth-nobody-wants-to-admit-chinese-or-not-open-models-are-competitive-now/5275879))

**2026-07-16→18 — the K3 shock.** Kimi K3 ships (2.8T, largest open
weights ever; Moonshot ARR $300M in June, ×3 since March), tops Frontend
Code Arena over Fable 5 (still trails Fable 5/GPT-5.6 Sol overall);
Alibaba's T-Head open-sources the **SAIL** Zhenwu software stack at WAIC
**07-18** (correcting our earlier ~07-20 dating), explicitly aimed at
CUDA.
([Yahoo/Reuters](https://finance.yahoo.com/technology/ai/articles/moonshots-kimi-k3-launch-shakes-124223269.html) ·
[China Tech News](https://www.chinatechnews.com/2026/07/18/125849-alibaba-targets-nvidias-dominant-software-ecosystem-with-open-source-ai-stack))

**2026-07-19→21 — the market prices it.** Chinese equities shed **$1.48T
over two weeks** (STAR Market −25% from July peak; Q2 GDP 4.3%, weakest
in 3+ years); the "national team" (China Reform >50B yuan + Chengtong
~10B) injects ~$8.9B with insurer pledges and 300+ buybacks. Qwen3.8-Max
previews 07-19 ("second only to Fable 5" — an independent StackPerf run
scores K3 83 vs 80 over it); Beijing weighs export controls on its own
models/weights/data/chip designs (FT).
([Epoch Times](https://www.theepochtimes.com/china/after-a-1-48-trillion-selloff-chinas-national-team-steps-in-to-steady-stocks-6065409) ·
[SCMP](https://www.scmp.com/tech/article/3361119/alibaba-says-newest-qwen-ai-model-second-only-anthropics-claude-fable-5) ·
[Cherry Creek News](https://thecherrycreeknews.com/alibaba-qwen-3-8-max-second-only-to-fable-5-first-benchmark-cherry_creek/) ·
[Reuters via Yahoo](https://finance.yahoo.com/technology/ai/articles/china-considers-tighter-export-controls-041139427.html))

**2026-07-21→22 — Washington splits.** Bessent threatens **sanctions on
Chinese model makers** over "IP theft" ("watermarks of our US LLMs" on
Chinese models; trigger: K3). Axios had reported a wholesale
Chinese-open-model ban under consideration — officials then distanced
from it. Huang pushes back publicly: US firms should be free to use
"excellent" Chinese open models; adoption grows chip demand.
Moonshot plans a final pre-IPO round at **$50B** (Aug), HKEX listing
targeted within 6 months.
([SiliconANGLE](https://siliconangle.com/2026/07/21/u-s-treasury-secretary-bessent-threatens-sanctions-chinese-ai-model-makers/) ·
[Yahoo/Axios](https://finance.yahoo.com/technology/ai/articles/jensen-huang-says-u-firms-131327067.html) ·
[TechNode](https://technode.com/2026/07/22/moonshot-ai-reportedly-plans-final-pre-ipo-round-at-50-billion-valuation/))

## ⚠️ Corrections to our own record (from this crawl)

- **"Commerce backing off toward procurement/hosting rules"** (our 07-21
  digest, via The Neuron): not corroborated. What's sourced: a reported
  wholesale ban that officials distanced from. Treat the "pivot" framing
  as unverified.
- **"US–China talks in September"** (our 07-21 digest + ledger, via a
  roundup): no fetched source specifies September — only "later this
  year." Ledger entry adjusted.
- **Z.AI's 1 GW / all-domestic-chip claims** rest on the paywalled
  Bloomberg piece alone; chip supplier (Ascend? SMIC-fabbed?) unnamed
  anywhere fetched. Confidence: source-limited, not retracted.

## Open questions (feed the watch)

- Who fabs Zhenwu and Z.AI's training silicon — SMIC capacity is the
  unnamed constraint in every "can't match TSMC" line.
- Do Beijing's own-stack export controls land in the next export-control
  catalogue revision, and do they conflict with Moonshot's 07-27 open
  weights?
- Does Bessent's sanctions threat materialize into an instrument?
- The capital-markets wave: Moonshot Aug round → HKEX; DeepSeek $71B
  raise/IPO; how much state capital ends up holding the sector after the
  national-team intervention?
