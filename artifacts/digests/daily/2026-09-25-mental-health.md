---
lens: mental-health
date: 2026-09-25
status: building
window_start: 2026-09-25T05:00:00-04:00
as_of: 2026-09-25T10:00:00-04:00
coverage: pending
---

# Mental Health — 2026-09-25

*Curated agentic-interim, 05:00 ET → about 10:45am ET Friday (sources:
ClinicalTrials.gov's own API queried by psychiatric condition and 09-25
first-posted date; the collector buffer's 09-25 rss, gdelt, federal_register,
sec_edgar and google_news_rss files as they landed through 10:25am ET
(google_news_rss landed late, ~10:25am ET, and was triaged by title/time
since 05:00 ET Friday); the California Legislature's bill-status pages,
re-checked live; CourtListener's docket for the Education Department school
mental-health grants case, re-checked live; Lawsuit Informer and DuckDuckGo
(via r.jina.ai) for the Raine JCCP conference outcome; ThriveNews's Reuters
syndication and the Alabama Attorney General's complaint for the TikTok
trial (Reuters.com itself 401'd); Ars Technica directly for the WISeR
report; and Yahoo Finance/GlobeNewswire and Manila Times/GlobeNewswire for
the two neuromodulation partnership releases).*

## Today's throughline

Alabama's lawsuit against TikTok and ByteDance over teen mental health becomes the first of the state social-media suits to reach a jury, with trial starting Monday in Montgomery. Ars Technica reported that the Government Accountability Office found in May that CMS skipped required procedure in setting up WISeR, Medicare's AI prior-authorization pilot, and that an HHS nominee wrongly told a 09-16 Senate hearing that its contractors are not paid more for denying care. Two neuromodulation companies announced distribution deals for FDA-cleared devices, neurocare and Wave Neuroscience for PTSD and Firefly Neuroscience and NeuroSigma for pediatric ADHD, and Slingshot AI registered a pilot trial of its Ash chatbot against psychoeducation for depression. The Education Department's status report under the school mental-health grants injunction is due by the end of today, California's four chatbot bills await the governor's signature or veto by 09-30, and no outcome has been reported from Wednesday's Raine v. OpenAI case-management conference.

## Policy, regulation & legal

- **An Alabama jury will hear the state's case against TikTok and ByteDance beginning Monday 09-28 in Montgomery, the first of at least 27 state lawsuits over the platform's alleged effects on teen mental health to reach trial, expected to last two to three weeks.** Alabama alleges TikTok designed its endless video feed and recommendation algorithm to keep children on the platform while steering some toward increasingly intense content involving violence and self-harm, and that it misled parents and consumers about its safeguards, age restrictions and the amount of sexual or violent material available to minors; the allegations have not been proven in court. TikTok says protecting teenagers is a priority and that federal law shields platforms from liability for user-created content; it did not respond to Reuters for comment. Alabama seeks financial penalties and other court-ordered relief, and the trial could surface internal TikTok material that has stayed sealed or redacted in earlier, settled cases.
  ([Reuters](https://www.reuters.com/world/us/first-us-trial-against-tiktok-test-claims-platform-fueled-teen-mental-health-2026-09-25/), [ThriveNews, syndicating Reuters](https://thrivenews.co/tiktok-alabama-trial-teen-mental-health/), [Alabama Attorney General's complaint](https://www.alabamaag.gov/wp-content/uploads/2025/04/2-Complaint.pdf))
  <!-- k: t=social-media-causality-fight e=bytedance axis=policy sev=major -->
- **Ars Technica's 09-25 report adds the Government Accountability Office's May finding that CMS officials skipped required procedure setting up WISeR, calling the program's legality into question, and a 09-16 Senate hearing exchange in which HHS deputy-secretary nominee Chris Klomp wrongly told Sen. Patty Murray that WISeR contractors don't get paid more for denying care — Murray corrected him on the record using a CMS Office of the Actuary memo.** The underlying documents — vendor Virtix's 53% denial rate on 6,096 requests reviewed by late March and Innovaccer's temporary blanket auto-approvals to avoid a launch delay — were first reported 09-15. New here: Virtix's corrective action plan for missing the required 72-hour decision window (some requests took over 80 days) closed 08-14, with turnaround now averaging 1.18 days, and Rep. Suzan DelBene's committee push to force release of more WISeR documents was voted down by Republicans last week. WISeR continues, with plans to expand through 2031.
  ([Ars Technica](https://arstechnica.com/health/2026/09/trump-admin-using-ai-to-deny-medical-care-for-seniors-in-disastrous-experiment/))
  <!-- k: t=payer-ai-claim-denial axis=policy -->

## Capital & corporate

- **neurocare group AG and Wave Neuroscience announced a partnership on 09-25 to make Wave's FDA-cleared MeRT EEG-guided brain-stimulation therapy for PTSD available on neurocare's Apollo TMS platform.** MeRT (developed by Wave Neuroscience) uses EEG-derived brain-activity measurements to individualize TMS treatment parameters and won FDA clearance for adult PTSD in June 2026; neurocare's CEO frames the deal as expanding its "open ecosystem" of compatible neuromodulation technologies through its growing US installed base of Apollo TMS devices. A distribution and commercialization partnership, not new clinical evidence — no new trial or outcome data accompanies the announcement.
  ([GlobeNewswire via Manila Times](https://www.manilatimes.net/2026/09/25/tmt-newswire/globenewswire/neurocare-and-wave-neuroscience-partner-to-expand-patient-access-to-fda-cleared-mert-therapy-for-ptsd-on-the-apollo-tms-therapy-system/2433023))
  <!-- k: t=neuromodulation-evidence axis=capital -->
- **Firefly Neuroscience and NeuroSigma announced a second neuromodulation distribution partnership the same day, 09-25: Firefly will introduce NeuroSigma's Monarch eTNS System, the first FDA-cleared non-drug treatment for pediatric ADHD, to the psychiatry, neurology and behavioral-health practices in its nationwide Evoke EEG/ERP clinician network.** Monarch is an at-home external trigeminal nerve stimulation device; Firefly's Evoke platform is its own FDA 510(k)-cleared AI-powered EEG/ERP system, so the deal pairs Firefly's brain-function measurement tool with NeuroSigma's treatment device. Firefly cites a 2024 Journal of Clinical Child & Adolescent Psychology estimate that about 7.1 million US children have an ADHD diagnosis and nearly a third of the 6.5 million with current ADHD get no ADHD-specific treatment. A second same-day distribution deal for an FDA-cleared brain-stimulation device, after neurocare/Wave Neuroscience above — a real-world-deployment pattern worth watching, not necessarily a coordinated one.
  ([Yahoo Finance, GlobeNewswire release](https://finance.yahoo.com/healthcare/articles/firefly-nasdaq-aiff-neurosigma-partner-114500758.html))
  <!-- k: t=neuromodulation-evidence axis=capital -->

## 🧪 Clinical trials

ClinicalTrials.gov's API, queried live for studies first posted 2026-09-25
(231 total that day across all conditions; not yet in the collector's own
09-25 clinicaltrials.jsonl file, which landed at 14:05 UTC but was not
re-queried against this day's postings), returned the following on-lens
records by condition-specific query.

- **Slingshot AI, maker of the "Ash" AI mental-health chatbot, registered a pilot randomized controlled trial testing Ash against a psychoeducation control for depression, with the primary outcome a change in PHQ-9 score at six weeks framed as a non-inferiority comparison (first posted 09-25, status "active, not recruiting").** About 500 adult US residents already using Ash with at least moderate depressive symptoms (PHQ-9 ≥10) are split between immediate free access to Ash for four weeks and four weeks of standard psychoeducation before getting access; follow-up runs to 36 weeks. This is Slingshot generating its own outcome data for a product this map already tracks as part of the AI-therapy evidence gap the industry is under pressure to close — registration only, no results, and the company is both sponsor and app-maker.
  ([ClinicalTrials.gov NCT07841483](https://clinicaltrials.gov/study/NCT07841483))
  <!-- k: t=ai-therapy-regulatory-reckoning,mh-evidence-watch e=slingshot-ai axis=clinical-trials -->
- **The University of Kentucky registered a trial of brain stimulation for patients with co-occurring major depressive disorder and opioid use disorder (first posted 09-25).** No phase listed, no participant count yet available in the record read; a dual-diagnosis population this lens's neuromodulation thread has not covered before. Registration only, no data.
  ([ClinicalTrials.gov NCT07842601](https://clinicaltrials.gov/study/NCT07842601))
  <!-- k: t=neuromodulation-evidence axis=clinical-trials -->
- Also first posted 09-25 and near the lens but not landmark:
  [NCT07840417](https://clinicaltrials.gov/study/NCT07840417), a University of Alberta trial of "deep brain reorienting," a novel psychotherapy technique, for PTSD;
  [NCT07842432](https://clinicaltrials.gov/study/NCT07842432), a Johns Hopkins Bloomberg School of Public Health trial of a universal trauma-informed intervention for student mental health (anxiety, PTSD symptoms, depression, behavioral problems);
  [NCT07843056](https://clinicaltrials.gov/study/NCT07843056), a Phase 2 comparing an unnamed compound (WAS123) with daily aripiprazole for maintenance treatment of schizophrenia, sponsor EMS;
  [NCT07840586](https://clinicaltrials.gov/study/NCT07840586), a National University Hospital Singapore trial of a culturally adapted, low-frequency parent-mediated early intervention for autism spectrum disorder; and
  [NCT07840404](https://clinicaltrials.gov/study/NCT07840404), a feasibility trial of a compassion-focused app for parents of children with chronic conditions, targeting caregiver distress, burnout and parental burnout.

## ⏳ Upcoming & expected

No flips today; the same items tracked in the 09-24 digest remain pending,
re-checked live this morning:

- **`raine-jccp-cmc-0923`** — still unreported (see throughline).
- **California governor's 09-30 deadline** — AB 1979, SB 903, AB 2575 and
  SB 503 all still "Enrolled and presented to the Governor," unchanged.
- **`wa-school-mh-grants-status-report-0925`** (due today) — not yet filed
  as of the ~10:05am ET docket check; entry 106 (the 09-22 injunction order)
  is still the newest entry on the docket.
- **`ac-v-altman-fnc-hearing-1105`** — no docket movement since 09-24.
- **Portland psychedelics ordinance** — second reading Wednesday 09-30,
  unchanged.
- 5 pending items carried from the 09-24 digest with no near-term action
  expected today (Xenon's X-Nova2 topline Q1 2027, Acadia's CTAD detail
  11-16, the DEA tryptamine comment period closing 10-23, the
  sword-headspace acquisition close 10-01, Pennsylvania's chatbot memo
  awaiting introduction).

## 🔄 Map changes

- **Coverage critic (2026-09-25 midday pass).** Reframed the WISeR bullet
  above to lead with the GAO's May procedural finding and the 09-16 Senate
  hearing exchange — the genuinely new facts in Ars Technica's report —
  rather than restating denial-rate documents already on
  `payer-ai-claim-denial` since 09-17; added Reuters as the first citation
  on the Alabama v. TikTok bullet, ahead of the ThriveNews syndication.
- None to `attention/` from this pass. All six items today are staged for
merge (below) as extensions of existing threads, not new ones: the Alabama
v. TikTok trial and the WISeR Medicare AI reporting (`social-media-causality-fight`
and `payer-ai-claim-denial` respectively), the Slingshot AI trial
registration (`ai-therapy-regulatory-reckoning`/`mh-evidence-watch`), and two
neuromodulation-distribution partnerships, neurocare/Wave Neuroscience and
Firefly/NeuroSigma (both `neuromodulation-evidence`). The Alabama trial is
tagged `sev=major` — the first of 27+ state suits over social-media
teen-mental-health harm to reach a jury is a first-of-kind development for
the litigation wave this thread tracks, and no other `sev=major` item sits
in this digest. Two apparent finds were ruled out as old stories resurfacing
under today's date (see throughline) and are not staged.

## 🧵 Thread candidates

None new today. The two candidates raised in the 09-24 digest (Medicaid
"medically frail" litigation; the federal school mental-health grant
termination fight) still stand, unanswered, and are not repeated here per
the brief's "unanswered candidates may reappear once" rule.

---
Alabama's TikTok trial, the first of 27-plus state teen-mental-health suits
against the platform to reach a jury, starts Monday in Montgomery. Ars
Technica detailed WISeR's chaotic Medicare AI prior-authorization rollout,
two companies announced same-day FDA-cleared neuromodulation distribution
deals, and Slingshot AI registered its own pilot trial of "Ash" against
psychoeducation for depression. Three deadlines are all still open past
their due dates or approaching them unresolved: the Education Department's
compliance report (due today, not filed), California's four bills (due
09-30, no action) and the Raine conference outcome (due 09-23, still
unreported).
