---
lens: global-capital
date: 2026-08-22
status: building
window_start: 2026-08-22T05:00:00-04:00
as_of: 2026-08-23T10:00:00-04:00
coverage: pending
---

# Global Capital — 2026-08-22

*Curated agentic-interim, **reconstructed** on 2026-08-23 from one tier-2
AI-financing/IPO/macro sweep and one tier-2 capex sweep covering the
whole 2026-08-21 15:00 ET → 2026-08-23 10:00 ET gap, because no `/daily`
ran on 08-22. Plus this run's collector legs (fred, epfr_flows,
sec_edgar, federal_register, treasury_tic, imf_data, bis_stats,
page_diff, rss, gdelt). Read against `attention/capital-context.yaml`
(asof 2026-08-18).*

⚠️ **Left `building` / `coverage: pending`, but ONE benchmark was
checkable today and was checked.** Of this lens's four baselines, **FT
Unhedged does publish a Saturday edition** — it ran weekly on 08-01,
08-08, 08-15 and 08-22 — and today's critic pass read it. Money Stuff and
Axios Pro Rata are weekday-only, and Bloomberg Technology is currently
unauditable (see 🔄 Map changes). So the coverage check below is real but
one-quarter complete; the next run finalizes against Monday's editions.

## Today's throughline

**The one thing that happened on Saturday was a price increase, and it
lands on this lens harder than on the one it was filed under.** Nvidia
told the contract manufacturers building AI servers for Microsoft, Google
and Oracle that prices rise **more than 15%** on systems shipping in
early 2027, and named memory costs rather than its own pricing power as
the cause. Every hyperscaler capex plan this map tracks — the combined
$610-650bn across the four — was sized against a cost base that just
moved against them, and the beneficiaries are three companies this map
holds as search terms rather than as tracked entities.

**Markets were shut, so the day's real content is what Monday is
carrying.** Three dated events now sit in a four-day cluster: Bessent's
Iran sanctions package on **08-24**, Nvidia's Q2 earnings after the close
on **08-26** — repeatedly named across the sweep as the next catalyst for
the chip-versus-hyperscaler rotation argument — and **Lisa Cook's
response deadline to the White House's removal notice, also 08-26**. Then
Jackson Hole runs **08-27 to 08-29**, with Kevin Warsh giving his first
keynote as Fed chair. That is a sanctions action, a bellwether print, a
Fed-independence deadline and a new chair's first major speech inside six
days.

⚠️ **The blind spot this lens has now carried for three consecutive days
is finally being put to Ben as a decision.** Treasury long-end stress and
the Bessent interventions led this lens on 08-20 and 08-21 with no thread
to land on; the 08-21 digest recorded it as a candidate and it is
re-offered below with the Jackson Hole and Cook dates attached, which is
what makes it a decision rather than a repeat.

## 📊 Macro strip

- ⛔ **US markets closed** — Saturday. No new prints, no new levels.
  Friday's closes and the full rates/gold/bitcoin strip are in the
  **08-21** digest, where they belong.
- **The one Friday figure this map had not logged: the S&P Global flash
  US composite PMI came in at 56 for August**, the fastest US
  private-sector output growth in over four years. It is folded into the
  08-21 digest as a late catch rather than shown here, since it is an
  08-21 release.
- **No collector-side macro movement.** This run's `fred` leg returned
  one series update, `treasury_tic`, `imf_data` and `bis_stats` returned
  nothing, and `epfr_flows` fetched 36 records of which none passed the
  watchlist filter — consistent with a closed weekend.

## Capital in my markets

- **Nvidia is raising AI server prices more than 15%, which reprices
  every hyperscaler capex plan this map tracks.** The increase applies to
  systems shipping in early 2027, including Vera Rubin and Grace
  Blackwell configurations, and was communicated through the contract
  manufacturers that build for Microsoft, Google and Oracle. Nvidia's
  stated cause is soaring DRAM and HBM costs, with Samsung, SK Hynix and
  Micron holding the leverage. Read against this lens rather than the AI
  one: the combined ~$610-650bn of 2026 hyperscaler capex was planned at
  one cost per unit of compute, and a 15%-plus rise in the dominant line
  item either buys 15% less compute for the same money or requires more
  money for the same compute. Both answers are consequential and they
  point in opposite directions for the "capex is peaking" rotation
  thesis.
  ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-22/nvidia-customers-notified-about-ai-related-price-hikes-above-15),
  [Fortune](https://fortune.com/2026/08/22/nvidia-customers-ai-related-price-hikes-15-percent-vera-rubin-grace-blackwell-chips/),
  [CNBC](https://www.cnbc.com/2026/08/22/nvidia-customers-reportedly-warned-about-ai-related-price-hikes-.html))
  <!-- k: t=chip-hyperscaler-rotation,hyperscaler-capex-big-picture,ai-memory-shortage e=nvidia,micron,sk-hynix,samsung axis=capital-in-my-markets interp=yes -->

## Deals & filings

- **Nothing in window.** The sweep specifically checked
  `ai-circular-financing-risk`, `nvidia-vendor-financing`,
  `frontier-lab-ipos` and `pif-ai-buildout` and found no dated Saturday
  development on any of them. Everything that surfaced traces to 08-17 to
  08-19: the Nvidia/OpenAI Ohio guarantee, the AMD warrant story, the
  SB Energy Ohio deal, PIF's FY2025 annual report, and the NEOM
  contractor-exit reporting. Stated rather than omitted.

## ⏳ Upcoming & expected

**No flips today; 46 pending.** Nothing came due on 08-22.

**Four new expectations logged from this window** — the reason this
Saturday matters more as a calendar than as a news day:
- `jackson-hole-warsh-keynote` (**08-28**) — the Kansas City Fed's
  symposium runs 08-27 to 08-29 on "Financial Innovation: Implications
  for Payments and Policy," with Kevin Warsh's first keynote as chair
  expected Friday morning. ✅ Verified against kansascityfed.org directly,
  not commentary. `logged_by: curate-add`.
- `nvidia-q2-fy2026-earnings` (**08-26**, after close) — named repeatedly
  across the sweep as the next catalyst for the chip-vs-hyperscaler
  rotation and circular-financing arguments. Now also the first print
  after the price-rise notice above.
- `lisa-cook-removal-response` (**08-26**) — Cook's deadline to respond to
  the White House's removal notice. ⚠️ Nothing Cook-related appeared
  anywhere in this window; the date is carried from prior reporting.
- `anthropic-public-s1-filing` — **already pending** at 08-31, and
  re-confirmed: CNBC reports the filing could come "as soon as end of
  August," following the 06-01 confidential draft.

## Power & lobbying

- **Nothing in window.** No new sanctions action, lobbying disclosure or
  regulatory filing dated 08-22. `lda` — the lobbying-disclosure collector
  — returned nothing this run, but ⚠️ **it failed rather than came back
  empty**: all 160 terms returned HTTP 403. That is an unchecked surface,
  not a clean one, and it is recorded as such.

## 🔄 Map changes

- **New timeline blocks:** `chip-hyperscaler-rotation`,
  `hyperscaler-capex-big-picture`, `ai-memory-shortage` — the Nvidia
  price rise, written to each thread's own narrative.
- **Four expectations logged** — see ⏳ above.
- **Checked, nothing found, no edit:** `ai-circular-financing-risk`,
  `nvidia-vendor-financing`, `frontier-lab-ipos`, `pif-ai-buildout`,
  `red-sea-oil-shock`, `fed-independence-fight`, `ai-trade-bear-turn`,
  `ai-buildout-debt-risk`.
- ⚠️ **No `capital-context.yaml` refresh this pass.** The standing
  snapshot is still `asof 2026-08-18` and its oil assumption was already
  corrected once on 08-21. It should be refreshed after Monday's
  sanctions package and Jackson Hole, not against a closed market.
- **No entity adds applied.** Three are **proposed and held for Ben** —
  see thread candidates.
- ⚠️ **Two benchmark-health findings from today's critic pass, both
  affecting this lens's ability to audit itself:**
  - ⛔ **Bloomberg Technology is now unauditable.** A direct fetch returns
    HTTP 403 and the `r.jina.ai` reader proxy — which still clears FT and
    Axios cleanly — returns a Bloomberg CAPTCHA page instead of content.
    This is a **new escalation past the proxy-class fix** that resolved
    the other three benchmarks, and it means one of four baselines cannot
    be checked on any day, not just weekends. `sources/benchmarks.yaml`
    should record it; the fix is not obvious and may not exist.
  - ⚠️ **Money Stuff has published nothing since 2026-08-13.** The feed's
    `lastBuildDate` updates but the newest column is ten days old. Read
    as an author hiatus rather than a block — but for ten days this lens
    has been auditing itself against three baselines, not four, without
    saying so.

## 🧵 Thread candidates

- **candidate: Treasury long-end stress and the Bessent interventions** —
  ⚠️ **third consecutive offer, and the one this map most needs
  answered.** For three days running this lens's actual lead has been the
  US long bond — the buyback ceiling doubled to $4bn per issue on 08-19,
  the rally fully round-tripping by Friday, gold at a three-month high
  and bitcoin up 7-9% as the market read it as a currency story rather
  than a rates story, and Bessent saying he is ready to go beyond $4bn.
  This lens's own definition names Fed and Treasury moves as in scope,
  and there is no node for any of it: `fed-independence-fight` covers the
  *composition* of the Fed, not the *plumbing* of the long end. Three
  dated tests land inside six days — the Cook deadline 08-26, Jackson
  Hole 08-27 to 08-29, Warsh's first keynote as chair 08-28. — track it?
  (curator-noticed, third offer)

- **candidate: the memory makers as tracked entities** — Samsung, SK
  Hynix and Micron now set the price of the AI buildout, and this map
  holds all three as watchlist search terms with no `entity:` slug, so
  they cannot be tagged on a bullet or appear on an entity page. The
  Nvidia price rise is the first item where the missing entities are the
  *subject*. Give them slugs, and consider lifting `ai-memory-shortage`
  from weight 2 to weight 3? — track it? (tier-2 capex sweep)

**Carried, not re-offered:** the Lubbock data-center moratorium petition
(offered 08-18, 08-19) still needs an explicit track/drop call.

⚠️ **No mechanically-scored candidates offered this run, and the reason
changed today.** `attention/world-news.yaml` has been stale from 08-18
because GDELT failed three consecutive collector runs. The collector's
`gdelt` leg **did** complete this run — but `build-world-news`, the tool
that actually rebuilds that file, reads **GDELT's BigQuery dataset via
`bq`**, not the collector buffer, and `bq` failed today on expired gcloud
credentials. ⛔ Only Ben can clear that, with `gcloud auth login`.

## Appendix — Coverage check vs. benchmarks (PARTIAL)

⚠️ **One of four benchmarks was checkable on a Saturday. This is a
partial pass and the day stays `coverage: pending` because of it.**

**They led with → we missed:** nothing. FT Unhedged's 08-22 edition led
with *"Chart of the Week: Who owns government bonds?"* — the
structural-ownership-shift angle on the same Treasury long-end story it
led with on 08-20 (*"Big Brother Bessent is watching you"*) and 08-21
(*"Nellie Liang: 'Ultimately the goal is to signal that high rates are a
concern'"*). ⚠️ **That is three consecutive editions of this lens's most
important benchmark leading with the one story this map has no node
for** — the strongest single argument yet for the thread candidate below,
and the reason it is being put as a decision rather than offered a fourth
time. It is not scored as a miss: a chart-of-the-week analysis piece is
not a dated event, and this map's 08-20 and 08-21 digests both carry the
underlying story in substance.

**Both covered:** the Treasury long-end story itself — in content, not in
structure.

**We had → they didn't:** the Nvidia server price rise. FT Unhedged's
Saturday edition did not carry it.

**Not checked:** Money Stuff (weekday-only, and dark since 08-13
regardless), Axios Pro Rata (weekday-only), Bloomberg Technology
(access-blocked — see 🔄).

---
US markets were shut, so Saturday's only real event was a price: Nvidia
told the manufacturers that build AI servers for Microsoft, Google and
Oracle that systems shipping in early 2027 cost more than 15% more, and
named DRAM and HBM rather than its own margin as the reason. That
reprices the roughly $610-650bn of hyperscaler capex this map tracks
against a cost base nobody planned for, and hands the pricing power to
three companies this map cannot currently tag on a bullet. The rest of
the day is a calendar: Bessent's Iran sanctions land Monday, Nvidia
reports Wednesday after the close on the same day Lisa Cook must answer
the White House's removal notice, and Kevin Warsh gives his first Jackson
Hole keynote as Fed chair on Friday.
