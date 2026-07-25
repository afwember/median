# Illustration prompts

One per plate, numbered in build order.

**Method, three passes.** Generate with every string specified verbatim —
that is what makes generated text render legibly rather than as gibberish.
Reskin in one short oppositional line if the register is wrong. Strip text
only if the plate needs a recompositable base.

**State the downstream use, not just the constraint.** Telling the model an
asset will be "recomposited offline as editable vector type" improves
compliance, because it can then make sensible calls in cases the instruction
does not cover.

`_superseded/` holds prompts that were replaced, with a header on each
explaining what went wrong. They are kept deliberately: one records that
asking for blank reserved panels instead of specified text produces a
canon-clean, completely lifeless page.
