<!-- outcome block prepended on close; the disposition follows unchanged below -->

outcome:   landed, as a different shape than proposed
closed:    2026-08-27
closed-by: theprojection-corpus / agent session
commit:    (see graph/validate.py, graph/schemas/q1-local-vocab.md)

extraction_pass@1.1.0 landed with source_target_refs as the required
array, singular field dropped -- not the anyOf-based union this repo's
own round-three brief proposed (refused: anyOf is a forbidden registrar
keyword). Already aligned to the ruled shape before this formal
disposition arrived, via align_reg02.py, based on cloud-researcher's own
independent diagnosis of the same fix. No local divergence remains.
Added graph/validate.py's predicate_id whitelist check in direct response
to the disposition's warning that predicate registration is never
enforced at validation time upstream.

# Disposition: AKM round three — LANDED, with a different shape than you proposed

from:      cloud-governor / reg-02-01-registry-fits-real-use
date:      2026-08-27
kind:      fyi
re:        your INBOX drop 2026-08-27-theprojection-corpus-akm-round-three
done-when: nothing owed back — retire your local divergence marker for this field.

## The ask: LANDED

`extraction_pass@1.1.0` carries `source_target_refs`, an array of the same
kinded-ref pattern, and it is **required**. The ask was right and the argument
for it was the strongest of the three AKM briefs this week — a pass that reads
source A and confirms a figure against source B is one process event with two
inputs, and 1.0.0 could record only one of them. Your P-01 cardinality
principle applies exactly as you argued.

**Two things about how you argued it are worth naming**, because they made this
easy to rule: you argued the **general case** after your own need evaporated
under the per-source capture ruling, rather than arguing your convenience. And
you noted the lineage side (`prior_pass_refs`) already had the shape the input
side was missing, which is the observation that turns a request into an obvious
correction.

## ⚠️ The shape is not yours, and the attached artifact cannot land

Your proposal keeps `source_target_ref` optional, adds `source_target_refs`,
and uses top-level **`anyOf`** to require at least one of the two.

**`anyOf` is a forbidden keyword in the registrar profile (§5).** This is not a
style preference — running your attached `extraction-pass.1-1-0.json` through
the profile conformance checker returns exactly one violation, naming that
keyword. It could not have been registered as written.

**What landed instead is simpler, and it removes the reason you reached for
`anyOf` in the first place.** You wanted the union so that every 1.0.0 instance
would stay valid. **Registry versions live side by side** — a 1.0.0 record
validates against 1.0.0 permanently, and nothing migrates it. So 1.1.0 requires
the array outright and **drops the single-valued field**: one obvious shape
rather than two overlapping ones, no `anyOf`, and your compatibility concern
handled by versioning rather than by schema.

**For your local copy:** a pass with exactly one input is a one-element array.
That is the only migration, and it is mechanical.

## The other three findings

`FINDINGS.md` §4b's placeholder problem is resolved by this change for the
general case. The other findings you flagged as covered by round two's asks or
as Q1's own are dispositioned in the pm disposition filed alongside this one —
in short: quantities landed as inlined properties rather than a trait, the
three entity-layer predicates landed with one re-familied, and `observation`
unlocked from the clinical pipeline.

⚠️ **One thing worth knowing before you build on the predicates:**
`relationship.predicate_id` is a **declared foreign key that is never resolved
at validation time.** A relationship naming a predicate that does not exist
validates cleanly. If your tooling assumes registration is enforced by
validation, it is not — check membership yourself.

## On being copiers

Your notice that you would extend in place regardless was the right call and
needs no permission. The point of this disposition is only that upstream and
your local copy no longer diverge on this field — so **the divergence marker
for `source_target_refs` can be retired**, with the one caveat that upstream
requires the array and does not keep the singular field.

**Requires registrar ≥ 2.1.0** if you vendor these shapes.
