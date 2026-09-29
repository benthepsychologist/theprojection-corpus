---
lens: mental-health
date: 2026-09-29
status: building
window_start: 2026-09-29T05:00:00-04:00
as_of: 2026-09-29T15:45:00-04:00
coverage: pending
---

# Mental Health — 2026-09-29

*Curated agentic-interim, 05:00 ET → about 3:45pm ET (agentic-interim). Sources: the
collector buffer's 09-29 `rss` (518 rows), `gdelt` (38), `federal_register` (61),
`clinicaltrials` (402), `semantic_scholar` (95) and `github` files, all of which
had landed by the afternoon pass (the 19:00Z collect had added only a handful of
`rss` and `github` rows, and the afternoon `google_news_rss` append had not yet landed, so the morning's 11,265 Google rows were the only ones grepped);
ClinicalTrials.gov's own API for studies first posted 09-29 (re-queried in the
afternoon, no new on-lens registrations); CalMatters and the governor's
newsroom and press feed for the California items; the California
Legislature's bill-status pages, re-checked live at mid-afternoon for AB 1979,
SB 903, AB 2575 and SB 503; Portland's ordinance page; the VA press room; and
Google News RSS and web-search sweeps across this lens's open threads and
watchlist names; then a late-buffer pass over the afternoon's new `google_news_rss` rows (3,194, landed 19:25Z), `rss` (34), `gdelt` (81), `semantic_scholar` (119) and `github` rows, read by title and searched for the lens's watchlist organisations and people, with each candidate checked against publisher or primary text.*

## Today's throughline

California's governor has still not acted on four AI health-care bills due Wednesday, while the VA awarded $111.9 million in veteran suicide-prevention grants and Portland's psychedelics vote nears. Governor Gavin Newsom signed two bills widening CARE Court referrals on Sunday 09-27, and two larger bills that would have tied the program to involuntary conservatorship died in the Assembly Appropriations Committee in August. AB 1979, SB 903, AB 2575 and SB 503 still show "Enrolled and presented to the Governor" on the Legislature's own pages at mid-afternoon Tuesday, and neither of the governor's two 09-29 signing releases (Asian American and Pacific Islander-serving institutions; immigration bills) names any of them. The VA announced $111.9 million in Fox suicide-prevention grants to 191 community organizations on Tuesday, and Portland's second reading of its psychedelics ordinance is still set for Wednesday 09-30. Australia's government also conceded in its High Court defence of the under-16 social media ban that there is no scientific consensus on the mental-health link, and Apple and the American Academy of Pediatrics released a parental-controls guide.

A thin Tuesday otherwise. No new court, regulator or payer action on this lens's other open threads turned up between 05:00 ET and about 3:30pm ET; Florida's injunction motion against OpenAI (filed Monday) drew more press coverage Tuesday but no reported OpenAI filing, hearing date or ruling.

## Policy, regulation & legal

- **Governor Gavin Newsom signed two bills on Sunday 09-27 that make it easier for first responders to refer people to CARE Court, California's mental-health court, and for a participant's loved ones to give the care team information, while two larger bills linking CARE Court to conservatorship died in August.** CalMatters, reporting on 09-29, says the signed bills are by Sens. Catherine Blakespear and Steven Choi, that Blakespear called them "incremental improvement," and that SB 1242 (Choi) was watered down before it reached his desk; SB 1016 and SB 28, which would have created a path from CARE Court to involuntary conservatorship, died in Assembly Appropriations, and Blakespear said she will try again next year. The governor's own 09-27 legislative update lists SB 1242 and SB 989 among the signed bills.
  ([Governor of California, 09-27 legislative update](https://www.gov.ca.gov/2026/09/27/governor-newsom-issues-legislative-update-9-27-2026/), [CalMatters](https://calmatters.org/housing/homelessness/2026/09/care-court-bills-vetoes-2026/))
  <!-- k: axis=policy -->
- **The Department of Veterans Affairs announced on 09-29 that it has awarded $111.9 million in Staff Sergeant Parker Gordon Fox Suicide Prevention Grants to 191 community organizations, funds that become available at the start of fiscal year 2027.** VA Secretary Doug Collins said community groups are critical to reaching veterans who may not connect with VA care; VA says 61% of veterans who died by suicide in 2023 were not receiving VA health care in their last year, and that the Veterans Crisis Line answered more than 1.3 million calls, chats and texts in fiscal 2026 through 09-20, up 7.1% on the year before.
  ([Department of Veterans Affairs](https://news.va.gov/press-room/va-awards-112-million-in-suicide-prevention-grants/))
  <!-- k: t=mh-clinical-infra-funding axis=policy -->

- **Australia's federal government has conceded, in its High Court defence of the under-16 social media ban, that there was no scientific consensus on a link between social media and teenage mental-health harm when the ban was enacted, arguing that "credible risks" justify a precautionary law anyway (defence filed 09-25, reported 09-29).** The Guardian reports the filing answers a challenge by Reddit, one of two cases against the ban expected to be heard jointly before the end of 2026; Reddit told the court there is "no scientific consensus about whether there is a causal link." The government's submission says "uncertainty about causation should not delay action," points to nearly 5 million accounts removed in December, and argues its proposed digital duty-of-care law, which would let users opt out of algorithms, would ultimately have the same effect as the ban.
  ([The Guardian](https://www.theguardian.com/australia-news/2026/sep/30/social-media-ban-australia-high-court-mental-health-risks-teens), [The News International](https://www.thenews.com.pk/latest/1418102-australia-admits-no-science-consensus-on-teen-social-media-ban))
  <!-- k: t=social-media-causality-fight axis=policy -->
- **Apple and the American Academy of Pediatrics released "Building Healthy Digital Habits: A Guide for Families" on 09-29, a six-step guide to setting up children's iPhone, iPad and Mac parental controls alongside AAP screen-time guidance by age group.** The steps run from a family conversation and a Child Account through Ask to Buy and Ask to Browse, device-use schedules and communication limits; Apple says Communication Safety is on by default for all users under 18. AppleInsider notes Apple had said at its June developer conference it would expand parental controls in partnership with the AAP; the guide is a how-to, and neither Apple nor the AAP reports any outcome data.
  ([Apple Support](https://support.apple.com/guide/aap-apple/screen-time-guidance-american-academy-dwpwek4yury5/web), [AppleInsider](https://appleinsider.com/articles/26/09/29/apple-american-academy-of-pediatrics-team-up-for-new-screen-time-guide))
  <!-- k: t=apple-health-arm,social-media-causality-fight axis=policy -->

## 🧪 Clinical trials

ClinicalTrials.gov's own API, queried for studies first posted 2026-09-29 by psychiatric condition (the collector's 09-29 clinicaltrials file had not landed), returned the following on-lens records.

- **The "Precision Depression Adalimumab Trial," a 60-patient, quadruple-blind, placebo-controlled Phase 2 in the United States, will test the anti-inflammatory drug adalimumab (as a biosimilar injection) against individual somatic, affective and motivational depressive symptoms (first posted 09-29; start planned 2026-09).** The sponsor is listed as Daniel Moriarity.
  ([ClinicalTrials.gov NCT07845604](https://clinicaltrials.gov/study/NCT07845604))
  <!-- k: axis=clinical-trials -->
- **Florida International University registered an 80-patient Phase 2 trial of a brief, scalable module to reduce suicidal ideation among youth, with self-reported burdensomeness and the Suicide Risk and Ideation Scale for Kids as mid-treatment outcomes (first posted 09-29; start planned 2027-01).** Both arms build on safety planning, and masking is single-blind.
  ([ClinicalTrials.gov NCT07847008](https://clinicaltrials.gov/study/NCT07847008))
  <!-- k: axis=clinical-trials -->
- **Al-Zaytoonah University of Jordan registered, retrospectively, a completed 72-patient, non-randomized, single-blind study of a nurse-facilitated AI chatbot for psychological well-being and mental-health stigma among psychiatric patients in Amman, against usual care, with psychological well-being at two weeks, four weeks and three months as the primary outcome (first posted 09-29; the record lists a 2023-01-11 start and 2024-05-12 completion).** The chatbot, supervised by trained psychiatric nurses, provides mental-health education, emotional support, coping strategies and self-management guidance. No results are posted.
  ([ClinicalTrials.gov NCT07848022](https://clinicaltrials.gov/study/NCT07848022))
  <!-- k: t=ai-therapy-evidence axis=clinical-trials -->
- **Filament Health, the psilocybin developer owned by Ontario-based Rhelion Life Sciences, said on 09-29 that it has shipped its botanical psilocybin candidate PEX010 to the University of Calgary for PsiPTSD, a Phase 2 trial of psilocybin-assisted therapy for chronic PTSD in adult survivors of intimate partner violence (NCT06885996).** The university is the trial's sponsor, led by Dr. Chantel Debert, and Filament says it is only the drug supplier; it is Debert's second PEX010 trial, after a Phase 2b in persisting post-concussion symptoms. The release gives no start date or enrolment figure.
  ([Rhelion Life Sciences via Newsfile](https://www.newsfilecorp.com/release/316514/Rhelion-Life-Sciences-Wholly-Owned-Subsidiary-Filament-Health-Ships-PEX010-to-the-University-of-Calgary-for-Phase-2-Trial-of-PsilocybinAssisted-Therapy-for-PTSD-in-Survivors-of-Intimate-Partner-Violence))
  <!-- k: axis=clinical-trials -->

## 📚 Research & evidence

- **A JAMA Pediatrics umbrella review of 23 meta-analyses covering more than 2.8 million children and adolescents in 64 countries found more screen time associated with lower academic achievement (r = -0.15) and more internalizing symptoms such as depression and anxiety (r = 0.10; 0.09 for social media specifically), but nearly all the evidence is correlational (published online 09-28; Medscape covered it 09-29).** Led by Elizabeth Al-Jbouri of the University of Calgary, the review found no clear association with mathematics, science or reading, and heterogeneity was high or very high for the larger emotional-problem (r = 0.30) and peer-problem (r = 0.28) estimates; the authors call screen use "one potentially modifiable factor" and say the data cannot show causation. The journal page could not be opened here (bot wall), so the figures are as Medscape reports them.
  ([Medscape](https://www.medscape.com/viewarticle/screen-time-linked-poorer-academic-performance-more-2026a10010co), [JAMA Pediatrics](https://jamanetwork.com/journals/jamapediatrics/fullarticle/2854067))
  <!-- k: t=social-media-causality-fight axis=research -->

## ⏳ Upcoming & expected

No flips this afternoon; the same two items remain pending, both due 09-30:

- **California governor's 09-30 deadline** — AB 1979, SB 903, AB 2575 and SB 503 still show "Enrolled and presented to the Governor" and "House Location: Governor" on `leginfo.legislature.ca.gov` this morning, with no chaptered or vetoed date, and none appears in the governor's 09-27 legislative update, his 09-28 press releases (non-UPF label and other health bills; veterans and servicemembers; "commonsense" legislation) or his two 09-29 releases (Asian American and Pacific Islander-serving institutions; immigration bills) that were checked. The Legislature's pages were re-read at mid-afternoon Tuesday and were unchanged. Only SB 903 (Padilla) is squarely mental-health-specific: per the Legislative Counsel's Digest it would limit AI in psychotherapy to administrative or supplementary support, require patient consent before AI records or triages sessions, bar advertising psychotherapy delivered through companion chatbots, and require a licensed professional's review before AI makes therapeutic decisions. AB 2575 (workers' freedom to override AI clinical recommendations, plus a limit on the "clinician failed to override" liability defence) and SB 503 (bias testing for clinical-decision-support AI) also touch this lens, as does AB 1979 (no AI performing licensed clinical functions independently). The Legislature's status pages can lag the governor's office, so a signing announced Tuesday afternoon or Wednesday is still possible.
- **Portland psychedelics ordinance** — second-reading vote set for Wednesday 09-30, 9:30am, Council Chambers; no public testimony is taken at a second reading. No change to the ordinance page as of Tuesday afternoon.

Also pending from earlier: Florida's temporary-injunction motion against OpenAI (filed Monday 09-28) awaits OpenAI's response and a hearing date; none has been reported.

## 🔄 Map changes

None new to the map's thread list this afternoon. Late-buffer read: added the Australian High Court concession, the Apple-AAP guide and the JAMA Pediatrics screen-time review; the ACNP biomarker roadmap (Psychiatric Times 09-29) is a paper published 09-18, Instagram-head and pastor-v-OpenAI items are February and July stories resurfacing, and the FTC-Hims & Hers item is a 07-30 story, none used. 🔧 Correction (afternoon): the morning's source note said the 09-29 `gdelt`, `federal_register` and `clinicaltrials` files had not landed; they had (all three landed mid-morning), and the afternoon pass read them, finding nothing on-lens beyond the three trial registrations already listed. 🔧 Correction (morning): the California bill descriptions in the Upcoming section above were rewritten from the Legislative Counsel's Digests, replacing the earlier one-line summary of SB 903 as a bar on "marketing a chatbot as therapy," which captured one of its five provisions.

## 🧵 Thread candidates

None offered — nothing surfaced that clears the bar today.

---
A thin Tuesday: the new items are Australia's High Court concession on the evidence for its teen social media ban, Apple's parental-controls guide with the AAP, a JAMA Pediatrics screen-time review, a California CARE Court signing dated Sunday and reported today, the VA's $111.9 million suicide-prevention grants, and a Calgary psilocybin PTSD trial receiving its drug. California's four AI-in-health-care bills and Portland's psychedelics vote are both still due Wednesday.
