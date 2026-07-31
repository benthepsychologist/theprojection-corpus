# Google/Alphabet capex — where the $195-205B is actually landing

*Crawl date: 2026-07-27. Backward crawl answering: what is Alphabet's
guided 2026 capex ($195-205B, "significantly more" flagged for 2027)
physically buying — sites, silicon, power, and the payoff case management
is making for it. Bundle: `artifacts/bundles/google-capex-2026-07-27/`.*

Method note: WebSearch was treated as exhausted (session-shared budget);
all research ran via WebFetch against Google News RSS search feeds, direct
outlet fetches, and primary sources (Google/Alphabet blogs, IR, company
press). Google News redirect links frequently would not resolve to article
body text — where that happened, the citation is the RSS feed item itself
(outlet, title, date confirmed from feed metadata) rather than a verified
article body, and is marked **medium** confidence rather than **high**.
Nothing below is fabricated; gaps are marked **(thin)** or **not found**
rather than guessed.

---

## 1. Sites — the physical buildout

Google's 2026 site activity reads as a **broad, simultaneous multi-region
land grab** rather than a small number of flagship megasites — at least
15 named US states plus a handful of international anchors, each carrying
individually large ($1B-$15B) commitments.

**United States, largest-confirmed campuses:**

- **Texas Panhandle (Gray County)** — Google + Intersect Power launched a
  "1-GW-plus" co-located data center *and power generation* complex,
  2026-06-04, corroborated by 3 outlets. (high)
- **Missouri (New Florence, Montgomery County)** — **$15B**, called the
  "largest single investment in state history," 2026-05-20, corroborated
  by 9+ outlets including a Google blog post. (high)
- **Michigan ("Project Cannoli," Van Buren Township, near Detroit)** —
  **1GW** campus confirmed 2026-03-18; DTE utility deal followed
  2026-03-24; substation cleared planning 2026-05-14; wetlands-impact
  pushback reported 2026-06-17. (high)
- **Alabama (Jackson County)** — additional **$1.5B** to expand the
  existing TVA-powered campus, 2026-06-15, corroborated by 5+ outlets.
  (high)
- **Virginia** — Botetourt County campus (2026-04-03) plus a separately
  reported **$9B "trio" of Chesterfield County campuses** (2026-06-22).
  (medium)
- **Georgia** — second Georgia data center, LaGrange, 2026-04-21/22,
  3 outlets. (medium-high)
- **Oklahoma** — utility OG&E confirmed it will power **three new** Google
  data centers in-state, 2026-04-30. (medium)
- **Wyoming** — Google named as the "mystery owner" behind what local
  reporting calls the state's largest data center project (2026-07-08);
  a separate report has Crusoe *exiting* a 1.8GW Wyoming project "after
  Google pressure" (2026-06-11), implying Google absorbed adjacent
  capacity. No single Google-specific GW figure confirmed. (medium)
- **West Virginia (Putnam County)** — governor-announced commitment to
  build a campus, 2026-03-27. (medium)
- **Minnesota (Hermantown)** — contentious campus; Form Energy 100-hour
  battery contracted to power it; a governance vote was tabled
  2026-05-05. (medium)
- **North Carolina (Lenoir)** — $1B, two-year investment, 2026-03-13.
  (thin — single outlet)
- **Iowa (eastern Iowa)** — a Google DC plan reported to have "created a
  rift between local governments," 2026-04-23; no site name, capacity, or
  dollar figure recovered. (thin)
- **Arkansas (West Memphis)** — single-outlet report that the associated
  bond issue "could reach **$60 billion**" — an outsized, uncorroborated
  number. **(thin — flagging explicitly, do not repeat as fact without
  a second source.)**

**Cross-cutting US infrastructure moves:**

- **Intersect Power acquisition** — Google to acquire the data-center-
  and-energy developer for **$4.75B**, gaining "several gigawatts" of
  energy assets (2025-12-22/2026-01-05) — this is the deal that produced
  the Texas Panhandle complex above. (high)
- **NextEra Energy partnership** — Google + NextEra to develop **"at
  least three gigawatt-scale data center campuses"** (2025-12-08/09),
  6+ convergent outlets including Reuters and NextEra's own release.
  (high)
- **Gas-fired power, a notable reversal** — Google confirmed tapping a
  gas plant to power an AI datacenter, reported as "a sharp turn from
  climate goals" (The Guardian, 2026-04-02), part of a broader hyperscaler
  shift toward gas alongside the clean-PPA buildout (TechCrunch,
  2026-04-03). (medium)
- **xAI capacity purchase (demand-side, not Google-built)** — Google
  reportedly paying SpaceX **$920M/month** for compute capacity at xAI
  datacenters (CNBC, 2026-06-05) — worth flagging as off-balance-sheet
  capacity Google is renting rather than building. (medium)

**International anchors:**

- **India (Visakhapatnam, Andhra Pradesh)** — **$15B** "AI Hub," announced
  2025-10-14, groundbreaking 2026-04-28, described as "gigawatt-scale";
  one outlet (ETEnterpriseai) puts capacity at **5GW** specifically and
  says it would "nearly double India's total data centre capacity."
  Adani Group reported as a potential **$5B** co-investor. ($15B framing:
  high, 5+ outlets over 6 months. 5GW figure: medium, single outlet.)
- **Sweden (Horndal)** — new data center groundbreaking, 2026-06-02,
  confirmed same-day by Google's own blog and HPCwire. (high)
- **Germany** — **€5.5B** AI hub / data-center expansion, reported
  2025-11-11/12 by 3 outlets. (medium-high)
- **Austria** — first Google data center "in the Alps," per Google's own
  blog, 2026-04-23; no capacity figure recovered. (medium)

**Not found:** no source ties a single aggregate global GW figure to the
new $195-205B guidance specifically — all sourcing above is campus-by-
campus, and no outlet in this crawl summed it.

---

## 2. Silicon — TPU v7 "Ironwood" vs. Nvidia

- **TPU v7 "Ironwood" is Google's current-generation chip**, rolled out
  2025-11-06, explicitly positioned against Nvidia's GB300/Blackwell —
  4 independent outlets (CNBC, Tom's Hardware, ServeTheHome, The
  Register) converge on the launch date and the competitive framing.
  (high)
  - Supply chain: co-designed with **Broadcom**, with **MediaTek** and
    **TSMC** as fab/design partners (2025-12-01, 2 outlets). (medium)
  - SemiAnalysis (a credible technical-analysis outlet) called it "The
    900lb Gorilla In the Room" for Nvidia, 2025-11-28. (medium — single
    outlet, body not independently verified)
- **Next-gen split announced April 2026**: "TPU 8i" (inference) and
  "TPU 8t" (training), per ServeTheHome, 2026-04-22. A lower-tier
  aggregator (tech-insider.org) attached a **"121 exaflops, $21B Nvidia
  challenge"** headline figure on 2026-04-23 — **this $21B figure is
  single-sourced from a non-primary outlet and should be treated as
  unverified**, not repeated as fact. (naming: medium; $21B figure: thin)
- **The TPU-vs-Nvidia dollar/unit split Ben asked about: not found.**
  Alphabet does not appear to disclose this breakdown publicly anywhere
  surfaced in this crawl. Two proxy signals stand in for it:
  - Broadcom **and** Nvidia shares both rose on Google's capex guidance
    raises (CNBC 2026-02-04, Barron's 2026-02-05) — the market reads
    Google's capex increases as feeding *both* the TPU supply chain and
    continued Nvidia purchases, i.e. this is not simple TPU-for-Nvidia
    substitution. (medium)
  - Apple confirmed extending its Private Cloud Compute workload to
    **Google Cloud running Nvidia Blackwell GPUs** (MLQ.ai, 2026-06-10) —
    direct evidence Google Cloud runs Nvidia silicon for at least some
    external customer workloads alongside its own TPU fleet. (medium)
- **External TPU capacity commitments (customers), the clearest volume
  signal available:**
  - **Anthropic, original deal** (2025-10-23/24) — access to **up to
    1 million TPUs**, "over 1GW of processing power" expected in 2026,
    deal reported worth "tens of billions of dollars." Large convergent
    cluster (CNBC, DCD, Tom's Hardware, PR Newswire + others). (high)
  - **Anthropic, expanded deal** (2026-04-06/07) — "multiple gigawatts of
    next-generation compute," a three-way Google+Broadcom+Anthropic
    structure, confirmed via Anthropic's own release plus 6+ outlets
    (CNBC, TechCrunch, PR Newswire). (high)
    - A single-outlet, "eyeing"-framed follow-on claims Anthropic may be
      discussing a **$200B** Google Cloud + chips deal (WinBuzzer,
      2026-05-06). **(thin, speculative, unconfirmed.)**
  - **Meta** reportedly weighing Google TPU deployment starting **2027**
    (TrendForce/Moomoo/TradingNEWS, 2025-11-24 to 11-30) — 3 outlets
    converge but all appear to trace back to one original unconfirmed
    report, not independent confirmation. (medium)
  - **Blackstone** — reported **$5B** TPU cloud venture with **500MW**
    of AI capacity (EdgeIR, 2026-05-25). (thin, single outlet)
- Reuters confirms the framing directly: "Google increases capex forecast
  again after cloud-driven quarterly beat" (2026-07-22). (high)

---

## 3. Power — what's actually signed

The power buildout is dominated by **solar PPAs at gigawatt scale**, with
nuclear/SMR and geothermal as smaller but strategically flagged bets, and
an emerging (and reputationally awkward) turn toward gas.

**Nuclear / SMR:**

- **Kairos Power** — framework for **up to 500MW** of SMR capacity by
  2035 (2024-10-15). (medium)
- **TVA + Google + Kairos** — the **first US utility PPA for Gen-IV
  nuclear**, Tennessee reactor targeted for **2030**; Data Center
  Dynamics puts the specific figure at **50MW**, sited across
  Tennessee/Alabama (2025-08-18), corroborated by 5 outlets including
  Reuters. (high on the deal/date; the 50MW figure rests on one outlet)
- **NextEra + Google** — deal to restart the **Duane Arnold** nuclear
  plant (2025-10-28); no capacity figure recovered. (thin)
- Counter-framing worth carrying alongside these: **"Data centers
  powered by next-gen nuclear? Don't fall for Big Tech's PR hype"**
  (Bulletin of the Atomic Scientists, 2026-07-20) — argues SMR timelines
  (2030+) lag current AI power demand by years. (medium)

**Solar (the largest-volume category):**

- **TotalEnergies** — **1GW** solar, Texas, 15-year PPA, ~28TWh total
  delivery; TotalEnergies' largest-ever US renewable PPA; construction
  starts Q2 2026. Directly fetched from ESGtoday, corroborated by 6+
  additional outlets. (high)
- **Clearway Energy** — **1.17GW** of PPAs across Missouri/Texas/West
  Virginia (2026-01-15/19, 2 outlets). (medium)
- **Enlight Renewable Energy** — **200MW AC**, Oklahoma, 15-year PPA
  (2026-05-26/27, 3 outlets). (medium-high)
- **Linea Energy** — 500MW solar, Texas, 15-year PPA (2026-05-14, 1
  outlet). (thin)
- 400MW Texas solar portfolio, multiple PPAs (2026-03-24, 1 outlet).
  (thin)
- **TotalEnergies** — Malaysia, 21-year PPA, ~1TWh/year (2025-12-16/18,
  4 outlets incl. TotalEnergies' own release). (high)
- Treaty Oak — 100MW solar, Grant County, Arkansas (2025-11-13, 2
  outlets). (medium)
- TotalEnergies — Ohio, 15-year PPA (2025-11-12, 1 outlet). (thin)
- **EnBW** — 100MW PPA, Germany's largest offshore wind project
  (2026-02-04/05, 2 independent sources: outlet + counterparty release).
  (medium)

**Geothermal:**

- **Ormat Technologies** — **up to 150MW** geothermal, Nevada, via NV
  Energy's Clean Transition Tariff; commercial ops 2028-2030, 15-year
  term post-COD. Directly fetched from ESGtoday (2026-02-18). (high)
  - Earlier, separate 115MW Nevada geothermal deal (2024-06-14) shows
    the Nevada geothermal build is cumulative. (thin, context only)
  - **No Fervo Energy deal found** in this crawl — Ormat, not Fervo, is
    the recurring Google geothermal counterparty. Don't assume a Fervo
    relationship without a fresh check.

---

## 4. Payoff claim — what management says this buys, vs. what's verifiable

**The claim, as reported around the 2026-07-22 Q2 print:**

- **Google Cloud backlog: $514B.** Corroborated by 4 outlets (Bloomberg,
  PYMNTS, Startup Fortune, Bitget), but **no primary Alphabet document
  was reachable this crawl** to verify against the original release —
  Alphabet's investor site returned only nav scaffolding, and guessed
  release-document URLs 404'd. Treat as high-confidence *headline*,
  unverified against the primary filing. (high/caveat)
- **Google Cloud revenue +82% YoY** — same 4-outlet cluster, same
  primary-source caveat. (high/caveat)
- **Gemini app: 950M monthly active users**, attributed directly to
  Sundar Pichai in reporting; "AI Mode" separately reported past 1B
  (unclear whether users or queries from feed metadata alone). 2 outlets
  (Eastern Mirror, Digital Information World), one explicitly sourcing
  the Pichai attribution. (medium-high)
- Google Cloud growth has been explicitly described as **"capacity-
  constrained"** in the prior quarter (TechCrunch, 2026-04-29, re:
  Q1 2026's $20B+ Cloud revenue) — i.e., management's own framing is that
  more capex is needed to *unblock* growth already in the pipeline, not
  just to chase speculative demand.
- **No direct, attributable Pichai/CFO quote on capex-to-revenue ROI
  linkage was recovered** in this crawl — earnings-call transcript
  sources (Fool.com, Investing.com, CNBC live-blog, MarketWatch, Reuters)
  either 404'd, wouldn't resolve, or blocked the fetch. **Flag for
  whoever picks this up next: this crawl could not confirm Alphabet's
  current CFO by name via a primary source** (the widely-known-as-of-2024
  name, Ruth Porat, moved to President/Chief Investment Officer that
  year; a successor name surfaced only from general background, not a
  fetched source here — verify before publishing anything CFO-attributed).

**The market's read — why GOOGL fell despite the beat:**

- Stock fell **~5%**, reporting ties the drop specifically to the
  **$205B** capex figure (MLQ.ai, 2026-07-23). (medium)
- **Negative free cash flow** specifically named as the more precise
  mechanism overshadowing the Cloud beat (TradingView, 2026-07-23) — a
  distinct, sharper claim than "capex spooked investors" generally.
  (medium)
- **Cantor Fitzgerald cut its price target to $420**, explicitly citing
  capex (Investing.com, 2026-07-23). (medium)
- Framed directly as an ROI-skepticism story: **"Alphabet Shares in
  Correction Territory as Investors Question Returns on AI Build-Out"**
  (24/7 Wall St., 2026-07-23). (medium)
- The pattern — beat on revenue/Cloud, but capex guidance (and per one
  outlet, negative FCF specifically) drove the drop — is corroborated
  **qualitatively** across 8-10 independent outlet headlines dated
  2026-07-22/23, including non-US coverage (아시아경제/Korea). Individual
  percentages and quotes inside that pattern are mostly single-sourced;
  the pattern itself is high-confidence. (high on pattern / medium-thin
  on individual figures)
- **Methodology flag:** the CNBC live-blog URL used as a "known-good"
  source in the 2026-07-23 thread entry
  (`cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html`)
  returned **403 Forbidden** on refetch this session — it may no longer
  be reliably fetchable via WebFetch; other threads citing it should be
  aware.

**What's still unverified:** independent third-party estimates of
Google's *AI-specific* revenue (as distinct from total Cloud revenue) —
not found anywhere in this crawl. The payoff case currently rests
entirely on Alphabet's own reported figures (backlog, Cloud growth, MAU),
relayed through press coverage that itself couldn't be traced back to the
primary filing this session.

---

## What to watch

- **Q3 2026 earnings** (next scheduled print) — does capex guidance climb
  again past $205B, and does Cloud growth/backlog keep pace, or does the
  "capacity-constrained" framing start resolving into realized revenue?
- **The TPU-vs-Nvidia split staying undisclosed** — if Alphabet ever
  breaks this out explicitly (e.g. in a 10-K/10-Q or analyst day), it
  would be the single most load-bearing missing number in this whole
  picture.
- **Nuclear/SMR timelines vs. near-term power need** — Kairos/TVA
  Tennessee reactor is a 2030 target against capacity being built now;
  the Bulletin of Atomic Scientists' "PR hype" framing (2026-07-20) is
  worth re-checking against actual construction milestones.
- **Gas-fired buildout** — whether the Guardian's "sharp turn from
  climate goals" (2026-04-02) is an isolated site or the start of a
  broader pattern across the newly announced US campuses.
- **A primary-source confirmation pass** — this crawl could not reach
  Alphabet's actual Q2 2026 earnings release or call transcript directly;
  a follow-up crawl fetching the primary filing would upgrade several
  "high/caveat" items above to fully verified.
