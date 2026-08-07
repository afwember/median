# OP — Decisions log → Change Guide

**A standing operation. Run it on any completed decisions thread before compiling a new GDD edition.**

Paste this as the first message of a fresh thread, with the decisions log attached. **Use a heavy model at high effort.** This is the judgment pass; the compile that follows it is clerical and can run lighter.

---

## What this does

Converts a verbose decision log — argued, discursive, written to persuade — into an **executable change guide**: a specification an assembler can follow without ever reading the log.

The guide is the artifact the compile consumes. **After this operation runs, the decisions log is never opened again.**

---

## Why it is necessary

A decision log has to be persuasive. It is arguing a case to a future reader who might reopen the question, and persuasion needs a foil — so **every entry carries the alternative it rejects welded to the claim it makes.** You cannot lift the claim without lifting the argument.

v0.4.5 was assembled straight from the logs. The result: 115 sentences lifted substantially verbatim, and a document that continually litigated its own design. The measured signature was not the obvious one. *"Rather than"* was barely elevated. What leaked was the **restraint-audit register** — sentences whose job is to certify design compliance to another designer:

> *already exists* · *no new system* · *no new machinery* · *without adding* · *at no cost* · *costs nothing* · *worth stating* · *which is the point* · *what X was reaching for*

Those phrases ran three to nine times denser in the logs than in the book. They are the tell.

There is a second, subtler leak. The house rule *"the book states what is, never what was rejected"* hunts version archaeology — *earlier*, *formerly*, *superseded*. But the dominant tic is **arguing with hypotheticals that were never in any draft**: *role reads from kit, not livery* · *a Presence, never a counted roster*. The rule's letter was followed and its spirit escaped through a side door. Watch for contrastive definition, not just history.

---

## Inputs and output

**In:** the decisions log for this edition, plus any prior-edition log with unapplied items. The base GDD, for locating what each decision touches.

**Out:** one change guide, `500 log/MEDIAN_change_guide_vX_to_vY.md`.

---

## The four weights

Assign one to every decision. **This is the most important judgment in the operation** — it decides whether a change earns words in the book at all.

| | |
|---|---|
| **state** | The book asserts it in prose. |
| **show** | The book must **not** assert it. An example, table, Record excerpt, caption or illustration carries it. Name which one. |
| **say** | A Law or Saying carries the feeling, set as typography on the page rather than another body paragraph. **Additive** — it never licenses cutting text that carries a concept. |
| **silent** | True of the game. Governs authoring, art, or a future pass. Earns no sentence. |

**Expect a quarter to a third to be silent, and expect that to surprise you.** The natural failure of this operation is over-assigning `state`, because a decision log's every entry *feels* like it needs saying — that is what a log is for. Most rules can govern an imagined game without being announced in it.

---

## The three fields

**STATE** — the only text permitted to become prose. Declarative, world-facing, positive. It defines the complete semantic payload; the assembler integrates it into the surrounding voice rather than pasting it. **It contains no reference to what it replaces, no rationale, and no comparison to a design alternative.**

**DO** — an edit action on the base document. Executed, then discarded. It may name old text, use imperatives, and reference what is being removed, precisely because **no DO text may reach the output in any form.**

**WHY** — one line, collected in a quarantined Archive at the end of the guide, keyed by entry ID. Consulted only when a decision is challenged. Physically separating it is the point: importing rationale should require a deliberate lookup.

---

## Procedure, per decision

**1. Find the canonical result.** Ask: *if this were already true and always had been, what would the book say?* That sentence is the STATE candidate. It is usually already in the entry, often as the bolded lead.

**2. Find the foil and quarantine it.** Almost every entry names an alternative — a rejected option, a previous rule, a hypothetical. Mark it. It goes to WHY, never to STATE.

**3. Assign the weight**, in this order:

- Could an animal in the world plausibly say this? → **say**
- Would a reader learn it from a picture, a table, or a worked example without being told? → **show**
- Does it govern authoring, art, or a future pass rather than the reader's understanding? → **silent**
- Is it a rule the reader must hold and cannot infer? → **state**

**4. Apply the lantern test.** *Does this sentence tell me about the world, or about the design?* If its subject is the design, it does not go in the book. The check: could it survive translation into an in-world voice? *The Margin is rich at both edges, in different goods* survives. *No new system — an existing modifier slot gains an existing quantity* cannot be said by anyone who lives there.

**5. Check for reversal.** `silent` works cleanly when a decision **adds**. When a decision **reverses** existing text, the old passage's thesis sentence has to be *replaced*, not merely deleted — otherwise the section is left with no thesis. A reversing `silent` usually still needs one clause. Flag these; they are the commonest execution failure.

**6. Delete assertions, protect concepts.** When cutting, remove claims about what is *not* true, what was *not* chosen, and what the design *avoided*. Keep causes, mechanisms and distinctions a reader needs. A beautiful line that costs the reader an idea is a bad trade.

**7. Write the DO** as an imperative edit action, naming the base text to be changed. Be blunt; none of it survives.

**8. Compress WHY to one line.**

---

## Sorting into phases

The guide is ordered by execution, not by decision number.

**Phase 0 — Global.** Decisions that apply document-wide: terminology replacements, sweeps, orthography, standing conventions.

**Phase 1 — Structure.** Anything that moves, splits, inserts or dissolves a section, or changes the Contents. **Moves only — no prose.** Anchor every operation on old heading text, never on section numbers.

**Phase 2 — Numbering, Contents, cross-references. FREEZE.** Not decisions; a mandatory checkpoint. Give the explicit old→new map here, including any special cases. Everything after this composes references in *final* numbers.

**Phase 3 — Content.** Section by section, in final numbering.

**Phase 4 — Appendices.** Whatever the standing appendix policy is. Route the substance to the appendix guide.

**Phase 5 — Audit.** Scriptable checks, plus a weight check and the voice grep above.

**Then the ARCHIVE.** WHY lines, keyed.

**A structural decision is easy to miss** because logs record it as a content note. The tell: does executing it change a heading, a section number, or the Contents? If so it is Phase 1, however it was written.

---

## The `say` harvest

Do this as a separate pass over the whole log, because a decision log never proposes folklore and you will not find these by working entry-by-entry.

Scan for claims that an animal could say. Each becomes a proverb — one line, in the setting's register — entering §6.2 *and* quoted at its point of use, following the precedent of the Laws.

**It is the only weight that grows the book while improving it**, and it is nearly free: a claim that would cost a paragraph of exposition costs a line of folklore instead. But it is **additive**. It displaces the gloss around a rule, never the rule, and never a cause the reader needs.

---

## Traps

**Decisions that settle something the log says is deferred.** Watch for an entry that demonstrates by example what another entry marks open. Showing it in fiction still settles it. Mark the entry `provisional` or strip the claim.

**One decision touching many sections.** Give it one entry per section, or an explicit *throughout*. A single entry with five section references will be executed in one of them.

**Pure rejections.** Some entries produce no STATE at all — only a DO that deletes, and a WHY. That is a complete entry. Do not manufacture a positive statement for a decision whose content is *don't*.

**Decision numbers and counts.** They belong to the log and to the change record, never to the book. A front-matter line announcing *governed by 157 settled decisions* tells the reader they are holding a legal instrument.

**Your own summary voice.** The guide's prose is not the book's prose, but STATE is. Keep STATE clean even where the surrounding entry is telegraphic.

---

## Output template

```
**C-nn · Short title** — *weight* · §refs · SRC decision-ids
STATE: (declarative, world-facing, positive; omit if silent or pure rejection)
SHOW: (what carries it, named; only for show)
SAY: (the proverb; only for say)
DO: (imperative edit actions on the base)
```

Archive, at the end:

```
- **C-nn** One line of rationale. Never enters the book.
```

---

## Self-check before delivering

- Every decision in the log appears exactly once, or is explicitly noted as superseded by a later one.
- No STATE field contains a negation of a design alternative.
- No STATE field references what it replaces.
- Every `show` names its carrier. Every `say` has a written proverb.
- Structural decisions are all in Phase 1, and Phase 2 gives the full numbering map.
- The Archive is separate, keyed, and marked never-to-enter.
- Weight distribution reported. If almost everything is `state`, the operation has not been performed — go back to step 3.
- Deferred items are still deferred, with their briefs intact.
