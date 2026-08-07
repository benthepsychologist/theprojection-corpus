# Q2 — Does the science of matching ever reach the clinic? (research memo, 2026-08-07)

Scope: measurement-based care's (MBC) know-do gap and precision psychiatry's validation gap, deepened from
`ebp-crawl-therapy-science.md` §2 (MBC) and §4 (precision psychiatry) with a focus on implementation-science
outcomes at scale, algorithm deployment status, pharmacogenomic payer decisions, the commercial MBC vendor
layer, and biomarker reality-checks — what changed 2021→2026, verified against primary/secondary sources
where the crawl file summarized.

---

## TL;DR

- **MBC's evidence is settled; its implementation gap is not closing at the point of care.** The VA mandated
  MBC in three programs (substance use disorder, mental-health residential rehab, PTSD) and now reports
  100% facility participation and 14.8M+ patient-reported outcome measures administered — but that number
  measures *compliance with collecting data*, not clinician use of it: a provider survey found only 58% of
  VA clinicians use/share results for at least half their caseload, and 2025–2026 studies of virtual/rural VA
  mental health still describe adoption below 50%. The mandate solved data collection; it did not solve the
  behavior-change problem implementation science has been naming for over a decade.
- **A commercial MBC vendor layer has emerged since 2024–2025 to attack that same friction** (Greenspace
  Health, Blueprint, Mirah, Owl, Quenza, OQ-Analyst), with a major 2025 EHR-integration deal (Qualifacts ×
  Greenspace, embedding MBC directly into the Credible/CareLogic behavioral-health EHRs used by many US
  community mental-health centers). But the only outcome numbers found are single-organization vendor case
  studies (one Florida provider reporting a 68% "recovery rate"), not independent peer-reviewed, population-
  scale evidence — the market is scaling *measurement delivery*, not yet proving it closes the know-do gap.
- **One treatment-selection algorithm cleared a real bar in 2025.** AID-ME — a deep-learning depression-
  treatment-selection clinical decision support system — was tested in a genuine multi-site cluster RCT (9
  sites, 47 clinicians, n=61 analyzed) and hit a statistically significant remission advantage (28.6% active
  vs. 0% active-control, *P*=.012). That's the first treatment-matching tool in this space to reach multi-site
  trial status rather than a single-site pilot — but the sample is small, the authors themselves flag limited
  generalizability (no primary-care clinicians), and call for replication before real-world deployment. No
  algorithm in this space (AID-ME, PReDicT, Personalized Advantage Index) has reached routine, unmonitored
  clinical use anywhere.
- **Pharmacogenomics hasn't moved since 2023, and a major US payer just re-confirmed it won't cover it.**
  CPIC's actionable-gene list (CYP2D6/CYP2C19/CYP2B6) is unchanged. Carelon — a clinical benefit manager
  used by multiple large US payers — kept antidepressant/psychiatric pharmacogenomic panels explicitly
  "Not Medically Necessary" through its November 2025 → January 2026 policy cycle, citing the same GUIDED
  trial and the VA's own PRIME pragmatic trial (<2 percentage-point remission gain) as before. No substantive
  change from 2024. Payer coverage is not following commercial marketing of these tests.
- **Biomarkers remain confirmed-preliminary in two fresh 2025–2026 reviews**, both explicitly stating no
  FDA-validated biomarker exists for any primary psychiatric disorder, external replication is low, and the
  realistic near-term role is prognostic/stratification support layered onto clinical judgment — not a
  standalone diagnostic — with no deployment timeline offered by either.

---

## What changed 2021→2026

**MBC: from "evidence exists, uptake is low" to "uptake is now mandated in the largest single US health
system, and a commercial layer is being built to automate around clinician non-adherence."** In 2021 the
story was purely implementation-science: strong trial evidence, weak real-world uptake, no clear lever.
By 2026 the VA has proven a *mandate* can force near-universal measure *administration* (100% of facilities,
14.8M+ PROMs) — a genuinely new data point implementation science alone never produced. What hasn't changed
is the harder half of the problem: getting a clinician to look at the score and change what they do in
session. VA's own implementation-facilitation trials (dating to the 2018–2019 period, still the field's best
evidence) found that *facilitation* — active coaching/support for clinicians — raised adoption and reach
significantly over passive rollout, and crucially that facilitation sites *held their gains through COVID*
while comparison sites' emphasis on MBC collapsed. That finding is the single clearest "yes, something works"
result in this whole strand — but it requires sustained investment in people, not just a policy mandate or a
software purchase, and 2025–2026 papers on VA virtual/rural mental health still describe sub-50% adoption in
exactly the settings where facilitation is hardest to deliver. Separately, since roughly 2024–2025 a real
commercial market (Greenspace, Blueprint, Mirah, Owl, Quenza, OQ-Analyst) has formed around embedding MBC
directly into EHR workflows — a genuinely new development, betting that removing manual/workflow friction
(the "measurement that depends on remembering does not happen" problem) is itself enough to move outcomes.
That bet is commercially live but not yet independently evidenced at population scale.

**Precision psychiatry: from "biomarker/algorithm pilots" to "one algorithm reaching a real multi-site RCT,
pharmacogenomics hitting a payer wall, and biomarkers still not validated."** In 2021 the field's best
evidence for treatment-matching was retrospective (Personalized Advantage Index) or single-cohort predictive
(iSPOT-D) — associational, not prospectively tested in a live clinical-decision context. AID-ME (published
August 2025, *Journal of Clinical Psychiatry*) is the first tool in this family to be prospectively tested as
a decision-support intervention across 9 independent sites and get a statistically significant outcome
advantage — a real, if narrow, step past the pilot stage. Pharmacogenomics moved the opposite direction:
where 2021-era coverage decisions were unsettled, by 2025–2026 a major payer's clinical-benefit-management
policy is unambiguous and unchanged year-over-year — the evidence bar (symptom-outcome improvement, not just
drug-gene-mismatch avoidance) has been applied and antidepressant PGx testing has failed it in payer eyes,
consistently, across two policy cycles. Biomarkers haven't moved qualitatively at all — 2025–2026 reviews use
nearly identical language to 2022-era reviews ("preliminary," "small heterogeneous samples," "low external
replication") — the newest twist is a more explicit accounting of what's actually FDA-validated in psychiatry
today: nothing, for any primary psychiatric disorder.

---

## Current state of the dispute

The two threads converge on the same underlying disagreement: **is this an evidence problem or a delivery
problem?** For MBC, the evidence question is closed (routine outcome monitoring works) and the fight has
fully relocated to delivery — does a top-down mandate (VA), a vendor-automated workflow (Greenspace/Qualifats),
or sustained implementation facilitation (VA's own strongest trial data) actually change what a clinician does
in the room, and none of the three approaches yet has independent, population-scale, peer-reviewed proof that
it does. For precision psychiatry, the dispute is still substantially an evidence problem: AID-ME is real
progress but is explicitly underpowered and site-limited by its own authors; pharmacogenomics has essentially
lost the argument on the endpoint payers care about (symptom outcomes) even while remaining defensible on a
narrower endpoint (avoiding drug-gene mismatches) that payers have declined to reward; and biomarkers have not
produced a single deployable instrument. The honest 2026 read, matching and sharpening the crawl file's
framing: **MBC has crossed from "we don't know if it works" to "we know it works and still can't make
clinicians do it reliably, even with a federal mandate behind it"; precision psychiatry has not yet crossed
from "promising pilot data" to "clinically actionable" for any of its three sub-strands (biomarkers,
pharmacogenomics, algorithmic matching), though algorithmic matching (AID-ME) is the strand showing the most
forward motion in the 2024–2026 window.**

---

## Key sources

| Title | Venue | Year | URL | Finding |
|---|---|---|---|---|
| **VA MBC national implementation-facilitation trial** (mixed-methods RCT) 🔬 | *Psychiatric Services* / PMC | 2019 (still anchor evidence through 2025–2026) | https://psychiatryonline.org/doi/10.1176/appi.ps.20220140 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6171308/ | Facilitation sites significantly outperformed comparison sites on MBC adoption/reach and *held gains through COVID* while comparison sites' MBC emphasis collapsed — the field's clearest "this intervention works" result for closing the know-do gap. |
| VA MBC national mandate/scale data (100% facility participation, 14.8M+ PROMs administered) | Secondary reporting (FierceHealthcare 2024 outlook; cross-confirmed via independent search) | 2024 | https://www.fiercehealthcare.com/providers/2024-outlook-measurement-based-care-behavioral-health | VA mandates MBC in SUD, residential rehab, and PTSD programs; near-universal measure *administration* achieved — but provider-level *use/sharing* of results still lags (~58% of providers use/share for ≥half their caseload, per synthesized VA provider-survey reporting). |
| Advancing MBC in military/Veteran mental health: an implementation-science perspective | *J. Military, Veteran and Family Health* | 2025 | https://utppublishing.com/doi/10.3138/jmvfh-2025-1107 | Frames VA MBC as an implementation-science case study; paywalled (403), cited via search abstract only — flagged for lower confidence. |
| Implementing MBC in virtual mental health services for rural veterans: pre-implementation evaluation | *BMC Health Services Research* | 2026 | https://link.springer.com/article/10.1186/s12913-026-14490-6 | Adoption in VA virtual/rural mental health settings remains <50% as of 2025–2026, despite the national mandate — paywalled (403), cited via search abstract only. |
| **AID-ME: Artificial Intelligence in Depression–Medication Enhancement**, cluster RCT | *Journal of Clinical Psychiatry* | Aug 2025 | https://pubmed.ncbi.nlm.nih.gov/40875536/ | First depression treatment-selection CDSS tested in a multi-site (9 sites, 47 clinicians) prospective RCT; remission 28.6% (active, 12/42) vs. 0% (active-control), *P*=.012; speed-of-improvement advantage *P*=.03; authors flag sample-size/generalizability limits and call for replication. |
| Qualifacts × Greenspace Health MBC–EHR integration announcement | Vendor resource page (Qualifacts) | May 2025 | https://www.qualifacts.com/resources/driving-quality-outcomes-with-greenspace-healths-measurement-based-care-platform/ | Commercial MBC platform now embeds directly into Credible/CareLogic behavioral-health EHRs; single-org case study (David Lawrence Centers, FL) reports 68% average PHQ-9/GAD-7 "recovery rate" — vendor-reported, not independently peer-reviewed or controlled. |
| Scalable MBC systems for expanding health-care organizations | MedCity News (sponsored/trade) | Feb 2026 | https://medcitynews.com/2026/02/designing-scalable-measurement-based-care-systems-for-expanding-health-care-organizations/ | Confirms no named health systems, no vendor-comparative outcome data, and no evidence commercial MBC platforms have closed the implementation gap academic implementation science left open — automation reduces administrative burden, not proven to change clinical outcomes at scale yet. |
| MBC outcome-software market comparison (Greenspace, Blueprint, Mirah, Owl, Quenza, OQ-Analyst) | Psychology.com | 2026 | https://psychology.com/therapy-software/therapy-outcome-measurement-software | Market has segmented (specialist MBC vs. AI-documentation-first vs. enterprise/population-analytics); confirms "most therapists still avoid routine measurement despite evidence" — software targets friction reduction, not novel clinical insight; no cross-platform efficacy data exists. |
| CMS Innovation in Behavioral Health (IBH) Model | CMS Innovation Center | Launched Jan 1, 2025 | https://www.cms.gov/priorities/innovation/innovation-models/innovation-behavioral-health-ibh-model | Value-based payment model tying behavioral-health practices to per-person-per-month + performance payments; 3 states currently (Michigan, New York, South Carolina; up to 8 planned) — but performance-based payments don't begin until the 2028–2032 implementation period, so it's not yet a live test of whether payment-linked outcome measurement moves results. |
| Carelon Pharmacogenetic Testing Coverage Policy (payer clinical guideline) | Carelon Medical Benefits Management | Updated Nov 2025 → Jan 2026 | https://guidelines.carelonmedicalbenefitsmanagement.com/pharmacogenetic-testing-2025-11-15-updated-2026-01-01/ | Antidepressant/psychiatric PGx panels explicitly "Not Medically Necessary," citing GUIDED trial (no significant response/remission difference) and VA's PRIME pragmatic trial (<2-point remission gain); unchanged from 2024 — payer coverage has not moved despite ongoing commercial marketing of these tests. |
| CPIC Guideline, CYP2D6/CYP2C19/CYP2B6/SLC6A4/HTR2A and SSRI/SNRI antidepressants | *Clin Pharmacology & Therapeutics* | 2023 (still current 2026) | https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt.2903 | No CPIC update to antidepressant-relevant gene actionability since 2023; SLC6A4/HTR2A remain explicitly non-actionable. |
| **"Editorial: Biomarkers of response to interventions in psychiatry"** 🔬 | *Frontiers*, via PMC | 2025–2026 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12872906/ | Synthesizes 6 recent studies; concludes the field remains preliminary/research-focused, biomarkers are "inherently multidimensional," and clinical utility depends on feasibility/interpretability/integration not yet achieved — no adoption numbers given. |
| **"Prognostic Biomarkers and Precision Psychiatry: A Review of the Available Evidence"** 🔬 (semi-systematic narrative review) | *Biomedicines* (MDPI) | 2026 | https://www.mdpi.com/2227-9059/14/3/558 | 30 studies, n=7,363, across depression/schizophrenia/bipolar/anxiety; evidence "comes mainly from observational studies and small and/or heterogeneous samples"; low external replication; recommends multimodal models + standardized protocols before deployment; frames realistic role as prognostic/stratification, not diagnostic. |

🔬 = meta-analysis, umbrella/systematic review, or reviews-of-reviews.

---

## Feed implications

**Candidate terms:**
- **"MBC know-do gap"** — the field's own name for exactly this dispute; worth tracking as a standing term since 2026 is the first year with a genuine at-scale natural experiment (VA's mandate) to test whether policy alone closes it.
- **"Treatment-matching algorithm"** — AID-ME is the first concrete instance; useful as a term to catch the next entrant (any tool claiming multi-site validation, not just single-cohort prediction).
- **"Precision psychiatry payer wall"** — captures the specific, newly-hardened dynamic where payers (Carelon) are applying a symptom-outcome evidence bar and pharmacogenomic testing is losing that argument on the record, unchanged across two policy cycles.

**Candidate threads:**
- **VA's MBC mandate as the field's largest live implementation experiment** — track whether provider *use* (currently ~58%) and virtual/rural adoption (currently <50%) close the gap with *administration* (100%) over the next 1–2 years; this is the best real-world test case available anywhere for "does a mandate alone solve implementation science's oldest problem."
  - *Why*: no other health system anywhere has forced this experiment at this scale; the outcome settles (or doesn't) a decade-old debate with real data instead of another pilot.
- **The commercial MBC vendor layer (Greenspace/Qualifacts, Blueprint, Mirah) and whether it produces independent outcome evidence** — watch for the first peer-reviewed, multi-site, controlled evaluation of an EHR-embedded MBC platform (none exists yet; everything found is vendor-reported).
  - *Why*: if this market matures without ever producing controlled evidence, it's a live case of commercial infrastructure substituting for implementation science rather than validating it — worth calling out either way it goes.
- **AID-ME replication** — the authors explicitly call for a larger, more diverse (incl. primary-care) replication; watch for whether one is funded/registered.
  - *Why*: this is the single nearest-term "did the science of matching reach the clinic" test case in the whole space; a positive replication would be the first genuinely deployment-ready treatment-matching tool in psychiatry.
- **CMS IBH Model's 2028 performance-payment phase-in** — currently pre-implementation only; nothing about outcome-linked payment is actually live yet despite the January 2025 "launch."
  - *Why*: easy to over-report as "value-based behavioral-health payment has arrived" when the model's actual outcome-payment linkage doesn't start for two more years — worth flagging the lag explicitly if this gets covered.

**Candidate expectations (for the ledger):**
- *By ~2027–2028, does VA provider-level MBC "use/sharing" data (currently ~58%) meaningfully close the gap with administration (100%)?* — testable, VA publishes this data periodically.
- *Does any EHR-embedded MBC vendor (Greenspace, Blueprint, Mirah) produce an independent, peer-reviewed, controlled outcome evaluation by ~2027?* — currently zero exist; a clean falsifiable marker for whether the commercial layer is substance or marketing.
- *Does AID-ME (or a comparable treatment-matching CDSS) get funded for a larger replication trial, and if so does the effect hold at a larger n?* — the field's nearest concrete test of whether algorithmic matching escapes the "promising pilot" trap that's held for over a decade.
