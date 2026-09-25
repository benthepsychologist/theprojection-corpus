---
lens: frontier-ai
date: 2026-09-25
status: building
window_start: 2026-09-25T05:00:00-04:00
as_of: 2026-09-25T10:00:00-04:00
coverage: pending
---

# Frontier AI — 2026-09-25

*Curated from the Friday-morning collector lanes that had landed by 10am ET
(rss, github; today's google_news_rss had not yet landed), Friday-morning
issues of The Rundown AI, TLDR AI and The Neuron, primary-source pages
(Microsoft, Anthropic, China's MFA) and wire coverage (agentic-interim).
Window: 05:00 ET → about 10:00 ET Friday. Thursday's news, including the
evening China MFA readout of the Trump-Xi talks and the Akamai-Anthropic
compute deal, is in the 2026-09-24 digest, finalized today.*

## Today's throughline

Microsoft rebuilt its Copilot app around Home, Code and Autopilot tabs, and US regulators issued a final finding of no significant environmental impact for restarting the former Three Mile Island Unit 1 reactor. Anthropic published an experiment in which 201 employees' Claude agents negotiated book trades on an internal marketplace. No outcome has been reported for Thursday's Warner-Schatz request for Senate consent to mandatory NSA testing of frontier models, and the White House has issued no readout of the Trump-Xi talks; China's own readout says only that the two leaders will continue a dialogue on AI and keep it under human control.

## Product & access

- **Microsoft unveiled a redesigned Copilot "super app" with three tabs — Home, Code and Autopilot — merging AI chat, an app/automation builder and a persistent agent that can keep working while the user is offline** — Code lets any user build an app, tracker or automation and share it as a cloud-hosted internal tool "powered by the same underlying technology as GitHub Copilot," while Autopilot is a cloud-based successor to Microsoft's Scout assistant that can watch Teams channels, run recurring tasks and handle follow-ups; Microsoft is moving to usage-based billing for Cowork, Code and Autopilot, tied to which models (including Astra and Fable) a task uses. CEO Satya Nadella called it "a new OS for work," and Microsoft is positioning it against Office's historical influence rather than against consumer agents like Muse. ([Microsoft](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/), [The Verge](https://www.theverge.com/news/1000532/microsoft-copilot-super-app-chat-coding-autopilot))
  <!-- k: t=enterprise-agent-product-race e=microsoft axis=product -->

## Research & safety

- **Anthropic published results from a summer experiment, Project Swap, in which 201 employees across six offices each gave a Claude-powered agent a five-minute conversation about their reading tastes and sent it to negotiate book trades against other employees' agents on an internal trading floor** — agents' book rankings matched their own person's stated preferences on 61% of pairs after the short chat, and re-running the trading floor with different models showed the underlying model mattered more to negotiating outcomes than the instructions given to it; Anthropic says the market fell short mainly because agents lacked information about participants, not because of how they traded, and frames the work as an early look at what markets built for AI agents will need (rules for entry, handling failed deals, visibility of activity). No exact publication date is given on Anthropic's page; it surfaced in Friday-morning trade coverage. ([Anthropic](https://www.anthropic.com/research/project-swap))
  <!-- k: e=anthropic axis=research -->

## Compute & buildout

- **The Nuclear Regulatory Commission and the Department of Energy issued a final environmental assessment and finding of no significant impact for restarting the Christopher M. Crane Clean Energy Center — formerly Three Mile Island Unit 1 — clearing an environmental-review step that began with a draft assessment in June** — the NRC is separately deciding whether to grant an exemption and three license amendments Constellation Energy requested to resume power operations through the reactor's 2034 license expiry, while DOE's Office of Energy Dominance Financing decides on a loan guarantee for refueling; Constellation cites its 2024, 20-year power purchase agreement to supply the 835-megawatt plant's output to Microsoft's data centers on the PJM grid. The environmental finding is not the license decision itself. ([Federal Register / NRC](https://www.federalregister.gov/documents/2026/09/25/2026-19603/constellation-energy-generation-llc-christopher-m-crane-clean-energy-center-environmental-assessment))
  <!-- k: t=nuclear-for-ai e=microsoft axis=capital -->

## ⏳ Upcoming & expected

- **Senate action on Warner and Schatz's pre-release AI-testing bill and Grassley's AI Whistleblower Protection Act — still no reported outcome.** Both senators sought unanimous consent Thursday afternoon; as of 10am ET Friday, no outlet had reported whether either request was made, granted or objected to on the floor.
- **Trump-Xi summit AI substance — resolved as "no operating rules."** China's Foreign Ministry readout (Thursday evening) has both leaders endorsing continued AI dialogue; no incident-notification channel, chip outcome or joint statement was confirmed, and no US government readout had appeared by 10am ET Friday. Full detail is in the 2026-09-24 digest.
- **Australia's OpenAI review** — the taskforce's rapid review continues to feed national AI standards due by year-end; no new development found this morning.
- **OpenAI DevDay, 09-29** — the reported $500-a-month ChatGPT Pro Max tier (see the 2026-09-24 digest) remains an unconfirmed leak; separately, Fortune reported Thursday evening that OpenAI plans to preview a cybersecurity-focused GPT-6 Cyber model "in the coming weeks," which a source says is a distinct release from the dozen-plus other products expected at DevDay itself.
- **09-30: California's deadline for Gov. Newsom to sign or veto pending bills**, AI bills among them; no signing or veto action found this morning.
- No expectation flips today; the ledger flips are the main session's.

## 🔄 Map changes

- Late triage (agent ZA) of the Friday google_news_rss lane and the AI-lens rows of sec_edgar, federal_register, semantic_scholar and clinicaltrials added one Friday item, a new Compute & buildout section for the NRC/DOE final environmental finding on the Crane Clean Energy Center (Three Mile Island) restart, and extended the DevDay ⏳ line with the GPT-6 Cyber report. Full detail staged in `buffer/sweeps/2026-09-25/ZA-frontier-ai.md`.

## 🧵 Thread candidates

- None new this morning.

---
A quiet Friday morning: Microsoft redesigned its Copilot app around chat, coding and a persistent agent, and Anthropic described a summer experiment in which employees' AI agents traded books on an internal marketplace. Thursday's open questions — the Senate's stalled AI-testing bill and the substance-free AI language from the Trump-Xi summit — remained unresolved as of 10am ET.
