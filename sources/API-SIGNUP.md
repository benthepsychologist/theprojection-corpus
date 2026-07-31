# API signup boilerplate (canonical — reuse verbatim)

**Contact / signup email:** ben@getmensio.com
**Declared User-Agent:** `kestrel/0.1 (personal research; ben@getmensio.com)`

## Use Case (standard)

A personal, non-commercial research and monitoring tool ("kestrel") built
and operated by an individual — a Canada-based clinical psychologist —
tracking developments at the intersection of AI, mental health care, and
capital markets. The tool runs low-volume, scheduled (roughly
daily-to-weekly) automated queries against public data sources to maintain
a personal intelligence notebook: it buffers small result sets, keeps
provenance records of every fetch, and never bulk-harvests or
redistributes source datasets. Selected findings are summarized, with
attribution and links back to the original source, on a small public
research site (theprojection.org); the tool itself is open source
(github.com/benthepsychologist/kestrel). All API interactions respect
documented rate limits, identify themselves with a contact User-Agent,
and cache results to minimize repeat queries.

## Use Case (short field)

Personal non-commercial research tool: low-volume scheduled monitoring of
AI / mental-health / finance developments for an attributed public
research notebook (theprojection.org). Open source, rate-limit-respecting,
contact ben@getmensio.com.

## Standard answers (used for LegiScan 2026-07-28; adapt per form)

- **Volume:** vertical topic areas, a few hundred items of interest —
  never "everything."
- **Query strategy:** weekly cadence, fixed keyword sets, change-hash /
  cache discipline so unchanged records are never re-fetched; expected
  usage a small fraction of any stated limit.
- **Agentic coding:** yes — LLM-assisted (Anthropic's Claude),
  human-reviewed, custom lightweight stdlib clients (no third-party
  client, no bulk SQL mirror).
- **Licensing:** attribution terms (e.g. CC BY 4.0) understood and
  honored — published output carries source attribution + links;
  stored data retains provenance.
