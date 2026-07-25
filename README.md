# MEDIAN

**An atmospheric animal colony-builder set on highway median strips** — "Age of Empires minus combat, with the heart of *Watership Down*." The player guides one small civilization of rabbits, squirrels, or wood mice, builds a permanent low-population colony in the green island between carriageways, and risks named citizens on expeditions across live traffic and along a corridor of changing median biomes.

*Conceived by Asa Wember, July 2026, after observing highway medians from a bus between Washington, DC and New York.*

**This repository is the working home of an illustrated concept book** — a complete, art-heavy sourcebook in the tradition of Classic Traveller, AD&D 2E, Star Wars D6 and *Mouse Guard*. Not a production design document for a game in development. The book is the deliverable.

---

## Where things stand

| | |
|---|---|
| **Canon** | `canon/MEDIAN_GDD_v0.4.3.md` — 93 settled design decisions |
| **Book plan** | 49 plates · 8 part openers · in-part artwork · 5 worked examples |
| **Complete** | 1 plate — *The Three Species* |
| **Format** | 16:9 landscape, desktop-first, three-column text grid |
| **Blocking** | Stage 2c — palette, typography, grid, page furniture |
| **Next** | *The Median Read Three Ways*, then the rest of Part I |

---

## How to read this repository

**Start with `canon/`.** The GDD is the single source of truth. Where anything in this repository disagrees with it, the GDD wins and the other document changes.

**`book/Contents.md` is the map.** It merges the GDD's structure with the illustration programme — every plate, opener and worked example placed against the sections it draws from, with its editorial claim and status.

**`log/` is why, not what.** `running_decisions.md` records production decisions as they lock, numbered P2-1 upward, including reversals and the reasoning behind them. `art_raised_questions.md` records design gaps the artwork exposes — logged, deliberately not solved, feeding a future canon pass.

---

## Layout

```
canon/      The GDD. Source of truth.
book/       Contents and the Phase 2 production plan.
log/        Decisions as they lock; questions as they arise.
prompts/    Illustration prompts, one per plate.
              _superseded/  kept as a record of approaches that failed, and why.
art/
  plates/   Finished information-design plates.
  keyart/   Part openers and full-page artwork.
  legacy/   Five decks and three loose images predating this pass,
            plus the v0.4 planning documents they were made against.
            Source material only — see the warning below.
wip/        Working iterations. Not tracked by git.
```

### A standing warning about `art/legacy/`

Those 52 assets were produced without canon rigor. **Their text is improvised and carries no authority** — labels, callouts, taxonomies and any concept a plate appears to assert are unverified, and most of it did not survive checking. Several assert things canon explicitly rejects: rats and raccoons as colony citizens, pheromone routing, canopy routes that bypass traffic, a standalone currency, industrial tiers.

**Mine them for pictures and arrangement. Take nothing from them as fact.**

---

## Working rules

These have each been earned by getting something wrong.

**A decision is not done until the log entry and every affected document land in the same commit.** Twice, a settled decision lived only in the log while a plan file still stated the reverse. One commit per decision makes that visible.

**All plate copy is written fresh from the GDD.** Never carried over from a legacy asset, never invented to fill a gap.

**Specify every string in an illustration prompt.** Generated text renders cleanly where the prompt supplies it verbatim, and turns to gibberish where the model is left to invent. This is the single most useful production finding in the project.

**Any upscale is a re-generation.** It preserves art and corrupts type, and it silently drifts detail. Re-check canon after one, every time.

**Log design gaps; do not solve them.** Phase 2 is production, not a second design thread. Gaps go to `log/art_raised_questions.md`.
