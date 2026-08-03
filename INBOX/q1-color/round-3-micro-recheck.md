<!-- color-team · round 3 · micro-recheck · 2026-08-03
     JOINT MEMO — covers the q1 v3.1 amendment (edge-typing) AND the
     q2 v3.1 amendment (ladder encoding) plus all eight line residues.
     q2-color/RESULTS.md points here.
     model: Claude (Fable-tier subagent, fresh context)
     memo below is the seat's return, verbatim and unedited. -->

# RED memo — micro-recheck of the two v3.1 amendments · 2026-08-03

**Scope held:** exactly the two substantive amendments + the eight line residues. No general scan performed.

> 🎯 **Verdict: both amendments RESOLVED, all eight line residues landed — PASS.**

---

## A. q1 edge-typing residue — **RESOLVED**

The original failure was a wording collision: "a payment for compute capacity or services is NEVER build" made an EPC contract simultaneously "a payment for services" (never build) and asset acquisition (build), so the sourcer's pick silently decided the flagship total. The amended rule in §3 closes it at both ends. First, the test is re-grounded: **"type by what the payment procures"** replaces payment-form language, so the classifying question is no longer "is this a service?" but "what does the buyer end up with?" — and under that question an EPC payment procures an asset, not use of capacity. Second, and decisively, the rule no longer leaves the EPC case to inference at all: it names it — *"an EPC, construction, or engineering contract for a datacenter the buyer will operate is asset acquisition, not a service — regardless of contract form."* The exact edge class the finding built its failure on is now enumerated with an explicit type. A payment to an EPC for a datacenter the buyer will operate has exactly one legal type (`asset purchase`); the old broad reading is textually foreclosed, not merely disfavored — no competent-operator interpretation is required. The rollup read-set piece also landed as specified: the Gross-build bullet now states the category rollup's read set as *operator-frontier asset purchases plus non-decomposed `capacity/service payment` crossings of the cut, rendered under "purchased compute capacity (services)"* — making the §12 category reachable, consistent with F1 (both components are filter-crossings/frontier reads), and giving R-17's "says so on its face" its carrier. The "non-decomposed" qualifier prevents double-counting where a capacity seller's own build IS traced. I checked the amendment for newly introduced problems and found none that rise above nit (the "purchase edges only" phrase for destination categories predates the amendment, and the new read-set sentence itself pins which category the crossings render under).

## B. q2 ladder-encoding residue — **RESOLVED**

The original failure: the ladder claimed q1's `stage` field as carrier while `recognized` and `collected` had no legal enum value, forcing improvisation on every revenue observation. The amended §4 table gives every rung exactly one legal encoding drawn entirely from q1 §4's existing enums — claimed run-rate → `guidance`; booked → `contract`; recognized → `delivered` + `accrual` basis; collected → `delivered` + `cash` basis — declared as "the rule, not a suggestion." Verified against the q1 enums as written: `guidance`, `contract`, `delivered` are all legal stage values; `accrual` and `cash` are legal basis values; no rung needs a value that doesn't exist, and the encoding is also uniquely decodable (the two `delivered` rungs are separated by basis; the two basis-free rungs by stage), so no (stage, basis) pair maps to two rungs. The mapping is coherent with the placement rule directly above it (booked = `contract` stage → commitment object; stage-3/4 = `delivered` → revenue edges via `commitment_ref`). The revenue-side consistency check is stated as required: **its own flag class**, running alongside q1's spend-side one, collected ≤ recognized ≤ booked, per seller-buyer pair per period — and it is now runnable because both comparands have legal encodings, with the enforcement locus stated ("on the encoded values, not on prose"). No new problem introduced by the amendment.

---

## Line-residue checklist

**q1 (v3.1):**
- ✅ **W-2 instrumentation note** — §6: first delta passes measure per-pass labor cost; ⚙ row joins §12 only if data demands
- ✅ **Coverage-state table restored** — §3 table (measured/aggregated/unmeasured); §4's "§3's coverage table" reference now resolves, wording matches verbatim
- ✅ **Operating-cash trimmed from edge tags** — tag list is debt · equity · vendor · sovereign; operating cash lives only in the pool, stated explicitly
- ✅ **§1.5 wobble wording softened** — now "never move *unexplained*," with coverage-extension named as a legitimate labelled mover

**q2 (v3.1):**
- ✅ **⚙ zero-until-scheduled** — §7, named as the forward-amortization convention, anti-confirmation direction noted; §7's LHS also reworded to "commitment drawdown amortizing per F4"
- ✅ **Bound-propagation rule** — §6: aggregates over typed values render as a range or state their point-convention on face
- ✅ **Burn single-cut sentence** — §7: same window convention and same single named cut on both sides; numerator/denominator never under different cuts
- ✅ **Consumer chase in Tier A** — §8 Tier A lists it explicitly, "not Tier B," per the round-1 adjudication

---

> **PASS — zero substantive residue remains.** Both amendments close their original failure modes as specified by the round-2 memos, neither introduces a new problem, and all eight line residues are applied. Both files await only the bar (§11 / decision g), which is Ben's by design.

No files were edited.
