<!-- state-of-the-game · q3 (datacenter census) · deep-research agent, verbatim
     2026-08-03 · fetch-only (WebSearch budget exhausted session-wide) -->

# STATE OF THE GAME — Who already maintains the AI-datacenter census?

> 🎯 **Verdict: partially settled — and for the 10 named AI players specifically, Epoch AI's free Frontier Data Centers Hub + AI Data Centers dataset is already ~80% of the census, with SemiAnalysis's Datacenter Industry Model the purchasable "complete" version.** The generic global-facility census (8,000–10,500 sites) is a mature commercial product sold by at least three vendors; the *AI-player-attributed, energized-vs-announced, per-facility-MW* cut is newer but no longer open ground.

## 1. Commercial datacenter intelligence

- **SemiAnalysis Datacenter Industry Model** — 5,000+ DCs; US/NA/APAC/China/EMEA; 50+ companies incl. hyperscalers, neoclouds (CoreWeave), xAI, Tesla. Per-facility MW, self-build vs **leased**, critical IT power, PUE, capex; forecasts to 2027–2030. Method: property records, permits, power usage, FOIA, satellite + CV. Institutional; quarterly; price undisclosed. https://semianalysis.com/datacenter-industry-model/
- **DC Byte** — 8,300+ DCs; GW IT capacity; live/committed/planned taxonomy. Enterprise, gated. https://www.dcbyte.com/
- **DataCenterHawk** — 10,500+ DCs, 460+ markets, 500+ GW; absorption/lease/vacancy + 2,900 transaction comps; 30+ analysts. Enterprise. https://www.datacenterhawk.com/
- **Baxtel datasets** — 8,000+ sites; **per-site current AND planned MW**, status, company ("40.5 GW under construction, 238 GW planned"). CSV snapshot or annual sub; "lower price point"; undisclosed. https://baxtel.com/services/datasets
- **Synergy Research** — 1,136 hyperscale DCs (end-2024), 19 operators; AMZN+MSFT+GOOG = 59% of capacity; MW critical IT load, operator-level; "discounted inflated marketing claims." Enterprise; press free.
- **Cushman & Wakefield** — 107 markets, 24 variables (2026), market-level; **free annual report**. JLL/CBRE — market-level MW, free PDFs.
- ⚠️ No vendor price verifiable anywhere — all contact-sales. Directories (DataCenterMap "Meta 159 DCs", datacenters.com, Dgtl Infra) thin on MW / fetch-blocked.

## 2. The AI-specific trackers (the real center of gravity)

- ✅ **Epoch AI — AI Data Centers** (epoch.ai/data/data-centers): 75 AI DCs, 15 owners, 12 GW IT, 12.9M H100e; per-facility IT-power MW, H100e, capex, construction phases; satellite (cooling-count) + permits + company statements; **free, CSV, CC-BY**, updated 2026-08-02.
- ✅ **Epoch — Frontier Data Centers Hub**: deep-tracks 13 largest US sites (~2.5M / ~15% of ~15M global H100e); annotated satellite build-out timelines; "five facilities cross 1 GW in 2026." Plus a **Stargate site-by-site tracker**.
- ✅ **Compute Atlas** (compute-atlas.com, Edward Kubiak) — 786 US sites, 284 operators, per-site GW + status, **2,813 cited sources**; "announced 197 GW vs operating 11.7 GW ≈ 17:1." Free, CC, API+RSS.
- ✅ **AI Infrastructure Map** (aiinfrastructuremap.com) — 250+ projects + nuclear/SMR + grid overlay; US ~100%, ex-US ~30%; LLM-extracted from ~40 feeds + SEC/FERC; free.
- **usdatamap.com** — 790 US facilities, MW + status, daily scrapes; free; thinner provenance. **Kovastack** — permit/utility monitoring, Stargate site lists.

## 3. Journalism
- **Business Insider** — interactive US DC map + bans map + satellite series (fetch-blocked; not downloadable). **Bloomberg** — recurring graphics; BNEF sells build tracking behind terminal; no public dataset. **Washington Post** — power investigations, narrative. **DCD / Data Center Frontier** — best per-announcement news layer, no public dataset, blocks scraping.

## 4. Government / academic / NGO
- **LBNL** 2024 report + 2025 update (OSTI, Jun 2026): DCs → 11.8% of US electricity by 2030 (9.5–15.3%). National aggregates, no facility list.
- **IEA Energy & AI** — 415 TWh (2024) → ~945 TWh (2030); regional aggregates; blocks fetch.
- **EPRI DCFlex** + IM3/EPRI load dataset; **PNNL IM3 Open Source Data Center Atlas** (immm-sfa.github.io/datacenter-atlas) — DOE-funded US atlas, OSM-derived geometries, **explicitly no MW**, ODbL.
- **Grid queues** — ERCOT large-load queue public (426+ GW pending, 1,846 rows); ercotqueue.com (CSV/GeoJSON, CC-BY). ⚠️ queue rows ≠ facilities, wildly inflated (400+ GW vs ~12 GW operating).
- **Germany RZReg** — public register live (EnEfG, 300 kW threshold, annual filings). **EU EED Article 12 / Reg 2024/1364** — mandatory per-facility reporting into a Commission DB; Commission publishes **aggregate only** (~64 GW EU installed). Real growing quasi-census for Europe, aggregate-only.

## 5. Open / community data
- **OpenStreetMap** `telecom=data_center` — no capacity attributes. **GitHub D-ivy/data-centers-info** — Parquet merge of IM3+Epoch+OSM+PeeringDB (a merge recipe). **Wikipedia** — per-site articles for marquee sites, no systematic MW list. ❌ "WikiDCs" does not exist.

## 6. Per-player disclosure
- **Google** — datacenters.google/locations: 30 active, 11 countries, no MW. **Microsoft** — regions not facilities, no MW. **Amazon** — Regions/AZs only, no addresses/MW. **Meta** — campus list, GW only for flagships. **OpenAI** — Stargate announcements, 7 US sites ~5 GW planned; Epoch's tracker is the discipline layer. **Anthropic** — states only, no MW (thinnest thread). **xAI** — nothing systematic; Epoch/SemiAnalysis cover Colossus. **Oracle** — regions only; Stargate capacity sits with Crusoe/Vantage propcos. **CoreWeave** — active vs contracted MW in investor materials (unverified). **Nvidia** — not an operator at scale; DGX Cloud rides partners (attribution problem).

## READ-FIRST / BUY-FIRST (ranked)
1. **Epoch AI — AI Data Centers + Frontier Hub** (free, CC-BY, CSV) — download first; IS the per-facility MW, energized-vs-planned census for the AI players.
2. **SemiAnalysis Datacenter Industry Model** ($) — the only systematic **lease-vs-self-build attribution** across all 10 players at 5,000+ scale; the completeness buy.
3. **Compute Atlas** (free) — US announced-vs-operating transparency benchmark; steal its sourcing model.
4. **Baxtel** (cheapest paid CSV) — 8,000+ sites, current+planned MW; value backbone if SemiAnalysis out of budget.
5. **Synergy releases** (free) — sanity-check totals. 6. **LBNL/IEA** (free) — aggregate envelopes to sum inside. 7. **Cushman/JLL/CBRE** (free) — market-level cross-checks. 8. **ERCOT queue** (free) — pipeline reality check + the 17:1 lesson. 9. **EU EED + German RZReg** (free) — European regulatory seam. 10. **DC Byte / DataCenterHawk demos** — only if brokerage-grade colo needed.

**Is the census already purchasable? Yes, twice** — Epoch free for the AI-frontier cut, SemiAnalysis for the exhaustive attributed version. Building from scratch re-derives a solved layer.

## GAP ANALYSIS — what nobody covers cleanly
- **Owner/operator/propco/tenant attribution** — the hardest seam (Abilene = Crusoe-built/Oracle-leased/OpenAI-dedicated; Rainier = Amazon-owned/Anthropic-dedicated). Only SemiAnalysis claims systematic lease-attribution; no open dataset models the four-layer stack.
- **Dedicated-lease share within colo** — contract-private everywhere.
- **Energized-vs-announced discipline outside the US** — Epoch + Compute Atlas do it for the US; everyone else blends pipeline into headline GW.
- **Anthropic and CoreWeave** are the thinnest per-player threads.
- **Non-US depth** — every AI-specific tracker is US-centric.
- **MW definitional chaos** — IT/critical vs utility connection vs campus conflated; only Synergy and Epoch state their definition.

## VERDICT
**Partially settled, leaning settled.** For the ~10 named players a free satellite-verified per-facility-MW energized-vs-planned census exists (Epoch, 75 sites/~12 GW/CC-BY) and a paid exhaustive lease-attributed version exists (SemiAnalysis); the generic census is a commodity (DC Byte/DataCenterHawk/Baxtel, 8,000–10,500 sites). Genuinely open: the *attribution graph* — who owns/operates/finances/consumes each MW across propco/developer/tenant layers, dedicated-lease shares in colo, disciplined non-US coverage. Ben's ex-CN/RU bet is correct — but the move is assemble-and-attribute on top of Epoch + Compute Atlas + Baxtel-class data (SemiAnalysis buy as completeness shortcut), NOT re-census from scratch.
