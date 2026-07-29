# Review — MEDIAN-OVERVIEW_compressed.pdf

A 45-slide in-progress overview deck, reviewed against `100 canon/MEDIAN_GDD_v0.4.6.md` and the `500 log/v0.4.7_decisions.md` (V6) direction. The deck's own slide 3 discloses that visuals and charts are stylistic concept art and may be outdated — that covers most of what's below. This review focuses on what the disclosure doesn't cover: real proper-noun violations, a depicted-weapons violation, and a couple of internal contradictions that are content problems, not style problems.

---

## Priority findings — not covered by the "stylistic staleness" disclosure

**1. "Fiver" and "Kehaar" are used as named, quoted sources — a direct Section 1.1 violation, repeated three times.**

Fiver and Kehaar are both real *Watership Down* characters, and Section 1.1 is unconditional: no real Watership Down proper nouns anywhere in MEDIAN's fiction. This isn't a stylistic issue the disclosure can absorb — it's fictional content, attributed as a quote:

- Slide 6: *"'I do not belong to you,' said Kehaar. 'But I fly here because it matters.'"* — Kehaar also appears as a named "Scout" Guest card on slides 4 and 6.
- Slide 28: *"'We have more than the warren. We have each other, and we have the land.' — Fiver"*
- Slide 37: the same Fiver quote, reused as the Rest Stop Metropolis DLC slide's closing line.

The Fiver line is doing double duty as a recurring hero quote, so it isn't a one-off slip — it needs a replacement line wherever it's used, and Kehaar needs to come off the Guest roster art (slides 4, 6) entirely, not just get renamed.

**2. Slide 29 depicts mice carrying rifles in a fortified tower position.**

Canon's "never depicted" list is explicit: no weapons, ever. Slide 29 (mice on a rusted-engine watchtower, armed, in a militia-like formation) is a clean, unambiguous violation — not an "outdated concept art" case, since weapons are prohibited regardless of art style or draft stage. Slide 1's cover image (mice apparently carrying spear-like implements) is the same issue at lower confidence — worth a second look at full resolution, but slide 29 alone is enough to flag this as a pattern to sweep the whole asset library for, not a single fixable image.

**3. Slide 28 frames Fox, Weasel, Raccoon, and Owl as predators to defend against — the opposite of what they are in canon.**

Slide 28 ("3. Predators") lists Red Fox, Long-Tailed Weasel, Raccoon, and Great Horned Owl as threats with "risk levels" and "defenses." But in the shipped v0.4.6 Guest Citizens system, Fox, Weasel, and Raccoon are three of the seven **Active Guests**, and Owl is one of the nine **Ambient Guests** — named individuals the player recruits, bonds with, and houses. Snake has the same double-cast problem (a "Creeping Threat" on slide 28, an Active Guest in canon). This isn't staleness so much as two irreconcilable framings of the same species sitting in the same deck; slide 14 (labeled "Guest Mechanic / v0.4.6," and verified accurate against canon — see below) is almost certainly the one to keep, and slide 28 the one to retire or rebuild around a *different* set of threats (weather, traffic, the "Giant Predators" — Lawn Mower, Snow Plow, Weed Trimmer — are a fun, canon-compatible idea and could anchor a rebuilt version of this slide on their own).

---

## What's actually accurate — more of the deck than the sampled early slides suggest

The first few slides (and the "v0.2"-labeled ones) skew toward older material, but a lot of the deck's text-heavy, structural slides are precisely current:

- Slide 14 ("Guest Citizens: Two Ways to Belong," labeled v0.4.6) — the 7 Active / 9 Ambient rosters, names, and the benefit/affinity/complication template all match canon exactly.
- Slides 19–20 (world cross-section, Four Registers) and slide 31 (Crossing/Field/Encounter/Exposure) — match canon closely, including body-unit resolution and the exposure-widens-the-distribution mechanic.
- Slide 16 (Work/Construction/Records) and slide 27 (the Economy) — accurate down to specific field names (Rigid/Flexible Scrap, Special Artifacts, the Community Board/Story Circle split).
- Slides 34–35 (Laws of the Median, the "Sharpnose at the fallen log" Tale) — original folklore and worked example, well-executed, no issues.
- Slides 40–42 (Table of Contents) are literal excerpts of `MEDIAN_GDD_v0.4.6.md` and match the shipped document's structure section-for-section.
- Slide 8 (Manor House / Cul-de-Sac / Web) is, notably, the spatial spec content itself already in the deck — meaning this slide is actually *ahead* of shipped canon, matching the direction of decision V6-1 before that decision was formally logged.

## Where the deck disagrees with itself (old drafts left in place, not clearly marked)

A few slides are explicitly self-aware about being drafts — slides 7 and 21 are labeled "v0.2 SPEC" — and those are fine as-is; a versioned old draft in an in-progress deck is expected. The more confusing case is slide 12 ("Three Species, Three Spatial Civilizations"), which has no version label and states Rabbit = Warren Flow / underground with specific stat values, directly contradicting the Cul-de-Sac imagery on slides 8, 10, and 11 a few pages earlier. A reader hitting slide 12 cold would reasonably think it's the current answer. Worth a version label at minimum, or removal now that V6-1 has decided the question.

Two smaller labeling issues: slide 22 identifies the mouse as "RAT," which isn't a MEDIAN species; and slide 6's Guest roster (Corvus, Old Fox, Mossback, Otter, Badger) invents four species/names outside the 16-strong canon roster — separate from the Kehaar violation on the same slide, this roster just isn't the one in the game.

## Corrected in the GDD directly, in passing

While cross-checking slide 43's "excerpted from the GDD" text against the actual document, I found the deck was quoting real (if odd) content: Section 23.1 of the shipped `MEDIAN_GDD_v0.4.6.md` used *"the Oakenshield half of a name"* as its illustrative example — Oakenshield being Thorin Oakenshield, a real Tolkien character. That's not a Section 1.1 violation (the rule is specifically about Watership Down), but it's the same category of problem at smaller scale, and it was a genuine authoring slip from the v0.4.6 assembly, not a deck error. Fixed directly in the GDD: the example now reads "the Flood-wise half of a name, as in Sharpnose Flood-wise," reusing the name already established at line 1274 of the same document rather than borrowing one from outside MEDIAN entirely.

## Not flagged individually — covered by the deck's own disclosure

Garbled/corrupted text is heavy on several slides (18, 22, 28, 30, 37 especially) — placeholder-looking body copy, mangled Latin binomials, a "Build. Father. Serve." misrender of the actual philosophy line. This is image-gen artifacting, not a content decision, and the deck says as much on slide 3. Real-world photo references (slide 24's biome photos, including a visible cigarette butt) read as mood-board material rather than final art and don't need individual notes. One small non-canon item: slide 38's "Iron Skillet Travel Plaza" signage uses a real truck-stop restaurant chain's name in the background — probably worth swapping for an invented chain if this art gets reused publicly, but it's a trademark housekeeping note, not a MEDIAN canon issue.

**Caveat on the garbled-text finding above:** the version reviewed was `MEDIAN-OVERVIEW_compressed.pdf`, converted to images at 30dpi to get all 45 pages through in one pass. A follow-up look at nine higher-resolution slides supplied separately (Choice-Event Cards, the Seven Design Pillars, Encounters, the Founding Escape, the Rest-Stop Metropolis, Road Work, Median at the Table, Tharn, and The Margin) rendered perfectly clean, with no text corruption at all. It's possible some of the "garbled" slides above are actually fine at full resolution and what I was seeing was my own conversion pipeline, not the deck. Worth a second pass at higher fidelity before treating slides 18/22/28/30/37 as needing text regeneration.

## Addendum — nine additional slides reviewed at full resolution

Choice-Event Cards, the Seven Design Pillars, Encounters, the Founding Escape, the Rest-Stop Metropolis, Road Work, Median at the Table, Tharn, and The Margin — all check out clean. No Watership Down names, no weapons, no predator/Guest contradictions. These are some of the most mechanically precise slides in the deck: the Encounters slide gets the five Approaches, the four-round hard cap, and "exposure widens the distribution, it does not shift it" exactly right; Road Work's Telegraph/Onset/Persistence structure and the Second Law quote match canon verbatim; The Margin nails "renewable, never buildable," Wind Draft, and the River's Spume precisely. Median at the Table is a pleasant surprise — concept art for the manifest-only Appendix F (tabletop) and Appendix G (card game), which doesn't appear anywhere else in the deck.

One minor, recurring pattern shows up again here: a Heron appears as a cameo in two of these slides (Encounters, Median at the Table), alongside a Weasel used as a generic Encounter adversary. Neither is a violation — Heron just isn't one of the 16 canon Guests, the same pattern as Otter/Badger/Opossum/Mossback elsewhere in the deck, and Weasel-as-adversary is consistent with canon's own §21.3 "antagonist fauna... who can change sides" rather than a contradiction like the slide-28 case.

---

## Summary

The deck's newest, most textual material (Guest Citizens, the Four Registers, the Economy, the Laws, the actual GDD excerpts) is accurate and well-aligned with v0.4.6. The problems worth acting on before this deck goes anywhere external are: the Fiver/Kehaar quotes (three instances, easy to find, non-negotiable to fix), the armed-mice image on slide 29 (and a second look at slide 1), and the Fox/Weasel/Raccoon/Owl predator-vs-Guest contradiction on slide 28. Everything else is either already-disclosed staleness or small labeling noise.
