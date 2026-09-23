---
lens: mental-health
date: 2026-09-22
status: final
window_start: 2026-09-22T05:00:00-04:00
as_of: 2026-09-23T10:00:00-04:00
coverage: done
---

# Mental Health — 2026-09-22

*Curated from tiered dispatch (collectors + mental-health hot-cluster
agent), window 05:00 ET Tuesday → 05:00 ET Wednesday. The morning pass
(as of 10:30 ET) is extended with a Wednesday-morning agentic-interim
read of Tuesday's afternoon and evening: the British Columbia complaint
itself and its N.D. Cal. docket (CourtListener), the Legislature's own
bill-history pages for the four California bills, ClinicalTrials.gov's
API queried by condition and first-posted date, company newsrooms
(PR Newswire), and the trade-press front pages (BHB, Fierce Healthcare,
Psychiatric Times, STAT).*

## Today's throughline

British Columbia's lawsuit against OpenAI over the Tumbler Ridge school
shooting anchored the day: the complaint, filed with the local school
board as co-plaintiff, alleges OpenAI's own human reviewers recommended
alerting Canadian police in June 2025 and company leadership overruled
them, and by Tuesday afternoon a federal judge had begun steering it
toward the judge who already holds earlier suits against OpenAI's chief
executive. Around it the industry kept building AI into mental-health
care: Pelago put an AI intake front door on a new combined
substance-use and mental-health platform, and Rula formed an outside AI
safety council, while Talkspace collected a TIME listing and a Seattle
Times question about its city youth-therapy contract.

Nothing moved on the four California chatbot and AI-therapy bills still
awaiting the governor (deadline 09-30), and the Raine chatbot-death
coordination proceeding's next conference falls on Wednesday.

## Policy, regulation & legal

- **British Columbia's government sued OpenAI and Sam Altman in federal
  court (Northern District of California, filed Monday 09-21) over the
  February 2026 Tumbler Ridge mass shooting that killed 8 — alleging
  OpenAI's own safety team internally flagged the shooter's gun-violence
  conversations but never notified police, deactivated (not banned) his
  account, and that he continued using ChatGPT via a second account
  through the killings; the province says OpenAI has since refused to
  hand over the chat history.**
  This is the first government civil suit against OpenAI on this
  thread's docket, filed jointly with the local school board (see the
  complaint bullet below). It is not the first government plaintiff (see
  the 🔧 correction below).
  ([Al Jazeera](https://www.aljazeera.com/news/2026/9/22/canadas-bc-sues-openai-over-chatgpt-role-in-tumbler-ridge-school-shooting), [CP24](https://www.cp24.com/news/canada/2026/09/22/openai-refused-to-share-tumbler-ridge-shooters-chat-history-bc-attorney-general-says-while-filing-california-lawsuit/), [Bloomberg Law](https://news.bloomberglaw.com/artificial-intelligence/british-columbia-sues-openai-for-failure-to-warn-before-shooting))
  <!-- k: t=ai-therapy-regulatory-reckoning e=openai axis=policy -->
- **The province and the Peace River South school board pleaded eight
  counts against OpenAI and Altman, from negligent failure to warn law
  enforcement to aiding and abetting a mass shooting and strict product
  liability, resting on an allegation that OpenAI's human reviewers
  recommended a referral to the RCMP in June 2025 and company leadership
  rejected it.** The complaint (Case 4:26-cv-10743, 39 pages) seeks
  damages for the province's and school board's recovery costs (a
  replacement school and wellness centre, a trauma-informed care
  program, staff and police time), punitive damages, an injunction and a
  jury trial. Its account of the leadership override rests on OpenAI
  whistleblowers first reported by the Wall Street Journal; the chat
  logs themselves have not been produced, and the plaintiffs say they
  will amend once they are. It quotes Altman's April apology to the
  community ("I am deeply sorry that we did not alert law enforcement to
  the account that was banned in June") as an admission that OpenAI
  identified the risk and failed to act. Counsel for the plaintiffs
  includes Lesley Weaver of Stranch, Jennings & Garvey, also named as one
  of four plaintiffs' co-lead counsel in the California state-court
  ChatGPT coordination proceeding (JCCP 5431), per an account of the
  08-04 case-management order.
  ([BC complaint, via CourtListener](https://storage.courtlistener.com/recap/gov.uscourts.cand.479418/gov.uscourts.cand.479418.1.0.pdf), [CBC](https://www.cbc.ca/news/canada/british-columbia/bc-government-announce-update-openai-legal-action-9.7352395), [AI Recovery Collective on JCCP 5431](https://airecoverycollective.substack.com/p/where-things-stand-the-chatgpt-product))
  <!-- k: t=ai-therapy-regulatory-reckoning e=openai axis=policy -->
- **A federal judge on Tuesday 09-22 referred British Columbia's suit to
  the judge handling earlier suits against Altman to decide whether the
  cases are related.** Judge Kandis Westmore's referral order names
  Stacey v. Altman (3:26-cv-03701, filed 04-29) before Judge Jacqueline
  Scott Corley; the docket does not state that case's subject, but
  Corley is also assigned several of the Altman-defendant suits filed
  09-02, the Tumbler Ridge family wave. A summons and an initial
  case-management scheduling order issued the same day. If the cases are
  related, the province's claims would sit in front of one judge beside
  the families'.
  ([CourtListener docket](https://www.courtlistener.com/docket/74825372/his-majesty-the-king-in-right-of-the-province-of-british-columbia-v-altman/))
  <!-- k: t=ai-therapy-regulatory-reckoning e=openai axis=policy -->
- **Tom Siegel, who founded Google's trust-and-safety team, said he is joining Common Sense Media as executive director of its Youth AI Safety Institute and warned that AI could harm children more than social media did, citing suicide, psychosis and cognitive offloading.** The institute, launched in May and backed by Anthropic and the OpenAI Foundation, aims to build independent risk ratings for AI tools used by minors, "similar to car crash testing"; Siegel warned that companies that do not act risk lawsuits and regulation. ([Reuters](https://www.reuters.com/legal/litigation/ex-google-safety-chief-warns-ai-could-harm-children-more-than-social-media-did-2026-09-22/), [USA Today](https://www.usatoday.com/story/tech/2026/09/22/artificial-intelligence-children-harm/91891276007/))
  <!-- k: t=ai-therapy-regulatory-reckoning e=anthropic,openai axis=policy -->

## Product & market

- **Pelago, a virtual substance-use-care company, launched a behavioral-health
  platform on 09-22 that puts substance-use, mental-health and
  behavioral-addiction care on one contract and routes every member
  through Sona, its voice-first clinical AI.** Announced at the
  Behavioral Health Tech conference in Nashville. The company says two
  observational studies of more than 9,000 member conversations found
  nearly half of members starting in the clinical range improved by at
  least five points on the PHQ-9 or GAD-7 within about a month; those are
  company-run, uncontrolled analyses, not peer-reviewed, and the release
  pitches Sona as a substitute for default one-on-one therapy referral
  for lower-acuity members.
  ([PR Newswire](https://www.prnewswire.com/news-releases/pelago-launches-behavioral-health-platform-uniting-substance-use-mental-health-and-behavioral-addiction-care-302885519.html), [MedCity News](https://medcitynews.com/2026/09/pelago-unveils-new-behavioral-health-platform-for-substance-use-mental-health-and-behavioral-addiction-care/))
  <!-- k: t=mh-clinical-infra-funding,ai-therapy-evidence axis=product -->
- **Rula Health, a nationwide behavioral-health provider, formed an
  external advisory council on AI ethics and safety (Rula CARES) as it
  moves "from concept to development" of AI-enabled products.** The
  council of clinical, academic and AI experts, including Cornell Tech's
  Tanzeem Choudhury, meets quarterly and will do retrospective case
  review and forward guidance; Rula frames its AI as administrative
  support that keeps clinicians "at the center."
  ([PR Newswire](https://www.prnewswire.com/news-releases/rula-health-launches-rula-cares-external-council-for-ai-ethics-and-safety-in-behavioral-health-302885614.html))
  <!-- k: t=ai-therapy-regulatory-reckoning axis=product -->
- **Anthropic and OpenEvidence are rolling out a free, regionally adapted version of OpenEvidence's clinical decision-support tool to physicians in about 100 low- and middle-income countries, including Uganda, Angola, Sudan, Haiti and Mongolia, with Anthropic providing back-end technology.** Mental health is not named in the announcement, and Reuters noted critics' concern that systems trained mainly on high-income-country data may not fit local practice; no financial terms were disclosed. ([Reuters via Yahoo News](https://www.yahoo.com/news/articles/exclusive-anthropic-openevidence-partner-bring-213129315.html))
  <!-- k: t=bigtech-into-health e=openai axis=product -->

## Capital & corporate

- **Talkspace and its sister brand Wisdo by Talkspace were both named to
  the second annual TIME/Statista "World's Top HealthTech Companies 2026"
  list (announced 09-17)** — a reputation/financial-performance/engagement
  ranking alongside Spring Health and other names this thread tracks.
  ([BusinessWire](https://www.financialcontent.com/article/bizwire-2026-9-21-talkspace-awarded-on-times-list-of-the-worlds-top-healthtech-companies-2026-list), [TIME](https://time.com/article/2026/09/16/worlds-top-healthtech-companies-2026/))
  <!-- k: t=mh-clinical-infra-funding e=talkspace axis=capital -->
- ⚠️ **The same week, the Seattle Times published an investigation
  ("Seattle's Talkspace deal for youth therapy falls short") into the
  city's $14.55M Talkspace/DEEL partnership offering free virtual therapy
  to an estimated 55,000+ residents ages 13-24.** The article sits behind
  a hard paywall — repeated fetch attempts (including a Googlebot-style
  user agent) returned no body text — so only the headline claim and the
  program's known scale are confirmed here; the specific shortfall
  figures are **not independently verified**. Flagged for a follow-up
  crawl with paywall access.
  ([Seattle Times](https://www.seattletimes.com/seattle-news/mental-health/seattles-talkspace-deal-for-youth-therapy-falls-short/))
  <!-- k: t=mh-clinical-infra-funding e=talkspace axis=capital -->

## 🧪 Clinical trials

Mostly collisions, but not all. Of the 173 mental-health-tagged
registrations in Tuesday's collector file, the multi-term rows are
overwhelmingly false matches: "Cerebral telehealth" fires on
neurology and headache trials, "Spring Health" on a bladder-cancer and an
asthma trial, "SAINT depression" on oncology and rehabilitation studies,
"ACCESS Model" on lung-cancer-screening and HPV-education studies. The real
signal sat in single-term rows and in a direct ClinicalTrials.gov query
by psychiatric condition and first-posted date, which surfaced the items
below. All verified live on the registry.

- **[NCT07833761](https://clinicaltrials.gov/study/NCT07833761), first
  posted 09-22 — ADEPT, a University of Minnesota Phase 1 open-label
  study adding two 25 mg psilocybin sessions to standard dialectical
  behavior therapy for borderline personality disorder.** 18 participants
  planned, start estimated December; primary outcomes are safety,
  including acute suicidal ideation after dosing. Filament Health, whose
  president was slated to speak at the FDA's 09-14 psychedelics hearing,
  is a collaborator. Early proof-of-concept, no efficacy claim.
  <!-- k: t=psychedelic-regulatory-sprint axis=clinical-trials -->
- **[NCT07834762](https://clinicaltrials.gov/study/NCT07834762), first
  posted 09-22 — a UC San Diego sham-controlled trial of home-based,
  remotely supervised "spaced" transcranial direct current stimulation for
  treatment-resistant depression, with NIMH as collaborator.** 74
  participants planned, start estimated 10-15, primary outcome the
  Montgomery-Åsberg Depression Rating Scale, plus TMS-EEG mechanism
  measures. A home-delivered neuromodulation test on the thread's
  evidence-catch-up question.
  <!-- k: t=neuromodulation-evidence axis=clinical-trials -->
- Also first posted 09-22 and near the lens but not landmark:
  [NCT07833709](https://clinicaltrials.gov/study/NCT07833709), a
  60-person mindfulness-CBT smartphone intervention for misophonia at
  Sakarya University; and
  [NCT07834203](https://clinicaltrials.gov/study/NCT07834203), a
  500-person University of Minnesota observational study of early
  psychosis.

## ⏳ Upcoming & expected

- **No flips.** `raine-jccp-cmc-0923` is due Wednesday 09-23: the next
  case-management conference in the coordinated ChatGPT chatbot-harm
  proceeding (JCCP 5431, Judge Ethan Schulman, San Francisco). As of the
  Wednesday-morning read no order or minute entry from it was reachable
  (California's case search is interactive); the parties' last public
  description of the agenda (08-25) names an ESI protocol and a
  protective order. Confirming outcome is a docket read after the
  hearing.
- **California governor's deadline 09-30 — no action yet on any of the
  four tracked bills.** The Legislature's bill-history pages, read
  Wednesday morning, show AB 1979 (presented 09-04), SB 903 (09-09),
  AB 2575 (09-15) and SB 503 (08-30) all still sitting with the governor
  with no signing or veto entry, and the governor's newsroom carries
  nothing on them. (SB 1119, "Adam's Law," was signed 09-10.)
- `sword-headspace-acquisition-close-0914` still pending (10-01 close).
- Concord II coordination order ✅ hit (filed 09-18, granted 09-21;
  frontier-ai territory, cross-referenced).

## 🔄 Map changes

- Timeline entries: `ai-therapy-regulatory-reckoning` (BC government's
  OpenAI suit, morning; complaint detail, relatedness referral and Rula
  CARES, afternoon read), `mh-clinical-infra-funding` (Talkspace TIME
  listing + Seattle Times investigation; Pelago platform).
- 🔧 **Correction to the morning BC bullet.** It called the suit "a new
  plaintiff type" and "a new harm type" on this thread. Neither holds.
  A state government is already a plaintiff here (Pennsylvania v.
  Character.AI, filed 05-01; Florida's attorney general opened a criminal
  probe of OpenAI 04-21 per the complaint), and the Tumbler Ridge
  failure-to-warn theory has been on this thread since the 09-02 family
  suits. What is new is a government's civil damages suit against OpenAI
  itself, a school board as co-plaintiff, and the recovery-of-public-costs
  theory. The morning timeline entry also describes the complaint as
  "negligence"; it pleads eight counts, and "OpenAI has since refused to
  share the chat history" is the attorney general's statement, not a
  finding. "San Francisco" in the morning text is the court's county
  venue; the filing is in the Northern District of California (case
  number carries the Oakland-division prefix). Corrected in the
  `ai-therapy-regulatory-reckoning` timeline (headline, "negligence", and
  the new-plaintiff framing) on the 09-23 run.
- No thread opens or closes proposed by this pass.

## 🧵 Thread candidates

- **candidate:** AI chatbots and violence against third parties, split out
  of `ai-therapy-regulatory-reckoning` — Tumbler Ridge (30-odd family
  suits 09-02, the BC and school-board suit 09-21), the FSU-shooting
  wrongful-death suit and Florida's criminal probe and liability bill,
  and OpenAI's police-referral policy all share a "withheld warning"
  liability theory distinct from that thread's suicide and
  psychosis-product-liability core. Track it? (BC complaint
  ¶¶ 5-6, 41-45, 58; existing entries 09-02, 09-08, 09-09 on the
  reckoning thread)
- IIT Bombay's four-suicide charter/account-reversal candidate (offered
  09-20, reoffered 09-21) drops per the standing one-reoffer rule —
  unanswered, not promoted. Flagging here rather than silently losing
  it: still a real, distinct story (institutional duty-of-care, not an
  AI-chatbot harm) if Ben wants it picked back up.

---
British Columbia's lawsuit against OpenAI over the Tumbler Ridge shooting
anchored Tuesday: the complaint alleges OpenAI's own reviewers urged a
police referral and leadership overruled them, and a federal judge began
routing it toward the judge with the earlier suits.
Pelago and Rula each added AI to behavioral-health care, and Talkspace
collected a TIME listing alongside a Seattle Times question.
Nothing moved on the California bills, and the Raine conference is due
Wednesday.
