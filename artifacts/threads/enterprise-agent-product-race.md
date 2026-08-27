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

## 2026-08-26 — Two enterprise pushes land the same day: Salesforce embeds Claude company-wide, Google verticalizes Gemini Enterprise for finance and legal

- **Salesforce and Anthropic announced "Claudeforce," making Claude the reasoning model behind Salesforce's Atlas Reasoning Engine and the default model for Agentforce Vibes and Agentforce Coworker, alongside a new "Salesforce in Claude" plugin carrying 37 prebuilt sales skills** (deal-health review, pipeline updates, meeting prep) that let sellers act on live Salesforce data from inside Claude itself. Announced as Salesforce opened its Q2 FY27 earnings call; in pilot now, open beta due September 2026, more prebuilt skills promised later in the year. Anthropic CEO Dario Amodei framed it as letting companies "point Claude at the customer information and business context they've been building in Salesforce for decades." Bidirectional embedding — Claude inside Salesforce, Salesforce inside Claude — is a sharper version of this thread's packaging throughline than a single-surface bundle. ([Salesforce, primary](https://www.salesforce.com/news/press-releases/2026/08/26/salesforce-and-anthropic-announce-claudeforce/), [CNBC](https://www.cnbc.com/2026/08/26/salesforce-anthropic-partnership-claudeforce.html), [VentureBeat](https://venturebeat.com/orchestration/salesforce-just-put-its-entire-crm-inside-claude-and-says-youll-never-need-its-app-again)) ⟨daily 2026-08-26⟩
- **Google Cloud shipped two industry-specific Gemini Enterprise editions, for financial services and legal, the same day.** The financial edition pairs a Google-managed "Financial Research" agent with 50+ specialized skills and 13 data connectors (FactSet, LSEG, Moody's, S&P Global, SEC EDGAR), with Deutsche Bank and CME Group as early adopters; the legal edition covers contract review, due diligence and regulatory monitoring via Docusign, iManage and Thomson Reuters integrations, with Cleary, Freshfields, Weil and Williams & Connolly as launch customers. Both are in global preview only — no GA date or pricing announced. Vertical-specific packaging, one layer down from the general-purpose platform bundling this thread already tracked from Google on 08-20. ([technode.global](https://technode.global/2026/08/26/google-gemini-enterprise-financial-legal/)) ⟨daily 2026-08-26⟩

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
