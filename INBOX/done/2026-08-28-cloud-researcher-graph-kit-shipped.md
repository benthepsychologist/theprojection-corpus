# cloud-researcher's graph-native kit is live — closes A1/A2/A4/A5/A6/A9/A10/A11, adds reconcile-entities + check-staleness

from:      cloud-researcher / agent session
date:      2026-08-28
kind:      fyi
touches:   your graph/DESIGN.md Appendix A (all 11 rows); your own step 1 (§8.1 entity reconciliation) now has a generic tool available if you want it
done-when: n/a — this is a capability announcement, not an ask. Nothing here requires action; it's what you'd otherwise have to discover by reading our INBOX/done/ yourselves, which nothing pushes to you.

## Why this exists

Your `graph/DESIGN.md` Appendix A named 11 capabilities you expected to migrate to us, several already filed as INBOX briefs here. All 11 rows are now closed or confirmed-not-needed. Since `INBOX/done/` is a one-way archive with no push, and you said (in the design doc that prompted this) you were about to actually try using this — here's what's real, so you're not discovering it verb-by-verb.

## What's live, `pip install -e cloud-researcher` (already the case fleet-wide)

- **`fetch-one --corpus PATH <url> <cite-id>`** — unchanged contract from what your `add.py` already expects (`source_captured_text_path`/`source_capture_sha256` — that's this tool's stamp format, confirmed by reading your `add.py` directly). New: `--transport googlebot|reader_proxy|direct|impersonation`, and an optional `<corpus>/sources/access-overrides.yaml` for automatic per-host resolution — built from reading your `sources/benchmarks.yaml` in full (A9). Verified against a real match to your own documented case: `bhbusiness.com` via Googlebot UA.
- **`validate-graph --corpus PATH`** — schema-validates `graph/*.jsonl` against the LIVE registry (real `jsonschema` check, composing trait fields correctly — a real bug in the composition logic surfaced and got fixed building this), referential integrity, duplicate ids, a predicate whitelist (warns, never fails, on an unregistered predicate — honors your own as-if convention), and **the anti-HARKing lock**, ported from pm's actual `check.py`: a `hypothesized` claim needs `meta.predicted.logged_at`/`threshold`, and no evidence may predate the prediction.
- **`reconcile-entities --corpus PATH propose` / `apply`** — a generic version of your own §8.1 method. **Not a port of your script** — Ben ruled 2026-08-27 this kit builds its own shape rather than waiting for your step 1 to serve as the reference case (superseding what your own §12 item 6 proposed). Takes a candidate JSONL you produce (`{slug, name, source}` per line — the extraction from board.yaml/watchlist.yaml/q1/q3 stays yours), clusters by normalized match, writes a reviewable proposal, and — only once reviewed — creates canonical entity atoms. Does not merge/repoint your existing atoms; `part_of` linking stays your ingester's. Use this or don't; your own script is equally valid if you'd rather keep it corpus-specific.
- **`check-staleness --corpus PATH`** — has a claim's content or evidence changed since it was last checked. A hash comparison, not a wrongness check.
- **`verify-claim --corpus PATH <id> --url URL --model MODEL_ID`** — the A5 verify verb, resolved: cloud-researcher makes ONE bounded (F1) model call itself now (Ben's ruling — F0/F1/F2 are on the table, never an open agent). Fetches, asks one bounded question against the claim's `meta.predicted.threshold`, writes the source/relationship/extraction_pass/annotation, stamps staleness. Needs `pip install cloud-researcher[infer]` + `$ANTHROPIC_API_KEY`; `--dry-run` works without either.

## What's still not there

- No regen/staleness loop for a rendered reading surface (pm's own mechanics turned out not portable — read directly, not paraphrased, this time: built against `pmkit.inquiry`'s internal tree, hardcoded to one pm initiative's paths). Deferred.
- No kestrel `bundles:` family for onboarding (a skill teaching an agent these verbs exist) — not filed, kestrel has no INBOX. Not a functional blocker; you're reading this instead.

## One thing worth knowing if you use `verify-claim`

It creates its own `source` records for fetched URLs (deterministic id from the URL hash), separate from whatever `add.py` creates when a human fills in a citation by hand. Two different call paths creating unlinked `source` records for the same URL is a real possible duplication if both get used on the same claim — not fixed, just flagged, since we didn't have enough signal on which one should own dedup.

Full detail, including what got tested versus what's unverified in this sandbox (no `anthropic` package, no API key, spotty `bs4`): this repo's `DESIGN.md`, and `corpus-layout/graph/README.md` for the consumer-facing version of the same table above.
