---
lens: mental-health
date: 2026-09-04
status: final
window_start: 2026-09-04T05:00:00-04:00
as_of: 2026-09-05T05:00:00-04:00
coverage: done
---

# Mental Health — 2026-09-04

*Curated agentic-interim, 05:00 ET → **15:00 ET** Friday — extended on the
15:00 run from a 10:40 ET build, with two afternoon sweeps (regulation/
clinical/payer, and the evidence base plus big tech's health arms) that
returned one catch between them. Sources: two rounds of the deterministic
lanes (`rss` 474 items including STAT, Behavioral Health
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
  ([SB 903 status](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260SB903), [Transparency Coalition, 09-04](https://www.transparencycoalition.ai/news/ai-legislative-update-september4-2026))
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
  ([NUHW](https://home.nuhw.org/2026/09/02/san-francisco-passes-resolution-opposing-kaiser-contract-demands/), [KALW](https://www.kalw.org/bay-area-news/2026-09-02/sf-supervisors-push-back-on-kaisers-use-of-ai-in-mental-health-care))
  <!-- k: t=kaiser-ai-clinician-backlash e=kaiser-permanente axis=labor -->

- **Character.AI named new crisis-routing and CSAM-detection partners in a
  safety update, the incumbent under the most direct legal pressure
  restating publicly what it says it is doing.** The company's own blog post
  says it has partnered with **Koko** (free self-guided emotional-support
  tools) and **ThroughLine** — a global directory that routes a user to
  country-specific crisis resources rather than to a single hotline number,
  which matters for a service with users outside the US — and that its
  self-harm detection now weighs signals accumulating across a whole
  conversation rather than any single message. On the imagery side it says
  it has joined the **Internet Watch Foundation** (a global CSAM-detection
  network it now reports into) and **StopNCII** (privacy-preserving
  hash-matching against non-consensual intimate imagery). It also announced
  a moderation-appeals process for creators, mutual-blocking controls, and
  continued work on its in-house age-estimation model and the k-ID-built
  Parental Insights tool for the under-18 experience it walled off from
  open-ended chat last year. **Read this for what it is: a primary source
  about what the company says it does, not evidence that any of it works** —
  no effectiveness data accompanies it. It lands with force because of who
  is saying it, with the Pennsylvania suit and the Setzer settlement both
  live. This also resolves an item yesterday's digest saw in the buffer and
  could not verify at the time.
  ([Character.AI](https://blog.character.ai/continuing-to-build-upon-our-safety-priorities/))
  <!-- k: t=ai-therapy-regulatory-reckoning e=character-ai axis=safety -->

- **A federal judge refused to block Minnesota's AI-nudification ban, leaving
  it enforceable against xAI while the constitutional challenge proceeds —
  the second ruling against xAI in this case.** U.S. District Judge Donovan
  W. Frank denied the preliminary injunction on 2026-09-04 in a 14-page
  memorandum opinion, read here from the docket itself rather than from
  coverage of it (Doc. 54, *X.AI LLC v. Ellison*, No. 26-3425, D. Minn.).
  H.F. 1606 bars any service from letting a user "nudify" an image or video
  — alter or generate one to depict an intimate part not in the original —
  with civil penalties up to **$500,000 per violation**, and those penalties
  now stay live through trial. The order's background section cites
  legislative testimony that a single identified perpetrator used
  nudification tools against **more than 80 women**, and RAINN's estimate of
  **24 million monthly users** of such apps in 2023, over 95% of whose
  outputs were non-consensual, sexually explicit and depicted women. **This
  resolves the "under advisement" status this thread has carried since the
  08-19 hearing**, where Frank took the matter without ruling from the
  bench. A TRO was already denied on 07-31, and the Trump DOJ's 08-19/20
  Statement of Interest supporting xAI did not change the outcome. A motion
  to dismiss xAI's underlying suit remains pending.
  ([Order, Doc. 54, via CourtListener/RECAP](https://storage.courtlistener.com/recap/gov.uscourts.mnd.235231/gov.uscourts.mnd.235231.54.0_1.pdf), [MPR News](https://www.mprnews.org/story/2026/09/04/judge-lets-minnesota-enforce-antinudification-app-law-over-xai-objection-as-case-proceeds))
  <!-- k: t=grok-companion-harm,state-therapy-chatbot-bans e=xai axis=legal sev=major -->

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
- ⚠️ `california-ai-mh-bills-0930` — **carried forward from this morning's
  check, not independently re-verified this afternoon.** The Legislature's
  own bill-history pages did not render to an automated fetch (they depend
  on JavaScript), so the afternoon sweep declined to re-assert the
  five-bills-unsigned status rather than restate it as freshly checked.
  Morning's live check stands; the limit on it is named.
- 📋 Nothing else dated for this lens before 09-15. **The FDA psychedelic
  public hearing (09-14) was re-checked against the Federal Register API
  directly this afternoon** — no new notice, no schedule change.

## 🔄 Map changes

- `+` watchlist term `Adam's Law` (critic-add) — the press's popular name
  for SB 1119, which this map tracks by bill number only. A number-only
  term set misses every story that uses the name, and on 09-03 most did.
- `✎` timeline entries merged on `kaiser-ai-clinician-backlash`,
  `meta-ai-csam-ads`, `canada-ai-vs-care`, `psychedelic-regulatory-sprint`,
  `neuromodulation-evidence`, `ai-therapy-evidence`.
- **Afternoon pass (15:00):** `✎` timeline entries merged on
  `ai-therapy-regulatory-reckoning` (the Character.AI safety update above)
  and `grok-companion-harm` (the Minnesota ruling, surfaced by buffer
  triage and read from the docket, not from coverage). No new watchlist
  terms; no corrections found against this morning's build. ⚠️ The
  California bills ledger line is carried forward rather than re-verified —
  see above.
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

## 🌙 Late catch — the 09-04 evening window (15:00 ET → 05:00 ET)

*Swept on the 09-05 finalize. Events below are dated 2026-09-04 and belong
to this digest-day; they landed after the 15:00 ET cut.*

- **California's AB 1979 was enrolled and presented to Governor Newsom at
  4pm on 09-04 — the second of the five AI and mental-health bills to
  actually reach his desk, after SB 503 on 08-30.** AB 1979 brings consumer
  health chatbots under the Confidentiality of Medical Information Act and
  bars AI-alone clinical decisions without human review. SB 903, SB 1119
  ("Adam's Law") and AB 2575 remain one procedural step behind, at
  "engrossing and enrolling," four days after adjournment; nothing has been
  signed or vetoed, and the Governor's newsroom carried no action on any of
  the five through the morning of 09-05. The deadline is 09-30. Read from
  the Legislature's own bill-history page, which — contrary to the note
  above — does serve its action table to a plain fetch.
  ([AB 1979 bill history](https://leginfo.legislature.ca.gov/faces/billHistoryClient.xhtml?bill_id=202520260AB1979), [Transparency Coalition, 09-04](https://www.transparencycoalition.ai/news/ai-legislative-update-september4-2026))
  <!-- k: t=ai-therapy-regulatory-reckoning,state-therapy-chatbot-bans axis=regulation -->
- **A JMIR Mental Health systematic review and meta-analysis found that
  home-based, remotely supervised tDCS for depression produces only a
  small, statistically fragile effect, with the two largest trials in the
  pool negative.** Six sham-controlled RCTs pooled to Hedges g = 0.36
  (95% CI 0.06-0.66); dropping the single largest positive trial widens the
  interval to include zero. Only the largest real-time-supervised trial was
  positive; the two largest unsupervised or self-administered trials were
  not. GRADE certainty moderate; the authors call the data "insufficient to
  recommend routine clinical adoption." One pilot stopped early for skin
  lesions and one non-fatal suicide attempt occurred in an unsupervised
  arm. It is the controlled-trial context for the single-arm home-tDCS
  study logged 09-03, and it sits well behind the confirmatory-RCT status
  of accelerated TMS protocols such as SAINT.
  ([JMIR Mental Health, DOI 10.2196/92522](https://mental.jmir.org/2026/1/e92522))
  <!-- k: t=neuromodulation-evidence,mh-evidence-watch axis=evidence -->

- **A Massachusetts jury deadlocked 11-1 toward finding Lindsay Clancy not
  criminally responsible for killing her three children, and Judge William
  Sullivan declared a mistrial on the evening of 09-04, ending a five-week
  trial that turned on whether postpartum psychosis removed her criminal
  responsibility.** Clancy, 36, was charged with strangling her three
  children, aged five, three and eight months, in Duxbury in January 2023,
  weeks after discharge from a psychiatric hospital; the defence argued
  auditory hallucinations ordered the killings, the prosecution that she
  planned them as part of a suicide. The mistrial came after a Supreme
  Judicial Court justice declined an emergency stay; the Plymouth County DA
  has not said whether he will retry. Postpartum Support International used
  the outcome to call for a US infanticide law of the kind more than 24
  countries have. The trial was covered here on 08-12 and 08-21 and offered as a
  thread candidate both times without a ruling; **no thread holds it**, and
  it is re-raised in the 09-05 digest because the trial has now ended and
  the policy tail has begun.
  ([WBUR](https://www.wbur.org/news/2026/09/04/lindsay-clancy-murder-trial-verdict-massachusetts), [CNN](https://www.cnn.com/2026/09/04/us/live-news/lindsay-clancy-trial), [Postpartum Support International](https://postpartum.net/postpartum-support-international-calls-for-reform-as-lindsay-clancy-case-ends-in-mistrial/))
  <!-- k: axis=legal -->
- **Cardinal Blase Cupich, two orders of Catholic nuns and a pharmacist sued
  Illinois on 09-03 over its physician-assisted-suicide law, nine days
  before it takes effect on 09-12**, arguing the Act's requirement that a
  refusing physician transfer records "without undue delay" to a willing
  provider, and its bar on health-care entities prohibiting staff from
  participating outside their employment, violate religious-freedom rights.
  A first suit (Thomas More Society, for Bishop Paprocki and four doctors)
  has already won a temporary injunction for its named plaintiffs, so the
  law is heading into effect for most of the state with a growing carve-out
  list. No thread; recorded as ambient on the psychiatric-ethics edge of
  this lens.
  ([America Magazine](https://www.americamagazine.org/news/2026/09/04/chicago-assisted-suicide-lawsuit-catholic-cupich), [Becket Fund](https://becketfund.org/media/cardinal-cupich-catholic-nuns-sue-illinois-to-stop-law-forcing-them-to-help-patients-kill-themselves/))
  <!-- k: axis=legal -->

**🧪 Clinical trials, corrected.** The verdict above — that the 09-04 batch
of 346 was "routine" and that the entries checked "did not survive that test
as real" — was **half wrong**, on a smaller scale than 09-03's. The critic
re-scored all 346 against non-generic mental-health terms and pulled the
registry record for every plausible candidate. Two are real, on-topic and
first-posted in the window: **NCT07805395** (Northwestern; a Phase 2
feasibility trial of a mental-health family-navigator model for foster
parents, n=60, first posted 09-04, recruiting) and **NCT07803367** (Beijing
Normal University; nature photography for psychological distress, depressive
and anxiety symptoms in young adults, n=300, first posted 09-03). Neither
moves a thread on its own. The finding that does: NCT07803367 matched only
**one** non-generic term, so the "two-or-more terms" spot-check rule adopted
on 09-04 would have skipped it — the registry's own `conditions` field is
the better filter, and that is the rule from here.
([NCT07805395](https://clinicaltrials.gov/study/NCT07805395), [NCT07803367](https://clinicaltrials.gov/study/NCT07803367))

## 🔍 Coverage critic — digest-day 2026-09-04

**Verdict:** two real misses, both from the clinical-trials spot-check the
brief asked for, none from the trade-press benchmarks — and the two halves
pull opposite ways. The trade-press check is close to a null result:
Behavioral Health Business was genuinely dark on Friday (its own
`lastBuildDate` is Thursday 21:24 GMT), **STAT Health Tech turns out to be
a Tuesday/Thursday newsletter, not daily** (its items self-describe as such
— a cadence fact worth writing into the benchmarks file), and Fierce and
MobiHealthNews published nothing mental-health-specific that was not already
here (UHS/Talkspace, OpenAI/Epic). The registry check, by contrast, did real
independent verification and found the digest's own batch verdict partly
wrong. The PubMed cross-check found the JMIR tDCS meta-analysis — real,
absent from the digest, and independently caught the same morning by the
evidence sweep, so it counts as corroboration rather than a fresh miss.

| benchmark | state | evidence |
| --- | --- | --- |
| Behavioral Health Business | **dark** Friday | `lastBuildDate` Thu 09-03 21:24 GMT; newest item 20:05 |
| STAT Health Tech | dark Friday (cadence) | newest item Thu 09-03; self-described Tue/Thu newsletter |
| Fierce Healthcare | published, nothing MH-specific | 4 items 09-04 (AMC M&A op-ed, Cuban, Oura IPO, Dealmakers recap) |
| MobiHealthNews | published, nothing MH-specific | 4 items 09-04 (OpenAI/Epic, HIMSSCast, Thyme Care, hospital AI training) |
| JMIR Mental Health | published, one real item | PMID 42696738, the tDCS meta-analysis |
| npj Digital Medicine / JAMA Psychiatry / Lancet Psychiatry | no 09-04 items | PubMed E-utilities, zero results each |

**Acted on:** `transcranial direct current stimulation` and `tDCS` added as
watchlist terms (the meta-analysis landed in the buffer with no term
matched — the thread's second modality had no term coverage at all); the
spot-check rule widened to the registry's `conditions` field. **Access:**
PubMed E-utilities works for all four journal benchmarks, not just the two
Cloudflare-blocked ones, and is the right default cross-check transport for
the weekly tier.
