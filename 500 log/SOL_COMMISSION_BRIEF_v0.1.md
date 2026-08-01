# Commission brief for the Sol thread — v0.1, 1 August 2026

Four requests, in priority order. Each asks for something that **exists only in
the authoring thread** and cannot be recovered by reading the documents. Paste
one at a time; they are independent.

A note on why the first registry worked so well mechanically: it was a table
with one row per term and stable columns. That parsed at 266 of 266 records
with no manual repair. **Please keep the same table discipline** — one row per
item, fixed columns, no prose inside cells beyond a sentence. Prose sections
around the tables are welcome; prose *instead of* tables is expensive to use.

---

## 1. Crossing terminology addendum — HIGHEST PRIORITY

**Why:** the Provisional Namespace and Terminology Registry v0.1 has no
source-owner code for the Crossing Register Specification. Its owner codes run
PHIL, HOME, EMB, ECO, MAN, MKT, AWAY, 4S, POP, GUEST2, BSA01-11, BSA12-22,
PHIL-ARCH, APP-PLAN, GDD046 — no CROSS. Only four Crossing terms appear
anywhere in its 266, and all four are sourced from AWAY, BSA12-22 or the
deprecated v0.4.6 language. The registry states the gap itself: "deliberately
provisional because the future Crossing specification... may require
additions", and its section 5 lists "Crossing/RISK: exact traffic taxonomy,
acuity language, interface labels and implementation-facing terms" as open.

This is the single largest hole, and it is in the register where compilation is
already struggling: 48 extracted claims currently have no system to belong to.

**Request:** an addendum in the same format as the v0.1 registry, covering the
Crossing Register Specification. In particular:

- The phase vocabulary — Planning, Commitment, Continuous Run, Resolution.
  Exact canonical forms, and whether "Staging" is a phase, a property of a
  phase, or something else.
- Traffic taxonomy: lanes, windows, gaps, the four Highway conditions, and any
  acuity or readability language.
- Adversity vocabulary: what attaches to the party globally versus to an
  individual Citizen, and the canonical names for each.
- Core Species crossing expression: the canonical name for the Mouse chain /
  Rabbit window / Squirrel route grammar, if one exists.
- Anything in the Crossing spec that **supersedes** language settled elsewhere.

---

## 2. Supersession and authoring-order ledger — HIGH PRIORITY

**Why:** the v0.5 specifications were written over roughly three days, and
later documents knowingly reconceived mechanics that earlier v0.5 documents had
already settled. That intent lives in the thread. The documents record the
outcome but rarely record *that they were overriding something*, and where they
do it is usually within a single document rather than across the set.

Without this, contradiction resolution can only detect that two passages
disagree — not which side was meant to win. Filename dates are a weak proxy and
should not be used as authority on their own.

**Request:** one table, one row per known supersession:

| Superseded claim | Where it was stated | What replaced it | Where the replacement was stated | Deliberate or drift? |

Plus, separately, a simple ordered list of the v0.5 documents in the order they
were authored, with one line each on what problem the document was written to
solve. Approximate order is fine; the reasoning matters more than the timestamp.

---

## 3. Open decisions register, with current lean — MEDIUM

**Why:** every explicitly unresolved item in the corpus will eventually need a
human ruling. Many of them were discussed in the thread and have a working lean
that never made it into a document.

**Request:** one table:

| Open question | Where it surfaces | Current lean, if any | What would settle it | Blocking or deferrable? |

"No lean" is a useful answer and should be recorded as such rather than
omitted. A lean recorded here is **advisory, not canon** — it will be presented
as a recommendation to be ruled on, not as a settled decision.

---

## 4. Rejected alternatives — MEDIUM, and partly for the book

**Why:** the compiler has a record type for design history — rejected
alternatives, version archaeology, why a system is shaped the way it is. Source
documents almost never contain it, because a spec states what *is*. The thread
contains what was considered and set aside.

This has two uses: it prevents re-litigating settled questions, and the good
ones are publishable as design commentary in the Concept Sourcebook.

**Request:** one table:

| Alternative considered | For which system | Why rejected | Would it be interesting to a reader? |

---

## What NOT to commission

Recorded here so it is not requested twice.

- **A revised full namespace.** We have one, reconciled against the registry,
  with an append-only ruling ledger carrying provenance for every decision.
  A second full tree would create a third authority to reconcile rather than
  resolving anything.
- **Extraction, classification or record-making.** That is the compiler's job
  and it runs against a fixed schema.
- **Anything derivable from the documents themselves.** Section headings,
  term frequency, structure and coverage are already computed locally at no
  cost. Only commission what needs the thread.
