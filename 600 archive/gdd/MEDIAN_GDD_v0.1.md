# MEDIAN — Game Design Document v0.1

> **Archival transcription.** The first MEDIAN design document, converted from
> `Median-v0.1-Claude.docx` to Markdown for the repository. **The text is unedited.**
> Headings, lists, tables and inline emphasis are preserved as they appeared; nothing
> has been corrected, updated, or reconciled against later canon.
>
> **This is not canon.** Current canon is `100 canon/MEDIAN_GDD_v0.4.4.md`. Much of what
> follows was later revised or dropped outright — among other things this draft carries a
> fourth shared stat, weighted survival odds in the Founding Escape, and zone terminology
> since retired. See Appendix B of the current edition for the full record.

---

**MEDIAN**
*(working title)*

A Survival / Colony-Building Game of Highway Median Ecology
Game Design Document — V1 Concept
Draft compiled July 2026

---

## Table of Contents

*(A generated Word field in the source document; it produced no transcribable text and is omitted. The section headings below serve in its place.)*

## 1. High Concept


Median is a survival, home-building, and resource-management game in which the player character and non-player characters are small animals, and the entire playable world is confined to the median strips and rights-of-way of large highways. The player founds and grows a colony of a single animal species inside a walled, road-bounded stretch of habitat, balancing visible, spatial base-building against the ever-present danger of the traffic and predators that define life on the median.

Design touchstone: "Age of Empires, minus combat, with the heart of Watership Down." The game favors legible, spatial, watchable systems (build, see it grow, see the threat coming) over abstracted ledger-style management (menus of ratios and production chains). Individual named citizens carry real, felt stakes, but the systems underneath stay light — no genetics/bloodline ledger, no skill trees, no grinding.

Core pillars:
- Visible, spatial colony building — grow a settlement you can see, not a spreadsheet you optimize.
- A hostile, well-motivated world boundary — sound walls and traffic make the map's edges believable without inventing lore.
- A small, named cast — every citizen has a name and an earned story, at a scale (dozens, not hundreds) where that's meaningful.
- An occasional, high-stakes traversal mechanic — road-crossing as a deliberate expedition choice, not a constant obstacle course.
- Real ecology as inspiration, relaxed wherever it fights good gameplay.

## 2. Setting & World Geometry


### 2.1 The World Boundary


Highway sound walls — tall, vine-covered concrete barriers common along developed highway corridors — form the permanent, impassable outer boundary of the playable world. This is a real, visible piece of infrastructure, not an invented lore device: the world doesn't feel arbitrarily bounded, it feels walled in by something the player can recognize. Animals simply cannot scale it. The world beyond the wall is never modeled, explained, or made accessible.

The traffic lanes form the inner, dangerous-but-crossable boundary. Sound walls and traffic therefore create two different kinds of edge: one permanent and absolute, one dangerous but negotiable.

### 2.2 Three Zone Types


| Zone | Description | Role |
|---|---|---|
| Median Interior | Wide, forested median between independently-aligned carriageways (real highways sometimes separate northbound/southbound by hundreds of feet). Room for real 2D sprawl, tree cover, water features. | Home territory. Safest zone. Where base-building, growth, and day-to-day colony life happen. |
| Shoulder Strip | The band between the active traffic lanes and the outer sound wall. Often overgrown and undisturbed. Resource-rich but exposed on the traffic side and bounded (trapped) on the wall side. | Short, high-value, round-trip excursions — go in, extract value, retreat to safety already held. Repeatable risk/reward. |
| Carriageway Gap / New Segments | The traffic-lane gap between one median segment and the next, or between the interior and an unclaimed segment. | Rare, one-way, higher-stakes journeys: territory expansion, recruiting rare guests, reaching a new home. |


*Thin, exposed roadside strips (the classic narrow divided-highway median) exist as a related but distinct geometry — linear, constantly edge-adjacent, vertical-expansion-only. They are folded into the Shoulder Strip / connective-tissue role rather than treated as a fourth zone.*

## 3. Founding & Origin Sequence


Each playthrough opens with a short sequence establishing the player's chosen species at its most developed: a grand, mature ancestral home (a warren, den, or burrow-metropolis) shown in a way that also previews the tech ceiling the player can build toward over the course of the game.

That home is then destroyed by road construction — played, not shown as a passive cutscene, as a short escape episode using a re-skinned version of the road-crossing mechanic (see Section 7). The destruction functions as the origin of the game's central hazard vocabulary: the same infrastructure that wrecked the ancestral home is the traffic that threatens the new one, the wall that bounds it, and (in later versions) the road-work event that may threaten it again.

The escape sequence's odds are invisibly weighted so the founding trio always survives — narrative sequences that exist to make the story function are held to a different standard than systemic mechanics that must be genuinely fair and masterable. The sequence should still play as tense and dangerous through staging, pacing, and presentation, not through genuine random risk of failure.

The player selects one of three base species at the start of the game (Section 4). The founding population — around three citizens — is entirely that species. There is no cross-species mixing among the base three at any point in a playthrough (see Section 4.4).

## 4. Base Species


All three base species share one mechanical system in full: identical building categories, identical resource types, identical dodge-traffic mechanic, identical population/economy math. They differ only through bias on four shared stats. This keeps balance tractable, keeps player skill transferable across species, and avoids tripling the content-design workload — while still producing genuinely different playthroughs, because the same four dials cascade differently through every other system in the game.

### 4.1 The Four Shared Stats

- Speed — determines exposure time during a road-crossing; higher speed means a shorter window of vulnerability per crossing.
- Carry Capacity — resource volume moved per expedition trip.
- Food Consumption — ongoing upkeep cost per individual.
- Population-per-Upkeep — how many bodies a given food budget supports, i.e. how "expendable" losses are.

### 4.2 The Base Three


| Species | Speed | Carry | Food Cons. | Identity |
|---|---|---|---|---|
| Rabbit | 2.0 (fastest) | 1.0 | 1.0 | Precision / single high-stakes crossing. Fewest exposure events, shortest exposure window each. Best raw crossing skill expression, worst raw logistics throughput. |
| Squirrel | 1.0 | 2.0 (highest) | 1.0 | Logistics / spatial optimization. Best total cargo per trip and per food spent, at the cost of a bigger single-point-of-failure per loss. |
| Mouse | 1.0 | 0.6 per individual | 0.5 per individual | Swarm / concurrent triage. For equal food spend, out-carries rabbit (2.4 vs 2.0 total) by splitting the same value across twice the bodies and twice the exposure events. |


Worked example, equal food spend of 2 units: 2 rabbits carry 2.0 total across 2 exposure-events; 2 squirrels carry 4.0 total across 2 exposure-events; 4 mice carry 2.4 total across 4 exposure-events. Squirrel wins on raw efficiency, mouse edges out rabbit on carry-per-food while trading up to twice the number of risk events, rabbit wins on minimizing exposure time per event.

### 4.3 Species Identity in Play


Each species points player attention at a different step of the same shared loop — Gather → Cross → Return → Grow:
- Rabbit — the bottleneck is the Cross step. One clean, precise, high-speed read-and-commit moment per trip. Dispatch UI foregrounds the live crossing view.
- Squirrel — the bottleneck is Return/Grow. Crossings matter, but the interesting decision is spatial allocation of what you brought home across a decentralized cache network. Dispatch UI foregrounds the territory/cache map.
- Mouse — the bottleneck is Gather/Cross under volume. Several low-stakes crossings run concurrently; the skill is triage and divided attention, not any single crossing's execution. Dispatch UI foregrounds a multi-slot expedition queue.

*Design rule: no base species mechanic may let a colonist bypass the traffic-dodge system entirely (no flight, no tunneling under active lanes). Every base species is a full participant in the central hazard — they differ in tools and tactics for engaging it, never in whether they engage it.*

### 4.4 No Cross-Recruitment Among Base Species


A colony of one base species may never recruit individuals of either other base species as guests. This keeps the game's central choice — which species do you want to play — meaningful for the entire run, and avoids the stat-triangle collapsing into "eventually recruit one of each." Cross-species flavor, where wanted, lives entirely in the Guest Citizen system (Section 5), which draws from a roster deliberately outside the base three.

### 4.5 Central Hub Buildings


All three species share one functional "Town Center" building slot — identical role in the tech tree — with unique per-species names, art, and a signature maintenance task that doubles as a second expression of that species' identity:

| Species | Hub Name | Maintenance Task |
|---|---|---|
| Rabbit | Warren | Structural upkeep: periodically dig/reinforce additional exits as population grows, keeping escape capacity ahead of threat — a defensive/structural task. |
| Squirrel | Den | Den has a deliberately small food-storage cap; surplus must be actively shuttled out to the Cache Network (Section 6.3) — a spatial/logistics task. |
| Mouse | Burrow | Capacity/scaling upkeep: the dense Burrow Cluster requires ongoing expansion to stay ahead of population growth, or crowding-related problems emerge — a scaling task. |


## 5. Guest Citizens


Guests are non-base-species specialists recruited from the wider world. They are full, equal-status, named citizens once recruited — not a subordinate tier — but they occupy their own separate, small, capped slot pool and are recruited through a distinct ceremony rather than born into the colony.

### 5.1 Two Guest Types


| Type | Definition | Risk Profile | Slot Pool |
|---|---|---|---|
| Expedition Guests | Join a 3–4 unit expedition party; have carry/fight/special stats like base citizens; travel into danger. | Can be lost (wounded, maimed, rarely killed) exactly like base citizens. | Separate capped pool, grows with colony tier. |
| Colony Guests | Stationed at the Town Center; never leave; provide a passive, colony-wide buff. | Never directly at risk — a safe investment by design. | Separate, smaller capped pool, grows with colony tier. |


### 5.2 Expedition Guest Roster


| Guest | Bias | Signature Trait |
|---|---|---|
| Weasel | High carry/fight, poor economy (eats quickly). | Can actively engage and drive off small predator threats raiding the colony — a direct defensive answer. |
| Mink | Bias toward water/drainage-adjacent terrain. | Can use culverts/water features as a safe travel route unavailable to other citizens. |
| Fox | Big carry/fight, big food cost — the roster's "muscle." | Only species that can safely process a predator kill or major roadkill windfall into usable resources. |
| Crow | Lowest carry, lowest fight of the roster (present on both axes, per the universal rule, but weak on each). | 2x predator-detection radius for its entire expedition party, for as long as the crow is alive — drops instantly if the crow is lost. Cannot fly on demand; this is a grounded, vigilance-based trait, not a movement ability. |
| Deer Mouse | Comparable to base mouse, but not a numbers play. | The only unit that can forage/extract value from degraded, barren, or disturbed-ground terrain (construction debris, gravel scatter, the ruins of the original destroyed home) — a unique terrain-access niche, not a stat reskin of base mouse. |
| Snake | Cannot carry at all (no limbs) — the one deliberate exception to the universal carry rule. | Venom: fight applies a damage-over-time effect plus a low, flat, capped chance of instant kill (excluded or reduced against top predator tiers; does not stack — re-application refreshes rather than compounds). A defending snake reduces incoming venom-DOT duration from an attacking snake specifically (counterplay, not general DOT resistance). |


*Universal rule: every citizen carries and fights to some non-zero degree, so no unit is ever pure dead weight in a context outside its specialty. Snake's lack of carry capacity is the sole, deliberately-justified exception.*

### 5.3 Colony Guest Roster


| Guest | Passive Trait | Domain |
|---|---|---|
| Owl | Increases the colony's passive perimeter predator-detection radius (possibly night-weighted). | See farther (settlement-wide, spatial) |
| Songbird | Ambient morale/efficiency buff — citizens work and move slightly faster at home. | Work happier (settlement-wide, economy) |
| Toad | Reduces spoilage/loss rate on stored food. | Waste less |
| Firefly | Extends the duration of safe nighttime colony activity. | Stay active later |
| Groundhog | Advance warning of seasonal/weather events before they hit. | Know sooner |
| Turtle | Small, steady, unraidable passive resource trickle each cycle. | Never run dry |
| Bee | Increases yield from foraged plant resources. | Harvest more |


*Each Colony Guest claims one clear, non-overlapping verb, so the roster reads as real strategic combinations ("the see-farther one plus the know-sooner one") rather than several reskins of one generic buff.*

### 5.4 Recruitment Sequence


Recruitment is a Terraria-style "meet them, satisfy a condition, they move in" loop — lightweight, legible, no dialogue trees or trust meters:
- 1. Encounter — during an expedition (or, for Colony Guests, a general exploration/development beat), a chance to meet a guest-species individual in the wild, weighted by zone type (docile/economic guests more likely in the median interior; scavenger/predator-adjacent guests in the shoulder strip).
- 2. Amenability check — a chance roll determines whether this individual is open to joining at all. On success, they make an offer rather than joining outright.
- 3. The offer — the guest specifies the accommodation (den/perch/etc.) they need before they'll move in, becoming a visible, trackable build objective.
- 4. Build it — the player constructs the required structure using the normal building system. No new resource type or minigame.
- 5. Arrival — once complete, the guest arrives (with a short travel delay for anticipation) and occupies the appropriate guest slot.

The accommodation is built after a successful encounter and offer, never speculatively beforehand — this keeps early recruitment low-frustration (no wasted investment on a guest never found). Accommodation cost scales with guest rarity/power, giving a natural balancing lever independent of the guest's combat/carry stats.

### 5.5 Guest Slot Loss & Recovery


The accommodation built for a guest is single-use and non-transferable. If a guest dies or leaves, the accommodation is consumed, not merely vacated — recruiting a replacement (even of the same species) requires building a fresh accommodation from scratch, plus a new encounter. This is the real cost of losing a guest: not just the (rare) loss of a named individual, but the sunk building investment, which keeps guest loss meaningful without reintroducing a genetics/bloodline ledger.

## 6. Buildings & Tier Progression


### 6.1 Progression Model


Progression follows an Age-of-Empires-style four-tier model: shared building categories and shared core rules across all species, gated by economy/population/building milestones — not by guest recruitment, which remains fully optional at every tier so a "no guests ever" playthrough is always fully valid and never soft-locked.

| Tier | Expedition Guest Slots | Colony Guest Slots | Notes |
|---|---|---|---|
| 1 — Founding | 0 | 0 | Core building set only (6.2). Founding trio and natural growth. No guests available yet. |
| 1.5 | 0 | 1 (choice of Owl or Songbird) | First Colony Guest slot opens on an early milestone (e.g. completing the core Tier 1 building set). A gentle, safe on-ramp to the recruitment ceremony before any risk is involved. |
| 2 — Expansion | 1 | 1 | First Expedition Guest slot opens. Shoulder-strip raiding becomes a regular activity. |
| 3 — Established | 2 | 2 (remaining roster unlocks) | Second Expedition Guest slot; the rest of the Colony Guest roster (Toad, Firefly, Groundhog, Turtle, Bee) becomes selectable. Buildings supporting carriageway-crossing expeditions unlock. |
| 4 — Mature | 3 | 3 | Final slot for both guest types. Full tech tree. The species' aspirational "mansion" structure from the opening sequence becomes buildable. |


### 6.2 Tier 1 Building Categories

- Town Center (Warren / Den / Burrow) — central hub, population anchor, houses non-storage chambers. One per colony; losing it is a major setback, not a run-ending wipe.
- Housing — population capacity. Cost/capacity biased per species (cheap & high-capacity for mouse; supports the exit-maintenance mechanic for rabbit; average for squirrel).
- Storage — the food/resource stockpile. Conventional single building for rabbit and mouse; for squirrel, deliberately replaced by a small-cap Den plus the Cache Network (6.3), the one structural asymmetry in the shared building set.
- Nursery — population production rate, distinct from Housing's capacity. Mouse's version ties into the Burrow Cluster's density mechanic (higher throughput, more frequent expansion needs).
- Watch-post / Sentry — basic predator-detection structure, feeding the base-defense telegraph system directly (deliberately modest without an Owl or Crow, to keep those guests valuable).
- Refuge — a non-combat fallback shelter citizens path toward automatically when a predator threat is telegraphed.

### 6.3 Squirrel's Cache Network


Squirrel's Den has a deliberately small food-storage cap; bulk storage lives instead in a scattered Cache Network of small, cheap, individually-capped structures placed across the territory. Squirrel citizens must actively shuttle surplus from the Den out to caches. This is squirrel's ongoing "maintenance task" (an active logistics puzzle rather than a set-and-forget system) and its core resilience trade-off: losing one cache to a raid never wipes the whole stockpile, at the cost of constant spatial management.

### 6.4 Care & Amelioration (Tier 3/4)


An optional Tier 3 or 4 building (an infirmary/care-den, named per species) offers partial — never full — amelioration of the Maimed debilitation state (Section 8.3): recovering roughly half the lost stat or granting a smaller compensating bonus. The maiming itself remains canonical and permanent in the citizen's log, description, and reference image; the building represents the colony learning to better support its injured veterans, not undoing what happened to them. Entirely optional — a legitimate colony may never build one.

## 7. The Road-Crossing Mechanic


Road-crossing is deliberately not the game's central, constant loop — repeated back-and-forth dodging would wear thin as a sole focus. Instead it is the shared traversal skill test underlying two distinct, purposeful contexts, plus the founding escape sequence.

### 7.1 Two Purposeful Contexts

- Shoulder Raids — short, round-trip excursions from the median interior into the resource-rich, wall-bounded Shoulder Strip. Enter danger temporarily to extract value, then retreat to safety already held. Repeatable, a regular activity from Tier 2 onward.
- Carriageway Crossings — rare, one-way, high-stakes journeys to expand into a new median segment, reach a rare guest, or (in the founding sequence) escape into the very first home. Dramatic because they are rare, not despite it.

### 7.2 Traffic as Weather, Not a Static Obstacle


Traffic follows learnable dynamic patterns rather than a fixed obstacle course: rush-hour surges, quiet overnight windows, seasonal variation, and rare generous windows opened by in-world events (a multi-vehicle incident temporarily halting a lane, a storm changing traffic behavior). Reading and timing around these patterns is the core skill being tested, not simple reflex alone.

### 7.3 Species Expression of the Same Mechanic


The underlying crossing mechanic, resolution logic, and stat inputs are identical for all three base species — see Section 4.3 for how each species' stat bias reframes the same mechanic into a different felt experience (precision for rabbit, post-crossing allocation for squirrel, concurrent triage for mouse).

### 7.4 The Founding Escape (Special Case)


The final beat of the origin sequence (Section 3) is structurally the same crossing mechanic, re-skinned as fleeing construction equipment into the median for the first time. Odds are invisibly weighted to guarantee the founding trio's survival; tension is carried entirely by staging and presentation. This is the one place the mechanic is not genuinely fair, and deliberately so — a narrative-serving exception to an otherwise fully systemic, masterable mechanic.

## 8. Hazards, Combat & Defense


### 8.1 Two Combat Contexts


| Context | Character | Resolution |
|---|---|---|
| Base Defense | Predators approach the home territory directly. Legible, spatial, watchable — the player sees the threat coming and has time to react. | Telegraphed approach (advance warning scaled by detection stat/buildings/guests) → citizens auto-path toward Refuge unless the player commits a defender → single-beat stat comparison (defender fight vs. threat power, weighted by some randomness) resolves the encounter. |
| Expedition Combat | A threat encountered mid-mission, away from home support; smaller-scale, more personal since it happens to a specific named party. | Whole-party-vs-threat aggregate fight-stat comparison, not unit-by-unit tactics. Species/guest specials (weasel's fight, snake's venom, crow's detection letting you avoid the fight) modify or bypass the encounter before it resolves. |


Both contexts are deliberately resolution-based rather than manually fought in real time: no hit points, cooldowns, or ability trees. The player's real decisions happen upstream — who to bring, whether to commit a defender, what to invest in detection — consistent with the game's overall preference for legible systems over ledger-heavy or twitch-combat depth.

### 8.2 Injury as the Default Stake


Citizen death is reserved for extreme, unlucky outcomes only — common enough to matter, rare enough that the named-citizen system stays affectionate rather than exhausting. Most failed encounters instead produce an injury, giving the game a real middle tier of consequence between "nothing happened" and "gone forever."

### 8.3 Wounded vs. Maimed


| State | Duration | Effect |
|---|---|---|
| Wounded | Temporary — heals after a recovery period at the Town Center/Refuge. | Temporary reduction to a relevant stat (fight, carry, or speed). |
| Maimed | Permanent. | Permanent partial stat reduction, paired with a unique, specific, visible disability (one eye lost, a cut tail, a limp) encoded into the citizen's log, description, and canonical reference image. Often paired with a small compensating trait, so a maimed citizen reads as changed and storied rather than simply weakened. |


Base defense failures default to injury rather than death; death is reserved for defenders already wounded and overwhelmed, or citizens caught fully unprotected. Expedition failures follow the same shape — a bad roll usually costs an injury (which may slow or strand the party, adding its own tension to getting home) rather than a body.

### 8.4 Universal Naming & Earned Identity


Every citizen — base species and guest alike, no tier distinction — is named on creation or recruitment. At the game's population scale (soft caps roughly in the dozens, not hundreds) this is manageable without a genetics/bloodline ledger underneath it. Following the model of Dwarf Fortress (full generated identity for everyone, but attention paid only where something notable happens) and Watership Down (a small cast where prominence is earned through action, not assigned upfront), each citizen keeps a small persistent log of notable events — missions survived, injuries taken, milestones reached. A small number of automatic, passive milestone bonuses (tied to the action-mode skill growth in 8.5) may trigger off this log, but it is not a player-managed system — narrative weight accrues through play, not through a menu.

### 8.5 Action-Mode Skill Growth


Individual growth is scoped narrowly to the action-mode (crossing and encounter) stats only — reaction timing, detection, fight — never to colony-economy stats like carry cap or food consumption, which stay static and simple. Growth is passive and automatic, an emergent byproduct of survived encounters (a citizen who's crossed and raided repeatedly becomes a de facto veteran), not a player-allocated skill tree or a grindable training system. This keeps the colony-management side clean and AoE-legible while still rewarding — and creating real stakes around protecting — experienced individuals.

## 9. Seasons & Weather


A single shared seasonal calendar modifies existing systems via multipliers and telegraphed events, rather than introducing a separate weather subsystem.

| Season | Colony-Level Effect | Expedition-Level Effect |
|---|---|---|
| Spring | Boosted foraging yield; higher Nursery/population growth. Thin regrowth means less predator concealment — abundance and exposure both peak. | Standard crossing conditions. |
| Summer | Peak resource yield, but peak traffic and the signature hazard: a telegraphed mowing event that temporarily strips median cover, forcing a scramble to shelter or a temporary foraging/defense penalty until regrowth. | Worse traffic odds — more vehicles, shorter/less frequent gaps. |
| Autumn | Hoarding season — squirrel's thematic high point; a colony-wide soft-pressure "stockpile before winter" beat for all species. | Standard crossing conditions. |
| Winter | Reduced foraging yield and population growth; increased predator aggression (hunger-driven). Snake guests/expedition members may be unavailable or weakened (seasonal dormancy). | Reduced predator activity in some cases, offset by cold-exposure risk contributing to Wounded status (a temporary-hardship framing, distinct from violent-injury Maiming). |


Shorter-cycle weather events (storms) sit under the seasonal layer and can open rare bonus crossing windows, consistent with the "traffic as weather" framing in Section 7.2. The Groundhog Colony Guest's advance-warning trait gives players a direct mechanical answer to these telegraphed seasonal hazards.

## 10. Version Roadmap


Whole-number versions represent a fundamental change to the opposition model or core systems. Half-number (.5) releases are additive DLC content layered on an already-complete base version, requiring no new opposition type.

| Version | Type | Content |
|---|---|---|
| V1 | Core game | Everything in Sections 1–9. Solo colony vs. environment: random, ambient, unorganized predators. No rival intelligence, no persistent NPC settlements. |
| V1.5 | DLC (additive) | Unique World Events — rare, scripted, high-drama set-pieces layered on the V1 base: multi-vehicle pileups (temporary safe crossing windows plus scavenging windfalls), mass bird migrations (predator surge paired with rare guest-encounter opportunities), and a returning road-construction threat that directly echoes the founding trauma. Rarer than a Terraria-style recurring raid rhythm — closer to once-or-twice-per-campaign bespoke drama. |
| V2 | Major version | Rival Civilizations — the same predator/hazard roster reorganized into actual competing AI-controlled colonies of animals, roughly 8–10 median segments away, contesting territory and resources. The fundamental change: environment-only opposition becomes environment plus peer competition. |
| V2.5 | DLC (additive) | Persistent Multi-Species Cities — the "rest-stop metropolis" reveal. A highway rest stop is the one place a highway-bound animal civilization could plausibly urbanize (concentrated human food waste, structures, shelter) without breaking the game's road-right-of-way containment. Builds on the V2 rival-civilization layer; the single largest content commitment on the roadmap. |


*Seeding for V2.5 is worth planting cheaply in V1 — rumors, a mysterious well-worn trail, an occasional trader-style NPC event — so the eventual civilization reveal lands as planted rather than bolted on.*

## 11. Open Questions & Parking Lot


Items discussed but not yet fully resolved, flagged here rather than silently decided:
- Base-species population/reproduction mechanic — referenced throughout as a future detailing pass; not yet specified.
- Exact tier-advancement thresholds (population/resource/building targets) beyond the guest-slot schedule in Section 6.1.
- Whether the destroyed ancestral home is ever revisited in-game (a visible-but-unreachable location, a rare scavenging location reachable only by Deer Mouse, or narrative flavor only).
- Full base-defense and expedition-combat resolution formulas (deterministic threshold vs. weighted-random roll) — the shape is specified in Section 8.1, the exact math is not.
- UI/roster-screen structure for up to ~40 named citizens (a flat list is likely sufficient at this scale, per the Dwarf Fortress comparison in Section 8.4, but unconfirmed).
- Dynamic per-citizen and per-base AI image generation, using a persistent text-log-plus-reference-image image-to-image update pipeline — a well-specified but deliberately tabled stretch system, architecturally separate from core gameplay design and likely deserving its own technical design document.
- Whether V2.5's cities interact with V2's rival civilizations as a distinct third faction type, or supersede them in city-adjacent segments.

## Appendix: Design Philosophy Notes


A few cross-cutting principles emerged over the course of this document's development and are worth stating explicitly, since they should guide resolution of the open questions above and any future system design:
- Ledger vs. legible: prefer systems where the player's core engagement stays visible and spatial (watching a colonist carry resources across a map) over systems that pull attention into abstracted menus of numbers to optimize in isolation. When in doubt, choose the version that would still make sense with the art removed only if it's still fundamentally a spatial decision, not a spreadsheet one.
- One shared system, biased expression: prefer giving species/guests/seasons a bias on shared mechanics over giving each one its own bespoke subsystem. Reserve genuinely unique mechanics for a tightly capped number of signature moments (one per guest, one per species hub) rather than letting them proliferate.
- Narrative-serving mechanics may be authored/guaranteed; systemic mechanics must be genuinely fair. It's correct to hold these to different standards, and to make that decision consciously and explicitly rather than by default.
- Attention is earned, not demanded: identity, names, and narrative weight should accrue through what happens to a citizen during play, not through upfront systems the player must actively manage before anything has happened.
- Every guest/unit contributes on the roster's baseline axes (carry, fight) even where it's not their specialty, so no recruit is ever pure dead weight outside one specific context.
