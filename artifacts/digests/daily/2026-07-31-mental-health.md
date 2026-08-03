---
lens: mental-health
date: 2026-07-31
status: final
window_start: 2026-07-31T05:00:00-04:00
as_of: 2026-08-01T06:50:00-04:00   # extended 08-01: 09:15 curation missed the rest of the day
coverage: done   # critic run 2026-08-02, two days late; appendix at foot
---

# Mental Health — 2026-07-31

*Curated from the 18-collector run (`collect.py`) plus 1 tier-2 cluster
research agent, WebSearch/WebFetch-verified against primary sources
(congress.gov, court filings) where available.*

## Today's throughline

The first FEDERAL companion-chatbot bill for minors surfaced — a
bipartisan Senate bill introduced 07-28 that this sweep only caught via
wire pickup dated 07-30, a genuine map gap now closed. It directly
answers `state-therapy-chatbot-bans`'s standing "preemption pressure"
watch question. Separately, a federal judge kept the Jane Doe plaintiffs
in the Grok deepfake suit pseudonymous — incremental, not a reset.

**Extended 08-01:** the day's biggest development came later and was
missed by the 09:15 curation — a second federal judge, in Minnesota,
denied xAI's bid to block that state's AI-nudification ban, so HF1606
took effect Saturday on schedule. Two adverse rulings against xAI, in two
different federal courts, in two unrelated cases, on one day. The state
bills were not quiet after all; Kaiser mediation, MHPAEA and CMS ACCESS
genuinely were.

## Policy & governance

- **A federal bipartisan companion-chatbot bill for minors was
  introduced 2026-07-28** (Sens. Andy Kim D-NJ / Jon Husted R-OH,
  S.5154, "Children Harmed by AI Technology Act 2.0") — a tiered
  risk-based framework barring AI companion chatbots from encouraging
  self-harm, generating sexual content, impersonating humans, or
  emotionally manipulative/romantic interaction with minors, plus
  parental-involvement and disclosure mandates; referred to Senate
  Commerce. A map gap: introduced 07-28, never logged until wire pickup
  surfaced it 07-30. First federal instrument in a space that's been
  entirely state-law so far.
  ([congress.gov S.5154](https://www.congress.gov/bill/119th-congress/senate-bill/5154))
  <!-- k: t=state-therapy-chatbot-bans,grok-companion-harm e= axis=policy-and-governance -->

## Clinical safety & harm

- **A federal judge denied xAI's bid to unmask the Jane Doe plaintiffs**
  in the Grok deepfake suit (N.D. Cal., Judge P. Casey Pitts) — the
  court found their fear of retaliation "reasonable," letting the case
  proceed pseudonymously. Incremental litigation development, not a
  reset.
  ([Law360](https://www.law360.com/articles/2507907))
  <!-- k: t=grok-companion-harm e=xai axis=clinical-safety-and-harm -->
- **A second, separate ruling went against xAI the same day: a federal
  judge in Minnesota denied its bid to block that state's AI-nudification
  ban, and HF1606 took effect Saturday 08-01 as scheduled.** Judge Donovan
  W. Frank held that xAI's near-three-month delay between the law's
  signing and its 07-27 suit "suggests that harm is not immediate" —
  precisely the filed-is-not-a-stay distinction the ledger entry was
  written to test. The statute carries civil penalties up to $500,000 per
  violation and a private right of action. Not adjudicated on the merits:
  Frank will treat the TRO motion as a preliminary-injunction request at
  an 08-19 hearing in St. Paul, with the state's opposition due 08-12 and
  xAI's reply 08-17. Two adverse rulings for xAI in two different federal
  courts on the same day, in two different cases — worth not conflating
  with the Jane Doe ruling above (that one is N.D. Cal., the Tennessee
  CSAM-adjacent deepfake suit; this one is D. Minn., No. 0:26-cv-03425,
  a First Amendment challenge to a state statute).
  ([Minnesota Legislature, primary](https://www.house.mn.gov/NewLaws/story/2026/5741), [NBC News](https://www.nbcnews.com/tech/elon-musk/judge-denies-request-elon-musks-xai-block-mn-nudification-ban-rcna589993))
  <!-- k: t=grok-companion-harm,state-therapy-chatbot-bans e=xai axis=clinical-safety-and-harm sev=major -->

## ⏳ Upcoming & expected

- **⟨08-01⟩ — the decisive event for both Minnesota entries happened
  today, not on their due date.** Judge Frank's TRO denial (above) landed
  07-31; the law then took effect 08-01, so `mn-nudify-ban-effective` and
  `minnesota-nudify-effective` both flip **hit** in 08-01's digest, on
  evidence generated inside this digest-day.
- `colorado-hb1195-effective` 08-12;
  `ca-sb903-assembly` still unresolved (08-14 vs 08-29 unsettled);
  `kaiser-nuhw-mediation` due 08-31, checked — no firm date found, the
  thread's "no date yet" stands.

## 🔄 Map changes

- `~ threads/state-therapy-chatbot-bans`, `~ threads/grok-companion-harm`
  — timeline blocks added (⟨daily 07-31⟩).

## 🧵 Thread candidates

- None new today — both real developments landed on existing threads.

---
A federal companion-chatbot bill for minors (S.5154) surfaced — introduced
07-28, only caught today, and it directly answers the state-ban thread's
preemption question. A federal judge kept the Grok deepfake plaintiffs
pseudonymous. And a second federal judge, in Minnesota, refused to block
that state's AI-nudification ban — so the law took effect Saturday, and
xAI lost twice in one day in two different courts.

## Appendix — Coverage check vs. benchmarks

*Run 2026-08-02 (two days late). Benchmarks: STAT Health Tech (accessed
directly), Fierce Healthcare (homepage confirmed, subsections 403),
Behavioral Health Business and MobiHealthNews (search-snippet only — both
403'd every direct fetch, so absence of a finding there is not
conclusive).*

**They led with → we missed:**
- ⚠️ **RETRACTED (08-03 critic) — the Woebot "miss" was a 15-month-old
  story, not a 07-31 development.** This appendix originally logged
  "Woebot Health is shutting down its app" as a benchmark-recall catch. The
  08-03 coverage critic verified the MobiHealthNews article is dated
  **2026-04-25 — of 2025**; the app retired **2025-06-30** (five mirror
  sites + a Feb-2026 Wayback capture agree). It is not from this window and
  was never a real miss — the recall "win" is withdrawn. The failure was
  logging on a headline+URL whose *date* had not actually been confirmed
  against the digest window, behind the same hedge that flagged the fetch
  as blocked. Root-cause and lesson are in `coverage-log.md`. Original
  (now-false) text struck through below.
  <br>~~**Woebot Health is shutting down its app** (MobiHealthNews, 07-31).
  A named AI-mental-health-chatbot company — it held an FDA breakthrough
  designation for a postpartum-depression chatbot — closing down on the
  same day this lens covered a federal companion-chatbot bill and two
  adverse AI-chatbot court rulings. Squarely on this lens's own theme and
  entirely absent. ⚠ Only the headline, URL and date are confirmed; the
  site blocked full-text fetch.~~
  ([MobiHealthNews](https://www.mobihealthnews.com/news/woebot-health-shutting-down-its-app))

**Both covered:** none — no benchmark surfaced the companion-chatbot bill,
the Grok pseudonymity ruling or the Minnesota ruling in what was
retrievable.

**We had → they didn't:** the federal bipartisan companion-chatbot bill
for minors (S.5154, Kim/Husted) · the Grok deepfake *Jane Doe*
pseudonymity ruling (N.D. Cal.) · the Minnesota AI-nudification ruling
against xAI (D. Minn.).

**Correctly out of scope, not misses:** BayMark's bankruptcy risk,
Acadia's bed-addition strategy, Precise Behavioral's $14.2M raise,
Function Health's $450M raise, a CMS IPPS rule, a 340B rebate pilot,
Alignment's Q2 — general healthcare-business items outside this lens's
AI-and-mental-health scope.

**Map adds:** none. Woebot is a single data point; the pattern worth
watching is AI-mental-health-chatbot companies under financial distress,
which wants a second instance before it earns a thread.
