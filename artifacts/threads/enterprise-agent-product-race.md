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

## 2026-08-29 — The adoption-number disclosure this thread has been waiting for arrives, from a bank

- **Citigroup's "Arc" platform was reported as the largest measured enterprise-agent deployment yet, with real usage figures attached**: 180,000 staff across 85 countries using its AI tools, 40,000 developers on the platform, 100,000+ agentic-development hours per week, service agents fielding 3M+ inquiries a year, a 30-40% developer-productivity gain, legacy-system migrations cut from 12 months to 4 weeks, and a 25% cut in servicing effort. Arc runs Cognition's Devin for agentic coding, with "Citi Sky" built jointly with Google Cloud/Google DeepMind — a bank running a coding agent from one lab inside a governance platform co-built with another. All outputs stay under human supervision; autonomous code or financial decisions are explicitly prohibited. ⚠️ **The figures trace to Citi's own May 7, 2026 Investor Day, not new data** — what's new 08-28 is Forkast framing it as the category's largest measured deployment and surfacing the numbers now.
  ([Forkast](https://forkast.news/citigroups-arc-platform-is-the-largest-measured-enterprise-agent-deployment-yet/)) ⟨daily 2026-08-29⟩
- 💡 **This is the disclosure this thread's own watch line named as unanswered** — "whether enterprise adoption numbers (seats, IDE installs) ever get disclosed." Every prior entry on this thread (Claudeforce, the Cowork/Chat memory merge, Antigravity, Slack code channels) shipped a product without a usage number attached. Arc is the first concrete count, even if the count itself is three-plus months old. ⟨daily 2026-08-29⟩

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
