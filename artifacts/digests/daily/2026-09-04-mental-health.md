---
lens: mental-health
date: 2026-09-04
status: building
window_start: 2026-09-04T05:00:00-04:00
as_of: 2026-09-04T15:00:00-04:00
coverage: pending
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
