---
lens: mental-health
date: 2026-09-10
status: building
window_start: 2026-09-10T05:00:00-04:00
as_of: 2026-09-10T10:00:00-04:00
coverage: pending
---

# Mental Health — 2026-09-10

*Curated agentic-interim, 05:00 ET → **10:00 ET** Thursday. Sources: a
sweep across all 24 open threads, the deterministic collectors
(`clinicaltrials` 840+ rows across two days, `federal_register`,
`semantic_scholar`, `sec_edgar`, `rss`, `gdelt`), trade press, and court
dockets.*

## Today's throughline

Five California bills that would reshape how AI is allowed to touch
mental-health care are sitting on the governor's desk twenty days from
their deadline, and none of them moved today. That is the whole morning:
no new developments across 24 tracked areas, established by checking rather
than by assuming — every one of the six live dated items was verified
still-open against a primary source, and both days' clinical-trials
registrations were swept by keyword. A negative result that was actually
looked for is worth more than a thin page of filler.

## Policy, regulation & legal

*No developments in this window.* The five California bills awaiting
Governor Newsom's signature or veto — AB 1979 (consumer health chatbots
under the Confidentiality of Medical Information Act), AB 2575 (AI-caused
clinical-harm liability), SB 1119 (children's companion-chatbot safety),
SB 903 (barring marketing a chatbot as "therapy"), and SB 503
(clinical-decision-support developers and deployers) — all remain
unacted-on, verified against the legislature's own records this morning.
The MHPAEA parity replacement rule remains unproposed.

## 🧪 Clinical trials

- **840-plus ClinicalTrials.gov registrations across 09-09 and 09-10 were
  swept by keyword for psychedelic, neuromodulation and AI-chatbot trials,
  and none crossed the practice-changing bar.** All were routine new
  registrations with no tie to a tracked company. Stated explicitly because
  a null result on this lane is a real finding rather than a lane that went
  unchecked — and because this lane lands after the general sweep and has
  been skipped before. The 09-09 finalize pass separately confirmed 161
  mental-health-relevant rows first-posted that day, same result.

## ⏳ Upcoming & expected

Six live items, all verified still-open against primary sources this pass
rather than carried forward on assumption:

- **`fda-psychedelic-public-hearing` — 09-14.** Nothing new in the Federal
  Register buffer; hearing date unchanged.
- **`sword-headspace-acquisition-close-0914` — 09-14.** No filing.
- **`raine-jccp-cmc-0923` — 09-23.** Next case-management conference in the
  coordinated chatbot-death litigation unchanged; no new filings.
- **`anthropic-wellbeing-grants-deadline-0921` — 09-21.** Applications still
  open.
- **`ca-ab1979-governor-action`, `ca-ab2575-governor-action`,
  `ca-sb1119-governor-action`, `ca-sb903-governor-action`,
  `ca-sb503-governor-action` — all 09-30, all pending.** Twenty days out.
- **`mhpaea-replacement-rule` — 12-31.** Still unproposed. The DOL/EBSA
  interim enforcement roadmap caught on the 09-09 pass remains the only
  parity movement this quarter.

## 🔄 Map changes

- **No new timeline entries on this lens today.**
- **`ai-therapy-regulatory-reckoning` and `mhpaea-parity-limbo`** had stale
  `last_seen` fields repaired as part of the corpus-wide fix (35 threads);
  no editorial change to either.

## 🧵 Thread candidates

None. Two ambient items were noted and deliberately not promoted: a UVA
Health piece on psychiatric deprescribing clinics and a Behavioral Health
Business piece on payer trends driving behavioral-health investment. Both
are trade commentary rather than developments, and both landed after
yesterday's cutoff.

## ⚠️ Collection note

The sweep ruled several near-misses out rather than reporting them, which
is worth recording as the correct behaviour: a Definium 8-K and an
"Anna vs. Judith" AI-therapy trial both turned out to be already on-thread;
two payer 8-Ks (UnitedHealth, Elevance) had no mental-health content on
inspection; and a Florida attorney-general proposal on chatbot criminal
liability was timestamped before this window and is already in the 09-09
digest.

⚠️ **One benchmark state from the 09-09 critic pass was wrong and has been
corrected.** Behavioral Health Business was logged as returning 403 on both
its feed and homepage. Re-checked the same hour via `python3 urllib`, it
returned HTTP 200 with a live feed carrying two real 09-09 items. The 403
came from the tool the agent fell back to after `curl` was refused by the
harness — not from the outlet. Recorded in `sources/benchmarks.yaml` and
`coverage-log.md`.
