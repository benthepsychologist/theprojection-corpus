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

## 2026-09-22 — Google pitches TPUs to Korea, outside its own cloud

- **Google has offered South Korea priority supply of its TPU accelerators for the country's sovereign-AI data-center buildout, following an April announcement that it would sell TPUs to data centers outside Google Cloud.** Seoul Economic Daily reports Google met Korean AI-strategy officials on 09-09, cites Morgan Stanley's estimate of Google direct TPU sales of $84bn in 2027 and $108bn in 2028, and notes Anthropic's plan to expand TPU use from 1GW this year to 5GW next year; an unnamed Korean industry official told the paper Nvidia GPU delivery lead times run "as long as 30 weeks" and that Google is exploiting the gap. It moves the TPU from an in-house inference chip toward a product sold to third parties and governments, which is a step past the inference-only framing on this thread. ([Seoul Economic Daily](https://en.sedaily.com/technology/2026/09/22/google-joins-nvidia-amd-in-race-for-koreas-ai-infrastructure)) ⟨daily 2026-09-23⟩

## 2026-09-17 — Broadcom's Sept 2 earnings call named OpenAI as a 4th custom-silicon customer, $10B in orders, Jalapeño already shipping

- **Broadcom's September 2 earnings call confirmed OpenAI as a named fourth AI-chip customer, alongside $10B in AI-chip orders and confirmation that the Jalapeño chip (already benchmarked at Hot Chips, 08-25 entry above) shipped this quarter, on track for a 1.3GW deployment.** Caught on this thread's cold-rotation pass, 15 days after the earnings call itself — a lag worth noting given how central Jalapeño's production timeline is to this thread's thesis. (Broadcom Q3 FY2026 earnings call, 2026-09-02) ⟨daily 2026-09-17⟩

- **Qualcomm and Amazon announced a multi-generation collaboration on custom AI-inference silicon and optical interconnects for AWS data centers, with Qualcomm also issuing Amazon warrants for $4B of Qualcomm stock and AWS committing to purchase up to $60B of Qualcomm chips and technology over the deal's life.** This is a new fork in the thread's thesis: rather than one hyperscaler-designed chip line per company, Amazon is now running Trainium in-house *and* buying custom AWS-specific silicon from a merchant vendor (Qualcomm, diversifying beyond its smartphone base) — a hybrid pattern this thread hasn't tracked before, distinct from Broadcom/Marvell's co-design-house role. Qualcomm's own release names the technology (custom inference silicon, SerDes/optical DSP, 1.6T+ interconnects) but discloses no dollar figures; the $4B warrant and $60B purchase-commitment figures come from Qualcomm's SEC-linked disclosure as reported by CNBC and Bloomberg.
  ([Qualcomm/PR Newswire](https://www.prnewswire.com/news-releases/qualcomm-announces-multi-generational-product-collaboration-with-amazon-to-build-next-generation-ai-data-center-infrastructure-302871895.html), [CNBC](https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html))
  ⟨daily 2026-09-14⟩

## 2026-09-02 — Broadcom names Anthropic its likely largest custom-chip customer, with 5GW of next-generation TPUs planned for 2027

- **Broadcom CEO Hock Tan said on the company's 09-02 earnings call that Anthropic "is on track to become our largest XPU customer in 2027 and sustain that in 2028."** Broadcom is deploying 1 gigawatt of Google's Ironwood TPU capacity for Anthropic in 2026, expects Anthropic to deploy another 5 gigawatts of the next-generation TPU v8i in 2027, and sees a further 10 gigawatts of potential Anthropic deployments in 2028; Tan also said production shipments of TPU v8i have begun. This is the sharpest evidence yet for this thread's anchor claim that a frontier lab running on custom silicon (rather than Nvidia GPUs) is real: the customer Broadcom expects to pass Google itself is a tenant, not a chip designer. It sits beside the OpenAI fourth-customer entry logged 09-17. ([Benzinga](https://www.benzinga.com/markets/tech/26/09/61594615/broadcom-ceo-hock-tan-anthropic-largest-xpu-customer-google-tpu-orders), [SiliconANGLE](https://siliconangle.com/2026/09/02/broadcom-beats-expectations-as-ai-labs-double-down-on-custom-chips/)) ⟨daily 2026-09-23⟩

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
