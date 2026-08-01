# MEDIAN extraction — Pass A
# prompt_version: 1.0
# schema_version: 1.0
#
# Frozen artifact. Changing this file invalidates every record produced with a
# previous version (compiler spec §7). Bump the version; do not edit in place
# once corpus extraction has run.

## Task

You are decomposing one chunk of one MEDIAN design source into atomic canon
records. You are not summarising, not resolving contradictions, and not
deciding what is true. You are making each independently actionable claim in
this chunk separately addressable, with its source wording attached.

Return JSON only: an object with a single key `records`, whose value is an
array of record objects matching the supplied schema. No prose, no preamble.

## What counts as one record

One record is one independently actionable claim: a requirement, a
prohibition, a definition, an interface instruction, an illustrative example, a
line of in-world voice, a tuning value, an open question, or a note about
history.

Split a paragraph that states three separate rules into three records. Keep a
single rule that spans three sentences as one record. If a sentence states a
rule *and* gives its rationale, the rule is the record; the rationale is
`status: rationale` only if it carries mechanical consequence, otherwise omit
it.

Do not create records for: headings on their own, navigational text, table of
contents entries, or running document furniture.

## Fields

**`id`** — `<SOURCE_ID>:NNNN`, four digits, numbered sequentially from the
starting number you are given. Never reuse or renumber.

**`loc`** — the coordinate of the block this claim came from, copied exactly
from the `<!--@...-->` marker above it.

> **Coordinates are opaque strings.** `3.1#2` is a different location from
> `3.1`. `4.2¶7` is different from `4.2¶7#2`. Copy the marker character for
> character. Do not normalise, tidy, renumber, or strip a `#n` suffix. A
> coordinate that has been "corrected" points the record at the wrong passage
> and will fail verification.

**`quote`** — the operative source text, verbatim, copied from the block. Long
enough to carry the whole condition including its exceptions and qualifiers.
Never paraphrase. Never stitch together text from two places. If the block is a
table row, quote the row.

**`claim`** — one compact sentence stating what the quote establishes, in
neutral present tense. The claim must not assert more than the quote supports:
if the quote says "usually", the claim may not say "always". When you cannot
state the claim without exceeding the quote, add the flag
`claim_exceeds_quote`.

**`type`** — one of:
`REQ` operative requirement · `GUARD` prohibition, limit or guardrail ·
`TERM` definition or terminology note · `UI` interface or presentation
instruction · `EXAMPLE` illustration · `SAY` in-world voice or folklore ·
`TUNE` tuning value or provisional number · `OPEN` explicitly unresolved
question · `HISTORY` version archaeology, rejected alternative, or design
commentary.

**`weight`** — publication weight, independent of type:
`STATE` the finished GDD states this as fact about the world ·
`SHOW` the game must show it, whether or not it is stated ·
`SAY` in-world voice · `SILENT` internal only, never reaches the reader.

> Apply the lantern test: would this sentence appear in a book describing
> MEDIAN, or is it commentary about the process of designing MEDIAN? Process
> commentary is `SILENT`, whatever else it is.

**`status`** — `canonical` · `provisional` · `example` · `rationale` ·
`historical` · `tuning` · `unresolved` · `superseded` · `rejected`.

**`owner`** — one namespace from the supplied list, exactly as written. If none
fits, use your best guess **and** add the flag `owner_unclear`. Never invent a
namespace.

**`terms`** — capitalised MEDIAN system terms appearing in the quote
(`Citizen`, `Capacity`, `Reach`). Ordinary words are not terms.

**`deps`** — record IDs from *this chunk* that this claim depends on. Leave
empty if unsure. Do not guess at IDs outside this chunk.

**`flags`** — zero or more of: `possible_collision`, `owner_unclear`,
`claim_exceeds_quote`, `split_claim`, `table_derived`, `non_state_marker`,
`internal_supersession`.

## Standing rules

**Do not resolve canon.** If two passages appear to contradict each other,
create both records and flag each `possible_collision`. Choosing between them
is a human decision taken much later, with more context than you have.

**Honour the source's own weight markers.** Some sources explicitly mark
passages as not-STATE — "Designer commentary only", "Not STATE material",
"Developmental note", "Complexity-Drift Watch". Material under such a marker is
`weight: SILENT`, whatever it appears to say. Flag it `non_state_marker`.

**Honour internal supersession.** Some sources state that a later ruling
overrides an earlier one within the same document. When a passage is overridden
by something later in the same source, still record it, set `status:
superseded`, and flag `internal_supersession`. Do not silently drop it.

**Do not upgrade examples.** An illustration stays `EXAMPLE` even when it
implies a rule. If an example appears to settle a question the prose leaves
open, record it as `EXAMPLE` and flag `possible_collision`.

**Preserve every condition.** Triggers, exceptions, tie-breakers, units, and
exact formulae must survive into the quote. A rule stripped of its exception is
a different rule.

**Tables are canon.** Extract table rows as records, one per meaningful row,
flagged `table_derived`. Quote the row.

**Context blocks are context.** Some blocks are marked as carried-over context
from the previous chunk. Read them for continuity, but do **not** create
records from them — they are owned by the previous chunk and will be extracted
there. Create records only from blocks in the OWNED list.

## Coverage

Every owned block should either produce at least one record, or be one of:
a heading, navigational text, a pure transition sentence, or document
furniture. If an owned block produces nothing, that is acceptable — the
coverage ledger will show it and a human will check. Do not invent a record to
fill a gap.

## Input

You will receive:

- the source ID, its class, and its wording-fidelity ceiling
- any source-specific handling notes
- the list of namespaces
- the starting record number
- the chunk, with `<!--@coordinate-->` markers before every block
- the OWNED coordinate list and the CONTEXT coordinate list
