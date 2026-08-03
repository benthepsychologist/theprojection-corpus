<!-- state-of-the-game · q2 (inference demand + contracts) · deep-research agent, verbatim
     2026-08-03 · fetch-only (WebSearch budget exhausted session-wide);
     ~30 fetches + DDG-lite; figures from snippets/aggregators flagged secondary. -->

# STATE OF THE GAME — "Who's buying inference, how much, and what are the contracts worth?"

**Method note:** WebSearch budget exhausted before start; worked via ~30 WebFetch + DDG-lite. Verified-by-fetch unless marked *(reported/unverified)*.

## 1. Spend / usage measurement — WELL COVERED, mostly free
- **Ramp AI Index** (ramp.com/data/ai-index, + free API) — % of US businesses with paid AI spend from real transactions; billions of txns from 30,000+ businesses; a business "adopted" if any paid AI txn that month. **Latest: 55.0% adoption, June 2026 (+0.8pp m/m).** Biases: Ramp-customer skew, misses free tools. Best free transaction-based adoption series — adoption share + vendor rankings, not aggregate dollar demand.
- **Anthropic Economic Index** (anthropic.com/economic-index) — Claude usage composition (tasks, occupations, geography) from ~1M conversations + ~1M API transcripts; 172 countries. Free. **Usage only — no dollars.**
- **OpenRouter rankings** — live token-share by model/lab, free; only OpenRouter-routed traffic (skews indie/app-layer, excludes direct enterprise API). Relative-share signal, not market-size.
- **Sensor Tower "State of AI 2026"** (Jun 16 2026) — global AI app IAP revenue **>$4B H1 2026 (+36% vs H2 2025)**; ChatGPT fastest app to 1B MAU (May 2026). *(secondary via PR)*. Paid platform; headline reports free.
- **Earnest Analytics** — card-panel: ChatGPT >73% of paid consumer AI spend; payments to 16 major consumer AI tools +570% YoY *(secondary)*.
- **Vendor self-disclosures** (event-driven): Google **3.2 quadrillion tokens/month** (I/O May 2026; vs 480T a year earlier), 22B API tokens/min *(secondary, multiply-reported)*. OpenAI ~900M WAU (Feb 2026), ~$2B/month run-rate (Mar 2026), 15B API tokens/min *(aggregator, unverified)*.
- **Epoch AI Data Hub** (epoch.ai/data) — standout free layer: AI Companies (revenue run-rates, funding, compute spend, credibility ratings; updated Jul 31 2026), AI Data Centers (satellite+permit; Aug 3 2026), AI Chip Sales, AI Chip Owners ("five companies control 71%"). Distinguishes annualized-run-rate from recognized in docs. **No explicit inference-vs-training split.**

## 2. Enterprise-adoption surveys — WELL COVERED; only Menlo does dollars
- **Menlo Ventures "2025 State of GenAI in the Enterprise"** (3rd annual, Dec 2025) — ~500 US decision-makers + bottoms-up sizing. **Enterprise AI spend $37B in 2025 (3.2× from $11.5B 2024); application layer $19B vs infra $18B; coding $4.0B.** Free PDF. Companion **Mid-Year LLM Update** (Jul 2025): model-API spend $3.5B→$8.4B in six months; usage share Anthropic 32% / OpenAI 25% / Google 20%. No 2026 edition found yet.
- **a16z "100 Enterprise CIOs 2025"** (Jun 2025) — 100 CIOs + 24 interviews; ~75% expect AI-spend growth; 37% use 5+ models. Free, annual, qualitative — no sizing.
- **US Census BTOS** — ~1.2M businesses, six panels of ~200k; biweekly; AI supplement by sector/state/size. Free. **The only nationally representative series** — incidence not dollars; base rates far below Ramp's (different universe).
- KPMG Global AI Pulse (quarterly, 2,100+), Deloitte State of AI (3,235 C-suite, annual), McKinsey State of AI — all free, sentiment/adoption, **no spend dollars**.

## 3. Revenue trackers — SEMI-COVERED; run-rate-vs-recognized lives in journalism
- **The Information** (theinformation.com/newsletters) — AI Agenda, AI Infrastructure, Applied AI + org charts (~70 cos). **The only place recognized-revenue vs claimed-run-rate is reported from primary documents.** Paywalled.
- **Sacra** (sacra.com/c/openai/) — OpenAI $25B annualized (Feb 2026), valuation $852B *(some page figures stale/inconsistent — verify)*. Partially paywalled (~$50/mo, approx).
- **Epoch AI Companies** — only *free, sourced, credibility-rated* revenue dataset; inherits run-rate framing but labels it.
- **Ed Zitron** — adversarial accounting: "OpenAI Losses Increased Nearly 8× in 2025, Spending $34B" (Jun 15 2026), "Anthropic's Profitability Swindle" (May 2026), "The Subprime Data Center Crisis" (Jul 2026). The prosecution brief.
- **Tanay Jaipuria** — historically useful on ARR/multiples; recent archive drifted to robotics/S-1s. Not currently a systematic tracker.
- **Major-outlet cluster (to-verify):** Anthropic run-rate crossed **$47B May 2026** (from $30B earlier), raised $65B at $965B valuation (CNBC/Reuters, May 28 2026, Reuters fetch-blocked); OpenAI $25–33B mid-2026 — implies Anthropic overtook OpenAI on revenue, thematically consistent with Ramp adoption. **Verify against The Information/primary before it carries weight.**
- **Sell-side:** JPM Cembalest "Smothering Heights" (2026 EOTM, free) — lab run-rates vs **$1.3T hyperscaler capex**, profitability risk, return concentration. PitchBook/CB Insights — funding-centric, not revenue-recognition.

## 4. Contract / backlog analysis — EARNINGS COMMENTARY only; no institutional tracker
- **Oracle** RPO **$455B Q1 FY26 (+359%)** → ~$638B by Q4 *(reported)*; ~half OpenAI, 88% beyond 12 months, negative FCF. Scattered, no tracker.
- **Microsoft** commercial RPO **$625B→$627B** (Q2→Q3 FY26); ~45% OpenAI *(secondary; consistent with the $250B Azure commitment)*.
- **CoreWeave** backlog ~$99–100B (Q1 2026) vs 2026 rev guide $12–13B; Microsoft 67% of revenue; OpenAI $11.9B; Meta $21B; Anthropic multibillion *(secondary)*.
- **OpenAI commitment web** ~$1.4T (Oracle $300B, Microsoft $250B, AWS $38B, + AMD/Nvidia/Broadcom/CoreWeave — figures don't sum; secondary). **No authoritative running tracker.**
- **Anthropic web** — Google $200B/5yr TPU (May 5 2026, "largest lab compute commitment ever") + earlier $40B/5GW (Apr 2026); Amazon $100B/10yr Trainium + up to $25B investment (Apr 2026) *(secondary)*.
- **ai-circular-economy.com** (Will Francis) — free, live, **sourced interactive map**: 24 companies, 60 deals, flow types, status tags (signed/LOI/paused), $725B 2026 capex, updated Jul 27 2026. **The closest thing to a sustained circularity tracker** — maps deal flows, does NOT reconcile against revenue.
- **SemiAnalysis** — sells the infra ground truth (AI Cloud TCO, Tokenomics, Inference Simulator, Datacenter Model, GPU Pricing); institutional; the paid answer to "what is capacity actually worth."

## 5. Government purchasing — THIN
- **USAspending.gov** — raw, free, mandated; everything derives from it.
- **Brookings "Where does federal AI spending stand in 2026?"** (biennial, data via Leadership Connect) — federal AI contracts 472 (2022) → 961 (2024) → 1,743 (2026); federal AI spend **$7.2B 2026 vs $355M 2024** *(secondary — verify in article)*.
- **GSA OneGov** (Aug 2025) — ChatGPT Enterprise **$1/agency**, Claude **$1/agency**, Gemini **$0.47/agency**. **Dollar-based measurement of federal AI adoption is now nearly meaningless** — usage, not spend, is the variable, and nobody publishes it.
- Pentagon ~$32B AI contract *ceiling* H1 FY26 *(secondary; ceilings ≠ obligations)*. Stanford HAI AI Index 2026 (annual, free) — yearly-synthesis altitude. "presenc.ai"-type sites = SEO marketing, skip.

## READ-FIRST (ranked)
1. **Menlo State of GenAI + Mid-Year LLM Update** — the only bottoms-up enterprise dollar sizing; free.
2. **Epoch AI Data Hub** — free, sourced, credibility-rated reference numbers.
3. **The Information — AI Agenda + OpenAI/Anthropic financial scoops** — the only recognized-vs-run-rate primary reporting.
4. **Ramp AI Index** (+ free API) — monthly transaction-based adoption.
5. **Cembalest "Smothering Heights"** — institutional capex-vs-revenue framing; free.
6. **Ed Zitron** ($70/yr) — the adversarial accounting.
7. **ai-circular-economy.com** — the deal web, sourced, current, free.
8. **Census BTOS** — the representative adoption baseline to calibrate vendor-skewed sources.
9. Sensor Tower + Similarweb + Earnest — consumer demand side.
10. Anthropic Economic Index + OpenRouter — usage composition. (+ SemiAnalysis if budget for paid infra ground truth.)

## GAP ANALYSIS
- **Inference vs training split, empirically:** only Deloitte's Nov 2025 *prediction* (~50%→~2/3) and SemiAnalysis's paywalled modeling. Nobody reconciles token-volume disclosures with revenue or capacity. **Nobody credibly measures it publicly.**
- **External vs circular revenue:** nobody computes what share of lab/neocloud revenue is funded by vendors' own commitments. The map shows flows; Zitron argues qualitatively; no reconciliation built.
- **Deduplicated obligation web:** the same OpenAI dollar sits in Oracle's, Microsoft's, AND CoreWeave's RPOs; no one nets ~$1.4T OpenAI + ~$300B+ Anthropic against seller backlogs to a single non-double-counted number.
- **Run-rate vs recognized as a dataset:** only leak-driven journalism (The Information) + Epoch's flag — no systematic series.
- **One summed external-demand number** (consumer + enterprise + government) set against committed capacity — the exact quantity q2 implies — exists nowhere.
- **Government usage:** $1-per-agency seats broke dollar measurement; no one tracks actual federal consumption.

## VERDICT: Partially settled — read the demand side, build the contracts side.
Adoption/usage measurement is well-covered and mostly free (Ramp, BTOS, Menlo, Epoch, OpenRouter, Sensor Tower, Anthropic's index) — researching from scratch duplicates good work. Revenue tracking is semi-covered: Epoch the dataset, The Information the recognized-vs-claimed reporting, Zitron the stress test; the mid-2026 headline numbers (Anthropic $47B vs OpenAI $25–33B) reported but deserve primary verification. Genuinely open, non-duplicative: a deduplicated valuation of the committed-capacity web (Oracle/Microsoft/CoreWeave/Google/Amazon RPOs vs the OpenAI/Anthropic commitment stack), an external-vs-circular revenue split, and any empirical inference-vs-training decomposition. Nobody publishes those; the closest artifacts are one hobbyist deal map, one bank outlook PDF, and a paywalled research shop's models.
