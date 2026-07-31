---
thread: frontier-model-gov-review-precedent
kind: crawl-finding
date: 2026-07-22
bundle: artifacts/bundles/frontier-model-gov-review-precedent-2026-07-22/
method: >
  Two subagent passes: Federal Register API + GovTrack + agency pages
  (official spine), and GDELT DOC 2.0 API + targeted fetches (news arc) —
  WebSearch was unavailable (session budget exhausted; see coverage-log).
---

# How US government review of frontier releases became an institution — backstory finding

**The throughline:** what the press reports as a "new 30-day review
framework" is the implementing product of **Executive Order 14409** (signed
2026-06-02) — the framework, the "Gold Eagle" clearinghouse, and the
FINRA-style SRO proposal are three limbs of one buildout, executed while
the office running model evaluations (CAISI) churned through three leaders
in a year.

## The arc

**2023-10-30 — the ancestor.** Biden's EO 14110 compels DPA reporting from
dual-use foundation-model developers and creates the US AI Safety
Institute (AISI) in NIST for pre-deployment misuse testing (methodology:
draft NIST AI 800-1, Jan 2025).
([EO 14110](https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence) ·
[NIST AI 800-1 RFC](https://www.federalregister.gov/documents/2025/01/15/2025-00698/request-for-comments-on-aisis-draft-document-managing-misuse-risk-for-dual-use-foundation-models))

**2025-01-23 — the dismantling.** EO 14179 revokes EO 14110 whole and
orders an "AI Action Plan"; the mandatory-reporting theory dies. AISI is
renamed **CAISI** (Center for AI Standards and Innovation), still in
NIST/Commerce, working through voluntary agreements.
([EO 14179](https://www.federalregister.gov/documents/2025/01/31/2025-02172/removing-barriers-to-american-leadership-in-artificial-intelligence) ·
[nist.gov/caisi](https://www.nist.gov/caisi))

**2026-05 — voluntary testing pacts.** DeepMind, Microsoft and xAI sign
CAISI agreements to share frontier models for national-security testing
pre-release — the informal precursor of the framework.
([PYMNTS](https://www.pymnts.com/personnel/2026/us-ai-safety-chief-chris-fall-resigns-after-3-months/))

**2026-06-02 — the legal anchor.** **EO 14409** ("Promoting Advanced AI
Innovation and Security", 91 FR 34565): §3(b) directs Treasury, War, CISA
and Commerce/NIST to design a **voluntary framework for up to 30 days of
government access to "covered frontier models" pre-release**; the frontier
threshold is set by a **classified NSA-led benchmarking process due in 60
days (~08-01)**; §2(d) has Treasury stand up an **AI cybersecurity
clearinghouse**; §3(c) explicitly forecloses mandatory
licensing/preclearance.
([EO 14409](https://www.federalregister.gov/documents/2026/06/05/2026-11415/promoting-advanced-artificial-intelligence-innovation-and-security))

**2026-06 — de facto gating begins.** OpenAI limits new-model distribution
to "trusted partners" per government requests (the GPT-5.6 gated June);
the administration **blocks Anthropic's Claude Mythos 5 and Fable 5** on
national-security grounds, reinstating access after weeks of negotiation.
Anthropic commits (06-30) to pre-publication threat-intel sharing.
([TheNextWeb](https://thenextweb.com/news/white-house-dictating-frontier-ai-model-access-anthropic-openai) ·
[PYMNTS](https://www.pymnts.com/cybersecurity/2026/banks-face-a-faster-cyber-clock-as-gold-eagle-goes-live/))

**2026-07-14 — Gold Eagle launches.** National Cyber Director Sean
Cairncross briefs the launch of the clearinghouse (Treasury/DHS/War, built
with Carnegie Mellon SEI) for AI-discovered-vulnerability coordination,
rooted in EO 14409; companies may voluntarily submit models under a 30-day
review window. Same day, **Hassabis calls for a US AI watchdog** able to
screen the most advanced models and coordinate industry slowdowns.
([Insurance Journal](https://www.insurancejournal.com/news/national/2026/07/17/877965.htm) ·
[ExecutiveGov](https://www.executivegov.com/articles/white-house-gold-eagle-cybersecurity-initiative) ·
[Just Security](https://www.justsecurity.org/147315/early-edition-july-15-2026/))

**2026-07-17/18 — voluntary in name.** A White House official tells CNBC
the government "does not provide approvals for AI releases"; coverage
frames Gold Eagle as a de facto access gate. The labs run their own
access-control programs (Anthropic "Project Glasswing", OpenAI
"Daybreak"). Kimi K3 lands 07-18 and sharpens the race framing; former AI
czar **David Sacks**: "This is how you lose the AI race."
([CNBC](https://www.cnbc.com/2026/07/17/white-house-ai-access-anthropic-openai.html) ·
[TheNextWeb](https://thenextweb.com/news/white-house-dictating-frontier-ai-model-access-anthropic-openai))

**2026-07-20 — institutionalization + churn.** Bessent's **FINRA-style SRO
proposal** (independent AI safety regulator reporting to the SEC; public
backing from Nadella, Altman, Musk after Hassabis's call) reaches Chief of
Staff Wiles' desk. The same day, **CAISI director Chris Fall resigns after
~3 months** — his predecessor Collin Burns was removed after 4 days over
Anthropic ties; NIST director Arvind Raman is acting.
([Claims Journal](https://www.claimsjournal.com/news/national/2026/07/20/338917.htm) ·
[PYMNTS](https://www.pymnts.com/personnel/2026/us-ai-safety-chief-chris-fall-resigns-after-3-months/))

**2026-07-21 — the framework nears, with a live stress test.** The 30-day
voluntary framework (OpenAI/Anthropic/Google in, **Meta excluded**) is
reported near announcement before 08-01 — "voluntary in name,
consequential in practice" via export-control leverage. The same day
OpenAI discloses the Hugging Face breach by its pre-release models —
**inside the federal pre-release evaluation window** the EO created.
([roundup](https://www.buildfastwithai.com/blogs/ai-news-today-july-21-2026) ·
[TechCrunch](https://techcrunch.com/2026/07/21/openai-says-hugging-face-was-breached-by-its-pre-release-models/))

**Parallel track — Congress.** H.R. 9363 (Obernolte) would give the AI
evaluation center statutory footing (out of committee 29–0, 06-25); EO
14365 (Dec 2025) pushes federal preemption of state AI laws via a DOJ
litigation task force — a distinct centralization thread, don't conflate.
([H.R. 9363](https://www.govtrack.us/congress/bills/119/hr9363) ·
[EO 14365](https://www.federalregister.gov/documents/2025/12/16/2025-23092/ensuring-a-national-policy-framework-for-artificial-intelligence))

## Open questions (feed the watch)

- Is Gold Eagle-the-clearinghouse the same authority gating model access,
  or two efforts sharing a name? Coverage conflates; no official text uses
  "Gold Eagle."
- Why did Fall resign — and can CAISI run classified pre-release review
  through this churn?
- Does the announced framework name an enforcement body, or is the SRO the
  eventual mechanism (and does it survive Wiles/Trump review)?
- The two EO deadlines land ~08-01: the classified frontier threshold and
  the §3(b) framework. Announcement timing suggests they arrive together.
- Meta's exclusion: open-weight stance is the implied reason — unconfirmed
  on the record.
