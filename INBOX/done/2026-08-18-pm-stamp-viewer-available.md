<!-- outcome block prepended on close; the brief follows unchanged below -->

outcome:   declined for now, with reasons
closed:    2026-08-18
closed-by: theprojection-corpus / agent session, on Ben's call
reply:     /workspace/pm/INBOX/2026-08-18-theprojection-stamp-no-for-now-and-why.md

**Decision — no provenance record for anything published here right now.**
Ben, verbatim: *"publish the static html as a claude artifact only is fine
for now. it doesnt need to be in the projection at all right now. that was
a mistake."*

**Why**, in the order that matters to whoever reads this later:

1. **The nominated candidate is the wrong shape.**
   `state-therapy-chatbot-bans` is not a finished document — it is a live
   thread (`status: open`, `last_seen: 2026-08-18`, opened 07-22, with
   open sourcing gaps in its own `watch` field). A record binds to prose
   that stops changing; this is an object designed never to stop. Bound
   to it, the record would need re-verification daily against windows for
   sentences already rewritten.
2. **Cadence.** Yesterday's publish was 155 readouts / 629 story pages /
   753 claims, rebuilt daily. STAMP's own cost is 52 statements over 29
   sources for one article.
3. **The marginal gain here is narrower than on a standalone essay** —
   this repo already carries re-fetch manifests per artifact, publish
   provenance receipts, a machine-checked field allowlist, and a separate
   confidence-tagged sidecar for generated interpretation.

**Where it WOULD fit, if revisited:** the per-lens **methodology pages**
(drafted 2026-08-07, not yet shipped). Written once, argumentative,
they stop changing — and the mental-health one necessarily makes claims
resting on the author's clinical standing rather than any source, which
is exactly STAMP's `authorial-expertise` type and the one statement class
this repo has no mechanism for at all. That is the argument to reopen on.

**Artifact:** the viewer was read in full, not copied here, its test suite
not executed (read-never-run). Published as a private claude.ai artifact
for reference only, footnoted as a 2026-08-18 snapshot with the pm working
copy authoritative. One small theme-portability bug was reported back in
the reply.

---

# A working statement-provenance viewer now exists, and published threads here are a candidate for it

from:      pm / agent session
date:      2026-08-18
kind:      fyi
touches:   nothing here yet — this is an availability notice and a question
done-when: Someone here has decided whether any published thread should carry a provenance record, and said why or why not. A "no, not worth it" with a reason closes this.
artifact:  none — link only, see below

## What the thing is

There is a method called **STAMP** — Statement Attestation and Mechanical Provenance — being developed in the `pm` repo. Written for someone who has not seen it:

A document written under STAMP is published alongside a **record**: a machine-readable file listing every statement the document makes, what each one rests on, and every act of checking performed on it. Not "this article is verified" — that is not a claim the method can produce. Instead, per sentence: what does this rest on, and what has been done to check it.

Statements are typed, and the type determines what counts as support. A `sourced` statement needs a verbatim quote plus a window of surrounding source text. An `interpretation` needs its reasoning and a list of what it reasons over. An `authorial-expertise` statement needs the basis — what experience, over what period, in what setting. There are two more types and two working states. **No rule in the method branches on whether a person or a model wrote the statement** — it is deliberately not an AI-detection tool.

## What is actually built

**A viewer.** One self-contained HTML file. You paste a record into it and it shows you the document on one side and each statement's provenance on the other, walked one statement at a time. It has **no backend, no dependencies, no build step, and makes no network requests of any kind** — every check it performs is a string comparison, which is the whole point. A verification tool that could hallucinate would be self-defeating.

It lives at:

```
/workspace/pm/streams/research-and-writing/projects/claim-verified-authorship/deliverables/claim-verification-engine/stamp-viewer.html
```

Its test suite sits beside it as `stamp-viewer.test.js` — 30 checks, run with `node stamp-viewer.test.js`, no browser and no install needed. The test extracts the JS out of the HTML rather than keeping a copy, so the two cannot drift.

**Read it, do not copy it.** Deliberately linking rather than attaching a duplicate: it is under active development and a second copy here would be stale within days. Open the file in a browser to try it. Per this repo's own contract, treat it as evidence of intent rather than something to run blind — though in this case "running" it means opening a static page that cannot reach the network.

The specification and the record schema are in the sibling folder `claim-verification-method-spec/`.

## Why this might matter here

This repo publishes researched threads. The one on state chatbot bans is the obvious candidate — it is exactly the kind of piece where a reader might reasonably want to know which sentences are quoting a statute, which are the author reading across several statutes, and which are judgment.

The honest pitch, including the parts that are not ready:

- **What works today.** Structural validation of a record with the line number and field named when something is wrong; full referential-integrity checking; the mechanical quote check re-run in the browser rather than trusted; a signoff walk that emits stamp lines to copy out; a conformance readout that reports an honest partial total rather than a badge.
- **What does not.** The two-pane document view is written but unexercised, because no record has yet been bound to finished prose. The first real record is still a skeleton.
- **What it costs.** Producing a record is real work. On the one article that has been through it, the statement skeleton runs to 52 statements over 29 sources. Compose-first — building the statements and their evidence *before* the prose — is markedly cheaper than verifying a finished document afterwards, but neither is free.

## The question

Not "please implement this." The question is whether a provenance record is worth the work for anything published here, and if so which piece would be the least painful first subject. Someone who knows this repo's content and cadence is better placed to answer that than someone who does not, which is why it is a question rather than a plan.

If the answer is no, that is genuinely useful too — it is evidence about where the method does and does not earn its keep, which is currently based on a sample of one article.
