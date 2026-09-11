---
thread: enterprise-agent-product-race
title: "The Enterprise Agent Land Grab"
lens: ai
entities: [anthropic, google-deepmind, mistral-ai]
opened: 2026-08-25
---

# The Enterprise Agent Land Grab — timeline

*Watch:* whether the pace of 2026-08-20 holds or was a one-off pileup;
whether any lab treats this as a distinct product line with its own
roadmap; whether enterprise adoption numbers (seats, IDE installs) ever
get disclosed.

## 2026-09-11 — OpenAI opens its Agents API to the public and Salesforce completes buying Fin, both pushing further into managed agent infrastructure

- **OpenAI opened public beta of an Agents API that exposes its managed Codex harness — sessions, orchestration, context compaction and crash recovery — as a general-purpose API rather than a Codex-specific tool.** Developers supply their own tools and choose an execution environment (OpenAI-managed sandbox, self-hosted via workspace/capability directories, or a partner sandbox); built-ins include code sandboxing, file editing, MCP connections, artifact generation and multi-agent delegation, with no fee beyond usage. It puts OpenAI's internal agent-orchestration stack into direct competition with the agent-framework vendors this thread tracks. ([OpenAI](https://openai.com/index/introducing-the-agents-api)) ⟨daily 2026-09-11⟩
- **Salesforce completed its acquisition of Fin, folding the AI customer-service company's model suite and technical team into Salesforce AI Labs alongside Agentforce.** Per Salesforce's own release, Fin serves 30,000+ companies with an average 76% autonomous resolution rate across chat, email, WhatsApp, SMS, voice and Slack, and will keep operating as a distinct product line rather than being absorbed. ([Salesforce](https://www.salesforce.com/news/)) ⟨daily 2026-09-11⟩

## 2026-09-08 — Cognition raises over $2bn at a $48bn valuation, nearly doubling in four months

- **Cognition raised more than $2bn in a Series E led by Andreessen Horowitz and Accel, valuing the maker of the Devin coding agent at $48bn** — close to double the $26bn it carried four months ago. The company put run-rate revenue at almost $900m, up from $492m, and named Nvidia, GE Aerospace, Citi and Mercedes-Benz as production customers of the agent. ⚠️ The revenue and customer figures are the company's own, reported via Bloomberg, not independently verified. ([Bloomberg](https://www.bloomberg.com/news/articles/2026-09-08/ai-startup-cognition-raises-2-billion-at-a-48-billion-value)) ⟨daily 2026-09-08⟩

## 2026-09-04 — Altman apologizes for a "messy" Astra rollout that left paying Plus/Pro/Business/Enterprise users without access

- **Sam Altman publicly apologized for the Astra launch's staged access, which prioritized OpenAI's own Daybreak cybersecurity-tester cohort and left paying ChatGPT subscribers — including Pro subscribers, who normally get first access to new releases — watching enterprise customers go first instead.** In his own words on X: "first, sorry for the messy rollout. second, when we screw up, we try to make it right. third, we should be able to begin broad rollout to API customers and chatgpt subscribers in the near future. as usual we will start with pro subscribers." OpenAI is compensating with "one banked reset for every day you don't have access to Astra on your paid ChatGPT plan," and Altman said he was hopeful (not promising) Pro subscribers could use it over the 09-05/09-06 weekend. This directly complicates this thread's own 09-03 entry, which read Astra reaching "Business and Enterprise tiers alongside Plus and Pro within days" — the "within days" promise ran into the same Daybreak-first gating that `frontier-model-gov-review-precedent` already tracks as this thread's lab-run access-control pattern. ([Sam Altman on X](https://x.com/sama/status/2095678759651438887), [The Verge](https://www.theverge.com/ai-artificial-intelligence/990060/altman-apologizes-messy-astra-rollout), [Unite.AI](https://www.unite.ai/sam-altman-apologizes-as-gpt-6-astra-staged-launch-denies-paid-access/)) ⟨daily 2026-09-04⟩

- **OpenAI silently changed several of GPT-6 Astra's headline benchmark
  figures in the hours and days after its own launch post went up, Fortune
  reported, rather than the independent-evaluator gap this thread already
  has on record.** Astra's stated hallucination rate went from 4.2% (in the
  version live at 2:23pm ET on launch day) to 2% roughly three hours later,
  then back to 4.2%. On ExploitBench, the score OpenAI published for
  predecessor GPT-5.6 Sol changed from 5.5% to 11.5%, which OpenAI told
  Fortune reflects "a reasoning level that is not commercially available"
  for Sol — i.e., the comparison model was tested with a configuration
  customers cannot actually buy. On ARC-AGI-3, an embargoed draft carried
  98.6%, the live blog post read 99.99%, and the Arc Prize Foundation's own
  "powerful harness" test scored it 99.9% against 63% on the standard
  harness — explaining a discrepancy the 09-04 digest's coverage-critic
  flagged and left unresolved (two AI newsletters had quoted a 99.9%/99.99%
  figure matching neither the 98.6% headline nor the then-known 62.7%
  standard-harness number). OpenAI's on-record response: "we care deeply
  about getting evaluations right. Most evaluations have noise within a few
  percentage points based on the exact checkpoint, scaffold, and eval run
  used in reporting," calling draft-to-final adjustment standard practice.
  Some outside researchers call it "benchmaxxing." This is a new axis on
  top of the Artificial Analysis/ARC Prize dispute already logged 09-04 —
  not that outsiders measured differently, but that OpenAI's own published
  numbers moved after the fact, and in one case a score for its own
  predecessor model rose on a configuration customers cannot buy.
  ([Fortune](https://fortune.com/2026/09/04/openai-quietly-boosts-some-of-astras-evaluation-metrics-amid-rare-delay-in-publication-of-the-modeblog-post-announcement/), [Startup Fortune](https://startupfortune.com/openai-changed-gpt-6-astras-benchmark-numbers-days-after-its-launch/)) ⟨daily 2026-09-05⟩

- **Artificial Analysis published version 4.2 of its Intelligence Index on 09-04, an interim update it said it had "deliberately held back" through the week's launches but released because "the frontier moving so quickly in the past weeks" made it necessary: AA-Briefcase (a private agentic knowledge-work set) and Surge AI's GDP.pdf are added, the saturated GPQA Diamond is dropped, and 40% of the weighting now sits on private held-out sets, double v4.1's.** On the re-weighted index Claude Fable 5.1 leads, GPT-6 Astra is second with a four-point gain over GPT-5.6 Sol (it had scored level with Sol on v4.1), and Meta is the third-ranked lab ahead of SpaceXAI, Moonshot, Z.AI and Google. AA's own note does not mention Fortune's report that OpenAI changed Astra's published figures after launch; The Decoder's reading that the overhaul was "likely in response to criticism" of the Astra scoring is The Decoder's. For the benchmark dispute this thread carries, the third-party index whose flat Astra score fed the skepticism now shows a gain — on a different test set, which is the point. ([Artificial Analysis](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2), [The Decoder](https://the-decoder.com/artificial-analysis-overhauls-its-intelligence-index-after-gpt-6-astra-scoring-drew-skepticism/)) ⟨daily 2026-09-06⟩

## 2026-09-03 — OpenAI markets Astra as "the world's best computer use model," publishing benchmark numbers and pricing it into Business/Enterprise ChatGPT tiers plus Azure and AWS

- **OpenAI's launch materials call Astra "the world's best computer use model,"** citing an OSWorld 2.0 offline-subset score of 72.6% completed in roughly 40 minutes per task, against predecessor GPT-5.6 Sol's 65.7% at roughly 75 minutes per task — a claimed 47% completion-time improvement — for a model built to navigate browsers, spreadsheets, websites and desktop applications and carry out multistep agentic workflows. It reaches ChatGPT's Business and Enterprise tiers alongside Plus and Pro within days of the Thursday cybersecurity-tester-only start, plus the OpenAI API, AWS Bedrock and Microsoft Azure — priced at $10/million input and $50/million output tokens standard ($20/$100 in a 2.5x-faster "Fast" mode). ([TechCrunch](https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model/), [VentureBeat](https://venturebeat.com/technology/welcome-to-the-agi-era-openai-launches-gpt-6-astra)) ⟨daily 2026-09-03⟩

- **OpenAI published a 39-page paper, "Improved Short Gaps Between Primes," proving that infinitely many consecutive primes differ by at most 186 — the paper's own introduction cites Polymath 8b's 246 from 2014 as the bound it builds past — and stating in its abstract that "the proof is due to GPT 6 Astra," with a machine-checked Lean formalization, as part of the 09-03 Astra launch materials.** The method combines Polymath 8a and Stadlmann's equidistribution estimates with new factorization conditions that enlarge the support of the multidimensional Selberg sieve, establishing DHL[40,2]; mathematicians Weijie Su and Perry Metzger noted the result the same day. The third lab pure-math claim in one week alongside Anthropic's Fermat formalization, and the second launch-day Astra claim this thread carries whose checking is left to outsiders. ([OpenAI — paper PDF](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), [Weijie Su on X](https://x.com/weijie444/status/2095600108956262911)) ⟨daily 2026-09-06⟩

## 2026-09-02 — Google's Gemini 3.8 Flash and Meta's Muse Spark 1.3 ship the same day, both pitched at long-horizon agentic work at workhorse prices

- **Gemini 3.8 Flash — Google's third Flash release in six weeks — ships at 3.7 Flash's introductory price ($0.75 / $3.75 per million input/output tokens) with Google claiming it "outperforms most larger frontier models" on DeepSWE v1.1 long-horizon software engineering and 54.9% on HLE-Verified; Meta's Muse Spark 1.3 rolled out the same day in Muse Code and the Meta Model API, trained on more long-horizon coding tasks, using ~20% fewer tool calls and ~25% fewer tokens than 1.2 by Meta's own engineers' comparison, with its maximum reasoning mode held back pending "additional safety testing."** Meta's scorecard benchmarks 1.3 against GPT-5.6 Sol and Opus 5 at max effort; coverage on 09-03 had Meta shares up ~4% on the parity claim. Both are the mid-tier, agent-workhorse layer of the launch week rather than flagships. ([Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/), [Meta](https://research.meta.ai/blog/introducing-muse-spark-1-3), [TLDR AI, 09-03](https://tldr.tech/ai/2026-09-03)) ⟨daily 2026-09-03⟩

## 2026-08-29 — The adoption-number disclosure this thread has been waiting for arrives, from a bank

- **Citigroup's "Arc" platform was reported as the largest measured enterprise-agent deployment yet, with real usage figures attached**: 180,000 staff across 85 countries using its AI tools, 40,000 developers on the platform, 100,000+ agentic-development hours per week, service agents fielding 3M+ inquiries a year, a 30-40% developer-productivity gain, legacy-system migrations cut from 12 months to 4 weeks, and a 25% cut in servicing effort. Arc runs Cognition's Devin for agentic coding, with "Citi Sky" built jointly with Google Cloud/Google DeepMind — a bank running a coding agent from one lab inside a governance platform co-built with another. All outputs stay under human supervision; autonomous code or financial decisions are explicitly prohibited. ⚠️ **The figures trace to Citi's own May 7, 2026 Investor Day, not new data** — what's new 08-28 is Forkast framing it as the category's largest measured deployment and surfacing the numbers now.
  ([Forkast](https://forkast.news/citigroups-arc-platform-is-the-largest-measured-enterprise-agent-deployment-yet/)) ⟨daily 2026-08-29⟩
- 💡 **This is the disclosure this thread's own watch line named as unanswered** — "whether enterprise adoption numbers (seats, IDE installs) ever get disclosed." Every prior entry on this thread (Claudeforce, the Cowork/Chat memory merge, Antigravity, Slack code channels) shipped a product without a usage number attached. Arc is the first concrete count, even if the count itself is three-plus months old. ⟨daily 2026-08-29⟩

## 2026-08-28 — SpaceX's ownership of Cursor breaks the "any lab, any model" premise this thread has assumed all along

- **OpenAI told SpaceX it is ending Cursor's direct access to OpenAI models, effective November 12, 2026 — the maximum notice period its contract allows — because SpaceX completed a $60 billion acquisition of Cursor's parent Anysphere on August 14 and OpenAI says it "cannot be confident that SpaceX will use our technology within our terms of service," citing Musk's history of contract disputes with OpenAI dating to the Twitter/X acquisition.** OpenAI's own post ("Our decision on Cursor following its acquisition by SpaceX") also rules out giving Cursor its forthcoming models, including Astra. This is a direct hit to the thread's own premise — every enterprise-agent product logged here (Claudeforce, Antigravity, Slack code channels, Citi's Arc) has assumed a coding agent can keep swapping in whichever lab's model is best; Cursor now cannot, because its owner is a frontier-lab competitor. Cursor CEO Michael Truell downplayed the impact (OpenAI models reportedly handle ~5% of Cursor's traffic); Musk called OpenAI's leadership "untrustworthy" on an all-hands call. ⚠️ The announcement itself dates to 2026-08-28 evening (OpenAI's own X post, 21:46 ET) — a genuine gap in this map's coverage of that evening window, caught only now.
  ([OpenAI](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/), [CNBC](https://www.cnbc.com/2026/08/29/openai-cursor-spacex-model-access.html), [the-decoder](https://the-decoder.com/openai-cuts-off-cursor-after-spacex-acquisition-citing-musks-history-of-breaking-contracts/)) ⟨daily 2026-08-30⟩
- **Anthropic moved immediately to fill the gap OpenAI is leaving.** Tom Brown, Anthropic's co-founder and Chief Compute Officer, posted on X that Cursor has been "a trusted partner since Sonnet 3.5" and that Anthropic will expand Claude compute capacity inside Cursor — even though Anthropic itself rents compute from SpaceX under its own $45B deal (Elon Musk has separately warned he could claw back capacity from that deal if SpaceX's own needs get "super tight"). **The land-grab reading:** a rival lab is using a competitor's principled-sounding exit to buy exclusivity in a coding-agent surface it does not own, in the same week its own compute supplier is the company benefiting from the fight. ⚠️ No dollar figure attached to Anthropic's compute commitment.
  ([wccftech, aggregating Tom Brown's X post](https://wccftech.com/anthropic-pounces-as-openai-abandons-spacexs-cursor-vowing-to-increase-claude-compute-even-as-openai-cites-contract-distrust/)) ⟨daily 2026-08-30⟩

## 2026-08-27 — The market prices Claudeforce at 22.58% in a day

- **Salesforce closed up 22.58% at $252.05, its strongest single day since 2020**, on a Q2 FY2027 beat announced with "Claudeforce" — Claude as the reasoning model behind the Atlas Reasoning Engine and Agentforce, the default model across Slack, and a "Salesforce in Claude" plugin carrying 37 prebuilt sales skills, in open beta expected September. Revenue was **$11.345bn, up ~10.8% YoY**, adjusted EPS **$5.90 against ~$3.27 expected**, FY2027 guidance raised $300M to $46.1-46.4bn. **The land-grab reading is distribution:** a frontier lab reaching enterprise seats through an incumbent's install base rather than its own product surface. ⚠️ **No dollar value is attached to the partnership** in either company's materials; **"Claudeforce" is Salesforce's own branding** and does not appear on Anthropic's newsroom, though Amodei is quoted in Salesforce's release; and **$200M of the $300M guidance raise is attributed to the pending Contentful and Fin acquisitions**, not organic growth.
  ([Salesforce investor relations](https://investor.salesforce.com/news/news-details/2026/Salesforce-and-Anthropic-Announce-Claudeforce-The-1-AI-Meets-the-1-AI-CRM)) ⟨daily 2026-08-27⟩

- **Anthropic opened a research preview of the Model Hardware Standard (MHS) on 08-27 — a model-agnostic specification for AI agents to operate physical devices with a programmable interface (microscopes, liquid handlers, robotic arms), developed with HHMI Janelia Research Campus and shared first with scientific labs and advanced manufacturers "ahead of making the standard open source."** Anthropic's own claim is that MHS cuts hardware integration from weeks or months to hours or minutes and lets agents run round-the-clock experiments, updating parameters in real time and in some cases recovering from hardware errors unaided; the MCP playbook — a shared protocol that becomes the default layer — extended from software tools to physical equipment. **Both The Rundown AI and TLDR AI led their 08-28 editions with it, and this map had nothing** — the clearest double-benchmark miss of the week, on the thread whose question is exactly where the lab-owned product surface goes next. ⚠️ Research preview with named partners, not a shipped product; no adoption number. ([Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview), [The Rundown AI](https://www.therundown.ai/articles/every-machine-is-about-to-speak-claude)) ⟨daily 2026-08-29⟩

## 2026-08-26 — Claudeforce puts the CRM inside the model, not the model inside the CRM

- **Salesforce and Anthropic announced "Claudeforce," a 37-skill Salesforce
  plugin running inside Claude** — deal-health review, pipeline updates and
  meeting prep against live CRM data from Claude's own interface, in pilot now
  with a broader beta in September. Announced 16:00 ET, timed to Salesforce's
  Q2 FY2027 earnings call. **The direction of travel is the development, not the
  feature list**: the enterprise application is moving inside the model's
  surface rather than calling the model from within the application, which
  inverts the integration pattern every vendor on this thread has used so far.
  ([Salesforce IR](https://investor.salesforce.com/news/news-details/2026/Salesforce-and-Anthropic-Announce-Claudeforce-The-1-AI-Meets-the-1-AI-CRM/default.aspx),
  [CNBC](https://www.cnbc.com/2026/08/26/salesforce-anthropic-partnership-claudeforce.html))
  ⟨daily 2026-08-26⟩

## 2026-08-25 — First live development since the thread opened: Anthropic merges memory across chat and its agent product

- **Anthropic merged the memory systems of Claude Chat and Claude
  Cowork, so context learned in one surface carries into the other** —
  and moved memory from an end-of-conversation summarisation step to
  continuous updating during a conversation. Users can view, edit and
  delete stored memories; sensitive categories (health, race, ethnicity,
  religion, politics, gender identity) are excluded by default behind an
  opt-in toggle, and government IDs, SSNs and criminal history are never
  stored. It is on by default across Free, Pro and Max, on web, desktop
  and mobile, at no extra cost. **This is the packaging pattern this
  thread was opened to track, applied to state rather than to
  capability:** the agent product and the chat product stop being two
  places you have to brief separately, which is the friction that keeps
  an agent surface from becoming the place work actually lives. No seat
  or adoption numbers disclosed — the disclosure question this thread
  watches stays unanswered.
  ([TechCrunch](https://techcrunch.com/2026/08/25/claude-cowork-finally-remembers-what-you-told-the-app-in-chat/))
  ⟨daily 2026-08-25⟩

## 2026-08-25 — Thread opened, backfilled from the 2026-08-20 coverage-critic catch

- **Opened on Ben's promotion of a candidate the map's own 2026-08-25
  weekly retrospective found: offered twice (08-20, 08-21) during the
  week it surfaced and dropped by inaction, not a ruling.** The case: on
  2026-08-20, five confirmed coverage-critic misses landed in one day,
  all on the same axis, with zero overlap with anything this map already
  tracked — the heaviest single-day miss count on record.
- **Anthropic bundled computer use, browser access, versioned Skills and
  a reusable Files API into a single production-agent surface for
  enterprises** — the pieces existed separately; what shipped is the
  packaging, which is what turns a demo capability into something a
  company can build a workflow on. ([Anthropic](https://claude.com/blog))
  ⟨merged 2026-08-25, originally daily 2026-08-20⟩
- **Google folded Antigravity, its coding-agent product, into eligible
  Gemini Enterprise Standard and Plus subscriptions**, with IDE
  extensions for VS Code (GA), Visual Studio, JetBrains and Zed
  (preview), plus unified billing, spend/quota controls, and audit
  logging — putting a coding agent inside seats enterprises already pay
  for. ([Google
  Cloud](https://cloud.google.com/blog/products/ai-machine-learning/expanding-google-antigravity-for-enterprise-customers))
  ⟨merged 2026-08-25, originally daily 2026-08-20⟩
- **Slack launched code channels, where teams plan, write and review
  software alongside AI agents inside Slack itself**, with GitHub,
  Anthropic and Vercel integrated as named partners. ([Slack](https://slack.com/blog))
  ⟨merged 2026-08-25, originally daily 2026-08-20⟩
- **Harvey released "Harvey Tenet," its first post-trained open-weight
  legal model, specialised for diligence and document review — built,
  per the benchmark that carried it, on Kimi K3.** Cross-references
  `kimi-distillation-fight`: an American legal-AI vendor post-training
  on Kimi K3 the same week Washington accused Moonshot of distilling a
  US frontier model to build it. ([Harvey](https://harvey.ai/blog))
  ⟨merged 2026-08-25, originally daily 2026-08-20⟩
- **Mistral shipped Agentic Search, giving a model five tool-like
  actions — search, open, navigate, read, grep** — the one item of the
  five that already had a thread to land on. Full detail on `mistral-ai`.
  ([Mistral](https://mistral.ai/news/agentic-search))
  ⟨merged 2026-08-25, originally daily 2026-08-20⟩
