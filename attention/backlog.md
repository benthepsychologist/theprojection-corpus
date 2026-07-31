# backlog.md — the big-player build-out map

*What needs to be crawled and built, per actor — mapped from a full local
audit of threads × timeline-depth × actor-doing × axes coverage
(ben-steer 2026-07-27: "map out all the stuff that needs to be crawled and
built out"). No investigation done here — this is the work order, not the
work. Items get checked off as crawls/steers land; provenance as usual.*

**The headline gap, Ben's words:** "I still don't have even a blurry
picture of what Microsoft and Google are DOING with all that CapEx."
The audit agrees: the capex *tree structure* exists but the leaves are
scaffolding — `microsoft-capex` has **1 timeline entry**, `aws-capex` 1,
`meta-capex` 2, `google-capex` 3, and the destination leaves
(`ai-compute-spend`, `ai-power-buildout`, `ai-datacenter-sites`) have
**1 entry each**. We track the guidance dollars; we don't track what the
dollars buy.

---

## W1 — THE CAPEX PICTURE (the named blur; highest priority)

One deep crawl per hyperscaler, answering the same four questions so the
answers are comparable. Output per actor: timeline backfill on its
`*-capex` leaf + entries pushed down into the destination leaves + a
finding + bundle.

**The four questions per actor:**
1. **Sites** — which datacenters, where, how many GW, what timeline?
   (→ `ai-datacenter-sites`)
2. **Silicon** — the split: own chips (TPU/Trainium/Maia/MTIA) vs Nvidia
   orders vs other; volumes where reported. (→ `ai-compute-spend`,
   `inhouse-silicon`, `nvidia-order-book`)
3. **Power** — signed PPAs, nuclear deals, grid interconnects; GW secured
   vs needed. (→ `ai-power-buildout`, `nuclear-for-ai`,
   `datacenter-power-grid`)
4. **Payoff claim** — what management says the spend buys (AI revenue
   run-rates, model training, product surface) vs what's verifiable.

- [x] `/crawl google-capex` — DONE 07-27 (54 sources): — the $195–205B: TPU v7 vs Nvidia mix, site
      list, PPA book, "significantly more in 2027"
- [x] `/crawl microsoft-capex` — DONE 07-27 (30 sources): — the $97B/yr + the $250B OpenAI Azure
      commitment: how much is OpenAI-serving vs own-model (MAI) vs
      enterprise; Maia volumes; the "$37B AI run-rate" verdict (earnings
      Wed)
- [x] `/crawl aws-capex` — DONE 07-27 (28 sources): — the ~$200B plan vs the AGI-team cuts: Trainium
      share, Anthropic-serving share, site map
- [x] `/crawl meta-capex` — DONE 07-27 (55 sources): — the $76B: MTIA vs Nvidia, the Scale AI angle,
      open-weights strategy as capex justification
- [x] After all four: **one synthesis pass** — DONE 07-27 (the table is in the meta-thread timeline): into
      `hyperscaler-capex-big-picture` — the comparable table (sites / GW /
      silicon mix / payoff evidence per actor), which becomes the meta
      thread's timeline anchor. This is the "blurry picture" fix.
- [ ] `camellia` (OpenAI Georgia site, w1, 0-entry) — fold into the site
      crawls or crawl standalone.

## W2 — ZERO-THREAD CHOKEPOINTS (highest gravity, no narrative)

Actors with **zero threads** on the board despite chokepoint gravity.
Each needs: 1–2 seed threads (candidates below — Ben confirms names),
a `/crawl` backstory, and an `actor-doing` entry.

- [x] **TSMC** — DONE 07-28 (`tsmc-capacity-race` + crawl, 50 src): (gravity ~$1.5T, 0 threads) — candidates:
      `tsmc-capacity-race` (AZ/JP/DE buildout, the $60B+ guidance, the
      forced geographic split) · CXMT/China exposure angle rides
      `china-stack-independence`
- [x] **Arm** — DONE 07-28 (`arm-royalty-regime` + crawl, 38 src): (gravity ~$800B, 0 threads) — candidate: `arm-royalty-regime`
      (SoftBank's 87%, the Qualcomm settlement aftermath, ISA leverage,
      v-next licensing economics)
- [x] **Intel** — DONE 07-28 (`intel-rescue` + crawl, 33 src): (0 threads) — candidate: `intel-rescue` (the state
      golden-share, Nvidia/SoftBank stakes, fab cancellations, thrust≈0
      story — the subsidized-builder paradox)
- [x] **CoreWeave** — DONE 07-28 (`coreweave-backlog-bet` + crawl, 51 src): (0 threads) — candidate: `coreweave-backlog-bet`
      ($99.4B backlog vs debt-financed capacity; the neocloud category)
- [x] **Qualcomm** — DONE 07-28: the story SHOWED (Dragonfly re-entry) — `qualcomm-dragonfly` opened; actor-doing written
- [x] **Broadcom** — DONE 07-28: crawl evidence settled merge-vs-new — `custom-asic-tolls` OPENED (Ben confirmed); actor-doing written. Original note: `custom-asic-tolls`
      (TPU/MTIA/OpenAI co-design + VMware annuity — the rentier story;
      the OpenAI Jalapeño story folded into `inhouse-silicon` partly
      covers this — decide merge vs new)

## W3 — TAGGING & STRUCTURE FIXES (cheap, do first)

- [x] **`xai` is untagged everywhere** — DONE 07-27: — `grok-frontier`,
      `grok-companion-harm`, `spacex-colossus` carry only
      spacex/elon-musk. Add `xai` → its node page stops being empty.
      (steer-sized)
- [x] **Sub-entity slugs not on watchlist** — DONE 07-27 (dropped to parent-only):: `microsoft-nuance`, `verily`,
      `apple-health`, `amazon-health` used as thread entities — either add
      as watchlist entities or drop to parent-only tags. (steer-sized)
- [x] **ASML not on the board** — DONE 07-27 (boarded + watchlisted; bundle rides row 24): — `/steer add actor` + axes_num + bundle
      (sole-EUV, gravity ~$1.5T — the biggest absent node). Also ROADMAP
      row 24.
- [x] **`apple`/`coreweave` unpocketed** — DONE 07-27 (both → hyperscaler): — assign pockets so their rings
      color. (steer-sized)

## W4 — ACTOR-DOING GAPS (the synthesis layer)

`actor-doing.yaml` covers 18 actors; these majors have **none** — their
node pages show no "what are they doing now":

- [x] xai — DONE 07-28 (L2 subnode under spacex per Ben: identity separate, MONEY WELDED to parent; actor-doing written) · [x] tsmc · [x] arm · [x] intel ·
      [x] broadcom · [x] coreweave · [x] cxmt · [x] softbank ·
      [x] samsung · [x] sk-hynix · [x] micron (all three 07-28, memory-trio crawl) · [x] blackrock ·
      [ ] vanguard · [x] qualcomm
- Cheapest path: write each from its crawl (W1/W2/W5) as it lands, rather
  than a standalone pass — but softbank + cxmt + blackrock can be written
  NOW from existing thread/timeline material.

## W5 — THE MONEY SIDE'S OWN STORIES

- [x] **BlackRock** — DONE 07-28 (`asset-managers-build-ai` opened, cohort thread; actor-doing written): (0 threads despite GIP/$40B Aligned, the Meta bond
      sale, MGX partnership) — candidate: `asset-managers-build-ai`
      (BlackRock GIP + KKR Helix + the SWF co-investors — the
      capital-pool entry into physical AI infra). One thread covering the
      cohort beats one per manager.
- [x] **SoftBank** — DONE 07-28 (judged: pieces lived in 4 threads, nothing tracked the CONCENTRATION — `softbank-all-in` opened; actor-doing written): (4 threads ride others' stories; no synthesis) —
      candidate: `softbank-all-in` (the $40B loan, Stargate equity, Arm
      87%, the Son-empire concentration risk) — or judge whether
      `stargate-buildout` + `openai-ipo-timing` already carry it and only
      actor-doing is missing.
- [x] **Memory trio** — DONE 07-28 (judged: widened `ai-memory-shortage` watch into the capacity-race ledger — a new thread would fragment; cxmt actor-doing written; samsung/sk-hynix/micron entries ride future crawls): (samsung/sk-hynix/micron share one thread) —
      candidate: `hbm-capacity-race` (the 3-year HBM deficit, capacity
      adds, CXMT pressure) — or widen `ai-memory-shortage`'s watch.

## W6 — NODE-PAGE DEPTH (site-side, after content exists)

- [x] Thread lists on node pages — DONE 07-28 (live sorted by depth w/ entry counts + meta marks + parent tags; resolved/retired collapse into 'Concluded'): — no meta-grouping, no
      timeline-depth signal. Revisit after W1/W2 fill content.
- [x] The retired/resolved threads — DONE 07-28 (collapsed, not hidden; enum comment fixed to match publish reality): in "their threads" —
      check node-page filtering.
- [x] Thrust×gravity diagonal plate — DONE 07-28 (self-contained embed on both financing thread pages; reach=spend labeled, click→node): `ai-circular-financing-risk` /
      `nvidia-vendor-financing` thread pages (queued from plate v2).
- [x] Nvidia `axes_num.thrust` → 30 (stakes in, per recipe — ben-steer
      07-27); Broadcom → 0 (dep-only rule kills the amortization artifact).
- [x] **Dep-only recompute — DONE 07-28** (wave H audit: microsoft 57→71, oracle 46→48, google Wiz-fix →140; amazon/google verified clean; elevance artifact-suppressed to 0). Original: — the
      pilot's capex−D&A figures used blended D&A; re-derive with
      depreciation-only during the W1/W2 crawls (biggest suspects: Oracle,
      Qualcomm, anyone post-acquisition).

---

*Sizing key: steer-sized = one /steer pass · crawl = a /crawl dispatch ·
build = template/publisher work. Sequence intent: W3 (cheap fixes) →
W1 (the named blur) → W2 → W4/W5 as their crawls land → W6.*
