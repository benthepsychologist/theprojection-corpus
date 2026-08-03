<!-- state-of-the-game · q1 (buildout flows) · deep-research agent, verbatim
     2026-08-03 · fetch-only (WebSearch budget exhausted session-wide);
     ~30 primary fetches; Bloomberg/FT/BI/WSJ/IEA fetch-blocked, marked. -->

# STATE OF THE GAME: Who already tracks "where the AI buildout money actually goes"

**Process caveat:** WebSearch budget exhausted before start; verified via ~30 direct WebFetch of primary pages. Solid for known vendors/analysts; the long tail of obscure newsletters may be under-sampled. Bloomberg, FT, Business Insider, WSJ, IEA could not be fetched (bot-blocked/paywalled) — marked.

## 1. Commercial data / research vendors
- **SemiAnalysis Datacenter Industry Model** — 5,000+ DCs, facility-level, property records + permits + power + FOIA + satellite/CV. Accelerator shipment forecasts to 2027, **"datacenter capex breakdowns by category"** (the what-the-money-buys decomposition), supply/demand per hyperscaler/region, 2023–2030, quarterly. Companion models: Accelerator Industry, AI Cloud TCO (neocloud economics — the vendor-financing-adjacent layer), AI Networking, Energy, GPU Pricing Index. Institutional pricing. **The de facto answer to "does anyone decompose by what the money buys" — at institutional prices.** https://semianalysis.com/datacenter-industry-model/
- **Dell'Oro** — Data Center IT Capex, Physical Infra, AI Back-end Networks, Liquid Cooling, High-density Power — money by equipment category, per quarter. "AI back-end switch sales to approach $1T over 2026–2030" (Jul 28 2026). https://www.delloro.com/market-research/
- **Synergy** — hyperscale capex/capacity quarterly; hyperscalers 67% of DC capacity by 2031; neocloud ~$400B by 2031. Enterprise wall; press free.
- **Sell-side (GS/MS/UBS)** — public summaries confirmed (Goldman "What the Capex Boom Means," Jul 21 2026; MS "Buying the AI Infrastructure Dip"); actual capex trackers client-only, contents unverifiable — treat public pages as marketing summaries.
- IDC/Omdia/Gartner — existence only, detail not verified. New Street — firm confirmed, AI-capex product not.

## 2. Independent analysts & newsletters
- **Epoch AI** (epoch.ai/data) — the open-data backbone (see §5). Free, CC-BY.
- **Paul Kedrosky** (paulkedrosky.com) — sharpest public work on flows *fragility*: "Hyperscaler CapEx Sits on Thin Implied Equity" (Jul 14 2026, relays Carlyle: NPV of future rentals net of capex ≈ 15% of ~$2.2T backlog); "Coming Mega-IPO Flow & Funding Problem of 2026." Free.
- **Ed Zitron — Where's Your Ed At** (wheresyoured.at) — closest thing to a running commitments-vs-delivered + circularity ledger, in polemic form; journalistic aggregation of filings, not a dataset, but does the reconciliation nobody else publishes free. Free + $70/yr.
- **McKinsey "The cost of compute: a $7T race"** — the one *verified* public what-the-money-buys decomposition: **$6.7T cumulative DC investment by 2030 ($5.2T AI-specific), split 60% chips/hardware · 25% power/cooling · 15% land/construction**; scenarios $3.7T–$7.9T. One-off, not recurring. https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-cost-of-compute-a-7-trillion-dollar-race-to-scale-data-centers
- **Sequoia / David Cahn "AI's $600B Question"** (Jun 2024) — canonical gap arithmetic (Nvidia run-rate ×2 for DC cost ×2 for margin = required end-revenue). Method sound, numbers dated.
- Others: Construction Physics (physical-buildout primers), Fabricated Knowledge / Irrational Analysis (semis value chain), Bain Technology Report 2025 (capex-to-required-revenue), JPM Cembalest EOTM, Apollo/Slok Daily Spark.

## 3. Government / academic / institutional
- **Epoch AI** (nonprofit) — AI Data Centers hub: 75 facilities, satellite + permits + drone; per-facility IT-power MW, H100e, capex, timelines; updated Aug 2–3 2026. ⚠️ capex DERIVED from IT power via cost-per-watt, not independently measured spend.
- **LBNL** (datacenters.lbl.gov) — official US DC electricity line; 2025 update out. Energy, not dollars.
- **IEA Energy and AI** — could not fetch (403); established but unverified this session.
- **Census C30 / Value of Construction** — the widely-cited "data center construction" line item **did NOT appear on the index page fetched**; FRED search surfaced **no dedicated DC-construction series**. Flag for one manual check of C30 detailed tables.
- **CSET ETO** (eto.tech) — free chip-supply-chain map (structural, not dollar-flow). **Grid Strategies** — load-growth/interconnection reports (titles unverified). Fed/BEA/academic flow-modeling papers under-sampled.

## 4. Journalism
- **The Information** — maintains **AI Data Center Database + AI Chip Database** under Pro; strongest verified maintained journalism dataset.
- **Data Center Watch** (datacenterwatch.org) — tracks **blocked/delayed** DC projects, quarterly back to 2023; Q1 2026 the largest concentration of blocked projects on record. Free. A real (narrow) commitments-vs-delivered signal.
- Bloomberg circular-deals graphic (Oct 2025) + power coverage — unverified (fetch-blocked). Business Insider US DC map — fetch-blocked. FT/WSJ — cover circularity heavily but no evidence of a maintained *dataset*.

## 5. Open datasets / APIs — Epoch AI is the category winner
All free, CC-BY, downloadable, current to within days (epoch.ai/data):
- AI Data Centers (75 facilities, MW/H100e/capex/timelines) · AI Chip Sales (units, compute, power, **cost USD** by vendor, quarterly, ~2× bands — supports total annual AI chip spend by vendor, the chip slice, free) · GPU Clusters (500+) · AI Chip Components (wafer/CoWoS/HBM) · AI Chip Owners ("five companies control 71% of global AI compute") · AI Companies (revenue, funding, compute).
Other: CSET ETO (structural), Synergy/Dell'Oro press (headline layer), Data Center Watch quarterlies, Data Center Map (429, unverified).

## READ-FIRST (ranked)
1. **Epoch AI data hub** — free, facility+chip level, updated this week.
2. **SemiAnalysis** — free newsletter minimum; the Datacenter Industry Model IS the commercial answer if budget allows.
3. **McKinsey $7T piece** — the one free what-the-money-buys split; the skeleton.
4. **Paul Kedrosky** — free; best public thinking on backlog vs equity.
5. **Where's Your Ed At** ($70/yr) — running commitments/circularity ledger in prose; keep the arithmetic.
6. JPM Eye on the Market (power-side flows). 7. Bain Technology Report (capex-to-revenue). 8. Synergy + Dell'Oro press (quarterly headline). 9. The Information Pro (AI DC + Chip databases). 10. Data Center Watch + Sequoia's $600B piece (once, for the method).

## GAP ANALYSIS
- **An integrated who-pays-whom flow map does not publicly exist.** Every layer has a tracker (chips, equipment, facilities/MW, power, totals) but nobody publishes a single reconciled Sankey from capex payers → vendors → components → facilities. SemiAnalysis comes closest, institutionally priced and organized by market not by flow.
- **Commitments-vs-delivered tracked in fragments, never reconciled in dollars.** Epoch measures delivered capacity (MW, not spend); Data Center Watch tracks blocked; pipeline vendors track stages behind paywalls; Zitron/Kedrosky argue in prose. No maintained "announced $X → contracted $Y → in-ground $Z" dataset. The MW↔dollars bridge is always derived, never measured.
- **Circular financing has journalism, not a dataset.** No maintained graph of vendor-financing edges (Nvidia equity→customers, Microsoft credits→OpenAI, GPU-collateralized debt, neocloud offtake guarantees) with amounts/dates/instrument types.
- **Official statistics can't see it.** No FRED DC-construction series; Census C30 line unconfirmed; chips imported and not broken out as "AI." Macro layer runs on ad-hoc analyst arithmetic.

## VERDICT: Partially settled — read the layers, build only the joins.
Each *component* is mature and tracked (chip dollars, equipment categories, facility buildout, power, totals + required-revenue arithmetic); SemiAnalysis sells nearly the whole stack to institutions. Researching any layer from scratch re-derives purchasable/free work. Genuinely open, additive not duplicative: a reconciled who-pays-whom decomposition across layers, a dollar-denominated commitments-vs-delivered ledger, and a maintained circular-financing graph. Those exist today only as prose (Zitron, Kedrosky, FT/Bloomberg stories) or partial behind institutional pricing — nobody publishes them as data.

Unverified-this-session: IEA (403) · Bloomberg/FT/WSJ/BI trackers (blocked) · Census C30 line · Grid Strategies list · IDC/Omdia/Gartner detail · Data Center Map (429) · Fed/academic flow-modeling papers (under-sampled).
