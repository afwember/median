<!--@1-->
# MEDIAN

<!--@1.1-->
## Game Design Document v0.4.6

<!--@1.1¶1-->
**Working title:** MEDIAN
**Genre:** Atmospheric animal colony builder with high-stakes expedition action — a base-builder first ("Age of Empires, minus combat, with the heart of *Watership Down*")
**Primary platform:** PC and console, including handheld console form factors such as Steam Deck and Switch-class devices
**Mode:** Single-player
**Presentation:** Four registers — an inhabited **Colony** view, a surveyed **Field** view, a rendered **Encounter** view, and an immediate **Crossing** view (Section 3)
**Status:** Pre-production concept document
**Origin:** Conceived by Asa Wember, July 2026, after observing highway medians from a bus between Washington, DC and New York City

<!--@1.1¶2-->
> **Animal colony building on highway median strips.** Build a beloved, physically legible settlement in the overlooked green islands between highways, then risk named citizens on dangerous expeditions across asphalt and along a chain of changing median biomes.

<!--@1.1¶3-->
**ARTWORK — Title and Wordmark**

<!--@1.1¶4-->
> **On the art markers.** Lines set like the one above mark where illustration belongs when this document is set as the illustrated concept book. **ARTWORK** is a full-page image; **INFOGRAPHIC** is an information-design plate; **CREATED VISUAL** is a third class — a specific, named, in-fiction moment, tied to actual citizens and events rather than to a system, and carrying its own fallback (Section 34). They are placement notes, not part of the specification, and carry no canon weight. Spot illustrations, which sit alongside body text throughout, are not marked individually.

<!--@1.1¶5-->
---

<!--@1.2-->
## The Founding Escape

<!--@1.2¶1-->
**INFOGRAPHIC — The Founding Escape and Onboarding**

<!--@1.2¶2-->
Every campaign opens with **The Founding Escape.** The player's chosen species is first shown at its most developed — a grand, mature ancestral home that also previews the endgame the player can build toward.

<!--@1.2¶3-->
**The opening is an establishing tracking shot.** Play begins by passively observing that home in motion: a camera move through a working colony, passing **one room per structure family** (Section 16.1), so the opening doubles as a visual table of contents for everything the player will spend the campaign reconstructing.

<!--@1.2¶4-->
**The Laws run as ambient audio across the whole move.** A Teacher is drilling the young in the nursery — call-and-response, carrying through the halls — and the player hears the Laws as *the sound of a working home* rather than as a lesson delivered at them.

<!--@1.2¶5-->
**The camera settles on the three.** The founding trio are **adolescents, not the children being drilled.** They are elsewhere: out at a peripheral storage room on the colony's outskirts.

<!--@1.2¶6-->
**The first mechanical action is a modified Choice-Event Card.** It asks what to do with a free afternoon, and offers a **responsible** option and a **naughty** one — both diegetically situated at the outskirts, so the trio's survival has an in-fiction cause the player participated in. The card carries no costed resource response — the colony's resources are not the player's yet — so its options are social rather than economic, leaving the full Choice-Event Card system its proper introduction later.

<!--@1.2¶7-->
The choice sets the **early tonal register.** The system writes the trio's characterization; the player reads it. The randomized-personality-trait rule (Section 18.2) is intact — the player picks a vibe, the system rolls within it.

<!--@1.2¶8-->
**Then the machines come.** One of the three has been mockingly reciting the Second Law — *"the mowing is fire"* — to needle the others about being made to memorize it. And then it is true.

<!--@1.2¶9-->
**Casualties: there are no survivors but the three.** The Teacher dies. The nursery dies. The ancestral colony is total. Consequences that run the length of the campaign:

<!--@1.2¶10-->
- The trio carry the Laws **imperfectly** — what three teenagers half-remembered (Section 6.1).
- The colony's **first assignment of the Teacher Role** is a real event: someone has to become the Teacher now.
- The Metropolis's contradictory Laws have teeth, because some of them are corrections (Section 30.3).
- A **wandering joiner** may one day prove the trio wrong about being alone (Section 18.4).

<!--@1.2¶11-->
**The loss is never depicted.** It is sensory-obscured — dust, noise, distance, narrowed perception — and known **by absence**: the trio come back and there is nothing (Section 34.2).

<!--@1.2¶12-->
**The played sequence.** The escape is played, not shown, and it moves through every register in turn:

<!--@1.2¶13-->
> **Cutscene** → **Encounter** → **Field Mode** (the ancestral Reach, crossed on foot toward the highway boundary) → **Crossing** → *(Field/Crossing repeating two or three times, each iteration compressing toward montage)* → **"time passes"** → arrival at an unfamiliar median → the line — *"the air smells good here"* → **Town Center placement.**

<!--@1.2¶14-->
This trains all four registers in order and earns the distance between the ancestral home and the new colony: they flee long and far, and the home the player builds is genuinely far from the one they lost.

<!--@1.2¶15-->
**The repeated crossings are the diegetic tutorial** for Return Logic's 10% forced manual re-crossing (Section 24.2) — the player learns a crossing can recur unbidden before the system ever does it to them.

<!--@1.2¶16-->
**"The air smells good here" becomes the colony's first original Saying** (Section 6.2), entering the Chronicle at the exact moment the Records begin.

<!--@1.2¶17-->
> **OPEN — Founding Escape ordering.** Whether the Encounter beat belongs second, as a tension curve opening at peak and decompressing, or third, as escalating complexity. · `500 log/open_items.md`

<!--@1.2¶18-->
**The Founding Escape is not an instance of the Mowing.** The Mowing is cyclical, evadable, and survivable — the median is damaged and then recovers. The Founding Escape is a **singular, permanent apocalypse**: a new overpass construction that annihilates the ancestral median entirely and leaves a permanent hazardous construction zone. **Nothing grows back.** Road Work is its recurring *echo* — the same class of machinery, returning — and never the same event at smaller scale.

<!--@1.2¶19-->
The ancestral home is seen intact exactly once, in this scene. It is revisitable, as a ruin, by Special Journey (Section 28.1).

<!--@1.2¶20-->
Its in-fiction name is the Founding Escape, and the home it took is the **Ancestral Warren, Den, or Burrow**, according to the campaign's species (Section 6.3).

<!--@1.2¶21-->
Each founding citizen may begin with a **Keepsake** carried out of the old home (Section 20).

<!--@1.2¶22-->
---

<!--@1.2.1-->
### Elevator pitch

<!--@1.2.1¶1-->
**Age of Empires-style colony progression in a highway median, with the emotional animal-world storytelling of *Watership Down*.** The player guides one small civilization of rabbits, squirrels, or wood mice. Safe local sustenance supports everyday life, but lasting advancement requires expeditions beyond the home median: across live traffic to the resource-rich Margin, or down the highway to discover new median biomes, establish outposts, meet outsiders, and eventually connect with a distant multi-species animal metropolis.

<!--@1.2.1¶2-->
MEDIAN is a base-builder first, and a resolution-based one — not a tactical-extraction shooter, not a combat-first RTS, and not a road-crossing arcade game with a management wrapper. The colony is the heart of the game. Expeditions are not the reason the base exists; they are the dangerous, dramaturgically justified action counterpart to a base-building game. The player should become attached to the place they build and to the handful of named animals who live there.

<!--@1.2.1¶3-->
Three young members of the chosen species escape the wreck of their ancestral home, destroyed by road construction. They flee to a green island between two highways, and begin again.

<!--@1.2.1¶4-->
---

<!--@1.2.1¶5-->
> **The base game must be complete, coherent and emotionally effective without any of it. Nothing in this layer is ever load-bearing.**

<!--@1.2.1¶6-->
---

<!--@1.3-->
## Contents

<!--@1.3¶1-->
**PART I — What MEDIAN is** · *Thesis and pillars, then the shape of the game.*

<!--@1.3¶2-->
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
- The world primer
- 3. Four registers
    - 3.1 Colony — dwell
    - 3.2 Field — travel
    - 3.3 Encounter — meet
    - 3.4 Crossing — risk
    - 3.5 Constraints binding all four
- 4. Three species
    - 4.1 Rabbit — burrow civilization
    - 4.2 Squirrel — canopy civilization
    - 4.3 Wood Mouse — dense, distributed civilization
    - 4.4 The shared stat frame
    - 4.5 Seasonal and environmental personalization
- 5. Two loops
    - 5.1 The domestic loop
    - 5.2 The bridge between them
    - 5.3 The expedition loop
- 6. One folklore
    - 6.1 The Laws of the Median
    - 6.2 The Sayings of the Median
    - 6.3 The Giants — vocabulary for the human world

<!--@1.3¶3-->
**PART II — The world** · *The ground the game happens on, and the forces acting on it.*

<!--@1.3¶4-->
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
- 10. Choice-Event Cards
- 11. Seasons and Road Work
    - 11.1 Seasons
    - 11.2 Road Work

<!--@1.3¶5-->
**PART III — The colony** · *The home the whole game is in service of.*

<!--@1.3¶6-->
- 12. Scale and the shape of a colony
- 13. Roles and daily work
- 14. Resources and the economy
- 15. Construction, decay, and the Construction Queue
- 16. Structures and upgrade ladders
    - 16.1 Structure families
    - 16.2 Named upgrade ladders
    - 16.3 Functional icons, the Community Board, and the Story Circle

<!--@1.3¶7-->
**PART IV — The citizens** · *Who lives there, what happens to them, how they are remembered.*

<!--@1.3¶8-->
- 17. The citizen record
- 18. Bonds, Hearths, and growth
    - 18.1 Bonds
    - 18.2 Hearths and lineage
    - 18.3 Nesting Season
    - 18.4 Wanderers — the other way a colony grows
    - 18.5 Death and memorialization
- 19. Harm, fear, and tharn
    - 19.1 The harm ladder
    - 19.2 Fear and going tharn
    - 19.3 Distinctions, the symmetry, and the After-name
    - 19.4 How citizens develop
- 20. Equipment: Keepsake, Tool, and Supply
- 21. Guest Citizens
    - 21.1 Active Guests
    - 21.2 Ambient Guests
    - 21.3 Antagonist fauna, and the ones who can change sides
- 22. The Records
    - 22.1 The Colony Record — Almanac and Chronicle
    - 22.2 The Citizen Record — Likeness and Tale
    - 22.3 Expedition Rating and the Report and Share debrief
- 23. Names
    - 23.1 Names of citizens — Given Name and After-name
    - 23.2 Names of places — the folk-name grammar
    - 23.3 The one name the player authors

<!--@1.3¶9-->
**PART V — Leaving home** · *The three away-registers, and the systems that govern what happens out there.*

<!--@1.3¶10-->
- 24. Crossing
    - 24.1 The crossing action
    - 24.2 Return logic
- 25. Field Mode
    - 25.1 What it is
    - 25.2 Presentation and overlays
    - 25.3 Node types
    - 25.4 Field Mode generalizes
- 26. Encounters
    - 26.1 The shape of an encounter
    - 26.2 Approaches
    - 26.3 The group layer — mass, never a roster
    - 26.4 Resolution
    - 26.5 Exposure — the individual layer
    - 26.6 The outcome distribution
    - 26.7 The epic case
    - 26.8 Guardrails
    - 26.9 What this system does not govern
- 27. Contest, recruitment, and Base Defense
    - 27.1 What is contested
    - 27.2 The recruitment funnel
    - 27.3 Slot scaling and scarcity
    - 27.4 Base Defense
- 28. Expeditions and the Launcher
    - 28.1 Expedition categories
    - 28.2 The Expedition Launcher
    - 28.3 Early expedition onboarding
- 29. Outposts
    - 29.1 Reach lifecycle and fog of war
    - 29.2 The outpost building set
    - 29.3 Stationing a citizen
    - 29.4 Contest and the value of investment
    - 29.5 Active versus passive value

<!--@1.3¶11-->
**PART VI — The Rest-Stop Metropolis** · *The corridor's one city.*

<!--@1.3¶12-->
- 30. The Metropolis
    - 30.1 The place
    - 30.2 Presentation — a Field territory with venues as nodes
    - 30.3 Core functions
    - 30.4 A founding myth, and what it does not mean
- 31. The Metropolis in the campaign
    - 31.1 Campaign role
    - 31.2 Victory and continuation

<!--@1.3¶13-->
**PART VII — Progression and presentation** · *Tiers, interface, art and sound, and how a campaign opens.*

<!--@1.3¶14-->
- 32. Progression tiers
    - Tier I — Scavenger Camp
    - Tier II — Fortified Settlement
    - Tier III — Independent Colony
    - Tier IV — Sovereign Network
    - 32.1 Advancement gates
- 33. Interface and information design
    - 33.1 The Colony view
    - 33.2 Blueprint / ledger overlay
    - 33.3 Citizen Records and the Village Roster
    - 33.4 The Expedition Launcher
    - 33.5 Controls and accessibility
- 34. Art and sound
    - 34.1 Visual identity
    - 34.2 Scale language and vehicle presence
    - 34.3 The sound of the world
- 35. Campaign onboarding
    - 35.1 The Founding Escape
    - 35.2 Tutorial sequence

<!--@1.3¶15-->
**PART VIII — Production notes** · *Suggestions rather than canon — plus the canonical summary.*

<!--@1.3¶16-->
- 36. Suggested scope and roadmap
    - 36.1 A suggested vertical slice
    - 36.2 A suggested V1 target
    - 36.3 A suggested approach to world events
    - 36.4 Suggested later expansion candidates
- 37. Suggested prototype success criteria
- 38. One-paragraph canonical summary

<!--@1.3¶17-->
**APPENDICES**

<!--@1.3¶18-->
- Appendix A — Building upgrade-name ladders
- Appendix B — Folk place-name component banks
- Appendix C — The hyphen-compounds
- Appendix D — The descriptive bands
- Appendix E — Played on a Screen
- Appendix F — Played at a Table
- Appendix G — Played with a Deck
- Appendix H — Pictured by the Machine

<!--@1.3¶19-->
---

<!--@2-->
# PART I — WHAT MEDIAN IS

<!--@2¶1-->
**ARTWORK — The Colony Between Two Highways**

<!--@2¶2-->
*Read in one sitting, this part should leave a reader able to describe the game accurately. It states the thesis and the pillars, then the game's shape: **four registers, three species, two loops, one folklore.***

<!--@2¶3-->
---

<!--@1#2-->
## 1. Creative thesis

<!--@1#2¶1-->
MEDIAN is about making a permanent home in a place humans consider leftover space.

<!--@1#2¶2-->
The highway provides more than a visual setting. It supplies the world geometry, boundaries, resources, hazards, rhythms, soundscape, and scale contrast. The animals do not imitate a tiny human industrial society. They remain animals, using teeth, paws, instinct, ecological knowledge, plant matter, and scavenged objects to survive inside human infrastructure.

<!--@1#2¶3-->
The desired emotional rhythm alternates between:

<!--@1#2¶4-->
- **Sanctuary:** patient construction, observation, maintenance, social life, and attachment inside the Home Median.
- **Exposure:** leaving safety for an expedition whose outcome can create resources, knowledge, relationships, injuries, and stories.
- **Return:** bringing both material gains and lived consequences back into the colony.

<!--@1#2¶5-->
The home must feel worth protecting. Danger has meaning because the player knows exactly who went out and what they came back to.

<!--@1#2¶6-->
This rhythm is not only thematic. It is **enacted by the game's presentation**: each of the four registers in Section 3 corresponds to a phase of it, so the player feels sanctuary, exposure, and return in the camera before feeling them in a mechanic.

<!--@1.1#2-->
### 1.1 Core inspirations

<!--@1.1#2¶1-->
*Watership Down* is the primary inspiration and sets the emotional and dramaturgical register. MEDIAN treats animal-scale peril, social identity, folklore, political encounters, found-family relationships, and the terror-freeze response known as going **tharn** as its narrative center of gravity. The game imagines a story beginning roughly where *Watership Down* leaves off: a small band that has already survived a founding catastrophe, now trying to build something lasting.

<!--@1.1#2¶2-->
- ***Watership Down* (primary):** animal-scale peril, social identity, folklore, political encounters, found family, and tharn.
- **Age of Empires:** comprehensible advancement tiers, a satisfying transformation from vulnerable settlement to mature civilization, and spatially readable economic growth — minus combat as a central pillar.
- ***Mouse Guard* (art reference only):** small-animal material culture and landscape-as-existential-force, in a modern register — not a source of medieval trappings, guild structures, or setting.
- **Final Fantasy Tactics (presentation reference only):** the scale of the leap between a travel view and a dramatic scene (Section 3.3).
- **Colony builders and town simulators:** attachment to a settlement shaped over time, visually active citizens, emergent personal stories.

<!--@1.1#2¶3-->
MEDIAN borrows *Watership Down*'s register and never its proper nouns. **No real *Watership Down* character name, place name, or invented word appears anywhere in MEDIAN's fiction.** All in-world lore text is original (Section 6).

<!--@1.2#2-->
### 1.2 What the game is not

<!--@1.2#2¶1-->
- A tactical-extraction or combat-first game. It is a base-builder first, with resolution-based conflict.
- An arcade road-crossing game with a base-management wrapper.
- A large-population swarm simulator.
- A combat-first RTS.
- A spreadsheet that hides its world behind menus.
- A technology fantasy in which animals become miniature humans, master electricity, or industrialize the corridor.
- A game about abandoning the town whenever the next biome opens.

<!--@1.2#2¶2-->
---

<!--@2#2-->
## 2. Design pillars

<!--@2#2¶1-->
**INFOGRAPHIC — The Seven Pillars: What It Is and Isn't**

<!--@2#2¶2-->
MEDIAN has seven design pillars.

<!--@2.1-->
### 2.1 Attachment-first base-building

<!--@2.1¶1-->
The Home Median is the permanent emotional and mechanical center of a campaign. The player improves, densifies, decorates, and remembers this place rather than replacing it. Distant expansion adds a network around the home; it does not negate the home. The base-building layer is where the colony is watched and shaped; the expedition layer is where individuals are tested. The game is a base-builder first and everything else is in service of that.

<!--@2.2-->
### 2.2 Named citizens, low population, durable identity

<!--@2.2¶1-->
Every core citizen is named, visually distinguishable, and historically tracked. Population growth is slow enough that the loss, injury, bravery, and specialization of one animal matters. The colony is small enough that the player knows every member by name — a deliberately low ceiling shared across all three species. There is no anonymous swarm. Citizens are companions and community members, not replenishable unit tokens.

<!--@2.2¶2-->
Naming is a system rather than a label generator: every citizen carries a **Given Name** from inception and may earn an **After-name** in the field (Section 23). The colony's rolling event feed names individuals rather than roles — "Nutmeg and Daisy healed Sharpnose," never "two citizens performed healing" (Section 22).

<!--@2.3-->
### 2.3 Ledger and legible

<!--@2.3¶1-->
Important state should first be visible in the world: a leaking burrow, a thin food store, a frightened posture, a frayed bridge, an animal moving with a limp. A numerical ledger must also exist for players who require clarity, especially for colony resources, capacity, construction, maintenance, and schedules.

<!--@2.3¶2-->
This does **not** mean every number is public. Character aptitudes and unexplored expedition danger retain uncertainty. The ledger clarifies known colony state; it does not eliminate discovery or suspense.

<!--@2.3¶3-->
The pillar has a recurring structural expression: wherever MEDIAN attaches a flavor name to something, it shows the functional metadata **alongside** it rather than behind it. Places carry a folk name plus functional tags (Section 23.2); the colony's history carries a Summary view beside a Literary view (Section 22); buildings carry an in-world upgrade name beside a persistent functional icon (Sections 16, 33). Field Mode carries the same logic as toggleable route overlays over an illustration (Section 25). One pattern, four applications.

<!--@2.4-->
### 2.4 Expeditions make stories and enable progress

<!--@2.4¶1-->
Nearby resources can sustain the colony, but meaningful advancement requires leaving home. Expeditions must be materially worthwhile even if all optional generative imagery is removed. Their systemic rewards include progression scrap, special artifacts, new biome access, outposts, Guest Citizens, intelligence, trade relationships, and story flags.

<!--@2.5-->
### 2.5 Consequence without disposability

<!--@2.5¶1-->
Failure usually produces fear, wounds, lost cargo, changed relationships, or maiming before death. Citizen death is uncommon; danger expresses first as fear, wounds, lost cargo, and changed relationships, all of which persist and are carried home. The harm ladder has three rungs before it has a fourth. A maimed citizen remains valuable. Experience can turn a physically limited veteran into a calm expedition anchor, teacher, planner, craft specialist, or colony leader.

<!--@2.5¶2-->
> *Most come home. Not all come home whole.*

<!--@2.5¶3-->
The encounter model gives this pillar a mechanism rather than only an intention: **exposure** determines what happens to an individual, and it widens the distribution in both directions at once (Section 26.5). The citizen who stuck their neck out is the one who comes home changed — in one direction or the other.

<!--@2.6-->
### 2.6 Mechanical restraint, expressive variety

<!--@2.6¶1-->
The simulation uses a small number of understandable resources and attributes. Visual skins, history, environment, species, and event combinations create variety. **Do not add a new currency or stat when an existing system can express the same decision.**

<!--@2.6¶2-->
This restraint pillar is load-bearing. World events, tharn, traffic-as-weather, the Records, Choice-Event Cards, the Construction Queue, and the entire Approach set are deliberately implemented as reskins, promotions, or extensions of existing mechanics rather than as new subsystems.

<!--@2.7-->
### 2.7 One world, four registers

<!--@2.7¶1-->
The game presents itself in four distinct visual and attentional registers, and **no fifth register may be added.** Every presentation need must resolve into Colony, Field, Encounter, or Crossing (Section 3). A fifth mode is a design failure rather than a feature.

<!--@2.7¶2-->
This is a pillar rather than an art note because the registers do structural work: they enact the Sanctuary/Exposure/Return rhythm, they determine where the art budget concentrates, and they are how the player knows what kind of decision they are being asked to make. The Colony Record and every citizen's Tale resolve at the Story Circle and the species hub, both inside Colony (Section 33.3).

<!--@2.7¶3-->
---

<!--@2.7.1-->
## The world primer

<!--@2.7.1¶1-->
**INFOGRAPHIC — The Cross-Section**

<!--@2.7.1¶2-->
The world has a repeating structural geometry, from one outer boundary to the other:

<!--@2.7.1¶3-->
**Sound Wall → Margin → Highway → Home Median → Highway → Margin → Sound Wall**

<!--@2.7.1¶4-->
The **Sound Wall** is impassable, and the world beyond it is never modeled. The **Margin** is the richest ground in the corridor and the most exposed, and it is never buildable, under any circumstance. **Highway** danger is set by lane count rather than by what lies beside it. The **Home Median** holds the colony.

<!--@2.7.1¶5-->
The cross-section repeats along the corridor: each median segment beyond the player's own is a **Median Reach**, and the chain of Reaches ends, far off, at the corridor's one city.

<!--@2.7.1¶6-->
A **Crossing** takes a party across the Highway to a Margin. A **Field** run reads a Reach on foot. An **Encounter** happens at one point inside one. The **Colony** is the Home Median, inhabited.

<!--@2.7.1¶7-->
---

<!--@3-->
## 3. Four registers

<!--@3¶1-->
**INFOGRAPHIC — The Four Registers**

<!--@3¶2-->
MEDIAN presents itself four ways, distinguished not by camera height but by **what the player is being asked to do with their attention.**

<!--@3¶3-->
| Mode | Verb | Register | Attention |
|---|---|---|---|
| **Colony** | **Dwell** | Embodiment | Inhabiting — this is mine, I know every corner |
| **Field** | **Travel** | Legibility | Reading territory — where things are, what my route is |
| **Encounter** | **Meet** | Drama | Present at a moment — this is happening, now, to someone named |
| **Crossing** | **Risk** | Immediacy | Committed — no reading, no planning, only nerve |

<!--@3¶4-->
**The rhythm of an expedition:**

<!--@3¶5-->
> **Colony** → *Crossing* → **Field** ⇄ *Encounter* ⇄ **Field** → *Crossing* → **Colony**

<!--@3¶6-->
An expedition alternates Field and Encounter — read the map, reach a node, drop into a rendered scene, return to the map changed — bookended by Crossings and returning home.

<!--@3¶7-->
**The transitions are the beats.** Each shift is an emotional event and is authored as one. **No transition is a load screen.**

<!--@3¶8-->
| Transition | What it should feel like |
|---|---|
| Colony → Crossing | **Commitment.** The world gets loud. There is no more preparing. |
| Crossing → Field | **Survival, then exposure.** You made it — and then the world flattens and you see how much of it there is. |
| Field → Encounter | **Rush-in.** Something is here. Distance collapses. |
| Encounter → Field | **Aftermath.** Back to the map, carrying what just happened. |
| Field → Crossing → Colony | **Return.** The world becomes warm, close, and yours again. |

<!--@3.1-->
### 3.1 Colony — dwell

<!--@3.1¶1-->
The place the player inhabits, improves, and becomes attached to. The game is a base-builder first, and this is where that is true.

<!--@3.1¶2-->
**Presentation:** rendered three-dimensional miniature diorama. Warm, tactile, gently storybook at home while remaining grounded stylized realism (Section 34). Soft organic material against harsh human infrastructure. Work routes, storage, structural problems, fear, injury, weather, and congestion all visually apparent.

<!--@3.1¶3-->
**Carries:** the three Colony hotspots — Community Board, Story Circle, and the species hub with its Village Roster (Section 33.1). Always-visible functional icons on every building. The Construction Queue.

<!--@3.1¶4-->
**Tempo:** slow. The only register the player can linger in without cost.

<!--@3.2-->
### 3.2 Field — travel

<!--@3.2¶1-->
Reading and crossing territory: where routes are chosen, nodes discovered, load managed, and the shape of a place learned. Specified in full in Section 25.

<!--@3.2¶2-->
**Presentation: the naturalist's survey plate.** Top-down and **illustrated, not schematic and abstract** — a hand-drawn field survey rather than an information display. Warm parchment ground, painterly terrain, visible hand, node markers as pins layered over the illustration, and **the highway always in frame** as textured asphalt bands with vehicles moving on them.

<!--@3.2¶3-->
This explicitly **rejects the Dwarf Fortress aesthetic while keeping its virtue**: MEDIAN takes the whole-territory legibility and information density and declines the deliberate stylistic austerity. Atmosphere is not optional in a game whose pitch is atmospheric.

<!--@3.2¶4-->
**Tempo:** deliberate. Planning speed.

<!--@3.3-->
### 3.3 Encounter — meet

<!--@3.3¶1-->
The moments that matter. Every node arrival opens this frame, and it is **the same frame whether the result is a windfall, a negotiation, or an ambush.** Specified in full in Section 26.

<!--@3.3¶2-->
**The vibrancy jump.** The delta between Field and Encounter should feel as large as Final Fantasy Tactics' leap from world map to cinematic. Field Mode is more built out than that reference's map; Encounter Mode must earn a proportionally larger jump. This is the presentation's primary production target.

<!--@3.3¶3-->
**Presentation:** rendered, close, character-scale, illustrated — the actual participants with their actual portraits, conditions, weather, and location. **This is where the art budget concentrates**, and it is what keeps a surveyed Field layer from making the dangerous half of the game look cheaper than the safe half.

<!--@3.3¶4-->
**Tempo:** the game's slowest and most weighted. An encounter is a scene.

<!--@3.4-->
### 3.4 Crossing — risk

<!--@3.4¶1-->
A signature mechanic and the moment of genuine commitment. **Leaving home happens here — not at a camera change.** Specified in Section 24.

<!--@3.4¶2-->
**Presentation:** immediate, low, lane-level. The most compressed and overwhelming view in the game. Audio-forward: traffic density and approach learnable by sound, low-frequency vibration from large vehicles, directional audio at night.

<!--@3.4¶3-->
**Tempo:** fast, brief, tense. Accessibility affordances are required rather than optional (Section 33.5).

<!--@3.4¶4-->
Crossings use no Approaches, no Turns, and no exposure. They are an action mode, not an encounter.

<!--@3.5-->
### 3.5 Constraints binding all four

<!--@3.5¶1-->
Canon rules, not art-direction preferences:

<!--@3.5¶2-->
1. **Spatial fidelity.** The Colony and Field presentations of the same ground **are the same place.** If a player learns their colony's shape in one and the other does not match it, both break. This binds level authoring.
2. **Traffic is never off-screen.** Every register keeps the highway present — visible, audible, or both. Traffic is present in the Colony register too, quieter, more distant, more filtered than at the road.

<!--@3.5¶3-->
   > *The road is never gone. It is only set far off.*

<!--@3.5¶4-->
3. **Each register has a distinct palette and temperature**, legible at a glance and without color dependence.
4. **Four registers, no more** (Pillar 2.7).
5. **No transition is a load screen.**

<!--@3.5¶5-->
---

<!--@4-->
## 4. Three species

<!--@4¶1-->
**INFOGRAPHIC — The Three Core Species**

<!--@4¶2-->
**INFOGRAPHIC — The Median Read Three Ways**

<!--@4¶3-->
Each campaign selects one core species. The three campaigns share the same economy, world logic, progression skeleton, expedition categories, and citizen model. Asymmetry comes from spatial architecture, stat bias, and one defining home-system problem — not from three unrelated games.

<!--@4¶4-->
**Each campaign is one species, for its whole length.** A rabbit colony is rabbits; a mouse colony is mice. The choice made at founding holds to the end, and the found-family beat lives in the Guest system (Section 21).

<!--@4¶5-->
Species colours everything downstream: the hub name, every structure family's vocabulary, the Given Name banks, the colony-naming imagery, the spatial signature system, and the way a party behaves in the field.

<!--@4.1-->
### 4.1 Rabbit — burrow civilization

<!--@4.1¶1-->
**Personality:** grounded, communal, fast, cautious, architectural.
**Spatial identity:** an underground warren connected to surface forage and multiple bolt holes.
**Bias:** strong sprinting and teamwork, larger bodies and appetites, modest carrying efficiency.

<!--@4.1¶2-->
Rabbit construction is a depth-and-flow puzzle. Chambers, tunnels, food stores, nurseries, and exits must fit beneath limited terrain. Surface access points create efficiency but also exposure. Poor circulation produces bottlenecks during a predator alarm or Road Work emergency.

<!--@4.1¶3-->
**Signature system — Warren Flow.** The player manages routes, chamber congestion, structural support, and escape coverage. The goal is not to chase a hidden "bolt-hole score," but to create a visibly functioning network with enough exits and alternate paths.

<!--@4.1¶4-->
**The system's readable signature is multiplicity.** A rabbit colony is legible at a glance by how many ways out it has: half a dozen or more bolt holes scattered irregularly across the ground above a mature warren, and at least one **Far-hole** — a further exit set far enough off to be a genuine alternative rather than a second front door. A mouse burrow may show a single mouth; a warren never should. Because the Colony and Field presentations of the same ground are the same place (Section 3.5), the Far-hole appears in the **Field layer** as well — the shape of a warren is partly visible from outside it, and reading a strip means noticing where its exits come up.

<!--@4.1¶5-->
> **OPEN — Warren Flow.** What the player actually manipulates, and how congestion reads in the Colony register. · `500 log/open_items.md`

<!--@4.1¶6-->
**Strengths:** fast open-ground movement, powerful coordinated hauling, efficient excavation, strong rescue capability.
**Pressures:** high food demand, tunnel moisture and collapse risk, limited vertical access, crowding at entrances.

<!--@4.2-->
### 4.2 Squirrel — canopy civilization

<!--@4.2¶1-->
**ARTWORK — The Squirrel Cache Network**

<!--@4.2¶2-->
**Personality:** mobile, opportunistic, dispersed, daring, logistical.
**Spatial identity:** nests, bridges, branches, trunks, guardrails, and scattered caches.
**Bias:** strong carrying and climbing, flexible routes, greater exposure when forced to ground.

<!--@4.2¶3-->
Squirrel construction turns the Home Median into a layered vertical network. Rather than one perfect central warehouse, supplies are distributed among visible caches. Location, redundancy, retrieval time, weather protection, and theft risk matter.

<!--@4.2¶4-->
**Signature system — Cache Network.** The player balances convenience against resilience. Centralizing goods is efficient but vulnerable; dispersal protects the colony but consumes labor and travel time. Losing one cache to a raid never wipes the whole stockpile, at the cost of constant spatial management.

<!--@4.2¶5-->
> **OPEN — Cache Network across outposts.** Whether it extends the corridor itself into a distributed store. · `500 log/open_items.md`

<!--@4.2¶6-->
**Strengths:** vertical mobility, heavy-item hauling, rapid response across connected canopy, route redundancy.
**Pressures:** exposed infrastructure, tree loss, weather damage, cache spoilage or theft, dependence on Anchor Points.

<!--@4.3-->
### 4.3 Wood Mouse — dense, distributed civilization

<!--@4.3¶1-->
**ARTWORK — The Wood Mouse Relay**

<!--@4.3¶2-->
**Personality:** ingenious, quiet, compact, cooperative, adaptable.
**Spatial identity:** tiny rooms, root passages, culverts, grass tunnels, densely interlocked micro-infrastructure.
**Bias:** low consumption and footprint, high acceleration and stealth, low individual carrying capacity and physical resilience.

<!--@4.3¶3-->
Mice permit the densest settlement, but they remain named individuals — not an anonymous swarm. Their spatial challenge is coordinating many small jobs and narrow routes without losing readability or turning the game into queue management.

<!--@4.3¶4-->
**Signature system — Relay Network.** Mice divide loads and tasks across short, visible handoffs. The player designs stations, micro-paths, and work neighborhoods so that small carrying capacities become an efficient collective chain.

<!--@4.3¶5-->
- **Safety in Numbers.** A mouse expedition is a *single commit-and-execute crossing* — the same player interaction as any other, with no split attention across simultaneous crossings. Its outcome resolves as a **partial-outcome distribution**: most of the group makes it, and occasionally one doesn't, rather than a binary pass/fail. This falls out of the exposure model without a special-case rule. A six-mouse party carrying the same haul as a three-rabbit party spreads that exposure across twice the bodies — each individual's share runs lower while the number exposed runs higher (Section 26.5).
- **Expedition Access Identity.** Mice reach certain resource nodes and pockets *within* a Margin that no other species can reach — but only after taking the same crossing risk everyone takes. This is never an alternate route *across* the highway, and does not extend to the Home Median. It is a reward for having crossed, not a way to avoid crossing.

<!--@4.3¶6-->
**Strengths:** efficient use of food and space, stealth, access to small voids, rapid light-material construction, unique Margin pockets.
**Pressures:** low load capacity, vulnerability to wind shear and direct trauma, narrow-route congestion, individual fragility.

<!--@4.4-->
### 4.4 The shared stat frame

<!--@4.4¶1-->
All three species run on the same handful of shared stats, differing only by bias. The economically-relevant dials are **Speed** (exposure time per crossing — higher speed means a shorter vulnerable window), **Carry Capacity** (value moved per trip), and **Food Consumption** (upkeep per individual). All three are integers on the same frame; Speed feeds hidden resolution (Sections 24.1, 26.4) and stays a descriptive band to the player rather than a shown number (Appendix D), on the same principle governing every hidden aptitude (Section 17).

<!--@4.4¶2-->
**All values are integers.** MEDIAN is integer-based throughout — one day, one carry slot, one expedition — and the stat frame is scaled so that no species carries a fractional value.

<!--@4.4¶3-->
| Species | Speed | Carry | Food Consumption | Emphasis |
|---|---|---|---|---|
| **Rabbit** | Fastest | 10 | 10 | Precision — one clean high-stakes crossing |
| **Squirrel** | Standard | 20 | 10 | Logistics — best cargo per trip and per food |
| **Wood Mouse** | Standard | 6 | 5 | Density — many small bodies, efficient per food |

<!--@4.4¶4-->
**One rabbit, one squirrel, or two mice is one body-unit.** Capacity, party size, and party score count in body-units: a rabbit or squirrel is one body-unit at 10 or 20 carry and 10 food; a wood-mouse pair is one body-unit at 12 carry and 10 food. Every body-unit eats 10; carry runs 10 : 12 : 20.

<!--@4.4¶5-->
They resolve capacity, party size, cooperative lifting, and food upkeep. They never resolve harm: wounds, maiming, tharn, exposure, death, bonds, and Records all resolve by the individual animal. A rabbit colony loses a whole body-unit at a time; a mouse colony loses half of one. A Standard item carried by two mice splits or drops if either goes down.

<!--@4.4¶6-->
A mouse colony gets more done per unit of food than a rabbit colony and runs larger (Section 12), but every mouse is still a named individual and every mouse crossing is a single committed action, not a swarm.

<!--@4.4¶7-->
**Three dials, and no more.** A species' expendability needs no stat of its own: it already falls out of the ratio between what a body-unit carries and what it eats.

<!--@4.5-->
### 4.5 Seasonal and environmental personalization

<!--@4.5¶1-->
Small, flavorful seasonal or environmental quirks personalize species and Guests. The first concrete instance: the **Snake Guest takes a movement penalty in Winter**. This is a template and an open design avenue — the team should look for similar small quirks for the core species — but no further instances are locked.

<!--@4.5¶2-->
The Guest roster's own situational trade-offs are handled systematically rather than as one-off quirks; see the roster's governing shape in Section 21.1.

<!--@4.5¶3-->
---

<!--@5-->
## 5. Two loops

<!--@5¶1-->
**INFOGRAPHIC — The Two Loops**

<!--@5¶2-->
MEDIAN runs on two loops. One is the reason the game exists; the other is the reason the first one can grow.

<!--@5.1-->
### 5.1 The domestic loop

<!--@5.1¶1-->
The domestic loop is how a place becomes worth protecting.

<!--@5.1¶2-->
1. Observe citizens, structures, stores, weather, and local ecology.
2. Assign standing **Roles** (Section 13) and standing **Tool** assignments (Section 20). Both persist until changed rather than being clicked per task.
3. Improve the Home Median's layout and resilience.
4. Read approaching needs: seasonal pressure, Road Work risk, scarce scrap, a promising expedition, a pending Choice-Event Card, a citizen opportunity.
5. Decide whether to commit eligible citizens to an expedition that day.
6. Absorb the expedition's gains and consequences into the physical town.

<!--@5.1¶3-->
The player may spend substantial time arranging and watching the colony, but game time is structured. Pausing is available for accessibility and strategy; pausing does not advance production.

<!--@5.2-->
### 5.2 The bridge between them

<!--@5.2¶1-->
**The colony can always survive at home, and can never advance there.** Everything it needs to live is within reach; everything it needs to become something is not.

<!--@5.2¶2-->
> *The Median feeds you. It will not make you.*

<!--@5.2¶3-->
Safe local ecology supplies subsistence → structures and ambitions demand salvage → expeditions secure scrap, artifacts, knowledge, and connections → the colony becomes safer and more capable → greater range exposes richer but more contested opportunities. This is not a third loop; it is the pressure that forces the first loop into the second.

<!--@5.2¶4-->
Local subsistence is not abstract. Because the Home Median is itself a Median Reach with its own Field layer (Section 25.4), everyday foraging is a **low-stakes Field run on home ground** — which means the first real expedition reads as *the same activity, across the road*.

<!--@5.3-->
### 5.3 The expedition loop

<!--@5.3¶1-->
The expedition loop is how the colony grows, and what growth costs.

<!--@5.3¶2-->
1. **Choose a purpose:** Margin Raid, Median Scout, Establish Outpost, Outpost Visit, or a Special Journey.
2. **Choose citizens:** one expedition per citizen per day. Selection depends on known traits, experience, wounds, relationships, species capabilities, Guest abilities, and player intuition.
3. **Prepare:** allocate carrying equipment and assign each departing citizen a **Supply** — a single per-run pick each, so preparation never becomes a loadout spreadsheet (Section 20).
4. **Depart:** for a transverse mission, enter the outbound Crossing sequence. Longitudinal travel uses corridor hazards and abstracted travel beats (Section 7.3).
5. **Enter Field Mode:** the party moves through surveyed territory dotted with discoverable nodes. Contest status and encounter type are revealed only on reaching a node, never at launch.
6. **Resolve each node as an Encounter:** choose an Approach, act on any Turns the contest earns, take the outcome (Section 26).
7. **Return:** the player chooses when to head home, feeding into Return Logic (Section 24.2).
8. **Record the story:** the expedition closes on a **Rating** and a **Report and Share** debrief, writing entries into the Colony Record and the Citizen Records of everyone who went (Section 22.3). This is the game's principal event-generator.

<!--@5.3¶3-->
---

<!--@6-->
## 6. One folklore

<!--@6¶1-->
MEDIAN's animals have a single oral culture, and it does real work: it teaches systems, it names the world, and it gives the Records their voice. All of it is **original in-world text.**

<!--@6¶2-->
It is one body of material with two registers inside it — the **Laws**, which teach, and the **Sayings**, which set tone — plus a shared vocabulary for the human world. The *naming systems* that grow out of this culture are mechanics rather than voice and live in Section 23.

<!--@6¶3-->
**A general canon note: animals in MEDIAN can read.** This is a suspension of disbelief the design requires and accepts openly. MEDIAN is not pursuing rigid ecological verisimilitude, and no in-world text needs a "read by the player, not the citizens" caveat.

<!--@6.1-->
### 6.1 The Laws of the Median

<!--@6.1¶1-->
**INFOGRAPHIC — The Laws and Sayings of the Median**

<!--@6.1¶2-->
The **Laws** are the functional half. Each teaches a real system, which makes folklore the game's tutorialization layer: the player learns to survive by learning what the animals already say.

<!--@6.1¶3-->
| Law | Text | Teaches |
|---|---|---|
| **The First Law — of the Roaring Iron** | *"Wait for the gap. The gap is given, not owed."* | The Crossing: gaps are readable, and never promised. |
| **The Second Law — of the Mowing** | *"The mowing is fire. Fire passes; the burned ground feeds."* | Road Work: it wipes the Margin, and the Margin comes back. |
| **The Third Law — of Water** | *"Drink where the water moves. Standing water remembers what fell in it."* | Sustenance and hydration, and the Pond Hollow's disease risk. |
| **The Fourth Law — of the Share** | *"A hoard in one belly is a store the winter never sees."* | The economy: pooled stores, no private accumulation. |
| **The Fifth Law — of the Sky** | *"Hawks own the day, owls own the night. Neither owns the hedge."* | Predators by time of day, and the value of cover. |

<!--@6.1¶4-->
*(Law text is authored canon and open to revision on tone; the teaching assignments are settled.)*

<!--@6.1¶5-->
**Four exposure surfaces:**

<!--@6.1¶6-->
1. **The Founding Escape (primary).** The campaign opens inside a mature ancestral home with a Teacher drilling the young in the Laws, call-and-response, heard as the camera moves through the halls — and then the machines come, and *"the mowing is fire"* stops being a recitation.
2. **Just-in-time contextual surfacing.** The first Road Work surfaces *"the mowing is fire."* The first night owl surfaces *"owls own the night."* Folklore is the tutorial prompt; there is no separate tutorial voice.
3. **Ongoing colony culture.** The Teacher passes the Laws to the young (Sections 13, 18). The **Story Circle** is their venue (Section 16.3). They are inscribed in the world, appear on the Community Board, and serve as loading-screen aphorisms.
4. **Worldbuilding variants.** The Rest-Stop Metropolis holds **competing and contradictory Laws** (Section 30) — a bigger, older, more cosmopolitan settlement remembers the world differently, and the player's colony discovers that its truths are local.

<!--@6.1¶7-->
**The colony's own Laws are imperfect.** The founding trio are adolescents who were *not* the students being drilled, and no adult survives the Founding Escape. What the colony carries forward is what three teenagers half-remembered. This is why the Metropolis's contradictions have teeth, and why the first assignment of the Teacher Role is a real event rather than a menu click.

<!--@6.2-->
### 6.2 The Sayings of the Median

<!--@6.2¶1-->
The **Sayings** are the tonal half, kept deliberately separate so the two registers do not blur. **Laws teach a system. Sayings have no teaching job attached.** They share the same exposure surfaces: loading screens, Teacher and elder dialogue, Story Circle recitation, Community Board inscriptions, banners at civic occasions.

<!--@6.2¶2-->
The Sayings are near one-to-one restatements of the design pillars, spoken from inside the fiction:

<!--@6.2¶3-->
- *"Stories over statistics."*
- *"Small is grand."*
- *"Observe. Plan. Adapt. Teach the young. The Median remembers."*
- *"Every life has a name."*
- *"The world is beautiful and dangerous."*
- *"Build. Gather. Survive."*
- *"Unity. Work. Harmony."*

<!--@6.2¶4-->
Nine more have entered the pool since, carrying the world rather than restating the pillars:

<!--@6.2¶5-->
- *"The road is never gone. It is only set far off."*
- *"The road gives what it throws away. The wall gives what it keeps."*
- *"The Median feeds you. It will not make you."*
- *"Far ground, thin cover."*
- *"Most come home. Not all come home whole."*
- *"The heavier the haul, the longer the road home."*
- *"We do not leave what we can carry."*
- *"The mending is not the making."*
- *"Walk it before you hold it."*

<!--@6.2¶6-->
Sayings are **anonymous collective wisdom** or attributed to invented in-world figures. They are never attributed to real *Watership Down* characters.

<!--@6.2¶7-->
**The pool grows.** The colony's founding produces its first original Saying at the moment the player chooses to stop running and stay — *"the air smells good here"* — the first thing the Records ever record.

<!--@6.3-->
### 6.3 The Giants — vocabulary for the human world

<!--@6.3¶1-->
**INFOGRAPHIC — The Giants: Vocabulary for the Human World**

<!--@6.3¶2-->
The animals have their own words for the human world, and those words distinguish rather than lump. An animal is far too observant to confuse a rider with the thing it rides in.

<!--@6.3¶3-->
- **The Giants** — humans, specifically. The word carries scale and otherness, not malice.
- **Roaring Iron** — vehicles, specifically. Named for force and momentum rather than shape.
- **The Rivers of Thunder** / **the Roaring Rivers** — the highway itself. A **regional-variant pair rather than one fixed term**: different colonies and dialects use different names, and both are canon simultaneously — the "many words for snow" principle applied to the one thing every animal in this world has an opinion about. The pool can grow the same way elsewhere in the vocabulary.
- **The Mowing** — an ordinary, survivable instance of Road Work (Section 11.2).

<!--@6.3¶4-->
Two further terms name the campaign's founding catastrophe and the home it took:

<!--@6.3¶5-->
- **The Founding Escape** — the event itself, the plain term and the in-world one at once, which suits a folk register tuned homely and plain rather than ornate (Section 23.2). It is categorically *not* an instance of the Mowing: the Mowing is cyclical, evadable and survivable, while the Founding Escape is a singular permanent apocalypse.
- **The Ancestral Warren / Den / Burrow** — the home that was lost, named with the campaign species' own hub term: a rabbit campaign mourns an Ancestral Warren, a squirrel campaign an Ancestral Den, a mouse campaign an Ancestral Burrow.

<!--@6.3¶6-->
---

<!--@3#2-->
# PART II — THE WORLD

<!--@3#2¶1-->
**ARTWORK — The Corridor at Golden Hour**

<!--@3#2¶2-->
*The ground the game happens on, and the forces acting on it.*

<!--@3#2¶3-->
---

<!--@7-->
## 7. World geography and terminology

<!--@7.1-->
### 7.1 The cross-section

<!--@7.1¶1-->
The world has a repeating structural geometry. From one outer boundary to the other, a typical playable cross-section is:

<!--@7.1¶2-->
**Sound Wall → Margin → Highway → Home Median → Highway → Margin → Sound Wall**

<!--@7.1¶3-->
The arrangement is symmetrical in principle, though terrain, lane count, elevation, vegetation, and accessibility may differ on each side. This is the one place in the document where *geometry* is the precise word: the cross-section is a designed structure that repeats, not a landscape.

<!--@7.1¶4-->
The **Sound Wall** is a real, recognizable piece of highway infrastructure — a tall, often vine-covered concrete barrier — and it forms the permanent, impassable outer boundary of the playable world. This grounds the map's edge in something the player recognizes rather than an invented lore device; animals simply cannot scale it, and the world beyond is never modeled. The sound wall's *height* is pure flavor, never a mechanical figure.

<!--@7.2-->
### 7.2 Home Median

<!--@7.2¶1-->
The **Home Median** is the central strip between opposing carriageways and the site of the player's colony. It can be narrow or broad, grassy or wooded, dry or culverted. It is relatively safe from traffic while still subject to predators, weather, runoff, vibration, disease, and Road Work.

<!--@7.2¶2-->
The colony is built **in and on the Median**, not under the active highway and not in the Margin.

<!--@7.2¶3-->
**The Home Median and the colony are two things with two names.** The Median is a Median Reach like any other and receives a **generated folk name** from the world (Section 23.2). The **colony** built on it receives the one name the player authors (Section 23.3). A colony called Horizon Fields may well stand on a reach the corridor has always called The Long Verge.

<!--@7.2¶4-->
Because the Home Median is a full Reach, it has a **Field layer** of its own — biome, Anchor Points, node-bearing ground — and is not only ever seen as a diorama (Section 25.4).

<!--@7.3-->
### 7.3 Highway

<!--@7.3¶1-->
The **Highway** is the active multi-lane barrier between a Median Reach and either of its Margins. **Every Reach in the corridor sits between carriageways** — that is what makes it a Reach — so the Highway borders all of them, and not only the Home Median. It is both boundary and playable hazard.

<!--@7.3¶2-->
Highway danger is governed by **lane count**, from two up to four or five. Lane count is independent of the median biome beside it — a wide, lush median can sit against a narrow two-lane crossing, and a thin grass ribbon against a five-lane gauntlet. This decouples "how rich is this place" from "how dangerous is it to reach."

<!--@7.3¶3-->
**Two manifestations.** The highway is encountered in two structurally different ways, and they should look and feel distinct:

<!--@7.3¶4-->
- **Transverse crossing — Median to Margin.** Cutting *across* the lanes. The standard Crossing sequence (Section 24): stage at protected micro-cover, read the traffic, commit. Short, lateral, and the game's signature moment of nerve.
- **Longitudinal travel — Reach to Reach.** Moving *along* the corridor to another Median Reach. Distance rather than width; abstracted travel beats and corridor hazards rather than a single lane-by-lane gauntlet.

<!--@7.3¶5-->
**Service crossovers mark the boundary between one Reach and the next.** The maintenance gaps and U-turn areas that break the median at intervals are how a party knows it has left one Reach and entered another.

<!--@7.3¶6-->
Their danger is exposure. Almost nothing uses a crossover — maintenance and police, rarely — and what it offers instead is open pavement, no cover, long sightlines, and nowhere to freeze that is not visible. At a crossover a party is seen rather than struck.

<!--@7.3¶7-->
> **OPEN — Longitudinal travel.** How it differs from a transverse crossing, in presentation and in mechanics. · `500 log/open_items.md`

<!--@7.3¶8-->
In the animals' own vocabulary the highway is a river: the **Rivers of Thunder** or the **Roaring Rivers**, depending on which colony is speaking. The vehicles on it are **Roaring Iron**, and the humans inside are **the Giants** (Section 6.3).

<!--@7.4-->
### 7.4 Margin

<!--@7.4¶1-->
The **Margin** is the resource-rich, ecologically chaotic strip between a highway and its outer sound wall. Fast pioneer plants, windblown seeds, insects, roadkill traces, litter, packaging, tire fragments, and other human detritus accumulate there.

<!--@7.4¶2-->
**Every Reach has a Margin on each side**, and each Margin has two edges of its own. The two share ground type and differ in everything that matters.

<!--@7.4¶3-->
> *The road gives what it throws away. The wall gives what it keeps.*

<!--@7.4¶4-->
| | **Road-edge** | **Wall-edge** |
|---|---|---|
| **Goods** | Rigid and Flexible Scrap, roadkill, litter, packaging, tire fragments | Sustenance — sheltered growth, seed drift banked against the wall, undisturbed soil, insects |
| **Hazard** | Lethal. Wind Draft and the River's Spume at full strength | Low. Quiet, still, out of the wind |
| **Why** | Everything the road sheds lands here | Nothing disturbs it — no mowing, no salt, no traffic |

<!--@7.4¶5-->
No litter reaches the wall. Debris is thrown or blown from the carriageway and settles near it; the far edge stays clean, and grows. Hazard rises toward the road (Section 9.3).

<!--@7.4¶6-->
A Reach therefore offers four working grounds rather than one strip.

<!--@7.4¶7-->
The Margin is renewable rather than permanently exhaustible. Nodes deplete locally, then replenish through plant growth and new waste deposition. Road Work can wipe the strip nearly bare for a time, resetting cover and yield before succession begins again.

<!--@7.4¶8-->
The Margin is **never buildable under any circumstance.** It can be raided and traversed, but nothing the player builds ever persists there. This is a permanent property of the world, not a tier gate.

<!--@7.5-->
### 7.5 The median chain and the Median Reach

<!--@7.5¶1-->
**INFOGRAPHIC — The Corridor Chain**

<!--@7.5¶2-->
The Home Median is one segment in a longitudinal chain of medians extending up and down the corridor. Each remote segment is a **Median Reach**. Reaches differ in width, hydrology, vegetation, infrastructure, exposure, predators, lane count, and resource character.

<!--@7.5¶3-->
A Reach stands in one of three states, described in full in Section 29:

<!--@7.5¶4-->
| | |
|---|---|
| **Unknown** | Never scouted. A blank on the corridor map. |
| **Walked** | Scouted, and visitable through Field Mode. Nothing persists, and the Reach reverts to wild between visits. |
| **Held** | Outposted. A genuine extension of the colony, its fog cleared for good. |

<!--@7.5¶5-->
> *Walk it before you hold it.*

<!--@7.5¶6-->
**Every Reach carries a folk name**, generated from its actual character (Section 23.2) and paired with functional metadata tags rather than a second literal name.

<!--@7.5¶7-->
**Each Reach is unified, and adjacent Reaches may differ sharply.** A Reach is internally coherent — one place with one character — and carries no sub-divisions. Its internal variation comes from Anchor Points (Section 8.2), which guarantee a mix rather than a monoculture.

<!--@7.5¶8-->
Correspondingly, two neighboring Reaches **may differ more sharply than real-world geography would produce** — a wooded median can sit directly upstream of a concrete trench. This is a deliberate legibility-driven convention, stated explicitly so future Reach content is not "corrected" as though a jarring biome transition were an error. Variety comes from travelling between whole Reaches, never from subdividing one.

<!--@7.6-->
### 7.6 What else is out there

<!--@7.6¶1-->
The corridor is not only medians and margins. Two things exist beyond the chain and are named here so the player has a map before they have an explanation:

<!--@7.6¶2-->
- **The Rest-Stop Metropolis.** Far down the corridor, a large, old, genuinely multi-species animal settlement hidden in the neglected margins of a human rest stop — drainage spaces, service voids, dumpster enclosures, embankments, vents. It is the only city in this world, the primary destination of the Special Journey expedition, and the endpoint of the campaign's victory arc. **Part VI** is devoted to it.
- **The ancestral home.** Wherever the campaign's chosen species came from before the Founding Escape destroyed it — now a permanent hazardous construction zone, and revisitable as a ruin by Special Journey from Tier II (Section 28.1).

<!--@7.6¶3-->
---

<!--@8-->
## 8. Median biomes and Anchor Points

<!--@8.1-->
### 8.1 The eight biomes

<!--@8.1¶1-->
**MULTI-PAGE SECTION — The Eight Biomes**

<!--@8.1¶2-->
Eight biomes are canon. They differ on **visuals, resource mix, and natural cover** — *not* on highway danger, which is governed entirely by lane count. Each biome is a whole-Reach property under the unified-Reach rule.

<!--@8.1¶3-->
- **Thin Grass Ribbon:** little building room, excellent sightlines, high wind exposure. Resource-poor.
- **Wooded Median:** trees enable squirrel infrastructure and shade, but conceal predators. Strong Durable sustenance; canopy and root Anchor Points.
- **Culvert Garden:** reliable water and rich soil with flood risk. Strong Perishable sustenance; high Flexible Scrap.
- **Creek Split:** abundant ecology divided by moving water. Strong Perishable sustenance; scattered Rigid Scrap.
- **Pond Hollow:** food-rich wetland with disease, amphibian, and snake encounters. Very strong Perishable sustenance; mixed scrap.
- **Concrete Trench:** scarce vegetation, strong shelter opportunities, extreme heat and runoff. Poor Sustenance; rich Rigid Scrap.
- **Overpass Shadow:** complex vertical structure, darkness, noise, protected dead spaces. Poor Sustenance; rich mixed scrap.
- **Interchange Expanse:** broad territory, many routes, severe navigational and predator exposure. Richest resource variety and the highest danger.

<!--@8.1¶4-->
Every biome carries the Road-edge / Wall-edge contrast at its own margins (Section 7.4): whatever a Reach offers, it offers most, and most dangerously, nearest the road.

<!--@8.2-->
### 8.2 Anchor Points

<!--@8.2¶1-->
**INFOGRAPHIC — Anchor Points**

<!--@8.2¶2-->
Each Reach generates a small, fixed set of named terrain features called **Anchor Points**, each suited to particular species or building types — a canopy tree for squirrel infrastructure, a deep root system for a rabbit warren, a culvert mouth for mouse micro-tunnels.

<!--@8.2¶3-->
Anchor Points are a **bonus layer, never a gate** — a Reach is always usable without perfectly matching its Anchors — and every Reach generates a *mix*, never a monoculture. This internal mix is the whole of a Reach's internal variation.

<!--@8.2¶4-->
Anchors are named through the same folk grammar as their Reach, and their names feed the Reach's own: a Reach with twin oaks at its heart is liable to be called for them. They are the most common thing a generated place name derives from, and they are what the Field register labels as a territory's named ground (Section 25.2).

<!--@8.2¶5-->
The one guaranteed exception is the first Home Median Reach, established immediately after the Founding Escape: it is guaranteed to suit the player's chosen species, so no campaign opens on hostile ground. Every later Reach follows the mixed-generation rule.

<!--@8.2¶6-->
> *Far ground, thin cover.*

<!--@8.2¶7-->
Anchor Points also modulate Road Work severity (Section 11.2).

<!--@8.2¶8-->
---

<!--@9-->
## 9. The day, traffic, and traffic as weather

<!--@9.1-->
### 9.1 Daily structure

<!--@9.1¶1-->
**INFOGRAPHIC — The Game Day**

<!--@9.1¶2-->
A game day is a bounded operational cycle, not infinite tinkering. Exact clock length remains a prototype variable. One expedition runs at once, colony-wide, and one expedition per citizen per day also holds: launching an expedition commits its participants for that day, and no citizen may complete a second before the next dawn. You send a party, and you wait.

<!--@9.1¶3-->
Suggested daily beats:

<!--@9.1¶4-->
- **Morning Rush / Domestic Opening:** consumption and recovery resolve; the player reviews the colony, repairs, builds, and makes assignments while traffic is dense and stressful.
- **Midday Operating Window:** the clearest default expedition window, balanced by daylight predators and faster vehicles.
- **Evening Rush / Domestic Return:** noise, fumes, and erratic traffic discourage normal departures; returning consequences and home tasks take focus.
- **Night Velocity:** a second operating window rather than a routine second expedition. Against it: extreme vehicle speed, reduced visibility, owls, and higher tharn risk. For it: far fewer vehicles, no hawks, a quieter Margin, and almost no human activity. The Fifth Law names the exchange.
- **Dawn Reckoning:** food consumption, healing progress, structural wear, regrowth, Construction Queue progress, scheduled events, and calendar advancement resolve.

<!--@9.1¶5-->
Time of day is an in-game system, not tied to the player's real-world clock.

<!--@9.2-->
### 9.2 Traffic cycles

<!--@9.2¶1-->
- **Rush:** dense, slower vehicles; fewer clean gaps, strong fumes, vibration, noise, stop-start unpredictability. Sets the River's Spume to **Exhaust**, and reinforces **Heat** in summer through idling engines.
- **Lull:** moderate density and speed; visually readable but exposed to raptors.
- **Night Velocity:** few vehicles at very high speed; headlights, darkness, spatial audio, and tharn risk dominate. Reinforces the Spume's **Cold** manifestation in winter. A highway after dark is one of the most illuminated environments there is — sodium vapour, headlight wash, brake-light red, reflective signage, all of it doubled in wet asphalt (Section 34.1).
- **Anomaly:** an accident, lane closure, weather event, convoy, maintenance crew, or unusual lull temporarily rewrites the pattern. This wildcard produces the rare **Oil Leak** Spume, and can stop traffic outright — opening a crossing window that does not otherwise exist, and spilling cargo into the Margin as a windfall.

<!--@9.3-->
### 9.3 Traffic behaves like weather

<!--@9.3¶1-->
**INFOGRAPHIC — Traffic as Weather**

<!--@9.3¶2-->
Traffic is a dynamic environmental system rather than a row of predictable moving platforms. Density, speed, vehicle class, wind shear, headlights, spray, thrown debris, pollution, accidents, and Road Work produce changing conditions that can be read but never made perfectly safe. Traffic-as-weather effects are present across all Margin nodes, with intensity scaling by proximity to the highway edge — the mechanical face of the Road-edge / Wall-edge contrast (Section 7.4): Wind Draft and the River's Spume grow worse toward the pavement and fall off toward the interior.

<!--@9.3¶3-->
**Manifestations.** Three named hazards, all reskins of existing systems:

<!--@9.3¶4-->
- **Wind Draft** — gusts thrown off passing vehicles, strongest at the road edge and scaling down by proximity.
- **The River's Spume** — the standing ambient hazard. Unlike a rolled encounter, the Spume is a **constant presence near the highway**; what changes is its texture, set by the current traffic cycle and season rather than randomized per visit. Six manifestations, each keyed to a distinct state:
  - **Heat** — Summer, reinforced near Rush-hour engine idle. *"The River's Spume is hot today, battering you with hot wind."*
  - **Cold** — Winter, reinforced by Night Velocity's darkness and exposure.
  - **Exhaust** — the Rush cycle. Hard to breathe.
  - **Oil Leak** — the rare one, keyed to the Anomaly cycle. Smells foul.
  - **Chemical** — Spring: salt runoff, herbicide, fertiliser drift. Taints what grows.
  - **Dust** — Autumn: chaff, leaf litter, grit. Reduces visibility.
- **Litter** — the discrete counterpart to the Spume's constancy: human detritus arrives occasionally rather than persisting, as a **Choice-Event Card** in Field Mode (Section 10). Salvage it for potential item value, or let it pass — it is travelling at highway speed and can injure a citizen who engages it carelessly. Risk and reward are the same object.

<!--@9.3¶5-->
Wind Draft and the River's Spume both feed the **weather modifier** in encounter resolution (Section 26.4).

<!--@9.3¶6-->
---

<!--@10-->
## 10. Choice-Event Cards

<!--@10¶1-->
**INFOGRAPHIC — Choice-Event Cards**

<!--@10¶2-->
**Choice-Event Cards** are the game's unified event layer — **one system with two homes** rather than two event systems — and they sit ahead of Seasons and Road Work because everything downstream of them plays through this one interface. A card presents a situation and a small set of costed responses — *Reinforce the Drainage* (−wood), *Move the Supplies* (−time), *Do Nothing* — and resolves into consequence. This is the player-agency event layer above and beyond Road Work.

<!--@10¶3-->
**Colony mode.** Weather, seasonal, social, and opportunity events arrive at the Home Median and at outposts. These carry the real costed decisions, and they are the primary reason the domestic layer has surprises in it at all. A **wandering core-species joiner** arrives this way (Section 18.4).

<!--@10¶4-->
**Field mode.** Occasional **random-encounter cards** appear during traversal — a light interstitial layer *between* structured node encounters, never a replacement for them. Kept deliberately occasional so node design is not diluted into a card shuffle. **Litter** is the flagship Field card (Section 9.3).

<!--@10¶5-->
**A card may open, stay open, and close later** — the response chosen now, the consequence landing after. Ongoing cards remain on the Community Board while they run.

<!--@10¶6-->
**Rules governing the whole system:**

<!--@10¶7-->
- **No numeric countdowns anywhere.** The non-numeric telegraph rule governs the entire event system, not Road Work alone. Every telegraph is qualitative and diegetic — a smell, a sound, a changed sky, a Guest's unease. Nothing anywhere in MEDIAN tells the player "3 days until X."
- **Road Work modifies the pool** rather than spawning a parallel event track.
- **The Groundhog Ambient Guest** is the in-fiction warning system for approaching cards (Section 21.2).
- **Outcomes feed the Records** as dated, named entries.
- **Restraint.** These are events, not nags. Frequency must stay low enough that a card is an occasion.

<!--@10¶8-->
---

<!--@11-->
## 11. Seasons and Road Work

<!--@11.1-->
### 11.1 Seasons

<!--@11.1¶1-->
**INFOGRAPHIC — The Turn of the Seasons**

<!--@11.1¶2-->
**ARTWORK — The Four Seasons at Home**

<!--@11.1¶3-->
Season length and campaign duration require playtesting. Seasons should be long enough to establish a distinct operating rhythm, not flip every few sessions. Seasons drive the Perishable/Durable sustenance split (Section 14) and set the ambient texture of the River's Spume.

<!--@11.1¶4-->
- **Spring — Thaw and Growth:** rain, flooding, rapid Margin regrowth, abundant greens, and the first **Nesting Season** of the year. Sets the Spume to **Chemical**.
- **Summer — Pavement Heat:** dehydration pressure, heat plumes, exposed-day penalties, marginally higher chance of Road Work. Sets the Spume to **Heat**.
- **Autumn — Detritus Harvest:** strong winds deliver scrap and seeds; stockpiling, and a possible second **Nesting Season**. Sets the Spume to **Dust**.
- **Winter — Freeze and Reserve:** low local forage, expensive warmth, draft and exposure risk, reliance on preparation. Sets the Spume to **Cold**. Snake Guests take a movement penalty.

<!--@11.1¶5-->
**Nesting Season** is the breeding window. It is the only time a **Hearth** can bring a new named citizen into the world, and it remains rare, expensive, and player-authorized (Section 18.3).

<!--@11.2-->
### 11.2 Road Work

<!--@11.2¶1-->
**INFOGRAPHIC — Road Work**

<!--@11.2¶2-->
**ARTWORK — Road Work: Telegraph, Onset, Persistence**

<!--@11.2¶3-->
**Road Work** is a family of municipal disturbance events — mowing, vegetation clearing, salt application, drainage work, barrier repair, resurfacing, construction staging, trash collection, lane reconfiguration. It functions like severe weather at the campaign scale and is one of the game's signature systems.

<!--@11.2¶4-->
In the animals' own vocabulary, an ordinary survivable instance is **the Mowing**, and the Second Law — *"the mowing is fire"* — is how the colony teaches its young to survive one.

<!--@11.2¶5-->
**Cadence and telegraph.** Road Work is decoupled from the season calendar — not a scheduled seasonal event — though summer carries a marginally higher chance. It is telegraphed *only* through subtle visual changes in the Margin (survey marks, disturbed ground, distant machinery, changed smell and vibration), **never through a numeric warning or countdown.**

<!--@11.2¶6-->
**Severity.** When Road Work strikes, the **Margin is fully wiped.** Severity *within the Median* scales with the Reach's Anchor Points and cover — a well-covered, root-anchored Reach weathers it better than an exposed one.

<!--@11.2¶7-->
**Road Work is local; disruption is not.** The physical work strikes one Reach. The card-pool modifier and the raised event frequency apply corridor-wide, so no Reach is insulated. A resurfacing programme may strike several Reaches in sequence.

<!--@11.2¶8-->
**Three phases:**

<!--@11.2¶9-->
1. **Telegraph.** Subtle Margin visual changes, no numeric warning.
2. **Onset.** A group-layer resolution (Section 26.4) for any citizens caught present — a single round, no Approach, no Turn. Citizens are exposed by circumstance rather than by choice.
3. **Persistence.** A bounded-duration altered-state window: a different soundscape, restricted and riskier expeditions, and construction machinery present as a distinct **environmental-hazard antagonist type** — something to evade or shelter from, never negotiated with or fought. The window's duration is **capped regardless of severity**; severity manifests as *intensity*, not length. The player can shorten it through active recovery work reusing the ordinary repair system.

<!--@11.2¶10-->
**Road Work reshapes the event pool.** While the persistence window runs, Road Work acts as a **card-pool modifier** on Choice-Event Cards: it tilts the pool toward hazard and disruption cards and raises event frequency.

<!--@11.2¶11-->
Road Work's recurring construction-equipment threat echoes the Founding Escape: the same class of machinery that destroyed the ancestral home returns to threaten the new one. The two are an **echo, not the same event** — the Founding Escape is a singular permanent apocalypse, while Road Work is cyclical and survivable.

<!--@11.2¶12-->
> **CREATED VISUAL — "The season the machines came back."** Catastrophic Road Work onset, at the Reach it struck, with the citizens caught in it. *Fallback: the event is written into the Chronicle.*

<!--@11.2¶13-->
---

<!--@4#2-->
# PART III — THE COLONY

<!--@4#2¶1-->
**ARTWORK — The Rabbit Warren**

<!--@4#2¶2-->
*The home the whole game is in service of: how it works, and what it builds.*

<!--@4#2¶3-->
---

<!--@12-->
## 12. Scale and the shape of a colony

<!--@12¶1-->
**INFOGRAPHIC — The Colony**

<!--@12¶2-->
This is a deliberately low-population colony game. A mature colony should still be small enough that the player recognizes every member by name (Pillar 2.2). Exact caps differ by species and tier, but population growth never becomes a continuous unit-production conveyor.

<!--@12¶3-->
A mature wood-mouse colony runs larger than a comparable rabbit or squirrel colony — on the order of one-and-a-half to two times the head-count — but stays within the same low, fully-named ceiling. **The difference is density, not anonymity.**

<!--@12¶4-->
Three paths grow a colony: **wanderers**, **Nesting Season** young, and **Guest Citizens**. The first two live with the citizens rather than here (Section 18.4). Stationing citizens at outposts moves them out of the home but never off the ceiling (Section 29.3).

<!--@13-->
## 13. Roles and daily work

<!--@13¶1-->
**INFOGRAPHIC — The Eight Roles**

<!--@13¶2-->
Citizens not on expedition are assigned a standing **Role** rather than being micromanaged task by task. A Role persists until the player changes it, and the game handles pathing and execution automatically. This is a batch-orders-and-priorities model, not click-per-task command.

<!--@13¶3-->
Eight Roles, each distinct, non-overlapping, and with **fixed, static output** — no leveling:

<!--@13¶4-->
- **Forager:** increases Sustenance yield; benefits from matching Anchor Points.
- **Caretaker:** reduces Perishable spoilage.
- **Builder:** reduces construction cost and time, slows structural decay, benefits from matching Anchor Points.
- **Healer:** speeds Wounded recovery.
- **Nursery Tender:** improves breeding-cycle conditions.
- **Watchkeeper:** improves Base Defense telegraph warning.
- **Crafter:** converts Scrap into finished goods and produces adaptive equipment for maimed veterans.
- **Teacher:** reduces colony-wide fear and stress, and speeds a young citizen's first-expedition readiness.

<!--@13¶5-->
**A Role's effect is identical no matter who holds it.** Assignments always produce visible action in the colony; the player watches the work happen rather than reading it off a menu.

<!--@13¶6-->
A new or unassigned citizen is a **Forager**.

<!--@13¶7-->
**The base-building layer never grows anyone.** A hard rule governs the relationship between domestic work and citizen development: the base-building layer is **personality-blind and never accesses individual growth.** All citizen development, without exception, happens through **expedition participation** (Section 26.5). This resolves the tension between static, legible Roles and the desire for citizens to feel like continuing, invested-in presences: the investment is real, but it is earned in the field, not at a workbench.

<!--@13¶8-->
**The Teacher's cultural work.** The Teacher is the colony's transmission mechanism for its own folklore — drilling the young in the Laws and repeating the Sayings, at the **Story Circle** (Section 16.3). This is the in-fiction reason the Role reduces colony-wide fear and speeds first-expedition readiness: the Laws are survival instruction in mnemonic form. The Teacher works from founding — fear reduction is active from the first day, and the readiness effect acts once there are young to ready.

<!--@13¶9-->
**Standing Tool assignment reuses this interface.** Assigning a citizen a **Tool** (Section 20) works exactly like assigning a Role: a persistent, colony-level decision made in the Colony register, changed when the player wants it changed, and never made at the Expedition Launcher. Role and Tool sit together on a citizen's Likeness (Section 22.2).

<!--@13¶10-->
**When both members of a Hearth hold the same standing Role, that work is slightly more efficient.**

<!--@14-->
## 14. Resources and the economy

<!--@14¶1-->
**INFOGRAPHIC — The Economy**

<!--@14¶2-->
**ARTWORK — A Colony Built Into a Wreck**

<!--@14¶3-->
The lean canonical economy has three regular categories plus a special class, and **no standalone currency layer**:

<!--@14¶4-->
1. **Sustenance** — food and hydration consumed by citizens, used for reserves, recovery, and rare reproduction. Forked into two sub-types:
   - **Perishable:** decays over time; abundant in spring and summer. *Berries, greens, insects, mushrooms, fallen fruit, fresh food scraps.*
   - **Durable:** stockpilable; the backbone of autumn and winter preparation. *Acorns and nuts, dried seeds, dried grass, preserved food scraps, dried mushrooms.*
2. **Flexible Scrap** — binding, weaving, lashing, sealing. *Copper wire, twine and packaging string, burlap and fabric strips, zip-tie fragments, plastic bag strips, rubber bands, shoelace lengths, fishing line.*
3. **Rigid Scrap** — bracing, shielding, surfacing, tools, load-bearing reinforcement. *Aluminum pull-tabs, bottle caps, smoothed glass pebbles, bread clips, popsicle sticks and wood splinters, tire-rubber fragments, small metal hardware, broken ceramic shards, gravel chips.*

<!--@14¶5-->
**The weight ladder.**

<!--@14¶6-->
| Class | Value | Examples | Who carries it |
|---|---|---|---|
| **Trifle** | 1 | Seed, crumb, bead, gravel chip | Anyone |
| **Small** | 5 | Acorn, bottle cap, pull-tab, berry cluster | One mouse |
| **Standard** | 10 | Grass bundle, large mushroom, coil of wire | A rabbit, or two mice at 12 |
| **Heavy** | 20 | Bread crust, folded fabric scrap | A squirrel, or two rabbits |
| **Cooperative** | 40+ | — | Two squirrels, four rabbits, seven mice |

<!--@14¶7-->
A pair of mice sharing one Standard item: six carried alone is not enough, twelve carried together is. The party's carry totals; anything within the total comes home, with heavy items visibly shared. An Almanac entry can name a haul the way a naturalist would — *six Smalls*, not sixty individual things.

<!--@14¶8-->
**Special Artifacts** are rare, tightly-limited objects that unlock a blueprint, solve a specific problem, enable a trade, improve an adaptive device, or open a narrative option. They are not generic "technology keys," and their uses must remain believable for animals. They operate at the **colony** level, distinct from the three citizen equipment slots (Section 20).

<!--@14¶9-->
Two classes of Artifact: **Colony Artifacts**, held by the colony — a blueprint unlocked, a trade enabled, a standing problem solved — and **Carried Artifacts**, which occupy a citizen's Tool slot and act in the field. Crafters make Tools from Scrap. One canonical Carried-Artifact effect worth naming: it may **grant an extra Turn in an encounter** (Section 26.7) — a non-numeric, situation-solving effect of exactly the kind this class exists for.

<!--@14¶10-->
The flagship crafted **Tool** comes straight out of the Rigid Scrap list: the **pull-tab-and-needle multitool**, assembled from an aluminum pull-tab and a scavenged needle. It is lent, returnable colony property rather than personal possession.

<!--@15-->
## 15. Construction, decay, and the Construction Queue

<!--@15¶1-->
**INFOGRAPHIC — Construction and the Queue**

<!--@15¶2-->
Structures visibly age through moisture, rot, wind, vibration, salt, heat, and use. Maintenance costs Flexible and Rigid Scrap on an ongoing basis, and fully-upgraded construction can reduce or eliminate routine decay in a limited footprint. The objective is meaningful stewardship, not a universal repair tax. Biomes wear differently: the **Culvert Garden** rots timber, the **Concrete Trench** bakes and cracks, the **Pond Hollow** damps, and the **Thin Grass Ribbon** scours with wind.

<!--@15¶3-->
No single decay formula is canonical. Prototype using broad durability states and event-based wear before considering fine percentages. The same repair-and-maintenance system is reused as the player's counterplay against Road Work's persistence window.

<!--@15¶4-->
**The Construction Queue** is the single shared model for every building project. New construction, per-building upgrades (Section 16.2), and an outpost's securing clock (Section 28.1) are all **instances of the same system** rather than three bespoke timers.

<!--@15¶5-->
- **Duration is measured in whole days,** fixed per building and per rung, generally escalating at higher tiers.
- **Resources are spent at the start, and are sunk.** No refund, no partial recovery, no mid-build loss risk.
- **Projects are uninterruptible.** Nothing derails a started project — not Road Work, not a Choice-Event Card, not a world event. This is deliberate: **certainty lives in construction, and risk stays where it already lives, in expeditions.** The colony layer is where the player is allowed to make a plan that holds.
- **A building under construction goes offline.** It does not perform its function for the duration — an Infirmary being rebuilt provides no healing while the work runs. This is the real strategic cost of an upgrade; the queue is a set of decisions, not a set of wait timers.
- **There is no Speed-Up mechanic of any kind.** Time spent building is time spent, and nothing shortens it.
- **Queue slots scale with Colony Tier**, on the same one-per-Tier pattern Guest slots use.

<!--@15¶6-->
The queue is visible in the Colony register and expanded in the ledger overlay (Sections 33.1, 33.2).

<!--@15¶7-->
> **OPEN — Construction Queue day-values.** Duration per building and rung, the escalation curve, and the Establish-Outpost securing-clock duration — one instance of this same system (Section 28.1). · `500 log/open_items.md`

<!--@16-->
## 16. Structures and upgrade ladders

<!--@16.1-->
### 16.1 Structure families

<!--@16.1¶1-->
**INFOGRAPHIC — Structures and Upgrade Ladders**

<!--@16.1¶2-->
Shared functions are visually and spatially adapted to each species. The central hub carries a species-specific flavor name — **Warren** (rabbit), **Den** (squirrel), **Burrow** (mouse) — used as flavor and visual differentiation, not as a mechanical system. **These three words are species terminology and are never used generically** anywhere else in the game, including at the tier level (Section 32).

<!--@16.1¶3-->
**Species flavor extends to every structure family, not just the hub** — the central hub, the food store, shelter, and the lookout network each carry their own species-specific vocabulary. A single shared ladder covers the workshop, the infirmary, the nursery, the Staging Post, the Guest House, the Story Circle, the Community Board, and species-signature structures. So a squirrel colony and a mouse colony reading the same functional map still feel like different civilizations.

<!--@16.1¶4-->
The canonical families:

<!--@16.1¶5-->
- Town Center / communal heart (Warren / Den / Burrow).
- Food store and dry reserve.
- Workshop and scrap store.
- Shelter and sleeping chambers.
- Nursery sanctuary.
- Infirmary / recovery nest.
- **Staging Post** at the highway edge — the departure threshold, and the place a party dresses for the road (Sections 20, 34.1).
- Lookout and warning network.
- **Guest House** — accommodation for Guests of both tiers.
- **Story Circle** — the memorial and history venue (Section 16.3).
- **Community Board** — the colony's ambient notice board (Section 16.3).
- **Welcome sign** — the colony's name made physical (Sections 23.3, 35.2).
- Species-signature transport, storage, and safety structures.

<!--@16.1¶6-->
**The Guest House is one family with many faces.** Rather than sixteen bespoke structures for sixteen possible Guests, there is a single building family whose **skin and build location vary with its occupant** — a nest raised in a tree, a lodge at the water, a burrow beneath, named for each Guest alongside their roster entry (Sections 21.1, 21.2). This is a charm feature the game invests in, not a cost to minimize.

<!--@16.1¶7-->
**Placement is part of the expression, not incidental.** Where a Guest House sits is bound to the same spatial logic as everything else the colony builds — Anchor Points suit some occupants and not others (Section 8.2), and a Guest housed badly is housed visibly badly. If a Guest leaves or dies, the structure can be cleaned, adapted, or re-skinned for another compatible Guest.

<!--@16.2-->
### 16.2 Named upgrade ladders

<!--@16.2¶1-->
Every upgradeable family has a **named ladder of two to four rungs** in place of a numeric "Level 2" label. Two gates govern it:

<!--@16.2¶2-->
1. **Availability.** Some families do not exist until a given Colony Tier. Tier II's "recovery space" and Tier III's "adaptive equipment" capabilities are gates of exactly this kind.
2. **The internal ladder.** Once available, the player climbs named rungs by spending ordinary Flexible and Rigid Scrap on that specific building, through the Construction Queue. This is separate from colony-wide Tier advancement, though a building's reachable rung is **capped by the current Colony Tier.**

<!--@16.2¶3-->
**Register escalates but never industrializes.** Rung names are humble and functional at Tier I and read as genuinely grand by Tier IV — but the grandeur comes from scrap-mastery and civic complexity, never from electrification, machinery, or manufacture.

<!--@16.2¶4-->
| Family | Rung 1 | Rung 2 | Rung 3 | Rung 4 |
|---|---|---|---|---|
| **Rabbit Lookout** | Watch Mound | Ear Warren | Long Watch | High Warren |
| **Squirrel Food Store** | Cache Hollow | Drey Larder | High Cache | Canopy Hoard |
| **Wood Mouse Infirmary** (Tier II gated) | *unavailable* | Moss Nook | Mending Burrow | Warm Root Hall |

<!--@16.2¶5-->
Full per-family tables for the remaining families are **deferred to Appendix A.** The principle is settled; the vocabulary is not yet written.

<!--@16.3-->
### 16.3 Functional icons, the Community Board, and the Story Circle

<!--@16.3¶1-->
**INFOGRAPHIC — The Community Board and the Story Circle**

<!--@16.3¶2-->
**Flavor names must never cost the player legibility.** Every building carries a persistent, always-visible **functional icon** — Healing, Storage, Warning, Craft, Shelter — living in the **base Colony register**, *not* gated behind the ledger overlay. The overlay's building-function data is the detailed text expansion of that icon rather than its only source.

<!--@16.3¶3-->
This is one established pattern, not a new UI rule: flavor name plus functional metadata, shown together (Pillar 2.3).

<!--@16.3¶4-->
The colony has two diegetic information objects, deliberately **not** merged because they do different jobs at different tempos:

<!--@16.3¶5-->
- **The Community Board** is the **day-to-day operational feed**, *ambiently visible at all times* — read in passing without entering anything. It carries alerts, standing duties, foraging shares, scout returns, and active Choice-Event Cards. It is the diegetic face of the Almanac's event feed (Section 22.1). Road Work notices stay strictly qualitative — never "Mowing Tomorrow," never a countdown.
- **The Story Circle** is the **ceremonial venue**, and its content exists only when entered. It is where the Teacher recites the Laws and Sayings, where the Colony Record is read, where grief is processed after a Hearth loss, and where the colony's understated physical memorials stand. It has its own named upgrade ladder like any other family.

<!--@16.3¶6-->
Operational versus ceremonial, expressed spatially as well as tonally.

<!--@16.3¶7-->
---

<!--@5#2-->
# PART IV — THE CITIZENS

<!--@5#2¶1-->
**ARTWORK — Bramble, Sharpnose, and Daisy at the Story Circle**

<!--@5#2¶2-->
*Who lives in the colony, what happens to them, and how they are remembered. Guest Citizens are here, with the citizens they become; the procedure for recruiting them is in Part V, where recruitment actually happens.*

<!--@5#2¶3-->
---

<!--@17-->
## 17. The citizen record

<!--@17¶1-->
**INFOGRAPHIC — The Citizen Record**

<!--@17¶2-->
Every citizen has a **Citizen Record** (Section 22.2), presented in two views — a **Likeness** for facts and a **Tale** for history.

<!--@17¶3-->
A citizen's Likeness carries:

<!--@17¶4-->
- **Given Name** and, if earned, **After-name** — two distinct name fields (Section 23.1).
- Species, appearance, and portrait.
- Age / life stage.
- **Bonds** — Trusted Friends and Hearth membership, named and characterized.
- A randomized personality trait, assigned at birth, unrelated to lineage.
- Broad visible aptitude descriptors, in the descriptive bands (Appendix D).
- Traits, learned history, and current standing Role.
- **Three equipment slots — Keepsake, Tool, and Supply** (Section 20).
- Expedition and colony-work history, with each expedition's Rating.
- Wounds, permanent impairments, adaptive equipment, and fear memories.
- Permanent **Distinctions** earned in the field (Section 19.3).
- Notable acts, discoveries, relationships, and memorial links.

<!--@17¶5-->
Underlying values may include movement, carrying, stealth and noise, perception, resilience, stress threshold, and social aptitude. **Exact values remain hidden.** Players see descriptive bands, clear consequences, and history rather than raw ratings.

<!--@18-->
## 18. Bonds, Hearths, and growth

<!--@18.1-->
### 18.1 Bonds

<!--@18.1¶1-->
**INFOGRAPHIC — Bonds, Hearths and Nesting Season**

<!--@18.1¶2-->
Citizens form **named, characterized bonds** that appear on their Records — *"Bramble and Twig — best friends"*, *"Sharpnose and Nutmeg — partners in crime"*, *"Daisy and Fennel — inseparable since the culvert"* — rather than accumulating on an invisible affinity meter. There is no relationship simulation and no visible relationship number; bonds are displayed descriptively and change through events, never through a tracked score.

<!--@18.1¶3-->
Two tiers:

<!--@18.1¶4-->
- **Trusted Friend.** Formed by a shared significant experience: surviving an expedition together, one rescuing the other, one leading the other out of tharn. Trusted Friend bonds form between core citizens and Guests alike. The displayed phrasing varies by the pair and by how the bond formed.
- **Hearth.** A family unit, formed when Trusted Friends accumulate *another* such experience together. Usually a pair, but it can take others in — an orphaned young citizen, a maimed veteran with nowhere else. **A Hearth is a found family**, and it is core-species only: the Hearth is the lineage unit, the Trusted Friend is the found-family unit that crosses to Guests.

<!--@18.1¶5-->
Bonds carry only the effects canon already implies: companions reduce each other's tharn risk when travelling together, a death produces grief in the survivors, and a Keepsake may be gifted within a living Hearth. Nothing else.

<!--@18.2-->
### 18.2 Hearths and lineage

<!--@18.2¶1-->
A **Hearth** is the unit that can bring a new named citizen into the world, and only during a **Nesting Season** (Section 11.1).

<!--@18.2¶2-->
**A Hearth that produces a child acquires descent — as a story fact, and only as a story fact.** The child's Tale records that they were **"born of [Hearth]"**, and the colony remembers who came from whom. Nothing whatsoever transmits mechanically. The child receives a **randomized personality trait unrelated to lineage**, exactly as every other citizen does.

<!--@18.2¶3-->
This distinction is load-bearing and is stated in both directions: **the fiction has families; the simulation has no heredity.** There is no genetics, no bloodline ledger, no inherited aptitude, no skill tree, and no breeding-optimization system. Hearths do not introduce one by the back door — they are a narrative structure sitting on top of an unchanged, lineage-blind trait roll.

<!--@18.2¶4-->
**Hearths are less deployable.** Bonded families trade flexibility for warmth, and the game states the trade openly:

<!--@18.2¶5-->
- **A Hearth cannot be split for solo outpost duty.** Hearth members are ineligible for solo stationing (Section 29.3).
- **A full Hearth may relocate together** to an outpost with two or more citizen slots.

<!--@18.2¶6-->
The colony's most emotionally settled citizens are therefore its least mobile, which deliberately puts the population pressure-valve and the cozy social layer in tension.

<!--@18.2¶7-->
**Grief.** When a Hearth member dies, survivors take a temporary **Shaken** state plus a persistent **fear memory** tied to the loss (Sections 19.1, 19.2). The Shaken state fades on its own; the fear memory is mitigable through the Teacher Role and time spent at the memorial in the Story Circle.

<!--@18.3-->
### 18.3 Nesting Season

<!--@18.3¶1-->
Core-species reproduction is rare, seasonal, expensive, and player-authorized.

<!--@18.3¶2-->
- A mating opportunity exists only in suitable seasonal and colony conditions.
- Two citizens are committed to care and cannot be treated as normal expedition labor during the critical period.
- Sustenance, shelter, safety, and space requirements are substantial.
- A successful cycle yields a very small number of named young, and the low-population ceiling is untouched.
- **The player is never encouraged to breed disposable replacements.**

<!--@18.3¶3-->
Exact biology can be stylized consistently across species to protect pacing. Each new citizen receives a **Given Name** at birth (Section 23.1), framed in-fiction as a name gifted by the Hearth.

<!--@18.4-->
### 18.4 Wanderers — the other way a colony grows

<!--@18.4¶1-->
**INFOGRAPHIC — Wanderers**

<!--@18.4¶2-->
A founding trio plus rare seasonal births is a very slow curve. **Displaced core-species wanderers are the primary early-game growth path**, with Nesting Season staying the rarer and more emotionally weighted one.

<!--@18.4¶3-->
**A wanderer joins as an ordinary named Citizen** — not a Guest, occupying no Guest slot, with full equal standing, a Given Name, a personality trait, and a Citizen Record from the moment of arrival. Adopting one costs no Guest slot, no amenability check, and only a lighter residence cost than a Guest recruitment. They are of the colony's own species; the colony's found-family beat lives in the Guest system instead (Section 21).

<!--@18.4¶4-->
Three arrival routes, all reusing existing systems:

<!--@18.4¶5-->
- **Expedition encounter**, on the contest funnel's non-antagonist branch (Section 27.2) — parallel to Guest recruitment but resolving to a Citizen.
- **Rescue**, from a hazard or a Road Work event.
- **A Choice-Event Card at the colony** (Section 10) — a stranger at the edge of the median, with a costed decision about taking them in.

<!--@18.4¶6-->
Every wanderer carries a backstory reason for being alone. That reason is what keeps them from reading as spawned units, and it is written into their Tale on arrival.

<!--@18.4¶7-->
**The flagship case: another survivor.** A wanderer may be **another survivor of the Founding Escape.** The trio's belief that they alone came through is therefore wrong, and the game can deliver that as an event — potentially years into a campaign. Such an arrival may also carry **a Law the trio remembered wrong**, which is the payoff for the imperfect folklore the colony has been teaching its young since the first day (Section 6.1).

<!--@18.4¶8-->
> **OPEN — Wanderers.** Arrival rate and whether it scales with Tier; whether a wanderer can be refused and at what cost; whether wanderers can arrive already maimed or fearful. · `500 log/open_items.md`

<!--@18.5-->
### 18.5 Death and memorialization

<!--@18.5¶1-->
**ARTWORK — The Memorial**

<!--@18.5¶2-->
Death is possible but uncommon outside catastrophic errors or extreme events. It should never become the routine expected price of ordinary expeditions.

<!--@18.5¶3-->
When a citizen dies, their **Citizen Record** — Likeness and Tale both, with portrait, relationships, and full history intact — moves into the colony's memorial archive rather than being deleted. **A Tale is closed, not erased**, and remains readable.

<!--@18.5¶4-->
Their **Keepsake** returns to the colony's shared stock as an inheritable memorial object (Section 20): a thing another citizen may one day carry, with the provenance of who carried it first recorded in the new holder's Record. This is the game's quietest continuity mechanic and one of its most important.

<!--@18.5¶5-->
The player may place an understated physical memorial in the Home Median. Memorials are placed **at the Story Circle**, which makes the ceremonial venue the place where loss is both marked and, over time, processed.

<!--@18.5¶6-->
---

<!--@19-->
## 19. Harm, fear, and tharn

<!--@19¶1-->
**INFOGRAPHIC — Harm, Fear and Tharn**

<!--@19.1-->
### 19.1 The harm ladder

<!--@19.1¶1-->
**ARTWORK — A Maimed Veteran, Valued**

<!--@19.1¶2-->
1. **Shaken / exhausted:** short recovery, reduced readiness. Also the state produced by grief at a Hearth member's death.
2. **Wounded:** meaningful temporary impairment requiring rest, food, care, and multiple days to heal.
3. **Maimed:** permanent bodily change with lasting functional consequences.
4. **Death:** rare, final loss.

<!--@19.1¶3-->
Maiming has weight because it changes what a citizen can safely do, not because it converts them into dead weight. Physical limitations remain real and visible; experience, relationships, knowledge, and emotional importance remain intact.

<!--@19.1¶4-->
Adaptive equipment, produced by the Crafter Role, **reduces a maiming's penalty and never grants a capability the citizen did not have.**

<!--@19.1¶5-->
> *The mending is not the making.*

<!--@19.1¶6-->
A maimed citizen may still expedition when the player judges the route and role appropriate, and some veterans — precisely because they have survived — become calm expedition anchors who reduce tharn risk in less-experienced companions.

<!--@19.1¶7-->
Adaptive equipment is a **fourth**, separate thing from the three citizen equipment slots: it offsets a specific impairment and is not chosen, lent, or swapped.

<!--@19.2-->
### 19.2 Fear and going tharn

<!--@19.2¶1-->
**ARTWORK — Going Tharn**

<!--@19.2¶2-->
Fear is a core system, not a cosmetic morale debuff. Stress accumulates through exposure to traffic, predators, darkness, noise, injury, exhaustion, separation, and recalled trauma. A fear memory is tied to the species that caused it. When a citizen exceeds their threshold they may go **tharn**: freezing, dropping carried items, failing to obey movement commands, and requiring rescue or calming intervention.

<!--@19.2¶3-->
Tharn is a rare, dramaturgically forefronted freeze-event, deliberately kept *distinct* from the Distinction/Maiming economy. It is available to all three core species — not rabbit-exclusive — each with its own thematic flavor.

<!--@19.2¶4-->
**Trigger.** A citizen goes tharn when their **exposure exceeds their stress threshold** during an encounter (Section 26.5). This is a single unified trigger built on machinery that exists only inside an encounter, with per-species flavor in how the freeze *manifests* rather than in what causes it. Load and isolation both feed it without needing triggers of their own: load raises exposure directly, and a citizen whose exposure has spiked far above the party's is, definitionally, the one out there alone.

<!--@19.2¶5-->
**Effect inside the encounter.** The tharn citizen stops contributing to the party's score, drops carried cargo, and their exposure continues climbing each round until they are resolved. The frame centres on them by name, and the next Turn is forced and scoped to the tharn: it presents the party members who could go, and the player chooses one.

<!--@19.2¶6-->
> *We do not leave what we can carry.*

<!--@19.2¶7-->
Tharn does not fire on a final round. Losing a citizen to untended tharn happens through deliberate abandonment or an impossible position, not through inattention.

<!--@19.2¶8-->
**Forced Withdrawal.** When a citizen goes tharn and sending a rescuer would leave nobody still in the encounter, the encounter ends there: the one still standing brings them out, the node is unresolved, and both come home. The trigger is the absence of a third body, not a party size or a Tier, so it also fires for a three-unit party that has already lost someone to a pin, a wound, or an earlier tharn. Withdraw, always permanently available (Section 26.2), fires here without being chosen. The encounter's Rating is **Failed**; exposure cuts party-wide as any Withdraw does, so nobody is maimed by this and nobody dies, and the tharn citizen's cargo drops.

<!--@19.2¶9-->
An under-strength run can end exactly this way: two citizens set out, one goes tharn at a node, and the one still standing carries them both home. The two come out of it bonded — leading a companion out of tharn is, as it already is, a bond-forming event (Section 18.1).

<!--@19.2¶10-->
Surviving tharn can create a persistent fear memory tied to a trigger. Recovery, trusted companions, experience, a veteran anchor, and certain Guest effects can mitigate future risk. **Trauma never simply converts into a numerical bonus.**

<!--@19.2¶11-->
**Fear memories also arise from grief** (Section 18.2), using this same system and mitigated the same ways.

<!--@19.2¶12-->
> **CREATED VISUAL — "Fennel, after the culvert."** At the permanent-change passage. **CREATED VISUAL — "Sharpnose goes tharn."** At the tharn passage. *Each carries its fallback in one line.*

<!--@19.2¶13-->
> **OPEN — Fear and tharn.** The numeric threshold values, and whether Crossing — an action mode, not an encounter — needs its own tharn trigger. · `500 log/open_items.md`

<!--@19.3-->
### 19.3 Distinctions, the symmetry, and the After-name

<!--@19.3¶1-->
Permanent *positive* traits — **Distinctions** (also "Feats") — mirror permanent *negative* traits structurally. Both are rare, discrete, earned through expedition participation, and both **accumulate over a career** — neither is gated to once-per-life or once-per-Tier.

<!--@19.3¶2-->
Distinctions are tied to the rare *good* tail of the outcome distribution, exactly the way Maiming is tied to its rare *bad* tail, and both are scoped entirely within the expedition-only rule: a citizen who never expeditions again earns no further Distinctions.

<!--@19.3¶3-->
**The symmetry has a shared driver.** Both tails are opened by the same thing — **exposure** (Section 26.5). The citizen who stuck their neck out is the one who comes home changed, in one direction or the other. A citizen who did nothing remarkable gets nothing remarkable, good or bad.

<!--@19.3¶4-->
**A citizen's first Distinction also grants their After-name** — the earned epithet that joins their Given Name and is used thereafter throughout the Records and the interface (Section 23.1). Later Distinctions accrue normally but do **not** churn the displayed name; the first one is the one that names you.

<!--@19.3¶5-->
> *Sharpnose's Tale, entry the ninth: for what she did at the culvert the night the water rose, the Circle names her Sharpnose Flood-wise, and the Distinction and the name are written as one line.*

<!--@19.3¶6-->
Most citizens never earn one. A citizen who stays home never will, and most who do expedition never hit the rare good tail. **This is intended rather than a gap** — an After-name means something precisely because the colony contains animals who do not have one.

<!--@19.4-->
### 19.4 How citizens develop

<!--@19.4¶1-->
Individual progression is deliberately narrow. Continuous, passive skill growth is **not** adopted. The sole individual-progression path is the discrete **Distinction / Maiming / Wounding** system — earned in the field, never at home.

<!--@19.4¶2-->
Separately and independently, there is one colony-wide progression event: **when the Colony graduates to a new Tier, every citizen receives a stat bump.** This is a property of the colony's advancement, distinct from any individual's history, and it applies to everyone at once.

<!--@19.4¶3-->
---

<!--@20-->
## 20. Equipment: Keepsake, Tool, and Supply

<!--@20¶1-->
**INFOGRAPHIC — Keepsake, Tool and Supply**

<!--@20¶2-->
Every citizen has **three equipment slots**. All three feed the equipment modifier in encounter resolution (Section 26.4) — three named sources filling one slot.

<!--@20¶3-->
All three are backend-numeric and **player-facing descriptive**: the interface says *"unsettles birds,"* never *"+3 versus Avian."* Effects are **small and situational**. They tilt a resolution; they never dominate one. There are no build-defining stacks, and no combination should ever feel like the reason an expedition succeeded. A number is only shown where the underlying stat is already public — colony-level carry and capacity figures, never a citizen's hidden aptitude or contest odds (Section 27.1).

<!--@20¶4-->
**Keepsake — personal, permanent, non-transferable.**
A Keepsake belongs to one citizen and characterizes them. It travels automatically with zero preparation, and always carries some small situational effect. The slot may start empty and fills through history: found in the field, inherited from the dead, or **gifted within a living Hearth** — that last path scoped deliberately to bonded family, so a gift means something. Each founding citizen may begin with one carried out of the old home.

<!--@20¶5-->
On death, a Keepsake **drops into the colony's shared stock as an inheritable memorial object**, and its provenance travels with it into whoever carries it next (Section 18.5).

<!--@20¶6-->
**Tool — colony property, lent out and returned.**
A Tool is a persistent, citizen-level assignment drawn from shared colony stock, **assigned at the colony-management level, never at the Expedition Launcher.** It uses the same standing-assignment interface as Roles (Section 13) — a decision about the colony, not about a mission. It can be reassigned or returned to stock exactly like lending out a physical object, because that is what it is. A **Carried Artifact** also occupies the Tool slot (Section 14).

<!--@20¶7-->
**Tools live at the Staging Post**, where a departing party also takes up its road dress (Section 34.1). The building at the highway edge is therefore the colony's threshold in a fuller sense than geography alone: it is where citizens stop being at home.

<!--@20¶8-->
The flagship example is the **pull-tab-and-needle multitool** (Section 14).

<!--@20¶9-->
**The slot is called Tool and not "Weapon," and the distinction is deliberate rather than cosmetic.** A slot named Weapon would invite exactly the weaponization this design excludes. Animals in MEDIAN use objects; they do not arm themselves.

<!--@20¶10-->
**Supply — per-run, per-citizen, consumable.**
A Supply is drawn from colony stock and chosen at the **Expedition Launcher**, one per departing citizen, for that run only. Its effect lives for the duration and then it is gone.

<!--@20¶11-->
This is the *only* one of the three the Launcher ever surfaces, which keeps the per-citizen picking burden at exactly one choice (Section 28.2). It is also the slot with a visible moment of use: **playing a Supply is a Turn action inside an encounter** (Section 26.4), which is what the slot exists for. On a citizen's Likeness (Section 22.2), Tools persist until changed or returned, and a Supply lasts one expedition, picked at the Launcher — the same distinction stated as a spread.

<!--@20¶12-->
**Distinct from neighboring systems.** Special Artifacts are colony-level (Section 14); adaptive equipment offsets maiming and is produced by the Crafter (Section 19.1). Neither is a slot, and a citizen may hold all of the above at once.

<!--@20¶13-->
---

<!--@21-->
## 21. Guest Citizens

<!--@21¶1-->
Guest Citizens are rare, named, non-breeding animals from outside the colony's core species. Inspired directly by Kehaar in *Watership Down* — a designer-facing reference; no *Watership Down* name appears in MEDIAN's own fiction (Section 6) — the system brings a wide variety of animal life into a campaign without requiring every species to support a full civilization ruleset. Each campaign is one species (Section 4), and this is where the found-family beat lives.

<!--@21¶2-->
**Every recruited Guest is a full, equal-status, named citizen** — not a subordinate, not a unit. They have Citizen Records, bonds, Keepsakes, Distinctions, and After-names like anyone else. They differ from core citizens in exactly two ways: they occupy their own separate capped slot pools, and they arrive through recruitment rather than birth. A joining Guest receives a **Given Name** (Section 23.1) — and carries it *from the first encounter*, before any decision to recruit. The player meets a named animal, not a candidate.

<!--@21¶3-->
Guests are housed in the **Guest House**, one building family whose skin and placement vary with its occupant (Section 16.1).

<!--@21¶4-->
Two tiers: **Active Guests** and **Ambient Guests.**

<!--@21¶5-->
*The procedure for recruiting a Guest — the contest funnel, the amenability check, the residence cost, and the slot cap — lives in Section 27, because recruitment happens in the field.*

<!--@21.1-->
### 21.1 Active Guests

<!--@21.1¶1-->
**INFOGRAPHIC — Active Guests: The Seven**

<!--@21.1¶2-->
**ARTWORK — Guest Vignettes**

<!--@21.1¶3-->
Active Guests join expedition parties, occupying a valuable slot and introducing a bounded ability, traversal option, defensive behavior, negotiation route, or information advantage. They do not remove the core citizens' need to take risks.

<!--@21.1¶4-->
The **universal contribution rule** holds with **zero exceptions**: every citizen, Guest included, contributes on *both* carry and fight to some non-zero degree, so no recruit is ever pure dead weight outside its specialty.

<!--@21.1¶5-->
**An Active Guest occupies one body-unit** (Section 4.4), displacing one rabbit, one squirrel, or two mice.

<!--@21.1¶6-->
| Standard Party with a Guest | Composition |
|---|---|
| Rabbit | 2 rabbits + 1 Guest |
| Squirrel | 2 squirrels + 1 Guest |
| **Wood Mouse** | **4 mice + 1 Guest** |

<!--@21.1¶7-->
A Guest's nominal carry is 10, matching a rabbit — but most Guests are not 10. Larger Guests exceed it and smaller ones fall short: the Raccoon carries 14, the Mink 12. The core species hold the tidy figures; outsiders do not, which is most of the point. Non-round party totals are harmless, since cooperative carrying uses combined capacity with no per-item bookkeeping (Section 14).

<!--@21.1¶8-->
**Guests are option-openers, not stat sticks.** This is the roster's governing design premise: a Guest modifies the **available options** in an encounter rather than the score.

<!--@21.1¶9-->
Every Active Guest carries three things:

<!--@21.1¶10-->
| | |
|---|---|
| **A benefit that travels** | Something the Guest does anywhere, on any ground. |
| **An affinity** | A node type where the Guest is extraordinary, and what it opens there. |
| **A complication** | Something the Guest **does** that costs the party. |

<!--@21.1¶11-->
Affinity attaches to **node types** — water hazards, sealed human containers, Margin pockets, Anchor Point nodes (Section 25.3). The affinity is an option-opener, never a multiplier; the travelling benefit is the substantial one, so the Launcher never becomes a matching puzzle (Section 28.2). A complication names something the Guest **does**, never an absence of benefit — no Guest is ever merely weak in the wrong place.

<!--@21.1¶12-->
**Worked example — the Mink.** Travels: retrieval from places nothing else reaches. Affinity, water hazards: rescue from water, culverts and drainage. Complication: she does not wait to be sent — at a water node she goes, and the forced Turn resolves without the player choosing who rescues.

<!--@21.1¶13-->
The known affinities among the rest of the roster:

<!--@21.1¶14-->
| Guest | Affinity | Dwelling |
|---|---|---|
| **Raccoon** | **Sealed human-container nodes** — latched coolers, zip-tied bags, capped bottles, bins (Section 25.3) | A raised box against the trunk |
| **Crow** | Aerial scouting — reveals a node's Approach set before the party commits | A nest raised in the canopy |
| **Fox** | Windfall processing — the only Guest that can safely render a predator kill or major roadkill into usable resources | An earth at the colony's edge |
| **Weasel** | Contest against small predators | A den worked into the bank |
| **Hedgehog** | Contest above the party's weight; durable escort and cover | A hollow under the hedge line |
| **Snake** | Parley by intimidation and display | A warm stone shelter, south-facing |
| **Mink** | Rescue from water, culverts, and drainage (worked above) | A lodge at the waterline |

<!--@21.1¶15-->
**Seven Guests against four slots.** The roster exceeds the slot cap deliberately: the player fields a fraction of what exists, and passing on a good recruit costs something (Section 27.3).

<!--@21.1¶16-->
> **OPEN — The Guest roster.** A travelling benefit for each of the six Guests beyond the Mink; a complication for each that names something the Guest does; exact carry values for the remaining five; and how Weasel and Hedgehog behave on the antagonist side of their duality (Section 21.3). · `500 log/open_items.md`

<!--@21.2-->
### 21.2 Ambient Guests

<!--@21.2¶1-->
**INFOGRAPHIC — Ambient Guests: The Nine**

<!--@21.2¶2-->
Ambient Guests live at the Home Median or, once unlocked, at an outpost, providing a spatial passive effect while remaining visible residents with routines and relationships. The option-opener template does not apply to them, because they never enter an encounter.

<!--@21.2¶3-->
**Ambient Guests can be hurt.** They are threatened during Base Defense, Road Work onset and catastrophe exactly as core citizens are. WHOOT can be lost.

<!--@21.2¶4-->
The roster is nine:

<!--@21.2¶5-->
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

<!--@21.2¶6-->
**The sky is answered by a bird.** The Fifth Law splits it by time — *"Hawks own the day, owls own the night"* — and the roster splits the same way. The Owl holds the night and the Songbird the day, and the pair is the colony's only cover against what comes from above. It costs a capped slot, so sky-safety competes directly with Bee yield, Toad preservation and Firefly light.

<!--@21.2¶7-->
When several Ambient Guests live at home, the player may select one effect for a temporary **Cultural Focus** boost; the others continue providing their normal effects. Ambient Guests may be assigned to compatible outposts, one per outpost central building.

<!--@21.2¶8-->
**Template character — WHOOT.** The Owl's eventual flavor writeup uses a template character: **WHOOT**, a barred owl with a permanently weak wing who can no longer hunt on the move and has become a stationary watcher instead. WHOOT gives a warm, concrete backstory reason for the rule that the Owl stays passive and is never an escort — and doubles as a lived demonstration of Pillar 2.5 applied to a Guest rather than a core citizen: a maimed animal remains valuable, and finds the role that fits. Because Ambient Guests do not expedition, WHOOT's injury reads as pre-colony history rather than an in-system Maiming, and it neither grants nor requires an After-name.

<!--@21.2¶9-->
> **OPEN — Example citizens.** A wider set of writeups in the register of tabletop RPG sourcebook NPC entries. · `500 log/open_items.md`

<!--@21.3-->
### 21.3 Antagonist fauna, and the ones who can change sides

<!--@21.3¶1-->
Not every animal met in the field is a candidate for the colony. Some are simply threats.

<!--@21.3¶2-->
| Antagonist | Where it appears |
|---|---|
| **Rat** | Contested nodes and Base Defense. Antagonist only. |
| **Raccoon** | Contested nodes and Base Defense — and the Active roster. |
| **Weasel** | Contested nodes — and the Active roster. |
| **Hedgehog** | Contested nodes — and the Active roster. |
| Predators, territorial rivals, desperate scavengers, environmental obstruction | Throughout |

<!--@21.3¶3-->
**Three animals sit on both sides of that line.** The raccoon is the worked case: bigger and cannier than the Rat, a real threat at a contested node, and recruitable. It can be met as an enemy, met again as a neutral, and eventually brought home (Sections 27.2, 21.1) — carrying the same name throughout, so the player can tell it is the same animal.

<!--@21.3¶4-->
**Antagonist status in MEDIAN is a position an animal currently occupies, not always a fixed nature.**

<!--@21.3¶5-->
---

<!--@22-->
## 22. The Records

<!--@22¶1-->
**INFOGRAPHIC — The Records**

<!--@22¶2-->
The colony's story, and each citizen's story inside it, is a **first-class named system** rather than a log buried in a menu. It is called **The Records.**

<!--@22¶3-->
The Records exist because MEDIAN's central promise — that the player will know these animals by name and remember what happened to them — needs somewhere to actually live. Two registers mirror the two independent halves of encounter resolution (Section 26.5): what the group did, and what happened to each individual.

<!--@22¶4-->
**The Records are narrative-first and are not a resource.** They introduce **no Knowledge currency, no Story currency, and no new tracked stat of any kind.** Where a Record implies a mechanical effect — a Teacher passing knowledge, a story spreading to another colony — that effect routes through the Teacher Role (Section 13), rumors and intelligence at the Expedition Launcher (Section 28.2), or the Rest-Stop Metropolis (Part VI).

<!--@22¶5-->
Each Record has **two views**, named per scale:

<!--@22¶6-->
| Scale | Summary view (now) | Literary view (history) |
|---|---|---|
| **Colony Record** | **Almanac** | **Chronicle** — in-world, *"The Remembering"* |
| **Citizen Record** | **Likeness** | **Tale** — *"Bramble's Tale"* |

<!--@22¶7-->
Placing a factual summary beside a literary history is the "ledger and legible" pillar and the "stories over statistics" principle sitting side by side rather than in tension.

<!--@22¶8-->
**Styling convention.** Colony views take the definite article: **"The Almanac," "The Chronicle."** Citizen views are possessive: **"Bramble's Likeness," "Sharpnose's Tale."** The grammar carries the scale — the colony has *the* record; each citizen owns *theirs*.

<!--@22.1-->
### 22.1 The Colony Record — Almanac and Chronicle

<!--@22.1¶1-->
**The Almanac** is the at-a-glance state of the colony: founded date, founding members, all current citizens **by name**, greatest triumph, largest threat, next goal, Tier milestones, and a dated feed of named events.

<!--@22.1¶2-->
Almost all of it auto-populates. The player touches it in only three places: naming the colony once at founding, pinning a **Greatest Triumph**, and setting a **Next Goal**. It is not a journal the player writes.

<!--@22.1¶3-->
**The event feed names individuals, always.** "Nutmeg and Daisy healed Sharpnose," never "two citizens performed healing." This is not flavor text — it is the atomic data spine of the whole system, feeding the Chronicle's prose upward and the Community Board's ambient display outward, and it is the most direct expression of Pillar 2.2.

<!--@22.1¶4-->
**The Chronicle** is the same material told as history, in the storyteller's mythic and reverent register — the voice of the Laws and Sayings (Section 6). Its in-world name is **The Remembering**.

<!--@22.1¶5-->
The Almanac is read in the interface and glimpsed ambiently on the **Community Board**; the Chronicle is read at the **Story Circle**, entered deliberately (Section 16.3).

<!--@22.2-->
### 22.2 The Citizen Record — Likeness and Tale

<!--@22.2¶1-->
Every citizen has one, from birth or recruitment to death and after.

<!--@22.2¶2-->
**The Likeness** is the citizen's current state, enumerated in Section 17. Portrait, the three equipment slots, standing Role and current condition sit on one screen and are changeable in place — the game's equip screen. Tools persist until changed or returned; a Supply lasts one expedition, and is picked at the Launcher.

<!--@22.2¶3-->
**The Tale** is the accreting personal strand: every expedition and its Rating, every Distinction and Maiming and where it happened, fear memories and what caused them, how each relationship formed, which Keepsake they carry and who carried it before them, and which colony events they were part of. "Bramble's Tale" is a life, written as it is lived.

<!--@22.2¶4-->
On death, the Record moves to the memorial archive rather than being deleted (Section 18.5).

<!--@22.2¶5-->
**The Village Roster** (Section 33.3) is the index screen that lists every citizen and leads into their Record.

<!--@22.2¶6-->
**One record, two outputs.** The Citizen Record is the same structured description the optional portrait system reads from when regenerating a citizen's image after a permanent change (Section 34). There is one canonical history per citizen, and it produces prose and portrait alike.

<!--@22.2¶7-->
> **CREATED VISUAL — "Bramble's Tale, illustrated."** **CREATED VISUAL — "A Legendary return."** *Each with its fallback. The Tale fallback is mandatory: templated prose from recorded events, no model involved.*

<!--@22.3-->
### 22.3 Expedition Rating and the Report and Share debrief

<!--@22.3¶1-->
The post-expedition screen has two halves — a **Rating** and a **debrief** — and together they are the Records' principal event-generator, writing into the Colony Record and every participant's Citizen Record at once.

<!--@22.3¶2-->
**The Rating** is one of four diegetic grades, player-facing descriptive language and **never a score**. It is **derived** from the encounter model rather than authored by designer judgment (Section 26.5):

<!--@22.3¶3-->
| Rating | Condition |
|---|---|
| **Legendary** | Objective met **+** at least one high-exposure **good** tail — a Distinction, an Artifact, a Guest opportunity |
| **Successful** | Objective met, exposure resolving without significant individual consequence |
| **Hard-Earned** | Objective met **+** at least one high-exposure **bad** tail — the costly victory |
| **Failed** | Objective not met |

<!--@22.3¶4-->
The Rating reflects the **group** outcome. A clean failure simply reads as Failed, with nuance carried by the debrief text rather than by a fifth grade. Every Rating is written into the Chronicle as a dated entry, and into the Tale of everyone who went.

<!--@22.3¶5-->
**The Report and Share debrief** is the content half: what the party found, what was dangerous, what was newly mapped, who fell. It writes the Record entries, and it updates the corridor map and the Launcher's previews and rumors (Section 28.2) so that what the colony *knows* reflects what it actually saw.

<!--@22.3¶6-->
There is **no sharing bonus.** Map and preview updates are simply "you now know what you saw" — not a reward to be farmed. The debrief is narrative and informational only.

<!--@22.3¶7-->
---

<!--@23-->
## 23. Names

<!--@23¶1-->
**INFOGRAPHIC — Names**

<!--@23¶2-->
Naming in MEDIAN is a system with a stated rule at its center: **the player authors exactly one name in the entire game.** Everything else is generated, discovered, or earned. Nobody in this world names themselves.

<!--@23.1-->
### 23.1 Names of citizens — Given Name and After-name

<!--@23.1¶1-->
A **Given Name** arrives at inception — gifted by a Hearth at birth, or carried in by a wanderer or Guest. Every citizen has one: the founding trio, every citizen born in a Nesting Season, every wanderer, and every Guest — the last carrying theirs from the first encounter, before any decision to recruit.

<!--@23.1¶2-->
The non-generative baseline is a **species-specific name-component bank** — the same engine family as the place-name grammar below, where every legal name assembles from curated parts so the register is guaranteed structurally rather than policed afterward. An optional enhanced layer can generate names through the system in Appendix H, on exactly the same terms as portraits and Chronicle prose: an enhancement, never a requirement.

<!--@23.1¶3-->
An **After-name** is earned — the *Oakenshield* half of a name. It is granted by a citizen's **first Distinction** (Section 19.3). Once granted it sticks, and it is used from then on throughout the Records and the interface. Later Distinctions accrue normally without churning the name.

<!--@23.1¶4-->
*(The designer-facing term for this field is the agnomen; **After-name** is what the game says, because MEDIAN's folk register is deliberately homely and plain.)*

<!--@23.1¶5-->
Most citizens never earn one. This is the point, not a shortfall — an After-name means something precisely because the colony contains animals who do not have one.

<!--@23.1¶6-->
**The moment of the After-name** is written into the citizen's Tale automatically. If the optional generative layer is active, that moment is also a candidate for a still image — already covered by the existing splash trigger for "a Distinction earned" (Appendix H), not a new subsystem.

<!--@23.2-->
### 23.2 Names of places — the folk-name grammar

<!--@23.2¶1-->
Places in MEDIAN are named by **the world and by history**, not by the player.

<!--@23.2¶2-->
**The shared engine is a curated folk-name grammar.** Every legal place name assembles from blessed parts — an article, modifier banks (materials, flora, qualities, water, fauna-trace), landform suffixes, and a small set of patterns. Because every name is built from approved components, the register is guaranteed *structurally*; there is no post-hoc profanity filtering and nothing to police.

<!--@23.2¶3-->
**The register is tuned homely and plain, never ornate** — the *"The Hill / Bywater"* end of Tolkien rather than the elvish end. Twin Oaks. The Low. Stonemouth. Bramble Cross. The Long Verge. Animals have an intimate, working relationship with ground they cross on foot every day, and their names for it should sound like it.

<!--@23.2¶4-->
Two authorities produce names:

<!--@23.2¶5-->
1. **The world names the place (primary).** Generated names derive from a Reach's actual character — its biome, its Anchor Points, its hydrology, its lane count. A Reach with twin oaks at its heart gets named for them. The player mostly **learns** these names — from a Teacher, from rumor, from the Metropolis — rather than assigning them.
2. **History names the place.** Notable nodes acquire event-conferred names in the Chronicle's voice: *Sharpnose's Rest*, *The Burning*. A place can gain a second name over time as things happen there, layering memory onto geography. This is where the Records and the map touch.

<!--@23.2¶6-->
**A node earns an After-name from what happened there.** The Home Median earns one by being inhabited, and that After-name is the colony's name — the player's single naming act (Section 23.3). No other Reach receives one, Held or otherwise; nodes within a Reach continue to earn event-conferred names as above.

<!--@23.2¶7-->
**One name per place, plus tags.** A place has **one folk name** and, separately, **functional metadata** shown as Almanac tags — *interchange*, *five-lane*, *wooded*. Not a literal-versus-folk name pair; the same flavor-plus-function pattern used everywhere else (Pillar 2.3).

<!--@23.2¶8-->
The component banks are **deferred to Appendix B.** The engine and register are settled; the vocabulary is not yet written.

<!--@23.3-->
### 23.3 The one name the player authors

<!--@23.3¶1-->
**The player names exactly one thing in MEDIAN: the Home colony.** Note that this is the *colony*, not the *Median* — the Home Median is a Reach and receives its own generated folk name like any other (Section 7.2). A colony called Horizon Fields may stand on ground the corridor has always called The Long Verge.

<!--@23.3¶2-->
Even that one name is a **curated pick, not a composition**:

<!--@23.3¶3-->
- **Choose one of three generated names**, offered one from each of three registers at founding: **Grounded** (biome-realistic, the same homely-plain grammar as every other place name), **Aspirational** (new-beginning, horizon-facing), and **Tribute** (remembering the Ancestral Warren, Den, or Burrow). Each reroll keeps the shape — one candidate per register, freshly generated. Both Grounded and Aspirational carry a **species-metaphor layer** — rabbit, squirrel, and mouse each draw from their own imagery bank, extending the Warren / Den / Burrow pattern.
- **Reroll freely.** A reroll is unlimited and free. This is a matter of taste, not a resource decision.
- **No free text. Anywhere.** There is no typed-name option for the colony, buried or otherwise. Three-plus-reroll gives enough expression on its own, and keeping it text-free makes *"all names are permanent, none are typed"* a clean total rule instead of a rule with an asterisk.
- **The aspirational and tribute registers are scoped to colony-naming alone.** They are *not* added to the general Reach and node grammar, which stays homely and plain everywhere else. The colony gets the extra emotional register because founding it is the one act of authorship the player is given.
- **Locked permanently once chosen.** There is no renaming.

<!--@23.3¶4-->
The mechanic lands in the tutorial at the first civic construction (Section 35.2), alongside the physical **welcome sign** that carries the name.

<!--@23.3¶5-->
---

<!--@6#2-->
# PART V — LEAVING HOME

<!--@6#2¶1-->
**ARTWORK — The Night Crossing**

<!--@6#2¶2-->
*The three away-registers in the order the player meets them, then the systems that govern what happens out there.*

<!--@6#2¶3-->
---

<!--@24-->
## 24. Crossing

<!--@24¶1-->
**INFOGRAPHIC — The Crossing**

<!--@24.1-->
### 24.1 The crossing action

<!--@24.1¶1-->
The standard transverse sequence runs Home → Away. The party gathers at a Staging Post; the view reveals the lanes between safe Median cover and Margin vegetation ahead; the player reads traffic density, vehicle types, audio, headlight cues, wind shear, lane islands, and micro-cover before committing movement between temporary safe positions or across the full gap.

<!--@24.1¶2-->
Citizen speed, fear, wounds, load, and formation affect responsiveness without replacing player skill. Load bears on the return as well as on encounters. The action must be **tense, brief, comprehensible, and tolerant enough that ordinary play does not produce routine mass casualty.**

<!--@24.1¶3-->
Accessibility options include time scaling, stronger telegraphs, simplified input, audio visualization, and possibly an assisted strategic resolution (Section 33.5).

<!--@24.1¶4-->
The First Law — *"Wait for the gap. The gap is given, not owed."* — is the crossing's tutorial text, its folklore, and an accurate description of its mechanics, all at once (Section 6.1).

<!--@24.1¶5-->
**Crossing is not an encounter.** It uses no Approaches, no Turns, and no exposure. It is an action mode with its own design.

<!--@24.1¶6-->
> **OPEN — Crossing, in full.** A signature mechanic and its least-specified system: input model, failure states, how the party moves as a group, how longitudinal travel differs (Section 7.3). · `500 log/open_items.md`

<!--@24.2-->
### 24.2 Return logic

<!--@24.2¶1-->
After a successful outbound crossing and a resolved Field run, the player chooses when to head home, and the return resolves on this distribution:

<!--@24.2¶2-->
- **70% — clean automatic return:** a short automatic or cinematic crossing that respects the challenge already completed.
- **20% — automatic with a swing:** the party gets home automatically, but with a swing that can break positive *or* negative — a bonus find, or lost cargo, a minor wound, gained fear.
- **10% — forced manual re-crossing:** changing traffic, Road Work, predator pressure, weather, fatigue, or a narrative event forces the player back into the crossing action.

<!--@24.2¶3-->
---

<!--@25-->
## 25. Field Mode

<!--@25¶1-->
**INFOGRAPHIC — Field Mode**

<!--@25¶2-->
**ARTWORK — Field Mode Traversal**

<!--@25.1-->
### 25.1 What it is

<!--@25.1¶1-->
Field Mode is a **traversable, surveyed territory** that the expedition party physically moves through, visiting multiple discoverable nodes rather than receiving an instant loot menu.

<!--@25.1¶2-->
- **Reaching a node** triggers *that specific node's* contest check — not one roll for the whole visit — and opens the Encounter frame (Section 26).
- **Carry-capacity and weight tension** plays out here: the party fills up as it goes and must decide when a heavy find is worth a cooperative carry or a trip home.
- **Traffic-as-Weather is present throughout** (Section 9.3), scaling by proximity to the road edge.
- **Choice-Event Cards appear occasionally** as a light interstitial layer between structured nodes (Section 10) — most visibly **Litter**.
- **Road Work's telegraph signs** appear here as readable environmental changes.
- The player **exits by choosing to head home**, feeding into Return Logic (Section 24.2).

<!--@25.1¶3-->
Field Mode is what keeps *uncontested* expeditions interesting: the tension of traversal, discovery, and load management exists even when nothing attacks.

<!--@25.2-->
### 25.2 Presentation and overlays

<!--@25.2¶1-->
Field Mode is **top-down and illustrated, not schematic and abstract** — a hand-drawn naturalist's field survey rather than an information display (Section 3.2). Warm parchment ground, painterly terrain, visible hand, node markers as pins over the illustration, the highway always in frame.

<!--@25.2¶2-->
**Named ground.** Anchor Points supply a Reach's labeled areas (Section 8.2), carrying the folk names the world gave them (Section 23.2).

<!--@25.2¶3-->
**Route overlays.** Dashed route lines drawn over the illustration, in the manner of a survey map annotating movement: **toggleable overlays** for animal paths, water flow, and wind and scent drift. This is the mode's information layer — Pillar 2.3 applied to territory rather than to resources — and it is what lets a player *plan* a route rather than merely walk one. Keeping the data on a toggleable layer also keeps the base illustration uncluttered.

<!--@25.2¶4-->
> **OPEN — Field Mode overlays.** Which overlays exist, whether they are independent toggles or a single cycling layer, and whether any are gated by Guest or Role. · `500 log/open_items.md`

<!--@25.3-->
### 25.3 Node types

<!--@25.3¶1-->
Nodes are the units of a territory. Beyond ordinary forage and salvage:

<!--@25.3¶2-->
- **Sealed human-container nodes** — a latched cooler, a zip-tied bag, a capped bottle, a bin. They hold rare loot and cannot be opened by any core species. **A raccoon in the party unlocks them** (Section 21.1) — a pure *access* niche, parallel to the Mink's water extraction and the wood mouse's Margin pockets, and distinct from the Fox's windfall *processing*.
- **Margin pockets** — reachable only by wood mice, and only after the same crossing everyone takes (Section 4.3).
- **Water hazards** — culverts, drainage, standing water; the Mink's domain.
- **Anchor Point nodes** — the named terrain features themselves, which is where an Establish Outpost party is headed.

<!--@25.4-->
### 25.4 Field Mode generalizes

<!--@25.4¶1-->
The same Field Mode is **reused, not rebuilt bespoke**, across every destination. The expedition types differ in what persists and what the party is there to do, not in a separate traversal engine each.

<!--@25.4¶2-->
**This includes home.** The Home Median is a Median Reach with a biome, Anchor Points, and node-bearing ground (Section 7.2), and it carries **both** the Colony register and a Field layer. Everyday local foraging is a **low-stakes Field run on home ground**, with structures appearing as nodes alongside forage and terrain.

<!--@25.4¶3-->
**Contest is possible on the Home Reach's Field layer**, and its likelihood falls with each Colony Tier: early foraging at home carries real risk, and mature ground is genuinely safe.

<!--@25.4¶4-->
Two consequences follow:

<!--@25.4¶5-->
- **The tutorial improves materially.** Field Mode is taught *safely*, at home, at the moment the player first feeds the group — so the first real expedition reads as *the same activity, across the road*, which is exactly what it is (Section 35.2).
- **Field Mode does not stop meaning "away."** The player leaves home by **Crossing**, not by changing camera. The emotional charge lives in Section 24, where it belongs.

<!--@25.4¶6-->
**It also includes the Metropolis**, which is a Field territory with venues as nodes (Part VI).

<!--@25.4¶7-->
---

<!--@26-->
## 26. Encounters

<!--@26¶1-->
Every node arrival opens the Encounter frame, and it is **the same frame whether the result is a windfall, a negotiation, or an ambush.** A quiet, uncontested node still gets its moment.

<!--@26¶2-->
That rule is not generosity toward pacing — it is the mode's rhythm. **Plan on the map, live in the room.** It is what concentrates the art budget at the moments that matter and keeps a surveyed Field layer from making the dangerous half of the game look cheaper than the safe half (Section 3.3).

<!--@26.1-->
### 26.1 The shape of an encounter

<!--@26.1¶1-->
**INFOGRAPHIC — The Encounter Frame**

<!--@26.1¶2-->
**Rounds resolve. Turns sit between them.** A contested encounter carries **one fewer Turn than it has rounds.**

<!--@26.1¶3-->
| Rounds | Turns | Character |
|---|---|---|
| **2** | **1** | Round 1 landed close rather than clean. The common case for a contested node. |
| **3** | **2** | Still close after Round 2. Rare. |
| **4** | **3** | Still close after Round 3. Rarest. The epic case, and where both the best and the worst outcomes live. |

<!--@26.1¶4-->
**Uncontested** — the frame opens and the node is described; it may resolve at once.

<!--@26.1¶5-->
**What continues an encounter:** a round that resolves *cleanly* ends it; a round that lands *close* — near the middle of the distribution rather than decisively either way — continues it. Length is therefore never arbitrary. An encounter runs long exactly because neither side would give ground, and it **self-selects**: evenly matched contests go the distance, mismatches end on contact.

<!--@26.1¶6-->
**The close window narrows each round** — wide after Round 1, tighter after Round 2, tighter again after Round 3 — which is what makes four rounds rare without a trigger, and keeps length never rolled for.

<!--@26.1¶7-->
**Hard cap: four rounds.** No exception, no artifact, no encounter type.

<!--@26.1¶8-->
The full beat sequence:

<!--@26.1¶9-->
| Beat | What happens | Player acts? |
|---|---|---|
| **Situation** | The encounter is described diegetically. Available **Approaches** are shown. | — |
| **Approach** | The player chooses how the party meets this. | **Yes — entry choice** |
| **Round 1** | Group resolution. If clean, the encounter ends here. | — |
| **Turn** | Only if Round 1 landed close. The player acts once. | **Yes** |
| **Round 2** | Group resolution, modified by the Turn. If clean, ends here. | — |
| **Turn** | Only if Round 2 landed close. The player acts once more. | **Yes** |
| **Round 3** | Group resolution. If clean, ends here. | — |
| **Turn** | Only if Round 3 landed close, and rare. The player acts a third time. | **Yes** |
| **Round 4** | Resolves finally, always. | — |
| **Exposure** | Each citizen's individual outcome resolves. | — |
| **Record** | Rating and debrief written to the Records (Section 22.3). | — |

<!--@26.1¶10-->
**The Approach sits outside the Turn count.** It is the entry choice, made once when the frame opens.

<!--@26.2-->
### 26.2 Approaches

<!--@26.2¶1-->
**ARTWORK — A Contested Encounter**

<!--@26.2¶2-->
**An encounter is not automatically a fight.** Combat is only one response; others include display, evasion, bribery, negotiation, trickery, surrendering part of the haul, rescue, and withdrawal. These are **player choices, made before the first round.**

<!--@26.2¶3-->
Five Approaches:

<!--@26.2¶4-->
| Approach | The party… | Tests | Baseline exposure |
|---|---|---|---|
| **Contest** | Meets it directly — fights, or displays hard enough to drive it off. | Resilience and fight | **High**, party-wide |
| **Evade** | Slips past, around, or beneath. | Stealth and movement | **Low** — but a failed Evade spikes it |
| **Parley** | Talks, warns, bargains, deceives, or bribes. | Social aptitude | **Low** overall, **high for whoever speaks** |
| **Yield** | Gives up part of the haul to end it. | Nothing — no roll | **Minimal** |
| **Withdraw** | Leaves. Node unresolved. | Nothing — no roll | **Minimal** |

<!--@26.2¶5-->
- **Trickery folds into Parley.** Deception is a social act, and a separate Approach for it would only fragment the set.
- **Rescue is not an Approach.** It is a Turn action, because it is always a response to something that just happened.
- **Withdraw and Yield are always available.** The player can always leave, and can always buy their way out if carrying anything. **Neither is ever removed** — not by an adversary, not by a Guest, not by an encounter type.
- **The other three vary** by encounter and by party. Weasels holding a culvert do not Parley. A sealed container cannot be Contested. This variance is where Guests earn their keep (Section 21.1).

<!--@26.2¶6-->
**Information rule.** Which Approaches are *available* is visible before choosing. How hard each will be is **not** — consistent with the prohibition on disclosing contest status or odds (Section 28.2). The player sees that Parley is on the table; they do not see that these weasels are unusually hungry.

<!--@26.3-->
### 26.3 The group layer — mass, never a roster

<!--@26.3¶1-->
**The adversary is a Presence, not a count.** MEDIAN never needs to know how many weasels. The fiction says *"a pair of weasels hold the culvert"* and the number stays flavor, permanently and by design.

<!--@26.3¶2-->
An encounter carries a **Presence value per available Approach.** The same weasels are formidable against Contest, moderate against Evade, and simply unavailable to Parley. This is what makes Approach a real decision rather than a reskin.

<!--@26.4-->
### 26.4 Resolution

<!--@26.4¶1-->
Conflict of every kind — expedition contest, Base Defense, Road Work onset — resolves through **augmented passive resolution**: a stat comparison, modified, then finalized with a bounded RNG roll. Never in real time, never a twitch test. This is the same engine behind all three; it is not three systems.

<!--@26.4¶2-->
**Party Score** = the participating citizens' relevant aptitude for the chosen Approach, summed, plus the **equipment modifier** (Keepsake, Tool, Supply — Section 20), plus Guest contributions, then modified by **terrain**, **weather** (Wind Draft, the River's Spume — Section 9.3), **carry load**, and any **citizen maiming**. A laden party is slower and more exposed.

<!--@26.4¶3-->
> *The heavier the haul, the longer the road home.*

<!--@26.4¶4-->
Score is compared to Presence; the margin is shifted by **bounded RNG** — bounded meaning the roll can narrow or widen a result but cannot overturn a large gap. A hopeless Contest stays hopeless.

<!--@26.4¶5-->
**Party size scales cleanly and honestly.** More citizens means a higher Party Score *and* more individuals exposed. A real trade-off requiring no bookkeeping.

<!--@26.4¶6-->
**The Turn.** A Turn occurs only when a round has landed close. The player then acts **once**, from a small set of options:

<!--@26.4¶7-->
| Option | Effect | Exposure |
|---|---|---|
| **Play a Supply** | Applies a departing citizen's per-run consumable to the next round. | Unchanged |
| **Commit a Rescue** | Sends a citizen to one who is pinned, wounded, or **tharn**. | **Raises rescuer, lowers rescued** |
| **Change Approach** | Switches to an Approach that was available at entry. The new Presence applies fresh. | Does not reset |
| **Press** | No intervention. Better group odds next round. | **Raises party-wide** |
| **Withdraw** | Take the partial outcome and go. | **Cuts party-wide** |

<!--@26.4¶8-->
Four things the Turn fixes: the **Supply** slot finally appears on screen rather than silently modifying a number; the Launcher's question — *"who do I trust with this?"* — becomes true, because the Turn asks *who goes back for them*; **bonds form where canon says they form**, since "co-expedition survival, rescue, tharn lead-out" (Section 18.1) are all Turn outcomes; and a posture chosen at the frame's opening can still be reconsidered once the room has answered back.

<!--@26.5-->
### 26.5 Exposure — the individual layer

<!--@26.5¶1-->
**INFOGRAPHIC — Exposure and Outcomes**

<!--@26.5¶2-->
**Exposure is how far a citizen personally stuck their neck out in this encounter.** It is derived from what the player chose, never rolled. It exists only within the encounter, **never displays as a number**, and never accumulates.

<!--@26.5¶3-->
**What sets it.** Baseline comes from the Approach (Section 26.2). Then:

<!--@26.5¶4-->
- Carrying the heaviest share of the load → **raises**
- Speaking, in a Parley → **raises**
- Committing to a Rescue → **raises the rescuer**, lowers the rescued
- Being pinned, wounded, or tharn → **raises, and keeps rising each round until resolved**
- Using a Guest's signature ability → **raises that Guest** — they are the one who went in
- Each additional round still committed → **raises everyone still in it**
- Withdrawing or Yielding → **cuts everyone**

<!--@26.5¶5-->
**How it resolves.** After the final round, each citizen resolves once against their own exposure. The governing principle, stated exactly:

<!--@26.5¶6-->
> **Exposure widens the distribution. It does not shift it.**

<!--@26.5¶7-->
High exposure does not mean *more likely to be hurt.* It means **more likely that something happened to you at all** — and the tails open in both directions together.

<!--@26.5¶8-->
| Exposure | Outcome band |
|---|---|
| **Minimal** | Nothing. The citizen was there; that is all the Record will say. |
| **Moderate** | Shaken, a fear memory, a minor wound. Ordinary consequence. |
| **High** | Both tails open: **Maiming** becomes possible, and so does a **Distinction**. |

<!--@26.5¶9-->
This gives the Distinction/Maiming symmetry the **shared driver it never had** (Section 19.3). A citizen who did nothing remarkable gets nothing remarkable, good or bad — not a failure of the system, but the system correctly declining to manufacture drama.

<!--@26.5¶10-->
**Group and individual resolution remain independent.** The two are computed separately and neither gates the other. A **Failed** encounter where everyone kept exposure low: the party comes home empty-handed and whole. A **Successful** encounter with one citizen at high exposure: the costly victory, graded **Hard-Earned**.

<!--@26.5¶11-->
Individual resolution only fires where genuine danger is present — a contested node, Base Defense, Road Work's onset — never as a background tax on clean, uncontested activity.

<!--@26.5¶12-->
> **OPEN — Exposure and Presence tuning.** Exposure bands and thresholds, and Presence values per Approach. · `500 log/open_items.md`

<!--@26.6-->
### 26.6 The outcome distribution

<!--@26.6¶1-->
Resolution forms a bell-shaped distribution: most results are ordinary success, compromise, retreat, partial yield, minor fear, or modest wounds; a rare bad tail brings maiming, major loss, capture, separation, or death; a rare good tail brings an exceptional artifact, powerful information, a diplomatic breakthrough, a resource cache, a Guest opportunity, or a **Distinction**.

<!--@26.6¶2-->
The engine can use hidden probability, but **the fiction always explains the result.**

<!--@26.7-->
### 26.7 The epic case

<!--@26.7¶1-->
Encounter length is generated by closeness (Section 26.1), so the "epic" encounter needs no separate mechanism — it is an encounter that refused to resolve three times running.

<!--@26.7¶2-->
**Length is never rolled for.** Closeness is the honest trigger.

<!--@26.7¶3-->
**Retained as an override:** a **Special Artifact** or **Tool** may grant an extra Turn outright, inserting a decision where a round would otherwise have resolved cleanly. It cannot breach the four-round cap.

<!--@26.7¶4-->
**The exposure interaction is the point.** Every additional round raises exposure for everyone still committed. Therefore **Legendary ratings and Maimings correlate** — the great stories and the terrible ones come out of the same encounters.

<!--@26.8-->
### 26.8 Guardrails

<!--@26.8¶1-->
This system sits one bad decision away from being a combat game. The following are canon prohibitions:

<!--@26.8¶2-->
- **Four rounds is the ceiling.**
- **No positioning, facing, turn order, initiative, or targeting.** The party is one body on the front end; individuality lives on the back end only.
- **Adversaries are never counted.** Presence, never a roster.
- **Never real-time, never a twitch test.**
- **Most contested encounters have one Turn.**
- **Exposure is never displayed as a number and never persists.**
- **Withdraw is never removed.**

<!--@26.9-->
### 26.9 What this system does not govern

<!--@26.9¶1-->
- **Crossing** (Section 24) is an action mode. No Approaches, no Turns, no exposure.
- **Road Work onset** (Section 11.2) uses the group layer only — a single round, no Approach, no Turn.
- **Base Defense** (Section 27.4) uses the full frame with the *colony* as the party.
- **Choice-Event Cards** (Section 10) are a separate system. A card may *lead into* an encounter; it is not one.

<!--@26.9¶2-->
---

<!--@27-->
## 27. Contest, recruitment, and Base Defense

<!--@27¶1-->
**INFOGRAPHIC — Contest, Recruitment and Base Defense**

<!--@27.1-->
### 27.1 What is contested

<!--@27.1¶1-->
Contest is revealed only on reaching a node (Section 25.1). Whether a node is contested at all varies with **Biome**, **Outpost status**, **season, recent Road Work**, and **RNG**.

<!--@27.2-->
### 27.2 The recruitment funnel

<!--@27.2¶1-->
1. **Is the node contested?** Determined by the factors above. Most nodes on genuinely wild territory can be; Held Reaches are calmer.
2. **If contested → 70% antagonist / 30% non-antagonist.** Antagonists are predators, territorial rivals, desperate scavengers, or environmental obstruction. *(This figure is scoped to contested nodes, not to all nodes.)*
3. **If non-antagonist → 30% chance the animal is amenable.** Non-antagonist contacts otherwise mean trade, warning, negotiation, aid, or mutual avoidance.
4. **If amenable → still gated** by the animal's own check plus a resource cost, fluffed as a "residence cost."
5. **Slot cap.** Recruitment is additionally capped by available Guest slots regardless of how often amenable animals appear — a full roster means *passing on* an amenable animal, not auto-recruiting it.

<!--@27.2¶2-->
**Two different things come out of this funnel.** An amenable animal of an outside species becomes a **Guest** and occupies a Guest slot. An amenable animal of the colony's *own* species becomes an ordinary **Citizen** and occupies no slot at all (Section 18.4).

<!--@27.2¶3-->
**The worked example: the raccoon.** The raccoon is the canonical illustration of the rival who joins, and it carries the same name from the first encounter through to the Story Circle. It appears first as antagonist scavenger fauna at contested nodes — bigger and cannier than the Rat, and a real threat. On a later encounter it may fall on the non-antagonist branch, then the amenable branch, and the party may pay the residence cost and bring it home. **The same animal that drove a party off a node last season can be sitting at the Story Circle this one.** Nothing about the funnel changes to accommodate this; the raccoon simply walks through it.

<!--@27.2¶4-->
> **CREATED VISUAL — "The night WHOOT came in."** At Guest recruitment. *With its fallback.*

<!--@27.3-->
### 27.3 Slot scaling and scarcity

<!--@27.3¶1-->
Guest slots scale with Colony Tier: **one new slot of each type per Tier reached**, for **four of each at max Tier.** This sits deliberately *below* full roster size — seven Active, nine Ambient — preserving meaningful-choice scarcity. The player never fields the entire roster and must choose.

<!--@27.3¶2-->
The first slot of each type is available from founding; it simply has nothing to fill it until the first non-adversarial encounter.

<!--@27.3¶3-->
> **OPEN — Guest slot scaling.** Tier graduation is rare, so slots open only four times in a campaign; whether Guest capacity should also scale along some lesser dimension — habitat quality, an amicable departure freeing a slot, a temporary visiting Guest. · `500 log/open_items.md`

<!--@27.4-->
### 27.4 Base Defense

<!--@27.4¶1-->
**ARTWORK — Base Defense**

<!--@27.4¶2-->
Base Defense is a distinct context: occasional animal incursions against the home territory, telegraphed by the Watchkeeper Role and the lookout network. It is **occasional, not relentless** — the home is a sanctuary that is sometimes threatened, not a tower-defense arena.

<!--@27.4¶3-->
It resolves through the full encounter frame (Section 26) with the **colony** as the party: a telegraphed approach, citizens auto-pathing to a refuge unless the player commits a defender, then resolution.

<!--@27.4¶4-->
Incursion types include predators, desperate scavengers, the Rat, and the **raccoon** — the last being both the most capable ordinary incursion and, uniquely, an animal the player may one day recruit.

<!--@27.4¶5-->
> **OPEN — Base Defense consequences.** What a successful incursion actually costs — stores, structures, wounded citizens, a lost Guest, spoiled Perishables. · `500 log/open_items.md`

<!--@27.4¶6-->
---

<!--@28-->
## 28. Expeditions and the Launcher

<!--@28¶1-->
**INFOGRAPHIC — Expeditions and the Launcher**

<!--@28.1-->
### 28.1 Expedition categories

<!--@28.1¶1-->
**Margin Raid.** A short transverse mission from the Home Median to either adjacent Margin, for renewable forage, scrap, discoveries, encounters, and high-frequency advancement needs. A Margin beside a wild Reach that is not yet Held can also be raided; it simply lacks Home efficiencies. A Held Reach with a Staging Post can run Margin Raids of its own (Section 29.2).

<!--@28.1¶2-->
**Median Scout.** A longitudinal reconnaissance journey opening an unknown Reach's Field territory **for reconnaissance only** — nothing buildable, nothing permanent. The party learns the Reach's lane count, biome, resources, Anchor Points, and **folk name**, and nothing persists afterward.

<!--@28.1¶3-->
**Establish Outpost.** A later expedition: a construction party carrying material returns to a scouted Reach, navigates to its preferred Anchor Point, and resolves that node's contest there. Winning — or an uncontested approach — *secures* the spot; it does **not** complete construction. Securing starts a construction clock, and when it finishes the Reach is claimed.

<!--@28.1¶4-->
That clock is explicitly **one instance of the Construction Queue** (Section 15) — a fixed number of whole days, resources sunk at the start, uninterruptible once begun. Its specific duration remains deferred.

<!--@28.1¶5-->
**Outpost Visit / Deep Extraction.** Returns to an established outpost's Field territory for active play: secure a large haul, repair facilities, respond to an event, meet a Guest, exploit a temporary opportunity, or push the frontier.

<!--@28.1¶6-->
**Special Journey.** Gated to Tier II or above. Its **primary** purpose is reaching the Rest-Stop Metropolis (Part VI). A **strong secondary** use is revisiting the destroyed ancestral home. Further story-forward destinations belong to this category as future content.

<!--@28.2-->
### 28.2 The Expedition Launcher

<!--@28.2¶1-->
The Launcher is character-centered — the question should feel like *"who do I trust with this?"* rather than *"which array has the largest number?"*

<!--@28.2¶2-->
It communicates the destination biome type and a partial resource preview, the destination's **folk name** where known, the mission purpose and known route demands, the eligible citizens as portrait cards with qualitative readiness and relevant history, condition and relationship dynamics, known traffic and weather observations, cargo capacity, and past expedition notes and rumors drawn from previous debriefs (Section 22.3).

<!--@28.2¶3-->
**The Launcher surfaces exactly one equipment decision per citizen: their Supply** (Section 20). Keepsakes travel automatically; Tools are standing colony-level assignments. Neither appears here. **Avoid a wall of stats.**

<!--@28.2¶4-->
It **never** discloses whether a destination will be contested, the exact encounter odds, exact victory percentages, or any hidden math. The player learns through experience, scouting, history, Guests, and environmental signs.

<!--@28.2¶5-->
> **OPEN — Resource preview specificity.** How specific the Launcher's partial resource preview should be. · `500 log/open_items.md`

<!--@28.2¶6-->
**Party size.** Three to five body-units is the tuned band, and the Standard Party is what the Launcher offers by default:

<!--@28.2¶7-->
| Species | Standard Party | Tuned range | Carry / Food |
|---|---|---|---|
| **Rabbit** | 3 animals | 3–5 body-units | 30 / 50 |
| **Squirrel** | 3 animals | 3–5 body-units | 60 / 100 |
| **Wood Mouse** | 6 animals (3 body-units) | 6–10 animals (3–5 body-units) | 36 / 60 |

<!--@28.2¶8-->
**Two body-units is a legal party for every species** — two rabbits, two squirrels, or four mice — and it is simply worse: less carry, a lower Party Score, and fewer bodies across which to spread exposure. Write no further penalty; the numbers already are one. The real cost is narrower: tharn's rescue needs a third body still holding the line, so a two-unit party has given up the rescue before it leaves, and a tharn there ends the run outright (Section 19.2).

<!--@28.3-->
### 28.3 Early expedition onboarding

<!--@28.3¶1-->
- **First major expedition:** a forced, strongly-framed physical confrontation — a "red in tooth and claw" moment teaching that the world is physical and contested and can wound citizens. It is *not* tuned to force permanent maiming every campaign.
- **Second or third expedition:** heavily weighted toward a **Guest recruitment opportunity** — the campaign's "Kehaar moment," where the player meets an outsider as an individual and learns the world contains relationships as well as threats.

<!--@28.3¶2-->
---

<!--@29-->
## 29. Outposts

<!--@29¶1-->
**INFOGRAPHIC — Outposts**

<!--@29¶2-->
**ARTWORK — Establishing an Outpost**

<!--@29¶3-->
Outposts expand the Home Median's reach without becoming replacement towns. The Home remains the population center, civic heart, and sentimental gravity of the campaign; outpost automation protects the game from multi-base micromanagement.

<!--@29.1-->
### 29.1 Reach lifecycle and fog of war

<!--@29.1¶1-->
A Median Reach moves through the three states named in Section 7.5 — **Unknown**, **Walked**, **Held.**

<!--@29.1¶2-->
**A Reach carries fog of war.** On a Median Scout, the territory reveals itself as the party moves through it — **Anchor Points are not shown immediately**, and the shape of a Reach is learned by walking it. This is what makes scouting an activity rather than a button, and it is the clearest expression of the Field register's "reading territory" purpose.

<!--@29.1¶3-->
**Completing an outpost's central building clears that Reach's fog permanently.** The player knows the whole Reach thereafter.

<!--@29.2-->
### 29.2 The outpost building set

<!--@29.2¶1-->
An outpost is intentionally a light footprint, drawn from a small dedicated set — **never** any of the core Home building catalogue:

<!--@29.2¶2-->
- A **central building** that claims the Reach and hosts the outpost's single **Ambient Guest** slot.
- A **Staging Post**, which lets a Held Reach run Margin Raids of its own (Section 28.1).
- Optional **resource-trickle** outbuildings — a modest passive yield from the local biome.
- Optional **visibility / predator-reduction** outbuildings.
- **One or two Citizen slots.**

<!--@29.2¶3-->
An outpost with **two or more citizen slots** can host a **full Hearth relocating together** (Section 18.2) — the intended way a bonded family reaches the frontier.

<!--@29.2¶4-->
**Passive effects have a radius smaller than the Reach.** Fog clears everywhere; benefit does not. **Where the outbuildings sit matters**, which keeps outpost construction a spatial decision rather than a checkbox.

<!--@29.2¶5-->
> **OPEN — Higher-Tier outpost significance.** Whether outposts gain optional significance of their own at Tier III or IV — a unique building, expanded slots, or a distinct role in the corridor network. · `500 log/open_items.md`

<!--@29.3-->
### 29.3 Stationing a citizen

<!--@29.3¶1-->
A citizen assigned to an outpost is **genuinely stationed there** — unavailable for Home Median work, Margin Raids, or Base Defense until reassigned — in exchange for boosting that outpost's passive trickle and being automatically present for Outpost Visits there. Stationing is not permanent; the citizen is reassignable at need.

<!--@29.3¶2-->
Stationed citizens **still count toward the same low-population ceiling** (Section 12). There is no exception that lets total population creep upward. In practice, sending citizens to satellites becomes a natural pressure valve as population climbs at home.

<!--@29.3¶3-->
**Hearths cannot be split.** A citizen belonging to a Hearth is **ineligible for solo stationing.** The family either goes together to a two-slot outpost or stays home.

<!--@29.4-->
### 29.4 Contest and the value of investment

<!--@29.4¶1-->
**Claiming a Reach is not the same as pacifying it.** An outpost's central building claims the **entire Reach** — rewarding exploration for a good, wide strip worth committing to rather than settling the first tile the party reaches — and it clears the fog. But claiming alone does **not** reset the Reach's contest risk.

<!--@29.4¶2-->
**Contest falls as the player invests.** It is the **outbuildings** — the visibility and predator-reduction structures in particular — that make a Reach genuinely calmer. A bare outpost is a flag in the soil and little more; a developed one is a place where the corridor has learned not to bother you.

<!--@29.4¶3-->
This keeps an outpost a project rather than a purchase, and it means Outpost Visits run safer than wild territory only to the degree the player has earned it.

<!--@29.4¶4-->
> **CREATED VISUAL — "The first outpost, finished."** *With its fallback.*

<!--@29.5-->
### 29.5 Active versus passive value

<!--@29.5¶1-->
Passive yield is reliable but modest. Visiting an outpost opens its Field territory and can produce greater rewards, special encounters, repairs, rare resources, and story events. The player chooses when the additional attention is worthwhile.

<!--@29.5¶2-->
---

<!--@7#2-->
# PART VI — THE REST-STOP METROPOLIS

<!--@7#2¶1-->
**ARTWORK — The Metropolis at Night**

<!--@7#2¶2-->
*The corridor's one city. It gets its own part because it is unlike anything else in the world: the only large settlement, the only genuinely multi-species population, the only place with a history older than the player's, and the only place whose folklore contradicts the colony's own.*

<!--@7#2¶3-->
---

<!--@30-->
## 30. The Metropolis

<!--@30¶1-->
**INFOGRAPHIC — The Rest-Stop Metropolis**

<!--@30.1-->
### 30.1 The place

<!--@30.1¶1-->
The **Rest-Stop Metropolis** is a distant, revisit-able multi-species settlement hidden within the neglected ecological and structural margins of a human rest stop.

<!--@30.1¶2-->
It should feel extraordinary but plausible: **not a fantasy capital sitting openly beside human foot traffic**, but an urban animal ecosystem distributed among drainage spaces, service voids, dumpster enclosures, embankments, roof edges, vents, and vegetation set back from the main buildings.

<!--@30.1¶3-->
Its population is genuinely multi-species and its scale is high — appropriate here in a way it never is at the low-population Home Median.

<!--@30.2-->
### 30.2 Presentation — a Field territory with venues as nodes

<!--@30.2¶1-->
**ARTWORK — A Venue as a Node**

<!--@30.2¶2-->
The Metropolis is surveyed like any other territory (Section 25.4): a top-down plate of drainage runs, service voids, embankments, and roof edges, with **venues as nodes.** Entering the tavern is an Encounter.

<!--@30.2¶3-->
Same engine, same rhythm, **no new register.** What differs is what the nodes contain: a fixer's workshop, a specialist crafter, a rumor-monger's corner, a trade floor, the tavern.

<!--@30.2¶4-->
**Its encounters lean overwhelmingly on Parley** (Section 26.2), which makes the Metropolis the best showcase in the game for the fact that an encounter is not automatically a fight. A player who has spent forty hours choosing Contest and Evade arrives somewhere that rewards neither.

<!--@30.3-->
### 30.3 Core functions

<!--@30.3¶1-->
- **Multi-species gathering place:** rumors, relationships, recruitable Guests, returning characters, social story.
- **Trade:** exchange local abundance and rare artifacts for unfamiliar resources or services.
- **Craft and adaptation:** commission specialized tools and accessibility aids beyond the Home workshop's knowledge.
- **Culture and mythology:** corridor legends, ecological memory, warnings, and **competing interpretations of the human world.** Concretely, the Metropolis holds **contradictory Laws of the Median** (Section 6.1) and its own **regional variants** for the highway's name (Section 6.3). The player's colony discovers that its own certainties are local — and, because the colony's Laws are genuinely imperfect (three teenagers' half-memory), some of those contradictions are corrections.
- **Intelligence:** learn about Road Work, routes, biomes, rare opportunities, political tensions.
- **Place names:** the richest source of names for ground the player has not yet walked (Section 23.2).

<!--@30.4-->
### 30.4 A founding myth, and what it does not mean

<!--@30.4¶1-->
**Raccoons are the Metropolis's historic founding species.** The current population is genuinely multi-species — other species arrived and settled later, and today they are the majority — but raccoons retain outsized **cultural and traditional standing** as a consequence of having been first.

<!--@30.4¶2-->
**This is heritage weight, not authority.** All Metropolis species are explicitly equal. There is no raccoon hierarchy, no raccoon rule, no political control, and no faction system attached. Founding priority buys respect and a set of customs, and nothing else.

<!--@30.4¶3-->
Its most concrete expression is a single figure: the multi-species tavern and trade hub at the heart of the Metropolis has a **bartender**, and the bartender is a **Raccoon.** Subtle raccoon-heritage nods in Metropolis architecture and decor are available as a Phase 2 art detail.

<!--@30.4¶4-->
**The myth rhymes with the game's own creative thesis** (Section 1): the Metropolis's founding story is a grander, older echo of the player's own Founding Escape — animals making a permanent home in leftover human space — rather than a copy of it. That resonance is the reason to have it at all.

<!--@30.4¶5-->
**Raccoons remain barred from being core colony citizens or domestic crafters, and Tier III remains structurally independent of the Metropolis** (Section 32).

<!--@30.4¶6-->
**The species mix.** Raccoons, plus a broad spread of the three core species and of animals that appear elsewhere as Guests. Core species being present here creates no conflict with the no-cross-recruitment rule (Section 4): that rule governs who joins the player's *colony*, not who exists in the world. The Metropolis is where a rabbit sees squirrels going about their business and cannot recruit a single one of them.

<!--@30.4¶7-->
**The central plaza's name is generated, not authored.** It is produced per campaign through the same folk-name grammar as every other place (Section 23.2), which means no two campaigns name it alike and the player learns it from rumor rather than from a map. Any name appearing in supporting material is therefore an example rather than the name.

<!--@30.4¶8-->
---

<!--@31-->
## 31. The Metropolis in the campaign

<!--@31.1-->
### 31.1 Campaign role

<!--@31.1¶1-->
The Metropolis belongs in the core campaign because the victory arc involves connecting the Home Median to the wider world. **It must not overshadow the base-builder or become the player's new primary town.**

<!--@31.1¶2-->
It is the **primary destination of the Special Journey** expedition type (Section 28.1), and it is reached only after a chain of outposts and relationships makes the journey survivable.

<!--@31.2-->
### 31.2 Victory and continuation

<!--@31.2¶1-->
A campaign's climactic objective is to establish a viable network of outposts and relationships reaching the Metropolis, then complete a **Grand Caravan** or equivalent final expedition proving the corridor connection can endure.

<!--@31.2¶2-->
**Victory is an offered conclusion, not forced retirement.** After the climax the player may conclude and read the colony's completed **Chronicle** (Section 22.1), or continue indefinitely in the same world.

<!--@31.2¶3-->
Post-victory play focuses on civic beautification, relationships, rare expeditions, long-term ecological events, veteran care, outpost refinement, trade, and the stories of later generations — **not infinite vertical power scaling.**

<!--@31.2¶4-->
---

<!--@8#2-->
# PART VII — PROGRESSION AND PRESENTATION

<!--@8#2¶1-->
**ARTWORK — The Founding Escape**

<!--@8#2¶2-->
---

<!--@32-->
## 32. Progression tiers

<!--@32¶1-->
**INFOGRAPHIC — Progression Tiers**

<!--@32¶2-->
The tier system expresses increasing security, spatial reach, institutional capability, and ecological integration. **It is not a ladder toward human-style industrialization.**

<!--@32¶3-->
**Every Tier graduation grants all citizens a stat bump** — a colony-wide progression event (Section 19.4). Each Tier also opens one new Active Guest slot and one new Ambient Guest slot (Section 27.3), raises the cap on **building upgrade rungs** (Section 16.2), unlocks **building availability** for families that did not previously exist, and adds a **Construction Queue slot** (Section 15).

<!--@32.1-->
### Tier I — Scavenger Camp

<!--@32.1¶1-->
**Fantasy:** a vulnerable settlement proving it can survive.
**Range:** Home Median and adjacent Margins.
**Capabilities:** basic shelters, food storage, simple repair, Staging Post, first expeditions, the first Guest slot of each type, a single Construction Queue slot.
**Pressures:** exposure, fragile construction, scarce scrap, unknown corridor, fear.

<!--@32.2-->
### Tier II — Fortified Settlement

<!--@32.2¶1-->
**Fantasy:** the colony is organized, defended, and able to prepare rather than merely react.
**Range:** first longitudinal scouts and one nearby outpost.
**Capabilities:** refined storage, stronger routes, recovery space, better tools, limited food preservation, second Guest slot of each type, additional Construction Queue capacity.
**Pressures:** maintaining the first network, seasonal preparation, contested sites.

<!--@32.2¶2-->
*(**Warren, Den, and Burrow are species terminology** — rabbit, squirrel, and mouse respectively — and are never used generically. A tier name shared by all three campaigns cannot borrow one of them.)*

<!--@32.3-->
### Tier III — Independent Colony

<!--@32.3¶1-->
**Fantasy:** a mature, self-governing home that can endure without external rescue.
**Range:** multiple outposts and deeper biomes.
**Capabilities:** durable anchored construction, outpost logistics, Ambient Guest assignment to outposts, adaptive equipment, advanced Role use, larger expedition choices, third Guest slot of each type, higher building rungs.
**Pressures:** regional relationships, Road Work at multiple nodes, preparing a corridor connection.

<!--@32.3¶2-->
Tier III is structurally independent of the Rest-Stop Metropolis (Section 30.4).

<!--@32.3¶3-->
> **CREATED VISUAL — "The colony at Tier III."** *With its fallback.*

<!--@32.4-->
### Tier IV — Sovereign Network

<!--@32.4¶1-->
**Fantasy:** the Home Median becomes the protected heart of a connected corridor community.
**Range:** a chain reaching the Rest-Stop Metropolis and other distant sites.
**Capabilities:** resilient dead-zone sanctuary spaces, mature outpost routes, trade and intelligence networks, the fourth and final Guest slot of each type, the top rungs of every building ladder, major civic works, grand caravan preparation.
**Pressures:** completing the route, protecting legacy, deciding what the colony will become.

<!--@32.4¶2-->
**Tier IV does not electrify the animal settlement or turn it into a tiny human empire.** Mastery means ecological invisibility, resilient routes, social connection, and intelligent use of overlooked infrastructure — and, in the building ladders, scrap-mastery and civic complexity rather than machinery.

<!--@32.1#2-->
### 32.1 Advancement gates

<!--@32.1#2¶1-->
Tier advancement should combine a civic construction milestone at the Home Median, sustained food and shelter capacity, a small amount of Flexible and Rigid Scrap, a demonstrated expedition or network achievement, and — at selected tiers — a believable Special Artifact, relationship, or knowledge requirement. Advancement costs run at the stat frame's resolution and are a visible drop in the stores; exact values are deferred.

<!--@32.1#2¶2-->
Avoid arbitrary giant resource sacrifices. Advancement must visibly transform the colony and unlock a new kind of decision.

<!--@32.1#2¶3-->
**Advancement is never gated by Guest recruitment**, which stays fully optional so that a "no Guests ever" run is always valid and never soft-locked.

<!--@32.1#2¶4-->
---

<!--@33-->
## 33. Interface and information design

<!--@33¶1-->
**INFOGRAPHIC — Interface and Information Design**

<!--@33.1-->
### 33.1 The Colony view

<!--@33.1¶1-->
The default view prioritizes the settlement as a living miniature ecosystem. Work routes, storage, structural problems, fear, injury, weather, and congestion should be visually apparent.

<!--@33.1¶2-->
**Functional icons are part of the base view.** Every building carries a persistent, always-visible functional symbol regardless of its in-world flavor name (Section 16.3). These are *not* gated behind the ledger overlay: a player who has never opened the overlay can still read the colony at a glance.

<!--@33.1¶3-->
**The Construction Queue is visible here**, showing what is being built, what is offline while it is built, and roughly how far along it is — in days, qualitatively presented, with no speed-up affordance because none exists.

<!--@33.1¶4-->
**Three distinct hotspots**, each at a different scope:

<!--@33.1¶5-->
| Hotspot | Exposure | Scope | Opens |
|---|---|---|---|
| **Community Board** | Ambient — always visible in the world | Operational, day-to-day | Alerts, duties, foraging shares, scout returns, active Choice-Event Cards; the diegetic face of the Almanac feed |
| **Story Circle** | Entered deliberately | Ceremonial, colony-scale | The **Colony Record** — Almanac and Chronicle |
| **Warren / Den / Burrow hub** | Entered deliberately | Personal, citizen-scale | The **Village Roster**, and through it each **Citizen Record** |

<!--@33.1¶6-->
Operational, ceremonial, and personal — three scopes, expressed spatially as well as tonally.

<!--@33.2-->
### 33.2 Blueprint / ledger overlay

<!--@33.2¶1-->
A toggle or hold input adds precise information for known systems: resource totals, consumption, capacity, and expected reserve duration; building function, durability state, repair need, construction cost, and current queue position; Role assignment and route congestion; healing, nursery, and scheduled-event progress; outpost status and known network flow.

<!--@33.2¶2-->
It should **not** reveal hidden citizen ratings, unknown encounters, exact contest probabilities, or future RNG.

<!--@33.2¶3-->
The overlay's building-function data is the **text expansion** of the base view's always-visible functional icons, not a substitute for them.

<!--@33.3-->
### 33.3 Citizen Records and the Village Roster

<!--@33.3¶1-->
The **Village Roster** is the index screen for the colony's people: every citizen, listed, leading into an individual's **Likeness** and **Tale** (Section 22.2). It is visually skinned as being *at the species hub* — the **Warren**, **Den**, or **Burrow**, using the campaign's actual species-specific hub name.

<!--@33.3¶2-->
An individual Record combines portrait, both name fields, descriptive aptitude bands, current condition, bonds and Hearth membership, assigned Role, equipment slots, earned Distinctions and Maimings, and a concise chronological history. The player can understand why a citizen is suitable without seeing raw hidden attributes.

<!--@33.4-->
### 33.4 The Expedition Launcher

<!--@33.4¶1-->
Specified in Section 28.2. In interface terms: character-centered, portrait cards, qualitative readiness, exactly one equipment decision per citizen.

<!--@33.5-->
### 33.5 Controls and accessibility

<!--@33.5¶1-->
The control target is PC and console with controller-first readability at both television and handheld distance.

<!--@33.5¶2-->
Required considerations include scalable text and UI, full remapping, pause and time scaling, color-independent signals, directional audio visualization, a reduced-input-speed crossing option, a strategic or assisted crossing alternative if feasible, motion/flash/camera-shake controls, and clear animal silhouettes and condition icons.

<!--@33.5¶3-->
---

<!--@34-->
## 34. Art and sound

<!--@34.1-->
### 34.1 Visual identity

<!--@34.1¶1-->
Grounded stylized realism at animal scale. The world combines soft organic material — fur, grass, roots, mud, bark, feathers — with harsh human infrastructure — wet asphalt, concrete, salt, rust, tire rubber, reflective signs, plastic, drainage metal. The art culture takes *Mouse Guard* as a modern-register touchstone, without its medieval trappings.

<!--@34.1¶2-->
The tone is **atmospheric and tactile, not relentlessly grim.** Home scenes may be warm, lively, and gently storybook; expedition scenes become colder, larger, and more cinematic.

<!--@34.1¶3-->
Avoid sci-fi interfaces, neon technology, and brushed-metal title treatments that make the animal world feel manufactured. There is no military or mature-rated visual framing.

<!--@34.1¶4-->
**Night is lit.** A highway after dark is one of the most illuminated environments there is: sodium vapour, headlight wash, brake-light red, reflective signage, and all of it doubled in wet asphalt (Section 9.2).

<!--@34.1.5-->
### On anthropomorphism — the line

<!--@34.1.5¶1-->
The citizens are heavily anthropomorphized as *characters*: they have names, families, grief, folklore, and standing jobs. What reaches their bodies is improvised from what the corridor sheds. *Mouse Guard* is the reference and the reference already contains the answer — MEDIAN takes its **small-animal material culture** and refuses its **medieval trappings** (Section 1.1).

<!--@34.1.5¶2-->
A **Keepsake** is a citizen's permanent identifier — a bead, a scrap of ribbon, a bottlecap on a cord. **Adaptive equipment** (Section 20) is as much a part of a citizen as their Keepsake, and a maimed citizen is visibly maimed.

<!--@34.1.5¶3-->
**Cloth is found, never dyed.** Colony material culture is scavenged (Section 15), and scavenged fabric carries the colors of the roadside: high-visibility orange, safety-vest yellow, sign green and white, tarp blue, burlap, plastic, retread black. Every citizen in a colony is the same animal, so cloth is what tells them apart — and it states the setting in the same stroke.

<!--@34.1.5¶4-->
**A citizen's kit reflects their work.** A Crafter carries a pouch of oddments, a Healer bundled moss, a Builder lashings; a Watchkeeper carries nothing at all, because their work is to watch.

<!--@34.1.5¶5-->
**Never depicted:** weapons of any kind · armor, including bracers and any cross-body strap, which reads as a weapon harness whether or not it carries one · anything forged, smithed or cast · helmets, uniforms, badges, cords, livery · animals dressed as miniature people. The equipment slot is named **Tool** and never "Weapon" for exactly this reason (Section 20).

<!--@34.1.5¶6-->
**The permitted side is house style and artwork.** Leaf helmets, cloth-scrap cloaks, twine belts, bark and shell, pouches, staffs — a staff carried, leaned on, balanced or slung, never one-ended and point-outward.

<!--@34.1.5¶7-->
**Expression sits in ears and posture first.** Rodent facial musculature is limited and pushing a face past it tips into cartoon. Ears are enormously expressive on all three species and cost nothing. This matters mechanically as well as tonally: fear must be visible in the world as a frightened posture (Pillar 2.3), and tharn must read through more than an icon (Section 34.3). The Crossing is four-legged without exception; elsewhere posture serves the picture.

<!--@34.1.5¶8-->
**Escalation without industry.** Dress quality tracks Colony Tier — torn bag strip at Tier I, selected and cleaned and well-stitched scrap by Tier IV — on exactly the principle governing the building ladders (Section 16.2): grandeur through scrap-mastery, never through machinery.

<!--@34.1.5¶9-->
**Wordmark and logomark (concept direction, adopted).** The MEDIAN title is rendered with a **cracked-asphalt and shattered-glass letterfill**, accompanied by a companion **"//" logomark** styled as **mossy concrete lane-marking relief** — a candidate app and loading icon, and a quiet piece of wordplay, since a median is precisely the thing that sits between two lane markings. Both are built from the material vocabulary already established: the title treatment is made of the world rather than imported from a hardware catalogue. **Concept direction only**; production must be delivered with **layered, editable text** rather than flattened.

<!--@34.2-->
### 34.2 Scale language and vehicle presence

<!--@34.2¶1-->
**INFOGRAPHIC — Scale Language**

<!--@34.2¶2-->
Scale should be communicated through recognizable infrastructure and material texture: lane paint, tire fragments, guardrail bolts, culvert mouths, drainage grates, barrier seams, distant vehicle mass. Cars should not intrude impossibly close to safe colony compositions.

<!--@34.2¶3-->
**Vehicle and machine flavor belongs throughout the world, not only on the road.** The corridor is littered with the remains of what passes along it, and biomes should carry that: a wrecked car under an interchange, an engine block half-swallowed by grass, a rusted piece of abandoned construction equipment, retread tire fragments, bumper shards, a hubcap. In the Margin, a wreck can be a **node** in its own right. This is how the world states its scale contrast without ever showing a human.

<!--@34.2¶4-->
**Human bodies never appear. There is no exception.** The Giants live in folklore, spoken about and never depicted (Section 6.3).

<!--@34.2¶5-->
Machinery without a visible operator reads as indifferent force rather than intent — something evaded or sheltered from and **never negotiated with** (Section 11.2). An operator invites appeal. The absence of one is the horror, and it is also the more accurate account of what the corridor actually is to the animals living in it: not malice, but weather with a schedule.

<!--@34.2¶6-->
This rule was only ever about human bodies. **Vehicles are unaffected** — Roaring Iron is visible constantly and by design, and machinery at work is visible in full.

<!--@34.2¶7-->
**Catastrophe is sensory-obscured.** Destruction and death are conveyed through dust, noise, vibration, distance, and narrowed perception rather than depicted. There is no explicit blood or gore. This is the same presentation vocabulary used for tharn (Section 34.3), which means the Founding Escape teaches the player how catastrophe *reads* in this game before tharn ever fires on a citizen.

<!--@34.3-->
### 34.3 The sound of the world

<!--@34.3¶1-->
**INFOGRAPHIC — Art and Audio Style Guide**

<!--@34.3¶2-->
A place is partly what it sounds like, and the corridor is a loud one.

<!--@34.3¶3-->
**Traffic is legible by ear.** Density and approach are learnable without looking, and something large announces itself as low-frequency vibration through the ground before it is visible at all. A party that has learned the sound knows to be somewhere else.

<!--@34.3¶4-->
**Tharn is narrowed sound, breath and pulse.** The world outside the frozen citizen recedes; what is left is very close and very loud.

<!--@34.3¶5-->
**Road Work changes the soundscape for the length of its persistence window** (Section 11.2). The return of ordinary noise is how the colony knows it is over.

<!--@34.3¶6-->
**The River's Spume is a continuous ambient bed**, its texture shifting with the season and the traffic cycle (Section 9.3): hot and battering in summer, thin and cold in winter, choking at Rush, gritty in the autumn dust.

<!--@34.3¶7-->
**Home sounds like home** — species-specific movement, construction, conversation, shelter against weather, and the domestic rhythms of a working colony. It is the one register where the road is held at arm's length (Section 3.5), and the sound design is what carries that.

<!--@34.3¶8-->
Adaptive devices and lasting injuries alter movement sound respectfully and consistently. Accessibility requirements for audio are specified in Section 33.5.

<!--@34.3¶9-->
---

<!--@35-->
## 35. Campaign onboarding

<!--@35.1-->
### 35.1 The Founding Escape

<!--@35.1¶1-->
The campaign's opening sequence is set out in full at the front of this document, before Part I. It is the player's first hour: the ancestral home, the trio, the machines, and the arrival at the green island between two highways.

<!--@35.2-->
### 35.2 Tutorial sequence

<!--@35.2¶1-->
The tutorial teaches emotional priorities before revealing the full system:

<!--@35.2¶2-->
1. **Find sanctuary:** begin with the founding group in a damaged but promising Home Median.
2. **Feed the group:** gather nearby sustenance and watch it move physically into storage — **taught as a low-stakes Field run on home ground** (Section 25.4), which is where Field Mode is introduced, safely.
3. **Build the first civic structure:** establish shelter or a communal center, introduce the Colony register — and **name the colony**, choosing one of three generated names at the new welcome sign (Section 23.3). This is the only name the player will ever author, and placing it as the first civic act makes founding feel like founding.
4. **Recognize a progression need:** a repair or construction problem requires material not available safely at home.
5. **Stage the first crossing:** read traffic, select citizens, make the Home-to-Margin run. The First Law surfaces here. **The Margin Field run reads as the same activity as step 2, across the road** — which is exactly what it is.
6. **Face the world:** resolve an early physical contest that can wound and frighten without scripting an unavoidable permanent mutilation (Section 28.3).
7. **Meet an outsider:** weight the second or third expedition toward a Guest encounter, establishing social possibility.
8. **See the corridor:** reveal the longitudinal median chain and the first Median Scout target, with its folk name.

<!--@35.2¶3-->
The founding setup always matches the selected core species; the game does not always begin with a lone mouse.

<!--@35.2¶4-->
---

<!--@9#2-->
# PART VIII — PRODUCTION NOTES

<!--@9#2¶1-->
> **This part is suggestions, not canon.** Everything in Sections 36 and 37 is a recommendation about *how to build and evaluate* MEDIAN, offered to be argued with. Where the rest of this document states what the game *is*, this part states what a team might reasonably *do* — and a team that finds a better order of operations should take it. Section 38 is the exception: the canonical summary is canon.

<!--@9#2¶2-->
---

<!--@36-->
## 36. Suggested scope and roadmap

<!--@36.1-->
### 36.1 A suggested vertical slice

<!--@36.1¶1-->
A persuasive prototype would probably want to prove that:

<!--@36.1¶2-->
- one species — rabbits or mice are likely easiest — can build a visually readable small colony in one Home Median;
- named citizens create attachment through work, fear, wounds, Distinctions, history, and relationships;
- the outbound crossing is tense, fair, and replayable;
- one Field territory supports renewable extraction, a Road Work reset, and legible traversal at the naturalist-plate register;
- one contested Encounter supports at least Contest, Parley, and Withdraw, with a Turn and an exposure resolution;
- expedition consequences visibly return to the colony **as written Record entries the player actually reads.**

<!--@36.1¶3-->
**The Records' non-generative layer probably belongs in the slice**, because "consequences return to the colony" is difficult to demonstrate without it.

<!--@36.1¶4-->
It would likely be wise *not* to prototype the Metropolis, the full season cycle, every Guest, all three species, or generative imagery before this loop works.

<!--@36.2-->
### 36.2 A suggested V1 target

<!--@36.2¶1-->
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

<!--@36.3-->
### 36.3 A suggested approach to world events

<!--@36.3¶1-->
Rare world-event set-pieces — a multi-vehicle pileup, a mass bird migration, a returning road-construction threat — are probably best implemented **not as new standalone systems** but as rare custom expedition modes that visually and resource-wise **reskin the existing Field and Encounter registers**, reusing infrastructure in keeping with Pillar 2.6. They would be bespoke drama on the scale of once or twice per campaign, not a recurring raid rhythm.

<!--@36.3¶2-->
Smaller world events can ride the **Choice-Event Card** system instead — the layer between "ordinary day" and "once-a-campaign set-piece."

<!--@36.4-->
### 36.4 Suggested later expansion candidates

<!--@36.4¶1-->
More biomes, Rest Stops, Guests, event chains, and infrastructure types; a playable Metropolis-focused campaign with different constraints; additional story-forward Special Journey destinations; expanded folklore pools and place-name banks.

<!--@36.4¶2-->
Rival organized civilizations only if localized encounter and diplomacy systems prove insufficient — adding fully-simulated distant AI colony economies by default seems unwise. Optional generated portrait, expedition, settlement, and Chronicle imagery after the base game is stable. A playable raccoon campaign remains a *possible* DLC only.

<!--@36.4¶3-->
---

<!--@37-->
## 37. Suggested prototype success criteria

<!--@37¶1-->
The concept is probably working when players:

<!--@37¶2-->
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

<!--@37¶3-->
Two criteria specific to MEDIAN's own systems: players should **read the Chronicle voluntarily** rather than treating it as a menu, and should **quote the Laws of the Median back at the game** — using folklore as shorthand for mechanics, which is the surest sign the tutorialization-as-culture approach landed.

<!--@37¶4-->
---

<!--@38-->
## 38. One-paragraph canonical summary

<!--@38¶1-->
MEDIAN is a single-player PC and console animal colony builder — a base-builder first, in the spirit of "Age of Empires, minus combat, with the heart of *Watership Down*" — set on the green islands between active highways. The player chooses rabbits, squirrels, or wood mice and, after a Founding Escape from a home destroyed by road construction, builds a permanent, low-population colony — the one thing they will ever name — whose named citizens forage, construct under standing Roles, form bonds and Hearths, take in wanderers, suffer fear and tharn, heal from wounds, adapt to permanent maiming, earn Distinctions and the After-names that come with them, and accumulate personal histories in the Records. All individual growth is earned in the field and never at home. The game presents itself in four registers — an inhabited Colony, a surveyed Field, a rendered Encounter, and an immediate Crossing — and that sequence enacts its emotional rhythm of sanctuary, exposure, and return before any mechanic does. Local ecology sustains life, but advancement requires expeditions: cross the traffic, its danger set by lane count, to the renewable and never-buildable Margin, or travel the corridor of Median Reaches — Unknown, Walked, or Held — to scout, establish Reach-claiming outposts, meet contested factions and rare Guest Citizens, and extend the colony's range. Capacity and party size resolve in body-units; individual animals carry every harm and every honor. Encounters resolve in two to four rounds through a chosen Approach — Contest, Evade, Parley, Yield, or Withdraw — against an adversary presence rather than a counted roster, while each citizen's individual fate is set by exposure, which widens the distribution in both directions so that the animal who stuck their neck out is the one who comes home changed. Traffic behaves like weather, expressed as Wind Draft, the River's Spume, and Litter, richest and most dangerous at the same edge; Road Work reshapes the ecosystem, tilts the event deck, and echoes the Founding Escape; a Construction Queue keeps the colony's plans certain while risk stays in the field. The animals carry their own folklore — the Laws of the Median, the Sayings, and their own words for the Giants and the Rivers of Thunder — which teaches the game's systems from inside the fiction and gives the colony's Chronicle its voice. Four progression tiers transform a vulnerable camp into a resilient sovereign network without turning animals into miniature industrial humans. The campaign culminates in a durable connection to the distant Rest-Stop Metropolis and a Grand Caravan, after which the player may conclude the colony's Chronicle or continue indefinitely. Optional generated portraits, illustrations, and milestone images can commemorate the actual citizens and settlement, but the game is designed to stand completely without them.

<!--@38¶2-->
---

<!--@10#2-->
# APPENDICES

<!--@10#2¶1-->
A manifest only. Each of the following is a separate authoring project; nothing beyond its title and scope line is written here.

<!--@10#2¶2-->
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

<!--@10#2¶3-->
---

<!--@10#2¶4-->
*End of MEDIAN Game Design Document v0.4.6.*
