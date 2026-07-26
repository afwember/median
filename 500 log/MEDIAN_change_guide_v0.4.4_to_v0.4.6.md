# MEDIAN — Change Guide, v0.4.4 → v0.4.6

Consolidates `v0.4.4_decisions.md` (V4-1…V4-18) and `v0.4.5_decisions.md` (V5-1…V5-64) into an executable merge specification.

Base document: `100 canon/MEDIAN_GDD_v0.4.4.md`. Output: **v0.4.6**, which supersedes the v0.4.5 assembly. Same decisions, differently weighted.

Where this guide and the base differ, this guide governs. Where this guide is silent, the base stands.

**Appendices are a separate project.** This compile carries an appendix **manifest** — title and one line of scope each — and no appendix content. What each will hold accumulates in `MEDIAN_appendix_guide.md`, maintained alongside this one.

**The old Appendices A through D leave the book.** The canon checklist, the superseded record, the change record and the open items are project apparatus rather than reader material, and they move to `500 log/`. Where an entry below says *log it*, it means to one of those four; the appendix guide says which.

---

## How to use this

### The fields

Every entry carries a **WEIGHT**, and most carry **STATE** and **DO**.

**WEIGHT** decides whether the change earns words in the book. It has four values, and it is the most important field in this document.

| Weight | Meaning |
|---|---|
| **state** | The book asserts this in prose. |
| **show** | The book must **not** assert this. It is carried by an example, table, Record excerpt, caption or illustration named in the entry. |
| **say** | The claim gains a Law or a Saying (§6.2), set as a **design element on the page** — an epigraph, a set line, an inscription — rather than as another body paragraph. **It is additive.** It never licenses cutting text that carries a concept; it displaces only the gloss around one. |
| **silent** | True of the game. Governs authoring, art and future passes. Earns no sentence. |

A rule can govern the imagined game without being announced. Roughly a third of what follows is **silent** — real constraints that a reader should meet only as consequences.

**say** is the only weight that grows the book while improving it. §6.2 states that the pool grows and has never been given anything to grow with, and a proverb adds to the world rather than subtracting from the document. It is available only where an animal could plausibly say the thing.

**Err toward keeping both.** A proverb is not an argument for deleting the plain statement beside it. Where the prose carries a concept — a cause, a mechanism, a distinction a reader needs — it stays, and the Saying sits alongside as typography. Cut prose only where the proverb genuinely makes it redundant, or where what is being cut is self-justification rather than content. A beautiful line that costs the reader an idea is a bad trade.

**STATE** is the only text permitted to become prose. Declarative, world-facing, positive. It contains no reference to what it replaces, no rationale, and no comparison to a design alternative.

**DO** is an edit action performed on v0.4.4. It is executed and then discarded. It may name old text, use imperatives, and reference what is being removed. **No DO text may appear in the output in any form** — not paraphrased, not inverted, not softened.

**SRC** traces to the source decisions, for audit. **WHY** lines are not here; they are in the Archive at the end, keyed by entry ID, and are consulted only when a decision is challenged.

### Rules for the assembler

1. **STATE defines the complete semantic payload.** Integrate it into the surrounding passage's syntax and voice without importing explanation from DO, SRC or WHY. Do not mechanically paste where integration is required.
2. **Never write a sentence whose subject is the design.** Sentences describe the world, the game as played, or the rule as it stands. Not what the rule replaces, not why it was chosen, not what it costs, not which pillar it satisfies.
3. **Never state that something is not a new system.** Restraint is invisible when it works.
4. **Never define a thing by what it is not**, unless the negation is a canon prohibition a reader can act on (*the Margin is never buildable*, *no human body is ever depicted*).
5. **An entry marked `show` that produces a declarative sentence has been executed incorrectly.**
6. Log anything that surfaces; do not solve it. Questions about the game go to the v0.4.7 log; questions about what an appendix should hold go to the appendix guide.

---

# PHASE 0 — Global

**G-1 · The book states what is** — *silent* · SRC V4-1, V5-64
DO: Sweep for revision archaeology and counterfactual defence. Patterns: version numbers · *earlier / formerly / superseded / supersedes / replaced / no longer / retired / rejected* · *There is no… / There are no…* · *X must not be…* · *Why not…* · *this document* · any parenthetical explaining a change rather than a fact · any sentence denying a system the reader was never shown. Rationale and rejected alternatives live outside the book.

**G-2 · Terminology** — *silent* · SRC V5-43
DO: Replace **Character Record** → **Citizen Record** throughout, including headings and Contents. Retire **Edge Effect** as a term. Retire **undiscovered / discovered-but-expedition-only / outposted**.

**G-3 · Production language** — *silent* · SRC V5-26
DO: Where a passage specifies implementation, convert the sensory or cultural content to description of the experienced world and drop the specification. Applies beyond audio.

**G-4 · Orthography of `body-unit`** — *silent* · SRC V5-1, V5-59
DO: Set lowercase and hyphenated. The in-world compound convention requires a capitalised first element; lowercase marks it as a plain designer term.

**G-5 · Forager default** — *state, one clause* · SRC V5-64
STATE: A new or unassigned citizen is a Forager.
DO: Remove the open-working-detail parenthetical at §12.

**G-6 · The lens** — *silent* · SRC editorial, 2026-07-26
DO: MEDIAN is a concept book told through a video-game lens. This is the document's identity and it governs what this pass must **not** strip. §3's registers keep their cameras, palettes, tempo and authored transitions. §34 keeps art and sound, because in this frame they are what the lens renders rather than production specification. Where an art rule goes silent below, it goes silent because the pictures enact it, never because art direction is misplaced.
DO NOT: Remove §§36–37, or author the four manifestation pages. Both belong to v0.5; the manifest names the pages and stops.

**G-7 · The new Sayings** — *state* · §6.2 · SRC editorial, 2026-07-26
STATE: Nine proverbs enter the pool, written out under their entries below and collected here for §6.2.

> *The road is never gone. It is only set far off.*
> *The road gives what it throws away. The wall gives what it keeps.*
> *The Median feeds you. It will not make you.*
> *Far ground, thin cover.*
> *Most come home. Not all come home whole.*
> *The heavier the haul, the longer the road home.*
> *We do not leave what we can carry.*
> *The mending is not the making.*
> *Walk it before you hold it.*

DO: §6.2 states that the pool grows and has never grown. These are concrete where the existing seven are abstract, which is the direction the register wants — the existing Sayings restate the pillars, and these carry the world. Rewrite any of them in the author's own hand; **the exposition each displaces is removed either way**, and a rewritten proverb does not license the paragraph back.

**G-8 · Open flags become one class** — *silent* · whole document · SRC editorial, 2026-07-26
DO: The body's twenty-three open-item pointers are **kept as working notes** and repointed at `500 log/open_items.md`. They are scaffolding for the author, not content for a reader, and they come out before the book is shared with anyone.

Convert each to a single uniform callout rather than a parenthetical buried in prose:

> **OPEN — Warren Flow.** What the player manipulates, what failure looks like, how congestion reads in the Colony register. · `500 log/open_items.md`

The callout replaces the **whole** flagged sentence, not only its parenthetical — *Flagged for further design*, *Open:*, *Still open:* and *Flagged for dedicated design* are all apparatus, and four lead-ins for one thing is three too many. One visual class throughout, on exactly the principle already governing the CREATED VISUAL panels: recognisable at a glance, and seen or skipped as a unit.

Every flag carries the **OPEN —** prefix, so lifting the whole class later is one regex rather than twenty-three judgment calls.

DO NOT: leave a flag as inline prose, invent new ones, or let a callout carry rationale. A flag names a question and points at the log; the brief lives in the log.

---

# PHASE 1 — Structure

Moves only. No prose is written or rewritten in this phase. Anchor every operation on the **old heading text**, not on numbers.

**S-1 · Opening narrative to the front** — SRC V5-61, V4-8
DO: Move the full Founding Escape to the front matter, before Part I and before any system material. Leave a short acknowledgement and cross-reference at §35.1. Elevator pitch follows the narrative.

**S-2 · Origin brief after the pitch** — SRC V4-3
DO: Insert immediately after the elevator pitch:
> Three young members of the chosen species escape the wreck of their ancestral home, destroyed by road construction. They flee to a green island between two highways, and begin again.

**S-3 · Optional-visual sidebar to the front** — SRC V5-63
DO: Create a short front-matter sidebar before Part I. It carries the guarantee in S-8's STATE, unshortened.

**S-4 · World primer before §3** — SRC V4-2
DO: Insert an unnumbered titled primer between §2.7 and §3. It takes a Contents line and does not alter section numbering. Part II keeps the full treatment.

**S-5 · Species before the stat frame** — SRC V4-4
DO: Move old §4.1 (shared stat frame) after old §4.4. Resulting order: Rabbit · Squirrel · Wood Mouse · stat frame · seasonal personalization.

**S-6 · Cards separated and moved first** — SRC V5-35
DO: Promote old §10.3 to a numbered section ahead of Seasons and Road Work. Remaining §10 material becomes a single section titled *Seasons and Road Work*.

**S-7 · Part IV opener** — SRC V5-23
DO: Replace the Part IV *Going Tharn* opener with a group portrait of named citizens. Move the *Going Tharn* marker inside, to the fear-and-tharn subsection.

**S-8 · Old §34 dissolved** — SRC V5-63
DO: Delete the numbered section. Its content goes to three destinations: the front sidebar (S-3), nine distributed sidebars (P3 entries), and the manifestation page for generated imagery. Drop the ownership-and-evaluation block entirely — vendor, model, API, authentication, cost, latency, service continuity, save portability.

**S-9 · Biome plate to biome section** — SRC V5-24
DO: Replace the single *Biome Codex* plate marker with a multi-page section marker. Remove the codex plate from the external book plan.

**S-9b · §21.4 dissolves** — SRC V5-22, V5-64, editorial
DO: Both of the subsection's contents leave — the single-species callout is document history, and the Guests-wear-less rule is reversed and silenced (C-12, C-67). The one surviving sentence, pointing at the Guest House, folds into the §21 preamble. **Delete the subsection.** Guest Citizens carries three subsections, not four, and the Contents follows.

**S-10 · The appendix set is rebuilt** — SRC V5-63, V5-56, V5-59, editorial
DO: Delete Appendices A, B, C and D from the book; their contents move to `500 log/` (see the appendix guide). Old E and F survive and are re-lettered. Four new appendices join them. The whole set becomes the manifest at A-1 — titles and scope lines, no content.

---

# PHASE 2 — Numbering, Contents, cross-references · **FREEZE**

Complete this phase before any Phase 3 prose is written. Phase 3 composes every cross-reference in **final** numbers.

**Final map.** §§1–9 unchanged. Old §10.3 → **§10**. Old §10.1–10.2 → **§11**. Old §§11–33 → **+1** (→ §§12–34). Old §34 dissolved. Old §§35–38 → unchanged.

**The two shifts cancel.** The insertion at 10 and the deletion at 34 offset, so the document still runs to thirty-eight sections and §§35–38 keep their numbers. State this once in the change record; derive it nowhere else.

DO, in order:
1. Apply the map to every `##` and `###` heading.
2. Apply the map to every `Section N` and `Sections N, M` reference, including ranges. Note the 10.x special cases: 10.1→11.1, 10.2→11.2, 10.3→10.
3. Rebuild Contents from the actual headings. Confirm it shows the opening narrative, the unnumbered primer, §10 Choice-Event Cards, §11 Seasons and Road Work, no generative-layer section, final §35, and Appendices G and H.
4. Re-point references to dissolved §34 at the generated-imagery manifestation page or at the relevant sidebar.
5. Verify: no reference resolves to a heading that does not exist.

---

# PHASE 3 — Content

Worked in final numbering. Each entry names its final section.

## §1–2 · Thesis and pillars

**C-01 · Death is rare** — *state + say* · §2.5, §6.2 · SRC V4-11
STATE: Citizen death is uncommon. Danger expresses as fear, wounds, maiming, lost cargo and changed relationships, all of which persist and are carried home. The harm ladder has three rungs before it has a fourth.
SAY: **Most come home. Not all come home whole.**
DO: Place within the existing pillar text. Do not explain what a high death rate would cost.

**C-02 · The documentary layer** — *silent* · §2.7 · SRC V4-17
DO: Nothing is added. The Records already resolve at the Story Circle and the species hub, both inside Colony. A reader does not ask whether reading a Chronicle is a fifth register; do not answer it.

**C-03 · Non-pillars aside** — *silent* · §2 · SRC V4-1
DO: Remove. The sound wall and real ecology are stated properly elsewhere.

## The world primer *(unnumbered, before §3)*

**C-04 · Primer content** — *state* · SRC V4-2
STATE: Cross-section, outer boundary to outer boundary — Sound Wall · Margin · Highway · Home Median · Highway · Margin · Sound Wall. The Sound Wall is impassable and the world beyond it is not modelled. The Margin is rich, exposed and never buildable. Highway danger is set by lane count. The Home Median holds the colony. The cross-section repeats along the corridor; each median segment is a Median Reach; the chain ends at the corridor's one city. A Crossing takes a party across the Highway to a Margin. A Field run reads a Reach. An Encounter happens at one point in one. The Colony is the Home Median, inhabited.
DO: ~200 words. Include the arrow diagram. No new art marker.

## §3 · Four registers

**C-05 · The zoom pairs** — *silent* · §3.5 · SRC V4-13
DO: The symmetry is real and governs level authoring — the surveyed place and the inhabited place must be the same place, which the spatial-fidelity constraint already requires. Add nothing. A reader meets four registers; observing that they form two elegant pairs is the designer admiring his own structure.

**C-06 · Colony attenuates the road** — *state, one clause + say* · §3.5, §6.2 · SRC V4-14
STATE: Traffic is present in the Colony, and quieter, more distant, more filtered.
SAY: **The road is never gone. It is only set far off.**
DO: Attach the factual clause to the never-off-screen constraint. The sanctuary line is a proverb and belongs among the Sayings, not in the constraint list.

**C-07 · Crossing is one of several** — *silent* · §3.4, §24.1 · SRC V5-62
DO: Change "the signature mechanic" to "a signature mechanic" in both places. No accompanying explanation.

## §4 · Three species

**C-08 · The body-unit** — *state* · §4.4 · SRC V5-1
STATE: One rabbit, one squirrel, or two mice is one body-unit. Capacity, party size and party score count in body-units.
Table — Rabbit carry 10 / food 10 / 1 animal. Squirrel 20 / 10 / 1 animal. Wood Mouse 6 / 5 / **2 animals**, so 12 carry and 10 food per unit.
Every body-unit eats 10. Carry runs 10 : 12 : 20.
DO: Published stat values are correct and unchanged. The mouse pair's 12 is the species' advantage; do not adjust carry to make the quantum exact.

**C-09 · Aggregate and consequence** — *state, as a table* · §4.4 · SRC V5-2
STATE: Resolves by body-unit — carry capacity, party size and composition, Party Score, cooperative lifting, food upkeep. Resolves by individual animal — wounds, maiming, tharn, exposure, death, bonds, Hearths, Records.
A rabbit colony loses a whole unit at a time; a mouse colony loses half of one. A Standard item carried by two mice splits or drops if either goes down.
DO: Let the table carry it. One sentence of consequence, not three.

**C-10 · Safety in Numbers has a cause** — *show* · §4.3 · SRC V5-2
SHOW: In the mouse section, a worked line — a six-mouse party and a three-rabbit party carrying the same haul, with exposure per animal falling as the number exposed rises.
DO: Do not add a sentence declaring that the claim is now arithmetic.

**C-11 · Species introductions lead** — *silent* · §4 · SRC V4-4
DO: Movement only, done in Phase 1. Do not add a note explaining the ordering.

**C-12 · One species per campaign** — *state, positive* · §4 · SRC V4-1
STATE: Each campaign is one species, for its whole length. The found-family beat lives in the Guest system.
DO: Remove cross-recruitment rebuttals at §4, §18.4 and §21.4.

## §5 · Two loops

**C-13 · Loop purposes** — *state, one sentence each* · §5.1, §5.3 · SRC V4-5
STATE: The domestic loop is how a place becomes worth protecting. The expedition loop is how the colony grows, and what growth costs.

**C-14 · §5.2 rebuilt around the pressure** — *state + say* · §5.2, §6.2 · SRC V4-6
STATE: The colony can always survive at home, and can never advance there. Everything it needs to live is within reach; everything it needs to become something is not. The corridor and its Reaches follow from that.
SAY: **The Median feeds you. It will not make you.**
DO: Lead with the pressure. The existing arrow chain moves below it.

## §6 · One folklore

**C-15 · The Escape is depicted, with names** — *silent* · §6.1 · SRC V4-9
DO: An instruction to the illustrator and to the narrative pass. The plate shows named animals; the opening narrative names them. Add no sentence telling the reader that it does.

**C-16 · Giants vocabulary varies** — *silent* · §6.3 · SRC V4-15
DO: Already stated for the Rivers of Thunder. Generalise in place — stable core, variable ornament — without a paragraph about why.

**C-17 · The hyphen-compound** — *silent in the body; stated in its own appendix* · SRC V5-59
DO: Create no §6.4. The body never addresses the convention. It is observed in the narrative, in the vocabulary, and diagrammatically on infographics, and it is set out once in the hyphen-compounds appendix. A translation convention exiled to an appendix is itself the tribute.

**C-18 · Compound constraints** — *silent* · SRC V5-59
DO: Compound nouns only; adjective-and-noun phrases stay as they are. Capital-lowercase. These govern authoring; they are not explained to the reader.

**C-19 · Compound vocabulary in use** — *show* · §4.1, §7.4, §21.2, §23.2 · SRC V5-59
SHOW: Use **Far-hole**, **Road-edge**, **Wall-edge**, **Sky-watch** in the passages where those things are described, without flagging them as instances of the convention.

## §7 · World geography

**C-20 · The Highway borders every Reach** — *state* · §7.3 · SRC V5-30
STATE: The Highway is the barrier between a Median Reach and either of its Margins. Every Reach in the corridor sits between carriageways.
DO: Correct the phrasing throughout the section.

**C-21 · Longitudinal / transverse** — *silent* · §7.3 · SRC V5-30
DO: The usage is correct and stays. Add nothing defending it.

**C-22 · Crossovers bound the Reaches** — *state* · §7.3 · SRC V5-31
STATE: Service crossovers and U-turn areas mark the boundary between one Reach and the next. Their hazard is exposure — open pavement, no cover, long sightlines, nowhere to freeze that is not visible. A party there is seen rather than struck.
DO: Do not explain that this makes them structurally different from a transverse Crossing.

**C-23 · The Margin's two edges** — *state, as a table* · §7.4 · SRC V5-27, V5-28
STATE: Every Reach has a Margin on each side. Each Margin has two edges.
Road-edge — rigid and flexible scrap, roadkill, litter, packaging, tyre fragments; hazard at full strength; everything the road sheds lands here.
Wall-edge — sheltered growth, seed banked against the wall, undisturbed soil, insects; quiet and out of the wind; nothing disturbs it.
No litter reaches the wall. Hazard rises toward the road.
DO: Delete the Edge Effect paragraph and the Quiet Zone. Delete the §8.1 edge-gradient sentence. The old Appendix A gradient line leaves with the appendix.

**C-24 · What the two edges ask** — *state + say* · §7.4, §6.2 · SRC V5-28
STATE: Everything the road sheds lands at the Road-edge. Nothing disturbs the Wall-edge — no mowing, no salt, no traffic — which is why it grows. A Reach therefore offers four working grounds rather than one strip.
SAY: **The road gives what it throws away. The wall gives what it keeps.**
DO: **Both.** The causes belong in the table as a third row; the proverb sits on the page as typography. The proverb is the better sentence and the row is the load-bearing one — cutting it would leave a reader knowing *that* the edges differ and not *why*. Write no sentence comparing the question to the one it replaces, and none observing that the answer changes with what the colony needs.

**C-25 · Reach lifecycle** — *state (table) + say* · §7.5, §29.1, §6.2 · SRC V5-29
STATE: **Unknown** — never scouted, blank on the corridor map. **Walked** — scouted and visitable; nothing persists, and the Reach reverts to wild between visits. **Held** — outposted; a genuine extension of the colony, fog cleared permanently.
SAY: **Walk it before you hold it.**
DO: Do not gloss the names, and do not observe that a Median Scout walks. The proverb teaches the sequence and the caution together, which is what the names were reaching for.

**C-26 · The ruined home is revisitable** — *state, one clause* · §7.6 · SRC V5-39
STATE: The Ancestral Warren, Den or Burrow can be returned to as a ruin, by Special Journey.

## §8 · Biomes and Anchor Points

**C-27 · Biome layout** — *silent* · §8.1 · SRC V5-24
DO: The layout — half-page renderings, three or four to a page, alternating sides — is a book-plan fact and lives in `200 book/Contents.md`. The GDD carries the art marker and nothing else. A book does not describe its own typesetting to the person holding it.

**C-28 · Scrub/briar aside** — *silent* · §8.1 · SRC V5-64
DO: Remove.

**C-29 · Selective expansion** — *say* · §6.2 · SRC V5-40
SAY: **Far ground, thin cover.**
DO: Anchors are already a bonus layer and §29.4 already rewards holding out for good ground. The proverb carries the cost. Do not reassure the reader that skipping Reaches is intended rather than a loophole.

## §9 · The day and traffic

**C-30 · One expedition at a time** — *state* · §9.1, §28 · SRC V5-5
STATE: One expedition runs at once, colony-wide. One expedition per citizen per day also holds. You send a party, and you wait.

**C-31 · Night is a trade** — *state, as a table* · §9.1 · SRC V5-25
STATE: Against night — extreme vehicle speed, reduced visibility, owls, higher tharn risk. For night — far fewer vehicles, no hawks, a quieter Margin, almost no human activity. The Fifth Law names the exchange.
DO: Rewrite the Night Velocity beat as a second operating window.

**C-32 · Bright night** — *state, one clause* · §34.1 · SRC V5-25
STATE: A highway at night is lit — sodium vapour, headlight wash, brake-light red, reflective signage, doubled in wet asphalt.
DO: Art direction only. Do not explain that this makes night look inviting.

**C-33 · An Anomaly reaches the Margin** — *state* · §9.2 · SRC V5-32
STATE: An Anomaly can stop traffic, opening a crossing window that does not otherwise exist, and spill cargo into the Margin as a windfall.

**C-34 · Six Spumes** — *state, in the existing list* · §9.3, §11.1 · SRC V5-33
STATE: Spring **Chemical** — salt runoff, herbicide, fertiliser drift; taints what grows. Autumn **Dust** — chaff, leaf litter, grit; reduces visibility. Existing four unchanged.
DO: Assign Chemical to spring and Dust to autumn in the seasons list. Remove the chemical-runoff-is-not-a-hazard line.

**C-35 · Hazard scales, richness does not** — *state, one sentence* · §9.3 · SRC V5-27
STATE: Wind Draft and the River's Spume grow worse toward the pavement and fall off toward the interior.
DO: Cross-reference §7.4 for the goods. Do not write a corrective sentence about gradients.

## §10 · Choice-Event Cards

**C-36 · Position** — *silent* · SRC V5-35
DO: Section move was Phase 1. Do not open the section by explaining why it comes first. One clause tying it forward to §11 is sufficient.

**C-37 · Ongoing cards** — *state* · §10 · SRC V5-55
STATE: A card may open, stay open, and close later — the response chosen now, the consequence landing after. Ongoing cards remain on the Community Board while they run.

## §11 · Seasons and Road Work

**C-38 · Road Work is local; disruption is not** — *state* · §11.2 · SRC V5-34
STATE: The physical work strikes one Reach. The card-pool modifier and the raised event frequency apply corridor-wide, so no Reach is insulated. A resurfacing programme may strike several Reaches in sequence.

**C-39 · Sidebar** — *state* · §11.2 · SRC V5-63
STATE: `CREATED VISUAL — "The season the machines came back"` · catastrophic Road Work onset, at the Reach it struck, with the citizens caught in it. Fallback: the event is written into the Chronicle.

## §12 · Scale

**C-40 · Three growth paths** — *state, one clause* · §12 · SRC V5-8
STATE: Wanderers, Nesting Season young, and Guest Citizens.

**C-41 · Growth in body-units** — *silent (deferred)* · §12 · SRC V5-8
DO: Log to the appendix guide as part of the population study. Do not settle it in the body. Do not describe the mouse curve's current shortcoming.

## §13 · Roles

**C-42 · The Leader** — *state* · §13, §28.2 · SRC V5-42
STATE: One citizen on each expedition is designated Leader, chosen at the Launcher. The Leader speaks in a Parley and takes the speaking exposure. The Leader is the subject of the expedition's Record entry.
DO: No expedition Role system. Scout, anchor and the rest stay describable in fiction and untracked. Do not write the argument against a second Role axis.

**C-43 · Teacher ungated** — *state, brief* · §13 · SRC V5-46
STATE: The Teacher is available from founding. Fear reduction works from the first day; the readiness effect acts once there are young. The Teacher works at the Story Circle, reciting the Laws.
DO: Do not characterise the staged effects as a progression signal that costs no rule.

**C-44 · Hearth work** — *state, one sentence* · §13 · SRC V5-47
STATE: When both members of a Hearth hold the same standing Role, that work is slightly more efficient.
DO: Frame as a Hearth effect. Do not explain that this preserves the Role-identical rule.

**C-45 · Standing assignments move** — *show* · folded into C-73 · SRC V5-43
DO: Redundant as a separate statement. The Likeness spread (C-73) and the slot tempo (C-64) already carry it. Delete the standing-Tool paragraph at §13 and cross-reference the Citizen Record instead.

## §14 · Resources

**C-46 · The weight ladder** — *state, as a table* · §14 · SRC V5-3
STATE: Trifle 1 — seed, crumb, bead, gravel chip; anyone. Small 5 — acorn, bottle cap, pull-tab, berry cluster; one mouse. Standard 10 — grass bundle, large mushroom, coil of wire; a rabbit, or two mice at 12. Heavy 20 — bread crust, folded fabric scrap; a squirrel, or two rabbits. Cooperative 40+ — two squirrels, four rabbits, seven mice.
DO: Replace the one-slot-equals-one-unit rate. Do not narrate the correction.

**C-47 · The relay in practice** — *show* · §4.3 or §14 · SRC V5-3
SHOW: A pair of mice sharing one Standard item — 6 alone is not enough, 12 together is.

**C-48 · Nameable hauls** — *show* · a Record excerpt · SRC V5-3
SHOW: A Standard Party's haul written as a fact in an Almanac entry — six Smalls, not sixty things.

**C-49 · Cooperative carrying** — *state, one sentence* · §14 · SRC V5-6
STATE: The party's carry totals; anything within the total comes home, with heavy items visibly shared.

**C-50 · Two Artifact classes** — *state* · §14, §20 · SRC V5-44
STATE: **Colony Artifacts** are held by the colony — a blueprint unlocked, a trade enabled, a standing problem solved. **Carried Artifacts** occupy a citizen's Tool slot and act in the field. Crafters make Tools from Scrap.
DO: Resolves the §14 / §26.7 disagreement about who holds an Artifact granting an extra Turn. Do not mention that a disagreement existed.

**C-51 · Numeric only where public** — *silent* · §19.4, §20 · SRC V5-45
DO: An item may state a number when the stat is already in the public ledger — carry, capacity. Hidden aptitude and contest odds stay descriptive. This governs how every item is written; it is not announced.

## §15 · Construction and decay

**C-52 · Maintenance drains Scrap** — *state* · §15 · SRC V5-48
STATE: Maintenance costs Flexible and Rigid Scrap on an ongoing basis.

**C-53 · Biomes wear differently** — *state, one line* · §15 · SRC V5-48
STATE: Culvert Garden rots timber · Concrete Trench bakes and cracks · Pond Hollow damps · Thin Grass Ribbon scours with wind.

## §16 · Structures

**C-54 · Species naming scoped** — *silent* · §16.1 · SRC V5-58
DO: Species-specific ladders for the central hub, food store, shelter and sleeping chambers, and lookout. One shared ladder elsewhere. The reader meets the result; the scoping rule is not explained, and no passage compares the four families against the rest.

**C-55 · Guest dwellings** — *show* · §16.1, §21.1, §21.2 · SRC V5-57
SHOW: Each Guest's roster entry names its Guest House skin and where it sits — a nest raised in a tree, a lodge at the water, a burrow beneath.
DO: Do not add a sentence observing that this makes the building family concrete.

## §17 · The Citizen Record

**C-56 · Bands reference** — *show* · §17 · SRC V5-56
SHOW: The Likeness spread uses the band names. The ordered table is the bands appendix's business, not this compile's.
DO: Do not write a paragraph explaining that the bands were previously undefined.

## §18 · Bonds and growth

**C-57 · Bonds cross; Hearths do not** — *state* · §18.1 · SRC V5-52
STATE: Trusted Friend bonds form between core citizens and Guests. Hearths are core-species only. The Hearth is the lineage unit; the Trusted Friend is the found-family unit.

**C-58 · Wanderers are easier** — *state* · §18.4 · SRC V5-53
STATE: Adopting a wanderer takes no Guest slot, no amenability check, and a lighter residence cost.

## §19 · Harm, fear and tharn

**C-59 · Maiming is ameliorated** — *state, one sentence, + say* · §19.1, §6.2 · SRC V5-17
STATE: Adaptive equipment reduces a maiming's penalty and never grants a capability the citizen did not have.
SAY: **The mending is not the making.**
DO: The veteran anchor effect already stands and is earned by having survived. Do not argue the case, and do not explain that the causality runs the right way round; the three reasons are in the Archive and the proverb carries the rest.

**C-60 · Tharn seizes the Turn** — *state + say* · §19.2, §26.4, §6.2 · SRC V5-11
STATE: When a citizen goes tharn the frame centres on them by name, and the next Turn is forced and scoped to the tharn. The Turn presents the party members who could go; the player chooses one. Tharn does not fire on a final round. Losing a citizen to untended tharn happens through deliberate abandonment or an impossible position, not through inattention.
SAY: **We do not leave what we can carry.**
DO: Do not observe that the dramaturgy falls out of the timing rule, or that this needs no new machinery. The proverb is deliberately ambiguous between cargo and citizen, which is the choice the Turn actually presents.

**C-61 · Fear memory has a trigger** — *state, one clause* · §19.2 · SRC V5-11
STATE: A fear memory is tied to the species that caused it.

**C-62 · Distinctions are named for their encounter** — *show* · §19.3, §23.1 · SRC V5-14
SHOW: A Tale excerpt granting a Distinction and the After-name together, both taking their wording from the night in question.
DO: Do not write the rule as a declarative. The excerpt is the rule.

**C-63 · Sidebars** — *state* · §19.1, §19.2 · SRC V5-63
STATE: `CREATED VISUAL — "Fennel, after the culvert"` at the permanent-change passage. `CREATED VISUAL — "Sharpnose goes tharn"` at the tharn passage. Each carries its fallback in one line.

## §20 · Equipment

**C-64 · Slot tempo** — *show* · §20, §22.2 · SRC V5-43
SHOW: On the Likeness spread — Tools persist until changed or returned; Supplies last one expedition and are picked at the Launcher.

**C-65 · Carried Artifacts in the Tool slot** — *state, one clause* · §20 · SRC V5-44

## §21 · Guest Citizens

**C-66 · A Guest is one body-unit** — *state, as a table* · §21.1 · SRC V5-4a
STATE: An Active Guest occupies one body-unit, displacing one rabbit, one squirrel, or two mice. Standard Party with a Guest — 2 rabbits + 1, 2 squirrels + 1, 4 mice + 1. Nominal Guest carry is 10.
DO: Do not explain that this equalises the Guest's weight across species.

**C-67 · Guests are depicted identically** — *silent* · §21.4, §34.1 · SRC V5-22
DO: Delete the passage stating that Guests wear less. Add nothing in its place. Guests appear dressed as core citizens are; the reader meets this in the artwork and in the Guest entries.

**C-68 · Ambient Guests can be hurt** — *state* · §21.2 · SRC V5-49
STATE: Ambient Guests are threatened during Base Defense, Road Work onset and catastrophe as core citizens are.
DO: Remove the downside-free-investment phrasing. Do not write the sentence about furniture.

**C-69 · The sky is answered by a Guest** — *state, brief* · §21.2 · SRC V5-41
STATE: **Owl** — night-weighted perimeter detection; the night Sky-watch. **Songbird** — home morale, and the day Sky-watch: songbirds mob raptors and give alarm calls.
DO: Two roster lines. The argument about currency, capped slots and found family is Archive. Do not state that nothing built defends against the sky — that belongs to the threat's own design pass.

**C-70 · Roster corrections** — *state, in the table* · §21.2 · SRC V5-50, V5-48
STATE: **Turtle** — a strongbox; a portion of stores is protected from any single loss event. **Firefly** — unchanged; lights the colony. **Bat** — protects structures from decay of every kind.
DO: Cultural Focus stays open; log it and say nothing in the body.

**C-71 · Dual species and the Rat** — *show, as a table* · §21.3 · SRC V5-51
SHOW: An antagonist table — Rat, antagonist only. Raccoon, Weasel, Hedgehog: contested nodes and the Active roster.
DO: Remove the paragraph explaining why the Rat is not a citizen.

**C-72 · Sidebar** — *state* · §27.2 · SRC V5-63
STATE: `CREATED VISUAL — "The night WHOOT came in"` at Guest recruitment, with its fallback.

## §22 · The Records

**C-73 · The Likeness is the equip screen** — *state* · §22.2 · SRC V5-43
STATE: Portrait, the three slots, standing Role and current condition sit on one screen and are changeable in place.

**C-74 · Sidebars** — *state* · §22.2, §22.3 · SRC V5-63
STATE: `CREATED VISUAL — "Bramble's Tale, illustrated"` and `CREATED VISUAL — "A Legendary return"`, each with its fallback. The Tale fallback is mandatory: templated prose from recorded events, no model involved.

**C-75 · Examples use the story colonies** — *show* · throughout · SRC V5-60
SHOW: Every worked example, Record excerpt and caption draws on one of the three colonies rather than a fresh anonymous instance.

## §23 · Names

**C-76 · Two naming acts** — *state* · §23.1 · SRC V5-54
STATE: A Given Name arrives — gifted by a Hearth at birth, or carried in by a wanderer or Guest. An After-name is earned. Nobody in this world names themselves.
DO: Remove *chosen* as a category.

**C-77 · A place's second name** — *state, one clause* · §23.2 · SRC V5-54
STATE: A place's event-conferred second name is its After-name.

**C-78 · Three colony registers** — *state, as a table* · §23.3 · SRC V4-16, V5-54
STATE: At founding the player is offered one candidate from each register — **Grounded** describes the place, **Aspirational** hopes, **Tribute** remembers the Ancestral Warren, Den or Burrow. Each reroll keeps the shape.
DO: Do not explain that this is more legible than three from one pool.

**C-79 · The three story colonies** — *state (table) + silent (recurrence)* · §23.3 · SRC V5-60, V4-7
STATE: Rabbit — Tribute. Squirrel — Aspirational. Wood Mouse — Grounded.
DO: The table is content. That the colonies' citizens recur through the book, and that the named Guests come from their histories, is the book narrating its own device — the reader meets the recurrence by meeting the same animals. Say neither. Names and citizens are a separate authoring pass; log it.

## §24 · Crossing

**C-80 · Load follows the party home** — *state, one clause* · §24.1 · SRC V5-10
STATE: Load bears on the return as well as on encounters.

## §25 · Field Mode

**C-81 · Home ground carries contest** — *state* · §25.4, §32 · SRC V5-36
STATE: Contest is possible on the Home Reach's Field layer, and its likelihood falls with each Colony Tier. Early foraging at home carries real risk; mature ground is genuinely safe.
DO: The aerial exception is logged, not a sentence in §25. Do not write the asymmetry argument into the body.

## §26 · Encounters

**C-82 · Encounter length** — *state, as a table* · §26.1 · SRC V5-9
STATE: Contested — 2 rounds, 1 Turn, the common case. 3 rounds, 2 Turns, when the second round stays close; rare. Uncontested — the frame opens and the node is described; it may resolve at once. Three rounds is the ceiling.
DO: Remove the one-round row and the "common case" label. Correct the §26.8 guardrail to *most contested encounters have one Turn*. Do not write the sentence about animation.

**C-83 · Change Approach** — *state, as a Turn row* · §26.4 · SRC V5-16
STATE: The party may change Approach at a Turn, to an Approach that was available at entry. The new Presence applies fresh and exposure does not reset.
DO: Do not write the paragraph about the fight that becomes a negotiation, or about the Turn gaining weight.

**C-84 · Load in resolution** — *state, one clause in the modifier list, + say* · §26.4, §6.2 · SRC V5-10
STATE: Carry load joins terrain, weather and maiming as a resolution modifier. A laden party is slower and more exposed.
SAY: **The heavier the haul, the longer the road home.**
DO: The proverb carries the expedition's arc. The node-limit consequence is one clause at §26.8 at most. Do not write "no new system," and do not describe the party as getting richer and worse at the same time.

**C-85 · Adversary numbers** — *silent* · §26.3 · SRC V5-12
DO: The adversary stays a Presence. Artwork and prose may show any number. This is an instruction to the illustrator; the reader should meet varied numbers, not a rule permitting them.

## §27 · Contest and recruitment

**C-86 · Antagonist frequency varies** — *silent* · §27.1 · SRC V5-15
DO: Vary with season, recent Road Work, biome, Reach state and outbuilding investment. Log the close. The body keeps its figure without a paragraph on variability.

**C-87 · Antagonists are named** — *show* · §27.2 · SRC V5-13
SHOW: The raccoon worked example carries the animal's name from the first encounter through to the Story Circle.
DO: Do not state that recognition requires a name.

## §28 · Expeditions

**C-88 · Party size** — *state, as a table* · §28 · SRC V5-4
STATE: Three to five body-units. Rabbit 3 animals, range 3–5, carry 30 / 50. Squirrel 3, 3–5, 60 / 100. Wood Mouse 6, 6–10, 36 / 60. The Launcher offers the Standard Party by default.
DO: Do not compute proportional-commitment percentages in the body; the ceilings they rest on are not canon.

**C-89 · Margin Raids from outposts** — *state* · §28.1, §29.2 · SRC V5-37
STATE: A Held Reach with a Staging Post can run Margin Raids of its own.

**C-90 · Special Journeys** — *state* · §28.1 · SRC V5-39
STATE: Gated to Tier II or above. The Rest-Stop Metropolis is the primary destination and the victory arc; the Ancestral Warren, Den or Burrow is revisitable as a ruin. Further story-forward destinations belong to this category.

## §29 · Outposts

**C-91 · Staging Post** — *state, one line in the set* · §29.2 · SRC V5-37

**C-92 · Three Outpost Roles** — *state, as a table* · §29.3 · SRC V5-38
STATE: **Keeper** maintains the central building and improves the trickle. **Watcher** works the visibility and predator-reduction outbuildings and lowers contest. **Forager** works the local ground.
DO: Do not add that this makes stationing a decision rather than a placement.

**C-93 · Sidebar** — *state* · §29.2 · SRC V5-63
STATE: `CREATED VISUAL — "The first outpost, finished"` with its fallback.

## §30 · The Metropolis

**C-94 · Lore guardrail** — *silent* · §30.4 · SRC V5-64
DO: Keep the guardrail as world fact. Remove the sentence explaining the document's caution about drift.

## §32 · Progression

**C-95 · Advancement costs** — *state, brief* · §32.1 · SRC V5-7
STATE: Advancement costs run at the stat frame's resolution and are a visible drop in the stores. Exact values are deferred.
DO: State Tier III positively; remove the Metropolis-dependence rebuttal.

**C-96 · Sidebar** — *state* · §32 · SRC V5-63
STATE: `CREATED VISUAL — "The colony at Tier III"` with its fallback.

## §34 · Art and sound

**C-97 · The material test** — *state, one clause* · §34.1, house style · SRC V5-18
STATE: What reaches a citizen's body is improvised from what the corridor sheds.
DO: **One clause, and it replaces the old framing rather than joining it** — the subsection currently opens by asking *how much* of a citizen's anthropomorphism reaches their body, which is the question this reverses, and deleting it without a replacement leaves the subsection with no thesis. The new clause is a description of the world, not a rule about a rule.
**The existing "Never depicted" list absorbs the banned side** — extend it to cover anything forged, smithed or cast. **The permitted side is house style and artwork only** — leaf helmets, cloth-scrap cloaks, twine belts, bark and shell, pouches, staffs; a staff carried, leaned on, balanced or slung, never one-ended and point-outward. Beyond the one clause, hang no lantern: every visible in the book obeys the test, which is how a reader learns it.

**C-98 · Gear is worn always** — *silent* · §34.1 · SRC V5-19
DO: Delete the dress-marks-leaving-home passage; the old Appendix A line leaves with the appendix. **Delete the "two things are worn at home as well as away" paragraph outright** — with no rule saying gear comes off, there is no expectation to correct, and the paragraph answers a question the reader never has.
**Keep its concrete visual content**, which is art direction rather than assertion: what a Keepsake looks like — a bead, a scrap of ribbon, a bottlecap on a cord — and that a maimed citizen is visibly maimed. One sentence, stripped of the always-worn framing. Write nothing about what dress does or does not mark.

**C-99 · Posture** — *silent* · §34.1, house style · SRC V5-20
DO: The Crossing is four-legged without exception; elsewhere posture serves the picture. Both are instructions to the illustrator, and every Crossing image will obey the first. Delete the existing naturalistic-posture paragraph and add nothing.

**C-100 · Role legibility** — *silent* · §34.1 · SRC V5-21
DO: Delete "Role is never worn." No uniform, badge, cord or livery; a citizen's carried kit plausibly reflects their work. The reader meets a Crafter with a pouch of oddments and a Watchkeeper carrying nothing. Do not write a rule contrasting kit with livery.

**C-101 · Sound as description** — *state, rewritten* · §34.3 · SRC V5-26
STATE: Traffic density and approach are learnable by ear. Something large arrives as low-frequency vibration before it is visible. Tharn is narrowed sound, breath and pulse. Road Work's window has its own soundscape, and the return of ordinary noise is how the colony knows it is over. The River's Spume is a continuous bed shifting with season and cycle. Home has its own species-specific rhythms.
DO: Retitle. Remove systemic-audio framing, directional-audio implementation and accessibility specification; the accessibility requirements stay at §33.5. Do not add a note explaining the conversion.

---

# PHASE 4 — Appendices

**Appendices are a separate project.** This compile writes no appendix content. It carries a manifest — the title of each, and one line saying what it will hold — and stops there. Everything else accumulates in `MEDIAN_appendix_guide.md`.

**A-1 · Document history leaves the book** — *silent* · SRC editorial
DO: Delete Appendices A, B, C and D. A canon checklist, a superseded record, a change record and an open-items list are contributor apparatus; none of them serves a reader. Their contents move to `500 log/canon_checklist.md`, `superseded.md`, `change_record.md` and `open_items.md`, and continue to be maintained there. Nothing is discarded and nothing is announced — the book does not explain that it once had them.

**A-2 · The manifest** — *state* · after §38
STATE, one line of scope each. Two groups of four:

| | Appendix | Holds |
|---|---|---|
| **A** | Building upgrade-name ladders | Named rungs for the four spatially distinct families |
| **B** | Folk place-name component banks | The parts every generated place name assembles from |
| **C** | The hyphen-compounds | The convention, and a growing glossary |
| **D** | The descriptive bands | The band names, in order, and what each means |
| **E** | Played on a Screen | MEDIAN as a video game — a page of depiction |
| **F** | Played at a Table | MEDIAN as a tabletop roleplaying game |
| **G** | Played with a Deck | MEDIAN as a card-driven game |
| **H** | Pictured by the Machine | MEDIAN as generated imagery |

DO: Titles and scope lines only. No content, no stubs, no *deferred, to be authored* notes — the manifest already says what is coming. Old E and F are re-lettered A and B; the rest are new. Further world appendices are proposed in the appendix guide and are not scoped here.

**A-3 · Generated imagery is a manifestation** — *silent* · SRC V5-63, editorial
DO: The reference-and-amend method is not a production note appended to the book; it is one of the four ways this world is rendered, on the same footing as a screen, a table and a deck. It takes a manifestation page and the same visual treatment. The front-matter sidebar and the nine distributed panels point at it.

**A-4 · Everything else** — *logged, not written*
DO: Route to `MEDIAN_appendix_guide.md`, which says where each lands: the new canon entries · the four rejections and the supersessions · the v0.4.6 record · the closes, the opens and the deferred authoring · the rescoping of the ladders · the Tribute components · the procedural method · the band set · the convention and glossary. Nothing on that list enters this compile.

**A-5 · Forward to v0.5** — *logged, not written*
DO: The four manifestation pages are authored as a project of their own, one visual page each. The screen page is **depiction** rather than specification, since the specification is already the book. §§36–37 leave the book at the same time — keeping the lens is not the same as keeping the production plan. None of this happens in this pass; the manifest names them and stops.

---

# PHASE 5 — Audit

Structural — thirty-eight sections · §§35–38 unchanged · no reference resolves to a missing heading · Contents matches the headings · no standalone generative-layer section · no Appendix A, B, C or D · the eight-appendix manifest present and empty of content.

Terminology — no *Character Record* · no *Edge Effect* · no *undiscovered / discovered-but-expedition-only / outposted* · `body-unit` lowercase throughout.

Substance — contested encounters always carry a Turn · body-units used for capacity, party size, food and score, and never for harm · Guests depicted as core citizens are · no core citizen bare by rule at home · the §34 guarantee present verbatim and unshortened · nine CREATED VISUAL panels · every worked example uses a story-colony citizen where one fits.

Voice — grep the body for: version numbers · *earlier · formerly · superseded · supersedes · replaced · no longer · retired · rejected* · *There is no… · There are no…* · *must not be* · *Why not* · *this document* · *no new system · no new machinery · without adding · at no cost · costs nothing* · *already exists · already does · already carries* · *worth stating* · *which is the point* · *reaching for*. Each hit is guilty until argued innocent.

Open flags — every one is an **OPEN —** callout pointing at `500 log/open_items.md`; none survives as inline prose; none carries a brief.

Weight — for every entry marked **show**, confirm no declarative sentence was written. For every **silent**, confirm nothing was added — **except where the entry replaces an existing thesis**, which is the one case a silent needs a clause. For every **say**, confirm the proverb reached §6.2 and its point of use, and that nothing carrying a concept was cut to make room for it.

Lens — confirm §3 kept its cameras, palettes, tempo and transitions, and §34 kept art and sound. Anything stripped from those two sections was stripped because the pictures carry it, never because the section was judged misplaced.

---

# ARCHIVE — WHY

Consulted only when a decision is challenged. **No line here may enter the book.** Where a full argument is wanted, the source decision logs hold it.

- **C-01** Replaceable citizens dissolve attachment; the ladder exists so danger has three rungs before a fourth.
- **C-02** §32.1 already places the Records inside Colony; the question is a designer's, not a reader's.
- **C-05** Makes four registers read as two symmetrical pairs and reinforces the spatial-fidelity rule.
- **C-08** Real ratios are 1 : 2 : 0.6; the ×10 frame exists so no species carries a fraction. The mouse pair's 12 pays for twice the bodies exposed.
- **C-09** Capacity quantizes; consequence does not. Same capability lost across a campaign, entirely different grief.
- **C-17** §1.1 forbids borrowing invented words and §6 requires original folklore, but nothing had established that these animals have a language. The convention asserts one at zero cost and is generative.
- **C-21** Highway engineering uses longitudinal for along-axis and transverse for across; geography is the wrong field.
- **C-23** Real verges are salt-damaged, compacted, mown and polluted at the pavement; plant richness peaks away from it. The Margin's canon richness was always the road's litter, which is edge-concentrated. Hazard survives the correction; the unified gradient does not.
- **C-29** Anchors are a bonus layer and §29.4 already rewards holding out. The strategy self-regulates: reach is paid for in exposure.
- **C-30** Protects the colony as the heart; expeditions are its dangerous counterpart, not a logistics network.
- **C-42** A second standing-assignment axis doubles the management surface and fights the group-mass model. §26.5 prices Parley speaking exposure without allocating it; the Leader allocates it for one choice rather than eight.
- **C-51** Pillar 2.3 makes colony capacity public and aptitude hidden. The rule was already implicit.
- **C-54** §16.1's claim that colonies feel like different civilizations is carried by the spatial families. Naming the infirmary three ways adds authoring cost without perceived difference — sixty rung names rather than a hundred and thirty.
- **C-59** The supercrip trope, rejected by name at §19.1. It inverts Pillar 2.5: a citizen valuable *because* of the loss has not lost anything. And it collapses the exposure symmetry, since a Maiming carrying a boost is not a bad tail. The veteran anchor effect is earned by surviving, not granted by the wound.
- **C-60** The Turn already exists between rounds. Rescue needs a subsequent Turn, so tharn can only fire in an encounter already running long — and long means close.
- **C-62** §23.1 grants the After-name with the first Distinction, so the After-name becomes derived from a remembered event rather than an adjective.
- **C-66** Counted per animal a Guest is 33% of a rabbit party and 17% of a mouse party. Counted in body-units it is a third of every Standard Party.
- **C-67** Decision 93 rested on distinguishability, which V5-19 dissolved. Cloth is about identity: a named crow with a satchel is a character.
- **C-68** §21 insists every Guest is a full equal-status citizen; one who cannot be hurt is furniture.
- **C-69** Ground danger falls with Tier because walls and lookouts are investments. Aerial danger cannot be built against, so it falls by relationship instead. WHOOT was written as the embodiment of this before the threat was specified.
- **C-82** An encounter where the player chooses an Approach and then watches is not a decision. The self-selecting length mechanism is untouched; only the floor moves.
- **C-83** §26.2 opens with *an encounter is not automatically a fight*, which was true only at entry. Change Approach makes it true inside the encounter.
- **C-84** Cargo ends the expedition without a limiter, and hands §24.2's choice of when to head home an actual decision.
- **C-85** Closes the art log's question about what a Presence looks like when it is never counted. The number was always flavour.
- **C-97** Decision 86 asked *how much* a citizen wears — a slider, endlessly arguable. Material is a category with a clean edge, and MEDIAN already applied it to buildings, crafting and equipment.
- **C-98** Decision 86 left citizens bare in the register where the player spends most of their time, which is exactly what Pillar 2.2 forbids. The registers were already enacting the rhythm.
- **C-100** *Role is never worn* cut against Ledger and Legible for a citizen standing still or out on expedition. Kit closes the gap through material culture rather than uniform.
