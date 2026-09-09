---
lens: mental-health
date: 2026-09-09
status: building
window_start: 2026-09-09T05:00:00-04:00
as_of: 2026-09-09T15:00:00-04:00
coverage: pending
---

# Mental Health — 2026-09-09

*Curated agentic-interim, 05:00 ET → 15:00 ET Wednesday. Sources: a
ClinicalTrials.gov v2 API sweep over the day's buffer, a trade-press sweep
(WUSF, WFSU, CBS Miami, NBC Miami, News4Jax) on the Florida AG chatbot-
liability story, HHS.gov for the FDA leadership appointment, and trade
coverage (BioPharma Dive, Clinical Trials Arena, GeneOnline) on Definium's
second Phase 3 trial.*

## Today's throughline

The `ai-therapy-regulatory-reckoning` thread moved on two fronts at once.
Florida's proposed chatbot-liability law, single-sourced yesterday, is now
carried by four independent outlets with real teeth added — criminal
penalties, state suspension of a company's Florida operations, and a
distinct medical-licensure angle via the state Board of Medicine — while
still short of an actual bill. And the federal side the thread has been
waiting on since the FDA's 08-23 promise of generative-AI guidance got its
first named owner: HHS announced Jared Seehafer as the FDA's first-ever
Deputy Commissioner for Technology and Artificial Intelligence. Elsewhere,
the evidence lane's next dated test came into view — Definium's second
Phase 3 psychedelic trial expects topline results this month — and the
day's ClinicalTrials.gov batch was, as usual, background-tier registry
noise rather than anything practice-changing.

## Policy, regulation & legal

- **Florida's AG chatbot-liability plan is now multi-sourced, with new
  specifics sharpening what was single-sourced reporting yesterday.**
  WUSF, WFSU, CBS Miami and NBC Miami each ran independent 09-08/09-09
  pieces on Attorney General James Uthmeier's proposal, adding detail the
  original News4Jax report did not have: the plan would allow **criminal**
  penalties, not just civil ones; remedies could include **state
  suspension** of a company's activity in Florida; and Uthmeier says he
  will work with the state Board of Medicine on rules for chatbots
  practicing medicine without a license — a distinct medical-licensure
  angle separate from the liability plan itself. ⚠️ Still no bill text or
  bill number located anywhere in this coverage — the scope described
  remains the AG's own characterisation of an announced intent, not
  statutory language, and that gap is unchanged from yesterday.
  ([WUSF](https://www.wusf.org/), [CBS Miami](https://www.cbsnews.com/miami/), [NBC Miami](https://www.nbcmiami.com/), [WFSU](https://www.wfsu.org/))
  <!-- k: t=ai-therapy-regulatory-reckoning,state-therapy-chatbot-bans axis=policy -->

- **HHS named the FDA's first-ever Deputy Commissioner for Technology and
  Artificial Intelligence, giving the agency's promised generative-AI
  guidance a named owner for the first time.** Jared Seehafer, a former
  life-sciences compliance-software CEO (Enzyme) rather than a clinician,
  fills the newly created role; HHS's 09-08 release also names three other
  senior FDA leadership picks (CDER, CBER, CTP directors). This is the
  concrete follow-through on the FDA's own 08-23 statement to STAT that
  formal generative-AI guidance was coming — a promise this thread has
  been carrying as unaddressed since then, and one that now has a specific
  federal official responsible for it.
  ([HHS.gov](https://www.hhs.gov/))
  <!-- k: t=ai-therapy-regulatory-reckoning axis=policy -->

## Research & evidence

- **Definium's second Phase 3 trial for DT120 — "Panorama," in generalized
  anxiety disorder — is reported to expect topline results this month.**
  Multiple trade outlets (BioPharma Dive, Clinical Trials Arena,
  GeneOnline) describe the trial design change alongside the timing: a
  low-dose 50µg arm was added specifically to counter functional
  unblinding (the problem of patients and raters guessing who got the
  active drug from its subjective effects), a methodological response to
  exactly the kind of blinding critique this lens has tracked on
  psychedelic trials generally. No exact date given, only "September
  2026." This is the next evidentiary test on the `psychedelic-regulatory-
  sprint` sub-thread, arriving ahead of the already-tracked 09-14 FDA
  public hearing. Logged to `attention/upcoming.yaml` as a month-precision
  entry. ⚠️ Trade-press synthesis of the company's own trial framing, not
  an independent read of a filing or publication.
  <!-- k: t=psychedelic-regulatory-sprint,mh-evidence-watch axis=evidence -->

## 🧪 Clinical trials

ClinicalTrials.gov v2 API buffer for 09-09 (407 rows; the buffer still
carries no `StudyFirstPostDate` field, so new registrations can't be
distinguished from record edits — a known, already-flagged gap, not
re-raised here). Title-filtering surfaced a handful of relevant
registrations, all registry entries with no results and none
practice-changing:

- **NCT07810348** — AI-Integrated Proactive Thought Control Intervention
  for Young Adults With Social Anxiety Disorder. Feeds
  `ai-therapy-regulatory-reckoning` / `mh-evidence-watch`.
- **NCT07105397** — Evaluating Conversational AI for Depression
  Management. Same relevance.
- **NCT06885996** — Psilocybin-Assisted Therapy for PTSD in IPV
  Survivors. Feeds `psychedelic-regulatory-sprint`.
- **NCT06615908** — Psilocybin-Assisted Therapy for Persisting Symptoms
  After Concussion. Same.
- **NCT06713616** — PCORI-funded (independent, not sponsor money)
  comparative-effectiveness study, esketamine (Spravato) vs. ketamine —
  directly useful for the evidence-vs-sponsor-claims question this lens
  keeps flagging on psychedelic/dissociative trials generally.
- **NCT07552909** — RCT of Home-based Digital Therapy for ADHD in
  Children. Feeds the digital-therapeutics thread.
- **NCT06928935** — Digital DBT for Youth at Clinical High Risk for
  Psychosis. Same.

Six more small academic registrations (an opioid-use-disorder digital
tool, neuromodulation for MDD/schizophrenia, a cancer-survivor depression
referral pathway, and veteran/youth suicide-prevention peer programs —
NCT07810322, NCT07768397, NCT07806877, NCT07091968, NCT07286383,
NCT07680179) are background-tier and not individually digest-worthy,
consistent with how a similar batch was treated on 09-08.

## ⏳ Upcoming & expected

- **No flips on this lens today.**
- 📋 **`fda-psychedelic-public-hearing` (due 09-14, 5 days out)** —
  confirmed, Federal Register citation 2026-14155, docket
  FDA-2026-N-7542, 12:30–16:30 ET. Definium's Panorama topline (see
  Research & evidence, above) is now the second dated evidentiary marker
  landing ahead of it this month.
- Otherwise pending on this lens's threads: `mhpaea-replacement-rule`
  (due 2026-12-31, month precision) — nothing due within the next 7 days.

## 🔄 Map changes

- **None new.** The FDA Seehafer appointment is tagged to the existing
  `ai-therapy-regulatory-reckoning` thread rather than opened as its own —
  it is a named-owner follow-through on that thread's already-tracked
  08-23 FDA-guidance promise, not a new development in its own right.

## 🧵 Thread candidates

**None offered.** Today's items all route to threads the map already
runs.

---
Florida's AI-liability plan for chatbots picked up real teeth today —
criminal penalties, state suspension — across four new outlets, still
without a bill. The FDA named its first AI deputy commissioner, giving
its generative-AI guidance promise an owner. And the next psychedelic
trial readout, this one in anxiety, is due this month.
