# Dry run — §7, §21, §34

Three sections executed against `MEDIAN_change_guide_v0.4.4_to_v0.4.6.md`, in final v0.4.6 numbering. Finished prose first; execution report after.

---
---

# §7 · World geography and terminology

### 7.1 The cross-section

**INFOGRAPHIC — The Cross-Section**

The world has a repeating structural geometry. From one outer boundary to the other, a typical playable cross-section is:

**Sound Wall → Margin → Highway → Home Median → Highway → Margin → Sound Wall**

The arrangement is symmetrical in principle, though terrain, lane count, elevation, vegetation, and accessibility may differ on each side. This is the one place in the document where *geometry* is the precise word: the cross-section is a designed structure that repeats, not a landscape.

The **Sound Wall** is a real, recognizable piece of highway infrastructure — a tall, often vine-covered concrete barrier — and it forms the permanent, impassable outer boundary of the playable world. This grounds the map's edge in something the player recognizes rather than an invented lore device; animals simply cannot scale it, and the world beyond is never modeled. The sound wall's *height* is pure flavor, never a mechanical figure.

### 7.2 Home Median

The **Home Median** is the central strip between opposing carriageways and the site of the player's colony. It can be narrow or broad, grassy or wooded, dry or culverted. It is relatively safe from traffic while still subject to predators, weather, runoff, vibration, disease, and Road Work.

The colony is built **in and on the Median**, not under the active highway and not in the Margin.

**The Home Median and the colony are two things with two names.** The Median is a Median Reach like any other and receives a **generated folk name** from the world (Section 23.2). The **colony** built on it receives the one name the player authors (Section 23.3). A colony called Horizon Fields may well stand on a reach the corridor has always called The Long Verge.

Because the Home Median is a full Reach, it has a **Field layer** of its own — biome, Anchor Points, node-bearing ground — and is not only ever seen as a diorama (Section 25.4).

### 7.3 Highway

The **Highway** is the active multi-lane barrier between a Median Reach and either of its Margins. **Every Reach in the corridor sits between carriageways** — that is what makes it a Reach — so the Highway borders all of them, and not only the Home Median. It is both boundary and playable hazard.

Highway danger is governed by **lane count**, from two up to four or five. Lane count is independent of the median biome beside it — a wide, lush median can sit against a narrow two-lane crossing, and a thin grass ribbon against a five-lane gauntlet. This decouples "how rich is this place" from "how dangerous is it to reach."

**Two manifestations.** The highway is encountered in two structurally different ways, and they should look and feel distinct:

- **Transverse crossing — Median to Margin.** Cutting *across* the lanes. The standard Crossing sequence (Section 24): stage at protected micro-cover, read the traffic, commit. Short, lateral, and the game's signature moment of nerve.
- **Longitudinal travel — Reach to Reach.** Moving *along* the corridor to another Median Reach. Distance rather than width; abstracted travel beats and corridor hazards rather than a single lane-by-lane gauntlet.

**Service crossovers mark the boundary between one Reach and the next.** The maintenance gaps and U-turn areas that break the median at intervals are how a party knows it has left one Reach and entered another.

Their danger is exposure. Almost nothing uses a crossover — maintenance and police, rarely — and what it offers instead is open pavement, no cover, long sightlines, and nowhere to freeze that is not visible. At a crossover a party is seen rather than struck.

> **OPEN — Longitudinal travel.** How it differs from a transverse crossing, in presentation and in mechanics. · `500 log/open_items.md`

In the animals' own vocabulary the highway is a river: the **Rivers of Thunder** or the **Roaring Rivers**, depending on which colony is speaking. The vehicles on it are **Roaring Iron**, and the humans inside are **the Giants** (Section 6.3).

### 7.4 Margin

The **Margin** is the resource-rich, ecologically chaotic strip between a highway and its outer sound wall. Fast pioneer plants, windblown seeds, insects, roadkill traces, litter, packaging, tire fragments, and other human detritus accumulate there.

**Every Reach has a Margin on each side**, and each Margin has two edges of its own. The two share ground type and differ in everything that matters.

> *The road gives what it throws away. The wall gives what it keeps.*

| | **Road-edge** | **Wall-edge** |
|---|---|---|
| **Goods** | Rigid and Flexible Scrap, roadkill, litter, packaging, tire fragments | Sustenance — sheltered growth, seed drift banked against the wall, undisturbed soil, insects |
| **Hazard** | Lethal. Wind Draft and the River's Spume at full strength | Low. Quiet, still, out of the wind |
| **Why** | Everything the road sheds lands here | Nothing disturbs it — no mowing, no salt, no traffic |

No litter reaches the wall. Debris is thrown or blown from the carriageway and settles near it; the far edge stays clean, and grows. Hazard rises toward the road (Section 9.3).

A Reach therefore offers four working grounds rather than one strip.

The Margin is renewable rather than permanently exhaustible. Nodes deplete locally, then replenish through plant growth and new waste deposition. Road Work can wipe the strip nearly bare for a time, resetting cover and yield before succession begins again.

The Margin is **never buildable under any circumstance.** It can be raided and traversed, but nothing the player builds ever persists there. This is a permanent property of the world, not a tier gate.

### 7.5 The median chain and the Median Reach

**INFOGRAPHIC — The Corridor Chain**

The Home Median is one segment in a longitudinal chain of medians extending up and down the corridor. Each remote segment is a **Median Reach**. Reaches differ in width, hydrology, vegetation, infrastructure, exposure, predators, lane count, and resource character.

A Reach stands in one of three states, described in full in Section 29:

| | |
|---|---|
| **Unknown** | Never scouted. A blank on the corridor map. |
| **Walked** | Scouted, and visitable through Field Mode. Nothing persists, and the Reach reverts to wild between visits. |
| **Held** | Outposted. A genuine extension of the colony, its fog cleared for good. |

> *Walk it before you hold it.*

**Every Reach carries a folk name**, generated from its actual character (Section 23.2) and paired with functional metadata tags rather than a second literal name.

**Each Reach is unified, and adjacent Reaches may differ sharply.** A Reach is internally coherent — one place with one character — and carries no sub-divisions. Its internal variation comes from Anchor Points (Section 8.2), which guarantee a mix rather than a monoculture.

Correspondingly, two neighboring Reaches **may differ more sharply than real-world geography would produce** — a wooded median can sit directly upstream of a concrete trench. This is a deliberate legibility-driven convention, stated explicitly so future Reach content is not "corrected" as though a jarring biome transition were an error. Variety comes from travelling between whole Reaches, never from subdividing one.

### 7.6 What else is out there

The corridor is not only medians and margins. Two things exist beyond the chain and are named here so the player has a map before they have an explanation:

- **The Rest-Stop Metropolis.** Far down the corridor, a large, old, genuinely multi-species animal settlement hidden in the neglected margins of a human rest stop — drainage spaces, service voids, dumpster enclosures, embankments, vents. It is the only city in this world, the primary destination of the Special Journey expedition, and the endpoint of the campaign's victory arc. **Part VI** is devoted to it.
- **The ancestral home.** Wherever the campaign's chosen species came from before the Founding Escape destroyed it — now a permanent hazardous construction zone, and revisitable as a ruin by Special Journey from Tier II (Sections 28.1, 35.1).

---
---

# §21 · Guest Citizens

Guest Citizens are rare, named, non-breeding animals from outside the colony's core species. Inspired directly by Kehaar in *Watership Down* — a designer-facing reference; no *Watership Down* name appears in MEDIAN's own fiction (Section 6) — the system brings a wide variety of animal life into a campaign without requiring every species to support a full civilization ruleset. Each campaign is one species (Section 4), and this is where the found-family beat lives.

**Every recruited Guest is a full, equal-status, named citizen** — not a subordinate, not a unit. They have Citizen Records, bonds, Keepsakes, Distinctions, and After-names like anyone else. They differ from core citizens in exactly two ways: they occupy their own separate capped slot pools, and they arrive through recruitment rather than birth. A joining Guest receives a **Given Name** (Section 23.1) — and carries it *from the first encounter*, before any decision to recruit. The player meets a named animal, not a candidate.

Guests are housed in the **Guest House**, one building family whose skin and placement vary with its occupant (Section 16.1).

Two tiers: **Active Guests** and **Ambient Guests.**

*The procedure for recruiting a Guest — the contest funnel, the amenability check, the residence cost, and the slot cap — lives in Section 27, because recruitment happens in the field.*

### 21.1 Active Guests

**INFOGRAPHIC — Active Guests: The Seven**

**ARTWORK — Guest Vignettes**

Active Guests join expedition parties, occupying a valuable slot and introducing a bounded ability, traversal option, defensive behavior, negotiation route, or information advantage. They do not remove the core citizens' need to take risks.

The **universal contribution rule** holds with **zero exceptions**: every citizen, Guest included, contributes on *both* carry and fight to some non-zero degree, so no recruit is ever pure dead weight outside its specialty.

**An Active Guest occupies one body-unit** (Section 4.4), displacing one rabbit, one squirrel, or two mice.

| Standard Party with a Guest | Composition |
|---|---|
| Rabbit | 2 rabbits + 1 Guest |
| Squirrel | 2 squirrels + 1 Guest |
| **Wood Mouse** | **4 mice + 1 Guest** |

A Guest's nominal carry is 10, matching a rabbit; larger Guests exceed it and smaller ones fall short.

**Guests are option-openers, not stat sticks.** This is the roster's governing design premise. A Guest modifies the **available options** in an encounter rather than the score: the Mink does not add a bonus, the Mink makes *"rescue from water"* an available Turn action that otherwise is not on the menu (Section 26).

> **The template: each Active Guest opens at least one Approach or Turn action, and closes or complicates at least one.**

This is how every Guest acquires a situational trade-off systematically, rather than through seven bespoke penalties invented one at a time. A Guest who opens one door and closes another is inherently a decision.

The roster is **seven**:

| Guest | Opens | Closes / complicates | Dwelling |
|---|---|---|---|
| **Weasel** | Contest against small predators; high carry and fight muscle | Parley with prey species — they are afraid of it | A den worked into the bank |
| **Fox** | Windfall processing — the only Guest that can safely render a predator kill or major roadkill into usable resources | Evade — too large to go unnoticed | An earth at the colony's edge |
| **Mink** | Rescue from water, culverts, and drainage | Little value away from water | A lodge at the waterline |
| **Crow** | Aerial scouting — reveals a node's Approach set before the party commits | The party cannot Evade while it is overhead | A nest raised in the canopy |
| **Hedgehog** | Contest above the party's weight; durable escort and cover | Slow — raises exposure on Evade | A hollow under the hedge line |
| **Snake** | Parley by intimidation and display; minimal but non-zero carry | Movement penalty in Winter (Section 4.5) | A warm stone shelter, south-facing |
| **Raccoon** | **Sealed human-container nodes** — latched coolers, zip-tied bags, capped bottles, bins (Section 25.3) | Draws other scavengers — raises contest frequency at nearby nodes | A raised box against the trunk |

**Seven Guests against four slots.** The roster exceeds the slot cap deliberately: the player fields a fraction of what exists, and passing on a good recruit costs something (Section 27.3).

> **OPEN — The Guest roster.** The opens/closes pairs, and each Guest's carry against the one-body-unit baseline. · `500 log/open_items.md`

### 21.2 Ambient Guests

**INFOGRAPHIC — Ambient Guests: The Nine**

Ambient Guests live at the Home Median or, once unlocked, at an outpost, providing a spatial passive effect while remaining visible residents with routines and relationships. The option-opener template does not apply to them, because they never enter an encounter.

**Ambient Guests can be hurt.** They are threatened during Base Defense, Road Work onset and catastrophe exactly as core citizens are. WHOOT can be lost.

The roster is nine:

| Guest | Passive effect | Dwelling |
|---|---|---|
| **Owl** | Increases passive perimeter predator-detection radius, night-weighted — the night **Sky-watch**. *Stays passive; never an escort.* | A hollow high in the largest tree |
| **Songbird** | Ambient morale and efficiency at home, and the day **Sky-watch**: songbirds mob raptors and give alarm calls. | A small nest near the Story Circle |
| **Toad** | Reduces spoilage and loss on stored food; steadies its wet-culvert surroundings. | A damp niche at the culvert mouth |
| **Firefly** | Extends the duration of safe nighttime colony activity, lighting the colony itself. | A grass hollow, unroofed |
| **Groundhog** | Advance warning of seasonal and weather events, and of approaching **Choice-Event Cards** — always qualitative, never a countdown. | A deep burrow at the perimeter |
| **Turtle** | A **strongbox**: a portion of the colony's stores is protected from any single loss event. | A sunk stone chamber by the water |
| **Bee** | Increases yield from foraged plant resources. | A hanging comb under shelter |
| **Mole** | Reveals soil and structural information. | Tunnels beneath the whole colony |
| **Bat** | Protects structures from decay of every kind (Section 15). | A roost in the highest dry dark |

**The sky is answered by a bird.** The Fifth Law splits it by time — *"Hawks own the day, owls own the night"* — and the roster splits the same way. The Owl holds the night and the Songbird the day, and the pair is the colony's only cover against what comes from above. It costs a capped slot, so sky-safety competes directly with Bee yield, Toad preservation and Firefly light.

When several Ambient Guests live at home, the player may select one effect for a temporary **Cultural Focus** boost; the others continue providing their normal effects. Ambient Guests may be assigned to compatible outposts, one per outpost central building.

> **OPEN — Cultural Focus.** How it flavours a colony rather than raising a number. · `500 log/open_items.md`

**Template character — WHOOT.** The Owl's eventual flavor writeup uses a template character: **WHOOT**, a barred owl with a permanently weak wing who can no longer hunt on the move and has become a stationary watcher instead. WHOOT gives a warm, concrete backstory reason for the rule that the Owl stays passive and is never an escort — and doubles as a lived demonstration of Pillar 2.5 applied to a Guest rather than a core citizen: a maimed animal remains valuable, and finds the role that fits. Because Ambient Guests do not expedition, WHOOT's injury reads as pre-colony history rather than an in-system Maiming, and it neither grants nor requires an After-name.

> **OPEN — Example citizens.** A wider set of writeups in the register of tabletop RPG sourcebook NPC entries. · `500 log/open_items.md`

### 21.3 Antagonist fauna, and the ones who can change sides

Not every animal met in the field is a candidate for the colony. Some are simply threats.

| Antagonist | Where it appears |
|---|---|
| **Rat** | Contested nodes and Base Defense. Antagonist only. |
| **Raccoon** | Contested nodes and Base Defense — and the Active roster. |
| **Weasel** | Contested nodes — and the Active roster. |
| **Hedgehog** | Contested nodes — and the Active roster. |
| Predators, territorial rivals, desperate scavengers, environmental obstruction | Throughout |

**Three animals sit on both sides of that line.** The raccoon is the worked case: bigger and cannier than the Rat, a real threat at a contested node, and recruitable. It can be met as an enemy, met again as a neutral, and eventually brought home (Sections 27.2, 21.1) — carrying the same name throughout, so the player can tell it is the same animal.

**Antagonist status in MEDIAN is a position an animal currently occupies, not always a fixed nature.**

---
---

# §34 · Art and sound

### 34.1 Visual identity

Grounded stylized realism at animal scale. The world combines soft organic material — fur, grass, roots, mud, bark, feathers — with harsh human infrastructure — wet asphalt, concrete, salt, rust, tire rubber, reflective signs, plastic, drainage metal. The art culture takes *Mouse Guard* as a modern-register touchstone, without its medieval trappings.

The tone is **atmospheric and tactile, not relentlessly grim.** Home scenes may be warm, lively, and gently storybook; expedition scenes become colder, larger, and more cinematic.

Avoid sci-fi interfaces, neon technology, and brushed-metal title treatments that make the animal world feel manufactured. There is no military or mature-rated visual framing.

**Night is lit.** A highway after dark is one of the most illuminated environments there is: sodium vapour, headlight wash, brake-light red, reflective signage, and all of it doubled in wet asphalt (Section 9.1).

### On anthropomorphism — the line

The citizens are heavily anthropomorphized as *characters*: they have names, families, grief, folklore, and standing jobs. What reaches their bodies is improvised from what the corridor sheds. *Mouse Guard* is the reference and the reference already contains the answer — MEDIAN takes its **small-animal material culture** and refuses its **medieval trappings** (Section 1.1).

A **Keepsake** is a citizen's permanent identifier — a bead, a scrap of ribbon, a bottlecap on a cord. **Adaptive equipment** (Section 19.1) is as much a part of a citizen as their Keepsake, and a maimed citizen is visibly maimed.

**Cloth is found, never dyed.** Colony material culture is scavenged (Section 14), and scavenged fabric carries the colors of the roadside: high-visibility orange, safety-vest yellow, sign green and white, tarp blue, burlap, plastic, retread black. Every citizen in a colony is the same animal, so cloth is what tells them apart — and it states the setting in the same stroke.

**A citizen's kit reflects their work.** A Crafter carries a pouch of oddments, a Healer bundled moss, a Builder lashings; a Watchkeeper carries nothing at all, because their work is to watch.

**Never depicted:** weapons of any kind · armor, including bracers and any cross-body strap, which reads as a weapon harness whether or not it carries one · anything forged, smithed or cast · helmets, uniforms, badges, cords, livery · animals dressed as miniature people. The equipment slot is named **Tool** and never "Weapon" for exactly this reason (Section 20).

**Expression sits in ears and posture first.** Rodent facial musculature is limited and pushing a face past it tips into cartoon. Ears are enormously expressive on all three species and cost nothing. This matters mechanically as well as tonally: fear must be visible in the world as a frightened posture (Pillar 2.3), and tharn must read through more than an icon (Section 34.3).

**Escalation without industry.** Dress quality tracks Colony Tier — torn bag strip at Tier I, selected and cleaned and well-stitched scrap by Tier IV — on exactly the principle governing the building ladders (Section 16.2): grandeur through scrap-mastery, never through machinery.

**Wordmark and logomark (concept direction, adopted).** The MEDIAN title is rendered with a **cracked-asphalt and shattered-glass letterfill**, accompanied by a companion **"//" logomark** styled as **mossy concrete lane-marking relief** — a candidate app and loading icon, and a quiet piece of wordplay, since a median is precisely the thing that sits between two lane markings. Both are built from the material vocabulary already established: the title treatment is made of the world rather than imported from a hardware catalogue.

### 34.2 Scale language and vehicle presence

**INFOGRAPHIC — Scale Language**

Scale should be communicated through recognizable infrastructure and material texture: lane paint, tire fragments, guardrail bolts, culvert mouths, drainage grates, barrier seams, distant vehicle mass. Cars should not intrude impossibly close to safe colony compositions.

**Vehicle and machine flavor belongs throughout the world, not only on the road.** The corridor is littered with the remains of what passes along it, and biomes should carry that: a wrecked car under an interchange, an engine block half-swallowed by grass, a rusted piece of abandoned construction equipment, retread tire fragments, bumper shards, a hubcap. In the Margin, a wreck can be a **node** in its own right. This is how the world states its scale contrast without ever showing a human.

**Human bodies never appear. There is no exception.** The Giants live in folklore, spoken about and never depicted (Section 6.3).

Machinery without a visible operator reads as indifferent force rather than intent — which is precisely what Section 11.2 already demands of it, something evaded or sheltered from and **never negotiated with**. An operator invites appeal. The absence of one is the horror, and it is also the more accurate account of what the corridor actually is to the animals living in it: not malice, but weather with a schedule.

This rule was only ever about human bodies. **Vehicles are unaffected** — Roaring Iron is visible constantly and by design, and machinery at work is visible in full.

**Catastrophe is sensory-obscured.** Destruction and death are conveyed through dust, noise, vibration, distance, and narrowed perception rather than depicted. There is no explicit blood or gore. This is the same presentation vocabulary used for tharn (Section 34.3), which means the Founding Escape teaches the player how catastrophe *reads* in this game before tharn ever fires on a citizen.

### 34.3 The sound of the world

**INFOGRAPHIC — Art and Audio Style Guide**

A place is partly what it sounds like, and the corridor is a loud one.

**Traffic is legible by ear.** Density and approach are learnable without looking, and something large announces itself as low-frequency vibration through the ground before it is visible at all. A party that has learned the sound knows to be somewhere else.

**Tharn is narrowed sound, breath and pulse.** The world outside the frozen citizen recedes; what is left is very close and very loud.

**Road Work changes the soundscape for the length of its persistence window** (Section 11.2). The return of ordinary noise is how the colony knows it is over.

**The River's Spume is a continuous ambient bed**, its texture shifting with the season and the traffic cycle (Section 9.3): hot and battering in summer, thin and cold in winter, choking at Rush, gritty in the autumn dust.

**Home sounds like home** — species-specific movement, construction, conversation, shelter against weather, and the domestic rhythms of a working colony. It is the one register where the road is held at arm's length (Section 3.5), and the sound design is what carries that.

Adaptive devices and lasting injuries alter movement sound respectfully and consistently.

---
---

# Execution report

*Rulings taken after the first draft are folded into the prose above. The findings are kept, since they are what the dry run was for.*

## Where the guide failed, or gave too little

### 1. §34.1's thesis sentence is orphaned by C-97 · **needs a ruling**

The existing subsection opens: *"The question is how much of that reaches their bodies."* That is precisely the question the material test **reverses** — the line is material, not quantity. C-97 is marked `silent`, so I may not state the replacement. Executing it strictly means deleting the framing and leaving the subsection with no thesis at all: a list of rules with nothing joining them.

Ruled: C-97 moves to `state, one clause` — one positive, world-facing clause replacing the old question:

> *What reaches their bodies is improvised from what the corridor sheds.*

That is a description rather than a rule about a rule, and it hangs no lantern. The two lists and the argument stay out. Applied in the prose above and in the guide.

**The general lesson.** `silent` works cleanly when a passage is *added*. When a passage is *reversed*, the old text's framing has to be replaced rather than deleted, and silent leaves a hole. Any entry reversing existing framing needs at least one clause. Worth checking C-05, C-15 and C-99 against this — I think all three are safe, because none of them replaces a thesis sentence.

### 2. "Two things are worn at home as well as away" needs rewriting, not deleting

C-98 says *extend silently to cloak, belt, pouch and kit*. But the paragraph's entire structure is a contrast against a rule that no longer exists — once everything is worn always, "two things are worn at home as well" is nonsense. Ruled: delete the paragraph outright — with no rule saying gear comes off, there is no expectation to correct. Its **concrete visual content** stays, because that is art direction rather than assertion: what a Keepsake looks like, and that a maimed citizen is visibly maimed. One sentence, no framing.

### 3. §21.4 collapses entirely · **not anticipated**

Both of its contents leave: the single-species callout is document history (C-12) and the Guests-wear-less rule is reversed and silenced (C-67). What survived was one sentence pointing at the Guest House. I folded that into the section preamble and **deleted §21.4**.

Ruled: §21 carries three subsections, not four, and the Contents follows. Now **S-9b** in Phase 1, rather than something an assembler discovers in Phase 3.

### 4. Where do Sayings get quoted, and what may they displace? · **ruled**

The guide said a `say` claim is carried by a Saying in §6.2 and stopped there. The **Laws are already quoted at point of use** — the First Law appears in §24.1 where Crossing is specified — so both §7 proverbs are quoted where the material sits as well as collected in §6.2. On the page they are typography rather than another body paragraph.

**And `say` is additive.** My first draft used the proverb to justify deleting the two-edge table's "Why" row. That was a bad trade: a reader was left knowing *that* the edges differ and not *why*. The row is restored, and the guide now reads — cut prose only where the proverb genuinely makes it redundant, or where what is being cut is self-justification rather than content. A beautiful line that costs the reader an idea is not worth having.

## What worked

**`say` earns its place, but not as a substitute.** In §7.4 the proverb sits above a table it does not replace. The section is longer than my first draft and better than either.

**Four consecutive `silent` entries in §34.1 did not leave a hole** — once the thesis was fixed. Dropping dress-marks-leaving, posture and role-never-worn removed ~180 words and the subsection reads better, not thinner. C-100's replacement is a single concrete sentence about what a Crafter carries, which does more work than the rule it replaced.

**The OPEN callouts are a clear improvement.** Four in §21 alone, where v0.4.4 had them buried mid-paragraph in three different formats. As a class they are obvious, skippable, and greppable.

**`show` worked in §21.3.** The antagonist table states the Rat's status without the paragraph that used to argue for it, and dropping that paragraph cost nothing.

## Smaller notes

- **§7.1 and the world primer now overlap.** Both give the cross-section, within four sections of each other. Not a conflict — the primer's job is to precede the registers — but a reader meets the same diagram twice. Worth a decision.
- **Guest dwellings became a table column** rather than prose, in both rosters. Cheaper than sentences and it reads as a field guide, which suits.
- **§7.3 retains "the game's signature moment of nerve."** C-07 names only §3.4 and §24.1, so strictly this survives. It probably wants the same treatment.
- **Section renumbering held.** Every cross-reference in all three sections mapped cleanly; no ambiguity, no orphans.
