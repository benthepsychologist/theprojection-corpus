---
thread: datacenter-power-grid
title: "Grid & Turbines"
lens: ai
entities: [spacex]
opened: 2026-07-24
crawled: 2026-07-24
---

# Grid & Turbines — timeline

*Watch:* The grid is the binding constraint on the buildout (not chips) —
interconnection queues exploding, hyperscalers "bringing their own power"
via behind-the-meter gas at gigawatt scale, a hard equipment ceiling
(turbines sold out to 2030, transformers ~3yr), and the ratepayer +
environmental-justice fights that improvisation generates.

## 2026-08-26 — Camellia's PSC clearance comes with a 1,000MW demand-response commitment

- **Georgia Power announced its 3.2 GW Camellia/OpenAI contract cleared PSC regulatory review at 9:00pm ET on 08-26**, attaching the specific grid-mechanism terms this thread tracks: OpenAI funds all of its own infrastructure, commits up to **1,000MW of flexible demand response** (Georgia Power can curtail the load at peak), and the deal is bundled into a "large-load" portfolio Georgia Power says nets ratepayers ~$950M/year in system savings starting 2029. ⚠️ Whether PSC staff affirmatively approved versus simply let their 08-25 objection-signalled deadline lapse is not independently confirmed in secondary coverage — full resolution-mechanism detail on `camellia`. If accurate, the demand-response commitment is a concrete instance of the "bring your own generation / shed load at peak" bargain this thread has been tracking in the abstract.
  ([Georgia Power, via PR Newswire — primary](http://www.prnewswire.com/news-releases/georgia-powers-contract-with-openai-approved-latest-approval-part-of-portfolio-of-large-load-contracts-delivering-approximately-950-million-in-annual-savings-beginning-in-2029-302861080.html),
  [WTOC](https://www.wtoc.com/2026/08/27/georgia-powers-openai-contract-effingham-county-approved-expected-lower-residential-bills/))
  ⟨daily 2026-08-26⟩

## 2026-08-26 — Amazon withdraws a groundwater bid after Virginia says no

- **Amazon Data Services withdrew its Virginia DEQ application to draw up
  to 6.4 million gallons a year from the Potomac aquifer for the proposed
  Birchwood Tech Campus in King George County**, after a DEQ report warned
  the aquifer could not absorb major new withdrawals and a state senator
  called the request "indefensible." Water is now doing what
  interconnection queues have been doing — a hard physical constraint a
  siting decision has to route around rather than negotiate.
  ([Virginia Mercury](https://virginiamercury.com/2026/08/26/amazon-changes-course-on-water-use-for-king-george-data-center-campus/))
  ⟨daily 2026-08-26⟩

## 2026-08-25 — US gas buildout outpaces China's, on AI load

- **A Global Energy Monitor analysis found the US now building roughly
  twice as much gas-fired capacity as China, with AI data-center demand
  the stated driver.** US gas capacity under development rose 50% since
  January, from 252GW to 378GW, after a 76% jump in projects under
  construction in the first half of 2026.
  ([Global Energy Monitor, via The Guardian](https://www.chinastrategy.org/2026/08/25/us-building-twice-as-much-gas-fired-capacity-as-china-in-ai-boom-analysis-finds/))
  ⟨daily 2026-08-25⟩

## 2026-08-24 — The buildout's demand reaches the electrical supply chain: two power-component acquisitions in one day

- **nVent Electric agreed to buy Maverick Power for $1.75bn, plus up to $550m of earnout tied to 2027-2028 performance.** Maverick (McKinney, Texas; ~900 employees; ~$700m of 2026 revenue) makes electrical power-distribution equipment specifically for data centres. The deal is expected to close in Q4 2026, funded with cash and new debt on a Bank of America bridge. **This is the buildout's demand showing up in the electrical supply chain rather than in chips or in grid capacity** — vendor consolidation one layer below the constraint this thread tracks.
  ([nVent, via GlobeNewswire](https://www.globenewswire.com/news-release/2026/08/24/3349571/0/en/nvent-to-acquire-maverick-power.html)) ⟨daily 2026-08-24⟩
  <!-- Corporate press release, which this map normally trims. Kept because
       the dollar figure and the direct data-centre tie make it a real
       capex datapoint rather than newswire churn. -->
- **Infineon is acquiring C2i Semiconductors, a Bangalore maker of power-management chips for AI data centres**, on undisclosed terms, expected to close in Q3 2026. Smaller and less consequential than the nVent deal; recorded because it is the same lane on the same day — multiphase controllers and smart power stages, the component level of the same power problem.
  ([Infineon](https://www.infineon.com/press-release/2026/infpr202608-129)) ⟨daily 2026-08-24⟩

## 2026-08-10 — OpenAI and Meta commit to Abbott's Texas rules; a scale check on the gas buildout

- **OpenAI and Meta both formally committed to Gov. Greg Abbott's new
  data-center standards.** OpenAI's letter (compute CTO Uday
  Ruddarraju) pledged to pay for its own grid infrastructure, support
  new Texas electricity generation and minimize water use; Meta made a
  parallel commitment. Direct response to Abbott's still-open
  PUCT/ERCOT audit-and-moratorium order (this thread's 08-03 entry) and
  five days after Trump publicly called the pause "a mistake" (08-07
  entry below).
  ([OpenAI](https://openai.com/index/responsible-ai-infrastructure-texas/), [Houston Public Media](https://www.houstonpublicmedia.org/articles/news/energy-environment/2026/08/10/559042/texas-data-centers-trump-abbott-meta-openai/)) ⟨daily 2026-08-10⟩
- **An AFP analysis put a number on the behind-the-meter gas buildout
  this thread has tracked qualitatively since it opened: research firm
  Cleanview counts ~60 planned US data centers totalling 97GW of
  off-grid generation into the early 2030s — roughly Mexico's entire
  installed capacity — with OpenAI and Anthropic alone leasing 10+GW of
  it.** Even conservative assumptions put resulting emissions above
  200M tons of CO2/year (46M+ gasoline cars' worth); new US
  fossil-capacity announcements in H1 2026 alone exceeded any full year
  in the past decade. Cross-refs `ai-power-buildout`, `meta-gas-pivot`.
  ([France24/AFP](https://www.france24.com/en/live-news/20260811-ai-s-hunger-for-power-sparks-us-private-gas-plant-boom)) ⟨daily 2026-08-10⟩

## 2026-08-07 (late catch, added 2026-08-11) — Amazon is behind the single largest instance in the buildout's own aggregate dataset

- **Amazon has confirmed plans to buy power from Pacifico Energy's "GW
  Ranch" gas plant on an ~8,000-acre site it acquired in Pecos County,
  Texas — permitted for up to 7.65GW (35 turbines, 5GW nominal delivered
  output) and up to 33 million tons of CO2/year, which the New York
  Times reports could make it the single largest climate-pollution
  source in the country if built out to its full permit.** Cleanview's
  own satellite-imagery-and-permit tracing broke this 2026-08-07, NYT
  corroborated 2026-08-08 — the same firm and the same underlying
  dataset (60 planned sites, 97GW) this thread's 08-10 entry already
  cites in aggregate, without its largest single instance. Amazon's
  statement: it "believes in paying the full costs of powering our
  operations," and the campus is "powered by new on-site generation
  that won't raise electricity costs for Texas families."
  ([Cleanview](https://newsletter.cleanview.co/p/scoop-amazon-is-behind-one-of-the), [DataCenterDynamics](https://www.datacenterdynamics.com/en/news/amazon-acquires-8000-acre-site-in-pecos-texas-for-natural-gas-powered-behind-the-meter-data-center-report/), [Pacifico Energy](https://www.pacificoenergy.com/post/pacifico-energy-announces-gw-ranch-project-bringing-5-gigawatts-of-reliable-off-grid-power-for-ai-i)) ⟨daily 2026-08-10, added 2026-08-11⟩

## 2026-08-08 — DOJ backs xAI's bid to gut citizen-suit enforcement entirely

- **The Justice Department intervened in the NAACP's Clean Air Act
  citizen suit against xAI's unpermitted Southaven, Mississippi
  turbines, arguing the Constitution lets the President and federal
  agencies decide whether to enforce federal law at all** — not a
  narrow defense of xAI's turbines specifically, but a challenge to the
  citizen-suit provision itself, a cornerstone of environmental
  enforcement for 50+ years. The DOJ separately argues shutting down
  power to the turbines would harm national security because Colossus
  "supports Department of War operations." Escalates this thread's
  already-logged DOJ national-security shield into a precedent fight
  that could outlive this specific case.
  ([Fortune](https://fortune.com/2026/08/08/lazarus-26-years-citizen-suits-musk-xai/), [Earthjustice](https://earthjustice.org/press/2026/trump-administration-attempts-massive-power-grab-in-defense-of-musks-xai)) ⟨daily 2026-08-08⟩

## 2026-08-07 — Trump publicly calls the Texas pause "a mistake"

- **In a Punchbowl News interview, Trump called Texas's new data-center
  construction pause "a mistake... it could be bigger than oil,"**
  responding to Gov. Abbott's 08-03 moratorium on new grid connections
  pending an ERCOT/PUCT power-and-water audit. First time the President
  has weighed in directly on a specific state's data-center permitting
  fight — pulls what had been a state-level grid/water dispute into
  national politics. Same interview, Trump separately said Congress
  wants to regulate AI "out of business" (logged on
  `frontier-model-gov-review-precedent`).
  ([Texas Tribune](https://www.texastribune.org/2026/08/07/donald-trump-texas-data-centers-greg-abbott/)) ⟨daily 2026-08-07⟩

## 2026-08-05 — PJM's answer to the same-week Texas freeze: bring your own power or get cut off

- **PJM (the 13-state PA-to-Illinois grid operator) launched an "Interim
  Resource Adequacy Service"**: large loads (50MW+, i.e. essentially all
  data centers) must be registered, and must either secure their own
  bilateral power contracts (generation, storage, demand-response) or
  face curtailment ahead of other emergency measures once the rule bites
  in June 2027. States/utilities enforce it — PJM itself has no authority
  to curtail a customer directly — and can run their own "reliability
  backstop procurement" auctions to help data centers avoid curtailment.
  Trigger: capacity-auction costs hit $16.4B in the June auction, data
  centers were 38% of that, and PJM projects 30-34GW of new data-center
  demand by the early 2030s.
  ([Canary Media](https://www.canarymedia.com/articles/data-centers/pjm-data-center-plan)) ⟨daily 2026-08-05⟩
- **Filed alongside a separate, more immediate fix: a one-time "backstop"
  capacity auction**, submitted to FERC 2026-07-31, running 2026-09-30 to
  2026-10-21, to plug a 6.8GW shortfall from PJM's last base auction —
  can procure up to $20B in new generation capacity through 2027.
  ([Utility Dive](https://www.utilitydive.com/news/pjm-backstop-capacity-auction-ferc-data-centers/826792/)) ⟨daily 2026-08-05⟩
- 💡 **This thread went quiet 07-25 on the "equipment ceiling + DOJ
  shield" verdict; the story has moved from equipment scarcity to grid
  governance.** PJM is now doing structurally what Texas's PUCT/ERCOT
  freeze did procedurally the same week (see `ai-power-buildout` and
  `where-the-capex-lands`) — pushing the risk of an unbuilt or
  under-powered site back onto the developer instead of the ratepayer.
  ⟨daily 2026-08-05⟩

## 2026-07-24 — Opened + crawled

- **Thread opened** (ben-steer). ⟨steer 2026-07-24⟩
- **Verdict: severe, worsening, multi-dimensional — power is the gating
  factor.** The defining escalation is legal-political: the DOJ now invokes
  national security to keep unpermitted turbines running against a citizen
  Clean Air Act suit — the improvisation has outrun the regulatory system.
  ⚠ WebSearch budget exhausted (fan-out) — flagship + high-value claims
  re-verified via fetch; some figures RSS-only, flagged. ⟨crawl 2026-07-24⟩

## ← Backstory (crawl 2026-07-24 → artifacts/findings/datacenter-power-grid-2026-07-24.md)

## 2026-07 — The equipment ceiling + the ratepayer bill

- **GE Vernova's gas-turbine backlog hit 116 GW, sold out through 2030**
  ($176B total backlog, data-center orders >$5B YTD = 2x all of 2025) —
  even self-supply can't scale fast. Same week, PJM's market monitor:
  **data centers drove 38% of the latest capacity-auction charges (46%
  across four auctions)**; the 2028/29 auction cleared at the $325/MW-day
  price cap; FERC's chair warned PJM faces a "grave legitimacy crisis."
  ([GE Vernova](https://www.gevernova.com)) ⟨crawl 2026-07-24⟩

## 2026-06-16 — The DOJ national-security shield

- **The Trump DOJ moved to dismiss the NAACP Clean Air Act suit on
  national-security grounds** — arguing shutting the 57 unpermitted
  Southaven turbines threatens security because Grok "supports Department
  of War operations" (a DoD official called Grok "paramount national
  security," citing the Iran strikes). Converts an environmental-permitting
  fight into a federal-power question. Cross-refs `spacex-colossus`.
  ([NYT](https://www.nytimes.com/2026/06/16/climate/)) ⟨crawl 2026-07-24⟩

## 2026-04 — Improvising around the grid, at scale

- **Meta's "Hyperion" got ~7 new gas plants fast-tracked in Louisiana**
  (Entergy +$14B capex; a later ratepayer-protection order); **NAACP/SELC/
  Earthjustice sued xAI** over 27 unpermitted methane turbines (~495 MW,
  alleged 1,700+ t/yr NOx) at Southaven — "a de facto power plant without
  an air permit," in a historically Black neighborhood leading TN in asthma.
  ([Earthjustice](https://earthjustice.org)) ⟨crawl 2026-07-24⟩

## 2026-01 — EPA: the turbines ran illegally

- **EPA ruled xAI's Memphis turbines ran illegally** under a bogus
  "temporary" exemption — 35 operated, only 15 permitted. Memphis is really
  two braided sites: Colossus 1 (Boxtown, TN) + Colossus 2 (Southaven, MS).
  ([TechCrunch](https://techcrunch.com/2026/01/16/epa-rules-that-xais-natural-gas-generators-were-illegally-used/)) ⟨crawl 2026-07-24⟩

## Backstory — the queue + the equipment wall

- **ERCOT's large-load queue hit ~438 GW (+~300% YoY)**; large-transformer
  lead times are ~2.5–3yr (vs 4–6 weeks pre-pandemic), Wood Mackenzie
  projected a 30% transformer supply deficit; AEP Ohio's landmark
  data-center tariff (07-2025) is the template other states now copy
  (make data centers pay for their minimum contracted power). ⚠ ERCOT
  438GW + transformer figures RSS/secondary-sourced. ⟨crawl 2026-07-24⟩
