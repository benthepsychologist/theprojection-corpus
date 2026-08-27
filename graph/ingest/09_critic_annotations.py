#!/usr/bin/env python3
"""Step 9 (F0): coverage-log.md misses -> extraction_review annotations
(graph/DESIGN.md §8.9). A **Missed:** finding is a process fact about our
OWN sweep, not first-hand data about the world -- no observation atoms
here (withdrawn in the design review). One extraction_pass per critic
pass (### <lens> / <date> section); where a **Map effect:** line names a
thread in backticks and that thread has a claim dated at or within 2 days
of the section date, an extraction_review annotation targets it
(justification = the Missed text). Where no claim can be identified
(most sections: "nothing that clears the bar", or Map effect names no
thread), the finding stays in the extraction_pass's own meta -- a process
outcome with nothing to annotate, per the design's own allowance. Only
13 real **Missed:** findings exist across the whole log; this is
deliberately conservative rather than fuzzy-matched.
"""
import datetime as dt
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
ORIGIN = "graph/ingest/09_critic_annotations.py, 2026-08-27"

def slug(s): return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
def base(kind, idf, idv, name):
    return {"kind": kind, idf: idv, "version": VER, "name": name, "data_domain": DOMAIN, "sensitivity": SENS}

def read(fname):
    p = os.path.join(GRAPH, fname)
    return [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []
def write(fname, rows):
    with open(os.path.join(GRAPH, fname), "w") as f:
        for r in rows: f.write(json.dumps(r, sort_keys=True) + "\n")

atoms = read("atoms.jsonl")
annos = read("annotations.jsonl")
passes = read("extraction_passes.jsonl")
pass_ids = {p["extraction_pass_id"] for p in passes}
ann_ids = {a["annotation_id"] for a in annos}

by_thread_date = {}
for a in atoms:
    if a.get("atom_type") != "claim":
        continue
    for t in a.get("meta", {}).get("thread", []) or []:
        try:
            d = dt.date.fromisoformat(a.get("valid_from", ""))
        except (ValueError, TypeError):
            continue
        by_thread_date.setdefault(t, []).append((d, a["knowledge_atom_id"]))

def nearest_claim(thread, section_date):
    cands = by_thread_date.get(thread, [])
    if not cands:
        return None
    try:
        target = dt.date.fromisoformat(section_date)
    except ValueError:
        return None
    best = min(cands, key=lambda c: abs((c[0] - target).days))
    return best[1] if abs((best[0] - target).days) <= 2 else None

SECTION_RE = re.compile(r"^### (\S[\w-]*) / (\d{4}-\d{2}-\d{2})\s*$", re.M)
BACKTICK_RE = re.compile(r"`([a-z0-9][a-z0-9-]*)`")

text = open(os.path.join(REPO, "coverage-log.md")).read()
sections = list(SECTION_RE.finditer(text))
new_annos, new_passes = [], []
annotated, no_target = 0, 0

for i, sec in enumerate(sections):
    lens, day = sec.group(1), sec.group(2)
    body = text[sec.end(): sections[i + 1].start() if i + 1 < len(sections) else len(text)]
    m_missed = re.search(r"\*\*Missed:\*\*\s*(.+?)(?=\n- \*\*|\n\n|\Z)", body, re.S)
    if not m_missed:
        continue
    missed_text = " ".join(m_missed.group(1).split())
    if re.match(r"(?i)^nothing\b", missed_text):
        continue  # "nothing that clears the bar" etc -- not a real miss

    pid = "ep-critic-" + slug(f"{lens}-{day}")
    if pid not in pass_ids:
        p = base("extraction_pass", "extraction_pass_id", pid, f"coverage-critic pass, {lens} {day}")
        p.update({"pass_type": "C1", "pass_iteration": 1, "pass_mode": "merge",
                  "agent_identity": "pipeline-daily-critic", "methodology_version": "attention-coverage-critic",
                  "source_target_refs": ["source:unspecified-timeline-tag"],
                  "meta": {"lens": lens, "date": day, "missed": missed_text, "origin": ORIGIN}})
        new_passes.append(p); pass_ids.add(pid)

    m_effect = re.search(r"\*\*Map effect:\*\*\s*(.+?)(?=\n- \*\*|\n\n|\Z)", body, re.S)
    target_claim = None
    if m_effect:
        for thread in BACKTICK_RE.findall(m_effect.group(1)):
            target_claim = nearest_claim(thread, day)
            if target_claim:
                break

    aid = "ann-critic-" + slug(f"{lens}-{day}")
    if aid in ann_ids:
        continue
    if target_claim:
        an = base("annotation", "annotation_id", aid, f"coverage-critic finding, {lens} {day}")
        an.update({"annotation_type": "extraction_review", "target_ref": f"knowledge_atom:{target_claim}",
                    "generated_by_ref": f"extraction_pass:{pid}", "justification": missed_text,
                    "extraction_confidence": "medium"})
        new_annos.append(an); ann_ids.add(aid)
        annotated += 1
    else:
        no_target += 1  # finding stays in the extraction_pass's own meta only

write("annotations.jsonl", annos + new_annos)
write("extraction_passes.jsonl", passes + new_passes)
print(f"{len(new_passes)} critic extraction_pass(es), {annotated} annotated to a specific claim, "
      f"{no_target} recorded as process outcome only (no identifiable claim)")
