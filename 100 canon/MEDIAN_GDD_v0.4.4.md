# MEDIAN

## Game Design Document v0.4.4

**Working title:** MEDIAN
**Genre:** Atmospheric animal colony builder with high-stakes expedition action — a base-builder first ("Age of Empires, minus combat, with the heart of *Watership Down*")
**Primary platform:** PC and console, including handheld console form factors such as Steam Deck and Switch-class devices
**Mode:** Single-player
**Presentation:** Four registers — an inhabited **Colony** view, a surveyed **Field** view, a rendered **Encounter** view, and an immediate **Crossing** view (Section 3)
**Status:** Pre-production concept document
**Origin:** Conceived by Asa Wember, July 2026, after observing highway medians from a bus between Washington, DC and New York City

> **Animal colony building on highway median strips.** Build a beloved, physically legible settlement in the overlooked green islands between highways, then risk named citizens on dangerous expeditions across asphalt and along a chain of changing median biomes.

> **About this document.** MEDIAN is governed by a settled record of **93 design decisions**. This body states what the game is. Its development history — what was considered, what was set aside, and why — is kept out of the body and collected in Appendix B; a change record is in Appendix C, and open items in Appendix D.

**ARTWORK — Title and Wordmark**

> **On the art markers.** Lines set like the one above mark where illustration belongs when this document is set as the illustrated concept book. **ARTWORK** is a full-page image; **INFOGRAPHIC** is an information-design plate. They are placement notes, not part of the specification, and carry no canon weight. Sixty-five appear in the body — forty-four plates and twenty-one images. Spot illustrations, which sit alongside body text throughout, are not marked individually.

### Elevator pitch

**Age of Empires-style colony progression in a highway median, with the emotional animal-world storytelling of *Watership Down*.** The player guides one small civilization of rabbits, squirrels, or wood mice. Safe local sustenance supports everyday life, but lasting advancement requires expeditions beyond the home median: across live traffic to the resource-rich Margin, or down the highway to discover new median biomes, establish outposts, meet outsiders, and eventually connect with a distant multi-species animal metropolis.

MEDIAN is a base-builder first, and a resolution-based one — not a tactical-extraction shooter, not a combat-first RTS, and not a road-crossing arcade game with a management wrapper. The colony is the heart of the game. Expeditions are not the reason the base exists; they are the dangerous, dramaturgically justified action counterpart to a base-building game. The player should become attached to the place they build and to the handful of named animals who live there.

## Contents


**PART I — What MEDIAN is** · *Thesis and pillars, then the shape of the game.*

- 1. Creative thesis
    - 1.1 Core inspirations
    - 1.2 What the game is not
- 2. Design pillars
    - 2.1 Attachment-first base-building
    - 2.2 Named citizens, low population, durable identity
    - 2.3 Ledger and legible
    - 2.4 Expeditions make stories and enable progress
    - 2.5 Consequence without disposability
    - 2.6 Mechanical restraint, expressive variety
    - 2.7 One world, four registers
- 3. Four registers
    - 3.1 Colony — dwell
    - 3.2 Field — travel
    - 3.3 Encounter — meet
    - 3.4 Crossing — risk
    - 3.5 Constraints binding all four
- 4. Three species
    - 4.1 The shared stat frame
    - 4.2 Rabbit — burrow civilization
    - 4.3 Squirrel — canopy civilization
    - 4.4 Wood Mouse — dense, distributed civilization
    - 4.5 Seasonal and environmental personalization
- 5. Two loops
    - 5.1 The domestic loop
    - 5.2 The bridge between them
    - 5.3 The expedition loop
- 6. One folklore
    - 6.1 The Laws of the Median
    - 6.2 The Sayings of the Median
    - 6.3 The Giants — vocabulary for the human world

**PART II — The world** · *The ground the game happens on, and the forces acting on it.*

- 7. World geography and terminology
    - 7.1 The cross-section
    - 7.2 Home Median
    - 7.3 Highway
    - 7.4 Margin
    - 7.5 The median chain and the Median Reach
    - 7.6 What else is out there
- 8. Median biomes and Anchor Points
    - 8.1 The eight biomes
    - 8.2 Anchor Points
- 9. The day, traffic, and traffic as weather
    - 9.1 Daily structure
    - 9.2 Traffic cycles
    - 9.3 Traffic behaves like weather
- 10. Seasons, Road Work, and Choice-Event Cards
    - 10.1 Seasons
    - 10.2 Road Work
    - 10.3 Choice-Event Cards

**PART III — The colony** · *The home the whole game is in service of.*

- 11. Scale and the shape of a colony
- 12. Roles and daily work
- 13. Resources and the economy
- 14. Construction, decay, and the Construction Queue
- 15. Structures and upgrade ladders
    - 15.1 Structure families
    - 15.2 Named upgrade ladders
    - 15.3 Functional icons, the Community Board, and the Story Circle

**PART IV — The citizens** · *Who lives there, what happens to them, how they are remembered.*

- 16. The citizen record
- 17. Bonds, Hearths, and growth
    - 17.1 Bonds
    - 17.2 Hearths and lineage
    - 17.3 Nesting Season
    - 17.4 Wanderers — the other way a colony grows
    - 17.5 Death and memorialization
- 18. Harm, fear, and tharn
    - 18.1 The harm ladder
    - 18.2 Fear and going tharn
    - 18.3 Distinctions, the symmetry, and the After-name
    - 18.4 How citizens develop
- 19. Equipment: Keepsake, Tool, and Supply
- 20. Guest Citizens
    - 20.1 Active Guests
    - 20.2 Ambient Guests
    - 20.3 Antagonist fauna, and the ones who can change sides
    - 20.4 Single-species colonies and Guest accommodation
- 21. The Records
    - 21.1 The Colony Record — Almanac and Chronicle
    - 21.2 The Character Record — Likeness and Tale
    - 21.3 Expedition Rating and the Report and Share debrief
- 22. Names
    - 22.1 Names of citizens — Given Name and After-name
    - 22.2 Names of places — the folk-name grammar
    - 22.3 The one name the player authors

**PART V — Leaving home** · *The three away-registers, and the systems that govern what happens out there.*

- 23. Crossing
    - 23.1 The crossing action
    - 23.2 Return logic
- 24. Field Mode
    - 24.1 What it is
    - 24.2 Presentation and overlays
    - 24.3 Node types
    - 24.4 Field Mode generalizes
- 25. Encounters
    - 25.1 The shape of an encounter
    - 25.2 Approaches
    - 25.3 The group layer — mass, never a roster
    - 25.4 Resolution
    - 25.5 Exposure — the individual layer
    - 25.6 The outcome distribution
    - 25.7 The epic case
    - 25.8 Guardrails
    - 25.9 What this system does not govern
- 26. Contest, recruitment, and Base Defense
    - 26.1 What is contested
    - 26.2 The recruitment funnel
    - 26.3 Slot scaling and scarcity
    - 26.4 Base Defense
- 27. Expeditions and the Launcher
    - 27.1 Expedition categories
    - 27.2 The Expedition Launcher
    - 27.3 Early expedition onboarding
- 28. Outposts
    - 28.1 Reach lifecycle and fog of war
    - 28.2 The outpost building set
    - 28.3 Stationing a citizen
    - 28.4 Contest and the value of investment
    - 28.5 Active versus passive value

**PART VI — The Rest-Stop Metropolis** · *The corridor’s one city.*

- 29. The Metropolis
    - 29.1 The place
    - 29.2 Presentation — a Field territory with venues as nodes
    - 29.3 Core functions
    - 29.4 A founding myth, and what it does not mean
- 30. The Metropolis in the campaign
    - 30.1 Campaign role
    - 30.2 Victory and continuation

**PART VII — Progression and presentation** · *Tiers, interface, art, the optional layer, and how a campaign opens.*

- 31. Progression tiers
    - Tier I — Scavenger Camp
    - Tier II — Fortified Settlement
    - Tier III — Independent Colony
    - Tier IV — Sovereign Network
    - 31.1 Advancement gates
- 32. Interface and information design
    - 32.1 The Colony view
    - 32.2 Blueprint / ledger overlay
    - 32.3 Character Records and the Village Roster
    - 32.4 The Expedition Launcher
    - 32.5 Controls and accessibility
- 33. Art and audio direction
    - 33.1 Visual identity
    - 33.2 Scale language and vehicle presence
    - 33.3 Audio
- 34. The optional generative layer
- 35. Campaign onboarding
    - 35.1 The Founding Escape
    - 35.2 Tutorial sequence

**PART VIII — Production notes** · *Suggestions rather than canon — plus the canonical summary.*

- 36. Suggested scope and roadmap
    - 36.1 A suggested vertical slice
    - 36.2 A suggested V1 target
    - 36.3 A suggested approach to world events
    - 36.4 Suggested later expansion candidates
- 37. Suggested prototype success criteria
- 38. One-paragraph canonical summary

**APPENDICES**

- Appendix A — Canonical decisions and explicit exclusions
- Appendix B — Document history and superseded material
- Appendix C — Change record
    - v0.4.4 — the document-history pass
    - v0.4.3 — the art direction edition
    - v0.4.2 — the restructuring edition
- Appendix D — Open items
    - Deferred numeric tuning
    - Open design
    - Parked
    - Unnamed in fiction
    - Deferred to Phase 2 — the art production pass
    - Deferred authoring
    - Future-work backlog
- Appendix E — Per-family building upgrade-name ladders
- Appendix F — Folk place-name component banks

---

# PART I — WHAT MEDIAN IS

**ARTWORK — The Colony Between Two Highways**

*Read in one sitting, this part should leave a reader able to describe the game accurately. It states the thesis and the pillars, then the game's shape: **four registers, three species, two loops, one folklore.***

---

## 1. Creative thesis

MEDIAN is about making a permanent home in a place humans consider leftover space.

The highway provides more than a visual setting. It supplies the world geometry, boundaries, resources, hazards, rhythms, soundscape, and scale contrast. The animals do not imitate a tiny human industrial society. They remain animals, using teeth, paws, instinct, ecological knowledge, plant matter, and scavenged objects to survive inside human infrastructure.

The desired emotional rhythm alternates between:

- **Sanctuary:** patient construction, observation, maintenance, social life, and attachment inside the Home Median.
- **Exposure:** leaving safety for an expedition whose outcome can create resources, knowledge, relationships, injuries, and stories.
- **Return:** bringing both material gains and lived consequences back into the colony.

The home must feel worth protecting. Danger has meaning because the player knows exactly who went out and what they came back to.

This rhythm is not only thematic. It is **enacted by the game's presentation**: each of the four registers in Section 3 corresponds to a phase of it, so the player feels sanctuary, exposure, and return in the camera before feeling them in a mechanic.

### 1.1 Core inspirations

*Watership Down* is the primary inspiration and sets the emotional and dramaturgical register. MEDIAN treats animal-scale peril, social identity, folklore, political encounters, found-family relationships, and the terror-freeze response known as going **tharn** as its narrative center of gravity. The game imagines a story beginning roughly where *Watership Down* leaves off: a small band that has already survived a founding catastrophe, now trying to build something lasting.

- ***Watership Down* (primary):** animal-scale peril, social identity, folklore, political encounters, found family, and tharn.
- **Age of Empires:** comprehensible advancement tiers, a satisfying transformation from vulnerable settlement to mature civilization, and spatially readable economic growth — minus combat as a central pillar.
- ***Mouse Guard* (art reference only):** small-animal material culture and landscape-as-existential-force, in a modern register — not a source of medieval trappings, guild structures, or setting.
- **Final Fantasy Tactics (presentation reference only):** the scale of the leap between a travel view and a dramatic scene (Section 3.3).
- **Colony builders and town simulators:** attachment to a settlement shaped over time, visually active citizens, emergent personal stories.

MEDIAN borrows *Watership Down*'s register and never its proper nouns. **No real *Watership Down* character name, place name, or invented word appears anywhere in MEDIAN's fiction.** All in-world lore text is original (Section 6).

### 1.2 What the game is not

- A tactical-extraction or combat-first game. It is a base-builder first, with resolution-based conflict.
- An arcade road-crossing game with a base-management wrapper.
- A large-population swarm simulator.
- A combat-first RTS.
- A spreadsheet that hides its world behind menus.
- A technology fantasy in which animals become miniature humans, master electricity, or industrialize the corridor.
- A game about abandoning the town whenever the next biome opens.

---

## 2. Design pillars

**INFOGRAPHIC — The Seven Pillars: What It Is and Isn't**

MEDIAN has seven design pillars.

### 2.1 Attachment-first base-building

The Home Median is the permanent emotional and mechanical center of a campaign. The player improves, densifies, decorates, and remembers this place rather than replacing it. Distant expansion adds a network around the home; it does not negate the home. The base-building layer is where the colony is watched and shaped; the expedition layer is where individuals are tested. The game is a base-builder first and everything else is in service of that.

### 2.2 Named citizens, low population, durable identity

Every core citizen is named, visually distinguishable, and historically tracked. Population growth is slow enough that the loss, injury, bravery, and specialization of one animal matters. The colony is small enough that the player knows every member by name — a deliberately low ceiling shared across all three species. There is no anonymous swarm. Citizens are companions and community members, not replenishable unit tokens.

Naming is a system rather than a label generator: every citizen carries a **Given Name** from inception and may earn an **After-name** in the field (Section 22). The colony's rolling event feed names individuals rather than roles — "Nutmeg and Daisy healed Sharpnose," never "two citizens performed healing" (Section 21).

### 2.3 Ledger and legible

Important state should first be visible in the world: a leaking burrow, a thin food store, a frightened posture, a frayed bridge, an animal moving with a limp. A numerical ledger must also exist for players who require clarity, especially for colony resources, capacity, construction, maintenance, and schedules.

This does **not** mean every number is public. Character aptitudes and unexplored expedition danger retain uncertainty. The ledger clarifies known colony state; it does not eliminate discovery or suspense.

The pillar has a recurring structural expression: wherever MEDIAN attaches a flavor name to something, it shows the functional metadata **alongside** it rather than behind it. Places carry a folk name plus functional tags (Section 22.2); the colony's history carries a Summary view beside a Literary view (Section 21); buildings carry an in-world upgrade name beside a persistent functional icon (Sections 15, 32). Field Mode carries the same logic as toggleable route overlays over an illustration (Section 24). One pattern, four applications.

### 2.4 Expeditions make stories and enable progress

Nearby resources can sustain the colony, but meaningful advancement requires leaving home. Expeditions must be materially worthwhile even if all optional generative imagery is removed. Their systemic rewards include progression scrap, special artifacts, new biome access, outposts, Guest Citizens, intelligence, trade relationships, and story flags.

### 2.5 Consequence without disposability

Failure usually produces fear, wounds, lost cargo, changed relationships, or maiming before death. Consequences persist, but a maimed citizen remains valuable. Experience can turn a physically limited veteran into a calm expedition anchor, teacher, planner, craft specialist, or colony leader.

The encounter model gives this pillar a mechanism rather than only an intention: **exposure** determines what happens to an individual, and it widens the distribution in both directions at once (Section 25.5). The citizen who stuck their neck out is the one who comes home changed — in one direction or the other.

### 2.6 Mechanical restraint, expressive variety

The simulation uses a small number of understandable resources and attributes. Visual skins, history, environment, species, and event combinations create variety. **Do not add a new currency or stat when an existing system can express the same decision.**

This restraint pillar is load-bearing. World events, tharn, traffic-as-weather, the Records, Choice-Event Cards, the Construction Queue, and the entire Approach set are deliberately implemented as reskins, promotions, or extensions of existing mechanics rather than as new subsystems.

The restraint shows most clearly in the negative space. There is no Reputation stat, no Knowledge currency, no Visitors-Helped counter, and no Speed-Up on construction, because existing systems already carry those stories.

### 2.7 One world, four registers

The game presents itself in four distinct visual and attentional registers, and **no fifth register may be added.** Every presentation need must resolve into Colony, Field, Encounter, or Crossing (Section 3). A fifth mode is a design failure rather than a feature.

This is a pillar rather than an art note because the registers do structural work: they enact the Sanctuary/Exposure/Return rhythm, they determine where the art budget concentrates, and they are how the player knows what kind of decision they are being asked to make.

---

## 3. Four registers

**INFOGRAPHIC — The Four Registers**

MEDIAN presents itself four ways, distinguished not by camera height but by **what the player is being asked to do with their attention.**

| Mode | Verb | Register | Attention |
|---|---|---|---|
| **Colony** | **Dwell** | Embodiment | Inhabiting — this is mine, I know every corner |
| **Field** | **Travel** | Legibility | Reading territory — where things are, what my route is |
| **Encounter** | **Meet** | Drama | Present at a moment — this is happening, now, to someone named |
| **Crossing** | **Risk** | Immediacy | Committed — no reading, no planning, only nerve |

**The rhythm of an expedition:**

> **Colony** → *Crossing* → **Field** ⇄ *Encounter* ⇄ **Field** → *Crossing* → **Colony**

An expedition alternates Field and Encounter — read the map, reach a node, drop into a rendered scene, return to the map changed — bookended by Crossings and returning home.

**The transitions are the beats.** Each shift is an emotional event and is authored as one. **No transition is a load screen.**

| Transition | What it should feel like |
|---|---|
| Colony → Crossing | **Commitment.** The world gets loud. There is no more preparing. |
| Crossing → Field | **Survival, then exposure.** You made it — and then the world flattens and you see how much of it there is. |
| Field → Encounter | **Rush-in.** Something is here. Distance collapses. |
| Encounter → Field | **Aftermath.** Back to the map, carrying what just happened. |
| Field → Crossing → Colony | **Return.** The world becomes warm, close, and yours again. |

### 3.1 Colony — dwell

The place the player inhabits, improves, and becomes attached to. The game is a base-builder first, and this is where that is true.

**Presentation:** rendered three-dimensional miniature diorama. Warm, tactile, gently storybook at home while remaining grounded stylized realism (Section 33). Soft organic material against harsh human infrastructure. Work routes, storage, structural problems, fear, injury, weather, and congestion all visually apparent.

**Carries:** the three Colony hotspots — Community Board, Story Circle, and the species hub with its Village Roster (Section 32.1). Always-visible functional icons on every building. The Construction Queue.

**Tempo:** slow. The only register the player can linger in without cost.

### 3.2 Field — travel

Reading and crossing territory: where routes are chosen, nodes discovered, load managed, and the shape of a place learned. Specified in full in Section 24.

**Presentation: the naturalist's survey plate.** Top-down and **illustrated, not schematic and abstract** — a hand-drawn field survey rather than an information display. Warm parchment ground, painterly terrain, visible hand, node markers as pins layered over the illustration, and **the highway always in frame** as textured asphalt bands with vehicles moving on them.

This explicitly **rejects the Dwarf Fortress aesthetic while keeping its virtue**: MEDIAN takes the whole-territory legibility and information density and declines the deliberate stylistic austerity. Atmosphere is not optional in a game whose pitch is atmospheric.

**Tempo:** deliberate. Planning speed.

### 3.3 Encounter — meet

The moments that matter. Every node arrival opens this frame, and it is **the same frame whether the result is a windfall, a negotiation, or an ambush.** Specified in full in Section 25.

**The vibrancy jump.** The delta between Field and Encounter should feel as large as Final Fantasy Tactics' leap from world map to cinematic. Field Mode is more built out than that reference's map; Encounter Mode must earn a proportionally larger jump. This is the presentation's primary production target.

**Presentation:** rendered, close, character-scale, illustrated — the actual participants with their actual portraits, conditions, weather, and location. **This is where the art budget concentrates**, and it is what keeps a surveyed Field layer from making the dangerous half of the game look cheaper than the safe half.

**Tempo:** the game's slowest and most weighted. An encounter is a scene.

### 3.4 Crossing — risk

The signature mechanic and the moment of genuine commitment. **Leaving home happens here — not at a camera change.** Specified in Section 23.

**Presentation:** immediate, low, lane-level. The most compressed and overwhelming view in the game. Audio-forward: traffic density and approach learnable by sound, low-frequency vibration from large vehicles, directional audio at night.

**Tempo:** fast, brief, tense. Accessibility affordances are required rather than optional (Section 32.5).

Crossings use no Approaches, no Turns, and no exposure. They are an action mode, not an encounter.

### 3.5 Constraints binding all four

Canon rules, not art-direction preferences:

1. **Spatial fidelity.** The Colony and Field presentations of the same ground **are the same place.** If a player learns their colony's shape in one and the other does not match it, both break. This binds level authoring.
2. **Traffic is never off-screen.** Every register keeps the highway present — visible, audible, or both.
3. **Each register has a distinct palette and temperature**, legible at a glance and without color dependence.
4. **Four registers, no more** (Pillar 2.7).
5. **No transition is a load screen.**

---

## 4. Three species

**INFOGRAPHIC — The Three Core Species**

**INFOGRAPHIC — The Median Read Three Ways**

Each campaign selects one core species. The three campaigns share the same economy, world logic, progression skeleton, expedition categories, and citizen model. Asymmetry comes from spatial architecture, stat bias, and one defining home-system problem — not from three unrelated games.

**Each campaign is one species, for its whole length.** A rabbit colony is rabbits; a mouse colony is mice. The choice made at founding holds to the end, and the found-family beat lives entirely in the Guest system (Section 20).

Species colours everything downstream: the hub name, every structure family's vocabulary, the Given Name banks, the colony-naming imagery, the spatial signature system, and the way a party behaves in the field.

### 4.1 The shared stat frame

All three species run on the same handful of shared stats, differing only by bias. The economically-relevant dials are **Speed** (exposure time per crossing — higher speed means a shorter vulnerable window), **Carry Capacity** (value moved per trip), and **Food Consumption** (upkeep per individual).

**All values are integers.** MEDIAN is integer-based throughout — one day, one carry slot, one expedition — and the stat frame is scaled so that no species carries a fractional value.

| Species | Speed | Carry | Food Consumption | Emphasis |
|---|---|---|---|---|
| **Rabbit** | Fastest | 10 | 10 | Precision — one clean high-stakes crossing |
| **Squirrel** | Standard | 20 | 10 | Logistics — best cargo per trip and per food |
| **Wood Mouse** | Standard | 6 | 5 | Density — many small bodies, efficient per food |

A mouse colony gets more done per unit of food than a rabbit colony and runs larger (Section 11), but every mouse is still a named individual and every mouse crossing is a single committed action, not a swarm.

**Three dials, and no more.** A species' expendability needs no stat of its own: it already falls out of the ratio between what a citizen carries and what a citizen eats.

### 4.2 Rabbit — burrow civilization

**Personality:** grounded, communal, fast, cautious, architectural.
**Spatial identity:** an underground warren connected to surface forage and multiple bolt holes.
**Bias:** strong sprinting and teamwork, larger bodies and appetites, modest carrying efficiency.

Rabbit construction is a depth-and-flow puzzle. Chambers, tunnels, food stores, nurseries, and exits must fit beneath limited terrain. Surface access points create efficiency but also exposure. Poor circulation produces bottlenecks during a predator alarm or Road Work emergency.

**Signature system — Warren Flow.** The player manages routes, chamber congestion, structural support, and escape coverage. The goal is not to chase a hidden "bolt-hole score," but to create a visibly functioning network with enough exits and alternate paths.

**The system's readable signature is multiplicity.** A rabbit colony is legible at a glance by how many ways out it has: half a dozen or more bolt holes scattered irregularly across the ground above a mature warren, and at least one further exit far enough off to be a genuine alternative rather than a second front door. A mouse burrow may show a single mouth; a warren never should. Because the Colony and Field presentations of the same ground are the same place (Section 3.5), that distant exit appears in the **Field layer** as well — the shape of a warren is partly visible from outside it, and reading a strip means noticing where its exits come up.

*Flagged for further design:* Warren Flow's **readable signature is now settled** — multiplicity of exits, above — but the system remains the least specified of the three. What the player actually manipulates, what failure looks like, and how congestion reads in the Colony register still need a dedicated pass (Appendix D).

**Strengths:** fast open-ground movement, powerful coordinated hauling, efficient excavation, strong rescue capability.
**Pressures:** high food demand, tunnel moisture and collapse risk, limited vertical access, crowding at entrances.

### 4.3 Squirrel — canopy civilization

**ARTWORK — The Squirrel Cache Network**

**Personality:** mobile, opportunistic, dispersed, daring, logistical.
**Spatial identity:** nests, bridges, branches, trunks, guardrails, and scattered caches.
**Bias:** strong carrying and climbing, flexible routes, greater exposure when forced to ground.

Squirrel construction turns the Home Median into a layered vertical network. Rather than one perfect central warehouse, supplies are distributed among visible caches. Location, redundancy, retrieval time, weather protection, and theft risk matter.

**Signature system — Cache Network.** The player balances convenience against resilience. Centralizing goods is efficient but vulnerable; dispersal protects the colony but consumes labor and travel time. Losing one cache to a raid never wipes the whole stockpile, at the cost of constant spatial management.

*Flagged for further design:* whether the Cache Network extends across outposts — turning the corridor itself into a distributed store — is open, with real consequences for Section 28 (Appendix D).

**Strengths:** vertical mobility, heavy-item hauling, rapid response across connected canopy, route redundancy.
**Pressures:** exposed infrastructure, tree loss, weather damage, cache spoilage or theft, dependence on Anchor Points.

### 4.4 Wood Mouse — dense, distributed civilization

**ARTWORK — The Wood Mouse Relay**

**Personality:** ingenious, quiet, compact, cooperative, adaptable.
**Spatial identity:** tiny rooms, root passages, culverts, grass tunnels, densely interlocked micro-infrastructure.
**Bias:** low consumption and footprint, high acceleration and stealth, low individual carrying capacity and physical resilience.

Mice permit the densest settlement, but they remain named individuals — not an anonymous swarm. Their spatial challenge is coordinating many small jobs and narrow routes without losing readability or turning the game into queue management.

**Signature system — Relay Network.** Mice divide loads and tasks across short, visible handoffs. The player designs stations, micro-paths, and work neighborhoods so that small carrying capacities become an efficient collective chain.

- **Safety in Numbers.** A mouse expedition is a *single commit-and-execute crossing* — the same player interaction as any other, with no split attention across simultaneous crossings. Its outcome resolves as a **partial-outcome distribution**: most of the group makes it, and occasionally one doesn't, rather than a binary pass/fail. This falls out of the exposure model without a special-case rule — a mouse party spreads exposure more thinly across more bodies, so each individual's exposure runs lower while the number exposed runs higher (Section 25.5).
- **Expedition Access Identity.** Mice reach certain resource nodes and pockets *within* a Margin that no other species can reach — but only after taking the same crossing risk everyone takes. This is never an alternate route *across* the highway, and does not extend to the Home Median. It is a reward for having crossed, not a way to avoid crossing.

**Strengths:** efficient use of food and space, stealth, access to small voids, rapid light-material construction, unique Margin pockets.
**Pressures:** low load capacity, vulnerability to wind shear and direct trauma, narrow-route congestion, individual fragility.

### 4.5 Seasonal and environmental personalization

Small, flavorful seasonal or environmental quirks personalize species and Guests. The first concrete instance: the **Snake Guest takes a movement penalty in Winter**, replacing older, vaguer "seasonal dormancy" language with a specific mechanical effect. This is a template and an open design avenue — the team should look for similar small quirks for the core species — but no further instances are locked.

The Guest roster's own situational trade-offs are handled systematically rather than as one-off quirks; see the option-opener template in Section 20.1.

---

## 5. Two loops

**INFOGRAPHIC — The Two Loops**

MEDIAN runs on two loops. One is the reason the game exists; the other is the reason the first one can grow.

### 5.1 The domestic loop

1. Observe citizens, structures, stores, weather, and local ecology.
2. Assign standing **Roles** (Section 12) and standing **Tool** assignments (Section 19). Both persist until changed rather than being clicked per task.
3. Improve the Home Median's layout and resilience.
4. Read approaching needs: seasonal pressure, Road Work risk, scarce scrap, a promising expedition, a pending Choice-Event Card, a citizen opportunity.
5. Decide whether to commit eligible citizens to an expedition that day.
6. Absorb the expedition's gains and consequences into the physical town.

The player may spend substantial time arranging and watching the colony, but game time is structured. Pausing is available for accessibility and strategy; pausing does not advance production.

### 5.2 The bridge between them

**Safe local ecology supplies subsistence → structures and ambitions demand salvage → expeditions secure scrap, artifacts, knowledge, and connections → the colony becomes safer and more capable → greater range exposes richer but more contested opportunities.**

This is not a third loop. It is the pressure that forces the first loop into the second: **the colony can always survive at home and can never advance there.**

Local subsistence is not abstract. Because the Home Median is itself a Median Reach with its own Field layer (Section 24.4), everyday foraging is a **low-stakes Field run on home ground** — which means the first real expedition reads as *the same activity, across the road*.

### 5.3 The expedition loop

1. **Choose a purpose:** Margin Raid, Median Scout, Establish Outpost, Outpost Visit, or a Special Journey.
2. **Choose citizens:** one expedition per citizen per day. Selection depends on known traits, experience, wounds, relationships, species capabilities, Guest abilities, and player intuition.
3. **Prepare:** allocate carrying equipment and assign each departing citizen a **Supply** — a single per-run pick each, so preparation never becomes a loadout spreadsheet (Section 19).
4. **Depart:** for a transverse mission, enter the outbound Crossing sequence. Longitudinal travel uses corridor hazards and abstracted travel beats (Section 7.3).
5. **Enter Field Mode:** the party moves through surveyed territory dotted with discoverable nodes. Contest status and encounter type are revealed only on reaching a node, never at launch.
6. **Resolve each node as an Encounter:** choose an Approach, act on any Turns the contest earns, take the outcome (Section 25).
7. **Return:** the player chooses when to head home, feeding into Return Logic (Section 23.2).
8. **Record the story:** the expedition closes on a **Rating** and a **Report and Share** debrief, writing entries into the Colony Record and the Character Records of everyone who went (Section 21.3). This is the game's principal event-generator.

---

## 6. One folklore

MEDIAN's animals have a single oral culture, and it does real work: it teaches systems, it names the world, and it gives the Records their voice. All of it is **original in-world text.**

It is one body of material with two registers inside it — the **Laws**, which teach, and the **Sayings**, which set tone — plus a shared vocabulary for the human world. The *naming systems* that grow out of this culture are mechanics rather than voice and live in Section 22.

**A general canon note: animals in MEDIAN can read.** This is a suspension of disbelief the design requires and accepts openly. MEDIAN is not pursuing rigid ecological verisimilitude, and no in-world text needs a "read by the player, not the citizens" caveat.

### 6.1 The Laws of the Median

**INFOGRAPHIC — The Laws and Sayings of the Median**

The **Laws** are the functional half. Each teaches a real system, which makes folklore the game's tutorialization layer: the player learns to survive by learning what the animals already say.

| Law | Text | Teaches |
|---|---|---|
| **The First Law — of the Roaring Iron** | *"Wait for the gap. The gap is given, not owed."* | The Crossing: gaps are readable, and never promised. |
| **The Second Law — of the Mowing** | *"The mowing is fire. Fire passes; the burned ground feeds."* | Road Work: it wipes the Margin, and the Margin comes back. |
| **The Third Law — of Water** | *"Drink where the water moves. Standing water remembers what fell in it."* | Sustenance and hydration, and the Pond Hollow's disease risk. |
| **The Fourth Law — of the Share** | *"A hoard in one belly is a store the winter never sees."* | The economy: pooled stores, no private accumulation. |
| **The Fifth Law — of the Sky** | *"Hawks own the day, owls own the night. Neither owns the hedge."* | Predators by time of day, and the value of cover. |

*(Law text is authored canon and open to revision on tone; the teaching assignments are settled.)*

**Four exposure surfaces:**

1. **The Founding Escape opening (primary).** The campaign opens inside a mature ancestral home with a Teacher drilling the young in the Laws, call-and-response, heard as the camera moves through the halls — and then the machines come, and *"the mowing is fire"* stops being a recitation (Section 35.1).
2. **Just-in-time contextual surfacing.** The first Road Work surfaces *"the mowing is fire."* The first night owl surfaces *"owls own the night."* Folklore is the tutorial prompt; there is no separate tutorial voice.
3. **Ongoing colony culture.** The Teacher passes the Laws to the young (Sections 12, 17). The **Story Circle** is their venue (Section 15.3). They are inscribed in the world, appear on the Community Board, and serve as loading-screen aphorisms.
4. **Worldbuilding variants.** The Rest-Stop Metropolis holds **competing and contradictory Laws** (Section 29) — a bigger, older, more cosmopolitan settlement remembers the world differently, and the player's colony discovers that its truths are local.

**The colony's own Laws are imperfect.** The founding trio are adolescents who were *not* the students being drilled, and no adult survives the Founding Escape (Section 35.1). What the colony carries forward is what three teenagers half-remembered. This is why the Metropolis's contradictions have teeth, and why the first assignment of the Teacher Role is a real event rather than a menu click.

### 6.2 The Sayings of the Median

The **Sayings** are the tonal half, kept deliberately separate so the two registers do not blur. **Laws teach a system. Sayings have no teaching job attached.** They share the same exposure surfaces: loading screens, Teacher and elder dialogue, Story Circle recitation, Community Board inscriptions, banners at civic occasions.

The Sayings are near one-to-one restatements of the design pillars, spoken from inside the fiction:

- *"Stories over statistics."*
- *"Small is grand."*
- *"Observe. Plan. Adapt. Teach the young. The Median remembers."*
- *"Every life has a name."*
- *"The world is beautiful and dangerous."*
- *"Build. Gather. Survive."*
- *"Unity. Work. Harmony."*

Sayings are **anonymous collective wisdom** or attributed to invented in-world figures. They are never attributed to real *Watership Down* characters.

**The pool grows.** The colony's founding produces its first original Saying at the moment the player chooses to stop running and stay (Section 35.1) — the first thing the Records ever record.

### 6.3 The Giants — vocabulary for the human world

**INFOGRAPHIC — The Giants: Vocabulary for the Human World**

The animals have their own words for the human world, and those words distinguish rather than lump. An animal is far too observant to confuse a rider with the thing it rides in.

- **The Giants** — humans, specifically. The word carries scale and otherness, not malice.
- **Roaring Iron** — vehicles, specifically. Named for force and momentum rather than shape.
- **The Rivers of Thunder** / **the Roaring Rivers** — the highway itself. Deliberately a **regional-variant pair rather than one fixed term.** Different colonies and dialects use different names, and both are canon simultaneously — the "many words for snow" principle applied to the one thing every animal in this world has an opinion about. The pool can grow later without a canon change.
- **The Mowing** — an ordinary, survivable instance of Road Work (Section 10.2).

Two further terms name the campaign's founding catastrophe and the home it took:

- **The Founding Escape** — the event itself. The designer's plain term is also the in-world one, which suits a folk register deliberately tuned homely and plain rather than ornate (Section 22.2). It is categorically *not* an instance of the Mowing: the Mowing is cyclical, evadable and survivable, while the Founding Escape is a singular permanent apocalypse (Section 35.1).
- **The Ancestral Warren / Den / Burrow** — the home that was lost, named with the campaign species' own hub term. This is a correct rather than generic use of that vocabulary (Section 15.1): a rabbit campaign mourns an Ancestral Warren, a squirrel campaign an Ancestral Den, a mouse campaign an Ancestral Burrow. The species terminology rule bars only *generic* use, and there is nothing generic about the place a colony came from.

---

# PART II — THE WORLD

**ARTWORK — The Corridor at Golden Hour**

*The ground the game happens on, and the forces acting on it.*

---

## 7. World geography and terminology

### 7.1 The cross-section

**INFOGRAPHIC — The Cross-Section**

The world has a repeating structural geometry. From one outer boundary to the other, a typical playable cross-section is:

**Sound Wall → Margin → Highway → Home Median → Highway → Margin → Sound Wall**

The arrangement is symmetrical in principle, though terrain, lane count, elevation, vegetation, and accessibility may differ on each side. This is the one place in the document where *geometry* is the precise word: the cross-section is a designed structure that repeats, not a landscape.

The **Sound Wall** is a real, recognizable piece of highway infrastructure — a tall, often vine-covered concrete barrier — and it forms the permanent, impassable outer boundary of the playable world. This grounds the map's edge in something the player recognizes rather than an invented lore device; animals simply cannot scale it, and the world beyond is never modeled. The sound wall's *height* is pure flavor, never a mechanical figure.

### 7.2 Home Median

The **Home Median** is the central strip between opposing carriageways and the site of the player's colony. It can be narrow or broad, grassy or wooded, dry or culverted. It is relatively safe from traffic while still subject to predators, weather, runoff, vibration, disease, and Road Work.

The colony is built **in and on the Median**, not under the active highway and not in the Margin.

**The Home Median and the colony are two things with two names.** The Median is a Median Reach like any other and receives a **generated folk name** from the world (Section 22.2). The **colony** built on it receives the one name the player authors (Section 22.3). A colony called Horizon Fields may well stand on a reach the corridor has always called The Long Verge.

Because the Home Median is a full Reach, it has a **Field layer** of its own — biome, Anchor Points, node-bearing ground — and is not only ever seen as a diorama (Section 24.4).

### 7.3 Highway

The **Highway** is the active multi-lane barrier between the Home Median and either Margin. It is both boundary and playable hazard.

Highway danger is governed by **lane count**, from two up to four or five. Lane count is independent of the median biome beside it — a wide, lush median can sit against a narrow two-lane crossing, and a thin grass ribbon against a five-lane gauntlet. This decouples "how rich is this place" from "how dangerous is it to reach."

**Two manifestations.** The highway is encountered in two structurally different ways, and they should look and feel distinct:

- **Transverse crossing — Home Median to Margin.** Cutting *across* the lanes. The standard Crossing sequence (Section 23): stage at protected micro-cover, read the traffic, commit. Short, lateral, and the game's signature moment of nerve.
- **Longitudinal travel — Reach to Reach.** Moving *along* the corridor to another Median Reach. Distance rather than width; abstracted travel beats and corridor hazards rather than a single lane-by-lane gauntlet.

*Flagged for further design:* exactly how the two differ in presentation and mechanics is open (Appendix D). What is settled is that they are not the same experience wearing two labels.

In the animals' own vocabulary the highway is a river: the **Rivers of Thunder** or the **Roaring Rivers**, depending on which colony is speaking. The vehicles on it are **Roaring Iron**, and the humans inside are **the Giants** (Section 6.3).

### 7.4 Margin

The **Margin** is the resource-rich, ecologically chaotic strip between a highway and its outer sound wall. Fast pioneer plants, windblown seeds, insects, roadkill traces, litter, packaging, tire fragments, and other human detritus accumulate there.

The Margin's richness is not incidental — it is the **Edge Effect** (Section 9.3) made concrete. Two zones overlap here, human and wild, and the overlap produces both the abundance and the danger. The Margin is the richest ground in the world and the most exposed, and it is both at the same place: hard against the road.

The Margin is renewable rather than permanently exhaustible. Nodes deplete locally, then replenish through plant growth and new waste deposition. Road Work can wipe the strip nearly bare for a time, resetting cover and yield before succession begins again.

The Margin is **never buildable under any circumstance.** It can be raided and traversed, but nothing the player builds ever persists there. This is a permanent property of the world, not a tier gate.

### 7.5 The median chain and the Median Reach

**INFOGRAPHIC — The Corridor Chain**

The Home Median is one segment in a longitudinal chain of medians extending up and down the corridor. Each remote segment is a **Median Reach**. Reaches differ in width, hydrology, vegetation, infrastructure, exposure, predators, lane count, and resource character.

A Reach has three lifecycle states, described in full in Section 28: **undiscovered**, **discovered-but-expedition-only**, and **outposted**.

**Every Reach carries a folk name**, generated from its actual character (Section 22.2) and paired with functional metadata tags rather than a second literal name.

**Each Reach is unified, and adjacent Reaches may differ sharply.** A Reach is internally coherent — one place with one character — and carries no sub-divisions. Its internal variation comes from Anchor Points (Section 8.2), which guarantee a mix rather than a monoculture.

Correspondingly, two neighboring Reaches **may differ more sharply than real-world geography would produce** — a wooded median can sit directly upstream of a concrete trench. This is a deliberate legibility-driven convention, stated explicitly so future Reach content is not "corrected" as though a jarring biome transition were an error. Variety comes from travelling between whole Reaches, never from subdividing one.

### 7.6 What else is out there

The corridor is not only medians and margins. Two things exist beyond the chain and are named here so the player has a map before they have an explanation:

- **The Rest-Stop Metropolis.** Far down the corridor, a large, old, genuinely multi-species animal settlement hidden in the neglected margins of a human rest stop — drainage spaces, service voids, dumpster enclosures, embankments, vents. It is the only city in this world, the primary destination of the Special Journey expedition, and the endpoint of the campaign's victory arc. **Part VI** is devoted to it.
- **The ancestral home.** Wherever the campaign's chosen species came from before the Founding Escape destroyed it — now a permanent hazardous construction zone, revisitable as a ruin (Sections 27.1, 35.1).

---

## 8. Median biomes and Anchor Points

### 8.1 The eight biomes

**INFOGRAPHIC — Biome Codex: The Eight Biomes**

**ARTWORK — The Eight Biomes, as establishing shots**

Eight biomes are canon. There is no separate scrub/briar biome; that flavor folds into the Wooded Median. Biomes differ on **visuals, resource mix, and natural cover** — *not* on highway danger, which is governed entirely by lane count. Each biome is a whole-Reach property under the unified-Reach rule.

- **Thin Grass Ribbon:** little building room, excellent sightlines, high wind exposure. Resource-poor.
- **Wooded Median:** trees enable squirrel infrastructure and shade, but conceal predators. Strong Durable sustenance; canopy and root Anchor Points.
- **Culvert Garden:** reliable water and rich soil with flood risk. Strong Perishable sustenance; high Flexible Scrap.
- **Creek Split:** abundant ecology divided by moving water. Strong Perishable sustenance; scattered Rigid Scrap.
- **Pond Hollow:** food-rich wetland with disease, amphibian, and snake encounters. Very strong Perishable sustenance; mixed scrap.
- **Concrete Trench:** scarce vegetation, strong shelter opportunities, extreme heat and runoff. Poor Sustenance; rich Rigid Scrap.
- **Overpass Shadow:** complex vertical structure, darkness, noise, protected dead spaces. Poor Sustenance; rich mixed scrap.
- **Interchange Expanse:** broad territory, many routes, severe navigational and predator exposure. Richest resource variety and the highest danger.

Every biome is subject to the Edge-Effect gradient at its own margins: whatever a Reach offers, it offers most, and most dangerously, nearest the road.

### 8.2 Anchor Points

**INFOGRAPHIC — Anchor Points**

Each Reach generates a small, fixed set of named terrain features called **Anchor Points**, each suited to particular species or building types — a canopy tree for squirrel infrastructure, a deep root system for a rabbit warren, a culvert mouth for mouse micro-tunnels.

Anchor Points are a **bonus layer, never a gate** — a Reach is always usable without perfectly matching its Anchors — and every Reach generates a *mix*, never a monoculture. This internal mix is the whole of a Reach's internal variation.

Anchors are named through the same folk grammar as their Reach, and their names feed the Reach's own: a Reach with twin oaks at its heart is liable to be called for them. They are the most common thing a generated place name derives from, and they are what the Field register labels as a territory's named ground (Section 24.2).

The one guaranteed exception is the first Home Median Reach, established immediately after the Founding Escape: it is guaranteed to suit the player's chosen species, so no campaign opens on hostile ground. Every later Reach follows the mixed-generation rule.

Anchor Points also modulate Road Work severity (Section 10.2).

---

## 9. The day, traffic, and traffic as weather

### 9.1 Daily structure

**INFOGRAPHIC — The Game Day**

A game day is a bounded operational cycle, not infinite tinkering. Exact clock length remains a prototype variable, but the intended rhythm is **one meaningful expedition opportunity per citizen per day.** Launching an expedition commits its participants for that day; no citizen may complete a second before the next dawn.

Suggested daily beats:

- **Morning Rush / Domestic Opening:** consumption and recovery resolve; the player reviews the colony, repairs, builds, and makes assignments while traffic is dense and stressful.
- **Midday Operating Window:** the clearest default expedition window, balanced by daylight predators and faster vehicles.
- **Evening Rush / Domestic Return:** noise, fumes, and erratic traffic discourage normal departures; returning consequences and home tasks take focus.
- **Night Velocity:** optional specialized departures may exist, but are rarer and meaningfully different rather than a routine second expedition. Low traffic density is offset by extreme vehicle speed, reduced visibility, owls, and fear.
- **Dawn Reckoning:** food consumption, healing progress, structural wear, regrowth, Construction Queue progress, scheduled events, and calendar advancement resolve.

Time of day is an in-game system, not tied to the player's real-world clock.

### 9.2 Traffic cycles

- **Rush:** dense, slower vehicles; fewer clean gaps, strong fumes, vibration, noise, stop-start unpredictability. Sets the River's Spume to **Exhaust**, and reinforces **Heat** in summer through idling engines.
- **Lull:** moderate density and speed; visually readable but exposed to raptors.
- **Night Velocity:** few vehicles at very high speed; headlights, darkness, spatial audio, and tharn risk dominate. Reinforces the Spume's **Cold** manifestation in winter.
- **Anomaly:** an accident, lane closure, weather event, convoy, maintenance crew, or unusual lull temporarily rewrites the pattern. This wildcard produces the rare **Oil Leak** Spume.

### 9.3 Traffic behaves like weather

**INFOGRAPHIC — Traffic as Weather**

Traffic is a dynamic environmental system rather than a row of predictable moving platforms. Density, speed, vehicle class, wind shear, headlights, spray, thrown debris, pollution, accidents, and Road Work produce changing conditions that can be read but never made perfectly safe. Traffic-as-weather effects are present across all Margin nodes, **with intensity scaling by proximity to the highway edge.**

**The Edge Effect — richness and danger share a gradient.** The strip nearest the highway is simultaneously the most resource-rich ground in the world and the most hazardous, and both qualities fall off together toward the interior. This is the world's organizing ecological principle: **the player is never choosing between a rich place and a safe place, because they are the same place read from two directions.** Toward the Median-facing side lies the **Quiet Zone** — calmer, thinner, safer, poorer. Traffic-as-weather's proximity scaling is the mechanical face of this gradient; the gradient is its ecological reason.

**Manifestations.** Three named hazards, all reskins of existing systems:

- **Wind Draft** — gusts thrown off passing vehicles, strongest at the road edge and scaling down by proximity.
- **The River's Spume** — the standing ambient hazard. Unlike a rolled encounter, the Spume is a **constant presence near the highway**; what changes is its texture, set by the current traffic cycle and season rather than randomized per visit. Four manifestations, each keyed to a state that already existed in canon but went unnamed:
  - **Heat** — Summer, reinforced near Rush-hour engine idle. *"The River's Spume is hot today, battering you with hot wind."*
  - **Cold** — Winter, reinforced by Night Velocity's darkness and exposure.
  - **Exhaust** — the Rush cycle. Hard to breathe.
  - **Oil Leak** — the rare one, keyed to the Anomaly cycle. Smells foul.
- **Litter** — the discrete counterpart to the Spume's constancy: human detritus arrives occasionally rather than persisting, as a **Choice-Event Card** in Field Mode (Section 10.3). Salvage it for potential item value, or let it pass — it is travelling at highway speed and can injure a citizen who engages it carelessly. Risk and reward are the same object.

Wind Draft and the River's Spume both feed the existing **weather modifier** in encounter resolution (Section 25.4). No new mechanic; a slot that already existed is now populated.

Chemical runoff and invasive growth are present in the Oil Leak's character and in the Margin's general texture, without being hazards of their own.

---

## 10. Seasons, Road Work, and Choice-Event Cards

### 10.1 Seasons

**INFOGRAPHIC — The Turn of the Seasons**

**ARTWORK — The Four Seasons at Home**

Season length and campaign duration require playtesting. Seasons should be long enough to establish a distinct operating rhythm, not flip every few sessions. Seasons drive the Perishable/Durable sustenance split (Section 13) and set the ambient texture of the River's Spume.

- **Spring — Thaw and Growth:** rain, flooding, rapid Margin regrowth, abundant greens, and the first **Nesting Season** of the year.
- **Summer — Pavement Heat:** dehydration pressure, heat plumes, exposed-day penalties, marginally higher chance of Road Work. Sets the Spume to **Heat**.
- **Autumn — Detritus Harvest:** strong winds deliver scrap and seeds; stockpiling, and a possible second **Nesting Season**.
- **Winter — Freeze and Reserve:** low local forage, expensive warmth, draft and exposure risk, reliance on preparation. Sets the Spume to **Cold**. Snake Guests take a movement penalty.

**Nesting Season** is the breeding window. It is the only time a **Hearth** can bring a new named citizen into the world, and it remains rare, expensive, and player-authorized (Section 17.3).

### 10.2 Road Work

**INFOGRAPHIC — Road Work**

**ARTWORK — Road Work: Telegraph, Onset, Persistence**

**Road Work** is a family of municipal disturbance events — mowing, vegetation clearing, salt application, drainage work, barrier repair, resurfacing, construction staging, trash collection, lane reconfiguration. It functions like severe weather at the campaign scale and is one of the game's signature systems.

In the animals' own vocabulary, an ordinary survivable instance is **the Mowing**, and the Second Law — *"the mowing is fire"* — is how the colony teaches its young to survive one.

**Cadence and telegraph.** Road Work is decoupled from the season calendar — not a scheduled seasonal event — though summer carries a marginally higher chance. It is telegraphed *only* through subtle visual changes in the Margin (survey marks, disturbed ground, distant machinery, changed smell and vibration), **never through a numeric warning or countdown.** It must create adaptation, not arbitrary punishment.

**Severity.** When Road Work strikes, the **Margin is fully wiped.** Severity *within the Median* scales with the Reach's Anchor Points and cover — a well-covered, root-anchored Reach weathers it better than an exposed one.

**Three phases:**

1. **Telegraph.** Subtle Margin visual changes, no numeric warning.
2. **Onset.** A group-layer resolution (Section 25.4) for any citizens caught present — a single round, no Approach, no Turn. Citizens are exposed by circumstance rather than by choice.
3. **Persistence.** A bounded-duration altered-state window: a different soundscape, restricted and riskier expeditions, and construction machinery present as a distinct **environmental-hazard antagonist type** — something to evade or shelter from, never negotiated with or fought. The window's duration is **capped regardless of severity**; severity manifests as *intensity*, not length. The player can shorten it through active recovery work reusing the ordinary repair system.

**Road Work reshapes the event pool.** While the persistence window runs, Road Work acts as a **card-pool modifier** on Choice-Event Cards: it tilts the pool toward hazard and disruption cards and raises event frequency. This is how Road Work is made "loud" — through an existing system rather than a new one.

**Thematic tie.** Road Work's recurring construction-equipment threat explicitly echoes the Founding Escape: the same class of machinery that destroyed the ancestral home returns to threaten the new one. The two are an **echo, not the same event** — the Founding Escape is a singular permanent apocalypse, while Road Work is cyclical and survivable (Section 35.1).

### 10.3 Choice-Event Cards

**INFOGRAPHIC — Choice-Event Cards**

**Choice-Event Cards** are the game's unified event layer — **one system with two homes** rather than two event systems. A card presents a situation and a small set of costed responses — *Reinforce the Drainage* (−wood), *Move the Supplies* (−time), *Do Nothing* — and resolves into consequence. This is the player-agency event layer above and beyond Road Work.

**Colony mode.** Weather, seasonal, social, and opportunity events arrive at the Home Median and at outposts. These carry the real costed decisions, and they are the primary reason the domestic layer has surprises in it at all. A **wandering core-species joiner** arrives this way (Section 17.4).

**Field mode.** Occasional **random-encounter cards** appear during traversal — a light interstitial layer *between* structured node encounters, never a replacement for them. Kept deliberately occasional so node design is not diluted into a card shuffle. **Litter** is the flagship Field card (Section 9.3).

**Rules governing the whole system:**

- **No numeric countdowns anywhere.** The non-numeric telegraph rule governs the entire event system, not Road Work alone. Every telegraph is qualitative and diegetic — a smell, a sound, a changed sky, a Guest's unease. Nothing anywhere in MEDIAN tells the player "3 days until X."
- **Road Work modifies the pool** rather than spawning a parallel event track.
- **The Groundhog Ambient Guest** is the in-fiction warning system for approaching cards (Section 20.2).
- **Outcomes feed the Records** as dated, named entries.
- **Restraint.** These are events, not nags. Frequency must stay low enough that a card is an occasion.

---

# PART III — THE COLONY

**ARTWORK — The Rabbit Warren**

*The home the whole game is in service of: how it works, and what it builds.*

---

## 11. Scale and the shape of a colony

**INFOGRAPHIC — The Colony**

This is a deliberately low-population colony game. A mature colony should still be small enough that the player recognizes every member by name (Pillar 2.2). Exact caps differ by species and tier, but population growth never becomes a continuous unit-production conveyor.

A mature wood-mouse colony runs larger than a comparable rabbit or squirrel colony — on the order of one-and-a-half to two times the head-count — but stays within the same low, fully-named ceiling. **The difference is density, not anonymity.**

Two things grow a colony, and both live with the citizens rather than here: **wandering joiners** and **Nesting Season births** (Section 17.4). Stationing citizens at outposts moves them out of the home but never off the ceiling (Section 28.3).

## 12. Roles and daily work

**INFOGRAPHIC — The Eight Roles**

Citizens not on expedition are assigned a standing **Role** rather than being micromanaged task by task. A Role persists until the player changes it, and the game handles pathing and execution automatically. This is a batch-orders-and-priorities model, not click-per-task command.

Eight Roles, each distinct, non-overlapping, and with **fixed, static output** — no leveling:

- **Forager:** increases Sustenance yield; benefits from matching Anchor Points.
- **Caretaker:** reduces Perishable spoilage.
- **Builder:** reduces construction cost and time, slows structural decay, benefits from matching Anchor Points.
- **Healer:** speeds Wounded recovery.
- **Nursery Tender:** improves breeding-cycle conditions.
- **Watchkeeper:** improves Base Defense telegraph warning.
- **Crafter:** converts Scrap into finished goods and produces adaptive equipment for maimed veterans.
- **Teacher:** reduces colony-wide fear and stress, and speeds a young citizen's first-expedition readiness.

**A Role's effect is identical no matter who holds it.** Assignments always produce visible action in the colony; the player watches the work happen rather than reading it off a menu.

*(Open working detail: whether a newly-born or newly-unassigned citizen defaults to Forager is not yet locked.)*

**The base-building layer never grows anyone.** A hard rule governs the relationship between domestic work and citizen development: the base-building layer is **personality-blind and never accesses individual growth.** All citizen development, without exception, happens through **expedition participation** (Section 25.5). This resolves the tension between static, legible Roles and the desire for citizens to feel like continuing, invested-in presences: the investment is real, but it is earned in the field, not at a workbench.

**The Teacher's cultural work.** The Teacher is the colony's transmission mechanism for its own folklore — drilling the young in the Laws and repeating the Sayings, at the **Story Circle** (Section 15.3). This is the in-fiction reason the Role reduces colony-wide fear and speeds first-expedition readiness: the Laws are survival instruction in mnemonic form.

**Standing Tool assignment reuses this interface.** Assigning a citizen a **Tool** (Section 19) works exactly like assigning a Role: a persistent, colony-level decision made in the Colony register, changed when the player wants it changed, and never made at the Expedition Launcher.

## 13. Resources and the economy

**INFOGRAPHIC — The Economy**

**ARTWORK — A Colony Built Into a Wreck**

The lean canonical economy has three regular categories plus a special class, and **no standalone currency layer**:

1. **Sustenance** — food and hydration consumed by citizens, used for reserves, recovery, and rare reproduction. Forked into two sub-types:
   - **Perishable:** decays over time; abundant in spring and summer. *Berries, greens, insects, mushrooms, fallen fruit, fresh food scraps.*
   - **Durable:** stockpilable; the backbone of autumn and winter preparation. *Acorns and nuts, dried seeds, dried grass, preserved food scraps, dried mushrooms.*
2. **Flexible Scrap** — binding, weaving, lashing, sealing. *Copper wire, twine and packaging string, burlap and fabric strips, zip-tie fragments, plastic bag strips, rubber bands, shoelace lengths, fishing line.*
3. **Rigid Scrap** — bracing, shielding, surfacing, tools, load-bearing reinforcement. *Aluminum pull-tabs, bottle caps, smoothed glass pebbles, bread clips, popsicle sticks and wood splinters, tire-rubber fragments, small metal hardware, broken ceramic shards, gravel chips.*

**Special Artifacts** are rare, tightly-limited objects that unlock a blueprint, solve a specific problem, enable a trade, improve an adaptive device, or open a narrative option. They are not generic "technology keys," and their uses must remain believable for animals. They operate at the **colony** level, distinct from the three citizen equipment slots (Section 19).

One canonical Artifact effect worth naming: an Artifact may **grant an extra Turn in an encounter** (Section 25.7) — a non-numeric, situation-solving effect of exactly the kind this class exists for.

The flagship crafted **Tool** comes straight out of the Rigid Scrap list: the **pull-tab-and-needle multitool**, assembled from an aluminum pull-tab and a scavenged needle. It is lent, returnable colony property rather than personal possession.

**Item weight and value.** The default rate is **one carry-slot equals one unit of value.** Large items scale proportionally, and true "windfall" finds are the rare exception where value exceeds the proportional rate. Item weight shares units with citizen carry capacity, so some large items require cooperative carrying. *(Exact thresholds deferred; Appendix D.)*

## 14. Construction, decay, and the Construction Queue

**INFOGRAPHIC — Construction and the Queue**

Structures visibly age through moisture, rot, wind, vibration, salt, heat, and use. Maintenance creates ongoing work, but fully-upgraded construction can reduce or eliminate routine decay in a limited footprint. The objective is meaningful stewardship, not a universal repair tax.

No single decay formula is canonical. Prototype using broad durability states and event-based wear before considering fine percentages. The same repair-and-maintenance system is reused as the player's counterplay against Road Work's persistence window.

**The Construction Queue** is the single shared model for every building project. New construction, per-building upgrades (Section 15.2), and an outpost's securing clock (Section 27.1) are all **instances of the same system** rather than three bespoke timers.

- **Duration is measured in whole days,** fixed per building and per rung, generally escalating at higher tiers. *(Exact day-values deferred; Appendix D.)*
- **Resources are spent at the start, and are sunk.** No refund, no partial recovery, no mid-build loss risk.
- **Projects are uninterruptible.** Nothing derails a started project — not Road Work, not a Choice-Event Card, not a world event. This is deliberate: **certainty lives in construction, and risk stays where it already lives, in expeditions.** The colony layer is where the player is allowed to make a plan that holds.
- **A building under construction goes offline.** It does not perform its function for the duration — an Infirmary being rebuilt provides no healing while the work runs. This is the real strategic cost of an upgrade; the queue is a set of decisions, not a set of wait timers.
- **There is no Speed-Up mechanic of any kind.** Time spent building is time spent, and nothing shortens it.
- **Queue slots scale with Colony Tier**, on the same one-per-Tier pattern Guest slots use.

The queue is visible in the Colony register and expanded in the ledger overlay (Sections 32.1, 32.2).

## 15. Structures and upgrade ladders

### 15.1 Structure families

**INFOGRAPHIC — Structures and Upgrade Ladders**

Shared functions are visually and spatially adapted to each species. The central hub carries a species-specific flavor name — **Warren** (rabbit), **Den** (squirrel), **Burrow** (mouse) — used as flavor and visual differentiation, not as a mechanical system. **These three words are species terminology and are never used generically** anywhere else in the game, including at the tier level (Section 31).

**Species flavor extends to every structure family, not just the hub.** Each building's name and imagery is drawn from its species' own material culture and metaphor, so a squirrel colony and a mouse colony reading the same functional map still feel like different civilizations.

The canonical families:

- Town Center / communal heart (Warren / Den / Burrow).
- Food store and dry reserve.
- Workshop and scrap store.
- Shelter and sleeping chambers.
- Nursery sanctuary.
- Infirmary / recovery nest.
- **Staging Post** at the highway edge — the departure threshold, and the place a party dresses for the road (Sections 19, 33.1).
- Lookout and warning network.
- **Guest House** — accommodation for Guests of both tiers.
- **Story Circle** — the memorial and history venue (Section 15.3).
- **Community Board** — the colony's ambient notice board (Section 15.3).
- **Welcome sign** — the colony's name made physical (Sections 22.3, 35.2).
- Species-signature transport, storage, and safety structures.

**The Guest House is one family with many faces.** Rather than sixteen bespoke structures for sixteen possible Guests, there is a single building family whose **skin and build location vary with its occupant**: a bird's is a nest raised in a tree, a Mink's sits at the water, a Mole's goes under. This is a charm feature the game invests in, not a cost to minimize.

**Placement is part of the expression, not incidental.** Where a Guest House sits is bound to the same spatial logic as everything else the colony builds — Anchor Points suit some occupants and not others (Section 8.2), and a Guest housed badly is housed visibly badly. If a Guest leaves or dies, the structure can be cleaned, adapted, or re-skinned for another compatible Guest.

### 15.2 Named upgrade ladders

Every upgradeable family has a **named ladder of two to four rungs** in place of a numeric "Level 2" label. Two gates govern it:

1. **Availability.** Some families do not exist until a given Colony Tier. Tier II's "recovery space" and Tier III's "adaptive equipment" capabilities are gates of exactly this kind.
2. **The internal ladder.** Once available, the player climbs named rungs by spending ordinary Flexible and Rigid Scrap on that specific building, through the Construction Queue. This is separate from colony-wide Tier advancement, though a building's reachable rung is **capped by the current Colony Tier.**

**Register escalates but never industrializes.** Rung names are humble and functional at Tier I and read as genuinely grand by Tier IV — but the grandeur comes from scrap-mastery and civic complexity, never from electrification, machinery, or manufacture.

| Family | Rung 1 | Rung 2 | Rung 3 | Rung 4 |
|---|---|---|---|---|
| **Rabbit Lookout** | Watch Mound | Ear Warren | Long Watch | High Warren |
| **Squirrel Food Store** | Cache Hollow | Drey Larder | High Cache | Canopy Hoard |
| **Wood Mouse Infirmary** (Tier II gated) | *unavailable* | Moss Nook | Mending Burrow | Warm Root Hall |

Full per-family tables for the remaining families are **deferred to Appendix E.** The principle is settled; the vocabulary is not yet written.

### 15.3 Functional icons, the Community Board, and the Story Circle

**INFOGRAPHIC — The Community Board and the Story Circle**

**Flavor names must never cost the player legibility.** Every building carries a persistent, always-visible **functional icon** — Healing, Storage, Warning, Craft, Shelter — living in the **base Colony register**, *not* gated behind the ledger overlay. The overlay's building-function data is the detailed text expansion of that icon rather than its only source.

This is one established pattern, not a new UI rule: flavor name plus functional metadata, shown together (Pillar 2.3).

The colony has two diegetic information objects, deliberately **not** merged because they do different jobs at different tempos:

- **The Community Board** is the **day-to-day operational feed**, *ambiently visible at all times* — read in passing without entering anything. It carries alerts, standing duties, foraging shares, scout returns, and active Choice-Event Cards. It is the diegetic face of the Almanac's event feed (Section 21.1). Road Work notices stay strictly qualitative — never "Mowing Tomorrow," never a countdown.
- **The Story Circle** is the **ceremonial venue**, and its content exists only when entered. It is where the Teacher recites the Laws and Sayings, where the Colony Record is read, where grief is processed after a Hearth loss, and where the colony's understated physical memorials stand. It has its own named upgrade ladder like any other family.

Operational versus ceremonial, expressed spatially as well as tonally.

---

# PART IV — THE CITIZENS

**ARTWORK — Going Tharn**

*Who lives in the colony, what happens to them, and how they are remembered. Guest Citizens are here, with the citizens they become; the procedure for recruiting them is in Part V, where recruitment actually happens.*

---

## 16. The citizen record

**INFOGRAPHIC — The Character Record**

Every citizen has a **Character Record** (Section 21.2), presented in two views — a **Likeness** for facts and a **Tale** for history.

A citizen's Likeness carries:

- **Given Name** and, if earned, **After-name** — two distinct name fields (Section 22.1).
- Species, appearance, and portrait.
- Age / life stage.
- **Bonds** — Trusted Friends and Hearth membership, named and characterized.
- A randomized personality trait, assigned at birth, unrelated to lineage.
- Broad visible aptitude descriptors.
- Traits, learned history, and current standing Role.
- **Three equipment slots — Keepsake, Tool, and Supply** (Section 19).
- Expedition and colony-work history, with each expedition's Rating.
- Wounds, permanent impairments, adaptive equipment, and fear memories.
- Permanent **Distinctions** earned in the field (Section 18.3).
- Notable acts, discoveries, relationships, and memorial links.

Underlying values may include movement, carrying, stealth and noise, perception, resilience, stress threshold, and social aptitude. **Exact values remain hidden.** Players see descriptive bands, clear consequences, and history rather than raw ratings.

## 17. Bonds, Hearths, and growth

### 17.1 Bonds

**INFOGRAPHIC — Bonds, Hearths and Nesting Season**

Citizens form **named, characterized bonds** that appear on their Records — *"Bramble and Twig — best friends"*, *"Sharpnose and Nutmeg — partners in crime"*, *"Daisy and Fennel — inseparable since the culvert"* — rather than accumulating on an invisible affinity meter. There is no relationship simulation and no visible relationship number; bonds are displayed descriptively and change through events, never through a tracked score.

Two tiers:

- **Trusted Friend.** Formed by a shared significant experience: surviving an expedition together, one rescuing the other, one leading the other out of tharn. The displayed phrasing varies by the pair and by how the bond formed.
- **Hearth.** A family unit, formed when Trusted Friends accumulate *another* such experience together. Usually a pair, but it can take others in — an orphaned young citizen, a maimed veteran with nowhere else. **A Hearth is a found family.**

Bonds carry only the effects canon already implies: companions reduce each other's tharn risk when travelling together, a death produces grief in the survivors, and a Keepsake may be gifted within a living Hearth. Nothing else.

### 17.2 Hearths and lineage

A **Hearth** is the unit that can bring a new named citizen into the world, and only during a **Nesting Season** (Section 10.1).

**A Hearth that produces a child acquires descent — as a story fact, and only as a story fact.** The child's Tale records that they were **"born of [Hearth]"**, and the colony remembers who came from whom. Nothing whatsoever transmits mechanically. The child receives a **randomized personality trait unrelated to lineage**, exactly as every other citizen does.

This distinction is load-bearing and is stated in both directions: **the fiction has families; the simulation has no heredity.** There is no genetics, no bloodline ledger, no inherited aptitude, no skill tree, and no breeding-optimization system (Appendix A). Hearths do not introduce one by the back door — they are a narrative structure sitting on top of an unchanged, lineage-blind trait roll.

**Hearths are less deployable.** Bonded families trade flexibility for warmth, and the game states the trade openly:

- **A Hearth cannot be split for solo outpost duty.** Hearth members are ineligible for solo stationing (Section 28.3).
- **A full Hearth may relocate together** to an outpost with two or more citizen slots.

The colony's most emotionally settled citizens are therefore its least mobile, which deliberately puts the population pressure-valve and the cozy social layer in tension.

**Grief.** When a Hearth member dies, survivors take a temporary **Shaken** state plus a persistent **fear memory** tied to the loss (Sections 18.1, 18.2). Both use systems that already exist — there is no grief meter and no new state. The Shaken state fades on its own; the fear memory is mitigable through the Teacher Role and time spent at the memorial in the Story Circle.

### 17.3 Nesting Season

Core-species reproduction is rare, seasonal, expensive, and player-authorized.

- A mating opportunity exists only in suitable seasonal and colony conditions.
- Two citizens are committed to care and cannot be treated as normal expedition labor during the critical period.
- Sustenance, shelter, safety, and space requirements are substantial.
- A successful cycle yields a very small number of named young, and the low-population ceiling is untouched.
- **The player is never encouraged to breed disposable replacements.**

Exact biology can be stylized consistently across species to protect pacing. Each new citizen receives a **Given Name** at birth (Section 22.1), framed in-fiction as a name gifted by the Hearth.

### 17.4 Wanderers — the other way a colony grows

**INFOGRAPHIC — Wanderers**

A founding trio plus rare seasonal births is a very slow curve. **Displaced core-species wanderers are the primary early-game growth path**, with Nesting Season staying the rarer and more emotionally weighted one.

**A wanderer joins as an ordinary named Citizen** — not a Guest, occupying no Guest slot, with full equal standing, a Given Name, a personality trait, and a Character Record from the moment of arrival. They are of the colony's own species; there is still no cross-recruitment between core species.

Three arrival routes, all reusing existing systems:

- **Expedition encounter**, on the contest funnel's non-antagonist branch (Section 26.2) — parallel to Guest recruitment but resolving to a Citizen.
- **Rescue**, from a hazard or a Road Work event.
- **A Choice-Event Card at the colony** (Section 10.3) — a stranger at the edge of the median, with a costed decision about taking them in.

Every wanderer carries a backstory reason for being alone. That reason is what keeps them from reading as spawned units, and it is written into their Tale on arrival.

**The flagship case: another survivor.** A wanderer may be **another survivor of the Founding Escape.** The trio's belief that they alone came through is therefore wrong, and the game can deliver that as an event — potentially years into a campaign. Such an arrival may also carry **a Law the trio remembered wrong**, which is the payoff for the imperfect folklore the colony has been teaching its young since the first day (Sections 6.1, 35.1).

*Open:* arrival rate and whether it scales with Tier; whether a wanderer can be refused and at what cost; whether wanderers can arrive already maimed or fearful (Appendix D).

### 17.5 Death and memorialization

**ARTWORK — The Memorial**

Death is possible but uncommon outside catastrophic errors or extreme events. It should never become the routine expected price of ordinary expeditions.

When a citizen dies, their **Character Record** — Likeness and Tale both, with portrait, relationships, and full history intact — moves into the colony's memorial archive rather than being deleted. **A Tale is closed, not erased**, and remains readable.

Their **Keepsake** returns to the colony's shared stock as an inheritable memorial object (Section 19): a thing another citizen may one day carry, with the provenance of who carried it first recorded in the new holder's Record. This is the game's quietest continuity mechanic and one of its most important.

The player may place an understated physical memorial in the Home Median. Memorials are placed **at the Story Circle**, which makes the ceremonial venue the place where loss is both marked and, over time, processed.

---

## 18. Harm, fear, and tharn

**INFOGRAPHIC — Harm, Fear and Tharn**

### 18.1 The harm ladder

**ARTWORK — A Maimed Veteran, Valued**

1. **Shaken / exhausted:** short recovery, reduced readiness. Also the state produced by grief at a Hearth member's death.
2. **Wounded:** meaningful temporary impairment requiring rest, food, care, and multiple days to heal.
3. **Maimed:** permanent bodily change with lasting functional consequences.
4. **Death:** rare, final loss.

Maiming has weight because it changes what a citizen can safely do, not because it converts them into dead weight. Physical limitations remain real and visible; experience, relationships, knowledge, and emotional importance remain intact.

Adaptive equipment, produced by the Crafter Role, can **ameliorate — not erase** — an impairment. A maimed citizen may still expedition when the player judges the route and role appropriate, and some veterans become calm expedition anchors who reduce tharn risk in less-experienced companions.

**The game must never imply that disability automatically grants genius or supernatural compensation.** Veteran strengths emerge from lived history and role design.

Adaptive equipment is a **fourth**, separate thing from the three citizen equipment slots: it offsets a specific impairment and is not chosen, lent, or swapped.

### 18.2 Fear and going tharn

Fear is a core system, not a cosmetic morale debuff. Stress accumulates through exposure to traffic, predators, darkness, noise, injury, exhaustion, separation, and recalled trauma. When a citizen exceeds their threshold they may go **tharn**: freezing, dropping carried items, failing to obey movement commands, and requiring rescue or calming intervention.

Tharn is a rare, dramaturgically forefronted freeze-event, deliberately kept *distinct* from the Distinction/Maiming economy. It is available to all three core species — not rabbit-exclusive — each with its own thematic flavor.

**Its resolution is a physical beat**: someone must reach the frozen citizen and lead them out, risking additional exposure, rather than paying a flat stat penalty. Retreat and abandonment remain possible, painful choices.

**Trigger.** A citizen goes tharn when their **exposure exceeds their stress threshold** during an encounter (Section 25.5). This is a single unified trigger built on machinery that exists only inside an encounter, with per-species flavor in how the freeze *manifests* rather than in what causes it. Load and isolation both feed it without needing triggers of their own: load raises exposure directly, and a citizen whose exposure has spiked far above the party's is, definitionally, the one out there alone.

**Effect inside the encounter:**

- The citizen stops contributing to the party's score.
- They drop carried cargo.
- Their exposure continues climbing each round until they are resolved.
- The Turn gains a **Rescue** option targeting them specifically.
- If never rescued, and the party withdraws or the encounter ends, **they are left behind.**

Surviving tharn can create a persistent fear memory tied to a trigger. Recovery, trusted companions, experience, a veteran anchor, and certain Guest effects can mitigate future risk. **Trauma never simply converts into a numerical bonus.**

Leading a companion out of tharn is one of the shared significant experiences that forms a **Trusted Friend** bond, and companions travelling together reduce each other's tharn risk — the system's social and psychological halves feed each other.

**Fear memories also arise from grief** (Section 17.2), using this same system and mitigated the same ways.

*Still open:* the numeric threshold values, and whether Crossing — an action mode, not an encounter — needs its own tharn trigger (Appendix D).

### 18.3 Distinctions, the symmetry, and the After-name

Permanent *positive* traits — **Distinctions** (also "Feats") — mirror permanent *negative* traits structurally. Both are rare, discrete, earned through expedition participation, and both **accumulate over a career** — neither is gated to once-per-life or once-per-Tier.

Distinctions are tied to the rare *good* tail of the outcome distribution, exactly the way Maiming is tied to its rare *bad* tail. This reuses an existing mechanism rather than adding one, and it is scoped entirely within the expedition-only rule: a citizen who never expeditions again earns no further Distinctions.

**The symmetry has a shared driver.** Both tails are opened by the same thing — **exposure** (Section 25.5). The citizen who stuck their neck out is the one who comes home changed, in one direction or the other. A citizen who did nothing remarkable gets nothing remarkable, good or bad.

**A citizen's first Distinction also grants their After-name** — the earned epithet that joins their Given Name and is used thereafter throughout the Records and the interface (Section 22.1). Later Distinctions accrue normally but do **not** churn the displayed name; the first one is the one that names you.

Most citizens never earn one. A citizen who stays home never will, and most who do expedition never hit the rare good tail. **This is intended rather than a gap** — an After-name means something precisely because the colony contains animals who do not have one.

### 18.4 How citizens develop

Individual progression is deliberately narrow. Continuous, passive skill growth is **not** adopted. The sole individual-progression path is the discrete **Distinction / Maiming / Wounding** system — earned in the field, never at home.

Separately and independently, there is one colony-wide progression event: **when the Colony graduates to a new Tier, every citizen receives a stat bump.** This is a property of the colony's advancement, distinct from any individual's history, and it applies to everyone at once.

---

## 19. Equipment: Keepsake, Tool, and Supply

**INFOGRAPHIC — Keepsake, Tool and Supply**

Every citizen has **three equipment slots**. All three feed the existing equipment modifier in encounter resolution (Section 25.4) — no new engine, three named sources filling one slot that already existed.

All three are backend-numeric and **player-facing descriptive**: the interface says *"unsettles birds,"* never *"+3 versus Avian."* Effects are **small and situational**. They tilt a resolution; they never dominate one. There are no build-defining stacks, and no combination should ever feel like the reason an expedition succeeded.

**Keepsake — personal, permanent, non-transferable.**
A Keepsake belongs to one citizen and characterizes them. It travels automatically with zero preparation, and always carries some small situational effect. The slot may start empty and fills through history: found in the field, inherited from the dead, or **gifted within a living Hearth** — that last path scoped deliberately to bonded family, so a gift means something. Each founding citizen may begin with one carried out of the old home.

On death, a Keepsake **drops into the colony's shared stock as an inheritable memorial object**, and its provenance travels with it into whoever carries it next (Section 17.5).

**Tool — colony property, lent out and returned.**
A Tool is a persistent, citizen-level assignment drawn from shared colony stock, **assigned at the colony-management level, never at the Expedition Launcher.** It uses the same standing-assignment interface as Roles (Section 12) — a decision about the colony, not about a mission. It can be reassigned or returned to stock exactly like lending out a physical object, because that is what it is.

**Tools live at the Staging Post**, where a departing party also takes up its road dress (Section 33.1). The building at the highway edge is therefore the colony's threshold in a fuller sense than geography alone: it is where citizens stop being at home.

The flagship example is the **pull-tab-and-needle multitool** (Section 13).

**The slot is called Tool and not "Weapon," and the distinction is deliberate rather than cosmetic.** A slot named Weapon would invite exactly the weaponization this design excludes. Animals in MEDIAN use objects; they do not arm themselves.

**Supply — per-run, per-citizen, consumable.**
A Supply is drawn from colony stock and chosen at the **Expedition Launcher**, one per departing citizen, for that run only. Its effect lives for the duration and then it is gone.

This is the *only* one of the three the Launcher ever surfaces, which keeps the per-citizen picking burden at exactly one choice (Section 27.2). It is also the slot with a visible moment of use: **playing a Supply is a Turn action inside an encounter** (Section 25.4), which is what the slot exists for.

**Distinct from neighboring systems.** Special Artifacts are colony-level (Section 13); adaptive equipment offsets maiming and is produced by the Crafter (Section 18.1). Neither is a slot, and a citizen may hold all of the above at once.

---

## 20. Guest Citizens

Guest Citizens are rare, named, non-breeding animals from outside the colony's core species. Inspired directly by Kehaar in *Watership Down* — a designer-facing reference; no *Watership Down* name appears in MEDIAN's own fiction (Section 6) — the system brings a wide variety of animal life into a campaign without requiring every species to support a full civilization ruleset. It is where the found-family beat lives, since the core species never cross-recruit.

**Every recruited Guest is a full, equal-status, named citizen** — not a subordinate, not a unit. They have Character Records, bonds, Keepsakes, Distinctions, and After-names like anyone else. They differ from core citizens in exactly two ways: they occupy their own separate capped slot pools, and they arrive through recruitment rather than birth. A joining Guest receives a **Given Name** (Section 22.1) — and carries it *from the first encounter*, before any decision to recruit. The player meets a named animal, not a candidate.

Two tiers: **Active Guests** and **Ambient Guests.**

*The procedure for recruiting a Guest — the contest funnel, the amenability check, the residence cost, and the slot cap — lives in Section 26, because recruitment happens in the field.*

### 20.1 Active Guests

**INFOGRAPHIC — Active Guests: The Seven**

**ARTWORK — Guest Vignettes**

Active Guests join expedition parties, occupying a valuable slot and introducing a bounded ability, traversal option, defensive behavior, negotiation route, or information advantage. They do not remove the core citizens' need to take risks.

The **universal contribution rule** holds with **zero exceptions**: every citizen, Guest included, contributes on *both* carry and fight to some non-zero degree, so no recruit is ever pure dead weight outside its specialty.

**Guests are option-openers, not stat sticks.** This is the roster's governing design premise. A Guest modifies the **available options** in an encounter rather than the score: the Mink does not add a bonus, the Mink makes *"rescue from water"* an available Turn action that otherwise is not on the menu (Section 25).

> **The template: each Active Guest opens at least one Approach or Turn action, and closes or complicates at least one.**

This is how every Guest acquires a situational trade-off systematically, rather than through seven bespoke penalties invented one at a time. A Guest who opens one door and closes another is inherently a decision.

The roster is **seven**:

| Guest | Opens | Closes / complicates |
|---|---|---|
| **Weasel** | Contest against small predators; high carry and fight muscle | Parley with prey species — they are afraid of it |
| **Fox** | Windfall processing — the only Guest that can safely render a predator kill or major roadkill into usable resources | Evade — too large to go unnoticed |
| **Mink** | Rescue from water, culverts, and drainage | Little value away from water |
| **Crow** | Aerial scouting — reveals a node's Approach set before the party commits | The party cannot Evade while it is overhead |
| **Hedgehog** | Contest above the party's weight; durable escort and cover | Slow — raises exposure on Evade |
| **Snake** | Parley by intimidation and display; minimal but non-zero carry | Movement penalty in Winter (Section 4.5) |
| **Raccoon** | **Sealed human-container nodes** — latched coolers, zip-tied bags, capped bottles, bins (Section 24.3) | Draws other scavengers — raises contest frequency at nearby nodes |


**Seven Guests against four slots.** The roster exceeds the slot cap deliberately: the player fields a fraction of what exists, and passing on a good recruit costs something (Section 26.3).

*Open:* the opens/closes pairs above are working sketches confirming the template rather than final tuning; a full roster pass is queued (Appendix D).

### 20.2 Ambient Guests

**INFOGRAPHIC — Ambient Guests: The Nine**

Ambient Guests live at the Home Median or, once unlocked, at an outpost, providing a spatial passive effect while remaining visible residents with routines and relationships. Unlike Active Guests they are **uniform, downside-free safe investments** — every Ambient Guest is a pure positive. The option-opener template does not apply to them, because they never enter an encounter.

The roster is nine:

| Guest | Passive effect |
|---|---|
| **Owl** | Increases passive perimeter predator-detection radius, night-weighted. *Stays passive — never an escort.* |
| **Songbird** | Ambient morale and efficiency; citizens work and move slightly faster at home. |
| **Toad** | Reduces spoilage and loss on stored food; steadies its wet-culvert surroundings. |
| **Firefly** | Extends the duration of safe nighttime colony activity. |
| **Groundhog** | Advance warning of seasonal and weather events, and of approaching **Choice-Event Cards** — always qualitative, never a countdown. |
| **Turtle** | Small, steady, unraidable passive resource trickle each cycle. |
| **Bee** | Increases yield from foraged plant resources. |
| **Mole** | Reveals soil and structural information. |
| **Bat** | Protects structures from insect and pest decay. |

When several Ambient Guests live at home, the player may select one effect for a temporary **Cultural Focus** boost; the others continue providing their normal effects. Ambient Guests may later be assigned to compatible outposts, one per outpost central building.

*Open:* the Turtle's effect is the weakest on the roster — a flat trickle duplicates what an outbuilding already does, and it deserves something with more character (Appendix D).

**Template character — WHOOT.** The Owl's eventual flavor writeup uses a template character: **WHOOT**, a barred owl with a permanently weak wing who can no longer hunt on the move and has become a stationary watcher instead. WHOOT gives a warm, concrete backstory reason for the rule that the Owl stays passive and is never an escort — and doubles as a lived demonstration of Pillar 2.5 applied to a Guest rather than a core citizen: a maimed animal remains valuable, and finds the role that fits. Because Ambient Guests do not expedition, WHOOT's injury reads as pre-colony history rather than an in-system Maiming, and it neither grants nor requires an After-name.

*(A wider set of example citizens, written in the register of tabletop RPG sourcebook NPC entries, is a future-work item — Appendix D.)*

### 20.3 Antagonist fauna, and the ones who can change sides

Not every animal met in the field is a candidate for the colony. Some are simply threats.

**The Rat is not a citizen in any form** — neither Active nor Ambient. It exists only as **antagonist fauna** in contested encounters and Base Defense. *(An earlier art asset depicting a rat citizen, "Grist," was a misdepiction of what should have been a mouse.)*

**The raccoon sits alongside the Rat as recurring antagonist fauna** — larger, cannier, and a more serious threat at both contested nodes and Base Defense — but differs from it in the one way that matters: **the raccoon is recruitable and the Rat is not.** The raccoon can be met as an enemy, met again as a neutral, and eventually brought home (Sections 26.2, 20.1). The pair exists to make that distinction legible: **antagonist status in MEDIAN is a position an animal currently occupies, not always a fixed nature.**

The **Weasel** and the **Hedgehog** should carry the same duality — both appear on the Active roster and both are plausible antagonists in the field — but this is not yet specified (Appendix D).

### 20.4 Single-species colonies and Guest accommodation

No-cross-recruitment among the core species is absolute: a rabbit colony never recruits squirrels or mice, and so on. The found-family story beat lives entirely in the Guest system instead.

Guest accommodation is the **Guest House**, one building family whose skin and placement vary with its occupant (Section 15.1).

**Guests wear less than core citizens, and most wear nothing.** Core citizens dress to leave home (Section 33.1); Guests generally do not, and several could not. A crow, a snake and a fox need no cloak to be told apart from one another or from the colony around them — being visibly a different species already does the work that dress does for a single-species colony. A Guest may carry one signature object; that is the ceiling. This is a difference in depiction only and implies nothing about standing: **every recruited Guest remains a full, equal-status, named citizen.**

---

## 21. The Records

**INFOGRAPHIC — The Records**

The colony's story, and each citizen's story inside it, is a **first-class named system** rather than a log buried in a menu. It is called **The Records.**

The Records exist because MEDIAN's central promise — that the player will know these animals by name and remember what happened to them — needs somewhere to actually live. Two registers mirror the two independent halves of encounter resolution (Section 25.5): what the group did, and what happened to each individual.

**The Records are narrative-first and are not a resource.** They introduce **no Knowledge currency, no Story currency, and no new tracked stat of any kind.** Where a Record implies a mechanical effect — a Teacher passing knowledge, a story spreading to another colony — that effect routes through a system that already exists: the Teacher Role (Section 12), rumors and intelligence at the Expedition Launcher (Section 27.2), or the Rest-Stop Metropolis (Part VI).

Each Record has **two views**, named per scale:

| Scale | Summary view (now) | Literary view (history) |
|---|---|---|
| **Colony Record** | **Almanac** | **Chronicle** — in-world, *"The Remembering"* |
| **Character Record** | **Likeness** | **Tale** — *"Bramble's Tale"* |

Placing a factual summary beside a literary history is the "ledger and legible" pillar and the "stories over statistics" principle sitting side by side rather than in tension.

**Styling convention.** Colony views take the definite article: **"The Almanac," "The Chronicle."** Citizen views are possessive: **"Bramble's Likeness," "Sharpnose's Tale."** The grammar carries the scale — the colony has *the* record; each citizen owns *theirs*.

### 21.1 The Colony Record — Almanac and Chronicle

**The Almanac** is the at-a-glance state of the colony: founded date, founding members, all current citizens **by name**, greatest triumph, largest threat, next goal, Tier milestones, and a dated feed of named events.

Almost all of it auto-populates. The player touches it in only three places: naming the colony once at founding, pinning a **Greatest Triumph**, and setting a **Next Goal**. It is not a journal the player writes.

**The event feed names individuals, always.** "Nutmeg and Daisy healed Sharpnose," never "two citizens performed healing." This is not flavor text — it is the atomic data spine of the whole system, feeding the Chronicle's prose upward and the Community Board's ambient display outward, and it is the most direct expression of Pillar 2.2.

**The Chronicle** is the same material told as history, in the storyteller's mythic and reverent register — the voice of the Laws and Sayings (Section 6). Its in-world name is **The Remembering**.

The Almanac is read in the interface and glimpsed ambiently on the **Community Board**; the Chronicle is read at the **Story Circle**, entered deliberately (Section 15.3).

### 21.2 The Character Record — Likeness and Tale

Every citizen has one, from birth or recruitment to death and after.

**The Likeness** is the citizen's current state, enumerated in Section 16.

**The Tale** is the accreting personal strand: every expedition and its Rating, every Distinction and Maiming and where it happened, fear memories and what caused them, how each relationship formed, which Keepsake they carry and who carried it before them, and which colony events they were part of. "Bramble's Tale" is a life, written as it is lived.

On death, the Record moves to the memorial archive rather than being deleted (Section 17.5).

**The Village Roster** (Section 32.3) is the index screen that lists every citizen and leads into their Record.

**One record, two outputs.** The Character Record is the same structured description the optional portrait system reads from when regenerating a citizen's image after a permanent change (Section 34). There is one canonical history per citizen, and it produces prose and portrait alike.

### 21.3 Expedition Rating and the Report and Share debrief

The post-expedition screen has two halves — a **Rating** and a **debrief** — and together they are the Records' principal event-generator, writing into the Colony Record and every participant's Character Record at once.

**The Rating** is one of four diegetic grades, player-facing descriptive language and **never a score**. It is **derived** from the encounter model rather than authored by designer judgment (Section 25.5):

| Rating | Condition |
|---|---|
| **Legendary** | Objective met **+** at least one high-exposure **good** tail — a Distinction, an Artifact, a Guest opportunity |
| **Successful** | Objective met, exposure resolving without significant individual consequence |
| **Hard-Earned** | Objective met **+** at least one high-exposure **bad** tail — the costly victory |
| **Failed** | Objective not met |

The Rating reflects the **group** outcome. A clean failure simply reads as Failed, with nuance carried by the debrief text rather than by a fifth grade. Every Rating is written into the Chronicle as a dated entry, and into the Tale of everyone who went.

**The Report and Share debrief** is the content half: what the party found, what was dangerous, what was newly mapped, who fell. It writes the Record entries, and it updates the corridor map and the Launcher's previews and rumors (Section 27.2) so that what the colony *knows* reflects what it actually saw.

There is **no sharing bonus.** Map and preview updates are simply "you now know what you saw" — not a reward to be farmed. The debrief is narrative and informational only.

---

## 22. Names

**INFOGRAPHIC — Names**

Naming in MEDIAN is a system with a stated rule at its center: **the player authors exactly one name in the entire game.** Everything else is generated, discovered, or earned.

### 22.1 Names of citizens — Given Name and After-name

**The Given Name** arrives at inception. Every citizen has one: the founding trio, every citizen born in a Nesting Season, every wanderer, and every Guest — the last carrying theirs from the first encounter, before any decision to recruit.

The non-generative baseline is a **species-specific name-component bank** — the same engine family as the place-name grammar below, where every legal name assembles from curated parts so the register is guaranteed structurally rather than policed afterward. An optional enhanced layer can generate names through the system in Section 34, on exactly the same terms as portraits and Chronicle prose: an enhancement, never a requirement.

**The After-name** is the earned epithet — the *Oakenshield* half of a name. It is granted by a citizen's **first Distinction** (Section 18.3), reusing a system that already exists rather than inventing a separate "moment of significance" trigger. Once granted it sticks, and it is used from then on throughout the Records and the interface. Later Distinctions accrue normally without churning the name.

*(The designer-facing term for this field is the agnomen; **After-name** is what the game says, because MEDIAN's folk register is deliberately homely and plain.)*

Most citizens never earn one. This is the point, not a shortfall — an After-name means something precisely because the colony contains animals who do not have one.

**"Earned, gifted, chosen" reconciled.** These are not three mechanics. *Earned* is the After-name. *Gifted* and *chosen* are two narrative framings of how a Given Name arrives — gifted by a Hearth at a Nesting Season birth, chosen by a Guest taking a new name on joining. One field, two lenses.

**The moment of the After-name** is written into the citizen's Tale automatically. If the optional generative layer is active, that moment is also a candidate for a still image — already covered by the existing splash trigger for "a Distinction earned" (Section 34), not a new subsystem.

### 22.2 Names of places — the folk-name grammar

Places in MEDIAN are named by **the world and by history**, not by the player.

**The shared engine is a curated folk-name grammar.** Every legal place name assembles from blessed parts — an article, modifier banks (materials, flora, qualities, water, fauna-trace), landform suffixes, and a small set of patterns. Because every name is built from approved components, the register is guaranteed *structurally*; there is no post-hoc profanity filtering and nothing to police.

**The register is tuned homely and plain, never ornate** — the *"The Hill / Bywater"* end of Tolkien rather than the elvish end. Twin Oaks. The Low. Stonemouth. Bramble Cross. The Long Verge. Animals have an intimate, working relationship with ground they cross on foot every day, and their names for it should sound like it.

Two authorities produce names:

1. **The world names the place (primary).** Generated names derive from a Reach's actual character — its biome, its Anchor Points, its hydrology, its lane count. A Reach with twin oaks at its heart gets named for them. The player mostly **learns** these names — from a Teacher, from rumor, from the Metropolis — rather than assigning them.
2. **History names the place.** Notable nodes acquire event-conferred names in the Chronicle's voice: *Sharpnose's Rest*, *The Burning*. A place can gain a second name over time as things happen there, layering memory onto geography. This is where the Records and the map touch.

**One name per place, plus tags.** A place has **one folk name** and, separately, **functional metadata** shown as Almanac tags — *interchange*, *five-lane*, *wooded*. Not a literal-versus-folk name pair; the same flavor-plus-function pattern used everywhere else (Pillar 2.3).

The component banks are **deferred to Appendix F.** The engine and register are settled; the vocabulary is not yet written.

### 22.3 The one name the player authors

**The player names exactly one thing in MEDIAN: the Home colony.** Note that this is the *colony*, not the *Median* — the Home Median is a Reach and receives its own generated folk name like any other (Section 7.2). A colony called Horizon Fields may stand on ground the corridor has always called The Long Verge.

Even that one name is a **curated pick, not a composition**:

- **Choose one of three generated names.** Candidates are drawn from a combined pool spanning two registers: **grounded and biome-realistic** (the same homely-plain grammar as every other place name, filtered to the Home Reach's actual biome) and **aspirational and mythic-hope** (new-beginning, horizon-facing names). Both carry a **species-metaphor layer** — rabbit, squirrel, and mouse each draw from their own imagery bank, extending the Warren / Den / Burrow pattern.
- **Reroll freely.** A reroll generates three more from the same pool, unlimited and free. This is a matter of taste, not a resource decision.
- **No free text. Anywhere.** There is no typed-name option for the colony, buried or otherwise. Three-plus-reroll gives enough expression on its own, and keeping it text-free makes *"all names are permanent, none are typed"* a clean total rule instead of a rule with an asterisk.
- **The aspirational register is scoped to colony-naming alone.** It is *not* added to the general Reach and node grammar, which stays homely and plain everywhere else. The colony gets the extra emotional register because founding it is the one act of authorship the player is given.
- **Locked permanently once chosen.** There is no renaming.

The mechanic lands in the tutorial at the first civic construction (Section 35.2), alongside the physical **welcome sign** that carries the name.

---

# PART V — LEAVING HOME

**ARTWORK — The Night Crossing**

*The three away-registers in the order the player meets them, then the systems that govern what happens out there.*

---

## 23. Crossing

**INFOGRAPHIC — The Crossing**

### 23.1 The crossing action

The standard transverse sequence runs Home → Away. The party gathers at a Staging Post; the view reveals the lanes between safe Median cover and Margin vegetation ahead; the player reads traffic density, vehicle types, audio, headlight cues, wind shear, lane islands, and micro-cover before committing movement between temporary safe positions or across the full gap.

Citizen speed, fear, wounds, load, and formation affect responsiveness without replacing player skill. The action must be **tense, brief, comprehensible, and tolerant enough that ordinary play does not produce routine mass casualty.**

Accessibility options include time scaling, stronger telegraphs, simplified input, audio visualization, and possibly an assisted strategic resolution (Section 32.5).

The First Law — *"Wait for the gap. The gap is given, not owed."* — is the crossing's tutorial text, its folklore, and an accurate description of its mechanics, all at once (Section 6.1).

**Crossing is not an encounter.** It uses no Approaches, no Turns, and no exposure. It is an action mode with its own design.

*Flagged for dedicated design:* Crossing is the game's signature mechanic and its least specified system. How it actually plays moment to moment — input model, failure states, how the party moves as a group, how longitudinal travel differs (Section 7.3) — needs its own pass (Appendix D).

### 23.2 Return logic

After a successful outbound crossing and a resolved Field run, the player chooses when to head home, and the return resolves on this distribution:

- **70% — clean automatic return:** a short automatic or cinematic crossing that respects the challenge already completed.
- **20% — automatic with a swing:** the party gets home automatically, but with a swing that can break positive *or* negative — a bonus find, or lost cargo, a minor wound, gained fear.
- **10% — forced manual re-crossing:** changing traffic, Road Work, predator pressure, weather, fatigue, or a narrative event forces the player back into the crossing action.

*(This 70/20/10 split supersedes the earlier 80/10/10 hypothesis.)*

---

## 24. Field Mode

**INFOGRAPHIC — Field Mode**

**ARTWORK — Field Mode Traversal**

### 24.1 What it is

Field Mode is a **traversable, surveyed territory** that the expedition party physically moves through, visiting multiple discoverable nodes rather than receiving an instant loot menu.

- **Reaching a node** triggers *that specific node's* contest check — not one roll for the whole visit — and opens the Encounter frame (Section 25).
- **Carry-capacity and weight tension** plays out here: the party fills up as it goes and must decide when a heavy find is worth a cooperative carry or a trip home.
- **Traffic-as-Weather is present throughout** (Section 9.3), scaling by proximity to the road edge.
- **Choice-Event Cards appear occasionally** as a light interstitial layer between structured nodes (Section 10.3) — most visibly **Litter**.
- **Road Work's telegraph signs** appear here as readable environmental changes.
- The player **exits by choosing to head home**, feeding into Return Logic (Section 23.2).

Field Mode is what keeps *uncontested* expeditions interesting: the tension of traversal, discovery, and load management exists even when nothing attacks.

### 24.2 Presentation and overlays

Field Mode is **top-down and illustrated, not schematic and abstract** — a hand-drawn naturalist's field survey rather than an information display (Section 3.2). Warm parchment ground, painterly terrain, visible hand, node markers as pins over the illustration, the highway always in frame.

**Named ground.** Anchor Points supply a Reach's labeled areas (Section 8.2), carrying the folk names the world gave them (Section 22.2).

**Route overlays.** Dashed route lines drawn over the illustration, in the manner of a survey map annotating movement: **toggleable overlays** for animal paths, water flow, and wind and scent drift. This is the mode's information layer — Pillar 2.3 applied to territory rather than to resources — and it is what lets a player *plan* a route rather than merely walk one. Keeping the data on a toggleable layer also keeps the base illustration uncluttered.

*Open:* which overlays exist, whether they are independent toggles or a single cycling layer, and whether any are gated by Guest or Role (Appendix D).

### 24.3 Node types

Nodes are the units of a territory. Beyond ordinary forage and salvage:

- **Sealed human-container nodes** — a latched cooler, a zip-tied bag, a capped bottle, a bin. They hold rare loot and cannot be opened by any core species. **A raccoon in the party unlocks them** (Section 20.1) — a pure *access* niche, parallel to the Mink's water extraction and the wood mouse's Margin pockets, and distinct from the Fox's windfall *processing*.
- **Margin pockets** — reachable only by wood mice, and only after the same crossing everyone takes (Section 4.4).
- **Water hazards** — culverts, drainage, standing water; the Mink's domain.
- **Anchor Point nodes** — the named terrain features themselves, which is where an Establish Outpost party is headed.

### 24.4 Field Mode generalizes

The same Field Mode is **reused, not rebuilt bespoke**, across every destination. The expedition types differ in what persists and what the party is there to do, not in a separate traversal engine each.

**This includes home.** The Home Median is a Median Reach with a biome, Anchor Points, and node-bearing ground (Section 7.2), and it carries **both** the Colony register and a Field layer. Everyday local foraging is a **low-stakes Field run on home ground**, with structures appearing as nodes alongside forage and terrain.

Two consequences worth stating:

- **The tutorial improves materially.** Field Mode is taught *safely*, at home, at the moment the player first feeds the group — so the first real expedition reads as *the same activity, across the road*, which is exactly what it is (Section 35.2).
- **Field Mode does not stop meaning "away."** The player leaves home by **Crossing**, not by changing camera. The emotional charge lives in Section 23, where it belongs.

**It also includes the Metropolis**, which is a Field territory with venues as nodes (Part VI).

*Open:* the home Field layer's risk floor — whether contest is possible on home ground at all, and what Road Work does to a home Field run (Appendix D).

---

## 25. Encounters

Every node arrival opens the Encounter frame, and it is **the same frame whether the result is a windfall, a negotiation, or an ambush.** A quiet, uncontested node still gets its moment.

That rule is not generosity toward pacing — it is the mode's rhythm. **Plan on the map, live in the room.** It is what concentrates the art budget at the moments that matter and keeps a surveyed Field layer from making the dangerous half of the game look cheaper than the safe half (Section 3.3).

### 25.1 The shape of an encounter

**INFOGRAPHIC — The Encounter Frame**

**Rounds resolve. Turns sit between them.** An encounter runs one, two, or three rounds and carries **one fewer Turn than it has rounds.** The final round always resolves finally — there is never a dangling choice after the last roll.

| Rounds | Turns | Character |
|---|---|---|
| **1** | **0** | The common case. The contest resolved decisively on contact — a windfall, a rout, a clean slip past. Fast. |
| **2** | **1** | Round 1 landed close rather than clean. One Turn, then Round 2 resolves. |
| **3** | **2** | Still close after Round 2. Two Turns, then Round 3 resolves finally. Rare. The epic case. |

**What continues an encounter:** a round that resolves *cleanly* ends it; a round that lands *close* — near the middle of the distribution rather than decisively either way — continues it. Length is therefore never arbitrary. An encounter runs long exactly because neither side would give ground, and it **self-selects**: evenly matched contests go the distance, mismatches end on contact.

**Hard cap: three rounds.** No exception, no artifact, no encounter type.

The full beat sequence:

| Beat | What happens | Player acts? |
|---|---|---|
| **Situation** | The encounter is described diegetically. Available **Approaches** are shown. | — |
| **Approach** | The player chooses how the party meets this. | **Yes — entry choice** |
| **Round 1** | Group resolution. If clean, the encounter ends here. | — |
| **Turn** | Only if Round 1 landed close. The player acts once. | **Yes** |
| **Round 2** | Group resolution, modified by the Turn. If clean, ends here. | — |
| **Turn** | Only if Round 2 landed close. The player acts once more. | **Yes** |
| **Round 3** | Resolves finally, always. | — |
| **Exposure** | Each citizen's individual outcome resolves. | — |
| **Record** | Rating and debrief written to the Records (Section 21.3). | — |

**The Approach sits outside the Turn count.** It is the entry choice, made once when the frame opens. A one-round encounter therefore involves choosing an Approach and nothing further — the player commits to a posture and the world answers immediately.

### 25.2 Approaches

**ARTWORK — A Contested Encounter**

**An encounter is not automatically a fight.** Combat is only one response; others include display, evasion, bribery, negotiation, trickery, surrendering part of the haul, rescue, and withdrawal. These are **player choices, made before the first round.**

Five Approaches:

| Approach | The party… | Tests | Baseline exposure |
|---|---|---|---|
| **Contest** | Meets it directly — fights, or displays hard enough to drive it off. | Resilience and fight | **High**, party-wide |
| **Evade** | Slips past, around, or beneath. | Stealth and movement | **Low** — but a failed Evade spikes it |
| **Parley** | Talks, warns, bargains, deceives, or bribes. | Social aptitude | **Low** overall, **high for whoever speaks** |
| **Yield** | Gives up part of the haul to end it. | Nothing — no roll | **Minimal** |
| **Withdraw** | Leaves. Node unresolved. | Nothing — no roll | **Minimal** |

- **Trickery folds into Parley.** Deception is a social act; a separate Approach would fragment the set without adding a decision.
- **Rescue is not an Approach.** It is a Turn action, because it is always a response to something that just happened.
- **Withdraw and Yield are always available.** The player can always leave, and can always buy their way out if carrying anything. **Neither is ever removed** — not by an adversary, not by a Guest, not by an encounter type.
- **The other three vary** by encounter and by party. Weasels holding a culvert do not Parley. A sealed container cannot be Contested. This variance is where Guests earn their keep (Section 20.1).

**Information rule.** Which Approaches are *available* is visible before choosing. How hard each will be is **not** — consistent with the prohibition on disclosing contest status or odds (Section 27.2). The player sees that Parley is on the table; they do not see that these weasels are unusually hungry.

### 25.3 The group layer — mass, never a roster

**The adversary is a Presence, not a count.** MEDIAN never needs to know how many weasels. The fiction says *"a pair of weasels hold the culvert"* and the number stays flavor, permanently and by design.

An encounter carries a **Presence value per available Approach.** The same weasels are formidable against Contest, moderate against Evade, and simply unavailable to Parley. This is what makes Approach a real decision rather than a reskin.

**Why not pairings.** Individual-versus-individual resolution would require generating adversary rosters, would immediately raise "does a five-mouse party face five weasels," would demand per-citizen encounter state, and would drift toward the tactical combat this design rejects by name (Section 1.2). The legibility it buys is recovered on the back end instead, at no such cost.

### 25.4 Resolution

Conflict of every kind — expedition contest, Base Defense, Road Work onset — resolves through **augmented passive resolution**: a stat comparison, modified, then finalized with a bounded RNG roll. Never in real time, never a twitch test. This is the same engine behind all three; it is not three systems.

**Party Score** = the participating citizens' relevant aptitude for the chosen Approach, summed, plus the **equipment modifier** (Keepsake, Tool, Supply — Section 19), plus Guest contributions, then modified by **terrain**, **weather** (Wind Draft, the River's Spume — Section 9.3), and any **citizen maiming**.

Score is compared to Presence; the margin is shifted by **bounded RNG** — bounded meaning the roll can narrow or widen a result but cannot overturn a large gap. A hopeless Contest stays hopeless.

**Party size scales cleanly and honestly.** More citizens means a higher Party Score *and* more individuals exposed. A real trade-off requiring no bookkeeping.

**The Turn.** A Turn occurs only when a round has landed close. The player then acts **once**, from options drawn only from systems that already exist:

| Option | Effect | Exposure |
|---|---|---|
| **Play a Supply** | Applies a departing citizen's per-run consumable to the next round. | Unchanged |
| **Commit a Rescue** | Sends a citizen to one who is pinned, wounded, or **tharn**. | **Raises rescuer, lowers rescued** |
| **Press** | No intervention. Better group odds next round. | **Raises party-wide** |
| **Withdraw** | Take the partial outcome and go. | **Cuts party-wide** |

Three things the Turn fixes: the **Supply** slot finally appears on screen rather than silently modifying a number; the Launcher's question — *"who do I trust with this?"* — becomes true, because the Turn asks *who goes back for them*; and **bonds form where canon says they form**, since "co-expedition survival, rescue, tharn lead-out" (Section 17.1) are all Turn outcomes.

### 25.5 Exposure — the individual layer

**INFOGRAPHIC — Exposure and Outcomes**

**Exposure is how far a citizen personally stuck their neck out in this encounter.** It is derived from what the player chose, never rolled. It exists only within the encounter, **never displays as a number**, and never accumulates.

**What sets it.** Baseline comes from the Approach (Section 25.2). Then:

- Carrying the heaviest share of the load → **raises**
- Speaking, in a Parley → **raises**
- Committing to a Rescue → **raises the rescuer**, lowers the rescued
- Being pinned, wounded, or tharn → **raises, and keeps rising each round until resolved**
- Using a Guest's signature ability → **raises that Guest** — they are the one who went in
- Each additional round still committed → **raises everyone still in it**
- Withdrawing or Yielding → **cuts everyone**

**How it resolves.** After the final round, each citizen resolves once against their own exposure. The governing principle, stated exactly:

> **Exposure widens the distribution. It does not shift it.**

High exposure does not mean *more likely to be hurt.* It means **more likely that something happened to you at all** — and the tails open in both directions together.

| Exposure | Outcome band |
|---|---|
| **Minimal** | Nothing. The citizen was there; that is all the Record will say. |
| **Moderate** | Shaken, a fear memory, a minor wound. Ordinary consequence. |
| **High** | Both tails open: **Maiming** becomes possible, and so does a **Distinction**. |

This gives the Distinction/Maiming symmetry the **shared driver it never had** (Section 18.3). A citizen who did nothing remarkable gets nothing remarkable, good or bad — not a failure of the system, but the system correctly declining to manufacture drama.

**Group and individual resolution remain independent.** The two are computed separately and neither gates the other. A **Failed** encounter where everyone kept exposure low: the party comes home empty-handed and whole. A **Successful** encounter with one citizen at high exposure: the costly victory, graded **Hard-Earned**.

Individual resolution only fires where genuine danger is present — a contested node, Base Defense, Road Work's onset — never as a background tax on clean, uncontested activity.

*Open:* exposure bands and thresholds, and Presence values per Approach, are deferred numeric tuning (Appendix D).

### 25.6 The outcome distribution

Resolution forms a bell-shaped distribution: most results are ordinary success, compromise, retreat, partial yield, minor fear, or modest wounds; a rare bad tail brings maiming, major loss, capture, separation, or death; a rare good tail brings an exceptional artifact, powerful information, a diplomatic breakthrough, a resource cache, a Guest opportunity, or a **Distinction**.

The engine can use hidden probability, but **the fiction always explains the result.**

### 25.7 The epic case

Encounter length is generated by closeness (Section 25.1), so the "epic" encounter needs no separate mechanism — it is an encounter that refused to resolve twice.

**Length is never rolled for.** It is the one place randomness feels least earned. A free extra round is a gift; a costly one is arbitrary. Closeness is the honest trigger.

**Retained as an override:** a **Special Artifact** or **Tool** may grant an extra Turn outright, inserting a decision where a round would otherwise have resolved cleanly. It cannot breach the three-round cap.

**The exposure interaction is the point.** Every additional round raises exposure for everyone still committed. Therefore **Legendary ratings and Maimings correlate** — the great stories and the terrible ones come out of the same encounters — and **Withdraw gains teeth at the second Turn**, since walking away from a contest you might still win becomes a genuine sacrifice.

### 25.8 Guardrails

This system sits one bad decision away from being a combat game. The following are canon prohibitions:

- **Three rounds is the ceiling.**
- **No positioning, facing, turn order, initiative, or targeting.** The party is one body on the front end; individuality lives on the back end only.
- **Adversaries are never counted.** Presence, never a roster.
- **Never real-time, never a twitch test.**
- **At most two Turns per encounter.** Most encounters have none.
- **Exposure is never displayed as a number and never persists.**
- **Withdraw is never removed.**

### 25.9 What this system does not govern

- **Crossing** (Section 23) is an action mode. No Approaches, no Turns, no exposure.
- **Road Work onset** (Section 10.2) uses the group layer only — a single round, no Approach, no Turn.
- **Base Defense** (Section 26.4) uses the full frame with the *colony* as the party.
- **Choice-Event Cards** (Section 10.3) are a separate system. A card may *lead into* an encounter; it is not one.

---

## 26. Contest, recruitment, and Base Defense

**INFOGRAPHIC — Contest, Recruitment and Base Defense**

### 26.1 What is contested

Contest is revealed only on reaching a node (Section 24.1). Whether a node is contested at all varies with **Biome**, **Outpost status**, and **RNG**.

*Open:* whether the antagonist/non-antagonist split should additionally vary with conditions — season, traffic cycle, recent Road Work, colony reputation-by-story — rather than sitting at a fixed ratio (Appendix D).

### 26.2 The recruitment funnel

1. **Is the node contested?** Determined by the factors above. Most nodes on genuinely wild territory can be; outposted Reaches are calmer.
2. **If contested → 70% antagonist / 30% non-antagonist.** Antagonists are predators, territorial rivals, desperate scavengers, or environmental obstruction. *(This figure is scoped to contested nodes, not to all nodes.)*
3. **If non-antagonist → 30% chance the animal is amenable.** Non-antagonist contacts otherwise mean trade, warning, negotiation, aid, or mutual avoidance.
4. **If amenable → still gated** by the animal's own check plus a resource cost, fluffed as a "residence cost."
5. **Slot cap.** Recruitment is additionally capped by available Guest slots regardless of how often amenable animals appear — a full roster means *passing on* an amenable animal, not auto-recruiting it.

**Two different things come out of this funnel.** An amenable animal of an outside species becomes a **Guest** and occupies a Guest slot. An amenable animal of the colony's *own* species becomes an ordinary **Citizen** and occupies no slot at all (Section 17.4).

**The worked example: the raccoon.** The raccoon is the canonical illustration of the rival who joins. It appears first as antagonist scavenger fauna at contested nodes — bigger and cannier than the Rat, and a real threat. On a later encounter it may fall on the non-antagonist branch, then the amenable branch, and the party may pay the residence cost and bring it home. **The same animal that drove a party off a node last season can be sitting at the Story Circle this one.** Nothing about the funnel changes to accommodate this; the raccoon simply walks through it, which is the point.

### 26.3 Slot scaling and scarcity

Guest slots scale with Colony Tier: **one new slot of each type per Tier reached**, for **four of each at max Tier.** This sits deliberately *below* full roster size — seven Active, nine Ambient — preserving meaningful-choice scarcity. The player never fields the entire roster and must choose.

The first slot of each type is available from founding; it simply has nothing to fill it until the first non-adversarial encounter.

*Open:* Tier graduation is rare, so slots open only four times in a campaign, which risks most amenable-animal encounters meeting a full roster and reading as non-events. Whether Guest capacity should also scale along some lesser dimension — habitat quality, an amicable departure freeing a slot, a temporary visiting Guest — is unresolved (Appendix D).

### 26.4 Base Defense

**ARTWORK — Base Defense**

Base Defense is a distinct context: occasional animal incursions against the home territory, telegraphed by the Watchkeeper Role and the lookout network. It is **occasional, not relentless** — the home is a sanctuary that is sometimes threatened, not a tower-defense arena.

It resolves through the full encounter frame (Section 25) with the **colony** as the party: a telegraphed approach, citizens auto-pathing to a refuge unless the player commits a defender, then resolution.

Incursion types include predators, desperate scavengers, the Rat, and the **raccoon** — the last being both the most capable ordinary incursion and, uniquely, an animal the player may one day recruit.

*Open:* what a successful incursion actually costs. Stolen stores, damaged structures, wounded citizens, a lost Guest, spoiled Perishables — none of this is specified, and Base Defense has no teeth until it is (Appendix D).

---

## 27. Expeditions and the Launcher

**INFOGRAPHIC — Expeditions and the Launcher**

### 27.1 Expedition categories

**Margin Raid.** A short transverse mission from the Home Median to either adjacent Margin, for renewable forage, scrap, discoveries, encounters, and high-frequency advancement needs. A Margin beside a wild, un-outposted Reach can also be raided; it simply lacks Home efficiencies.

**Median Scout.** A longitudinal reconnaissance journey opening an unknown Reach's Field territory **for reconnaissance only** — nothing buildable, nothing permanent. The party learns the Reach's lane count, biome, resources, Anchor Points, and **folk name**, and nothing persists afterward.

**Establish Outpost.** A later expedition: a construction party carrying material returns to a scouted Reach, navigates to its preferred Anchor Point, and resolves that node's contest there. Winning — or an uncontested approach — *secures* the spot; it does **not** complete construction. Securing starts a construction clock, and when it finishes the Reach is claimed.

That clock is explicitly **one instance of the Construction Queue** (Section 14) — a fixed number of whole days, resources sunk at the start, uninterruptible once begun. Its specific duration remains deferred.

**Outpost Visit / Deep Extraction.** Returns to an established outpost's Field territory for active play: secure a large haul, repair facilities, respond to an event, meet a Guest, exploit a temporary opportunity, or push the frontier.

**Special Journey.** A story-specific expedition. Its **primary** purpose is reaching the Rest-Stop Metropolis (Part VI). A **strong secondary** use is revisiting the destroyed ancestral home. Further story-forward destinations remain open as future content.

### 27.2 The Expedition Launcher

The Launcher is character-centered — the question should feel like *"who do I trust with this?"* rather than *"which array has the largest number?"*

It communicates the destination biome type and a partial resource preview, the destination's **folk name** where known, the mission purpose and known route demands, the eligible citizens as portrait cards with qualitative readiness and relevant history, condition and relationship dynamics, known traffic and weather observations, cargo capacity, and past expedition notes and rumors drawn from previous debriefs (Section 21.3).

**The Launcher surfaces exactly one equipment decision per citizen: their Supply** (Section 19). Keepsakes travel automatically; Tools are standing colony-level assignments. Neither appears here. **Avoid a wall of stats.**

It **never** discloses whether a destination will be contested, the exact encounter odds, exact victory percentages, or any hidden math. The player learns through experience, scouting, history, Guests, and environmental signs.

*(The exact specificity of the resource preview is deferred; Appendix D.)*

### 27.3 Early expedition onboarding

- **First major expedition:** a forced, strongly-framed physical confrontation — a "red in tooth and claw" moment teaching that the world is physical and contested and can wound citizens. It is *not* tuned to force permanent maiming every campaign.
- **Second or third expedition:** heavily weighted toward a **Guest recruitment opportunity** — the campaign's "Kehaar moment," where the player meets an outsider as an individual and learns the world contains relationships as well as threats.

---

## 28. Outposts

**INFOGRAPHIC — Outposts**

**ARTWORK — Establishing an Outpost**

Outposts expand the Home Median's reach without becoming replacement towns. The Home remains the population center, civic heart, and sentimental gravity of the campaign; outpost automation protects the game from multi-base micromanagement.

### 28.1 Reach lifecycle and fog of war

A Median Reach moves through three states:

1. **Undiscovered** — not yet scouted; a blank on the corridor map.
2. **Discovered-but-expedition-only** — visitable and raidable through Field Mode, but nothing persists: no building, no passive yield, and the Reach reverts to wild between visits.
3. **Outposted** — a genuine extension of the base-building layer.

**A Reach carries fog of war.** On a Median Scout, the territory reveals itself as the party moves through it — **Anchor Points are not shown immediately**, and the shape of a Reach is learned by walking it. This is what makes scouting an activity rather than a button, and it is the clearest expression of the Field register's "reading territory" purpose.

**Completing an outpost's central building clears that Reach's fog permanently.** The player knows the whole Reach thereafter.

### 28.2 The outpost building set

An outpost is intentionally a light footprint, drawn from a small dedicated set — **never** any of the core Home building catalogue:

- A **central building** that claims the Reach and hosts the outpost's single **Ambient Guest** slot.
- Optional **resource-trickle** outbuildings — a modest passive yield from the local biome.
- Optional **visibility / predator-reduction** outbuildings.
- **One or two Citizen slots.**

An outpost with **two or more citizen slots** can host a **full Hearth relocating together** (Section 17.2) — the intended way a bonded family reaches the frontier.

**Passive effects have a radius smaller than the Reach.** Fog clears everywhere; benefit does not. **Where the outbuildings sit matters**, which keeps outpost construction a spatial decision rather than a checkbox.

*Open:* whether higher-Tier outposts gain optional significance of their own — a unique Tier III or IV outpost building, expanded Citizen or Guest slots, or a distinct role in the corridor network (Appendix D).

### 28.3 Stationing a citizen

A citizen assigned to an outpost is **genuinely stationed there** — unavailable for Home Median work, Margin Raids, or Base Defense until reassigned — in exchange for boosting that outpost's passive trickle and being automatically present for Outpost Visits there. Stationing is not permanent; the citizen is reassignable at need.

Stationed citizens **still count toward the same low-population ceiling** (Section 11). There is no exception that lets total population creep upward. In practice, sending citizens to satellites becomes a natural pressure valve as population climbs at home.

**Hearths cannot be split.** A citizen belonging to a Hearth is **ineligible for solo stationing.** The family either goes together to a two-slot outpost or stays home.

### 28.4 Contest and the value of investment

**Claiming a Reach is not the same as pacifying it.** An outpost's central building claims the **entire Reach** — rewarding exploration for a good, wide strip worth committing to rather than settling the first tile the party reaches — and it clears the fog. But claiming alone does **not** reset the Reach's contest risk.

**Contest falls as the player invests.** It is the **outbuildings** — the visibility and predator-reduction structures in particular — that make a Reach genuinely calmer. A bare outpost is a flag in the soil and little more; a developed one is a place where the corridor has learned not to bother you.

This keeps an outpost a project rather than a purchase, and it means Outpost Visits run safer than wild territory only to the degree the player has earned it.

### 28.5 Active versus passive value

Passive yield is reliable but modest. Visiting an outpost opens its Field territory and can produce greater rewards, special encounters, repairs, rare resources, and story events. The player chooses when the additional attention is worthwhile.

---

# PART VI — THE REST-STOP METROPOLIS

**ARTWORK — The Metropolis at Night**

*The corridor's one city. It gets its own part because it is unlike anything else in the world: the only large settlement, the only genuinely multi-species population, the only place with a history older than the player's, and the only place whose folklore contradicts the colony's own.*

---

## 29. The Metropolis

**INFOGRAPHIC — The Rest-Stop Metropolis**

### 29.1 The place

The **Rest-Stop Metropolis** is a distant, revisit-able multi-species settlement hidden within the neglected ecological and structural margins of a human rest stop.

It should feel extraordinary but plausible: **not a fantasy capital sitting openly beside human foot traffic**, but an urban animal ecosystem distributed among drainage spaces, service voids, dumpster enclosures, embankments, roof edges, vents, and vegetation set back from the main buildings.

Its population is genuinely multi-species and its scale is high — appropriate here in a way it never is at the low-population Home Median.

### 29.2 Presentation — a Field territory with venues as nodes

**ARTWORK — A Venue as a Node**

The Metropolis is surveyed like any other territory (Section 24.4): a top-down plate of drainage runs, service voids, embankments, and roof edges, with **venues as nodes.** Entering the tavern is an Encounter.

Same engine, same rhythm, **no new register.** What differs is what the nodes contain: a fixer's workshop, a specialist crafter, a rumor-monger's corner, a trade floor, the tavern.

**Its encounters lean overwhelmingly on Parley** (Section 25.2), which makes the Metropolis the best showcase in the game for the fact that an encounter is not automatically a fight. A player who has spent forty hours choosing Contest and Evade arrives somewhere that rewards neither.

### 29.3 Core functions

- **Multi-species gathering place:** rumors, relationships, recruitable Guests, returning characters, social story.
- **Trade:** exchange local abundance and rare artifacts for unfamiliar resources or services.
- **Craft and adaptation:** commission specialized tools and accessibility aids beyond the Home workshop's knowledge.
- **Culture and mythology:** corridor legends, ecological memory, warnings, and **competing interpretations of the human world.** Concretely, the Metropolis holds **contradictory Laws of the Median** (Section 6.1) and its own **regional variants** for the highway's name (Section 6.3). The player's colony discovers that its own certainties are local — and, because the colony's Laws are genuinely imperfect (three teenagers' half-memory), some of those contradictions are corrections.
- **Intelligence:** learn about Road Work, routes, biomes, rare opportunities, political tensions.
- **Place names:** the richest source of names for ground the player has not yet walked (Section 22.2).

### 29.4 A founding myth, and what it does not mean

**Raccoons are the Metropolis's historic founding species.** The current population is genuinely multi-species — other species arrived and settled later, and today they are the majority — but raccoons retain outsized **cultural and traditional standing** as a consequence of having been first.

**This is heritage weight, not authority.** All Metropolis species are explicitly equal. There is no raccoon hierarchy, no raccoon rule, no political control, and no faction system attached. Founding priority buys respect and a set of customs, and nothing else. **This guardrail is stated in the text deliberately**, because "founding species" is exactly the kind of lore detail that drifts into politics if left unattended.

Its most concrete expression is a single figure: the multi-species tavern and trade hub at the heart of the Metropolis has a **bartender**, and the bartender is a **Raccoon.** Subtle raccoon-heritage nods in Metropolis architecture and decor are available as a Phase 2 art detail and are not further specified here.

**The myth rhymes with the game's own creative thesis** (Section 1): the Metropolis's founding story is a grander, older echo of the player's own Founding Escape — animals making a permanent home in leftover human space — rather than a copy of it. That resonance is the reason to have it at all.

It creates no conflict with existing canon: raccoons remain barred from being core colony citizens or domestic crafters (Appendix A), and Tier III remains structurally independent of the Metropolis (Section 31).

**The species mix.** Raccoons, plus a broad spread of the three core species and of animals that appear elsewhere as Guests. Core species being present here creates no conflict with the no-cross-recruitment rule (Section 4): that rule governs who joins the player's *colony*, not who exists in the world. The Metropolis is where a rabbit sees squirrels going about their business and cannot recruit a single one of them.

**The central plaza's name is generated, not authored.** It is produced per campaign through the same folk-name grammar as every other place (Section 22.2), which means no two campaigns name it alike and the player learns it from rumor rather than from a map. Any name appearing in supporting material is therefore an example rather than the name.

---

## 30. The Metropolis in the campaign

### 30.1 Campaign role

The Metropolis belongs in the core campaign because the victory arc involves connecting the Home Median to the wider world. **It must not overshadow the base-builder or become the player's new primary town.**

It is the **primary destination of the Special Journey** expedition type (Section 27.1), and it is reached only after a chain of outposts and relationships makes the journey survivable.

### 30.2 Victory and continuation

A campaign's climactic objective is to establish a viable network of outposts and relationships reaching the Metropolis, then complete a **Grand Caravan** or equivalent final expedition proving the corridor connection can endure.

**Victory is an offered conclusion, not forced retirement.** After the climax the player may conclude and read the colony's completed **Chronicle** (Section 21.1), or continue indefinitely in the same world.

Post-victory play focuses on civic beautification, relationships, rare expeditions, long-term ecological events, veteran care, outpost refinement, trade, and the stories of later generations — **not infinite vertical power scaling.**

---

# PART VII — PROGRESSION AND PRESENTATION

**ARTWORK — The Founding Escape**

---

## 31. Progression tiers

**INFOGRAPHIC — Progression Tiers**

The tier system expresses increasing security, spatial reach, institutional capability, and ecological integration. **It is not a ladder toward human-style industrialization.**

**Every Tier graduation grants all citizens a stat bump** — a colony-wide progression event (Section 18.4). Each Tier also opens one new Active Guest slot and one new Ambient Guest slot (Section 26.3), raises the cap on **building upgrade rungs** (Section 15.2), unlocks **building availability** for families that did not previously exist, and adds a **Construction Queue slot** (Section 14).

### Tier I — Scavenger Camp

**Fantasy:** a vulnerable settlement proving it can survive.
**Range:** Home Median and adjacent Margins.
**Capabilities:** basic shelters, food storage, simple repair, Staging Post, first expeditions, the first Guest slot of each type, a single Construction Queue slot.
**Pressures:** exposure, fragile construction, scarce scrap, unknown corridor, fear.

### Tier II — Fortified Settlement

**Fantasy:** the colony is organized, defended, and able to prepare rather than merely react.
**Range:** first longitudinal scouts and one nearby outpost.
**Capabilities:** refined storage, stronger routes, recovery space, better tools, limited food preservation, second Guest slot of each type, additional Construction Queue capacity.
**Pressures:** maintaining the first network, seasonal preparation, contested sites.

*(**Warren, Den, and Burrow are species terminology** — rabbit, squirrel, and mouse respectively — and are never used generically. A tier name shared by all three campaigns cannot borrow one of them.)*

### Tier III — Independent Colony

**Fantasy:** a mature, self-governing home that can endure without external rescue.
**Range:** multiple outposts and deeper biomes.
**Capabilities:** durable anchored construction, outpost logistics, Ambient Guest assignment to outposts, adaptive equipment, advanced Role use, larger expedition choices, third Guest slot of each type, higher building rungs.
**Pressures:** regional relationships, Road Work at multiple nodes, preparing a corridor connection.

**Tier III must not be named for or structurally dependent on the Rest-Stop Metropolis.** The Metropolis's own history and mythology is worldbuilding and creates no dependency here.

### Tier IV — Sovereign Network

**Fantasy:** the Home Median becomes the protected heart of a connected corridor community.
**Range:** a chain reaching the Rest-Stop Metropolis and other distant sites.
**Capabilities:** resilient dead-zone sanctuary spaces, mature outpost routes, trade and intelligence networks, the fourth and final Guest slot of each type, the top rungs of every building ladder, major civic works, grand caravan preparation.
**Pressures:** completing the route, protecting legacy, deciding what the colony will become.

**Tier IV does not electrify the animal settlement or turn it into a tiny human empire.** Mastery means ecological invisibility, resilient routes, social connection, and intelligent use of overlooked infrastructure — and, in the building ladders, scrap-mastery and civic complexity rather than machinery.

### 31.1 Advancement gates

Tier advancement should combine a civic construction milestone at the Home Median, sustained food and shelter capacity, a small amount of Flexible and Rigid Scrap, a demonstrated expedition or network achievement, and — at selected tiers — a believable Special Artifact, relationship, or knowledge requirement.

Avoid arbitrary giant resource sacrifices. Advancement must visibly transform the colony and unlock a new kind of decision.

**Advancement is never gated by Guest recruitment**, which stays fully optional so that a "no Guests ever" run is always valid and never soft-locked.

---

## 32. Interface and information design

**INFOGRAPHIC — Interface and Information Design**

### 32.1 The Colony view

The default view prioritizes the settlement as a living miniature ecosystem. Work routes, storage, structural problems, fear, injury, weather, and congestion should be visually apparent.

**Functional icons are part of the base view.** Every building carries a persistent, always-visible functional symbol regardless of its in-world flavor name (Section 15.3). These are *not* gated behind the ledger overlay: a player who has never opened the overlay can still read the colony at a glance.

**The Construction Queue is visible here**, showing what is being built, what is offline while it is built, and roughly how far along it is — in days, qualitatively presented, with no speed-up affordance because none exists.

**Three distinct hotspots**, each at a different scope:

| Hotspot | Exposure | Scope | Opens |
|---|---|---|---|
| **Community Board** | Ambient — always visible in the world | Operational, day-to-day | Alerts, duties, foraging shares, scout returns, active Choice-Event Cards; the diegetic face of the Almanac feed |
| **Story Circle** | Entered deliberately | Ceremonial, colony-scale | The **Colony Record** — Almanac and Chronicle |
| **Warren / Den / Burrow hub** | Entered deliberately | Personal, citizen-scale | The **Village Roster**, and through it each **Character Record** |

Operational, ceremonial, and personal — three scopes, expressed spatially as well as tonally.

### 32.2 Blueprint / ledger overlay

A toggle or hold input adds precise information for known systems: resource totals, consumption, capacity, and expected reserve duration; building function, durability state, repair need, construction cost, and current queue position; Role assignment and route congestion; healing, nursery, and scheduled-event progress; outpost status and known network flow.

It should **not** reveal hidden citizen ratings, unknown encounters, exact contest probabilities, or future RNG.

The overlay's building-function data is the **text expansion** of the base view's always-visible functional icons, not a substitute for them.

### 32.3 Character Records and the Village Roster

The **Village Roster** is the index screen for the colony's people: every citizen, listed, leading into an individual's **Likeness** and **Tale** (Section 21.2). It is visually skinned as being *at the species hub* — the **Warren**, **Den**, or **Burrow**, using the campaign's actual species-specific hub name and never a generic "Town Center" placeholder.

An individual Record combines portrait, both name fields, descriptive aptitude bands, current condition, bonds and Hearth membership, assigned Role, equipment slots, earned Distinctions and Maimings, and a concise chronological history. The player can understand why a citizen is suitable without seeing raw hidden attributes.

The word **dossier** has no place in the interface. It reads as a file on a stranger, and the whole premise is that these are not strangers.

### 32.4 The Expedition Launcher

Specified in Section 27.2. In interface terms: character-centered, portrait cards, qualitative readiness, exactly one equipment decision per citizen.

### 32.5 Controls and accessibility

The control target is PC and console with controller-first readability at both television and handheld distance.

Required considerations include scalable text and UI, full remapping, pause and time scaling, color-independent signals, directional audio visualization, a reduced-input-speed crossing option, a strategic or assisted crossing alternative if feasible, motion/flash/camera-shake controls, and clear animal silhouettes and condition icons.

---

## 33. Art and audio direction

### 33.1 Visual identity

Grounded stylized realism at animal scale. The world combines soft organic material — fur, grass, roots, mud, bark, feathers — with harsh human infrastructure — wet asphalt, concrete, salt, rust, tire rubber, reflective signs, plastic, drainage metal. The art culture takes *Mouse Guard* as a modern-register touchstone, without its medieval trappings.

The tone is **atmospheric and tactile, not relentlessly grim.** Home scenes may be warm, lively, and gently storybook; expedition scenes become colder, larger, and more cinematic.

Avoid sci-fi interfaces, neon technology, and brushed-metal title treatments that make the animal world feel manufactured. There is no military or mature-rated visual framing.

### On anthropomorphism — the line

The citizens are heavily anthropomorphized as *characters*: they have names, families, grief, folklore, and standing jobs. The question is how much of that reaches their bodies. *Mouse Guard* is the reference and the reference already contains the answer — MEDIAN takes its **small-animal material culture** and refuses its **medieval trappings** (Section 1.1). A cloak is material culture. A sword is a trapping.

**Dress marks leaving home.** At home, citizens wear nothing. Away, they wear a cloak, a belt, and carry a Tool, taking all three up at the Staging Post before a crossing (Section 19). This puts the Sanctuary–Exposure–Return rhythm (Section 1) on the body: an animal's dress says whether it is home or away before anything else does. It is also why the world is not a costume drama — a cloak means something precisely because most citizens most of the time are not wearing one.

**Two things are worn at home as well as away.** A **Keepsake**, which is permanent, personal, and the citizen's always-on identifier — a bead, a scrap of ribbon, a bottlecap on a cord. And **adaptive equipment** (Section 18.1), because a maimed citizen is visibly maimed at home; that is the whole of Pillar 2.5, and it would vanish if impairment only showed on expeditions.

**Cloth is found, never dyed.** Colony material culture is scavenged (Section 13), and scavenged fabric carries the colors of the roadside: high-visibility orange, safety-vest yellow, sign green and white, tarp blue, burlap, plastic, retread black. This does the work a single-species colony needs — every citizen is the same animal, so cloth is what tells them apart — while stating the setting in the same stroke.

**Posture is naturalistic.** Citizens sit up on their haunches to work with their forepaws and drop to all fours to travel, as all three species genuinely do. They do not stand and walk as small people. Full bipedalism would cost the Crossing its terror: an animal low to the asphalt is far more vulnerable than a little person running, and it would drift toward the miniature-humans fantasy this design excludes by name (Section 1.2).

**Role is never worn.** There is no uniform, badge, or livery marking a citizen's standing Role. Role reads from **activity and place** — assignments produce visible work (Section 12), and every building carries a functional icon (Section 15.3), so a Healer is a citizen working at a building marked for healing. Cloth stays free to carry individual identity rather than job function.

**Never depicted:** weapons of any kind · armor, including bracers and any cross-body strap, which reads as a weapon harness whether or not it carries one · forged metal · helmets, uniforms, livery · animals dressed as miniature people. The equipment slot is named **Tool** and never "Weapon" for exactly this reason (Section 19).

**Expression sits in ears and posture first.** Rodent facial musculature is limited and pushing a face past it tips into cartoon. Ears are enormously expressive on all three species and cost nothing. This matters mechanically as well as tonally: fear must be visible in the world as a frightened posture (Pillar 2.3), and tharn must read through more than an icon (Section 33.3).

**Escalation without industry.** Dress quality tracks Colony Tier — torn bag strip at Tier I, selected and cleaned and well-stitched scrap by Tier IV — on exactly the principle governing the building ladders (Section 15.2): grandeur through scrap-mastery, never through machinery.

*Guests are treated differently and wear less; see Section 20.4.*

**Wordmark and logomark (concept direction, adopted).** The MEDIAN title is rendered with a **cracked-asphalt and shattered-glass letterfill**, accompanied by a companion **"//" logomark** styled as **mossy concrete lane-marking relief** — a candidate app and loading icon, and a quiet piece of wordplay, since a median is precisely the thing that sits between two lane markings.

Both are built entirely from the material vocabulary already established, which makes this a *positive* instance of the same instinct behind the brushed-metal warning rather than a violation of it: the title treatment is made of the world instead of imported from a hardware catalogue. **Concept direction only**; production belongs to Phase 2, and must be delivered with **layered, editable text** rather than flattened.

### 33.2 Scale language and vehicle presence

**INFOGRAPHIC — Scale Language**

Scale should be communicated through recognizable infrastructure and material texture: lane paint, tire fragments, guardrail bolts, culvert mouths, drainage grates, barrier seams, distant vehicle mass. Cars should not intrude impossibly close to safe colony compositions.

**Vehicle and machine flavor belongs throughout the world, not only on the road.** The corridor is littered with the remains of what passes along it, and biomes should carry that: a wrecked car under an interchange, an engine block half-swallowed by grass, a rusted piece of abandoned construction equipment, retread tire fragments, bumper shards, a hubcap. In the Margin, a wreck can be a **node** in its own right. This is how the world states its scale contrast without ever showing a human.

**Human bodies never appear. There is no exception.** The Giants live in folklore, spoken about and never depicted (Section 6.3).

Machinery without a visible operator reads as indifferent force rather than intent — which is precisely what Section 10.2 already demands of it, something evaded or sheltered from and **never negotiated with**. An operator invites appeal. The absence of one is the horror, and it is also the more accurate account of what the corridor actually is to the animals living in it: not malice, but weather with a schedule.

This rule was only ever about human bodies. **Vehicles are unaffected** — Roaring Iron is visible constantly and by design, and machinery at work is visible in full.

**Catastrophe is sensory-obscured.** Destruction and death are conveyed through dust, noise, vibration, distance, and narrowed perception rather than depicted. There is no explicit blood or gore. This is the same presentation vocabulary used for tharn (Section 33.3), which means the Founding Escape teaches the player how catastrophe *reads* in this game before tharn ever fires on a citizen.

### 33.3 Audio

**INFOGRAPHIC — Art and Audio Style Guide**

Audio is systemic. Traffic density and vehicle approach must be learnable by sound; large vehicles produce low-frequency vibration and wind pressure; night crossings use directional audio without becoming inaccessible.

Home has species-specific movement, construction, conversation, weather-shelter, and domestic rhythms.

**Tharn is communicated through narrowed sound, breath, pulse, and overwhelming threat** — not only a UI icon.

Road Work's persistence window has its own distinct soundscape. The River's Spume has its own continuous ambient bed, shifting texture with season and traffic cycle (Section 9.3).

Adaptive devices and lasting injuries may alter movement sound respectfully and consistently.

---

## 34. The optional generative layer

> **IMAGEGEN — summary.** Everything in this section is a **game-designer-optional modular add-on.** It is not a dependency of the core game and not necessarily a player-facing option in the first design pass. **The base game must be complete, coherent, and emotionally effective without any of it.** Every trigger below has a mandatory non-generative fallback using standard art, text, and recorded game state. Nothing in this section may become load-bearing.

The layer has four applications and one ownership policy.

> **IMAGEGEN — evolving canonical portraits.** Each citizen has a canonical image and structured textual description. A permanent visible change updates the record with factual deltas and, through image-to-image generation, creates a revised canonical portrait. Continuity of identity, species anatomy, orientation, existing scars, and the citizen's randomized physical quirk is essential. The structured description this reads from **is** the citizen's Character Record (Section 21.2) — one record, two outputs.
> *Fallback:* the canonical portrait simply does not change; the Record carries the factual change in words.

> **IMAGEGEN — expedition splash images.** Selected high-value moments — first contest, rare encounter, Guest recruitment, major victory, a Distinction earned, catastrophic Road Work — can produce a cinematic loading-screen-style image using the actual participants, conditions, and location. Because an After-name is granted by a citizen's first Distinction (Section 22.1), the naming moment is already covered by this trigger and needs no separate subsystem.
> *Fallback:* the moment is written into the Tale regardless.

> **IMAGEGEN — settlement milestone images.** At Tier advancement or civic milestones — including outpost completion — the system interprets the actual layout and produces a ground-level storybook view of the player's settlement.
> *Fallback:* a standard illustrated milestone card.

> **IMAGEGEN — Chronicle and Tale illustration.** The Records' literary views can carry generated illustration alongside generated prose.
> *Fallback — mandatory and load-bearing:* the Chronicle and every Tale must read as complete, factual, templated prose assembled from recorded events with no model involved at all. Stylized mythic-register prose and accompanying imagery are the *enhanced* layer. **A player who never enables this system still gets their colony's whole history in words.**

> **IMAGEGEN — ownership and evaluation.** Generated images become available as exportable PNGs or a campaign scrapbook. Cost, latency, moderation, privacy, API authentication, service continuity, reproducibility, and save-file portability must be evaluated separately.

*(In a future full GDD these blocks become sidebars. They are marked inline here so the optional layer is never mistaken for core specification.)*

---

## 35. Campaign onboarding

### 35.1 The Founding Escape

**INFOGRAPHIC — The Founding Escape and Onboarding**

Every campaign opens with **The Founding Escape.** The player's chosen species is first shown at its most developed — a grand, mature ancestral home that also previews the endgame the player can build toward.

**The opening is an establishing tracking shot.** Play begins by passively observing that home in motion: a camera move through a working colony, passing **one room per structure family** (Section 15.1), so the opening doubles as a visual table of contents for everything the player will spend the campaign reconstructing.

**The Laws run as ambient audio across the whole move.** A Teacher is drilling the young in the nursery — call-and-response, carrying through the halls — and the player hears the Laws as *the sound of a working home* rather than as a lesson delivered at them.

**The camera settles on the three.** The founding trio are **adolescents, not the children being drilled.** They are elsewhere: out at a peripheral storage room on the colony's outskirts.

**The first mechanical action is a modified Choice-Event Card.** It asks what to do with a free afternoon, and offers a **responsible** option and a **naughty** one — both diegetically situated at the outskirts, so the trio's survival is explained either way. This **replaces the older "survival odds are invisibly weighted" designer's fudge with an in-fiction cause the player participated in.** The card is *modified* in that it carries **no costed resource response** — the colony's resources are not the player's yet — so its options are social rather than economic, leaving the full Choice-Event Card system its proper introduction later.

The choice sets the **early tonal register.** It does not grant the player granular authorship of the trio's personalities: **the system writes their characterization and the player reads it**, because granular trait authorship offered once and never again would be a false promise about the shape of the game. The randomized-personality-trait rule (Section 17.2) is intact — the player picks a vibe, the system rolls within it.

**Then the machines come.** One of the three has been mockingly reciting the Second Law — *"the mowing is fire"* — to needle the others about being made to memorize it. And then it is true.

**Casualties: there are no survivors but the three.** The Teacher dies. The nursery dies. The ancestral colony is total. Consequences that run the length of the campaign:

- The trio carry the Laws **imperfectly** — what three teenagers half-remembered (Section 6.1).
- The colony's **first assignment of the Teacher Role** is a real event: someone has to become the Teacher now.
- The Metropolis's contradictory Laws have teeth, because some of them are corrections (Section 29.3).
- A **wandering joiner** may one day prove the trio wrong about being alone (Section 17.4).

**The loss is never depicted.** It is sensory-obscured — dust, noise, distance, narrowed perception — and known **by absence**: the trio come back and there is nothing (Section 33.2).

**The played sequence.** The escape is played, not shown, and it moves through every register in turn:

> **Cutscene** → **Encounter** → **Field Mode** (the ancestral Reach, crossed on foot toward the highway boundary) → **Crossing** → *(Field/Crossing repeating two or three times, each iteration compressing toward montage)* → **"time passes"** → arrival at an unfamiliar median → the line — *"the air smells good here"* — → **Town Center placement.**

This trains all four registers in order and earns the distance between the ancestral home and the new colony: they flee long and far, and the home the player builds is genuinely far from the one they lost.

The **repeated crossings are the diegetic tutorial** for Return Logic's 10% forced manual re-crossing (Section 23.2) — the player learns a crossing can recur unbidden before the system ever does it to them.

**"The air smells good here" becomes the colony's first original Saying** (Section 6.2), entering the Chronicle at the exact moment the Records begin.

*Open:* whether the Encounter Screen belongs second, as a tension curve opening at peak and decompressing, or third, as escalating complexity — encounters being the most systemically dense register and the least intuitive cold (Appendix D).

**Scope: the Founding Escape is not an instance of the Mowing.** The Mowing is cyclical, evadable, and survivable — the median is damaged and then recovers. The Founding Escape is a **singular, permanent apocalypse**: a new overpass construction that annihilates the ancestral median entirely and leaves a permanent hazardous construction zone. **Nothing grows back.** Road Work is its recurring *echo* — the same class of machinery, returning — and never the same event at smaller scale.

**Build the ancestral home as the ruin map first**, seen intact exactly once. It is revisitable via Special Journey (Section 27.1).

**Its in-fiction name is the Founding Escape**, and the home it took is the **Ancestral Warren, Den, or Burrow** according to the campaign's species (Section 6.3).

Each founding citizen may begin with a **Keepsake** carried out of the old home (Section 19).

### 35.2 Tutorial sequence

The tutorial teaches emotional priorities before revealing the full system:

1. **Find sanctuary:** begin with the founding group in a damaged but promising Home Median.
2. **Feed the group:** gather nearby sustenance and watch it move physically into storage — **taught as a low-stakes Field run on home ground** (Section 24.4), which is where Field Mode is introduced, safely.
3. **Build the first civic structure:** establish shelter or a communal center, introduce the Colony register — and **name the colony**, choosing one of three generated names at the new welcome sign (Section 22.3). This is the only name the player will ever author, and placing it as the first civic act makes founding feel like founding.
4. **Recognize a progression need:** a repair or construction problem requires material not available safely at home.
5. **Stage the first crossing:** read traffic, select citizens, make the Home-to-Margin run. The First Law surfaces here. **The Margin Field run reads as the same activity as step 2, across the road** — which is exactly what it is.
6. **Face the world:** resolve an early physical contest that can wound and frighten without scripting an unavoidable permanent mutilation (Section 27.3).
7. **Meet an outsider:** weight the second or third expedition toward a Guest encounter, establishing social possibility.
8. **See the corridor:** reveal the longitudinal median chain and the first Median Scout target, with its folk name.

The founding setup always matches the selected core species; the game does not always begin with a lone mouse.

---

# PART VIII — PRODUCTION NOTES

> **This part is suggestions, not canon.** Everything in Sections 36 and 37 is a recommendation about *how to build and evaluate* MEDIAN, offered to be argued with. Where the rest of this document states what the game *is*, this part states what a team might reasonably *do* — and a team that finds a better order of operations should take it. Section 38 is the exception: the canonical summary is canon.

---

## 36. Suggested scope and roadmap

### 36.1 A suggested vertical slice

A persuasive prototype would probably want to prove that:

- one species — rabbits or mice are likely easiest — can build a visually readable small colony in one Home Median;
- named citizens create attachment through work, fear, wounds, Distinctions, history, and relationships;
- the outbound crossing is tense, fair, and replayable;
- one Field territory supports renewable extraction, a Road Work reset, and legible traversal at the naturalist-plate register;
- one contested Encounter supports at least Contest, Parley, and Withdraw, with a Turn and an exposure resolution;
- expedition consequences visibly return to the colony **as written Record entries the player actually reads.**

**The Records' non-generative layer probably belongs in the slice**, because "consequences return to the colony" is difficult to demonstrate without it.

It would likely be wise *not* to prototype the Metropolis, the full season cycle, every Guest, all three species, or generative imagery before this loop works.

### 36.2 A suggested V1 target

- Three core species on one shared system architecture.
- Four advancement tiers.
- Several Home Median seeds and a modest chain of distinct remote biomes.
- Margin Raids, Median Scouts, Establish Outpost, Outpost Visits, and Special Journeys — all reusing Field Mode.
- Traffic, traffic-as-weather with its named hazards, seasons, and Road Work.
- The Construction Queue across new builds, upgrades, and outpost securing.
- Choice-Event Cards in both homes.
- The full encounter model: Approaches, Turns, exposure, extended encounters.
- The Records — Almanac, Chronicle, Likeness, Tale — fully functional without any generative layer.
- The folklore layer: Laws, Sayings, the Giants vocabulary, and both naming systems.
- Low-population citizen life cycle: bonds, Hearths, Nesting Season, wanderers, fear, wounds, maiming, Distinctions, After-names, adaptation, death, and memorials.
- A curated Guest roster across Active and Ambient tiers.
- Rest-Stop Metropolis and a final connection/caravan arc.
- Endless continuation after victory.
- Strong non-generative presentation throughout.

### 36.3 A suggested approach to world events

Rare world-event set-pieces — a multi-vehicle pileup, a mass bird migration, a returning road-construction threat — are probably best implemented **not as new standalone systems** but as rare custom expedition modes that visually and resource-wise **reskin the existing Field and Encounter registers**, reusing infrastructure in keeping with Pillar 2.6. They would be bespoke drama on the scale of once or twice per campaign, not a recurring raid rhythm.

Smaller world events can ride the **Choice-Event Card** system instead — the layer between "ordinary day" and "once-a-campaign set-piece."

### 36.4 Suggested later expansion candidates

More biomes, Rest Stops, Guests, event chains, and infrastructure types; a playable Metropolis-focused campaign with different constraints; additional story-forward Special Journey destinations; expanded folklore pools and place-name banks.

Rival organized civilizations only if localized encounter and diplomacy systems prove insufficient — adding fully-simulated distant AI colony economies by default seems unwise. Optional generative portrait, expedition, settlement, and Chronicle imagery after the base game is stable. A playable raccoon campaign remains a *possible* DLC only.

---

## 37. Suggested prototype success criteria

The concept is probably working when players:

- refer to citizens by name without prompting;
- spend time improving the Home Median even when a purely optimal layout is available;
- understand colony problems by looking, then use the ledger to confirm rather than to discover;
- want to launch expeditions for both progression and character story;
- experience the outbound crossing as tense but fair;
- find Field traversal worthwhile even on an uncontested trip;
- accept wounds and changed plans without immediately reloading every failure;
- continue valuing a maimed citizen and find a meaningful adapted role for them;
- recognize the Margin, Highway, Median, and longitudinal chain without explanation;
- feel relief on returning home;
- choose to keep living in the colony after the formal campaign victory.

Two criteria specific to MEDIAN's own systems: players should **read the Chronicle voluntarily** rather than treating it as a menu, and should **quote the Laws of the Median back at the game** — using folklore as shorthand for mechanics, which is the surest sign the tutorialization-as-culture approach landed.

---

## 38. One-paragraph canonical summary

MEDIAN is a single-player PC and console animal colony builder — a base-builder first, in the spirit of "Age of Empires, minus combat, with the heart of *Watership Down*" — set on the green islands between active highways. The player chooses rabbits, squirrels, or wood mice and, after a Founding Escape from a home destroyed by road construction, builds a permanent, low-population colony — the one thing they will ever name — whose named citizens forage, construct under standing Roles, form bonds and Hearths, take in wanderers, suffer fear and tharn, heal from wounds, adapt to permanent maiming, earn Distinctions and the After-names that come with them, and accumulate personal histories in the Records. All individual growth is earned in the field and never at home. The game presents itself in four registers — an inhabited Colony, a surveyed Field, a rendered Encounter, and an immediate Crossing — and that sequence enacts its emotional rhythm of sanctuary, exposure, and return before any mechanic does. Local ecology sustains life, but advancement requires expeditions: cross the traffic, its danger set by lane count, to the renewable and never-buildable Margin, or travel the corridor of Median Reaches to scout, establish Reach-claiming outposts, meet contested factions and rare Guest Citizens, and extend the colony's range. Encounters resolve in one to three rounds through a chosen Approach — Contest, Evade, Parley, Yield, or Withdraw — against an adversary presence rather than a counted roster, while each citizen's individual fate is set by exposure, which widens the distribution in both directions so that the animal who stuck their neck out is the one who comes home changed. Traffic behaves like weather, expressed as Wind Draft, the River's Spume, and Litter, richest and most dangerous at the same edge; Road Work reshapes the ecosystem, tilts the event deck, and echoes the Founding Escape; a Construction Queue keeps the colony's plans certain while risk stays in the field. The animals carry their own folklore — the Laws of the Median, the Sayings, and their own words for the Giants and the Rivers of Thunder — which teaches the game's systems from inside the fiction and gives the colony's Chronicle its voice. Four progression tiers transform a vulnerable camp into a resilient sovereign network without turning animals into miniature industrial humans. The campaign culminates in a durable connection to the distant Rest-Stop Metropolis and a Grand Caravan, after which the player may conclude the colony's Chronicle or continue indefinitely. Optional AI-generated portraits, illustrations, and milestone images can commemorate the actual citizens and settlement, but the game is designed to stand completely without them.

---

# APPENDICES

---

## Appendix A — Canonical decisions and explicit exclusions

A reference checklist. Everything here is stated in the body; this appendix exists so a contributor can check a proposal against settled canon without rereading the document.

**Genre and framing**

- Base-builder first, with resolution-based expedition action as its paired risk system. No tactical-extraction or combat-first framing. No TEEN/MATURE or military tone.
- *Watership Down* is the primary dramaturgical inspiration; *Mouse Guard* is an art reference only; Age of Empires governs colony-mechanics structure; Final Fantasy Tactics is a presentation reference only.
- **No real *Watership Down* proper nouns appear in MEDIAN's fiction.** All in-world folklore, sayings, place names, and citizen names are original. Sayings are anonymous or attributed to invented in-world figures.

**Presentation**

- **Four registers — Colony, Field, Encounter, Crossing — and no fifth may be added.**
- Field Mode is illustrated and surveyed, **not** schematic; it is further out and more abstract than Colony, not "more immediate."
- Spatial fidelity: the Colony and Field presentations of the same ground are the same place.
- Traffic is never off-screen in any register. No transition is a load screen.
- **No explicit blood or gore.** Catastrophe is sensory-obscured.
- **No human body is ever depicted, anywhere, without exception.** Vehicles and machinery are visible constantly.
- **Dress marks leaving home.** Citizens are bare at home and take up cloak, belt and Tool at the Staging Post. Keepsakes and adaptive equipment are worn always. Cloth color is scavenged, never dyed. Posture is naturalistic — upright to work, four-legged to travel. **Role is never worn.**
- **Nothing may read as arming a citizen** — no weapons, no armor, no bracers, no cross-body straps, no forged metal, no uniforms.

**World**

- The Home Median remains permanent; expansion uses outposts and a corridor network rather than migration.
- Geography is **Sound Wall / Margin / Highway / Median / Highway / Margin / Sound Wall.** The colony lives in the Median. The Margin is **never buildable.**
- The corridor segment term is **Median Reach** ("Median Zone" retired). Highway danger is governed by **lane count**, independent of biome.
- **Each Reach is unified and never internally sub-divided**; adjacent Reaches may differ more sharply than real geography would allow. A deliberate legibility convention, not an error to correct.
- **Richness and danger share one gradient** — the Edge Effect — both peaking at the highway edge.
- **Animals can read.** No in-world text needs a diegetic-legibility caveat.

**Expeditions and risk**

- Contest is hidden until a node is reached. Expedition risk and citizen attributes are never shown as exact percentages; known colony economics and construction state do have clear numerical ledger support.
- **One expedition per citizen per day.**
- **No numeric countdowns anywhere in the event system.** Every telegraph is qualitative and diegetic.
- **Construction is certain and uninterruptible; risk lives in expeditions.** Resources sunk at the start, buildings offline while worked on, and **no Speed-Up mechanic of any kind.**
- **Encounters run at most three rounds and carry at most two Turns.** No positioning, facing, initiative, or targeting. Adversaries are a Presence, never a counted roster. **Withdraw is never removed.**
- **Exposure never displays as a number and never persists** past an encounter.
- Claiming a Reach clears its fog; **only investment in outbuildings reduces its contest risk.**

**Citizens**

- **Low population, every member known by name**, across all three species. **No anonymous sacrificial swarm** and **no pheromone macro-swarm.**
- Wounds heal; **maiming persists but does not erase a citizen's value.** Distinctions mirror maiming as the rare good tail, and **both are driven by exposure.** **Tharn** is a central fear state available to all three species.
- **No genetics, heredity, bloodline ledger, skill trees, or breeding-optimization.** Every citizen gets a randomized personality trait at birth. **A Hearth acquires descent as a story fact only** — "born of [Hearth]" carries no mechanical inheritance whatsoever.
- All citizen development happens through **expedition participation only**; the base-building layer never levels anyone. Domestic **Roles** have fixed output. A separate **Tier-graduation stat bump** applies colony-wide.
- Citizens have **three equipment slots — Keepsake, Tool, Supply.** The slot is named **Tool** and never "Weapon."
- **"Dossier" is retired** in favor of the Character Record, shown as a Likeness and a Tale.
- **All shared stats are integers.** No fractional species values.

**Naming**

- **The player names exactly one thing: the Home colony** — by picking one of three generated candidates with unlimited rerolls. **There is no free-text naming anywhere in the game.** The name is permanent.
- The Home *Median* is a Reach and receives its own generated folk name, distinct from the colony's name.
- All other names are generated, discovered, or earned: places by the world and by history, citizens by a Given Name at inception and an **After-name** at first Distinction.
- **Warren, Den, and Burrow are species terminology** — rabbit, squirrel, mouse — and are never used generically, including at tier level.

**Guests and other species**

- The core species **never cross-recruit.** Found-family flavor lives in the **Guest** system. Guest tiers are **Active** and **Ambient.** The **Rat is antagonist fauna only,** never a citizen.
- Guest accommodation is the **Guest House** — one building family, skin and placement varying by occupant. **Guests wear less than core citizens and most wear nothing**, a difference in depiction only; every Guest is a full equal-status named citizen.
- **Active Guests are option-openers, not stat sticks**: each opens at least one Approach or Turn action and closes or complicates at least one.
- Guest slots scale one-per-Tier-per-type, capped below full roster — seven Active against four slots.
- Same-species **wanderers join as ordinary Citizens**, occupying no Guest slot.
- The **raccoon** is canon as a Guest, an antagonist, and a Metropolis figure. It is **never a core colony citizen and never a domestic crafter.** A playable raccoon campaign is a possible future DLC only.

**Systems restraint**

- **Population-per-Upkeep is not a separate stat.**
- **No new tracked stats.** Reputation, Knowledge, and Visitors-Helped are each explicitly rejected.
- **The Records introduce no currency.** No Knowledge resource, no Story resource, no sharing bonus.
- Optional generative imagery and prose are modular and nonessential; **every trigger has a mandatory non-generative fallback.** Full distant rival-civilization simulation is dropped; localized contested factions remain.

**Metropolis**

- Part of V1 and supports the campaign climax, but is not a replacement home. **Tier III does not name-check or require the Metropolis.** Victory can transition into endless play. **Electricity is not the endpoint of progression.**
- Raccoons are the Metropolis's **historic founding species**, carrying **cultural standing only — never political control and never a hierarchy.** All Metropolis species are equal.

---

## Appendix B — Document history and superseded material

*This appendix exists so the body of the document can describe the game as it currently stands, without narrating its own revision history. Nothing here is canon; it is a record of what was considered and set aside.*

**Version lineage.** v0.1 was the original concept document. v0.2 was a design conversation, since superseded. v0.3 was a canonical-context draft. **v0.4** consolidated all three into one document governed by a settled record of 66 decisions. **v0.4.1** folded in a completed review of the v0.4 Infographic Analysis plus the Decision 67 raccoon material, reaching 72 decisions. **v0.4.2** restructured the document, added the encounter and mode specifications, and reached 85 decisions. **v0.4.3** — this edition — folds in eight decisions from the Phase 2 art production pass and reaches 93.

**Dropped inspirations.** Earlier brainstorming referenced S.T.A.L.K.E.R., Subnautica, *The Secret of NIMH*, and Pikmin. None are inspirations for this game.

**Superseded terminology.** "Median Zone" → Median Reach. "Dossier" → Character Record. "Expedition Guests" → Active Guests. "Fortified Warren" → Fortified Settlement. "Agnomen" → After-name in-world, agnomen retained as the designer-facing term. "Sentimental base-building" → Attachment-first base-building.

**Superseded mechanics and figures.** An 80/10/10 return-logic split, replaced by 70/20/10. A fourth shared stat, "Population-per-Upkeep," never required. A "pheromone macro-swarm" mouse mechanic. Continuous passive action-mode skill growth. A v0.1 line pairing every maiming with "a small compensating trait." A rat citizen art asset named "Grist," which should have been a mouse. A construction Speed-Up. A post-expedition sharing bonus. Two competing names per place. A buried free-text colony-naming option. Intra-median sub-zones. Chemical Runoff and Invasive Plants as separate named hazards. A front-matter description of Field Mode as "a more immediate traversable view," reversed in v0.4.2.

**Rejected on record, with reasons.** As names for **Roaring Iron** (Section 6.3): *Beasts* — an animal does not find "beast" pejorative, so it fails to convey otherness at all; *Growler* — unavoidable beer connotation; *Shells* — too passive for something that kills by momentum; and *Dragons* — an excellent image-match, headlights as fire-eyes and exhaust as smoke, but a borrowed high-fantasy creature noun, failing the same test as borrowing a *Watership Down* name. Keep the imagery, drop the genre word. As names for **the Founding Escape** (Sections 6.3, 35.1), all considered and none adopted before the plain term was kept: *The Widening*, *The Unmaking*, *The Breaking*, *The Uprooting*, *The Flattening*, *The Overturning*. Reputation, Knowledge, and Visitors-Helped as tracked stats. A Deer Mouse Guest. Roadside-PSA signage flavor. Individual-versus-individual encounter pairing. A low-probability roll as the trigger for extended encounters. Granular player authorship of the founding trio's personality traits.

**Reclassified.** The infographic-era "Raccoon Workshop" tinkerer depiction remains drift; raccoon as Guest, antagonist, and Metropolis figure is canon.

**Superseded in v0.4.3.** The **human-figure exception** in Section 33.2, which permitted human bodies during Road Work and Founding-Escape-class threats — closed, no exception now stands. The **placeholder status of the Founding Escape's name**. The characterization of **Guest accommodation as bespoke per-Guest architecture**, replaced by one Guest House family with varying skin and placement. And a **generic "Staging Post"** with no function beyond geography.

**Rejected on record in v0.4.3.** A **worn Role signifier** — badge, cord, or colored tie marking each of the eight Roles. Rejected as a new visual system where two existing ones already carry it: work is visible (Section 12), and buildings carry functional icons (Section 15.3). Also **dyed cloth**, in favor of scavenged color, and **full bipedalism**, which would cost the Crossing its terror.

---

## Appendix C — Change record

### v0.4.4 — the document-history pass

No new decisions, no changed rules, no restructuring. **The decision count stands at 93.**

A single editorial sweep across all thirty-eight sections, removing passages in which the document argued with its own earlier drafts. The governing rule: **a reader should not be able to tell from the body what previous versions said.** Rationale, negation and revision-history belong in Appendix B.

Twenty-six passages were removed or restated. The pattern took four forms:

| Form | Example removed | Handling |
|---|---|---|
| **Explicit negation of a prior draft** | *"The rejected 'pheromone macro-swarm' concept is not canonical"* · *"The old v0.1 line pairing every maiming with a small compensating trait is deliberately not pursued"* | **Cut.** The positive statement already stood beside it |
| **Rules phrased as rebuttals** | *"There is no cross-recruitment among the core species at any point"* · *"'Population-per-Upkeep' is not a separate stat"* | **Restated as rules.** → *"Each campaign is one species, for its whole length"* · *"Three dials, and no more"* |
| **Terminology archaeology** | *"the term 'Median Zone' is retired"* · *"This tier was formerly 'Fortified Warren'"* · *"The term 'dossier' is retired"* | **Cut.** The current term needs no predecessor |
| **Editorial voice addressing the reader** | *"Species is not a chapter a reader can skip… It is stated here, early, because…"* | **Cut.** Instructions on how to read the document are not part of the game |

**Nothing was lost.** Material with standing value moved to Appendix B rather than being deleted — most substantially the reasoning behind the rejected names for Roaring Iron, and the six candidates considered for the Founding Escape, both of which now sit in *Rejected on record, with reasons* in fuller form than they held in the body.

**One deliberate exception.** Part VIII retains its framing note that it is suggestion rather than canon. That is structural signposting telling a reader how to weigh what follows, not an argument with a previous draft.

#### Art markers threaded through the body

The same edition threads **sixty-six placement markers** through the body — forty-four **INFOGRAPHIC** lines and twenty-two **ARTWORK** lines — locating every planned plate and full-page image at the section it illustrates.

These are production notes and carry no canon weight. They exist so that the document and its illustration programme stay in one place rather than in two, and so that a section's art can be judged against the text it sits beside rather than against a list.

**Placement follows three rules.** Each of Parts I through VII opens on a full-page image chosen to state that part's argument before a word of it is read. Plates sit at the section whose system they document. Artwork sits at the passage it depicts, which is not always the same place — the Squirrel Cache Network is marked at §4.3 where the system is described, while the rabbit warren opens Part III as the colony's own image.

**Two things are deliberately unmarked.** Spot illustrations, which attach to body text throughout and are built from the offcuts of larger pieces; and the book's closing part, *Stories of Survival*, which has no counterpart section here because it is a structure of the book rather than of the design.

### v0.4.3 — the art direction edition

A surgical edition. No structural change, no new systems. Eight decisions (86–93), all arising from the Phase 2 art production pass, and **four Appendix D items closed.**

| # | Decision |
|---|---|
| **86** | **The anthropomorphism line** — dress marks leaving home; Keepsake and adaptive equipment worn always; scavenged color, never dyed; naturalistic posture; Role never worn |
| **87** | **No human body is ever depicted** — the Section 33.2 exception is closed |
| **88** | **The Founding Escape** is the event's in-fiction name; the home it took is the **Ancestral Warren / Den / Burrow** |
| **89** | **The Guest House** — one building family, skin and placement varying by occupant |
| **90** | **Warren Flow's readable signature is multiplicity** — many bolt holes, one of them distant, visible in the Field layer |
| **91** | **The Staging Post is the departure threshold** — where Tools live and where a party dresses for the road |
| **92** | **The Metropolis** — species mix specified; the central plaza's name is generated per campaign, not authored |
| **93** | **Guests wear less than core citizens**, a difference in depiction only |

**Closed from Appendix D:** the anthropomorphism line · the Founding Escape's in-fiction name · the Metropolis's central plaza name · the Metropolis's species mix. **Partially closed:** Warren Flow, whose readable signature is now settled while its mechanics remain open.

**Sections touched:** 4.2 · 6.3 · 15.1 · 19 · 20.4 · 29.4 · 33.1 · 33.2 · 35.1, plus Appendices A, B, C and D.

---

### v0.4.2 — the restructuring edition

Thirteen decisions (73–85) and a rebuilt architecture.

#### New decisions

| # | Decision |
|---|---|
| **73** | **Wanderers** — same-species loners join as ordinary Citizens, the primary early-game growth path |
| **74** | **The Founding Escape** as a full multi-register sequence, with no survivors but the three |
| **75** | **The resolution model** — mass on the front end, exposure on the back end |
| **76** | **Approaches** — Contest, Evade, Parley, Yield, Withdraw |
| **77** | **Encounter length** — N rounds carry N−1 Turns; closeness continues, cleanness ends |
| **78** | **Tharn unparked** — trigger is exposure exceeding stress threshold |
| **79** | **Guests as option-openers** — each opens one thing and closes another |
| **80** | **Four registers** — Colony, Field, Encounter, Crossing |
| **81** | **Field Mode presentation** — the naturalist's survey plate |
| **82** | **Encounter Mode** and the Final Fantasy Tactics vibrancy jump |
| **83** | **The Home Median has a Field layer**; the Metropolis is a Field territory |
| **84** | **Naming and scale calls** — Fortified Settlement, After-name, ×10 stats, Active/Ambient, Attachment-first |
| **85** | **The v0.4.2 structure** — eight parts, thirty-eight sections, six appendices |

### Structural changes

- **Eight parts replace a flat section list.** Global understanding comes first; granular detail follows.
- **Part I is sequenced as a countdown:** thesis and pillars, then **four registers, three species, two loops, one folklore.**
- **Species moved from the middle of the document to Part I**, because everything after it is coloured by the choice.
- **Traffic-as-Weather removed from the pillars** and relocated to Part II with the other environmental pressures. It is a mechanic, not a philosophical principle.
- **Folklore split in two.** Laws, Sayings, and vocabulary are voice and live in Part I; the naming *systems* are mechanics and live with the citizens.
- **The Colony and the Citizens are now separate parts.**
- **Guest Citizens moved to the Citizens part** as entities; the recruitment *procedure* stays in Leaving Home, where recruitment happens.
- **The Rest-Stop Metropolis is its own part.**
- **Production notes are explicitly marked as suggestions**, not canon.
- **Document self-history moved to Appendix B.** The body no longer narrates its own revisions.
- **Exclusions moved to Appendix A** as a reference checklist rather than a body section.
- **IMAGEGEN blocks** mark every instance of the optional generative layer inline.

### Resolved from the v0.4.1 review

Colony-versus-Median naming · the two highway manifestations (terminology corrected — transverse to the Margin, longitudinal to a Reach) · Hearth lineage as story fact only · Warren removed from the Tier II name · integer stat frame · bond-tier phrasing variants · Guest names carried from first encounter · fog of war on scouting · outpost contest gated on outbuilding investment · vehicle flavor throughout the world · a top-line summary for the generative layer · the duplicate Founding Escape paragraph.

---

## Appendix D — Open items

### Deferred numeric tuning

- **Item-weight and carry-capacity thresholds** — cutoffs governing cooperative carrying (Section 13).
- **Resource-preview specificity** on the Expedition Launcher (Section 27.2).
- **Construction Queue day-values** per building and rung, and the escalation curve (Section 14).
- **Establish-Outpost clock duration**, now one instance of the Queue (Section 27.1).
- **Exposure bands and thresholds**, and how stress threshold compares against them (Section 25.5).
- **Presence values per Approach** — the encounter difficulty surface (Section 25.3).
- **The "close" window** — how near the middle a round must land to continue an encounter (Section 25.1).
- **Raccoon recruitment rarity**, sealed-container reward tuning, and whether the raccoon reads as a singular recurring rival or one of several.

### Open design

- **Crossing, in full.** The signature mechanic and least-specified system: input model, failure states, group movement, and how longitudinal travel differs from transverse (Sections 7.3, 23.1).
- **Warren Flow** — what the player actually manipulates, what failure looks like, how congestion reads in the Colony register (Section 4.2). *Its readable signature — multiplicity of exits — was settled in v0.4.3; the mechanics were not.*
- **Cache Network across outposts** — whether the squirrel signature extends to the corridor (Section 4.3).
- **Base Defense consequences** — what a successful incursion costs (Section 26.4).
- **Guest slot scaling** between rare Tier graduations, so amenable-animal encounters do not routinely meet a full roster (Section 26.3).
- **The full Guest roster pass** against the option-opener template, including the Turtle's effect and the Weasel/Hedgehog antagonist duality (Sections 20.1–20.3).
- **Conditional antagonist ratio** — whether the 70/30 split should vary with conditions (Section 26.1).
- **Higher-Tier outpost significance** — a unique Tier III or IV building, expanded slots, or a distinct network role (Section 28.2).
- **Field Mode overlay set** — which overlays exist, toggles or cycle, any gating (Section 24.2).
- **Home Field Mode's risk floor** — whether contest is possible on home ground, and what Road Work does to a home Field run (Section 24.4).
- **Wanderer arrival rate**, refusal cost, and whether wanderers can arrive maimed or fearful (Section 17.4).
- **Tharn's per-species manifestation flavor**, and whether Crossing needs its own trigger (Section 18.2).
- **Whether a citizen left behind can be recovered later** — an obvious story hook and an obvious cruelty (Section 18.2).
- **Founding Escape ordering** — Encounter second (tension curve) or third (escalating complexity) (Section 35.1).
- **Transition treatment** — cuts, camera moves, or authored short beats (Section 3).
- **Default Role** for a newly-born or newly-unassigned citizen (Section 12).

### Parked

- **Fire as an environmental threat** — literal grass and median fire in a dry summer, delivered as a rare Choice-Event Card or world event. The resonance is strong: *"the mowing is fire"* becoming literal fire. Deliberately not rushed in half-formed.

### Unnamed in fiction

*(Empty. The Founding Escape was named in v0.4.3.)*

### Deferred to Phase 2 — the art production pass

- **Species-tracking review across all artwork** — unified within colonies, diverse at the Metropolis.
- **Raccoon-heritage visual nods** in Metropolis architecture and decor.
- **Field Mode art specification** — palette, line weight, label typography, and how a Reach's biome changes the plate's character.
- **All Phase 2 artwork, including the wordmark, must be produced with layered and editable text** rather than flattened. *(Being applied risk-weighted in practice: plates on settled canon ship with generated type flat, plates touching open items above retain a stripped base for recompositing.)*

*A note on process: "Phase 2" refers to the art and infographic production pass, **not** a numbers pass. The numeric tuning above is in scope for the current design thread.*

### Deferred authoring

- **Appendix E** — per-family building upgrade-name ladders.
- **Appendix F** — folk place-name component banks.

### Future-work backlog

- **Example and template citizen writeups** in the register of tabletop RPG sourcebook NPC entries. WHOOT (Section 20.2) is the first instance in that spirit.

---

## Appendix E — Per-family building upgrade-name ladders

*Deferred. To be authored.*

Section 15.2 establishes the principle and three worked examples (Rabbit Lookout, Squirrel Food Store, Wood Mouse Infirmary). This appendix will carry the full two-to-four-rung named ladder for every remaining structure family, across all three core species: food store, workshop and scrap store, shelter, nursery, infirmary, Staging Post, lookout, Guest accommodation, Story Circle, Community Board, and species-signature structures.

Constraints already settled: species-flavored vocabulary drawn from each species' material culture; humble and functional at Tier I, genuinely grand by Tier IV; grandeur expressed through scrap-mastery and civic complexity, never through machinery or electrification.

---

## Appendix F — Folk place-name component banks

*Deferred. To be authored.*

Section 22.2 establishes the grammar — article, modifier banks, landform suffixes, and assembly patterns — and the register. This appendix will carry the actual component contents: materials, flora, qualities, water features, fauna-trace modifiers, landform suffixes, and the pattern set that combines them, plus the separate species-metaphor and aspirational-register banks used only for colony naming (Section 22.3).

Constraints already settled: homely and plain throughout, never ornate; every legal name assembles from blessed parts so register is guaranteed structurally and no filtering is required; the aspirational register is scoped to colony naming alone.

---

*End of MEDIAN Game Design Document v0.4.4. Values marked as placeholders in Appendix D remain open by design.*
