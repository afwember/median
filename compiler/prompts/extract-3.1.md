# MEDIAN extraction — Pass A
# prompt_version: 3.1
# schema_version: 3.0
#
# Frozen artifact. Changing this file invalidates every record produced with a
# previous version (compiler spec §7). Bump the version; do not edit in place
# once corpus extraction has run.
#
# v2.0 changes, driven by measurement of a real v1.0 call:
#   - `quote` is no longer emitted. The compiler already holds the block text
#     keyed by `loc`; buying it back at output rates cost 33% of every record.
#     The model now emits two short span markers and the compiler resolves the
#     full quotation deterministically.
#   - `id`, `src`, `terms` and `deps` are no longer emitted. The compiler
#     assigns IDs, derives `src` from the ID prefix, and finds terms by lexicon
#     scan. v1.0 omitted `src` on every record anyway, which would have failed
#     validation corpus-wide.
#   Net effect: ~40% fewer output tokens per record, and four fewer fields the
#   model can get wrong.
#
# v2.1: `split_claim` was applied to 45 of 121 records on SPEC_CROSS, but 27 of
#   those spans ended mid-block, so the claim provably could not continue
#   anywhere. The flag was being read as "this block holds more than this one
#   claim", which is the normal case and not a flag at all. Defined precisely
#   below, with the negative case spelled out.
#
# v3.0: `weight` (STATE/SHOW/SAY/SILENT) is replaced by `voice`
#   (world/process). Three of the four weight values are decided after the
#   architecture is frozen — SAY at the Stage 9 harvest, SHOW in Stage 10
#   Section Contracts — so asking for them here asks a question whose answer
#   does not exist yet. Across 297 pilot records the field became a noisy
#   restatement of `type`: 8 GUARDs and 10 OPENs marked SILENT, conflating
#   "not yet settled" (status) with "not published" (weight). Only the lantern
#   test is knowable from the passage alone, and that is what `voice` asks.
#
# v3.1, four changes:
#   - BUG: v3.0 replaced `weight` with `voice` in its header and its example,
#     but left the `weight` field specification in the body. The schema forbids
#     unknown fields, so a model following the body would have produced an
#     unparseable response. `voice` is now specified where `weight` was.
#   - `branch_charter` added. A namespace with children accumulates systems and
#     is not one, so owning a record to it says only "somewhere in here" — with
#     one exception, measured: 8 of 56 bare `away.crossing` records defined the
#     register as a whole and belonged to no leaf. Charter is now sayable, so
#     the remaining 48 read as the missing system they are.
#   - The subject/system seam. The Citizen is MEDIAN's base person unit and
#     roughly 80% of rules concern Citizens, which makes `citizen` an attractor
#     that would swallow the corpus.
#   - The transverse/longitudinal seam, after `world.corridor` was found to
#     conflate the cross-section of one Reach with the chain of Reaches.

## Task

You are decomposing one chunk of one MEDIAN design source into atomic canon
records. You are not summarising, not resolving contradictions, and not
deciding what is true. You are making each independently actionable claim in
this chunk separately addressable.

Return JSON only: an object with a single key `records`, whose value is an
array of record objects. No prose, no preamble. Records must appear in
document order.

## What counts as one record

One record is one independently actionable claim: a requirement, a
prohibition, a definition, an interface instruction, an illustrative example, a
line of in-world voice, a tuning value, an open question, or a note about
history.

Split a paragraph that states three separate rules into three records. Keep a
single rule that spans three sentences as one record. If a sentence states a
rule *and* its rationale, the rule is the record; include the rationale as a
separate record with `status: rationale` only if it carries mechanical
consequence.

Do not create records for: headings on their own, navigational text, table of
contents entries, or running document furniture.

## Fields

**`loc`** — the coordinate of the block this claim came from, copied exactly
from the `<!--@...-->` marker above it.

> **Coordinates are opaque strings.** `3.1#2` is a different location from
> `3.1`. `4.2¶7` differs from `4.2¶7#2`. Copy the marker character for
> character. Do not normalise, tidy, renumber, or strip a `#n` suffix. A
> "corrected" coordinate points the record at the wrong passage and will fail
> verification.

**`q0`** — the **first four to eight words** of the operative passage, copied
verbatim from the block, exactly as written.

**`q1`** — the **last three to six words** of the same passage, verbatim.

> `q0` and `q1` mark a span. The compiler locates them in the block and
> recovers the full quotation between them, so you never need to reproduce the
> passage itself. Both markers must appear verbatim in the block, `q1` at or
> after `q0`. Copy punctuation and capitalisation as they appear. If the whole
> block is the passage, use its first and last words.
>
> The span must carry the entire condition, including its exceptions and
> qualifiers. A rule stripped of its exception is a different rule — choose
> `q1` accordingly.

**`claim`** — one compact sentence stating what the span establishes, in
neutral present tense. It must not assert more than the span supports: if the
source says "usually", the claim may not say "always". If you cannot state the
claim without exceeding the span, add the flag `claim_exceeds_quote`.

**`type`** — `REQ` operative requirement · `GUARD` prohibition, limit or
guardrail · `TERM` definition or terminology note · `UI` interface or
presentation instruction · `EXAMPLE` illustration · `SAY` in-world voice or
folklore · `TUNE` tuning value or provisional number · `OPEN` explicitly
unresolved question · `HISTORY` version archaeology, rejected alternative, or
design commentary.

**`voice`** — `world` the passage describes MEDIAN · `process` the passage
describes the work of designing MEDIAN.

> Apply the lantern test: would this sentence appear in a book describing
> MEDIAN, or is it commentary about the process of designing MEDIAN? Rationale,
> acceptance tests, complexity guards, version archaeology and notes to the
> designer are `process`, whatever else they are.
>
> Do not emit `weight`. Publication weight is decided after the architecture is
> frozen; a `weight` field will be rejected.

**`status`** — `canonical` · `provisional` · `example` · `rationale` ·
`historical` · `tuning` · `unresolved` · `superseded` · `rejected`.

**`owner`** — one namespace from the supplied list, exactly as written. Each
arrives with a one-line description of what it owns; use it. If none fits, give
your best guess **and** add the flag `owner_unclear`. Never invent a namespace.

> **The use/make seam.** `items.*` covers *using* an item unit;
> `economy.recipes` covers *making* one. "A Crafter prepares Supplies from
> Flexible Scrap" is `economy.recipes`. "A Supply is consumed when its effect
> is applied" is `items.supplies`. More generally: who does it and where it
> happens at Home is `home.dwell.*`, what is produced and by what recipe is
> `economy.*`, what the object does in a Citizen's hands is `items.*`.

> **Mode and Register are in the name.** Home Mode contains DWELL and EMBODY;
> Away Mode contains FIELD and CROSSING; MEET is universal, reachable from
> either Mode. A Home rule about Roles is `home.dwell.roles`, not `home`.
> Prefer the most specific namespace that is clearly correct.

> **The subject/system seam.** A rule is owned by the system that *governs* it,
> never by the subject it acts upon. The Citizen is MEDIAN's base person unit
> and nearly every rule mentions one, so `citizen.*` is reserved for claims
> about the Citizen unit itself. "A Citizen carries weight up the cooperative
> ladder" is `economy.carrying`. "A Citizen occupies one Role at a time" is
> `home.dwell.roles`. "A Citizen is a named colony member with one equal Home
> share" is `citizen`. The test: strike the word Citizen and see what the rule
> is about. If a system remains, the system owns it.

> **The transverse/longitudinal seam.** `world.reach` is the cross-section —
> one slice across the road: Sound Wall, Margin, Highway, Median, Highway,
> Margin, Sound Wall. `world.corridor` is the chain of Median Reach units laid
> end to end. What a Margin *is* goes to `world.reach`; how Reaches *join* goes
> to `world.corridor`. Separately, `away.corridor` is the expedition's progress
> along the ground, not the ground itself.

**`flags`** — omit entirely when empty. Otherwise any of:
`possible_collision`, `owner_unclear`, `claim_exceeds_quote`, `split_claim`,
`table_derived`, `non_state_marker`, `internal_supersession`,
`branch_charter`.

> **A branch is a shelf; a leaf is a system.** Namespaces marked `[container]`
> in the list have children, and owning a record to one usually says only
> "somewhere in here", which is not an owner. Name the leaf.
>
> The exception is a claim that defines the container *as a whole* — what the
> register is, what it is not, or how its parts relate to each other. "Crossing
> is a short, high-attention threshold Register, neither an ordinary Field leg
> nor a turn-based encounter" belongs to no leaf and must not be forced into
> one. Own it to the container and flag `branch_charter`.
>
> The distinction is between a claim about the *whole* and a claim about a
> *part*. "Planning is the phase of observing the road" is about a part; if no
> leaf fits it, that is a missing system — use `owner_unclear`, not
> `branch_charter`. Do not use `branch_charter` on a leaf.

> **`split_claim` means the sentence is cut off**, not that the block contains
> other claims. Use it only when the passage you are quoting runs past the end
> of this block and its rule is therefore incomplete here — a condition whose
> exception is in the next block, a list that continues, a formula whose terms
> are defined after the break.
>
> A block containing three separate rules is the ordinary case: emit three
> records and flag none of them. If your span ends before the end of the block,
> the claim cannot be continuing elsewhere, so `split_claim` is wrong.

Do not emit `id`, `src`, `quote`, `terms` or `deps`. The compiler supplies all
five.

## Standing rules

**Do not resolve canon.** If two passages appear to contradict each other,
create both records and flag each `possible_collision`. Choosing between them
is a human decision taken later, with more context than you have.

**Honour the source's own markers.** Some sources explicitly mark passages as
design commentary — "Designer commentary only", "Not STATE material",
"Developmental note", "Complexity-Drift Watch". Material under such a marker is
`voice: process`, whatever it appears to say. Flag it `non_state_marker`.

**Honour internal supersession.** When a passage is overridden by something
later in the same source, still record it, set `status: superseded`, and flag
`internal_supersession`. Do not silently drop it.

**Do not upgrade examples.** An illustration stays `EXAMPLE` even when it
implies a rule. If an example appears to settle a question the prose leaves
open, record it as `EXAMPLE` and flag `possible_collision`.

**Tables are canon.** Extract meaningful table rows as records, one per row,
flagged `table_derived`. Use the row's opening and closing words as the span.

**Context blocks are context.** Blocks in the CONTEXT list are carried over
from the previous chunk. Read them for continuity; do **not** create records
from them. Create records only from blocks in the OWNED list.

## Coverage

Every owned block should either produce at least one record, or be a heading,
navigational text, a pure transition, or document furniture. If an owned block
produces nothing, that is acceptable — the coverage ledger will show it and a
human will check. Do not invent a record to fill a gap.

## Example

For a block marked `<!--@4.2¶3-->` reading:

    Each present and available Citizen contributes one unit of Role Capacity,
    except while Away, in which case they contribute none.

emit:

    {"loc":"4.2¶3",
     "q0":"Each present and available Citizen",
     "q1":"they contribute none.",
     "claim":"Each present and available Citizen contributes one unit of Role Capacity, and none while Away.",
     "type":"REQ","voice":"world","status":"canonical","owner":"home.dwell.roles"}
