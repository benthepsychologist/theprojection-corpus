---
lens: mental-health
date: 2026-09-04
status: building
window_start: 2026-09-04T05:00:00-04:00
as_of: 2026-09-04T10:40:00-04:00
coverage: pending
---

# Mental Health — 2026-09-04

*Curated agentic-interim, 05:00 ET → **10:40 ET** Friday. Sources: the
deterministic lanes (`rss` 474 items including STAT, Behavioral Health
Business, Internet Interventions and Frontiers in Psychiatry;
`clinicaltrials` 346; `federal_register` 48; `google_news_rss` 7,812),
plus a regulatory/clinical/payer sweep, an evidence-and-big-tech sweep
reading the journals directly, and two buffer-triage passes. Material
dated 09-03 is folded into `2026-09-03-mental-health.md` as a 🌙 late
catch, together with this run's coverage critic.*

## Today's throughline

California's five AI and mental-health bills are still sitting unsigned on
the governor's desk, and nothing new broke on this lens between dawn and
mid-morning. The FDA newsroom and the Federal Register carried no
behavioural-health action, CMS was quiet, and the Tumbler Ridge and Grok
dockets show no new entries.

**The honest report is that this run's substance for this lens landed on
yesterday's record rather than today's.**

What the run did produce for this lens is a correction to how it reads its
own inputs. **Yesterday's digest read the day's clinical-trials buffer and
dismissed all 44 new registrations as "every one a term collision... no new
mental-health trial." At least six were real** — a ketamine plus
behavioural-activation trial for treatment-resistant depression, an
accelerated-TMS trial for treatment-resistant anxiety, a
neuromodulation-plus-sensor depression trial, a suicide-prevention RCT, a
digital parenting RCT, and a PTSD trial comparing CBT with mindfulness.
Several land on `neuromodulation-evidence`'s own stated TMS anchor. The
file was not unread. It was read and misjudged, which is the harder failure
and the one this run is now carrying a rule against. The full account is in
yesterday's digest and in `coverage-log.md`.

## Regulation & legislation

- **California's five AI/mental-health bills remain unsigned.** A live
  fetch of `leginfo.legislature.ca.gov` this morning confirms SB 903,
  SB 1119, AB 2575, AB 1979 and SB 503 all still sit on the governor's
  desk with no signature or veto. The ledger item stays open to 09-30.
  Recorded because a checked negative on a dated item is a real result,
  not an absence of one.
  <!-- k: t=state-therapy-chatbot-bans,ai-therapy-regulatory-reckoning axis=regulation -->
- **San Francisco's Board of Supervisors voted 11-0 to formally demand
  Kaiser Permanente withdraw its "Terrible Three" contract demands and
  negotiate in good faith.** ⚠️ Dated 09-01, out of this window — carried
  because it resolves an item the 09-03 digest explicitly left as "to
  verify next run," and because it escalates past July's procedural "heard
  and filed" hearing into a formal city position. Supervisor Chyanne Chen,
  who introduced it: "how we're taking care of our patients and workers,
  especially with emerging technology, is more important" than the
  procedural posture. Sourced to NUHW's own release and KALW.
  <!-- k: t=kaiser-ai-clinician-backlash e=kaiser-permanente axis=labor -->

## 🧪 Clinical trials

**The 09-03 batch is re-opened, not closed.** Six registrations wrongly
dismissed as term collisions yesterday are real and are named in the
09-03 digest's critic section. Today's `clinicaltrials` batch (346 items)
was read and is routine — new study postings, broad sponsor-text matches
on "Google," "Samsung," "AMD" rather than mental-health substance, no
results postings. **That verdict is offered with the caveat that the same
verdict was wrong yesterday**, and under the rule adopted from this pass:
entries matching multiple non-generic terms get checked against the live
registry before a batch is called empty. The ones checked here did not
survive that test as real; that is the difference from yesterday.

## ⏳ Upcoming & expected

- 🚧 `california-ai-mh-bills-0930` — open, all five unsigned on a live
  check this morning.
- 🚧 `meta-warner-csam-response` — remains passed-silent since 08-26 on the
  US side. ⚠️ Worth noting the asymmetry: **India's NHRC opened a formal
  two-week inquiry into the same allegations on 09-03** (see yesterday's
  digest). Senator Warner's letter has gone unanswered for two and a half
  weeks; the first actual regulatory consequence came from another
  jurisdiction.
- 📋 Nothing else dated for this lens before 09-15.

## 🔄 Map changes

- `+` watchlist term `Adam's Law` (critic-add) — the press's popular name
  for SB 1119, which this map tracks by bill number only. A number-only
  term set misses every story that uses the name, and on 09-03 most did.
- `✎` timeline entries merged on `kaiser-ai-clinician-backlash`,
  `meta-ai-csam-ads`, `canada-ai-vs-care`, `psychedelic-regulatory-sprint`,
  `neuromodulation-evidence`, `ai-therapy-evidence`.
- 📋 **Flagged, not acted on:** `psychedelic-regulatory-sprint` had gone
  three weeks without a timeline entry while real state-program and access
  news accumulated (New Mexico's program acceleration, a Rhelion Germany
  compassionate-use shipment). Today's UCSF result breaks the streak but
  does not clear the backlog; the thread wants a dedicated catch-up crawl
  rather than a daily sweep.

## 🧵 Thread candidates

- **The ABA billing-fraud and enforcement saga** *(coverage-critic argued)*
  — **ABA Centers of America is under active federal criminal
  investigation** for money laundering and healthcare and wire fraud, an
  escalation from the civil billing-fraud claims this lens logged a month
  ago, and **no thread holds the story**. Three escalating events now exist
  with nowhere to live. The critic's own recommendation is worth passing on
  verbatim: this may belong as a distinct **fraud-and-enforcement strand**
  rather than inside `mh-clinical-infra-funding`, because the money in it
  is negative — job cuts, Medicaid scrutiny, now DOJ attention — and that
  thread tracks capital going in. **Track it?**

## 🚨 Flash

**None.**

## ⚠️ Collection note

**A source-list gap worth recording.** Both of this run's real evidence
finds came from journals **not** on this lens's named list — Molecular
Psychiatry (a candidate EEG biomarker of Stanford Neuromodulation Therapy
response) and Behavioral Sciences (a 10-study meta-analysis finding no
significant difference in patient acceptance between AI-delivered and
conventional psychotherapy). The list currently names JMIR Mental Health,
npj Digital Medicine, Internet Interventions, Frontiers in Psychiatry,
JAMA Psychiatry and Lancet Psychiatry. Two for two from outside it, in one
run.

**Transport, for the record:** JAMA Psychiatry and Lancet Psychiatry are
now Cloudflare-blocked even through the `r.jina.ai` proxy, but **PubMed's
E-utilities API reaches both cleanly with real per-article dates.** That
belongs in `sources/benchmarks.yaml`.

**Two aggregator traps were caught and excluded** rather than published:
the "Anna vs. Judith" chatbot trial and the AiTAPI attitude-scale
validation both resurfaced in today's Internet Interventions feed with
fresh timestamps and are old news (June and 09-01), confirmed via Crossref
before anything was written.
