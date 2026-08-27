#!/usr/bin/env python3
"""Step 6 (F0): artifacts/threads/*.md timeline entries -> S2 claims
(graph/DESIGN.md §8.6). Runs after step 7 by design (§11).

REVISED after the first run: matching by slugify(bold-lead)+date, the key
step 7 uses for its own cross-posted-bullet dedup, does NOT work here --
audited before trusting it (only 232 of ~1700 timeline bullets matched an
S1 atom; checking why showed most of the "new" ones fell inside the
digest-covered date range anyway, meaning the text itself differs: a
timeline entry is often a reworded/condensed rewrite of its source
digest bullet, not a verbatim copy, so text-slug matching silently
missed real matches rather than correctly finding none.

Fixed match key: (thread_slug, date) instead of text. A digest bullet
already carries `t=<thread-slug>` in meta.thread and `valid_from`=its
digest day; a timeline entry is authored under exactly one thread file
and one section date. If exactly one S1 claim already has this thread in
its meta.thread AND this date as valid_from, that's the same underlying
fact -- bump it to S2, don't duplicate. Two or more same-day claims on
one thread (a thread can log more than one fact per day) are left
UNMATCHED and created fresh rather than guessed at from text -- real
ambiguity, not silently resolved.

Skips spine actions (Thread opened/Promoted/Retired/Merged -- watch
history, not propositions) per §8.6. `## <- Backstory` entries ARE
ingested (past facts), tagged meta.backstory:true. `<verb date>` tag ->
one extraction_pass per distinct (verb, date) pair, reused across every
bullet citing it that run.
"""
import glob, hashlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
ORIGIN = "graph/ingest/06_timelines.py, 2026-08-27"

SPINE_LEADS = re.compile(r"^(Thread opened|Promoted|Retired|Merged)\b", re.I)
SECTION_RE = re.compile(r"^## (.+?)$", re.M)
BULLET_RE = re.compile(r"^- (.+?)(?=\n- |\n## |\Z)", re.M | re.S)
BOLD_RE = re.compile(r"^[^*\n]{0,6}\*\*(.+?)\*\*", re.S)
TAG_RE = re.compile(r"⟨(\w+)\s+(\d{4}-\d{2}-\d{2})⟩")
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

def slug(s): return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
def rel_id(s, p, t): return "rel-" + slug(f"{s}:{p}:{t}")
def rel_name(s, p, t):
    b = lambda r: r.split(":", 1)[1]
    return f"{b(s)}:{p}:{b(t)}"
def base(kind, idf, idv, name):
    return {"kind": kind, idf: idv, "version": VER, "name": name, "data_domain": DOMAIN, "sensitivity": SENS}

def read(fname):
    p = os.path.join(GRAPH, fname)
    return [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []
def write(fname, rows):
    with open(os.path.join(GRAPH, fname), "w") as f:
        for r in rows: f.write(json.dumps(r, sort_keys=True) + "\n")

atoms = read("atoms.jsonl")
sources = read("sources.jsonl")
rels = read("relationships.jsonl")
annos = read("annotations.jsonl")
passes = read("extraction_passes.jsonl")
atom_ids = {a["knowledge_atom_id"] for a in atoms}
rel_ids = {r["relationship_id"] for r in rels}
src_by_url = {s.get("locator"): s["source_id"] for s in sources if s.get("locator")}
pass_by_key = {(p["meta"]["verb"], p["meta"]["date"]): p["extraction_pass_id"]
               for p in passes if p.get("meta", {}).get("verb")}

# (thread, date) -> [S1 claim ids] -- the real match key, built ONLY from
# step 7's own output (excludes this script's own prior atoms), so the
# printed diagnostics stay stable across re-runs even though a re-run
# would otherwise see its own previously-created claims as candidates too.
# The written output was already idempotent either way; this only fixes
# what the console reports.
by_thread_date = {}
for a in atoms:
    if a.get("atom_type") != "claim" or a.get("meta", {}).get("origin") == ORIGIN:
        continue
    for t in a.get("meta", {}).get("thread", []) or []:
        by_thread_date.setdefault((t, a.get("valid_from")), []).append(a["knowledge_atom_id"])

bumped, created, skipped_spine, no_bold, no_tag, ambiguous = 0, 0, 0, 0, 0, 0

for path in sorted(glob.glob(os.path.join(REPO, "artifacts/threads/*.md"))):
    thread_slug = os.path.splitext(os.path.basename(path))[0]
    text = open(path).read()
    # walk section-by-section so a bullet's date comes from ITS OWN section header
    sections = list(SECTION_RE.finditer(text))
    for i, sec in enumerate(sections):
        header = sec.group(1)
        is_backstory = "backstory" in header.lower()
        m = DATE_RE.search(header)
        sec_date = m.group(1) if m else None
        body_start = sec.end()
        body_end = sections[i + 1].start() if i + 1 < len(sections) else len(text)
        section_text = text[body_start:body_end]

        for bm in BULLET_RE.finditer(section_text):
            raw = bm.group(1).rstrip()
            bold = BOLD_RE.search(raw)
            if not bold:
                no_bold += 1
                continue
            title = bold.group(1).strip()
            if SPINE_LEADS.match(title):
                skipped_spine += 1
                continue
            tag = TAG_RE.search(raw)
            if not tag:
                no_tag += 1
                continue
            verb, tag_date = tag.group(1), tag.group(2)
            day = sec_date or tag_date
            body = TAG_RE.sub("", raw)
            links = LINK_RE.findall(body)
            body = LINK_RE.sub("", body)
            body = re.sub(r"\(\s*,?\s*\)", "", body)  # empty parens left by stripped links
            body = " ".join(body.split())

            candidates = by_thread_date.get((thread_slug, day), [])
            existing = None
            if len(candidates) == 1:
                existing = next(a for a in atoms if a["knowledge_atom_id"] == candidates[0])
            elif len(candidates) > 1:
                ambiguous += 1  # real ambiguity (2+ S1 claims, same thread+day) -- create fresh, don't guess

            if existing:
                cid = existing["knowledge_atom_id"]
                if existing.get("formalization_stage") in (None, "S1"):
                    existing["formalization_stage"] = "S2"
                tl = existing["meta"].setdefault("timeline", [])
                if thread_slug not in tl:
                    tl.append(thread_slug)
                if is_backstory:
                    existing["meta"]["backstory"] = True
                bumped += 1
                cref = f"knowledge_atom:{cid}"
            else:
                cid = f"kat-claim-timeline-{slug(thread_slug)}-{day}-{slug(title[:50])}"
                if cid in atom_ids:
                    continue  # idempotency guard for the fresh-creation path
                c = base("knowledge_atom", "knowledge_atom_id", cid, title[:160])
                c.update({"atom_type": "claim", "label": title[:160], "summary": body[:280], "body": body,
                          "valid_from": day, "epistemic_status": "accepted", "source_process": "extraction",
                          "question": [],
                          "meta": {"timeline": [thread_slug], "thread": [thread_slug],
                                   "backstory": True if is_backstory else None, "origin": ORIGIN},
                          "formalization_stage": "S2", "lifecycle_status": "active", "sources": []})
                c["meta"] = {k: v for k, v in c["meta"].items() if v is not None}
                atoms.append(c); atom_ids.add(cid)
                created += 1
                cref = f"knowledge_atom:{cid}"
                for label, url in links:
                    sid = src_by_url.get(url)
                    if not sid:
                        h = hashlib.sha1(url.encode()).hexdigest()[:10]
                        sid = "src-timeline-" + slug(label)[:40] + "-" + h
                        s = base("source", "source_id", sid, label)
                        s.update({"source_type": "web_page", "title": label, "locator": url,
                                   "published_at": day, "evidence_class": "published_document",
                                   "meta": {"origin": ORIGIN}})
                        sources.append(s); src_by_url[url] = sid
                    c["sources"].append(sid)
                    rid = rel_id(f"source:{sid}", "supports", cref)
                    if rid not in rel_ids:
                        r = base("relationship", "relationship_id", rid, rel_name(f"source:{sid}", "supports", cref))
                        r.update({"source_ref": f"source:{sid}", "target_ref": cref, "predicate_id": "supports",
                                   "evidence_class": "published_document", "review_status": "unreviewed"})
                        rels.append(r); rel_ids.add(rid)

            # extraction_pass per (verb, date), reused across every bullet citing it
            pkey = (verb, tag_date)
            if pkey not in pass_by_key:
                pid = "ep-" + slug(f"{verb}-{tag_date}")
                p = base("extraction_pass", "extraction_pass_id", pid, f"{verb} {tag_date}")
                p.update({"pass_type": "A5", "pass_iteration": 1, "pass_mode": "merge",
                          "agent_identity": f"pipeline-{verb}", "methodology_version": "attention-pipeline",
                          "source_target_refs": [f"source:{s}" for s in ([] if not links else [src_by_url.get(links[0][1])]) if s] or ["source:unspecified-timeline-tag"],
                          "meta": {"verb": verb, "date": tag_date}})
                passes.append(p); pass_by_key[pkey] = pid
            ann_id = "ann-timeline-" + slug(f"{thread_slug}-{cid}")[:70]
            if ann_id not in {a["annotation_id"] for a in annos}:
                an = base("annotation", "annotation_id", ann_id, f"timeline entry provenance for {cid}")
                an.update({"annotation_type": "extraction_provenance", "target_ref": cref,
                            "generated_by_ref": f"extraction_pass:{pass_by_key[pkey]}"})
                annos.append(an)

write("atoms.jsonl", atoms); write("sources.jsonl", sources); write("relationships.jsonl", rels)
write("annotations.jsonl", annos); write("extraction_passes.jsonl", passes)
print(f"{bumped} bullet(s) matched an existing S1 atom by (thread,date) (bumped to S2), "
      f"{created} new S2 claim(s), {ambiguous} genuinely ambiguous (2+ same-day S1 claims on one thread, created fresh), "
      f"{skipped_spine} spine-action bullet(s) skipped, {no_bold} with no bold lead, {no_tag} with no <verb date> tag")
