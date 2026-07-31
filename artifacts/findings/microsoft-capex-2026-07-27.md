# Finding — Microsoft capex: where does the ~$97B/yr go?

**Thread:** microsoft-capex · **Crawled:** 2026-07-27 · **Bundle:** `artifacts/bundles/microsoft-capex-2026-07-27/provenance.yaml`

Ben's prompt: "I still don't have even a blurry picture of what Microsoft is
DOING with all that CapEx." This crawl pulls the destination apart into
four questions — sites, silicon, power, payoff — using Google News RSS +
direct WebFetch of Microsoft's own blog/IR pages (WebSearch tool not used;
session budget risk per crawl skill preflight). Every claim below is dated
and sourced; thin/unverified items are marked explicitly rather than
smoothed over.

**Housekeeping note up front:** the literal "**$97B/yr TTM**" figure named
in the brief was **not found verbatim** in any source this crawl reached.
Microsoft's own IR page gives nine-month FY26 capex as **$80.1B** (through
2026-03-31) plus a Q3 quarterly figure of **$30.9B**. A TTM number near
$97B is arithmetically plausible if you add an estimated Q4 FY25 quarter,
but that arithmetic is this crawl's own derivation, not a disclosed or
press-stated number — treat "$97B" as **an estimate pending the 2026-07-29
earnings call**, which will report the real FY26 Q4 and full-year figures.

---

## 1. SITES — the named build-out

- **Wisconsin — Fairwater #1 (Mount Pleasant, Racine County):** first
  facility's construction **completed 2026-06-23**; ~550 FTE now, ~800
  once the second facility is operational; equipment startup began
  April 2026; second facility slated for **2028**. 315-acre site.
  ([Microsoft Source, 2026-06-23](https://news.microsoft.com/source/2026/06/23/microsoft-completes-construction-on-first-datacenter-facility-in-mount-pleasant-wisconsin/))
  — investment figure is inconsistent across headlines over time
  ($1B→$3.3B→$7.3B→$7.7B at different announcement dates back to 2023);
  most recent large figure is **$7.3B** (Data Center Dynamics/Tom's
  Hardware, 2025-09-18, RSS-listed, body unverified — **thin** on the
  exact current total).
- **Georgia — Fairwater #2 (Atlanta/Fayetteville):** unveiled
  **2025-11-12**, explicitly wired to the Wisconsin site via a dedicated
  "AI WAN" — 120,000+ miles of new fiber — forming what Microsoft calls
  its first **"AI superfactory."**
  ([Microsoft "Infinite Scale" blog, 2025-11-12](https://blogs.microsoft.com/blog/2025/11/12/infinite-scale-the-architecture-behind-the-azure-ai-superfactory/))
  No dollar or MW figure given in that post; a Fayetteville, GA campus
  opening was reported 2025-11-21 (AJC.com, **thin** — RSS headline only).
  Earlier, separate GA sites (Rome ~$1B, near-Atlanta $1.8B, Tyrone) are
  **thin** and not confirmed as the same superfactory footprint.
- **Combined WI+GA capacity:** reported as **"over 2 GW"** for the linked
  superfactory. ([NextBigFuture, 2025-11-16](https://www.nextbigfuture.com/2025/11/microsoft-has-largest-multi-site-ai-data-center-at-2-gigawatts.html))
  — **medium** confidence, single secondary source, though consistent
  with a Data Center Dynamics headline making the same claim.
- **Texas — Pecos, Reeves County (new for 2026):** announced
  **2026-06-22**, **~2GW** capacity, co-located natural-gas power plant,
  5–7 year build-out, 6,000+ peak construction jobs; separately, 4.7GW of
  contracted renewable electricity cited for Microsoft's Texas operations
  overall.
  ([Microsoft blog, 2026-06-22](https://blogs.microsoft.com/blog/2026/06/22/powering-the-next-wave-of-ai-expanding-capacity-with-our-new-datacenter-in-pecos/))
  This is the site tied to the Chevron "Project Kilby" power deal (see
  §3). **This is a second, distinct 2GW figure from the WI+GA
  superfactory — the two should not be summed as if reported the same
  way; no single company-wide total-GW figure was found anywhere.**
- **International (all thin — RSS headline/title only, bodies blocked
  by bot-detection on most outlets):** Portugal €8.6B hub (2025-11-12);
  Australia "record $25B" (2026-04-23, AFR — fetch blocked); UAE 200MW
  expansion with G42 by 2026; West Virginia 1.35GW with
  Nscale/Nvidia/Caterpillar (2026-03); a "$50B by 2030" Global South
  pledge (2026-02). None independently verified past headline level this
  pass — worth a dedicated follow-up crawl with retries against
  DCD/AJC.com (both 403'd, likely bot-blocking rather than absence of a
  story).

## 2. SILICON — Maia vs. Nvidia, and the OpenAI/MAI split

- **Maia 200 launched 2026-01-26:** TSMC 3nm, 140B transistors, ~10
  petaFLOPS FP4 / 5 petaFLOPS FP8, claimed 30% better perf/$ than the
  prior fleet; deployed first in Des Moines, Iowa (Phoenix, AZ next).
  Microsoft's own post is explicit that Maia 200 is **dual-purpose**: it
  serves **OpenAI's GPT-5.2 inference** *and* is used internally for
  "synthetic data generation and reinforcement learning to improve
  next-generation in-house models" — the clearest documented statement
  that the same silicon serves both workloads, though **no percentage
  split is given anywhere in the post**.
  ([Microsoft blog, 2026-01-26](https://blogs.microsoft.com/blog/2026/01/26/maia-200/))
- **Maia timeline:** first-gen Maia 100 unveiled 2023-11-15 (medium);
  next-gen Maia chip production reported **delayed ~6 months** with
  scaled-back ambitions (2025-06-27/30, Tom's Hardware/DCD/The
  Information, medium); **Intel Foundry** picked to build Maia 2 on
  18A/18A-P (2025-10-17/19, medium); **SK Hynix** named exclusive HBM3E
  supplier for Maia 200 (2026-01-27/28, medium); DCD claims Maia 200
  "already in production" (2026-06-03, medium, body blocked). **No
  production volume/unit-count figure was found anywhere**, including in
  Microsoft's own announcement.
- **Nvidia side:** Nscale signed a **$14B Nvidia GPU supply deal** tied
  to Microsoft (a neocloud arrangement, not a direct Microsoft-Nvidia PO)
  on 2025-10-16 (medium). A 2024-12-18 headline claims Microsoft bought
  "twice as many Nvidia Hopper GPUs as other big tech" but no exact
  unit/dollar figure was recoverable (thin, fetch blocked). Microsoft was
  also added as a buyer of **AMD's Helios rack system** — a third
  silicon vendor alongside Nvidia and in-house Maia — reported
  2026-07-20 (CNBC, medium).
- **No numeric compute split is disclosed anywhere** between (a) OpenAI's
  workloads under the $250B Azure commitment, (b) Microsoft's own MAI
  in-house model training/serving, and (c) third-party/enterprise Azure
  AI customers. This is the single biggest gap in the public record —
  flagged explicitly, not filled with an estimate.
- Cross-ref: Anthropic reportedly in talks to use Microsoft's Maia chips
  for Claude compute (2026-05-21/24, medium — see thread
  `microsoft-mai-openai-decoupling`).

## 3. POWER — PPAs, nuclear, and the GW gap

- **Three Mile Island / Crane Clean Energy Center:** original 20-year PPA
  with Constellation signed Sept 2024, restarting TMI Unit 1 (renamed
  Crane), 835MW. DOE approved a **$1B loan** to Constellation for the
  restart, 2025-11-18/19 (high — CBS News, WSJ, E&E News/Politico all
  converge). PennLive reported operators **affirming a 2027 restart
  date**, 2026-03-27 (medium). E&E News reported the **NRC issued a draft
  finding of no significant environmental impact**, restart "closing in"
  on NRC approval, 2026-06-09 (medium). FERC approved transfer of
  **760MW of capacity interconnection rights** to enable the grid
  connection, 2026-06-16 (medium).
- **Chevron "Project Kilby" (Pecos, TX):** **2.67–2.7GW** off-grid
  natural-gas plant, **20-year PPA**, **$7B** project cost, first power
  targeted **2028** — this is the power deal underpinning the Pecos
  datacenter site in §1. Reported 2026-06-22/23 across 5 converging
  outlets (CNBC, Rigzone, WSJ, Redmondmag, Business Journals) — **high**
  confidence.
- **Other nuclear:** Helion (fusion) — Microsoft's 2023 PPA commitment
  (50MW by 2028) referenced again when Helion raised $465M, 2026-06-08
  (medium). Microsoft partnered with Aalo Atomics on AI tools for nuclear
  permitting, 2025-11-18 (high on the fact, but it's a permitting-speed
  partnership, not a power deal). Oklo/X-Energy joined a **$200M
  DOE-coordinated advanced-reactor initiative** with Microsoft and Nvidia
  named as tech partners, 2026-07-24 — this is a federal multi-company
  program, not a Microsoft-specific PPA or MW commitment (**thin** as a
  Microsoft-specific data point).
- **Total secured vs. needed:** the most-repeated aggregate figure is
  **~40GW of contracted renewable capacity worldwide, ~19GW already
  online** (esg-investing.com, loosely corroborated by a Reuters piece on
  Microsoft's ongoing renewable buying, 2026-02-18) — **medium**,
  secondary-aggregator sourced, not a Microsoft primary filing. A
  competing **34GW** figure exists in one source (ainvest.com, thin,
  unreconciled). **No GW-needed-vs-secured gap figure was found anywhere**
  — Microsoft does not appear to publish one, and no outlet has
  reconstructed it independently.

## 4. PAYOFF CLAIM — the $37B run-rate, Azure growth, and the OpenAI mapping

- **$37B AI run-rate:** Microsoft's FY26 Q3 earnings (**reported
  2026-04-29**, quarter ended 2026-03-31) stated the AI business run-rate
  **crossed $37B annualized, up 123% YoY** — Microsoft's own metric,
  corroborated by multiple financial outlets repeating it through
  June–July 2026 (high).
- **Azure growth same quarter:** **+40% YoY** (39% constant currency);
  total company revenue **$82.9B** (+18%); Microsoft Cloud revenue
  **$54.5B** (+29%) — pulled directly from Microsoft's IR press-release
  page (high).
- **Capex same quarter:** **$30.9B** quarterly; **$80.1B** nine-month
  FY26 (through 2026-03-31) — Microsoft IR, high. A CNBC headline reports
  Microsoft guiding to **~$190B in calendar-2026 capital spending**
  (medium — headline only, article body blocked).
- **The $250B OpenAI commitment:** Microsoft's own blog (2025-10-28)
  confirms OpenAI "has contracted to purchase an **incremental $250B of
  Azure services**," alongside Microsoft's **~27% as-converted stake**
  (~$135B) and Microsoft giving up its right of first refusal as OpenAI's
  compute provider. **No timeframe is stated for the $250B**, and no
  source found in this crawl quantifies what share of Microsoft's capex
  maps to fulfilling it versus Copilot/enterprise Azure AI/in-house MAI
  workloads — this split is simply not public (high confidence on the
  deal terms; thin/not-disclosed on the capex mapping).
- **Circular-financing skepticism** is an active, ongoing press theme
  (WSJ 2025-10-22, Bloomberg 2025-11-24, Seeking Alpha 2025-09-29, Times
  of India 2025-11-23) tying Big Tech capex — Microsoft/Nvidia/OpenAI's
  web of deals — to a self-reinforcing revenue loop and bubble concern.
  Coverage found is general Big-Tech framing, not a Microsoft-specific
  dollar reconciliation (medium).
- **Earnings date confirmed:** Microsoft reports **FY26 Q4 / full-year
  results Wednesday 2026-07-29** — cross-confirmed by 6+ independent
  preview outlets this week (GeekWire, Zacks, tastylive, Money Morning,
  Motley Fool). Already logged in `attention/upcoming.yaml` as
  `microsoft-q2-earnings` (due 2026-07-29, status pending) — not
  duplicated here.

### What to verify at the 2026-07-29 call
- The actual **capex TTM number** — does Microsoft state a $97B-shaped
  figure, or is the real headline the **FY27 forward guidance** (previews
  point to $190–220B for calendar/fiscal 2026, nothing yet for FY27)?
- Updated **AI run-rate** past $37B and its new YoY growth rate.
- **Azure growth%** for Q4 — was 40% in Q3; sustaining vs. decelerating
  is the central investor question per this week's previews.
- Any **explicit disclosure** (unlikely, but worth checking) of how much
  capex or Azure capacity maps to OpenAI's $250B commitment vs.
  Microsoft's own workloads.
- Whether management addresses the circular-financing/bubble narrative
  directly.

---

## Open gaps (explicit, not smoothed over)
- No single company-wide total-GW figure for Microsoft's global
  build-out — only project-level figures (2GW WI+GA superfactory, 2GW
  Pecos TX) that should not be summed without more confirmation.
- No Maia production volume/unit-count figure anywhere, including from
  Microsoft itself.
- No numeric split of Azure AI compute between OpenAI serving / MAI
  in-house / third-party customers — the central question behind "what
  is the $97B actually buying" remains **unanswered by public
  disclosure**, only qualitatively addressed (Maia 200 explicitly
  dual-purpose).
- No GW-needed-vs-secured power gap figure published by Microsoft or
  reconstructed by any outlet found.
- The "$97B/yr TTM" figure itself is this crawl's derivation from
  Microsoft's own $80.1B nine-month FY26 number, not a disclosed or
  press-stated figure — pending confirmation/correction at the 07-29
  call.
