# MEDIAN Phase 2 — Production Plan

**Supersedes:** `MEDIAN_v0.4_Infographic_Plan.md` and `MEDIAN_v0.4_Needed_Artwork.md`, both of which were written against v0.4 and are two revisions stale. Those two documents are merged here into one plan with two tracks.

**Canon:** `MEDIAN_GDD_v0.4.2.md`, 85 decisions. Where this plan and the GDD disagree, the GDD wins.

**Status:** Stage 1 deliverable, amended through Stage 2b.

**What this is for.** The book is the deliverable, not a specification for someone else to build a game from. That simplifies things: no downstream handoff, no art-team brief, no need to spec anything twice. It also means the work is done incrementally by one person over a long stretch, which changes the build order — see §7.

---

## 0. Standing rules for the pass

These govern every plate and override anything inherited from the old Plan or the handoff.

1. **The deck has one visual identity, applied uniformly.** Styling never varies with a plate's subject. There is no warm treatment for colony plates and cold treatment for crossing plates, no parchment-survey treatment for Field plates. One identity, all plates. *(This retires the handoff's "two visual languages" instruction — see §1.3.)*

2. **Plates are illustrative, not depictions of UI.** A plate is a drawn document about the game, not a frame of the game and not a screenshot. Where an interface genuinely is the subject, it appears as an **annotated inset specimen** sitting inside an illustrative plate — never as the plate's own surface.

3. **All copy is written fresh from the GDD.** No text from any existing plate is reusable. Labels, callouts, headings, taxonomies, and threat lists on the legacy plates are improvised and carry no canon weight.

4. **Mine the legacy decks for pictures and arrangement only** — drawings, compositions, info-box forms, diagram devices, framing.

5. **Layered, editable text on everything** (§33.1, Appendix D). Generated illustration inside a plate will be a raster layer; text, labels, callouts, and shape elements sit over it live. Output is `.pptx` unless changed.

6. **Log design gaps, do not solve them.** Anything a plate exposes goes to `MEDIAN_Phase2_art_raised_questions.md`. Phase 2 does not become a design thread.

7. **The reader is an enthusiast, not a designer.** The deck is a mix of a game design document and an RPG core sourcebook — the kind worth reading cover to cover. Information is decorated rather than stripped; in-world material is set apart from body text; designer-facing content recedes as the deck iterates. *(P2-13.)*

8. **No people, anywhere.** No human figures in any plate or concept art — tighter than §33.2, which permits them during Road Work and Founding-Escape-class threats. Those moments are carried by machinery alone. Vehicles are unaffected and remain constantly visible. *(P2-14.)*

### What rule 1 does *not* mean

Within-plate coding is not style variation. The *Turn of the Seasons* poster colour-codes five parallel season columns; that is ordinary information design inside one identity, and it stays available. Rule 1 governs the deck's identity across plates, not the coding of a taxonomy inside one.

9. **Every plate carries a claim, not a topic.** "Seasons" is a subject heading; *"Winter is not a debuff — it reorganizes the colony economy"* is an editorial idea the whole spread then proves. Canon supplies most of them ready-made.

10. **Every plate answers at least one play question.** What does the player choose · what do they risk · what do they not know · what can go wrong · what changes because of their decision. A plate that answers none of these is documenting a setting rather than a game.

11. **Bounded mystery.** Do not explain everything. A named Reach the player has heard of but never walked is worth more than six paragraphs about it. The test: *a good unexplained detail generates ideas; a bad one generates confusion.* Canon already supplies the mechanism — fog of war, folk names learned from rumor, and the Metropolis's contradictory Laws.

### What rule 2 costs us

Four plates in the old Plan were conceived as screens and must be reconceived: the Colony Dashboard, the Expedition Launcher, Field Mode, and Expedition Rating & Debrief. Their subjects survive; their format does not. See §4.

---

## 1. Concordance — v0.4 → v0.4.2

### 1.1 Section renumbering

Every cross-reference in the old Plan and Analysis is dead until remapped. The ones those documents actually used:

| Old ref (v0.4) | Subject | Now (v0.4.2) |
|---|---|---|
| §2.5 | Traffic-as-weather | §9.3 |
| §2.7 | Mechanical restraint pillar | §2.6 |
| §3.5 | Median chain / Reach | §7.5 |
| §3.7 | Anchor Points | §8.2 |
| §4.3 step 8 | "Record the story" | §5.3 step 8 |
| §5.3 | Seasons / sustenance fork | §10.1, §13 |
| §5.4 | Road Work active recovery | §10.2 |
| §6.3 | Scrap economy | §13 |
| §8.1 | Citizen dossier | §16 + §21.2 |
| §8.4 | Valuing a maimed citizen | §18.1, Pillar 2.5 |
| §9.3 | Field Mode | §24 |
| §9.6 | Contested node encounter | §25, §26.1 |
| §9.7 | Group-level resolution | §25.4, §25.5 |
| §13 | Rest-Stop Metropolis | Part VI, §29–30 |
| §13.3 | Legacy / continuation | §30.2 |
| §15.1 | Anthropomorphism | §33.1 |
| §15.2 | Scale language, humans off-screen | §33.2 |

Terminology renames applied document-wide: Expedition Guests → **Active Guests** · Fortified Warren → **Fortified Settlement** · Agnomen → **After-name** · Citizen dossier → **Character Record** (*Likeness* / *Tale*) · Sentimental → **Attachment-first** base-building · Median Zone → **Median Reach**.

### 1.2 Analysis recommendations that canon has since ruled on

The Analysis doc proposed pickups. v0.4.2 accepted most, changed two, and rejected three. **The three rejections matter most, because the old Plan builds plates on them.**

**Adopted — now canon, safe to plate:** citizen Keepsakes (§19) · Expedition Rating (§21.3) · Report and Share debrief (§21.3, *minus* the sharing bonus, which was cut) · Colony Record chronicle (§21.1) · named relationship pairs (§17.1) · Community Board (§15.3) · named event log (§21.1) · construction queue (§14) · Laws of the Median (§6.1) · Giants vocabulary (§6.3) · culture mottos, now the Sayings (§6.2) · Story Circle (§15.3) · Edge Effect / Quiet Zone (§9.3) · the three traffic hazards, now **Wind Draft, the River's Spume, Litter** (§9.3).

**Changed in canon — plate the new version, not the recommendation:**

- **Dual literal + folk place-naming is dead.** The Analysis recommended it (C12); §22.2 explicitly rules **one folk name per place plus functional metadata tags**, and Appendix B lists "two competing names per place" as superseded. Set 1's dual-name device ("Mowing Zone / The Burning") is now drift.
- **Traffic hazards were renamed and re-scoped.** Highway Draft / Road Spray / Thermal Plume became Wind Draft / the River's Spume (four manifestations: Heat, Cold, Exhaust, Oil Leak) / Litter. Chemical Runoff and Invasive Plants were **not** adopted as named hazards.

**Rejected in canon — do not plate:**

- **Roadside-PSA signage flavor** ("Leave a Gap, Save a Life," "All Creatures Welcome"). Listed under *Rejected on record* in Appendix B. The old Plan's end plate was built on this; it needs a new concept.
- **Intra-median sub-zones** (Set 2's "Lay of the Land"). §7.5 makes each Reach **unified and never internally sub-divided**; Appendix B lists sub-zones as superseded. Internal variation comes from Anchor Points only.
- **Reputation and Knowledge as tracked stats.** Rejected under Pillar 2.6 and Appendix A.

### 1.3 The handoff's "two visual languages" instruction is retired

The handoff asked that each plate be tagged with a visual pipeline — Rendered-embodied for Colony/Encounter/Crossing subjects, Illustrated-surveyed for Field subjects. That is styling varying by plate content, which Standing Rule 1 forbids.

**What survives is the distinction as subject matter.** A Field Mode plate still has to *depict* a naturalist's survey plate, because that is what §24.2 says the game's Field register looks like. It depicts one as an illustrated object; it is not *rendered as* one. Same for the other three registers: the plate shows them, it does not adopt them.

**The pipeline column is therefore reframed from styling to production** — what a plate needs *made*, which is a genuine plan-level fact:

| Tag | Meaning |
|---|---|
| **NEW** | Original illustration required; nothing usable exists |
| **HARVEST** | A usable drawing exists; recompose and correct |
| **DIAGRAM** | No scene — objects, specimens, structure, ladders |
| **INSET** | Carries an annotated interface specimen (rule 2) |

---

## 2. Asset inventory — 52 assets

Visual content only. Text on all of these is non-canonical.

| Deck | Pages | What is visually worth having |
|---|---|---|
| **v0.1 Set 1** — photoreal miniature | 4 | Annotated aerial-of-the-median composition; **object plates of real scrap** (bottle cap, soda can, zip tie, glove, granola wrapper) — the best economy art in any deck; Community Board and welcome-sign props; Acorn Hollow establishing render; folk-law panel *device* (icon + line + gloss) |
| **v0.1 Set 2** — illustrated storybook | 14 (≈12 unique) | Buildings and per-species home ladders (strongest original); citizen cards; expedition six-step flow; crossing sequence; highway-ecology gradient; predator plates; species comparison. **Near-duplicate spreads:** Highway Ecology ×2, Expeditions ×2 |
| **v0.3** — tactical/military | 11 | Corridor cross-section and chain diagrams (bones only); scale-differential devices (tire/rabbit/mouse, object-to-terrain); Margin before/after reset states; tier diorama escalation; guest-species drawings (opossum, snake, crow, toad, rat). Chrome retires entirely |
| **Concept Artwork** | 11 | Cracked-asphalt wordmark; **engine-block colony**; night crossing in rain; winter sled-haul; underground pipe-workshop cutaway; two golden-hour establishing shots; canopy village with duties board; pull-tab-and-needle prop. Least infographic, most usable — under rule 2 this is now the **most valuable source deck** |
| **GSS Text-backgrounds** | 9 | Frames retire (navy blueprint chrome). **Nine corner vignettes are keepers, at small scale:** salvage-sort workshop, winter food-store cutaway, crow trading a pull-tab to mice, rabbit hauling party along a barrier, mice sheltering under a reflector by night, culvert lantern scene, squirrel at night. These are the seed of the **spot-illustration** class — see §5 |
| **Rogue — Turn of the Seasons** | 1 | A **Set 2 plate**, not a separate generation: same portrait geometry, same green header band, same Acorn Hollow sign, same Core Philosophy sidebar, same footer motto rule. Carries no more authority than any other Set 2 plate |
| **Rogue — opossum encounter** | 1 | Contested-node staging and scale; wet-highway realism; a raccoon in a party, which is now canon |
| **Rogue — Metropolis at night** | 1 | Definitive Metropolis establishing art |

**Species balance across all 52:** mouse-dominant. Squirrels adequate (canopy villages). **Rabbits are the gap** — one hauling party, some panel cameos, one face in the opossum scene, no signature rabbit colony image anywhere. Rabbit is co-equal in canon and the usual default species. Closing this is Priority 1 in the concept-art track.

---

## 3. Disposition table

**Keep** — stands with correction; layout and art largely survive.
**Revise** — rebuilt on its existing bones; substantial art survives, copy fresh.
**Supersede** — subject survives, plate does not; contributes fragments only.
**Retire** — dropped; drift, duplicate, or non-canon.

### v0.1 Set 1

| Plate | Verdict | Why / harvest |
|---|---|---|
| Overview / folk register | **Supersede** | Folk vocabulary is now canon (§6.3) but the plate asserts a raccoon workshop and rat inhabitants. Harvest the annotated-aerial composition |
| Colony HUD + rumor cards | **Retire** | UI-as-plate (rule 2); HUD carries Reputation and a single Materials stat, both rejected. Harvest the rumor-card *object* form |
| "Laws of the Median" + dual place-naming | **Revise** | Laws are canon (§6.1) with **entirely new text**; dual naming is now drift (§1.2). Harvest the icon+line+gloss device. Drop bottle-cap "Currency" |
| Acorn Hollow render + Community Board | **Keep** | Community Board and welcome sign are canon (§15.3, §22.3). Species-mix needs correcting to single-species |

### v0.1 Set 2

| Plate | Verdict | Why / harvest |
|---|---|---|
| Overview poster | **Supersede** | Splits into the title plate and the Founding Escape plate |
| Buildings & Infrastructure | **Revise** | Closest to canon of any legacy plate — upgrade ladders, durability states, placement bonuses all survive as §14–15. Add the Construction Queue |
| Colony Homes (per-species ladders) | **Revise** | Genuinely useful per-species tier art; correct names against §15.2 and Appendix E's pending vocabulary |
| Expeditions (six-step flow) | **Revise** | Flow survives as §5.3; add Field Mode and the Rating. **Duplicate spread — retire one** |
| Colony Overview dashboard | **Supersede** | UI-as-plate (rule 2). Content becomes the Almanac plate, drawn illustratively. Roles and economy both wrong |
| Highway Ecology | **Revise** | Edge Effect is now canon and named (§9.3). **Duplicate spread — retire one.** Sub-zone panel is drift (§1.2) |
| The Crossing | **Revise** | Survives as §23; drop "Smoke Pouch"; return split is 70/20/10. Keep conceptual — least-specified system |
| Citizens of the Median | **Supersede** | Excellent card art, wrong frame: star-pips must become descriptive bands, "dossier" is retired, Distinctions and the three equipment slots are missing. Harvest every portrait |
| Predators | **Revise** | Good animal drawings; roster and roles need checking against §20.3 |
| Gameplay Overview (phone UI) | **Retire** | UI-as-plate, and the wrong platform — PC and console, not phone |
| The Three Core Species | **Revise** | Survives as §4; remove pheromone routing and canopy bypass; stats are now integers |
| Guests From Afar | **Supersede** | Roster wrong in six ways; superseded by the Guest plates |
| Rest Stop Metropolis | **Revise** | Survives as Part VI; raccoons are now founding species (§29.4); venues are nodes |

### v0.3

| Plate | Verdict | Why / harvest |
|---|---|---|
| Creative DNA / title | **Retire** | Skin is drift; STALKER/NIMH/TEEN-MATURE framing is rejected. Harvest the scale-differential thesis |
| Highway Corridor Biomes (6) | **Revise** | Expand to eight (§8.1); decouple danger from biome — danger is lane count |
| Corridor Geometry & Central Hub | **Revise** | The bones of the cross-section and chain plates. Remove subterranean bypass conduits; wall height is flavor |
| The Corridor Civilizations | **Supersede** | Superseded by the species plate; harvest drawings only |
| Expedition Control (MEDIAN OS) | **Retire** | UI-as-plate *and* militarized *and* discloses odds. Useful only as a negative reference |
| Colony Management | **Retire** | Same. Harvest the predator-alert telegraph idea |
| Game Tiers | **Revise** | Survives as §31; no Industrial Hub or Sovereign Empire; Tier II is **Fortified Settlement** |
| Citizen Archetypes | **Retire** | Rat citizen "Grist" is a misdepiction on record; gear reads weaponized. Harvest material-culture language |
| Creative DNA & Inspirations | **Retire** | Harvest scale and atmosphere matrices |
| The Margin | **Revise** | Before/after reset states are the Road Work plate's spine (§10.2) |
| Guest Citizen Registry | **Supersede** | Roster wrong; Catalyst/Ambient naming retired. Harvest the animal drawings — the only Guest art that exists |

### Concept Artwork

| Plate | Verdict | Why / harvest |
|---|---|---|
| Front plate / wordmark | **Keep** | Cracked-asphalt letterfill is adopted concept direction (§33.1). Must be rebuilt with live text |
| Key-art scenes (7) | **Keep** | Establishing shots, night crossing, winter haul, engine-block colony. Reference and plate art throughout |
| Underground workshop cutaway | **Revise** | Cutaway format is excellent and reusable. **Drop the copper smelting and anvil** — animal metallurgy is rejected |
| End plate "Corridor Secured" | **Supersede** | Pull-tab prop survives; **the PSA signage it is built on is rejected on record** (§1.2). Needs a new closing concept |

### GSS Text-backgrounds

| Asset | Verdict | Why / harvest |
|---|---|---|
| All 9 navy frames | **Retire** | Blueprint chrome is obsolete, and dark busy fields behind body text fail on legibility regardless of style |
| The 9 corner vignettes | **Keep, at small scale** | **Not** promoted to standalone plates. These are **spot illustrations for body-text pages** — which is what the deck was reaching for in the first place. The original error was compositing text *on top of* the art; a sourcebook sets spot art *beside* text. The crow-trading-a-pull-tab vignette is the Guest-interaction beat already drawn |

### Rogue images

| Asset | Verdict | Why / harvest |
|---|---|---|
| Turn of the Seasons | **Revise** | A Set 2 plate that an earlier thread met in isolation and over-weighted. It is a seasons plate we need, not a style precedent. One fix: Mowing is **not** a fifth season — Road Work is decoupled from the calendar (§10.2) and belongs in its own callout, off the wheel |
| Opossum encounter | **Revise** | Narrower fix than previously recorded. **The raccoon is fine** — canon as an Active Guest (§20.1). The violation is **three core species in one party** (rabbit + squirrel + mouse); pick one and keep the raccoon as the Guest. The rabbit's staff is a separate question, gated on 2a |
| Metropolis at night | **Keep** | Anchor art. Use a fictional plaza name; push multi-species variety |

---

## 3.5 Editorial method

Four devices that govern how a plate is written, distinct from how it looks.

### Levels of certainty

Not every system needs the same resolution, and pretending otherwise is what makes a book either thin or exhausting. Three levels, assigned deliberately:

| Level | Meaning | Example |
|---|---|---|
| **Fully specified** | Enough detail to imagine actually playing it | The encounter model — Approaches, rounds, Turns, exposure |
| **Structurally specified** | All inputs and outcomes exist; exact values stay light | Base Defense — telegraph, resolution and stakes exist, costs do not |
| **Evocatively specified** | Carried by example, image and consequence rather than rules | Crossing — the least-specified system in the GDD |

**This replaces "flagged as open" as the book's way of handling Appendix D.** Seventeen open design items stop being seventeen holes and become seventeen resolution choices. Crossing is not unfinished; it is evocatively specified.

**But it is not a license to invent.** The tempting version of this advice — *"where a mechanic is unsolved, choose a plausible answer and move on"* — is exactly how the five legacy decks improvised 90% of their content into material that did not survive contact with canon. Declarative about what is settled; evocative about what is not; **never a number invented to fill a hole.** Gaps still go to `art_raised_questions.md`.

### The claim test

Every plate gets a one-line editorial thesis before it gets a layout. Canon supplies most of them:

- *Richness and danger are the same place read from two directions.* — Traffic as Weather
- *Exposure widens the distribution; it does not shift it.* — Exposure & Outcomes
- *Claiming a Reach is not the same as pacifying it.* — Outposts
- *The colony can always survive at home, and can never advance there.* — The Two Loops
- *An encounter is not automatically a fight.* — The Encounter Frame
- *The fiction has families; the simulation has no heredity.* — Bonds & Hearths
- *Certainty lives in construction; risk stays in the field.* — Construction & the Queue

### The regret test

*Can a sensible player genuinely regret either available choice?* Applied to every plate as a check that the **tradeoff** is visible and not merely the capability. MEDIAN passes in more places than the plates currently show — Hearths trade deployability for warmth, Guests open one door and close another, the Cache Network trades convenience against resilience, and party size raises the score *and* the number of bodies exposed.

### Four voices

Distinct registers, kept distinct, with the last one rare:

| Voice | Carries |
|---|---|
| **Authoritative** | The neutral system explanation |
| **In-world** | Colony records, Laws and Sayings, field notes, folk names |
| **Player-facing** | Worked examples, the shape of a decision |
| **Designer** | Why a mechanic exists — **used sparingly; too much breaks the spell** |

*Open for 2c:* whether the book's running prose uses reader vocabulary ("vehicles," "culvert") or colony vocabulary ("Roaring Iron," and the Rivers of Thunder), and where the friction between them is deliberate.

---

## 3.6 Worked examples — a third track

The book needs a recurring **example of play** box: the device that turns an encyclopedia into a game. Nothing in the pass currently produces one.

A worked example teaches species asymmetry, opportunity cost, incomplete information and emergent consequence in a paragraph, without a rules transcript. The model:

> *The colony needs insulation before the cold. A rabbit can carry the milkweed in one trip, but the stand lies beyond two open lanes. The mouse route through the drainage seam is safer and takes three. Committing a squirrel to lookout delays the east cache another day. On the second trip it begins to rain, and the seam closes.*

**Five to write, one per major system:**

1. **One expedition, end to end** — Launcher to Record entry: who is trusted with it, the crossing, a node reached, an Approach chosen, a Turn taken, exposure resolving, the Rating written into a Tale. This is the flagship.
2. **One building, from need to completion** — through the Construction Queue, with the building offline while it is worked and no way to hurry it.
3. **One crisis across several days** — Road Work: telegraph, onset, persistence, recovery.
4. **One colony at three stages** — Tier I, II and IV on the same ground.
5. **The same decision made two ways** — two colonies, two philosophies, both defensible.

---

## 4. The plate list

Named, not numbered — numbering deferred until text is live and layered. Ordered by GDD part.

**Claims are written per part as that part is built**, not speculatively for all 49 at once. Part I's are below; the rest inherit the principle.

### Part I — What MEDIAN is

**Claims for this part:**

| Plate | Claim |
|---|---|
| Title & Wordmark | *Small is grand.* |
| Pillars | *A base-builder first. Everything else is in service of the place you build.* |
| The Four Registers | *You always know what kind of decision you are being asked to make.* |
| The Three Species ✔ | *One landscape, three civilizations — and the choice lasts the whole campaign.* |
| **The Median Read Three Ways** | *The same ground is a different place depending on who is standing on it.* |
| The Two Loops | *The colony can always survive at home, and can never advance there.* |
| Laws & Sayings | *The folklore is the tutorial. What the colony teaches its young is what keeps them alive.* |
| The Giants | *An animal is far too observant to confuse a rider with the thing it rides in.* |

| Plate | Must show | Source | Tag | Gated by |
|---|---|---|---|---|
| **Title & Wordmark** | Cracked-asphalt wordmark, "//" logomark as mossy concrete relief, one-line pitch, the Sayings as a philosophy sidebar | Concept front plate | HARVEST | — |
| **Pillars — What it is and isn't** | Seven pillars; base-builder-first framing; the explicit not-list (§1.2) | New | DIAGRAM | — |
| **The Four Registers** | Colony/Field/Encounter/Crossing as verb, register, attention; the expedition rhythm; transitions as authored beats; *no fifth register* | New — **nothing exists** | NEW | — |
| **The Three Species** ✔ **DONE** | *Complete 2026-07-24.* Four descriptor fields per column plus a shared stat-frame comparison strip and the no-cross-recruitment rule. Rabbit's seven-plus scattered bolt holes, squirrel's six legible caches, mouse relay chain. Shipped flat (P2-41) | New, per `PROMPT_03` | — | — |
| **The Median Read Three Ways** | **One stretch of median, three overlays.** Rabbit: sightlines, escape lanes, burrowable soil, aerial exposure. Squirrel: vertical routes, cache sites, ground-crossing gaps. Mouse: cracks, enclosed runs, Margin pockets nothing else reaches. Makes the asymmetry **spatial rather than tabular** | New — **nothing exists** | NEW | — |
| **The Two Loops** | Domestic loop, expedition loop, and the bridge — survive at home, advance only away | Set 2 p1, v0.3 loop vector | DIAGRAM | — |
| **Laws & Sayings of the Median** | Five Laws with what each teaches; the Sayings; the four exposure surfaces; the colony's Laws are imperfect | Set 1 device, **all text new** | HARVEST | — |
| **The Giants — vocabulary** | Giants / Roaring Iron / Rivers of Thunder / the Mowing / the Founding Escape, as spoken folklore over imagery. **No human figures** | New | NEW | — |

### Part II — The world

| Plate | Must show | Source | Tag | Gated by |
|---|---|---|---|---|
| **The Cross-Section** | Sound Wall → Margin → Highway → Home Median → Highway → Margin → Sound Wall, symmetrical, colony cut away below; Edge Effect gradient overlaid | v0.3 geometry (clean v0.2), Concept cutaway | HARVEST | — |
| **The Corridor Chain** | Home Reach plus chain; three lifecycle states; fog of war; outpost claims the whole Reach | v0.3 chain panel | HARVEST | — |
| **Biome Codex — eight** | Eight biomes, resource character, cover profile, typical Anchors; **danger is lane count, not biome** | v0.3 six biomes | HARVEST | — |
| **Anchor Points** | Named terrain features; bonus never gate; every Reach a mix; first Home Reach guaranteed to fit | New | NEW | — |
| **The Game Day** | Five daily beats; four traffic cycles; one expedition per citizen per day | New | DIAGRAM | — |
| **Traffic as Weather** | Wind Draft; the River's Spume and its four manifestations; Litter as a Choice-Event Card; Edge Effect and Quiet Zone | Set 2 ecology gradient | HARVEST | — |
| **The Turn of the Seasons** | Four seasons, sustenance fork, Nesting Season; **Mowing off the wheel** | Rogue poster | HARVEST | — |
| **Road Work** | Telegraph → Onset → Persistence; Margin wiped; severity is intensity not length; machinery evaded never fought; tilts the card pool; echoes the Founding Escape. **Machinery unoperated** | v0.3 Margin states, seasons Mowing column | HARVEST | — |
| **Choice-Event Cards** | A card as a drawn object with costed responses; both homes; **no numeric countdowns anywhere** | Set 2 mockup, **reconceived as object not screen** | NEW | — |

### Part III — The colony

| Plate | Must show | Source | Tag | Gated by |
|---|---|---|---|---|
| **The Colony** | The settlement as living miniature; three hotspots — Community Board, Story Circle, species hub; always-visible functional icons; Construction Queue present | Set 2 dashboard content, Concept canopy village | NEW + INSET | — |
| **The Eight Roles** | Eight standing Roles, fixed output, identical whoever holds it; the base layer never grows anyone | New | DIAGRAM | Default Role open |
| **The Economy** | Sustenance (Perishable/Durable) + Flexible + Rigid + Special Artifacts; 1 slot = 1 value; cooperative carrying; **no currency** | **Set 1 scrap object plates** | HARVEST | Weight thresholds deferred |
| **Construction & the Queue** | Whole days, resources sunk, uninterruptible, building offline while worked, **no speed-up**, slots scale by Tier | New | DIAGRAM | Day-values deferred |
| **Structures & Upgrade Ladders** | Structure families; named rungs; durability states; species-flavored vocabulary; grandeur without industry | Set 2 buildings + colony homes | HARVEST | Appendix E unwritten |
| **The Community Board & the Story Circle** | Operational versus ceremonial, expressed spatially; memorials at the Story Circle | Set 1 board, Concept duties board | HARVEST | — |

### Part IV — The citizens

| Plate | Must show | Source | Tag | Gated by |
|---|---|---|---|---|
| **The Character Record** | Likeness and Tale as two views; **descriptive bands, never pips**; Given Name and After-name as separate fields; three equipment slots; Distinctions and Maimings | Set 2 citizen cards | HARVEST + INSET | *2a settled* |
| **Bonds, Hearths & Nesting Season** | Trusted Friend → Hearth; found family; descent as story fact only, no heredity; Hearths are less deployable | New | NEW | *2a settled* |
| **Wanderers** | The primary early growth path; three arrival routes; joins as ordinary Citizen, no slot; the other-survivor case | New | NEW | Arrival rate open |
| **Harm, Fear & Tharn** | The four-rung ladder; tharn's trigger and its rescue beat; Distinction↔Maiming symmetry; the After-name at first Distinction | New | NEW | Per-species tharn flavor open |
| **Keepsake, Tool & Supply** | Three slots, three ownership models; descriptive never numeric; **the slot is Tool and never Weapon** | Set 1 objects, Concept pull-tab prop | HARVEST | *2a settled* |
| **Active Guests — seven** | Seven Guests as option-openers: each opens one Approach or Turn and closes another; seven against four slots; **the Guest House in seven skins and placements** | v0.3 registry drawings, GSS crow vignette | HARVEST | Roster pass queued (App. D) |
| **Ambient Guests — nine** | Nine passives; downside-free; Cultural Focus; WHOOT as template character; **Guest House variants — a nest in a tree, a burrow, a waterside** | Set 2 guests, v0.3 registry | HARVEST | Turtle effect open; ladder unwritten |
| **The Records** | Almanac / Chronicle / Likeness / Tale; the event feed names individuals; Rating's four grades; Report and Share; **no currency, no sharing bonus** | Set 2 rating and record panels | HARVEST + INSET | — |
| **Names** | Given Name and After-name; folk-name grammar, homely and plain; **one name per place plus tags**; the one name the player authors | New | DIAGRAM | Appendix F unwritten |

### Part V — Leaving home

| Plate | Must show | Source | Tag | Gated by |
|---|---|---|---|---|
| **The Crossing** | **A survey of the mode**, not of play: what it is for, staging, reading traffic, commitment; the First Law as literal mechanics; accessibility; **70/20/10 return**; not an encounter | Set 2 crossing, Concept night crossing | HARVEST | Asserts nothing about moment-to-moment play |
| **Field Mode** | Traversable surveyed territory; node arrival triggers *that* node's check; fog of war; carry tension; route overlays; **generalizes to home and the Metropolis** | New — **nothing exists** | NEW | Overlay set open; home risk floor open |
| **The Encounter Frame** | Same frame for windfall or ambush; five Approaches; N rounds carry N−1 Turns; closeness continues, cleanness ends; hard cap three. **Opposing party of roughly equal mass, composed not to invite counting** | New — **nothing exists** | NEW | Presence values deferred |
| **Exposure & Outcomes** | Exposure widens the distribution, does not shift it; both tails open together; group and individual resolve independently; the four Ratings derived | New | DIAGRAM | Bands deferred; **probabilities recede under Rule 7** |
| **Contest, Recruitment & Base Defense** | The funnel — contested → 70/30 → 30% amenable → check and residence cost → slot cap; Guest versus Citizen outcomes; **the raccoon worked example**; Base Defense as the colony-as-party | v0.3 (as corrected opposite) | NEW | Base Defense cost open; ratio conditionality open |
| **Expeditions & the Launcher** | Five categories; the eight-step loop; character-centered launcher; **exactly one equipment decision per citizen**; never discloses contest or odds | Set 2 expeditions | HARVEST + INSET | — |
| **Outposts** | Lifecycle; claim clears fog but **only outbuildings reduce contest**; light footprint, never Home buildings; stationing; Hearths cannot be split | New | NEW | Higher-Tier significance open |

### Part VI–VII — Metropolis, progression, presentation

| Plate | Must show | Source | Tag | Gated by |
|---|---|---|---|---|
| **The Rest-Stop Metropolis** | Extraordinary but plausible; a Field territory with venues as nodes; leans on Parley; contradictory Laws; **raccoons as founding species — heritage, never authority**; raccoons plus a mix of core species and Guests; **any plaza name shown as a generated example** | Rogue night render | HARVEST | Raccoon-heritage nods still unspecified |
| **Progression Tiers** | Tier I–IV with fantasy, range, capabilities, pressures; **Tier II is Fortified Settlement**; what each graduation grants; mastery as ecological invisibility | v0.3 tiers | HARVEST | — |
| **Interface & Information Design** | The one plate where UI is the subject — annotated insets of ledger overlay, Village Roster, Launcher; functional icons in the base view | Set 2 UI fragments | INSET | — |
| **Scale Language** | Everyday objects at true scale becoming terrain; species size cards; vehicle and machine flavor throughout the world | v0.3 scale devices, Concept engine block | HARVEST | — |
| **The Founding Escape** | The **Ancestral Warren / Den / Burrow** intact, seen once; the modified Choice-Event Card; no survivors but the three; the multi-register played sequence; loss sensory-obscured; **machinery unoperated** | Set 2 storyboard | NEW | Register order open |
| **Art & Audio Style Guide** | The pass's own conventions once Stage 2 locks | New | DIAGRAM | **Blocked on all of Stage 2** |

### Part IX — Stories of Survival *(new closing part)*

A book of systems needs a place where the systems are *seen operating*. This part is where the worked examples of §3.6 live as finished spreads rather than as boxes, and it gives the book the dramatic arc a pure reference work lacks — the reader ends inside a colony's history rather than inside its rules.

| Plate | Must show | Source | Tag | Claim |
|---|---|---|---|---|
| **One Expedition, End to End** | The flagship worked example: who is trusted with it, the crossing, a node reached, an Approach chosen, a Turn taken, exposure resolving, the Rating written into a Tale | New | NEW | *This is what a day out there costs, and what it is worth.* |
| **A Colony at Three Ages** | The same ground at Tier I, Tier II and Tier IV — growth as accumulation and memory, never industrialization | v0.3 tier diorama | HARVEST | *Mastery is ecological invisibility, not empire.* |
| **The Winter That Was Hard** | One crisis across several days — Road Work's telegraph, onset, persistence and recovery, told as colony history | New | NEW | *Fire passes; the burned ground feeds.* |
| **Two Colonies, Two Philosophies** | The same decision made differently and defensibly by two colonies — the regret test made into a spread | New | NEW | *Both were right. That is what makes it a decision.* |

*These are late-build. They depend on the systems plates existing first, and on enough of the book's voice being settled that in-world material reads as record rather than as flavor text.*

---

## 5. Concept-art track

Merged from `MEDIAN_v0.4_Needed_Artwork.md`. Many of these are the illustrations that go *inside* the plates above, which is why they are tracked here rather than separately.

**Three classes, not one.** The sourcebook register (Standing Rule 7) means the deck needs more than plates and key art:

| Class | What it is | Where it lives |
|---|---|---|
| **Plates** | The 44 information-design sheets in §4 | Standalone, and as full-page inserts in the GDD |
| **Key art** | Establishing shots, story beats, hero images | Section openers, marketing, plate interiors |
| **Spot illustrations** | Small, single-subject art — an object, an animal, a moment | **Beside body text on ordinary GDD pages.** This is what the GSS deck was reaching for and got backwards |

The spot class is the one with no backlog yet. The nine GSS vignettes seed it; the GDD's ~2,275 lines of body text will want far more, and they are cheap relative to plates. A running spot list should be built as plates are produced, since most plates generate offcuts that serve.

**Priority 1 — the rabbit gap.** Rabbit warren establishing cutaway (surface life above, cross-section below, multiple bolt-holes) · rabbit party staging and crossing · three or four rabbit citizen portraits · rabbit Founding Escape. Plus one squirrel Cache Network hero shot to round out the three signature systems.

**Priority 1 — systems with no art.** Road Work as a three-beat set (Telegraph / Onset / Persistence + recovery) · outpost establishment and the claim moment · wild-versus-outposted Reach pair.

**Priority 2.** Field Mode traversal and one node-reveal frame · a canon-clean contested encounter · Base Defense · **Going Tharn** (absent, high emotional value, strong marketing image) · a maimed veteran valued, with a Distinction counterpart · Guest vignettes prioritising Raccoon, Mink, Crow, Fox, Weasel, Hedgehog, Snake · the eight biomes as establishing shots.

**Priority 3.** Return-home relief · the memorial space · the Grand Caravan · four-season home scenes · brand set.

**Priority 3 — Citizen Likeness examples.** A set of worked Character Records presented as an RPG sourcebook would present NPCs: portrait, Given Name and After-name, descriptive bands rather than pips, bonds, three equipment slots, earned Distinctions and Maimings, a few lines of Tale. This is the visual counterpart to the GDD's own queued future-work item — *"example and template citizen writeups in the register of tabletop RPG sourcebook NPC entries,"* of which WHOOT is the first instance — and it is the single clearest expression of Standing Rule 7. Cover all three core species plus a Guest, and use it to help close the rabbit gap.

**Standing guardrails for all of it:** single-species colonies · no weaponization · no forge or smelting · machinery evaded never fought · human bodies off-screen except Road Work and Founding-Escape-class threats · vehicles always visible · traffic never off-screen · no explicit blood or gore, catastrophe sensory-obscured.

---

## 6. Open-item gating

Seventeen open design items in Appendix D, plus eight deferred numerics and five Phase-2 deferrals. Status after the Stage 1 question pass, which closed nine of the ten gaps the artwork raised:

**Stage 2a is settled** — decisions P2-27 to P2-34 in `running_decisions.md`. Dress marks leaving home; colour comes from the roadside; upright to work and four-legged to move; no role-specific dress. Keepsake and adaptive equipment are the two things worn at home. **Every citizen plate is unblocked.**

**Stage 2b is settled** — and then reversed the same day. Final: **16:9 landscape, desktop-first, no spreads** (P2-39). The book is read on a screen and not printed, which knocked out all three arguments for portrait. Spreads disappear entirely, the world's horizontal geometry stops fighting the page, and the legacy landscape decks are already exactly 16:9 so they re-use at native aspect. Three-column text grid. PowerPoint's native slide size.

The GDD still *becomes* the sourcebook: one book, with the plates as its illustration programme rather than a separate deck (P2-36).

**Now the only blocker: Stage 2c** — palette, tonal register, headers, typography, grid, iconography, labelling, caption voice, text density, and — new, because it is a book — page furniture: running heads, folios, section openers, sidebars, table styling.

*Though much of 2c is now settled by demonstration rather than decree: the completed Three Species plate establishes the register, palette, descriptor-panel form, header and footer bars, comparison-strip form, and the ink-arrow annotation device.*

**Two authoring dependencies the book cannot close without**, neither of them art tasks: **Appendix E** (per-family upgrade ladders) and **Appendix F** (folk place-name component banks), both currently *"Deferred. To be authored."*

**Settled in the Stage 1 question pass** *(details in `running_decisions.md`, P2-13 to P2-22)*:

| Was gating | Now |
|---|---|
| Founding Escape unnamed | Name stands; the lost home is the **Ancestral Warren / Den / Burrow** |
| Metropolis plaza name and species mix | Procedural name, shown only as a captioned example; raccoons plus a mix of core species and Guests |
| Guest accommodation unspecified | One **Guest House** family, skin and placement varying by species |
| Warren Flow undrawable | **Multiplicity of exits** is the rabbit's readable signature, extending into the Field layer |
| Presence never counted, but must be drawn | Contested plates show a **roughly equal opposing party**, composed not to invite counting |
| Exposure never displayed | Plateable either way; the deck explains the game rather than serving as a handbook |
| Crossing least-specified | The plate is a **survey of the mode**, asserting nothing about moment-to-moment play |
| Deck had no defined reader | GDD × RPG core sourcebook (Standing Rule 7) |
| Traffic-as-weather hazards | Confirmed designed; art only |

**Still deferred *to* this phase, not yet settled:** raccoon-heritage visual nods in Metropolis architecture · species-tracking review across all artwork · Field Mode's art specification (palette, line weight, label typography, how biome changes a plate's character).

**Plate stays conceptual until designed:** Base Defense consequences · higher-Tier outpost significance.

**Flagged on the plate, does not block it:** exposure bands · Presence values · Construction Queue day-values · item-weight thresholds · wanderer arrival rate · Turtle's effect · Guest slot scaling · default Role · Field overlay set · home Field risk floor.

**New, raised by the answers:** whether the multiplicity grammar covers all three species — rabbit exits, squirrel caches, mouse relay stations. Affects every species plate and the three Priority 1 colony images; wants a decision at 2a or 2b.

---

## 7. Build order

**Stage 2 first, in the handoff's order.** 2a anthropomorphism ✔ settled → 2b portrait versus landscape → 2c everything else. Nothing below starts before 2b, because orientation is structurally prior to all layout.

**2a's settlement adds a subject the old Plan did not have.** Because dress marks leaving home (P2-27), the **Staging Post** becomes where a party kits up — giving an existing structure family a concrete second function, and giving the Structures plate and the Expeditions plate a shared beat worth drawing.

**There is no proven house style to codify.** The old Plan's first standing rule was *"house style = Turn of the Seasons,"* and the Analysis concluded that "v0.3 bones + Set 2 skin" was not hypothetical because one poster had already executed it. That argument rested on the poster being a separate, later, deliberate synthesis. It was not — it is a Set 2 plate, from the same generative pass, met out of order. **Stage 2c is therefore an original decision, not a codification of something already achieved.** Nothing in the five decks holds precedential authority; they are source material only.

This is consistent with where the pass has landed anyway. A poster is a standalone sheet; a sourcebook is not a stack of posters. The register in Standing Rule 7 was never going to be reachable by codifying a poster.

**Build in vertical slices, not horizontal layers.** A book made in evenings over a long stretch should be *finished somewhere* at all times rather than half-done everywhere. So: complete one section entirely — its text pages, its plates, its spot art, its furniture — before starting the next. A finished 30-page Part I is a real artifact; 44 plates at 60% are not.

This also means **2c is derived rather than decided.** Settling typography, grid, and palette in the abstract is guessing; settling them by making three good pages and looking at what they wanted is not. Make the first slice, extract the conventions from it, *then* lock them and hold the line for everything after.

**Suggested first slice: Part I.** Seven plates, and it is the part that makes a reader want the rest — thesis, the four registers, the three species, the folklore. It also front-loads the two most quotable things in the whole document, the Laws and the Sayings.

**Status: the first plate is done.** **The Three Species** — complete, canon-checked, shipped flat per P2-41. It establishes the register and the device kit for everything after it.

**Remaining Part I plates**, in suggested order:

1. **The Four Registers.** The interesting one: nothing exists for it, and it must make Colony, Field, Encounter and Crossing feel distinct at a glance *without* the chassis varying (P2-1). Distinctness has to come from the illustrations and the descriptors, not from styling.
2. **The Median Read Three Ways.** New, and the strongest companion to the plate just finished — it turns the species asymmetry from a table into a place.
3. **The Two Loops** — domestic and expedition, and the bridge that forces one into the other.
3. **Laws & Sayings** — five Laws with what each teaches; tests P2-38's folklore-as-connective-tissue proposal.
4. **The Giants — vocabulary.** No human figures (P2-14).
5. **Pillars — what it is and isn't.**
6. **Title & Wordmark.**
7. **A specimen text page with spot art.** The sparse page is the harder test of an identity, and it is the page type nothing has proven yet.

**Then, early in Part II: Field Mode.** Not a Part I plate, but it should be proven early — it is the one that must depict a naturalist's survey plate without *becoming* one (P2-1).

**Then the spine:** Four Registers · Corridor Chain · Biome Codex · Species · Encounter Frame · Exposure & Outcomes · Expeditions · Crossing · Colony · Economy · Roles · Structures · Harm/Fear/Tharn · Active Guests · Tiers · Road Work · Seasons.

**Then supporting:** Anchor Points · Game Day · Traffic as Weather · Choice-Event Cards · Construction Queue · Bonds/Hearths · Wanderers · Keepsake/Tool/Supply · Ambient Guests · The Records · Names · Contest/Recruitment · Outposts · Metropolis · Founding Escape · Community Board/Story Circle · Interface.

**Last:** Title · Pillars · Two Loops · Laws & Sayings · The Giants · Scale Language · Style Guide (blocked on all of Stage 2 by definition).

---

## 8. Coverage check

| GDD part | Covered by |
|---|---|
| I — thesis, pillars, registers, species, loops, folklore | Title · Pillars · Four Registers · Species · Two Loops · Laws & Sayings · The Giants |
| II — geography, biomes, day, seasons, Road Work, events | Cross-Section · Corridor Chain · Biome Codex · Anchor Points · Game Day · Traffic as Weather · Seasons · Road Work · Choice-Event Cards |
| III — colony, roles, economy, construction, structures | The Colony · Eight Roles · Economy · Construction & Queue · Structures & Ladders · Board & Story Circle |
| IV — citizens, bonds, harm, equipment, Guests, Records, names | Character Record · Bonds/Hearths · Wanderers · Harm/Fear/Tharn · Keepsake/Tool/Supply · Active Guests · Ambient Guests · The Records · Names |
| V — crossing, field, encounters, contest, expeditions, outposts | Crossing · Field Mode · Encounter Frame · Exposure & Outcomes · Contest/Recruitment/Base Defense · Expeditions & Launcher · Outposts |
| VI — Metropolis | The Rest-Stop Metropolis |
| VII — tiers, interface, art, generative, onboarding | Tiers · Interface · Scale Language · Founding Escape · Style Guide |
| VIII — production notes | *No plate. Suggestions, not canon.* |
| **IX — Stories of Survival** *(new)* | One Expedition End to End · A Colony at Three Ages · The Winter That Was Hard · Two Colonies, Two Philosophies |

**49 plates** — 8 · 9 · 6 · 9 · 7 · 1 · 5 across Parts I–VII, plus 4 in the new Part IX. Every canon section has a home; §34's generative layer is deliberately unplated, as canon requires it never become load-bearing.

*Part I gained "The Median Read Three Ways," and Part IX is new — the closing narrative part where the systems are seen operating rather than described.*

That is up from the old Plan's ~28, and the growth is almost entirely v0.4.2's new systems rather than scope creep: the four registers, the encounter model, the Records, the folklore and naming layers, equipment, bonds and Hearths, wanderers, the Construction Queue, and Choice-Event Cards had no plates because they did not exist.
