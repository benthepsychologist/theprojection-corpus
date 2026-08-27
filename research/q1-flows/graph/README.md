# research/q1-flows/graph/ — the authoritative Q1 money-flow graph

**This directory, not the YAML files one level up, is the live source of
truth for Q1 as of 2026-08-27.** `../nodes.yaml`, `../edges.yaml`, and
`../memberships.yaml` are frozen (see their own headers) — kept as a
safety net and historical record for a couple of `/week` cycles, then
retired. Nothing operational reads them anymore.

## What's here

AKM-shaped (`lifeos-registry`'s knowledge_atom/source/relationship/
annotation/extraction_pass model), one JSONL file per kind, one JSON object
per line:

| file | what it holds |
| --- | --- |
| `atoms.jsonl` | entity atoms, event atoms (financing rounds), claim atoms (one per financing observation) |
| `sources.jsonl` | one row per real, distinct citation |
| `relationships.jsonl` | `about` (claim→entity), `funds` (entity→entity, materialized from the current claim), `member_of` (investor→round), `supports` (source→claim), and the mechanically-detected `has_part`/`qualifies`/`conflicts_with` cluster |
| `annotations.jsonl` | extraction provenance — why each claim was created from its source, one per claim |
| `extraction_passes.jsonl` | the process record of who/what captured each source and when |

`schemas/q1-local-vocab.md` documents `flow_type` and `destination_category`
— fields AKM has no home for, kept local per pm's own `schemas/akm-proposed/`
convention, versioned and explicitly marked divergent.

## Why this exists — the short version

Full findings: `../akm-tinkerspace/FINDINGS.md` (the experiment that proved
this was buildable) and this repo's `AGENTS.md` discipline 1 (the
mechanization ladder this whole migration was designed against). In brief:
AKM's `source`→`supports`→`annotation` factoring genuinely replaces the old
`observations: [...]` list with no loss, and its predicate vocabulary
(`has_part`, `qualifies`, `conflicts_with`, `supersedes`) turned out to
already have the right names for a real ambiguity the flat YAML couldn't
express — a second dollar figure on one flow could mean four different
things, and forcing all four through one field is what produced wrong
guesses in the migration experiment's first draft.

## `build_graph.py` — how this graph was seeded, once

A one-time, idempotent script that read the frozen YAML's 2026-08-27 state
and produced everything in this directory. **It is not meant to be re-run
against live data** — the YAML source is frozen, so re-running it just
reproduces the same graph byte-for-byte. Its docstring is the accurate
record of every judgment call made seeding this graph: which multi-amount
edges got `has_part` vs `qualifies` vs `conflicts_with` and why (mechanical,
not a keyword guess — see the script's own comments), which two
"inference from other claims" sources turned out to have real citations that
were mis-bucketed in the migration experiment's draft, and which two
genuinely had none and got `has_part` with no fabricated source instead.

## `add.py` — how new data goes in from here forward

**The seam.** `add_financing(...)` takes a fully-described, already-sourced
financing and does only the AKM-shape structuring — new entity atoms if
needed, a claim atom, `about`/`funds` relationships, and a
`source`/`supports`/`annotation`/`extraction_pass` set from whatever source
info it's handed. **It never fetches a URL and never classifies evidence
itself.**

Today, "already-sourced" means a research agent did a real WebSearch/
WebFetch and filled in the fields by hand — reliability, evidence class,
rationale — exactly as every Q1 research pass has done since the first one.
That's the honest, working, manual practice, and it stays the practice for
now.

**Where the fetch-and-classify step is supposed to live instead:**
`cloud-researcher` already has this built and it's better than anything
handwritten here — `fetch-one.py` (hash-stamped verbatim capture),
`fill-provenance.py` (a real, maintained host→evidence-class table),
`runlog.py` (an append-only, machine-written run ledger — the
`extraction_pass` concept, already running elsewhere). It just isn't reachable
from a consuming repo yet: no `--corpus` support on those tools, none of them
on the installed CLI, no `bundles:` declared in this repo's `kestrel.yaml`.
Filed as
`cloud-researcher/INBOX/2026-08-27-theprojection-corpus-verify-kit-not-reachable-from-consuming-repos.md`.
**The moment that's answered, only what fills in `add_financing`'s input
dict changes — nothing in `add.py` itself does.** That's the point of
keeping the fetch/verify concern strictly outside this file.

**Per-source capture granularity** (Ben, 2026-08-27): every call to
`add_financing` writes exactly one `extraction_pass`, covering exactly the
one source it was given — never a session-level marker covering many. This
is the discipline the frozen YAML's `capture_ref` never had (see the
extraction_pass cardinality finding in `../akm-tinkerspace/FINDINGS.md` §4b
and the round-three brief it produced). The historical seed in this
directory still carries the old, coarser session-level markers — honestly
labeled as such in each seeded `extraction_pass`'s `meta` — but everything
added via `add.py` from 2026-08-27 onward gets it right from the start.

## How `filters/cut-core-buildout.yaml` applies here — unchanged, by design

R-16 rules boundaries as filters over the map, never classification baked
into it. That file is untouched by this migration — it still lists bare
entity names (`anthropic`, `openai`, ...). Every entity atom in this graph
carries `meta.entity_slug` for exactly this purpose: to apply that filter,
match an atom's `entity_slug` against the filter's `members` list. No
predicate, no graph relationship, no atom in this graph "belongs to" a cut —
the map stays classification-free, exactly as ruled.

## Known limitation, stated rather than hidden

`build_graph.py`'s evidence-class assignment for the two "inference from
other claims" sources that turned out to have real citations (TSMC's
earnings-call transcript, Stargate's press relay) both landed on the generic
`published_document` default rather than a more precise class
(`testimony_interested` for the earnings call; `testimony_disinterested` for
the relay) — correct-but-imprecise, not wrong. Left as a known gap rather
than hand-tuned for two cases, since the real fix is `fill-provenance.py`'s
host-based classification table doing this properly once the cloud-researcher
gap above is resolved.
