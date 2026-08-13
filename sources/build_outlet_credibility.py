#!/usr/bin/env python3
"""Rebuild sources/outlet-credibility.yaml — the domain-keyed credibility layer.

    python3 sources/build_outlet_credibility.py [--dry-run]

WHY THIS FILE EXISTS (2026-08-11). The 2026-08-07 build had no committed
builder — it was assembled ad hoc, which is exactly why it drifted: the file
documented a rebuild procedure in prose that nobody could run. Now it is a
script, so "rebuild the credibility layer" is a command rather than a project.

WHAT CHANGED IN THIS REBUILD, and it is the whole point:

  The 08-07 universe was BUFFER FREQUENCY (domains with >=3 records in the
  30-day buffer). That silently excluded the domains we actually CITE.
  Measured before the change: 224 of the 267 domains appearing as sources in
  our own story pages were absent from the file — including aljazeera.com
  (22 citations), npr.org (11), sec.gov (9) and washingtonpost.com (6). They
  were not judged unrateable; they were never looked up.

  The universe is now CITED-DOMAINS ∪ BUFFER(n>=3). Citations come first
  because a domain we quote on a public page matters more than one that
  merely passed through collection.

THREE LAYERS, unchanged in kind from 08-07:
  pc1  Lin/Lasser/Lewandowsky/Cole/Gully/Rand/Pennycook 2023 ensemble
       (PNAS Nexus 2(9):pgad286, CC BY 4.0), data from
       github.com/hauselin/domain-quality-ratings. USE THE pc1 COLUMN ONLY —
       the component columns inherit their raters' restrictive terms; the PCA
       aggregate is the authors' own published measure.
  rsp  Wikipedia perennial sources (CC BY-SA 4.0, attribution required on
       render), parsed from the 8 subpages via the MediaWiki API. A domain
       with several RSP rows carrying different verdicts is slash-joined and
       rendered "disputed / split" — never resolved by picking a side.
  class: primary-source
       Not a quality rating. A category assertion: this domain publishes the
       thing itself (a filing, a paper, a company's own announcement) rather
       than reporting on someone else's. It OUTRANKS rsp at render, because
       RSP rates arxiv "generally unreliable" AS A WIKIPEDIA CITATION, which
       is the wrong frame for a feed whose evidence hierarchy puts primary
       sources at the top.

PUBLICATION: cleared by ben-steer 2026-08-11 ("permission granted"), which
supersedes the earlier keep-INTERNAL hold on pc1. Attribution obligations for
both datasets travel with the data and are rendered on every story page.
"""
import argparse
import collections
import csv
import glob
import json
import os
import re
import sys
import urllib.request

ROOT = os.environ.get("KESTREL_INSTANCE", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "sources/outlet-credibility.yaml")
PC1_URL = "https://raw.githubusercontent.com/hauselin/domain-quality-ratings/main/data/domain_pc1.csv"
RSP_API = ("https://en.wikipedia.org/w/api.php?action=parse&page="
           "Wikipedia:Reliable_sources/Perennial_sources/{n}&prop=wikitext&format=json")
UA = "theprojection-corpus/1.0 (research; contact ben@mensiomentalhealth.com)"
BUFFER_FLOOR = 3          # for buffer-only domains; cited domains bypass this

RSP_CLASS = {"s-gr": "generally-reliable", "s-nc": "no-consensus",
             "s-gu": "generally-unreliable", "s-d": "deprecated",
             "s-b": "blacklisted"}

# --- primary-source classification -----------------------------------------
# Mechanical where a rule is genuinely mechanical, curated where it needs
# judgment, and the split is explicit so a reader can audit either half.

def _is_gov(d):
    """Government, legislature, court and regulator domains."""
    return (d.endswith(".gov") or ".gov." in d or d.endswith(".gov.uk")
            or d.endswith(".europa.eu") or d.endswith(".gc.ca")
            or d.endswith(".parliament.uk")
            or re.search(r"\b(legislature|assembly|senate|house)\.", d) is not None
            or d.endswith(".mil"))

# Journal platforms, preprint servers, registries and model/code registries —
# "the paper or the record itself".
PRIMARY_PLATFORMS = {
    "arxiv.org", "biorxiv.org", "medrxiv.org", "doi.org", "sciencedirect.com",
    "frontiersin.org", "link.springer.com", "onlinelibrary.wiley.com",
    "journals.plos.org", "pubmed.ncbi.nlm.nih.gov", "ssrn.com",
    "huggingface.co", "github.com", "openrouter.ai", "courtlistener.com",
    "jmir.org", "mental.jmir.org", "papers.ssrn.com",
}

# Corporate / institutional OWN channels. Curated deliberately: a bare
# `news.` prefix is not evidence (news.crunchbase.com is Crunchbase NEWS, a
# publication, not a company announcement channel), so this is a list rather
# than a pattern, and it only contains domains we actually cite.
PRIMARY_OWN_CHANNEL = {
    "openai.com", "anthropic.com", "x.ai", "blog.google", "about.fb.com",
    "microsoft.com", "news.microsoft.com", "nvidianews.nvidia.com",
    "newsroom.intel.com", "newsroom.amd.com", "ir.amd.com", "newsroom.arm.com",
    "news.samsung.com", "news.skhynix.com", "blackstone.com", "macquarie.com",
    "allianz.com", "group.pingan.com", "group.softbank", "investors.cvshealth.com",
    "ir.nasdaq.com", "about.kaiserpermanente.org", "hcahealthcaretoday.com",
    "home.nuhw.org", "nuhw.org", "nationalnursesunited.org",
    "unit42.paloaltonetworks.com", "news.stanford.edu", "chai.org",
    "psychotherapy.org.uk", "phti.org", "mhdi.uk", "gibsondunn.com",
    # added 2026-08-11 (evening): each is the subject's OWN channel for the
    # story we cited it for, which is what this class means — not a quality
    # judgement. pacificoenergy.com is the developer of the Pecos County gas
    # plant; newsletter.cleanview.co is the market-intelligence firm that
    # traced that project from satellite imagery and permits, publishing its
    # own analysis; jstreet.org is an advocacy organisation cited for its own
    # position.
    "pacificoenergy.com", "newsletter.cleanview.co", "jstreet.org",
}
# Structural own-channel markers, applied only to a domain that is NOT already
# a known news publisher. Kept narrow on purpose.
OWN_CHANNEL_PREFIX = ("newsroom.", "ir.", "investors.", "investor.", "press.")


def classify_primary(domain):
    if _is_gov(domain):
        return "primary-source"
    if domain in PRIMARY_PLATFORMS or domain in PRIMARY_OWN_CHANNEL:
        return "primary-source"
    if any(domain.startswith(p) for p in OWN_CHANNEL_PREFIX):
        return "primary-source"
    return None


INDICATORS = ["masthead", "bylines", "corrections", "ownership", "standards",
              "ad_separation", "primary_sourcing"]
PRACTICES_FILE = os.path.join(ROOT, "sources/outlet-practices.yaml")
MIN_CHECKED = 4   # below this, publish no rating rather than a thin one


def load_practices():
    """Layer 3 — our OWN published-practice observations, per domain.

    Kept in a SEPARATE committed file on purpose. pc1 and rsp are re-derived
    from external sources on every rebuild and can be thrown away safely;
    these are observations we made, with evidence urls and a checked date, and
    a rebuild must never silently discard them. Merged in below.

    The rubric is published at /methodology/ BEFORE any rating ships — that
    gate is written into this layer's own spec ("Rubric TBD on the methodology
    page before any rating ships; observable practices only, never truth
    verdicts") and is the reason layer 3 sat unbuilt from 2026-08-07 to
    2026-08-11.
    """
    if not os.path.exists(PRACTICES_FILE):
        return {}
    import yaml
    return (yaml.safe_load(open(PRACTICES_FILE)) or {}).get("domains", {}) or {}


def band_of(pc1):
    return "high" if pc1 >= 0.8 else "solid" if pc1 >= 0.6 else "mixed" if pc1 >= 0.4 else "low"


def _domain(url):
    """Host of a url, lowercased, minus a leading `www.` and any :port.

    The port strip is not hypothetical — the first build of this file emitted
    `asiaone.com:443` as a distinct domain from `asiaone.com`, splitting one
    outlet's rating across two keys. And this is `startswith`, not
    `lstrip("www.")`: lstrip removes a leading RUN OF CHARACTERS, which turned
    washingtonpost.com into "ashingtonpost.com" in the story builder before it
    was caught.
    """
    m = re.match(r"https?://([^/]+)", url or "")
    if not m:
        return ""
    h = m.group(1).lower().split(":")[0]
    return h[4:] if h.startswith("www.") else h


def parent(d):
    """One level up, so ir.amd.com can inherit amd.com's rating."""
    p = d.split(".")
    return ".".join(p[-3:]) if len(p) > 3 else ".".join(p[-2:])


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")


def load_pc1():
    rows = csv.DictReader(fetch(PC1_URL).splitlines())
    return {r["domain"].strip().lower(): float(r["pc1"])
            for r in rows if r.get("pc1") not in (None, "")}


def load_rsp():
    out = collections.defaultdict(set)
    for n in range(1, 9):
        w = json.loads(fetch(RSP_API.format(n=n)))["parse"]["wikitext"]["*"]
        parts = re.split(r'\n\|-\s*class="([^"]+)"', w)
        for i in range(1, len(parts), 2):
            status = RSP_CLASS.get(parts[i].strip())
            if not status:
                continue
            for m in re.finditer(r"\{\{WP:RSPUSES\|([^}]*)\}\}", parts[i + 1]):
                for d in m.group(1).split("|"):
                    d = d.strip().lower()
                    if d and "." in d and " " not in d:
                        out[d].add(status)
    return {d: "/".join(sorted(v)) for d, v in out.items()}


def load_universe():
    """Domains we CITE (from published stories) plus frequent buffer domains."""
    cited = collections.Counter()
    stories_path = os.path.join(ROOT, "artifacts/readouts")  # placeholder guard
    site = os.environ.get("THEPROJECTION_SITE_DIR", "/workspace/theprojection-site")
    sp = os.path.join(site, "data/stories.json")
    if os.path.exists(sp):
        for s in json.load(open(sp)):
            for x in s.get("sources", []):
                if x.get("domain") and not x.get("redirect"):
                    cited[x["domain"]] += 1
    buf = collections.Counter()
    # gdelt + rss ONLY — google_news_rss urls are redirect links, not publishers
    for f in (glob.glob(os.path.join(ROOT, "buffer/*-gdelt.jsonl"))
              + glob.glob(os.path.join(ROOT, "buffer/*-rss.jsonl"))):
        for line in open(f):
            try:
                d = _domain(json.loads(line).get("url"))
            except Exception:
                continue
            if d:
                buf[d] += 1
    return cited, buf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print("fetching pc1 …", flush=True)
    pc1 = load_pc1()
    print(f"  {len(pc1)} rated domains")
    print("fetching Wikipedia perennial sources …", flush=True)
    rsp = load_rsp()
    print(f"  {len(rsp)} domains with a verdict")
    practices = load_practices()
    if practices:
        print(f"practice sheets on file: {len(practices)}")
    cited, buf = load_universe()
    universe = sorted(set(cited) | {d for d, v in buf.items() if v >= BUFFER_FLOOR})
    print(f"universe: {len(universe)} domains "
          f"({len(cited)} cited, {sum(1 for v in buf.values() if v >= BUFFER_FLOOR)} buffer>={BUFFER_FLOOR})")

    domains, stats = {}, collections.Counter()
    for d in universe:
        rec = {}
        score = pc1.get(d, pc1.get(parent(d)))
        if score is not None:
            rec["pc1"] = round(score, 3)
            rec["band"] = band_of(score)
            stats["pc1"] += 1
        verdict = rsp.get(d, rsp.get(parent(d)))
        if verdict:
            rec["rsp"] = verdict
            stats["rsp"] += 1
            if "/" in verdict:
                stats["rsp_split"] += 1
        cls = classify_primary(d)
        if cls:
            rec["class"] = cls
            stats["primary"] += 1
        # Layer 3 — published-practice indicators, our own observations.
        # A count, never a score: it measures whether an outlet has made
        # itself ACCOUNTABLE (who wrote this, who owns it, how to get an
        # error fixed), not whether it is right.
        pr = practices.get(d)
        if pr and pr.get("indicators") and not pr.get("unreachable"):
            ind = pr["indicators"]
            # An indicator recorded as null/None was NOT CHECKABLE — the page
            # it lives on blocked us — and is dropped from the denominator.
            # Counting a blocked About page as an absent one would turn a
            # transparency check into a penalty for bot-blocking, which is a
            # different measurement. fiercehealthcare.com is the live case:
            # articles serve fine, /about-us and /editorial-advisory-council
            # hard-403.
            checked = [k for k in INDICATORS if ind.get(k) is not None]
            if len(checked) >= MIN_CHECKED:
                rec["practices"] = sum(1 for k in checked if ind[k])
                rec["practices_of"] = len(checked)
                rec["practices_checked"] = str(pr.get("checked", ""))
                if len(checked) < len(INDICATORS):
                    rec["practices_partial"] = True
                stats["practices"] += 1
            else:
                stats["practices_too_thin"] += 1
        if not rec:
            rec["status"] = "unrated"
            stats["unrated"] += 1
            if cited.get(d, 0) >= 2 or buf.get(d, 0) >= 8:
                rec["gap_fill"] = "candidate"
                stats["gap_fill"] += 1
        if cited.get(d):
            rec["cited"] = cited[d]
        if buf.get(d):
            rec["n30d"] = buf[d]
        domains[d] = rec

    cit_total = sum(cited.values())
    # `practices` counts as a badge — it is layer 3, and excluding it would
    # under-report exactly the trade-press coverage this layer exists to add.
    cit_cov = sum(n for d, n in cited.items()
                  if any(k in domains[d] for k in ("pc1", "rsp", "class", "practices")))
    print(f"\n  pc1-rated {stats['pc1']} · rsp {stats['rsp']} ({stats['rsp_split']} split) · "
          f"primary-source {stats['primary']} · practices {stats['practices']} · "
          f"unrated {stats['unrated']} ({stats['gap_fill']} gap_fill)")
    print(f"  CITATION COVERAGE: {cit_cov}/{cit_total} = {100*cit_cov//max(cit_total,1)}%")

    if args.dry_run:
        print("\n--dry-run: not written")
        return

    header = open(OUT).read().split("\nmeta:")[0] if os.path.exists(OUT) else ""
    import yaml
    body = {"meta": {"built": os.environ.get("BUILD_DATE", "2026-08-11"),
                      "builder": "sources/build_outlet_credibility.py",
                      "provenance": "ben-steer 2026-08-11 (rebuild)",
                      "universe": "cited-domains UNION buffer(gdelt+rss) n30d>=%d" % BUFFER_FLOOR,
                      "domains_total": len(domains),
                      "cited_domains": len(cited), "citations_total": cit_total,
                      "citation_coverage_pct": 100 * cit_cov // max(cit_total, 1),
                      "pc1_rated": stats["pc1"], "rsp_tagged": stats["rsp"],
                      "rsp_split": stats["rsp_split"],
                      "primary_source": stats["primary"],
                      "practice_rated": stats["practices"],
                      "unrated": stats["unrated"], "gap_fill_candidates": stats["gap_fill"]},
             "domains": domains}
    with open(OUT, "w") as f:
        f.write(header + "\n" + yaml.safe_dump(body, sort_keys=True, allow_unicode=True,
                                                default_flow_style=None, width=100))
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
