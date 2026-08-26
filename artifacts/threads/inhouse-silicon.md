---
thread: inhouse-silicon
title: "In-House Silicon"
lens: ai
entities: [google, amazon-aws, microsoft, meta-ai]
opened: 2026-07-24
crawled: 2026-07-24
---

# In-House Silicon — timeline

*Watch:* The custom-silicon revolt (TPU/Trainium/Maia/MTIA) — real and
reducing Nvidia dependence, but only for INFERENCE and via two anchor cases
(Anthropic on Trainium + TPU). At the training frontier and in absolute
dollars Nvidia demand still grows; the clearest winners are the co-design
houses (Broadcom, Marvell), not the hyperscalers.

## 2026-08-25 — Jalapeño's first public benchmarks land at Hot Chips

- **OpenAI and Broadcom published Jalapeño's first performance
  benchmarks at Hot Chips 2026, claiming better performance-per-watt
  than Nvidia's flagship.** The inference ASIC the two announced in June
  was disclosed at 700W TDP, with a 128-chip pod at 1.7 exaflops in
  4-bit and 27.5TB of HBM4, and claimed advantages up to 1.9x
  throughput-per-kilowatt and 3.6x lower latency on SemiAnalysis's
  InferenceX benchmark; small-scale deployment inside OpenAI is targeted
  for end-2026, broader rollout 2027. The June item was a partnership
  announcement — this is the first evidence the silicon works.
  ([OpenAI](https://openai.com/index/jalapeno-first-results/),
  [TechCrunch](https://www.techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/))
  ⟨daily 2026-08-25⟩

## 2026-08-21 — Anthropic hires the founding architect of Google's TPU program

- **Amir Salek, who founded and led Google's custom-silicon division from
  2013 to 2022 across the first seven generations of the TPU, joined
  Anthropic's compute team**, reporting to James Bradbury, as part of a
  push to design its own AI chips. This thread has read the custom-silicon
  revolt as real but inference-only, anchored by Anthropic *running* on
  Trainium and TPU rather than building. This is the first hard evidence
  it intends to design — and the most senior custom-silicon hire any
  frontier lab has made.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-21/anthropic-taps-google-chip-veteran-as-part-of-push-into-hardware),
  [Crypto Briefing](https://cryptobriefing.com/ex-google-amir-salek-joins-anthropic/),
  [Seeking Alpha](https://seekingalpha.com/news/4636024-anthropic-hires-former-google-chip-developer-as-it-pursues-in-house-solution-report))
  ⟨daily 2026-08-21⟩
  <!-- k: caught 08-23 by the tier-3 cold rotation; Bloomberg's body is
       paywalled, so the date rests on its dated URL plus three same-day
       secondaries citing its "Friday" report — solid on date, unpinned
       on hour. -->

## 2026-08-06 — Anthropic joins the in-house silicon story

- **Anthropic confirmed it is building an in-house AI chip-design team,
  targeting ~50% inference-cost cuts, with Samsung scouted as a fab
  partner** (disclosed 08-05; caught by the 08-07 finalize's coverage
  critic — 3 of 4 benchmark newsletters carried it while this thread's
  terms only swept the hyperscalers' chips, which is exactly why the
  thread had gone quiet). First frontier-lab entrant on a thread that
  had been hyperscaler-only; term and entity added.
  ([TechCrunch](https://techcrunch.com/2026/08/05/anthropic-is-hiring-an-ai-chip-design-team/)) ⟨daily 2026-08-07⟩

## 2026-08-05 — A fifth entrant: Anthropic starts building its own chip-design team

- **Anthropic is assembling an internal AI chip-design team**, confirmed
  by the company after Business Insider broke the story — recruiting
  through a "custom silicon team" job listing, aiming to "co-design
  hardware and models to help its technology run faster and more
  efficiently." Anthropic currently relies entirely on external partners
  (AWS, Google, Nvidia, AMD) for compute; The Information separately
  reported it is evaluating Samsung as a manufacturing partner. This is
  the customer side of the story, not another hyperscaler program — the
  exact company this thread cites as the anchor case for
  "inference-only, still mostly Nvidia plus Trainium+TPU" is now moving
  toward designing silicon of its own rather than only consuming
  hyperscaler chips. Coverage doesn't specify whether the target is
  training or inference/serving — a genuine open question, not yet
  resolved by any source.
  ([TechCrunch](https://techcrunch.com/2026/08/05/anthropic-is-hiring-an-ai-chip-design-team/)) ⟨daily 2026-08-05⟩

## 2026-07-27 — Four programs, one wall ⟨crawl 2026-07-27⟩

- TPU v7 Ironwood (Broadcom/MediaTek/TSMC co-design) · Maia 200
  (dual-purpose, volumes undisclosed) · Trainium 1.4M deployed ·
  MTIA "millions" H100-eq, Iris Sept-26. All four decline to state the
  own-vs-Nvidia split — the wall every capex crawl hit.

## 2026-07-24 — Opened + crawled

- **Thread opened** (ben-steer). ⟨steer 2026-07-24⟩
- **Verdict: diversification at the margin and on inference, not a rout.**
  The CUDA-vs-XLA software moat keeps Nvidia the default for anyone without
  a captive anchor customer; the "in-house" silicon is largely outsourced
  to Broadcom/Marvell. ⚠ WebSearch budget exhausted (fan-out) — primary-doc
  fetch path; Maia 200 + some codenames single-sourced, flagged. ⟨crawl 2026-07-24⟩

## ← Backstory (crawl 2026-07-24 → artifacts/findings/inhouse-silicon-2026-07-24.md)

## 2026-06 — Broadcom is the real winner

- **Broadcom's custom-AI revenue hit $10.8B in a single quarter (+143%
  YoY)**, guiding $29.4B next and reaffirming ">$100B AI revenue in 2027";
  ~6 hyperscaler XPU customers. Marvell (Trainium/Maia co-design)
  projecting ~$11B AI-ASIC revenue in 2026. The revolt enriches the
  co-designers.
  ([Reuters](https://www.reuters.com/business/broadcom-tumbles-revenue-miss-clouds-ai-boom-bets-2026-06-04/)) ⟨crawl 2026-07-24⟩

## 2026-04 — Google Ironwood + the Anthropic anchor

- **Ironwood (TPU v7) hit broad Cloud GA** (04-22); combined with the Oct
  2025 Anthropic–Google deal (up to 1M TPUs / >1GW in 2026, first phase
  400k Ironwood). SemiAnalysis: Ironwood ~44% lower TCO than a GB200 server;
  Anthropic ~52% lower TCO/PFLOP vs GB300 — the economics behind the revolt.
  ([SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)) ⟨crawl 2026-07-24⟩

## 2026-03 — Meta MTIA: inference, not frontier

- **Meta's MTIA 300 in production** (ranking/rec), 400/450/500 on a 6-month
  cadence, "hundreds of thousands" deployed for inference — but explicitly
  NOT frontier-LLM training (Meta still buys Nvidia/AMD for that). The
  workload-specific pattern.
  ([Meta](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/)) ⟨crawl 2026-07-24⟩

## 2026-01 — Microsoft the laggard

- **Maia 200 launched — inference-only** (TSMC 3nm, claims 30% better
  perf/$); next-gen "Braga" reportedly delayed into 2026. Microsoft is
  furthest behind and still overwhelmingly Nvidia-reliant for training. ⚠
  Maia 200 specs are a vendor claim, single-sourced — don't treat as
  independent benchmark.
  ([Microsoft](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)) ⟨crawl 2026-07-24⟩

## 2025-10→12 — The Anthropic-on-Amazon anchor

- **Amazon Trainium3 UltraServers GA** (re:Invent, up to 50% lower cost);
  **Project Rainier** live (~500k Trainium2 for Claude training, Indiana);
  AWS passed 1M+ Trainium deployed (+150% YoY); Anthropic committed >$100B
  to AWS/10yr, up to 5GW Trainium. A frontier lab running mostly off Nvidia
  is the strongest evidence the revolt is real.
  ([Anthropic](https://www.anthropic.com/news/anthropic-amazon-compute)) ⟨crawl 2026-07-24⟩
