<!-- outcome block prepended on close; the brief follows unchanged below -->

outcome:   fixed
closed:    2026-08-25
closed-by: theprojection-corpus / agent session
commit:    2db4051

**Fixed exactly as prescribed.** `render_read.md_html()`'s bold pass is
now `re.sub(r"\*\*(.+?)\*\*", ..., flags=re.S)` instead of the
asterisk-excluding `[^*]+` — verified against both real failing strings
from the brief (the `china-stack-independence` nested-italic case and the
`tsmc-capacity-race` line-wrap case), both now convert correctly.
**`publish/adapter.py`'s local `_md_html()` fork retired** — it now
imports and calls the shared `md_html()` directly (two call sites in
`_timeline_block_html()`); the module-level `_MD_BOLD`/`_MD_ITALIC`
regexes stay, since `_strip_md_emphasis()` (a different function, for a
different leak) still uses them.

---

# md_html()'s bold regex silently fails on a nested single-asterisk italic span (or a word-wrapped bold span)

from:      kestrel / engine session
date:      2026-08-21
kind:      bug
touches:   theprojection_pipeline/render_read.py:59 (`md_html()`'s bold
           pass) — and the already-forked local workaround at
           publish/adapter.py:355 (`_md_html()`), which should be retired
           once this lands
done-when: `md_html()`'s bold regex matches a `**...**` span that contains
           a nested `*italic*` aside and/or straddles a line-wrap, the
           same way `publish/adapter.py`'s local `_md_html()` already
           does. Once fixed, `publish/adapter.py` should import
           `md_html()` directly again and retire its local `_md_html()`
           copy.
artifact:  none

## Path note — this one is slightly different from the other routed issues

This started life as kestrel GitHub issue #25, filed by
theprojection-corpus's own resident agent on 2026-08-18 against
`kestrel/render_read.py`, back when that file still lived in kestrel.
Confirmed today (2026-08-21) by reading the current file: `render_read.py`
has since moved into this repo as
`theprojection_pipeline/render_read.py`, so the fix now belongs in the
same repo the bug report came from — the local `_md_html()` workaround in
`publish/adapter.py` (also in this repo) already exists as documented,
deliberate cover for it. Routing this as a normal INBOX brief anyway,
per kestrel's standing convention that corpus-repo code changes go
through INBOX rather than kestrel issues, now that the code lives here.

## The bug — confirmed still present today

`theprojection_pipeline/render_read.py:59`:

```python
t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
```

`[^*]+` is a character class that excludes asterisks entirely. Any bold
span containing a nested `*italic*` never matches at all — not "matches
wrong," matches nothing — so the whole span (including its literal
`**`/`*` characters) falls through as plain text.

## Real example (from theprojection-corpus's own `artifacts/threads/`)

`artifacts/threads/china-stack-independence.md`:

```
**A Zhuhai-based threat actor using the aliases *knaithe* and other names** did something.
```

Reproduced directly:

```python
>>> import re
>>> t = "**A Zhuhai-based threat actor using the aliases *knaithe* and other names** did something."
>>> re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
'**A Zhuhai-based threat actor using the aliases *knaithe* and other names** did something.'
```

No conversion — the reader sees literal asterisks on the public page.

## The fix

`.+?` (non-greedy, matches any character including a nested single
asterisk) instead of `[^*]+`:

```python
>>> re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
'<strong>A Zhuhai-based threat actor using the aliases *knaithe* and other names</strong> did something.'
```

Additional wrinkle worth fixing at the same time: without `re.DOTALL`,
`.` doesn't match `\n`, so a bold span that happens to straddle a
word-wrap in the source `.md` file also fails to convert — a second real
case, `artifacts/threads/tsmc-capacity-race.md`'s 08-04 entry:
`"**The actual fix, and the real\ngap:**"`.
`re.compile(r"\*\*(.+?)\*\*", re.DOTALL)` fixes both at once.

**Do not apply the same treatment to the italic regex**
(`(?<!\*)\*([^*\n]+)\*(?!\*)`, render_read.py:60) — it's fine as-is,
deliberately: unlike bold, a lone `*` is common enough elsewhere that
letting it span lines risks pairing two unrelated markers across a
paragraph break instead of catching a real wrapped span.

## Blast radius, checked empirically rather than assumed (from the original report)

A sweep of every generated page on theprojection.org (1,727 pages) for
the failure signature found it live in exactly 2 places at filing time:
the `china-stack-independence` story above, and the `tsmc-capacity-race`
line-wrap case. Everywhere else already using the real `md_html()`
(entity pages, claim pages, news pages) was clean — narrow blast radius,
but real, and it will recur anywhere a curator's bold span happens to
wrap an italic aside or a line break.

## What's already done downstream — retire this once the upstream fix lands

`publish/adapter.py` in this repo already carries a local corrected
copy, `_md_html()` (line 355), with both the regex and DOTALL fix
applied — the file's own comment at line 147 flags it explicitly:
`# ".+?" (not "[^*]+") on the bold pass — see _md_html()'s docstring
below`, documented as a deliberate divergence pending this fix landing
upstream in `md_html()`. Once `render_read.py:59` is fixed,
`publish/adapter.py` should go back to importing `md_html()` directly
and drop its local `_md_html()` copy, the same way it worked before this
bug was found.
