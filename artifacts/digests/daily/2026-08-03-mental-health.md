---
lens: mental-health
date: 2026-08-03
status: building
window_start: 2026-08-03T05:00:00-04:00
as_of: 2026-08-03T18:45:00-04:00
coverage: pending
---

# Mental Health — 2026-08-03

*Curated from the tier-2 mental-health deep sweep (agentic-interim). ⚠
Session WebSearch budget was exhausted before this lens ran; every claim
was verified via WebFetch, direct `curl` against primary sources, and
Google News RSS used for discovery only — nothing rests on an RSS snippet
alone. Legislative facts were pulled from RAW HTML, bypassing the WebFetch
summarizer that fabricated an "Aug 5" date on the 08-02 sweep.*

## Today's throughline

The thing this lens has been holding for finally exists. On the
legislature's first day back from recess, **SB 903 landed on the Assembly
Appropriations Committee's calendar for a hearing this Wednesday, August 5
at 9am** — the calendar entry naming the bill that the ledger said would
upgrade it from `reported` to `confirmed`. It is dual-verified against raw
HTML from two primary sources: leginfo's bill-status page (Committee
Hearing Date 08/05/26, "Asm Appropriations") and the committee's own live
Daily File (Wed Aug 5, 9am, Room 1100, Wicks chair, SB 903 named in the
day's list). This is a clean sequence, not a contradiction of the 08-02
read: on Sunday, in recess, the entry genuinely did not exist and the
summarizer's premature "Aug 5" was correctly refused; today it materialized
and is confirmed on the record.

## Policy, regulation & legal

- **SB 903 is confirmed calendared — Assembly Appropriations, Wed 08-05,
  9am.** leginfo carries the live Committee Hearing Date field (08/05/26,
  "Asm Appropriations"); the committee's own Daily File names SB 903
  (Padilla, "Mental health professionals: artificial intelligence") in that
  day's bill list, heard in sign-in order. The Daily File does **not** label
  it a suspense hearing, so whether it is held on suspense or moves forward
  is decided at/after 08-05. Sits inside the 08-14 fiscal-report deadline.
  Dual-verified against raw HTML, not the summarizer. `reported` →
  `confirmed`.
  ([California Legislature, primary](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260SB903))
  <!-- k: t=state-therapy-chatbot-bans e= axis=policy-and-governance sev=major -->
- **A named federal bill surfaced: the CHAT Act 2.0 (Husted/Kim).**
  Bipartisan senators introduced (07-29, picked up in coverage 08-03) an
  update to Husted's 2025 CHAT Act, tailored to companion and health
  chatbots: age verification, mandatory parental notification if a minor
  "expresses suicidal ideation," human-disclosure, usage limits,
  crisis-referral, memory restrictions and pre-deployment risk assessments,
  on a three-tier (educational/companion/health) framework enforceable by
  FTC/state AGs. ⚠ This is very likely the named version of — or successor
  to — the S.5154 Kim/Husted companion-chatbot bill this lens already
  tracks; the formal `S.` number could **not** be confirmed (congress.gov
  CAPTCHA-walled; the press release cites a drafting number, "LAN26388," not
  a public bill number). Treated as the same storyline, not a second item.
  ([Sen. Husted](https://www.husted.senate.gov/media/press-releases/husted-kim-lead-bipartisan-bill-to-protect-children-from-ai-companion-chatbots/))
  <!-- k: t=ai-therapy-regulatory-reckoning e= axis=policy-and-governance -->
- **Colorado HB 26-1195 nears its 08-12 effective date with no visible
  preparation** — no DORA rulemaking notice, no legal challenge, no
  professional-association statement. DORA's site 403'd most sub-paths on
  direct check (noted per discipline, not substituted with a claim). One
  more check closer to the date.
  <!-- k: t=state-therapy-chatbot-bans e= axis=policy-and-governance -->
- **Litigation quiet.** CourtListener (37 Character.AI cases, 109 entries)
  shows most-recent activity 07/23 (an amicus brief), before the window; no
  new filings/rulings dated 08-02/03 across Character.AI, Replika, OpenAI,
  Meta or xAI. The Minnesota xAI TRO denial (07-31) and 08-19 preliminary-
  injunction hearing are unchanged.
  <!-- k: t=state-therapy-chatbot-bans e=xai axis=policy-and-governance -->

## Clinical safety & harm

- **No new safety or harm development in this window.** The lens's active
  harm stories (the companion-chatbot litigation, the state bans) are
  covered under Policy above; nothing new on FDA digital-therapeutics
  (today's TEMPO/FDA item is Dexcom glucose-monitoring, confirmed out of
  scope), payer AI-denial, or MHPAEA parity.
  <!-- k: t= e= axis=clinical-safety-and-harm -->

## 🧪 Clinical trials

*Nothing new — no registrations or results in this window relevant to the
lens.*

## ⏳ Upcoming & expected

- ✅ **Confirmed calendared — `ca-sb903-assembly`**: the Appropriations
  calendar entry now exists; confidence `reported` → `confirmed`, source
  swapped to the bill-status page. The entry stays pending on the 08-14
  report-out outcome.
- **New to the ledger:** `ca-sb903-appropriations-hearing` **08-05** (the
  hearing itself — suspense-or-forward decision).
- ⚠️ **Two dates checked, neither adopted as new:** the SAMHSA **$73.2M**
  grant award (dated 07-31, general behavioral-health funding, not
  AI-specific — out of scope); an unconfirmed NY "restricting AI friends for
  teens" story on small-market outlets (could not get past bot-blocking to
  tell if it is existing S9051B/S9408A or new — flagged as a lead only).
- Next in this lens: `ca-sb903-appropriations-hearing` **08-05** ·
  `colorado-hb1195-effective` **08-12** · `ca-sb903-assembly` **08-14**
  (outer bound 08-29) · `cms-access-cohort-august` **08-17** ·
  `xai-mn-preliminary-injunction` **08-19** · `kaiser-nuhw-mediation`
  ~**08-31**.

## 🔄 Map changes

- `~ threads/state-therapy-chatbot-bans` — SB 903 confirmed calendared
  (08-05 hearing), `last_seen` → 08-03 (⟨daily 08-03⟩).

## 🧵 Thread candidates

- None from this lens today — the day's items route to existing threads.

---
SB 903 is confirmed on the Assembly Appropriations calendar for a hearing
this Wednesday, August 5 — the entry this lens has been waiting for,
dual-verified against raw HTML on the legislature's first day back from
recess. A named federal bill, the CHAT Act 2.0, surfaced in coverage but
is very likely the same Kim/Husted companion-chatbot storyline already
tracked, its bill number unconfirmed behind a CAPTCHA wall. Everything else
— Colorado's approaching effective date, the litigation docket, Kaiser-NUHW
— was genuinely quiet.
