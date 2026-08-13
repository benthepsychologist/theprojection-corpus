"""publish/adapter.py — the theprojection.org adapter: everything
site-specific for publish (kestrel ROADMAP/DESIGN.md §6). Instance-owned
code, not engine code — kestrel's tools/publish.py locates this file via
this repo's own kestrel.yaml `outputs.adapter` and loads it dynamically;
nothing about theprojection lives in the kestrel checkout anymore
(relocated 2026-07-31, out of tools/publish/adapters/theprojection.py —
same behavior, moved so the engine holds no per-site code at all). Page
inventory (threads, entities, beats, board/claims, interpretations, map
pages, readouts export), the payload assembly, and resolution of the
THEPROJECTION_SITE_DIR/THEPROJECTION_DEPLOY_HOOK env vars (the env NAMES
are declared here, per-site) are unchanged from the pre-move version.

Every thread publishes by default (Ben, 2026-07-22: "no private information
on here... I don't want to hand gate the feed"). Set `public: false` on a
thread in attention/threads.yaml to hold it back — an escape hatch, not a
gate. The allowlist that still applies is at the *field* level, not the
thread level: only hardcoded fields ever cross over (never `notes`, never
`terms`), and every export is secret-scanned as a mechanical backstop, not
an editorial one.

Ports the internal read's weekly-dashboard shape (Ben, 2026-07-22: "look at
the thing for claude" — throughlines, lens filters, active-threads-by-week,
entities, not-yet-a-thread items, map changes) — reuses render_read.py's
parsing (same digest/timeline format, just scrubbed and re-targeted at the
site repo instead of the internal artifact). render_read.py/thumbnails.py
are shared engine tooling (kestrel's tools/), importable here because
kestrel's tools/publish.py puts that directory on sys.path before loading
this module — this file does no path-finding of its own.
"""
import glob
import collections
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone

import yaml

from publish import core

# Instance root: this adapter reads this repo's own data (attention/,
# artifacts/, digests). Required, not defaulted — kestrel's tools/publish.py
# always sets KESTREL_INSTANCE before loading an adapter (AGENTS.md
# discipline 9: honest failure beats silent fallback).
ROOT = os.environ["KESTREL_INSTANCE"]

from render_read import (digest_day, load_entities as _load_watchlist_entities,  # noqa: E402
                         parse_digest, parse_front, load_flash, load_world_news)
from thumbnails import get_thumbnails  # noqa: E402

PLACEHOLDER_SLUG = "sample-placeholder"
LENS_OF_FILE = {"frontier-ai": "ai", "mental-health": "mental-health",
                 "global-capital": "global-capital", "world-news": "world-news"}
# "money" renamed to "global-capital" 2026-07-30 (Ben, full rename). Digests
# dated before the rename keep their historical "-money.md" filename and
# `lens: money` frontmatter — not rewritten; only the going-forward
# convention changed. render_read.py's own LENS_OF_FILE carries the same
# key so both readers agree on what to look for.

# Cloudflare Workers Builds deploy hook — not a full credential (it can only
# queue a build, not read anything), but it's still a live trigger against the
# site, so it's config, never a repo-committed default. Set via env var; if
# unset, --push just skips the auto-fire (see push_site()'s `if
# deploy_hook_url:`).
DEPLOY_HOOK_URL = os.environ.get("THEPROJECTION_DEPLOY_HOOK")

# Site checkout path — mirrors DEPLOY_HOOK_URL: a per-site env var this
# adapter resolves and hands to the CLI shim as the --site-dir default.
SITE_DIR = os.environ.get("THEPROJECTION_SITE_DIR")

# Audio-briefing generation (Ben, 2026-08-13: "an AUDIO briefing... this
# shouldn't run automatically in other repos... a local extension of the
# upstream protocol"). Deliberately NOT a kestrel engine feature — this
# whole block lives only in this instance-owned adapter, so no other
# kestrel instance (therapybulletin-data, etc.) is touched by it; each
# instance's own adapter.py would need to opt in separately if it wanted
# the same thing. The generator (sources/generate_audio_briefing.py)
# needs a dedicated venv with kokoro+soundfile installed
# (/workspace/.venvs/kokoro-tts, ~5.2GB — see that script's own docstring
# for why it's not the adapter's normal Python env) plus system
# espeak-ng/ffmpeg. Hardcoded rather than env-configurable for now,
# matching this adapter's existing style of hardcoding what's genuinely
# fixed about this one site (BEATS, LENS_OF_FILE) rather than adding
# config surface for a value that has exactly one correct answer today.
AUDIO_VENV_PYTHON = "/workspace/.venvs/kokoro-tts/bin/python3"
AUDIO_GEN_SCRIPT = os.path.join(ROOT, "sources", "generate_audio_briefing.py")

# Front-matter fields allowed across the boundary for a thread page. Nothing
# else from a threads.yaml entry — notably never `notes` (explicitly the
# internal running log per the schema header) or `terms` (query internals).
ALLOWED_THREAD_FIELDS = ("slug", "title", "lens", "status", "opened", "last_seen",
                          "weight", "entities", "parent")


def thread_blurb(t):
    raw = (t.get("public_blurb") or " ".join((t.get("watch") or "").split())).strip()
    # linkify=False: rendered by the site as plain escaped text ({{ . }} in
    # _default/single.html's .dek), not markdown — see clean_reader_facing_body's
    # docstring for why a real link would be wrong here.
    return clean_reader_facing_body(raw, linkify=False)


def load_threads_yaml():
    return yaml.safe_load(open(os.path.join(ROOT, "attention/threads.yaml")))["threads"]


def public_slugs(threads):
    return {t["slug"] for t in threads if t.get("public") is not False}


def strip_internal_header(body):
    """Drop the leading '# Title — timeline' H1 and its *Watch* paragraph —
    the site's front matter supplies title/blurb instead. Body starts at the
    first '## ' timeline entry."""
    m = re.search(r"^## ", body, re.M)
    return body[m.start():] if m else body


_PROVENANCE_MARKER = re.compile(
    # Started as a keyword+date allowlist (daily|crawl|seed|...); widened to
    # match ANY ⟨...⟩ span after a full sweep of every digest turned up 23
    # distinct real variants — free-text asides like ⟨overnight extension,
    # 08-04 05:40 ET⟩ and ⟨sourced this morning⟩, not just the strict
    # ⟨keyword YYYY-MM-DD⟩ form the thread-timeline template documents.
    # Verified none of the 23 are reader-facing content — ⟨ ⟩ (U+27E8/9) is
    # used nowhere in this corpus except as the provenance-aside delimiter.
    r"\s*⟨[^⟩]*⟩"
)
_CODE_SPAN = re.compile(r"`([^`]+)`")
_HTML_CODE_SPAN = re.compile(r"<code>([^<]+)</code>")
_SLUG_TITLE_CACHE = None


def _slug_title_map():
    """Lazily built, memoized: thread slug -> title, for resolving inline
    backtick cross-references. Reads threads.yaml once per publish run."""
    global _SLUG_TITLE_CACHE
    if _SLUG_TITLE_CACHE is None:
        _SLUG_TITLE_CACHE = {t["slug"]: t["title"] for t in load_threads_yaml()}
    return _SLUG_TITLE_CACHE


def clean_reader_facing_body(text, linkify=True, html_safe=False):
    """Two things leak from internal curation practice straight into public
    reader-facing prose, found on a 2026-08-09 site UX crawl: the
    `⟨daily YYYY-MM-DD⟩`-style provenance markers appended to nearly every
    timeline bullet (production metadata, zero reader value, never
    explained anywhere on the site — the five keywords here are every one
    actually in use across artifacts/threads/*.md, confirmed by grep, not
    guessed), and inline `` `thread-slug` `` cross-references rendered as
    raw monospace code with no link and no gloss. Fixed here, not by
    hand-editing artifacts/threads/*.md, because the markers ARE meant to
    stay in the internal timeline files (that's where provenance is a
    feature, not a bug) — this only touches what crosses the publish
    boundary into public prose.

    Provenance markers: stripped outright, they carry no public meaning.
    Backtick spans naming a known public thread slug: with `linkify=True`
    (the timeline body, which Hugo renders as markdown) turned into a real
    `[Title](/threads/slug/)` link. With `linkify=False` (the `blurb`
    front-matter field, which the site's `.dek` partial outputs as plain
    escaped text via `{{ . }}` — markdown syntax there would show up
    LITERALLY as bracket/paren text, not a link) resolved to just the
    plain title instead. Any other backtick span (curator shorthand like
    `sev=major`) is unwrapped to plain text in both modes — it reads fine
    as plain words once it's not styled as code the reader was never told
    how to interpret.

    A third case, orthogonal to `linkify`: `<code>slug</code>` spans —
    found 2026-08-09 on the "Items this week" list, whose `.html` field
    arrives PRE-RENDERED (kestrel's md_html() already turned a backtick
    span into a real `<code>` tag before this function ever sees the
    string). Only unwrapped to a real `<a href="/threads/slug/">Title</a>`
    tag when the CALLER explicitly passes `html_safe=True` — meaning the
    caller knows for certain this string is inserted via Hugo's `safeHTML`
    (raw HTML), not auto-escaped `{{ . }}` output, where an injected `<a>`
    tag would show up as literal angle-bracket text instead of a link.
    Deliberately NOT inferred from the tag's mere presence — right now
    every real `<code>` span in this corpus happens to come from an
    `html_safe` context, but that's an invariant about today's data, not
    a property of the string itself, so it isn't safe to assume silently.
    Without `html_safe`, a `<code>` span just unwraps to its plain content
    text (still fine to read, just not a link).
    """
    text = _PROVENANCE_MARKER.sub("", text)

    def _resolve_span(m):
        content = m.group(1)
        title = _slug_title_map().get(content)
        if not title:
            return content
        return f"[{title}](/threads/{content}/)" if linkify else title

    text = _CODE_SPAN.sub(_resolve_span, text)

    def _resolve_html_span(m):
        content = m.group(1)
        title = _slug_title_map().get(content)
        if not title:
            return content
        return f'<a href="/threads/{content}/">{title}</a>' if html_safe else title

    return _HTML_CODE_SPAN.sub(_resolve_html_span, text)


# The only dict key anywhere in this payload whose value is inserted via
# Hugo's safeHTML rather than auto-escaped {{ . }} — items' pre-rendered
# `.html` field (news/single.html, entities/single.html: `{{ .html |
# safeHTML }}`). _deep_clean_reader_facing passes html_safe=True ONLY for
# this key, so a resolved `<code>slug</code>` span becomes a real `<a>`
# link there and nowhere else — see clean_reader_facing_body's docstring
# for why that has to be explicit rather than inferred from the tag alone.
_HTML_SAFE_KEYS = {"html"}


def _deep_clean_reader_facing(value, html_safe=False):
    """Recursive sweep for the same leak, applied to a whole JSON-shaped
    structure at once. Landed 2026-08-09 after individually patching five
    separate fields (thread bodies, blurbs, map-changes, readout bullets,
    interpretation sub-fields) and still finding a sixth (throughlines) on
    the next sweep — chasing each field by name doesn't converge, because
    any string anywhere in this payload can carry one of these markers.

    Cheap and safe by construction: only strings actually CONTAINING '⟨', a
    backtick, or a `<code>` tag get touched (the three sub-patterns inside
    `clean_reader_facing_body` are no-ops on anything else), and none of
    those appear in this corpus's urls, slugs, ids, or dates — verified by
    grep, not assumed — so this can run unconditionally over every string
    in the structure with no per-field allowlist to maintain or forget.
    linkify is always False (nothing in this payload is markdown-rendered);
    html_safe defaults False too and is threaded through recursion only
    for keys in `_HTML_SAFE_KEYS` — everything else stays a plain-text
    unwrap even if a `<code>` tag somehow shows up somewhere unexpected.
    """
    if isinstance(value, str):
        if "⟨" in value or "`" in value or "<code>" in value:
            return clean_reader_facing_body(value, linkify=False, html_safe=html_safe)
        return value
    if isinstance(value, dict):
        return {k: _deep_clean_reader_facing(v, html_safe=(k in _HTML_SAFE_KEYS))
                for k, v in value.items()}
    if isinstance(value, list):
        return [_deep_clean_reader_facing(v, html_safe=html_safe) for v in value]
    return value


def build_thread_page(t):
    slug = t["slug"]
    path = os.path.join(ROOT, "artifacts/threads", f"{slug}.md")
    if not os.path.exists(path):
        return None, [f"no timeline artifact for public thread '{slug}' ({path})"]

    src = open(path).read()
    fm_match = re.match(r"---\n.*?\n---\n", src, re.S)
    body = src[fm_match.end():] if fm_match else src
    body = strip_internal_header(body).rstrip() + "\n"
    body = clean_reader_facing_body(body)

    fm = core.apply_allowlist(t, ALLOWED_THREAD_FIELDS)
    fm["thread_kind"] = t.get("kind", "story")
    fm["blurb"] = thread_blurb(t)
    title = fm.pop("title")
    slug_out = fm.pop("slug")

    errors = []
    scan_text = json.dumps(fm, default=str) + "\n" + title + "\n" + body
    errors += core.secret_scan(scan_text, f"thread '{slug}'")
    if errors:
        return None, errors

    front = "---\n" + yaml.safe_dump(
        {"title": title, **fm}, sort_keys=False, allow_unicode=True
    ).strip() + "\n---\n\n"
    return slug_out, front + body


def load_outlet_credibility():
    """domain -> credibility record, from sources/outlet-credibility.yaml.

    PUBLICATION CLEARED ben-steer 2026-08-11, verbatim: "outlet credibility
    can be public, no problem. even the stuff we're waiting to hear back on.
    It already says feel free to use it. We are oss on the web. We should
    feel free until we hear back. permission granted." That supersedes the
    keep-INTERNAL hold the file previously carried on `pc1`.

    Two attribution obligations travel WITH the data and are rendered by
    layouts/story/single.html, not optional:
      pc1 — Lin et al. 2023, PNAS Nexus 2(9):pgad286 (CC BY 4.0)
      rsp — Wikipedia perennial sources (CC BY-SA 4.0, attribution on render)
    """
    p = os.path.join(ROOT, "sources/outlet-credibility.yaml")
    if not os.path.exists(p):
        return {}
    return (yaml.safe_load(open(p)) or {}).get("domains", {}) or {}


def _source_domain(url):
    """Host of a source url, minus a leading `www.`.

    NOT `lstrip("www.")` — that strips any leading run of the CHARACTERS
    w/./, so washingtonpost.com became "ashingtonpost.com" and wired.com
    became "ired.com", and every w-initial domain silently missed its
    credibility lookup. Caught by eyeballing the unbadged-domain list.
    """
    m = re.match(r"https?://([^/]+)", url or "")
    if not m:
        return ""
    host = m.group(1).lower().split(":")[0]   # drop :port — `asiaone.com:443`
    return host[4:] if host.startswith("www.") else host


def build_stories(pub_slugs, threads_by_slug):
    """Every dated block in a published thread's timeline becomes a STORY.

    Ben, 2026-08-11, on clicking a briefing bullet and landing on a thread:
    "a non-intuitive UX leap… what I really want is a STORY page, that lists
    the story headline, a summary of the story and its coverage, and links to
    sources with the accuracy/credibility ratings we picked up."

    A THREAD is a narrative arc over time; a STORY is one event with many
    witnesses. Those are different objects and the site only had the first,
    so every story-level click had to resolve to the arc that contained it.

    v1 derives stories from the timeline rather than inventing a new curation
    artifact, which is what makes the backfill immediate — 520 dated blocks
    across 99 threads, 387 of them already carrying at least one source link
    (689 links, ~1.8 per sourced story). Sources are the block's own inline
    citations, badged from the outlet-credibility layer.

    Known v1 limits, deliberate and on the roadmap rather than hidden:
      - A story's source list is what CURATION CITED, not every outlet that
        covered it. The wider count exists (world-news.yaml clustered the
        Nvidia financing story at 54 distinct outlets) but keeps only five
        outlet NAMES and no urls, and most of that breadth arrives as
        google_news_rss redirect links rather than publisher domains — so a
        true master source list is v2 and needs redirect resolution.
      - A block with no inline citation yields a story with no sources. It
        still gets a page (the prose is the record) but says so plainly.
    """
    cred = load_outlet_credibility()
    stories, seen = [], {}
    for slug in sorted(pub_slugs):
        t = threads_by_slug.get(slug) or {}
        path = os.path.join(ROOT, "artifacts/threads", f"{slug}.md")
        if not os.path.exists(path):
            continue
        src = open(path).read()
        fm_match = re.match(r"---\n.*?\n---\n", src, re.S)
        body = src[fm_match.end():] if fm_match else src
        body = strip_internal_header(body)
        for block in re.split(r"^## ", body, flags=re.M)[1:]:
            head, _, rest = block.partition("\n")
            m = re.match(r"(\d{4}-\d{2}-\d{2})\s*(?:—|-|–)?\s*(.*)$", head.strip())
            if not m:
                continue                      # "← Backstory" and other dividers
            date, headline = m.group(1), (m.group(2) or "").strip()
            if not headline:
                headline = f"{t.get('title', slug)} — {date}"
            sid = f"{slug}--{date}"
            seen[sid] = seen.get(sid, 0) + 1
            if seen[sid] > 1:
                sid = f"{sid}-{seen[sid]}"    # two blocks share a date
            prose = clean_reader_facing_body(rest.strip(), html_safe=True)
            sources = []
            for label, url in re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", rest):
                if any(s["url"] == url for s in sources):
                    continue
                dom = _source_domain(url)
                c = cred.get(dom, {})
                # A google-news link is a REDIRECT, not a publisher — curation
                # is supposed to never cite one, but 45 made it into the
                # timelines historically. Flag rather than drop: the reader
                # should see that the citation doesn't resolve to an outlet,
                # and a silent drop would make a story look unsourced when it
                # is really mis-sourced. Nothing gets a credibility badge here
                # because the domain isn't the publisher's.
                redirect = dom in ("news.google.com", "google.com")
                sources.append({"url": url, "label": label.strip(), "domain": dom,
                                 "redirect": redirect,
                                 "pc1": None if redirect else c.get("pc1"),
                                 "band": None if redirect else c.get("band"),
                                 "rsp": None if redirect else c.get("rsp"),
                                 "class": None if redirect else c.get("class"),
                                 # layer 3 — published-practice COUNT, not a
                                 # score, and rendered on its own scale so it
                                 # can't be misread as a quality band
                                 "practices": None if redirect else c.get("practices"),
                                 "practices_of": None if redirect else c.get("practices_of")})
            stories.append({
                "id": sid, "headline": headline, "date": date,
                "thread": slug, "thread_title": t.get("title", slug),
                "lens": t.get("lens", ""), "html": prose, "sources": sources,
            })
    return stories


def build_payload(pub_slugs, today=None):
    """Assemble the weekly read payload — same shape render_read.py builds
    for the internal page, filtered to what's publishable. today defaults to
    the real digest-day (ET); pass a date for testing."""
    today = today or digest_day()
    week_start = today - timedelta(days=today.weekday())

    days, throughlines, items, map_changes = [], {}, [], []
    for i in range(7):
        d = week_start + timedelta(days=i)
        if d > today:
            break
        ds, found = d.isoformat(), False
        for fl, lens in LENS_OF_FILE.items():
            p = os.path.join(ROOT, "artifacts/digests/daily", f"{ds}-{fl}.md")
            if not os.path.exists(p):
                continue
            found = True
            thr, its, chg = parse_digest(p, ds, lens)
            if thr:
                throughlines.setdefault(ds, {})[lens] = thr
            items += its
            map_changes += chg
        fp = os.path.join(ROOT, "artifacts/digests/daily", f"{ds}-front.md")
        if os.path.exists(fp):
            front = parse_front(fp)
            if front:
                throughlines.setdefault(ds, {})["front"] = front
                found = True
        if found:
            days.append(ds)

    # Same today/now split the internal read uses (2026-07-29): `today`
    # centers the page on the newest CURATED day, `now` is the real
    # digest-day that imminence and calendar labels measure from. Without
    # this the site centers on an uncurated day and its top strip is blank.
    now = today
    if days and today.isoformat() not in days:
        today = datetime.strptime(days[-1], "%Y-%m-%d").date()

    # An item is publishable unless every thread it's tagged to is private.
    items = [it for it in items
             if not it.get("threads") or any(s in pub_slugs for s in it["threads"])]
    items = [{**it, "threads": [s for s in it.get("threads", []) if s in pub_slugs]}
             for it in items]

    # Real per-article thumbnails (og:image), best-effort — cached in
    # buffer/thumbnails.json so only genuinely new URLs get fetched each
    # run. A miss just means no `img` field; the frontend already falls
    # back to a favicon-on-gradient tile, never a broken image.
    thumbs = get_thumbnails([it.get("url") for it in items])
    items = [{**it, "img": thumbs.get(it.get("url"))} for it in items]

    threads_raw = load_threads_yaml()

    def timeline_depth(slug):
        # dated-entry count in the timeline artifact — the node pages'
        # depth signal (W6, 2026-07-28); 0 if no artifact yet
        tp = os.path.join(ROOT, "artifacts/threads", f"{slug}.md")
        if not os.path.exists(tp):
            return 0
        return len(re.findall(r"^## ", open(tp).read(), re.M))

    threads = [{"slug": t["slug"], "title": t["title"], "lens": t["lens"],
                "status": t.get("status", "developing"), "kind": t.get("kind", "story"),
                "weight": t.get("weight", 2), "opened": t.get("opened"),
                "last_seen": t.get("last_seen"), "entities": t.get("entities", []),
                "parent": t.get("parent"), "genre": t.get("genre"),
                "depth": timeline_depth(t["slug"]),
                "blurb": thread_blurb(t)}
               for t in threads_raw if t["slug"] in pub_slugs]

    # Expectations ledger: keep entries with no thread, or attached to a
    # public one. Never export logged_by/logged — internal bookkeeping.
    upc_path = os.path.join(ROOT, "attention/upcoming.yaml")
    upcoming = []
    if os.path.exists(upc_path):
        for u in yaml.safe_load(open(upc_path)).get("expectations", []):
            if u.get("thread") and u["thread"] not in pub_slugs:
                continue
            upcoming.append({k: u.get(k) for k in
                              ("id", "claim", "due", "thread", "entities",
                               "confidence", "what_confirms", "status")})

    # Entities: only what's actually referenced by public threads/items —
    # never the full private watchlist (that would leak everything Ben is
    # silently tracking, not just what he's published about).
    referenced = set()
    for t in threads:
        referenced.update(t.get("entities", []))
    for it in items:
        referenced.update(it.get("entities", []))
    for u in upcoming:
        referenced.update(u.get("entities") or [])
    all_entities = {e["slug"]: e for e in _load_watchlist_entities()}
    entities = core.referenced_only(referenced, all_entities)

    payload = {
        "schema_version": 1,
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "week_start": week_start.isoformat(), "today": today.isoformat(),
        "now": now.isoformat(), "days": days,
        "entities": entities, "threads": threads, "items": items,
        "throughlines": throughlines, "upcoming": upcoming, "map_changes": map_changes,
        "asks": [],  # not yet derived automatically — same gap the internal tool has
        # The flash rail publishes (Ben, 2026-07-29: "this is MY news feed
        # FIRST. If its big world news it affects finance so its cohesive").
        # Nothing in flash.yaml is private by construction, and it still
        # passes the allowlist + secret-scan like everything else.
        "flash": load_flash(now),
        # World News (ROADMAP §World News, Ben 2026-07-30) -- a mechanical
        # cross-spectrum volume fact, not editorial like flash. Nothing in
        # world-news.yaml is private by construction (it is headlines +
        # outlet names + a thread pointer), so it publishes the same way
        # flash does, still through the allowlist + secret-scan backstop.
        "world_news": load_world_news(now),
    }
    # 2026-08-09: strip the same provenance-marker/backtick-slug leak from
    # EVERY string in this payload at once — see _deep_clean_reader_facing's
    # docstring for why a per-field approach kept missing fields (items'
    # interpretation sub-object, throughlines, map_changes text all turned
    # up on successive sweeps before this replaced them).
    return _deep_clean_reader_facing(payload)


# Board fields allowed across the boundary. The board is neutral by
# construction (no `notes`, no secrets — the costume lives on the site), but
# it still passes the allowlist + secret-scan as a mechanical backstop, same
# as everything else. NEVER exports anything not named here.
ALLOWED_HOUSE_FIELDS = ("slug", "name", "gloss", "deployable", "deployable_asof",
                        "kind", "level")
ALLOWED_ORG_FIELDS = ("slug", "rank", "kind", "level", "parent", "pocket", "held_by",
                      "liege", "depends_on", "sphere",
                      "holdings", "posture", "condition", "succession", "gloss",
                      "commanded_capital", "thrust", "optionality", "gravity", "axes_asof",
                      "axes_num",
                      "tier", "double_dependent", "vassals-note", "armies", "mines")

# sphere -> the State node that a gov agency (regulator) sits under, for the
# rough parent-seed. Ambiguous spheres (gulf/jp/none) get no auto-parent.
SPHERE_STATE = {"us": "united-states", "china": "china", "eu": "european-union",
                "uk": "united-kingdom", "fr": "france"}

# Display names for board orgs that are NOT watchlist entities (states,
# regulators, the route layer) or whose entity name reads awkwardly. Names are
# surface, resolved in one place so the list + per-actor pages agree. Anything
# not here falls back to the watchlist entity name, then a humanized slug.
BOARD_ORG_NAMES = {
    "amazon-aws": "Amazon", "meta-ai": "Meta", "alibaba-qwen": "Alibaba",
    "spacex": "SpaceXAI", "microsoft-mai": "Microsoft MAI", "sk-hynix": "SK Hynix",
    "cxmt": "CXMT", "tsmc": "TSMC", "pif": "PIF", "mgx": "MGX", "nuhw": "NUHW",
    "silk-road": "The Silk Road", "united-states": "United States", "china": "China",
    "european-union": "European Union", "united-kingdom": "United Kingdom",
    "france": "France", "uae": "UAE", "saudi-arabia": "Saudi Arabia", "russia": "Russia",
    "us-state-legislatures": "US State Legislatures", "eu-ai-act": "EU AI Act",
    "proposed-sro": "Proposed SRO", "nsa-frontier-review": "NSA Frontier Review",
    "caisi": "CAISI", "fda": "FDA", "dmhc": "DMHC", "mhra": "MHRA",
    "kaiser-permanente": "Kaiser Permanente",
}


def build_board():
    """Export attention/board.yaml as the neutral power layer. Costume-free —
    the site's data/labels.yaml projects the vocabulary at render time. Houses
    get a derived `holds` (inversion of orgs' held_by; one source of truth
    stays on the org); orgs get a resolved display `name`."""
    b = yaml.safe_load(open(os.path.join(ROOT, "attention/board.yaml")))
    ent_names = {e["slug"]: e["name"] for e in _load_watchlist_entities()}
    houses = [core.apply_allowlist(h, ALLOWED_HOUSE_FIELDS) for h in b.get("houses", [])]
    orgs = [core.apply_allowlist(o, ALLOWED_ORG_FIELDS) for o in b.get("orgs", [])]
    # The synthesis layer — the standing "what are they doing now" roll-up,
    # merged in from its own file (kept separate from structure by design).
    doing_path = os.path.join(ROOT, "attention/actor-doing.yaml")
    doing = (yaml.safe_load(open(doing_path)).get("actors", {})
             if os.path.exists(doing_path) else {})
    for o in orgs:
        o["name"] = (BOARD_ORG_NAMES.get(o["slug"]) or ent_names.get(o["slug"])
                     or o["slug"].replace("-", " ").title())
        d = doing.get(o["slug"])
        if d and d.get("doing"):
            o["doing"] = " ".join(d["doing"].split())
            o["doing_asof"] = str(d.get("asof", ""))
    held = {}
    for o in orgs:
        if o.get("held_by"):
            held.setdefault(o["held_by"], []).append(o["slug"])
    for h in houses:
        h["holds"] = held.get(h["slug"], [])

    # --- node model (2026-07-26): derive kind + level as the default seed;
    # any explicit kind/level/parent on the node overrides. kind = WHAT it is,
    # level = WHERE it sits (L1 = nothing over it, L2+ = has a parent). Regulators
    # are agencies at L2 whose parent is seeded from their sphere's State.
    for o in orgs:
        rank = o.get("rank")
        if not o.get("parent") and rank == "regulator":
            p = SPHERE_STATE.get(o.get("sphere"))
            if p:
                o["parent"] = p
        if "kind" not in o:
            o["kind"] = ("state" if rank == "state"
                         else "agency" if rank == "regulator"
                         else "corp")
        if "level" not in o:
            o["level"] = "L2" if (o.get("parent") or rank == "regulator") else "L1"
    for h in houses:
        h.setdefault("kind", "person")   # our board's people are controllers → seed L1
        h.setdefault("level", "L1")

    return {
        "schema_version": b.get("schema_version", 2),
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ranks": b["ranks"], "postures": b["postures"], "conditions": b["conditions"],
        "genres": b["genres"], "spheres": b["spheres"], "groups": b.get("groups", []),
        "houses": houses, "orgs": orgs,
    }


# --- CLAIMS layer (2026-07-26): each metric in a per-node bundle becomes a
# CLAIM (PKG/CAPI convention — subject × dimension -> value, with `source`
# citations + a stable, supersession-ready id). Bundles:
# artifacts/bundles/<slug>-node/provenance.yaml. The value on the board is the
# summary; the claim page is the clickable receipt.
DIM_LABELS = {
    "posture": "Posture", "optionality": "Optionality", "gravity": "Gravity",
    "capital-available": "Capital · available", "capital-operating": "Capital · operating",
    "capital-deployed": "Capital · deployed", "capital-in": "Capital · in",
    "capital-out": "Capital · out",
}


# Bundle/receipt links: this repo (theprojection-corpus, renamed from
# theprojection-data 2026-08-05) is PRIVATE, so these receipts resolve for
# Ben (logged in) and 404 for the public; a public receipt export is an
# open follow-up (kestrel STATUS.md).
KESTREL_REPO_BLOB = "https://github.com/benthepsychologist/theprojection-corpus/blob/main/"


def _mk_source(s):
    """PKG `source` shape from a bundle's {figure,label,url,as_of,confidence}.

    Internal repo paths as `url` (e.g. `attention/board.yaml` — how judgment
    claims like posture cite their basis) rendered as RELATIVE hrefs on the
    site and 404'd under /claim/<id>/ (Ben, 2026-07-28). This repo is public
    on GitHub, so rewrite them to real GitHub blob links — the receipt stays
    clickable instead of dead.
    """
    url = s.get("url", "") or ""
    if url and not url.startswith(("http://", "https://")):
        url = KESTREL_REPO_BLOB + url.lstrip("/")
    return {"title": s.get("label") or s.get("figure") or "source",
            "figure": s.get("figure", ""), "url": url,
            "as_of": s.get("as_of", ""), "reliability": s.get("confidence", "")}


def build_claims(board):
    """Every metric across the -node bundles -> a claim {id, subject, dimension,
    value, basis, confidence, as_of, sources[]}. id = `<node>--<dimension>`. Plus
    AGGREGATE claims for group nodes (pocket G1 · sector G2), derived from members
    (posture = modal + spread; other dims link to the member claims)."""
    claims = []
    for f in sorted(glob.glob(os.path.join(ROOT, "artifacts/bundles/*-node/provenance.yaml"))):
        d = yaml.safe_load(open(f)) or {}
        node = d.get("node")
        if not node:
            continue
        asof = str(d.get("asof", ""))

        def add(dim, sub):
            if not sub or not sub.get("value"):
                return
            srcs = [_mk_source(s) for s in (sub.get("sources") or [])]
            conf = next((s["reliability"] for s in srcs
                         if s["reliability"] in ("high", "med", "low")), "")
            claims.append({"id": f"{node}--{dim}", "subject": node, "dimension": dim,
                           "label": DIM_LABELS.get(dim, dim.replace("-", " ").title()),
                           "value": sub.get("value"), "basis": sub.get("basis", ""),
                           "confidence": conf, "as_of": asof, "sources": srcs})
        add("posture", d.get("posture"))
        for k, sub in (d.get("capital") or {}).items():
            add("capital-" + k, sub)
        for dim in ("optionality", "gravity"):
            add(dim, d.get(dim))

    # --- aggregate claims for group nodes: derived from member node claims.
    orgs = board.get("orgs", [])
    groups = board.get("groups", [])
    g1 = [g for g in groups if g.get("tier") == "G1"]
    AGG_DIMS = ("posture", "capital-available", "capital-operating", "capital-deployed",
                "capital-in", "capital-out", "optionality", "gravity")

    def _agg(subject, value_orgs, link_nodes, dim, by):
        link_ids = [f"{m}--{dim}" for m in link_nodes if (m, dim) in by]
        if not link_ids:
            return
        if dim == "posture":
            vals = [by[(m, "posture")]["value"] for m in value_orgs if (m, "posture") in by]
            if not vals:
                return
            cnt = collections.Counter(vals)
            top, n = cnt.most_common(1)[0]
            value = f"{top} — {n} of {len(vals)}  ({' · '.join(f'{k} {v}' for k, v in cnt.most_common())})"
        else:
            value = f"across {len(link_ids)} members — open each for the figure + sources"
        claims.append({"id": f"{subject}--{dim}", "subject": subject, "dimension": dim,
                       "label": DIM_LABELS.get(dim, dim.replace("-", " ").title()),
                       "value": value, "basis": "aggregate of member nodes",
                       "confidence": "", "as_of": "", "sources": [],
                       "members": link_ids, "aggregate": True})

    by = {(c["subject"], c["dimension"]): c for c in claims}
    for g in g1:  # pockets aggregate over their member orgs
        mems = [o["slug"] for o in orgs if o.get("pocket") == g["slug"]]
        for dim in AGG_DIMS:
            _agg(g["slug"], mems, mems, dim, by)
    by = {(c["subject"], c["dimension"]): c for c in claims}  # incl. pocket aggregates
    for g in [g for g in groups if g.get("tier") == "G2"]:  # sectors -> their pockets
        pkts = [pk["slug"] for pk in g1 if g["slug"] in (pk.get("member_of") or [])]
        sector_orgs = [o["slug"] for o in orgs if o.get("pocket") in pkts]
        for dim in AGG_DIMS:
            _agg(g["slug"], sector_orgs, pkts, dim, by)
    return claims


# Beat pages — one per lens (Ben, 2026-07-29: "Morning briefing on the
# front page and on each beat page"). Until now a lens was only a
# client-side filter chip on the homepage, so there was no page for a
# lens's own briefing to live on and no shareable URL for it.
# "money" renamed to "global-capital" 2026-07-30 (Ben, full rename) —
# /beat/money/ becomes /beat/global-capital/. No redirect: personal
# site, no external backlinks to preserve.
BEATS = [("ai", "AI"), ("global-capital", "Global Capital"), ("mental-health", "Mental Health")]


def stage_audio_briefing(site_dir, today_iso):
    """Generate (if needed) and stage the day's narrated front-page mp3.

    Idempotent per day: if artifacts/audio/<today>-front.mp3 already
    exists (this run or an earlier one today), generation is skipped and
    the existing file is just re-staged — a day's briefing text is
    finalized once, not re-narrated on every one of a day's several
    publish passes. Never fatal: audio is a nice-to-have layered on top
    of the text site, not a requirement of it, so any failure here
    (venv missing, kokoro/espeak-ng broken, generation error) is caught,
    printed, and the rest of the publish run continues untouched —
    matching this function's neighbors' own graceful-skip style (see the
    readouts.json block above: "no readouts store yet — skipped").
    """
    audio_dir = os.path.join(ROOT, "artifacts", "audio")
    mp3_path = os.path.join(audio_dir, f"{today_iso}-front.mp3")

    if not os.path.exists(mp3_path):
        if not os.path.exists(AUDIO_VENV_PYTHON):
            print(f"  no audio venv at {AUDIO_VENV_PYTHON} — skipped audio briefing")
            return
        try:
            subprocess.run(
                [AUDIO_VENV_PYTHON, AUDIO_GEN_SCRIPT, "--date", today_iso],
                cwd=ROOT, check=True, capture_output=True, text=True, timeout=600,
            )
        except subprocess.CalledProcessError as e:
            print(f"  audio generation failed for {today_iso} — skipped audio briefing\n"
                  f"    {e.stderr.strip().splitlines()[-1] if e.stderr.strip() else e}")
            return
        except subprocess.TimeoutExpired:
            print(f"  audio generation timed out for {today_iso} — skipped audio briefing")
            return
        if not os.path.exists(mp3_path):
            print(f"  audio generation reported success but {mp3_path} is missing — skipped")
            return
        print(f"  generated audio/{today_iso}-front.mp3")

    site_audio_dir = os.path.join(site_dir, "static", "audio")
    os.makedirs(site_audio_dir, exist_ok=True)
    shutil.copyfile(mp3_path, os.path.join(site_audio_dir, f"{today_iso}-front.mp3"))
    print(f"  staged static/audio/{today_iso}-front.mp3")


def write_site(site_dir, pages, good_slugs, payload, payload_blob, board, board_blob, pub_slugs):
    """Write every page + data file this run produces into the site repo's
    working tree. Validates site_dir itself — nothing gets written to a
    missing/misconfigured checkout."""
    if not site_dir:
        sys.exit("no site checkout configured — pass --site-dir or set THEPROJECTION_SITE_DIR")
    threads_dir = os.path.join(site_dir, "content", "threads")
    entities_dir = os.path.join(site_dir, "content", "entities")
    if not os.path.isdir(threads_dir):
        sys.exit(f"site repo not found at {threads_dir} — pass --site-dir or "
                 f"set THEPROJECTION_SITE_DIR")
    os.makedirs(entities_dir, exist_ok=True)

    # Remove the scaffold placeholder and any stale/unpublished thread pages.
    for fname in os.listdir(threads_dir):
        if fname in ("_index.md",):
            continue
        this_slug = fname[:-3] if fname.endswith(".md") else fname
        if this_slug == PLACEHOLDER_SLUG or (fname.endswith(".md") and this_slug not in good_slugs):
            os.remove(os.path.join(threads_dir, fname))
            print(f"  removed stale page: {fname}")

    for slug, out, _ in pages:
        with open(os.path.join(threads_dir, f"{slug}.md"), "w") as f:
            f.write(out)
        print(f"  wrote content/threads/{slug}.md")

    # Entity stub pages — one per entity actually referenced this run.
    current_entity_slugs = {e["slug"] for e in payload["entities"]}
    for fname in os.listdir(entities_dir):
        if fname == "_index.md":
            continue
        this_slug = fname[:-3] if fname.endswith(".md") else fname
        if fname.endswith(".md") and this_slug not in current_entity_slugs:
            os.remove(os.path.join(entities_dir, fname))
            print(f"  removed stale entity page: {fname}")
    for e in payload["entities"]:
        fm = yaml.safe_dump({"title": e["name"], "entity_kind": e["kind"], "lenses": e["lenses"]},
                             sort_keys=False, allow_unicode=True).strip()
        with open(os.path.join(entities_dir, f"{e['slug']}.md"), "w") as f:
            f.write(f"---\n{fm}\n---\n")
    print(f"  wrote {len(payload['entities'])} entity page(s)")

    # Beat pages — one per lens, now NESTED UNDER /news/ (Ben, 2026-08-03:
    # the whole news feed — AI, Global Capital, Mental Health — moves under
    # /news/ so the front page can become the projects hub). Each beat is a
    # child page of the news section: content/news/<slug>.md -> /news/<slug>/,
    # rendered by layouts/news/single.html. content/news/_index.md (the news
    # dashboard, hand-authored) is left alone. BEATS carries the rename
    # history; /beat/money/ -> /beat/global-capital/ -> /news/global-capital/.
    news_dir = os.path.join(site_dir, "content", "news")
    os.makedirs(news_dir, exist_ok=True)
    for slug, label in BEATS:
        fm = yaml.safe_dump({"title": label, "lens": slug},
                            sort_keys=False, allow_unicode=True).strip()
        with open(os.path.join(news_dir, f"{slug}.md"), "w") as f:
            f.write(f"---\n{fm}\n---\n")
    print(f"  wrote {len(BEATS)} beat page(s) under /news/")

    os.makedirs(os.path.join(site_dir, "data"), exist_ok=True)
    with open(os.path.join(site_dir, "data", "payload.json"), "w") as f:
        f.write(payload_blob)
    print("  wrote data/payload.json")
    with open(os.path.join(site_dir, "data", "board.json"), "w") as f:
        f.write(board_blob)
    print(f"  wrote data/board.json ({len(board['houses'])} houses, {len(board['orgs'])} orgs)")

    # --- Claims: data/claims.json + one content stub per claim (/claim/<id>/),
    # rendered by layouts/claim/single.html. Each metric = a clickable receipt.
    claims = build_claims(board)
    with open(os.path.join(site_dir, "data", "claims.json"), "w") as f:
        f.write(json.dumps(claims, default=str))
    print(f"  wrote data/claims.json ({len(claims)} claims)")

    # --- Executive readouts: data/readouts.json (Ben, 2026-07-29 — "an exec
    # readout on literally every page"). Generated by tools/readouts.py;
    # BREAKING/NEWS are mechanical, SUMMARY is model-written. Filtered to
    # published scopes so a `public: false` thread's readout never ships,
    # and its news bullets are stripped of unpublished thread pointers so a
    # bullet can never link to a page that does not exist.
    ro_src = os.path.join(ROOT, "artifacts/readouts/readouts.json")
    if os.path.exists(ro_src):
        ro = json.load(open(ro_src))
        kept = {}
        for scope, rec in ro.get("readouts", {}).items():
            kind, _, key = scope.partition(":")
            if kind == "thread" and key not in pub_slugs:
                continue
            for sec in ("breaking", "news"):
                for b in rec.get(sec) or []:
                    b["threads"] = [t for t in (b.get("threads") or [])
                                    if t in pub_slugs]
                    # Same provenance-marker leak as thread bodies/blurbs/
                    # map-changes (2026-08-09 sweep) — BREAKING/NEWS bullet
                    # text is pulled straight from digest item records,
                    # which carry the same ⟨...⟩ asides. Rendered via
                    # readout.html's {{ .text }} — plain escaped text, so
                    # linkify=False, matching the blurb/map-changes cases.
                    if b.get("text"):
                        b["text"] = clean_reader_facing_body(b["text"], linkify=False)
            kept[scope] = rec
        with open(os.path.join(site_dir, "data", "readouts.json"), "w") as f:
            f.write(json.dumps({"schema_version": ro.get("schema_version", 1),
                                "readouts": kept}, default=str))
        print(f"  wrote data/readouts.json ({len(kept)} readouts)")
    else:
        print("  no readouts store yet — skipped data/readouts.json")

    stage_audio_briefing(site_dir, payload["today"])

    claim_dir = os.path.join(site_dir, "content", "claim")
    os.makedirs(claim_dir, exist_ok=True)
    claim_ids = {c["id"] for c in claims}
    for fname in os.listdir(claim_dir):
        if fname == "_index.md":
            continue
        s = fname[:-3] if fname.endswith(".md") else fname
        if fname.endswith(".md") and s not in claim_ids:
            os.remove(os.path.join(claim_dir, fname))
    for c in claims:
        fm = yaml.safe_dump({"title": f"{c['subject']} — {c['label']}", "claim_id": c["id"]},
                             sort_keys=False, allow_unicode=True).strip()
        with open(os.path.join(claim_dir, f"{c['id']}.md"), "w") as f:
            f.write(f"---\n{fm}\n---\n")
    print(f"  wrote {len(claims)} claim page(s)")

    # --- Global Capital interpretations: data/interpretations.json + one
    # content stub per interpretation (/interpretation/<id>/), rendered by
    # layouts/interpretation/single.html (DESIGN.md Part 2 §10). Same move
    # as a claim page — a teaser on the surface, the full reasoning one
    # click away. Sourced straight from payload["items"] (parse_digest()
    # already attached `interpretation` there) rather than re-scanning the
    # sidecar files, so this list is exactly what the page itself shows.
    interp_items = [it for it in payload["items"] if it.get("interpretation")]
    interps = []
    for it in interp_items:
        interps.append({"id": it["interpretation_id"], "day": it["day"], "lens": it["lens"],
                         "item_title": it["title"], "item_url": it.get("url"),
                         "threads": it.get("threads", []),
                         **it["interpretation"]})
    with open(os.path.join(site_dir, "data", "interpretations.json"), "w") as f:
        f.write(json.dumps(interps, default=str))
    print(f"  wrote data/interpretations.json ({len(interps)} interpretations)")

    interp_dir = os.path.join(site_dir, "content", "interpretation")
    os.makedirs(interp_dir, exist_ok=True)
    interp_ids = {i["id"] for i in interps}
    for fname in os.listdir(interp_dir):
        if fname == "_index.md":
            continue
        s = fname[:-3] if fname.endswith(".md") else fname
        if fname.endswith(".md") and s not in interp_ids:
            os.remove(os.path.join(interp_dir, fname))
    for i in interps:
        fm = yaml.safe_dump({"title": i["item_title"], "interp_id": i["id"]},
                             sort_keys=False, allow_unicode=True).strip()
        with open(os.path.join(interp_dir, f"{i['id']}.md"), "w") as f:
            f.write(f"---\n{fm}\n---\n")
    print(f"  wrote {len(interps)} interpretation page(s)")

    # --- STORY pages: data/stories.json + one content stub per story
    # (/story/<id>/), rendered by layouts/story/single.html. See
    # build_stories() for why a story is a different object from a thread.
    stories = build_stories(pub_slugs, {t["slug"]: t for t in load_threads_yaml()})
    with open(os.path.join(site_dir, "data", "stories.json"), "w") as f:
        f.write(json.dumps(stories, default=str))
    n_src = sum(len(s["sources"]) for s in stories)
    n_badged = sum(1 for s in stories for x in s["sources"]
                   if x.get("band") or x.get("rsp") or x.get("class")
                   or x.get("practices") is not None)
    print(f"  wrote data/stories.json ({len(stories)} stories, "
          f"{n_src} sources, {n_badged} credibility-badged)")

    story_dir = os.path.join(site_dir, "content", "story")
    os.makedirs(story_dir, exist_ok=True)
    story_ids = {s["id"] for s in stories}
    for fname in os.listdir(story_dir):
        if fname == "_index.md":
            continue
        s_id = fname[:-3] if fname.endswith(".md") else fname
        if fname.endswith(".md") and s_id not in story_ids:
            os.remove(os.path.join(story_dir, fname))
    for s in stories:
        fm = yaml.safe_dump({"title": s["headline"], "story_id": s["id"],
                              "date": s["date"], "lens": s["lens"]},
                             sort_keys=False, allow_unicode=True).strip()
        with open(os.path.join(story_dir, f"{s['id']}.md"), "w") as f:
            f.write(f"---\n{fm}\n---\n")
    print(f"  wrote {len(stories)} story page(s)")

    # Per-actor Map pages — one content stub per org + House, rendered by
    # layouts/map/single.html from board.json (same pattern as entity stubs).
    map_dir = os.path.join(site_dir, "content", "map")
    os.makedirs(map_dir, exist_ok=True)
    map_records = ([("org", o["slug"], o["name"]) for o in board["orgs"]]
                   + [("house", h["slug"], h["name"]) for h in board["houses"]]
                   + [("group", g["slug"], g["slug"].replace("-", " ").title())
                      for g in board.get("groups", [])])
    current_map_slugs = {slug for _, slug, _ in map_records}
    for fname in os.listdir(map_dir):
        if fname == "_index.md":
            continue
        s = fname[:-3] if fname.endswith(".md") else fname
        if fname.endswith(".md") and s not in current_map_slugs:
            os.remove(os.path.join(map_dir, fname))
            print(f"  removed stale map page: {fname}")
    for kind, slug, name in map_records:
        fm = yaml.safe_dump({"title": name, "board_kind": kind},
                             sort_keys=False, allow_unicode=True).strip()
        with open(os.path.join(map_dir, f"{slug}.md"), "w") as f:
            f.write(f"---\n{fm}\n---\n")
    print(f"  wrote {len(map_records)} map page(s)")
    old_site_json = os.path.join(site_dir, "data", "site.json")
    if os.path.exists(old_site_json):
        os.remove(old_site_json)
        print("  removed superseded data/site.json")
