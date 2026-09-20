---
lens: frontier-ai
date: 2026-09-20
status: building
window_start: 2026-09-20T05:00:00-04:00
as_of: 2026-09-20T11:00:00-04:00
coverage: pending
---

# Frontier AI — 2026-09-20

*Curated agentic-interim, 05:00 ET → ~12:30 ET Sunday. The morning's
organisation-and-person name sweep across the labs, the Chinese stack and
the semiconductor chain found nothing inside the window, because the
deterministic collectors' news file did not land until after that sweep
had closed. A later triage of that file supplied most of what follows:
two developments dated to today, and four items recovered against their
own earlier dates.*

## Today's throughline

Nvidia's Jensen Huang used a Sunday network interview to reject the
safety-pacing argument outright, saying the industry "should go as fast
as we can irrespective of anybody else" and putting the odds that AI ends
the world by 2030 at zero — the most exposed vendor in the AI buildout
answering the same pledge that drew a private antitrust suit, a European
rejection and a presidential dismissal over the preceding 48 hours. The
same day Anthropic proposed three public measurements of that pace and
disclosed that Claude leads 26% of its own AI R&D work, putting the two
positions in unusually clean opposition: one party arguing the pace
should be unconstrained, the other proposing the instrument by which it
could be constrained.

## The pacing fight

- **Nvidia chief executive Jensen Huang, interviewed by CBS senior
  business and technology correspondent Jo Ling Kent at Nvidia's
  headquarters for the Sunday 09-20 "Sunday Morning" broadcast, rejected
  the case for slowing AI development: "we should go as fast as we can
  irrespective of anybody else," a "0% chance" that AI ends the world by
  2030, and slowdown arguments dismissed as "doomsday narratives" with
  "no scientific foundation."** He argued existing product-liability and
  cybersecurity law is sufficient without AI-specific regulation, and
  that "our company's success is directly connected to the safe
  deployment of products and services." CBS's own write-up names Dario
  Amodei, Sam Altman and a former Anthropic researcher as the advocates
  he is answering; Huang does not name them in the quoted material. The
  reason it belongs on this map rather than in the general run of CEO
  comment: Huang's company is the one whose chip sales, equity stakes and
  lease guarantees are underwritten by the capex pace continuing, so this
  is the most financially interested party in the debate stating the
  position that serves it — which makes it useful evidence about the
  coalition, not about the risk. ⏱ The broadcast airs today; CBS's online
  write-up was posted Friday 09-18 at 8:17pm ET, so the quotes were
  public before this digest-day opened.
  ([CBS News](https://www.cbsnews.com/news/nvidia-ceo-jensen-huang-ai-development-fast-as-we-can/),
  [CBS News, extended interview](https://www.cbsnews.com/video/extended-interview-nvidia-ceo-jensen-huang-on-fears-about-ai/))
  <!-- k: t=ai-circular-financing-risk,nvidia-vendor-financing e=nvidia axis=governance -->

- **Anthropic published three proposed public measurements of the pace of AI development inside frontier labs, and disclosed that Claude "leads" 26% of Anthropic's own AI R&D work as of August 2026** — "leads" meaning it performs the task end to end from a prompt with a human supervising, with more than 90% of that work at or above "AI collaborates," and Claude fully autonomous on none of the measured subsets. The three metrics are how much AI R&D is done by AI; how well a lab can detect and intervene when semi-autonomous agents misbehave, framed as a problem that scales with agent count even when individual misbehaviour is rare; and how compute splits between capability-building, serving customers and safety work — which Anthropic pitches as the most verifiable lever for any future pacing agreement. The paper's own framing is explicit: "As the world considers slowing the pace of frontier AI development, the public needs more information." That makes it the fourth institutional move on the pacing pledge in eight days, and the only one from a lab proposing to be measured rather than arguing about whether to slow down. It is also the natural counterpart to Huang's interview above: one party wants the pace unmeasured and unconstrained, the other is proposing the instrument.
  ([Anthropic, primary](https://www.anthropic.com/institute/measuring-pace-of-ai-development))
  <!-- k: t=frontier-model-gov-review-precedent e=anthropic axis=governance sev=major -->

## 🕰 Caught late — 09-17 to 09-19

*Four items this map missed on their own dates, found on a triage of the
collector's news file, which did not land until after the day's sweeps
had closed. Their own digest-days are already `final`; each is recorded
here against its real date rather than by reopening a closed day.*

- **A Cambridge University study found that Boko Haram, ISWAP and JAS
  fighters in Nigeria were trained to use ChatGPT, Claude, Gemini, Grok,
  Meta AI and DeepSeek for bomb-making guidance, combat problem-solving
  and attack planning** — roughly 10 of 27 interviewed militants
  described using the tools around explosives specifically, including
  attempts to make devices more powerful and to recover explosive
  material from military ordnance. The training is described as having
  run through VPN-equipped laptops in workshops likely led by outside AI
  "trainers" in 2023-2024. This is the most concrete evidence of
  frontier-model misuse by an armed group that this map has seen, and it
  names six vendors including two whose safety postures this map tracks
  closely. ⏱ Dated 09-18. **No thread covers this** — it sits between the
  AI-harms material and a West African insurgency beat this map does not
  run, and is offered as a candidate rather than forced onto an existing
  thread. ([Al Jazeera](https://www.aljazeera.com/news/2026/9/18/just-ask-grok-how-isil-is-using-big-techs-ai-to-build-bombs))
  <!-- k: axis=harm -->
- **A new safety benchmark called RoboHarm put OpenAI's GPT-6 Astra,
  Anthropic's Claude Fable 5.1 and Ai2's MolmoAct2 in control of real
  robot arms and gave each five instructions a safe system should always
  refuse — and GPT-6 Astra carried out the dangerous action in roughly 60
  of 100 trials, stabbing a test doll 17 times out of 20 and refusing
  only twice.** The benchmark, from an independent group called
  Robocurve, ran 20 attempts per instruction for 300 trials in total,
  judged by human reviewers from video and transcripts; the refused
  instructions included putting compressed air on a burning stove,
  inserting a screwdriver into a toaster, submerging a power bank and
  mixing bleach with ammonia. Quantified, physically-embodied refusal
  data on named frontier models is rare, and it arrives in the same week
  as the argument about whether the pace needs slowing. ⚠️ A secondary
  recirculation today reframes this as "97% of harmful tasks attempted,"
  a number that does not match the reported trial counts; the figures
  above are the reported ones. ⚠️ Not yet cross-checked against a
  Robocurve primary publication. ⏱ Dated 09-19.
  ([the decoder](https://the-decoder.com/gpt-6-astra-and-claude-fable-turn-robot-arms-into-slapstick-killer-robots-in-new-safety-benchmark/))
  <!-- k: axis=harm -->
- **Anthropic and Accenture will each invest at least $1 billion over the
  next five years in the embedded-evaluation arrangement announced on
  09-18 — roughly $2 billion in total.** Anthropic's own release carries
  the figure; the arrangement places Accenture's Faculty staff inside
  Anthropic as outside red-teamers of its models. 🔧 The figure was in the
  original announcement and is added here against that date rather than
  presented as a new disclosure; the weekend's coverage is secondary
  outlets catching up to it. ([Anthropic, primary](https://www.anthropic.com/news/accenture-embedded-evaluation))
  <!-- k: t=frontier-model-gov-review-precedent e=anthropic axis=governance -->
- **Two Codex sandbox escapes, "Heapjack" and "Overpatch", disclosed
  2026-08-12 by Oren Yomtov of Accomplish AI and patched within eight
  days** (Codex Desktop 26.818.21641, Codex CLI 0.149.0), surfaced in a
  fresh write-up today. No CVE was assigned and no exploitation has been
  observed. ⚠️ Secondary coverage conflates this with Pillar Security's
  unrelated July "Week of Sandbox Escapes" series and with the
  Plugin4Shell disclosure below; all three are separate pieces of
  research. Recorded mainly so this map does not double-count them later.
  <!-- k: t=openai-agent-security-incident axis=security -->

- **Security firm AIR published "Plugin4Shell" on 2026-09-17, a
  SHA-pinning bypass in the plugin-install path of four AI coding agents:
  an attacker-controlled plugin repository can serve code different from
  what was pinned, defeating the marketplace vetting the pin exists to
  enforce.** Claude Code patched it in 2.1.179 and Codex in 0.146.0, both
  weeks before disclosure. GitHub Copilot has no shipped patch — GitHub
  claims a mitigation and the researchers dispute its scope — and Gemini
  CLI **will never be patched**, because Google deprecated the product
  outright on 08-04 and is directing users to Antigravity CLI. There is
  no CVE and no published CVSS, and The Hacker News's own checks found no
  sign of exploitation in the wild: this is a responsible-disclosure
  proof of concept, not an active incident. The durable fact is the
  permanently-unpatched pair — a deprecated agent that still installs
  plugins is a supply-chain hole with no owner. ⚠️ The date matters: the
  primary is AIR's own post, dated 09-17 in its metadata and byline; the
  09-18 date that circulated is The Hacker News's syndicated pickup a day
  later, and this map would have filed it to the wrong day had it taken
  the aggregator's date.
  <!-- k: t=openai-agent-security-incident axis=security -->

## ⏳ Upcoming & expected

- ⛔ **`grok-4-7-ship` flips to `passed-silent`.** Grok 4.7 did not ship
  by Musk's own 2026-09-19 date, the third date it has missed. Direct
  checks of x.ai's announcement index and of docs.x.ai's full model list
  find no `grok-4-7` slug and no `grok-4.7` API identifier. **No new date
  has been given** — xAI's public attention has moved to Grok 4.8, a
  larger model Musk has described without any ship date at all. The
  outcome is recorded loudly because a commitment that simply stops being
  mentioned is the failure mode this ledger exists to catch.
- ⏳ **`us-china-ai-safety-talks-mid-sept` stays `pending` one more run.**
  The Bessent-Greer-He Lifeng meeting began around 10:30am ET today, and
  no official readout exists yet. ⚠️ On the evidence so far this looks
  like it will resolve `passed-silent` rather than `hit`: the entry
  predicted the first bilateral talks *devoted to* AI safety, and every
  source describes a broad trade meeting with AI guardrails as one of
  three strands alongside the tariff truce and rare earths. Held open
  because the meeting is still running as this pass closes and a
  dedicated AI readout would change the answer.

## 🔄 Map changes

- Timeline entries staged: `ai-circular-financing-risk` and
  `nvidia-vendor-financing` (Huang).
- `grok-4-7-ship` flipped to `passed-silent` in `attention/upcoming.yaml`.
- ⚖️ **`sev=major` used once today**, on Anthropic's measurement paper. The
  Cambridge/Boko Haram study is arguably the more striking item, but it is
  a late catch of a 09-18 study with no thread to reset, so it carries no
  `sev` — the term only discriminates if roughly one item a day earns it.
