# The Memory Trio — Samsung / SK Hynix / Micron capacity-race backstory

*Crawl date: 2026-07-28. Backward crawl answering: who's actually winning the
HBM race the AI buildout is squeezing DRAM/NAND supply for, and how exposed
is each of the three non-China HBM makers to Nvidia's favor and to CXMT's
entry. Bundle: `artifacts/bundles/memory-trio-2026-07-28/`. Feeds the
ai-memory-shortage thread's capacity-race backstory and the missing
actor-doing syntheses for samsung/sk-hynix/micron.*

Method note: WebSearch was pre-exhausted on all three lanes before a single
query ran (session-shared budget). Three parallel sonnet subagents ran
WebFetch against Google News RSS search feeds and DuckDuckGo HTML search as
fallback, resolving to publisher URLs where possible. Google News' own
redirect links (`news.google.com/rss/articles/...`) essentially never
resolve to article body text via WebFetch (empty JS shell) — those are
cited as RSS metadata only (title/source/date), marked **medium** at best.
**High** = a full article body was directly fetched from the publisher (or
a primary IR/press-release page). **Medium** = RSS/search-snippet metadata
only, single outlet or a small convergent cluster. **Thin** = single
outlet, headline-only, unclear methodology, or a figure that looks like an
outlier and wasn't cross-verified. Nothing below is fabricated; explicit
gaps are marked **not found** rather than guessed. Several outlets
(chosun.com, techtimes.com, reuters.com) blocked direct WebFetch (403) —
their claims are carried at RSS/snippet confidence only.

---

## 1. Samsung — chasing a lead it's never had

**HBM share + roadmap.** Historically the #2 to SK Hynix's #1: a
2026-01-29 Chosun figure puts SK Hynix at 55% vs Samsung's 27% HBM share
(medium, snippet-level — chosun.com blocked direct fetch). But UBS
(reported 2026-07-16, finance.biggo.com) forecasts Samsung **overtaking**
SK Hynix on HBM bit-capacity share in 2027 — **41% vs 39%**, Samsung's
first-ever lead — with Bernstein projecting 45% by 2028 (medium). On
qualification, the picture is contested: winbuzzer.com (direct fetch,
**high**, 2026-07-17) reports Samsung is still at Nvidia's "paid
evaluation" stage for HBM4, no confirmed volume-production order, while SK
Hynix has "deepened" its Nvidia tie and Micron stayed HBM3E-focused as of
that date. Competing reporting (Investing.com, 2026-06-05, medium) has
Jensen Huang publicly validating all three as qualified HBM4 Vera Rubin
suppliers and Samsung starting HBM4 mass production in Feb 2026 at 11.7
Gbps/pin. Read the two together as: broad qualification cleared industry-
wide, but the decisive Nvidia *volume-order* milestone specifically had
not landed for Samsung as of mid-July. HBM4E: Samsung passed **$1B
cumulative HBM4E sales** by 2026-06-23 (medium, Chosun snippet), ahead of
the other two's full HBM4 ramp.

**Capacity expansion.** 2026 capex raised to **~$73.2B (110tn won)**,
+22% YoY, announced 2026-03-19 — Pyeongtaek and Yongin (Korea) plus Taylor,
TX named in coverage (medium, search-synthesis, not a raw fetch). **Xi'an
was NOT substantiated** in this crawl — do not cite it. A new Giheung DRAM
fab targeting 100K wafers/month "to ride the HBM wave" surfaced
2026-07-15 (thin, RSS title only). Several thin/RSS-only items point to
Pyeongtaek allocating 50%+ to HBM4 base die and capacity moves being
accelerated 6 months.

**AI-demand exposure.** Nvidia and AMD are the named customers; no
Google/Amazon/Meta/Broadcom-specific Samsung HBM allocation surfaced.

**Pricing posture.** Confirmed sequential Q2 2026 contract pricing: **DRAM
+44%, NAND +53% QoQ** (high — direct fetch, TheNextWeb). A further ~20%
Q3 hike is being sought (thin-but-multi-outlet-corroborated, 2026-07-03/06)
— and **Vivo and Oppo reportedly rejected** Samsung's latest DRAM price
hike (2026-07-21, thin, two outlets) — the clearest customer-pushback
signal found across the trio. Full memory-division profitability
(separate from the group Q2 headline) is due **2026-07-30**.

**CXMT pressure response.** No explicit 2026 Samsung statement price-
matching or directly responding to CXMT was found — flagged **not
found**. What did surface: a "world's first" 900-layer V-NAND
announcement (2026-05-25, medium) framed by the outlet as a competitive
answer to CXMT's IPO push, and older 2025 moves (DDR4 phase-out, LPDDR6
development explicitly "to shake off Chinese competition") that predate
this year's window.

**Latest quarter + next earnings.** Q2 2026 (guidance released
2026-07-07/08, high — direct fetch): operating profit **89.4tn won
(~$58.4B)**, +19x YoY, 3rd consecutive record; revenue **171tn won**,
slightly below the ~173tn won consensus. Stock fell **>6%** same day
(beat priced in). **Full divisional detail + conference call: 2026-07-30.**
(One widely-run headline citing "$89B" operating profit is a likely
won/dollar mix-up against the correctly-converted $58.4B figure — don't
reuse the $89B number.)

---

## 2. SK Hynix — the incumbent, defending it under the sharpest shock

**HBM share + roadmap.** 50–62% range depending on source; best-sourced
figure is Chosun's 55% (medium, snippet). First to clear Nvidia's HBM4
Vera Rubin qualification and reportedly commands **60–70% of that
volume** vs Samsung's 25–30% (medium, search-snippet level, no full
article secured — treat as directional). TrendForce (2026-01-28, thin,
RSS-title): "to supply about two-thirds of NVIDIA HBM4."

**Capacity expansion.** M15X (Cheongju) DRAM+HBM4 line begins operations
May 2026 as an interim bridge (thin). **Yongin cluster: 21.6tn won
(~$15.7B)** new tranche announced 2026-02-25, **120tn won total** across
all phases, Phase 1 targeted **May 2027** (medium). New: a **$3.87–4B
Indiana (West Lafayette) HBM packaging plant** — SK Hynix's first US
advanced-packaging fab, construction underway since late Feb 2026,
targeting operations by **end of 2028**, ~7,000 jobs, backed by **up to
$458M CHIPS direct funding + $500M in loans** plus a ~25% investment tax
credit (medium).

**AI-demand exposure.** Nvidia is the dominant customer (see above).
**High confidence** (full article, Korea Times 2026-07-26): KB Securities
analyst Kim Dong-won: sales to global tech companies and AI datacenter
operators will be **~70% of SK Hynix's total Q2 revenue**. A Google-TPU
HBM-share claim (SK Hynix "over half," via Chosun) directly conflicts with
a separate snippet crediting Samsung as primary Google TPU HBM3E supplier
— **flagged as unreconciled, do not cite either as settled**.

**Pricing posture.** High-confidence company-reported figures: **Q1 2026**
sales 52.6tn won (~$39B), operating profit **37.6tn won (+405% YoY)**, op.
margin **~72%**, 4th consecutive record quarter (theinvestor.co.kr, full
fetch). CFO Kim Woo-hyun credited "expanded investments in AI
infrastructure"; VP DRAM Marketing Park Joon-deok: "favorable pricing
conditions are expected to continue for the time being." **Q2 2026
consensus** (reports **2026-07-29**, tomorrow relative to this crawl):
operating profit **64.1tn won (~$43.7B)**, all-time high, beating the
prior full-year (FY2025) record of 47.2tn won; sales 84.1tn won; margin
75–77% (high, Korea Times + Yonhap convergent). Scattered aggregator ASP
claims (+55–130% cumulative, an unverified 8Gb-DDR4-10x claim, an
unverified ~700% spot-price claim) are **thin** and not primary-press
confirmed — directionally consistent with severe pricing power but not
individually citable.

**CXMT pressure response — the crawl's headline finding.** SK Hynix stock
fell **~14.65%** (one source: "-11.5%," a discrepancy not reconciled) in a
**2026-07-28 "Black Tuesday" Seoul selloff** — KOSPI fell **10.84%**
with a circuit breaker triggered (high, full article, Korea Times). Direct
cause per the article: **CXMT's Shanghai STAR-market debut the prior day
(2026-07-27)** triggered investor fears of intensified China memory
competition, compounding a Wall Street semiconductor selloff (Philadelphia
SOX -2.23%) and Middle East tension. Unattributed analyst quote in the
piece: "Risk aversion has resurfaced as investors refocus on concerns over
the AI investment cycle and China's growing competitiveness in the memory
and other semiconductor industries." This is the sharpest, most immediate
market-priced reaction to CXMT found across the whole trio crawl — **today
is the day the capacity race got repriced as a threat, not a distant
one.** Separately, SK Hynix is reported targeting Chinese clients with
advanced LPDDR6 to compete with CXMT domestically (thin, URL unresolved).

**Latest quarter + next earnings.** Q1 actual as above. **Q2 2026 earnings
land 2026-07-29** — one day after this crawl, directly actionable for the
expectations ledger. Market cap crossed **$1T for the first time on
2026-05-27** (medium), briefly overtook Samsung as Korea's most valuable
company in early July, broke $1T again 2026-07-26 — just before the
07-28 crash.

---

## 3. Micron — #3, the one most exposed to Nvidia's on-again-off-again favor

**HBM share + roadmap.** Historically #3. Public reporting swung twice
this year: excluded from early Vera Rubin HBM4 allocations per a wave of
Feb–Mar 2026 headlines (medium, multi-outlet corroborated but no body
text), then **reinstated alongside Samsung/SK Hynix** by June (Bloomberg
"Nvidia Clears Memory's Big Three," 2026-06-04; Jensen Huang quoted
directly confirming all three cleared — medium). Micron's own Q3 FY26
press release (2026-06-24, **high**, direct IR fetch): **"HBM4, built on
1-beta DRAM technology, is in high-volume shipments"**; HBM4E development
underway. Some outlets (EBC Financial, Seeking Alpha) still frame Micron
as "third" behind the other two (thin/medium).

**Capacity expansion.** **$200B total US manufacturing commitment**
(announced 2025-06-12 with President Trump, NIST.gov + trade press,
medium). **$100B New York (Clay) megafab** groundbreaking 2026-01-16;
second Idaho (Boise) fab accelerated; **$24B Singapore plant** announced
2026-01-27 explicitly framed as an AI-boom supply response; 1-alpha DRAM
production launched at Manassas, VA, 2026-05-22. **CHIPS Act: $6.1B
finalized 2024-12-10** for Idaho + NY (medium-high, multiple official
sources convergent) — a separate $275M CHIPS figure appeared once and
wasn't reconciled to the $6.1B total. Hiroshima, Japan not found this
pass.

**AI-demand exposure.** "Sold out" framing recurs across three
independent headlines (Yahoo Finance 02-27, TradingKey 05-27, Startup
Fortune 06-21) — **medium/thin**, not cross-verified against Micron's own
press release, which doesn't itself use "sold out" language in what was
retrieved. Segment revenue from the Q3 FY26 release (high): Cloud Memory
BU $13.77B, Core Data Center BU $11.52B, Mobile & Client BU $11.52B,
Automotive & Embedded BU $4.63B — **no separate DRAM/NAND/HBM dollar
breakout disclosed**. The "only US-based DRAM maker" framing is the
national-security hook the other two lack — tied explicitly to the $200B
Trump-era investment announcement.

**Pricing posture.** Q3 FY26 (reported 2026-06-24, **high**, direct IR
fetch): revenue **$41.456B** (vs $23.86B prior quarter, $9.30B a year
ago), GAAP gross margin **84.6%**, GAAP net income **$28.243B**, GAAP
diluted EPS **$24.67**. **Q4 FY26 guidance: revenue $50.0B ± $1.0B**,
gross margin ~86%. Broader DRAM contract-pricing context (TrendForce,
medium): Q1 2026 industry DRAM revenue +81% QoQ; Q3 2026 guidance:
server DRAM contract prices +13–18% QoQ (with wider analyst claims of
+30–40% circulating but not Micron-specific).

**CXMT pressure response.** **Not found** — no direct Micron statement or
action responding to CXMT surfaced in this crawl. Read alongside: Micron
**exited China's server/datacenter chip market entirely in 2023**
(four-outlet convergent, 2025-10-17, medium) after Beijing's "critical
information infrastructure" ban — Micron has structurally less exposure
to defend in China than Samsung or SK Hynix, which may explain the
silence rather than indicate indifference.

**Latest quarter + next earnings.** Fiscal Q3 2026 as above. Market cap:
**$1.37T** cited 2026-06-25 (medium, two convergent sources), briefly
overtaking Meta and Tesla by market cap. **Next earnings date: not
found** — only a KeyBanc investor-conference appearance (2026-08-10)
located on the IR site; fiscal Q4 (ending ~Aug 2026) would typically
report **late September 2026**, unconfirmed this crawl.

---

## 4. Trio-level facts

**The "three-year HBM deficit" claim — origin identified, high
confidence.** Traced to **SK Hynix's own Q1 2026 earnings call
(2026-04-23)** — company guidance, not an outside analyst estimate. CFO
Kim Woo-hyun and VP Park Joon-deok guided that HBM demand would outpace
supply for **at least the next three years**, tied to "expanded
investments in AI infrastructure" (high, full article,
theinvestor.co.kr). The CXMT-synthesis framing already on file ("the
three-year HBM deficit it's racing into") likely draws from a Tech Times
piece (2026-07-27) that repeats the figure but is itself 403-blocked to
direct fetch — treat SK Hynix's own Q1 call as the primary source going
forward, not the Tech Times repetition of it. A related-but-distinct
figure: SK Hynix Chairman Chey Tae-won separately said the shortage
persists **"through 2030"** (medium, two outlets); other coverage cites
"through 2028" — these are not identical to the "three-year" framing and
shouldn't be conflated with it.

**DRAM price trajectory, 2026 YTD.** No single authoritative percentage
holds up across all three crawls — this is the weakest-sourced area
industry-wide, not just for one actor. The highest-confidence numbers are
outcome-side (Samsung's confirmed Q2 sequential **DRAM +44%/NAND +53%**;
SK Hynix's ~72% and guided 75–77% operating margins), which imply severe
pricing power without themselves being a clean price-increase percentage.
Scattered thin claims across all three crawls (Q1 +55–90%, cumulative
+130%, an 8Gb-DDR4 "10x in a year" outlier, a "~700% spot" outlier) are
directionally consistent — DRAM/HBM pricing is compounding sharply
through 2026 — but none individually clears medium confidence without a
Reuters/Bloomberg/TrendForce-primary re-confirmation.

---

## 5. Today — the "Black Tuesday" repricing (2026-07-28)

The single most consequential fact this crawl surfaced landed on the crawl
date itself: **CXMT's Shanghai STAR-market listing debut (2026-07-27,
+466% to ~$489B) triggered a same-week Seoul selloff** — KOSPI **-10.84%**
with a circuit breaker, SK Hynix **-14.65%** (one source: -11.5%,
unreconciled) — explicitly attributed by Korean financial press to
investors "refocus[ing] on concerns over... China's growing
competitiveness in the memory... industries," compounding a Wall Street
semiconductor selloff and Middle East tension (high, full article, Korea
Times). This is the clearest, most immediate market verdict on the
capacity race found across all four actors this crawl covers (including
last week's separate CXMT-focused crawl): **the market is now pricing
CXMT as a near-term competitive threat to the Korean HBM duopoly, not a
multi-year-out one.** Whether this holds past one bad session, or gets
partly reversed once SK Hynix's own record Q2 print lands the next day
(07-29), is the single best next-crawl target.

---

## What to watch

- **SK Hynix Q2 2026 earnings, 2026-07-29** — record operating profit
  guided at $43.7B; watch whether the print itself steadies the stock
  after the 07-28 crash, or whether China-competition fear dominates the
  reaction regardless of the number.
- **Samsung's full Q2 divisional breakdown + call, 2026-07-30** — first
  chance to see actual memory-division HBM revenue/margin split, and
  management commentary on the Vivo/Oppo price-hike rejection.
- **Samsung's Nvidia HBM4 volume order** — still unconfirmed as of
  2026-07-17 (paid-evaluation stage); the single clearest "who's really
  ahead" tell for 2027 share.
- **Micron's next earnings date** — unconfirmed this crawl; fiscal Q4
  (Aug close) likely reports late September — needs a direct-fetch
  follow-up on investors.micron.com closer to the date.
- **The DRAM price-increase percentage** — genuinely unsettled across all
  three crawls; worth one more targeted TrendForce/Bloomberg primary-source
  pass rather than trusting any of the aggregator figures collected here.
- **Whether "Black Tuesday" (07-28) is a one-day panic or a repricing that
  holds** — the temperature check for how seriously markets now treat
  CXMT as competition to Samsung/SK Hynix, not just to each other.
