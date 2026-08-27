#!/usr/bin/env python3
"""Step 7 (F0): digest bullets -> S1 claims (graph/DESIGN.md §8.7). Ruled in
(Ben, 2026-08-27). Reuses render_read.py's own parse_digest() regexes
VERBATIM rather than re-deriving them, since they're the parser this
repo's own site pipeline already trusts.

Scope, exactly as designed: status:final only (a `building` digest's text
can still change, which would mean a duplicate atom later); skip *-front.md
(composition over the lens digests, its bullets duplicate them) and
weekly/ (composition, not S1 source material).

Dedupe key (graph/DESIGN.md §7): slugify(bold-lead[:50]) + date. Lens is
NOT in the key -- a bullet cross-posted to two lens digests with an
identical lead is one atom with lens:[a,b]; confirmed to actually occur
by checking the front digest cross-references two lenses' items already.

`question` facet derives from lens per §12.1's stated interim (threads
don't carry a question pointer yet): ai->[q1,q5], global-capital->[q2,q7],
mental-health->[q3,q4,q6], world-news->[] (radar has no dedicated news
question by design). Marked question_derived:true so a later real mapping
(via threads.yaml once it carries `questions:`) is a known, findable
overwrite, not silently indistinguishable from a real assignment.

`about` uses the e= tag's watchlist slugs DIRECTLY (already the exact
entity slug the tag was authored with) -- no fuzzy substring matching
needed or wanted here, unlike interp/q3 where no such tag exists.
"""
import glob, hashlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.dirname(HERE)
REPO = os.path.dirname(GRAPH)
DOMAIN, SENS, VER = "knowledge", "internal", "1.0.0"
ORIGIN = "graph/ingest/07_digest_bullets.py, 2026-08-27"

QUESTION_BY_LENS = {"ai": ["q1", "q5"], "global-capital": ["q2", "q7"],
                     "mental-health": ["q3", "q4", "q6"], "world-news": []}

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
atom_ids = {a["knowledge_atom_id"] for a in atoms}
rel_ids = {r["relationship_id"] for r in rels}
src_by_url = {s.get("locator"): s["source_id"] for s in sources if s.get("locator")}
entity_by_slug = {a["meta"]["entity_slug"]: a for a in atoms
                  if a.get("atom_type") == "entity" and a.get("meta", {}).get("entity_slug")}

TRAILING_LINKS = re.compile(r"\s*\(\[[^\]]+\]\(https?://[^)\s]+\)(?:,\s*\[[^\]]+\]\(https?://[^)\s]+\))*\)\s*$")

# BULLET regex verbatim from theprojection_pipeline/render_read.py:317-319
BULLET_RE = re.compile(r"^- ((?:(?!^- )(?!^#).)+?)\n  <!-- k: ([^>]*?) -->", re.S | re.M)
TITLE_RE = re.compile(r"^[^*\n]{0,6}\*\*(.+?)\*\*", re.S)
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")

created, skipped_existing, no_title = 0, 0, 0
files_processed = 0
new_atoms, new_sources, new_rels = [], [], []

for path in sorted(glob.glob(os.path.join(REPO, "artifacts/digests/daily/*.md"))):
    fname = os.path.basename(path)
    if fname.endswith("-front.md"):
        continue
    text = open(path).read()
    fm_match = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not fm_match or "status: final" not in fm_match.group(1):
        continue
    m_lens = re.search(r"^lens:\s*(\S+)", fm_match.group(1), re.M)
    m_date = re.search(r"^date:\s*(\S+)", fm_match.group(1), re.M)
    if not m_lens or not m_date:
        continue
    lens, day = m_lens.group(1), m_date.group(1)
    files_processed += 1

    for b in BULLET_RE.finditer(text):
        raw_text = " ".join(l.strip() for l in b.group(1).strip().split("\n"))
        ann = b.group(2).strip()
        tags = dict(kv.split("=", 1) for kv in ann.split() if "=" in kv)
        tm = TITLE_RE.search(raw_text)
        if not tm:
            no_title += 1
            continue
        title = tm.group(1).strip()
        key = slug(title[:50]) + "--" + day
        cid = f"kat-claim-digest-{key}"
        body = TRAILING_LINKS.sub("", raw_text).strip()
        links = LINK_RE.findall(raw_text)
        threads = [t for t in (tags.get("t", "").split(",")) if t]
        entities = [e for e in (tags.get("e", "").split(",")) if e]
        axis = tags.get("axis", "")
        question = QUESTION_BY_LENS.get(lens, [])

        if cid in atom_ids:
            # cross-posted to another lens digest: merge lens/question, don't duplicate
            existing = next(a for a in atoms + new_atoms if a["knowledge_atom_id"] == cid)
            if lens not in existing["meta"].get("lens", []):
                existing["meta"]["lens"] = sorted(set(existing["meta"].get("lens", []) + [lens]))
                existing["question"] = sorted(set(existing.get("question", []) + question))
                existing["meta"]["digest"] = sorted(set(
                    (existing["meta"]["digest"] if isinstance(existing["meta"]["digest"], list) else [existing["meta"]["digest"]])
                    + [fname]))
            skipped_existing += 1
            continue

        c = base("knowledge_atom", "knowledge_atom_id", cid, title[:160])
        c.update({"atom_type": "claim", "label": title[:160], "summary": body[:280], "body": body,
                  "valid_from": day, "epistemic_status": "accepted", "source_process": "extraction",
                  "question": question,
                  "meta": {k: v for k, v in {
                      "thread": threads or None, "axis": axis or None, "digest": [fname],
                      "lens": [lens], "question_derived": True if question else None,
                      "origin": ORIGIN}.items() if v is not None},
                  "formalization_stage": "S1", "lifecycle_status": "active", "sources": []})
        new_atoms.append(c); atom_ids.add(cid)
        created += 1
        cref = f"knowledge_atom:{cid}"

        for eslug in entities:
            ent = entity_by_slug.get(eslug)
            if not ent:
                continue
            eref = f"knowledge_atom:{ent['knowledge_atom_id']}"
            rid = rel_id(cref, "about", eref)
            if rid not in rel_ids:
                r = base("relationship", "relationship_id", rid, rel_name(cref, "about", eref))
                r.update({"source_ref": cref, "target_ref": eref, "predicate_id": "about",
                          "qualifiers": {"role": "subject"}, "review_status": "unreviewed"})
                new_rels.append(r); rel_ids.add(rid)

        for label, url in links:
            sid = src_by_url.get(url)
            if not sid:
                h = hashlib.sha1(url.encode()).hexdigest()[:10]
                sid = "src-digest-" + slug(label)[:40] + "-" + h
                s = base("source", "source_id", sid, label)
                s.update({"source_type": "web_page", "title": label, "locator": url,
                           "published_at": day, "evidence_class": "published_document",
                           "meta": {"origin": ORIGIN}})
                new_sources.append(s); src_by_url[url] = sid
            c["sources"].append(sid)
            rid = rel_id(f"source:{sid}", "supports", cref)
            if rid not in rel_ids:
                r = base("relationship", "relationship_id", rid, rel_name(f"source:{sid}", "supports", cref))
                r.update({"source_ref": f"source:{sid}", "target_ref": cref, "predicate_id": "supports",
                          "evidence_class": "published_document", "review_status": "unreviewed"})
                new_rels.append(r); rel_ids.add(rid)

write("atoms.jsonl", atoms + new_atoms)
write("sources.jsonl", sources + new_sources)
write("relationships.jsonl", rels + new_rels)
print(f"{files_processed} final digest file(s) processed; {created} new S1 claim(s), "
      f"{skipped_existing} cross-posted merge(s), {no_title} bullet(s) with no bold-lead title (skipped)")
