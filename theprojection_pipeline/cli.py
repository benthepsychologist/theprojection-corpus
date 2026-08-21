#!/usr/bin/env python3
"""theprojection_pipeline.cli — this corpus's own surfaces.

    theprojection <verb> [...]

These render THIS repo's pages. They lived in kestrel until 2026-08-21,
which was always slightly wrong and became clearly wrong once kestrel was
ruled "the agent monitor": a consumer map across all seven repos found
**zero** callers outside this one. They are the corpus's product, not the
engine's capability and not the research seat's — gathering moved to
`cloud-researcher`, rendering came here.
"""

from __future__ import annotations

import importlib
import sys

VERBS = {
    "readouts":         ("theprojection_pipeline.readouts", "briefing/readout extraction"),
    "render-read":      ("theprojection_pipeline.render_read", "render the attention read surface"),
    "world-news":       ("theprojection_pipeline.world_news", "world-news clustering and ranking"),
    "build-world-news": ("theprojection_pipeline.build_world_news", "build the world-news surface"),
    "thumbnails":       ("theprojection_pipeline.thumbnails", "per-article thumbnail capture"),
}


def _usage() -> str:
    w = max(len(v) for v in VERBS) + 2
    out = ["theprojection — this corpus's own read/digest surfaces", "",
           "  theprojection <verb> [...]", ""]
    for v, (_m, s) in VERBS.items():
        out.append(f"  {v:<{w}} {s}")
    out += ["",
            "Gathering lives in `cloud-researcher` (collect, tend); fleet",
            "administration lives in `kestrel` (fleet status, install)."]
    return "\n".join(out)


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(_usage()); return 0
    verb, rest = argv[0], argv[1:]
    if verb not in VERBS:
        print(f"[theprojection] unknown verb {verb!r}.\n\n{_usage()}", file=sys.stderr)
        return 2
    module_path, _ = VERBS[verb]
    module = importlib.import_module(module_path)
    entry = getattr(module, "main", None)
    if entry is None:
        print(f"[theprojection] {module_path} defines no main()", file=sys.stderr)
        return 2
    # argv via sys.argv, not as a parameter: these modules parse it
    # themselves and their main() signatures are not uniform. Learned the
    # hard way on cloud-researcher's dispatcher the same night.
    sys.argv = [f"theprojection {verb}"] + rest
    return entry() or 0


if __name__ == "__main__":
    raise SystemExit(main())
