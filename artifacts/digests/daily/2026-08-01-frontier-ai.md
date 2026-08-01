---
lens: frontier-ai
date: 2026-08-01
status: building
window_start: 2026-08-01T05:00:00-04:00
as_of: 2026-08-01T07:10:00-04:00
coverage: pending
---

# Frontier AI — 2026-08-01

*Curated from a partial collector run plus a dedicated expectations sweep
(agentic-interim). **The digest-day is roughly two hours old at this
writing** — it opened at 05:00 ET this morning — so this is an opening
read, not a day in review; a later run extends it. The collector run was
also partial: `collect.py` timed out at 900s having completed only 7 of
its lower-yield sources, and the three news-bearing collectors had to be
re-run individually (`rss` and `gdelt` returned; `google_news_rss` was
still running at this writing). See ⚠ note under Map changes.*

## Today's throughline

The day's real event is a non-event, and it is the loud kind. **Two
federal AI-governance deadlines came due today and neither was met.**
Executive Order 14409, signed 2026-06-02, required two 60-day
deliverables by 08-01: a classified NSA-led benchmarking process to set
the threshold at which a model becomes a "covered frontier model," and
the design of the Section 3(b) framework giving the government up to 30
days of pre-release access. Neither has been published, and there is no
public acknowledgment that even the classified half was delivered — not
a terse notice from NSA, CISA, Treasury or NIST. The separately-tracked
White House announcement of that same voluntary framework also did not
happen; as of 07-29 it was still a draft in dispute with OpenAI,
Anthropic and Google over what counts as a "frontier model" and how
open-source is treated. Both ledger entries flip to **passed-silent**,
which in this system is the loud outcome, not the empty one.

## Policy & governance

- **EO 14409's two 60-day deliverables passed their deadline with
  nothing published** — the classified frontier-model threshold
  (Treasury / Dept of War-NSA / DHS-CISA, consulting NIST and Commerce)
  and the Section 3(b) 30-day pre-release access framework design. The
  classified half could legitimately have landed without public content,
  but there is no acknowledgment of completion at all, which is the
  weaker signal. A CRS brief (IF13268, 07-09) independently confirms the
  same deadline and agency list, so the date itself is not in question.
  ([EO 14409, primary](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/))
  <!-- k: t=frontier-model-gov-review-precedent e= axis=policy-and-governance sev=major -->
- **The White House's voluntary pre-release review framework was not
  announced either** — the "before 08-01" target from 07-22 reporting.
  whitehouse.gov carries no successor to the original EO page. As of
  07-29 the framework was still circulating as a draft, with the three
  labs having jointly submitted revisions and core disputes unresolved on
  the definition of "frontier model" and open-source exemptions;
  Altman's meeting with chief of staff Susie Wiles the week of 07-27 was
  itself a symptom of it not being final. **These two entries were
  tracking the same deliverable** — same 60-day clock, same agencies,
  same 30-day access mechanism — and are recorded as such now.
  <!-- k: t=frontier-model-gov-review-precedent e=openai,anthropic,google axis=policy-and-governance -->

## Product & access

- **Nothing yet — the day is two hours old.** No release, access change,
  or pricing move from any lab inside this window at this writing.
  <!-- k: t= e= axis=product-and-access -->

## ⏳ Upcoming & expected

- ⚠️ **passed-silent — `eo14409-deadlines`**: both 60-day deliverables
  unmet, no acknowledgment of the classified half. 3-day retro-flip grace
  runs to 08-04 before this stands.
- ⚠️ **passed-silent — `gov-review-framework-announce`**: no announcement;
  still a disputed draft as of 07-29. Same grace window to 08-04. Same
  underlying deliverable as the entry above.
- ✅ **hit — `mn-nudify-ban-effective`** and ✅ **`minnesota-nudify-effective`**:
  full detail on Mental Health.
- **New — and it lands tomorrow:** `eu-ai-act-code-of-practice`, due
  **08-02**. The EU AI Act's Code of Practice obligations for
  general-purpose models bind on Sunday. This map was not tracking it at
  all; it surfaced only because OpenAI published a compliance post two
  days ahead of it. ⚠ Logged `confidence: reported` — the date comes from
  OpenAI's own post and trade press, and should be verified against the
  EU instrument itself before it is treated as confirmed.
- **New:** `xai-mn-preliminary-injunction` — 08-19 hearing (curate-add).
- Next 7 days: `spacex-q2-earnings` 08-04 · `softbank-q1-earnings` and
  `spacex-insider-unlock` 08-06 · `grok-4-6-ship` and
  `cxmt-congress-letters` 08-07.
- 41 expectations on the ledger: 15 hit, 2 passed-silent, 24 pending.

## 🔄 Map changes

- `~ upcoming/gov-review-framework-announce` — pending → **passed-silent**,
  evidence attached, grace to 08-04 (⟨daily 08-01⟩).
- `~ upcoming/eo14409-deadlines` — pending → **passed-silent**, evidence
  attached, grace to 08-04 (⟨daily 08-01⟩).
- `~ upcoming/mn-nudify-ban-effective`, `~ upcoming/minnesota-nudify-effective`
  — pending → **hit**, primary-sourced evidence attached (⟨daily 08-01⟩).
- `+ upcoming/xai-mn-preliminary-injunction` — 08-19 (curate-add 08-01).
- `~ threads/*` — 9 timeline files updated for 07-30/07-31 developments
  caught by this run's finalize and late-window sweeps; `last_seen`
  advanced on 7 threads.
- ⚠ **Tooling note, not a map change:** `collect.py`'s serial fan-out hit
  its 900s timeout after 7 low-yield sources, leaving the news collectors
  unrun. Running `--source rss`, `--source gdelt` and
  `--source google_news_rss` concurrently instead returned `rss` in under
  a minute. This is direct evidence for the diagnosis already filed to
  kestrel's INBOX on 07-31; the engine repo owns the fix.

## 🧵 Thread candidates

- None from this lens — the day is two hours old. One candidate is open
  on World News (the Gaza war).

---
Two federal AI-governance deadlines came due today and neither was met:
EO 14409's classified frontier-model threshold and its 30-day
pre-release access framework, plus the White House announcement of that
same framework, which was still a disputed draft as of Wednesday. Both
ledger entries flip to passed-silent, with a three-day grace before they
stand. Nothing else has happened yet — the day is two hours old.
