# MEDIAN

## Game Design Document v0.3 — Canonical Context Edition

**Working title:** MEDIAN  
**Genre:** Atmospheric animal colony builder with high-stakes expedition action  
**Primary platform:** PC and console, including handheld console form factors such as Steam Deck and Switch-class devices  
**Mode:** Single-player  
**Camera:** Readable miniature-diorama colony view, shifting to a more immediate tactical view during crossings and expeditions  
**Status:** Pre-production concept document  
**Origin:** Conceived by Asa Wember, July 2026, after observing highway medians from a bus between Washington, DC and New York City

> **Animal colony building on highway median strips.** Build a beloved, physically legible settlement in the overlooked green islands between highways, then risk named citizens on dangerous expeditions across asphalt and along a chain of changing median biomes.

### Elevator pitch

**Age of Empires-style colony progression in a highway median, with the emotional animal-world storytelling of *Watership Down* and *Mouse Guard*.** The player guides one small civilization of rabbits, squirrels, or wood mice. Safe local sustenance supports everyday life, but lasting advancement requires expeditions beyond the home median: across live traffic to the resource-rich Margin, or down the highway to discover new biomes, establish outposts, meet outsiders, and eventually connect with a distant multi-species animal metropolis.

The colony is the heart of the game. Expeditions are not the reason the base exists; they are the dangerous, dramaturgically justified action counterpart to a base-building game. The player should become attached to the place they build and to the handful of named animals who live there.

---

## 1. Creative thesis

MEDIAN is about making a permanent home in a place humans consider leftover space.

The highway provides more than a visual setting. It supplies the world geometry, boundaries, resources, hazards, rhythms, soundscape, and scale contrast. The animals do not imitate a tiny human industrial society. They remain animals, using teeth, paws, instinct, ecological knowledge, plant matter, and scavenged objects to survive inside human infrastructure.

The desired emotional rhythm alternates between:

- **Sanctuary:** patient construction, observation, maintenance, social life, and attachment inside the Home Median.
- **Exposure:** leaving safety for an expedition whose outcome can create resources, knowledge, relationships, injuries, and stories.
- **Return:** bringing both material gains and lived consequences back into the colony.

The home must feel worth protecting. Danger has meaning because the player knows exactly who went out and what they came back to.

### 1.1 Core inspirations

- **Age of Empires:** comprehensible advancement tiers, a satisfying transformation from vulnerable settlement to mature civilization, and spatially readable economic growth.
- **Watership Down:** animal-scale peril, social identity, folklore, political encounters, and the terror response known as going **tharn**.
- **Mouse Guard:** small-animal heroism, patrol-like journeys, weather and landscape as existential forces, and material culture assembled from the natural and discarded world.
- **Colony builders and town simulators:** attachment to a settlement shaped over time, visually active citizens, and emergent personal stories.

### 1.2 What the game is not

MEDIAN is not:

- An arcade road-crossing game with a base-management wrapper.
- A large-population swarm simulator.
- A combat-first RTS.
- A spreadsheet that hides its world behind menus.
- A technology fantasy in which animals become miniature humans, master electricity, or industrialize the corridor.
- A game about abandoning the town whenever the next biome opens.

---

## 2. Design pillars

### 2.1 Sentimental base-building first

The Home Median is the permanent emotional and mechanical center of a campaign. The player improves, densifies, decorates, and remembers this place rather than replacing it. Distant expansion adds a network around the home; it does not negate the home.

### 2.2 Named citizens, low population, durable identity

Every core citizen is named, visually distinguishable, and historically tracked. Population growth is slow enough that the loss, injury, bravery, and specialization of one animal matters. Citizens are companions and community members, not replenishable unit tokens.

### 2.3 Ledger and legible

Important state should first be visible in the world: a leaking burrow, a thin food store, a frightened posture, a frayed bridge, an animal moving with a limp. A numerical ledger must also exist for players who require clarity, especially for colony resources, capacity, construction, maintenance, and schedules.

This does **not** mean every number is public. Character aptitudes and unexplored expedition danger retain uncertainty. The ledger clarifies known colony state; it does not eliminate discovery or suspense.

### 2.4 Expeditions make stories and enable progress

Nearby resources can sustain the colony, but meaningful advancement requires leaving home. Expeditions must be materially worthwhile even if all optional generative imagery is removed. Their systemic rewards include progression scrap, special artifacts, new biome access, outposts, Guest Citizens, intelligence, trade relationships, and story flags.

### 2.5 Traffic behaves like weather

Traffic is a dynamic environmental system rather than a row of predictable moving platforms. Density, speed, vehicle class, wind shear, headlights, spray, thrown debris, pollution, accidents, and road work produce changing conditions that can be read but never made perfectly safe.

### 2.6 Consequence without disposability

Failure usually produces fear, wounds, lost cargo, changed relationships, or maiming before death. Consequences persist, but a maimed citizen remains valuable. Experience can turn a physically limited veteran into a calm expedition anchor, teacher, planner, craft specialist, or colony leader.

### 2.7 Mechanical restraint, expressive variety

The simulation uses a small number of understandable resources and attributes. Visual skins, history, environment, species, and event combinations create variety. Do not add a new currency or stat when an existing system can express the same decision.

---

## 3. World geometry and terminology

### 3.1 The full roadway cross-section

From one outer boundary to the other, a typical playable cross-section is:

**Sound Wall → Margin → Highway → Home Median → Highway → Margin → Sound Wall**

The arrangement is symmetrical in principle, though terrain, lane count, elevation, vegetation, and accessibility may differ on each side.

### 3.2 Home Median

The **Home Median** is the central strip between opposing carriageways and the site of the player’s colony. It can be narrow or broad, grassy or wooded, dry or culverted. It is relatively safe from traffic while still subject to predators, weather, runoff, vibration, disease, and Road Work.

The colony is built **in and on the Median**, not under the active highway and not in the Margin.

### 3.3 Highway

The **Highway** is the active multi-lane barrier between the Home Median and either Margin. It is both boundary and playable hazard. Standard outbound Margin expeditions begin at the Home Median, stage at protected micro-cover near the road edge, and cross toward the Margin.

### 3.4 Margin

The **Margin** is the resource-rich, ecologically chaotic strip between a highway and its outer sound wall. Fast pioneer plants, windblown seeds, insects, roadkill traces, litter, packaging, tire fragments, and other human detritus accumulate there.

The Margin is renewable rather than permanently exhaustible. Nodes deplete locally, then replenish through plant growth and new waste deposition. Road Work can wipe the strip nearly bare for a time, resetting cover and yield before succession begins again.

### 3.5 The median chain

The Home Median is one segment in a longitudinal chain of medians extending up and down the highway corridor. Remote segments differ in width, hydrology, vegetation, infrastructure, exposure, predators, and resource character. They are reached through longitudinal expeditions represented at a useful strategic scale rather than by simulating every continuous mile.

### 3.6 Example median biomes

- **Thin Grass Ribbon:** little building room, excellent sightlines, high wind exposure.
- **Wooded Median:** trees enable squirrel infrastructure and shade, but conceal predators.
- **Culvert Garden:** reliable water and rich soil with flood risk.
- **Creek Split:** abundant ecology divided by moving water.
- **Pond Hollow:** food-rich wetland with disease, amphibian, and snake encounters.
- **Concrete Trench:** scarce vegetation, strong shelter opportunities, extreme heat and runoff.
- **Overpass Shadow:** complex vertical structure, darkness, noise, and protected dead spaces.
- **Interchange Expanse:** broad territory, many routes, severe navigational and predator exposure.

---

## 4. Player experience and core loops

### 4.1 The domestic colony loop

1. Observe citizens, structures, stores, weather, and local ecology.
2. Assign safe work: forage, build, repair, prepare food, tend young or wounded citizens, craft, and organize stores.
3. Improve the Home Median’s layout and resilience.
4. Read approaching needs: seasonal pressure, Road Work risk, scarce scrap, a promising expedition, or a citizen opportunity.
5. Decide whether to commit eligible citizens to an expedition that day.
6. Absorb the expedition’s gains and consequences into the physical town.

The player may spend substantial time arranging and watching the colony, but game time is structured. Pausing is available for accessibility and strategy; pausing does not advance production.

### 4.2 The progression loop

**Safe local ecology supplies subsistence → structures and ambitions demand salvage → expeditions secure scrap, artifacts, knowledge, and connections → the colony becomes safer and more capable → greater range exposes richer but more contested opportunities.**

### 4.3 The expedition loop

1. **Choose a purpose:** Margin Raid, Scout, Establish Outpost, Outpost Visit, or special narrative journey.
2. **Choose citizens:** one expedition per citizen per day. Selection depends on known traits, experience, wounds, relationships, species capabilities, Guest abilities, and player intuition.
3. **Prepare:** allocate carrying equipment or mission-specific supplies without turning preparation into a loadout spreadsheet.
4. **Depart:** for a cross-lane mission, enter the outbound Highway Crossing action sequence. Longitudinal travel uses appropriate corridor hazards and abstracted travel beats.
5. **Reveal conditions on arrival:** contest status and encounter type are not disclosed at launch.
6. **Resolve the location:** forage, salvage, negotiate, evade, fight, rescue, scout, build, or withdraw.
7. **Return:** most successful Margin returns resolve quickly; some impose an incident or renewed crossing crisis.
8. **Record the story:** update cargo, citizen history, wounds, fear memories, relationships, maps, and optional generated art.

---

## 5. The game day and calendar

### 5.1 Daily structure

A game day is a bounded operational cycle, not infinite tinkering. The world advances through recognizable traffic periods. Exact clock length remains a prototype variable, but the intended rhythm is one meaningful expedition opportunity per citizen per day.

The player can perform colony management throughout the day, subject to citizen availability and time. Launching an expedition commits its participants for that day. No citizen may complete a second expedition before the next dawn.

Suggested daily beats:

- **Morning Rush / Domestic Opening:** consumption and recovery resolve; the player reviews the colony, repairs, builds, and makes assignments while traffic is dense and stressful.
- **Midday Operating Window:** the clearest default expedition window, balanced by daylight predators and faster vehicles.
- **Evening Rush / Domestic Return:** noise, fumes, and erratic traffic discourage normal departures; returning consequences and home tasks take focus.
- **Night Velocity:** optional specialized departures may exist, but are rarer and meaningfully different rather than a routine second expedition. Low traffic density is offset by extreme vehicle speed, reduced visibility, owls, and fear.
- **Dawn Reckoning:** food consumption, healing progress, structural wear, regrowth, scheduled events, and calendar advancement resolve.

### 5.2 Traffic cycles

- **Rush:** dense, slower vehicles; fewer clean gaps, strong fumes, vibration, noise, and stop-start unpredictability.
- **Lull:** moderate density and speed; visually readable but exposed to raptors.
- **Night Velocity:** few vehicles at very high speed; headlights, darkness, spatial audio, and tharn risk dominate.
- **Anomaly:** an accident, lane closure, weather event, convoy, maintenance crew, or unusual lull temporarily rewrites the normal pattern.

Time of day is an in-game system, not tied to the player’s real-world clock.

### 5.3 Seasons

Season length and campaign duration require playtesting. Seasons should be long enough to establish a distinct operating rhythm, not flip every few sessions.

- **Spring — Thaw and Growth:** rain, flooding, rapid Margin regrowth, abundant greens, first possible breeding window.
- **Summer — Pavement Heat:** dehydration pressure, heat plumes, exposed-day penalties, aggressive Road Work and mowing.
- **Autumn — Detritus Harvest:** strong winds deliver scrap and seeds; stockpiling and a possible second breeding window.
- **Winter — Freeze and Reserve:** low local forage, expensive warmth, draft and exposure risk, reliance on preparation.

### 5.4 Road Work

**Road Work** is a family of municipal disturbance events, not merely mowing. It functions like severe weather at the campaign scale.

Possible forms include mowing, vegetation clearing, salt application, drainage work, barrier repair, resurfacing, construction staging, trash collection, and lane reconfiguration. Effects vary by zone and species architecture. Road Work can erase Margin cover and resources, damage exposed surface works, flood or crush tunnels, remove a squirrel anchor tree, create new salvage, or temporarily open unusual safe routes.

Road Work should be forecast imperfectly through signs: human machinery, warning markers, smell, vibration, rumors, or Metropolis intelligence. It must create adaptation rather than arbitrary punishment.

---

## 6. Home colony simulation

### 6.1 Scale

This is a deliberately low-population colony game. A mature colony should still be small enough that the player recognizes its members. Exact caps differ by species and tier, but population growth never becomes a continuous unit-production conveyor.

### 6.2 Citizen work

Domestic tasks include:

- Gathering renewable local sustenance and natural material.
- Carrying and storing supplies.
- Building, reinforcing, and repairing species-specific structures.
- Preparing reserves and special expedition provisions.
- Healing wounded citizens.
- Caring for a seasonal litter.
- Teaching, watchkeeping, mapping, crafting, and organizing.
- Maintaining outpost routes and receiving deliveries.
- Hosting and benefiting from Guest Citizens.

Assignments should produce visible action in the colony. Batch orders and priorities reduce repetitive clicking.

### 6.3 Resources

The lean canonical economy has three regular mechanical categories:

1. **Sustenance:** food and hydration consumed by citizens, used for reserves, recovery, and rare reproduction.
2. **Flexible Scrap:** binding, weaving, lashing, sealing, and flexible construction material.
3. **Rigid Scrap:** bracing, shielding, surfacing, tools, and load-bearing reinforcement.

Items may retain flavorful identities—clover, mustard seed, apple core, copper wire, packaging ring, burlap strand, bottle cap, bread clip, glass pebble—while resolving into these shared categories. A few distinctive finds can carry special traits without requiring separate global currencies.

**Special Artifacts** are rare, non-stackable or tightly limited objects that unlock a blueprint, solve a specific problem, enable a trade, improve an adaptive device, or open a narrative option. They are not generic “technology keys,” and their uses must remain believable for animals.

### 6.4 Construction and decay

Structures visibly age through moisture, rot, wind, vibration, salt, heat, and use. Maintenance creates ongoing work, but fully upgraded construction can reduce or eliminate routine decay in a limited footprint. The objective is meaningful stewardship, not a universal repair tax.

No single decay formula in the old thread is canonical. Prototype the system using broad durability states and event-based wear before considering fine percentages.

### 6.5 Example structure families

Shared functions should be visually and spatially adapted to each species:

- Town Center / communal heart.
- Food store and dry reserve.
- Workshop and scrap store.
- Shelter and sleeping chambers.
- Nursery sanctuary.
- Infirmary / recovery nest.
- Staging Post at the highway edge.
- Lookout and warning network.
- Guest accommodation or integration space.
- Memorial and history space.
- Species-signature transport, storage, and safety structures.

Guest accommodation is not necessarily a disposable bespoke house. If a Guest leaves or dies, the relevant habitat can be cleaned, adapted, or renovated for another compatible guest.

### 6.6 Reproduction and recruitment

Core-species reproduction is rare, seasonal, expensive, and player-authorized.

- A mating opportunity exists only in suitable seasonal and colony conditions.
- Two citizens are committed to care and cannot be treated as normal expedition labor during the critical period.
- Sustenance, shelter, safety, and space requirements are substantial.
- A successful cycle yields a very small number of named young.
- The player is never encouraged to breed disposable replacements.

Exact biology can be stylized consistently across species to protect pacing. Recruitment of Guests and occasional displaced core-species wanderers supplements growth without creating a factory loop.

### 6.7 Death and memorialization

Death is possible but uncommon outside catastrophic errors or extreme events. It should never become the routine expected price of ordinary expeditions. When a citizen dies, their dossier, portrait, relationships, and key history move into a colony archive. The player may place an understated physical memorial in the Home Median.

---

## 7. Core species

Each campaign selects one core species. The three campaigns share the same economy, world logic, progression skeleton, expedition categories, and citizen model. Asymmetry comes from spatial architecture, stat bias, and one defining home-system problem—not from three unrelated games.

### 7.1 Rabbit — Burrow civilization

**Personality:** grounded, communal, fast, cautious, architectural.  
**Spatial identity:** an underground warren connected to surface forage and multiple bolt holes.  
**General bias:** strong sprinting and teamwork, larger bodies and appetites, modest carrying efficiency.

Rabbit construction is a depth-and-flow puzzle. Chambers, tunnels, food stores, nurseries, and exits must fit beneath limited terrain. Surface access points create efficiency but also exposure. Poor circulation produces bottlenecks during a predator alarm or Road Work emergency.

**Signature system — Warren Flow:** The player manages routes, chamber congestion, structural support, and escape coverage. The goal is not to chase a hidden “bolt-hole score,” but to create a visibly functioning network with enough exits and alternate paths.

**Strengths:** fast open-ground movement, powerful coordinated hauling, efficient excavation, strong rescue capability.  
**Pressures:** high food demand, tunnel moisture and collapse risk, limited vertical access, crowding at entrances.

### 7.2 Squirrel — Canopy civilization

**Personality:** mobile, opportunistic, dispersed, daring, logistical.  
**Spatial identity:** nests, bridges, branches, trunks, guardrails, and scattered caches.  
**General bias:** strong carrying and climbing, flexible routes, greater exposure when forced to ground.

Squirrel construction turns the Home Median into a layered vertical network. Rather than one perfect central warehouse, supplies are distributed among visible caches. Location, redundancy, retrieval time, weather protection, and theft risk matter.

**Signature system — Cache Network:** The player balances convenience against resilience. Centralizing goods is efficient but vulnerable; dispersal protects the colony but consumes labor and travel time.

**Strengths:** vertical mobility, heavy-item hauling, rapid response across connected canopy, route redundancy.  
**Pressures:** exposed infrastructure, tree loss, weather damage, cache spoilage or theft, dependence on anchor points.

### 7.3 Wood Mouse — Dense, distributed civilization

**Personality:** ingenious, quiet, compact, cooperative, adaptable.  
**Spatial identity:** tiny rooms, root passages, culverts, grass tunnels, and densely interlocked micro-infrastructure.  
**General bias:** low consumption and footprint, high acceleration and stealth, low individual carrying capacity and physical resilience.

Mice permit the densest settlement, but they remain named individuals—not an anonymous swarm. Their spatial challenge is coordinating many small jobs and narrow routes without losing readability or turning the game into queue management.

**Signature system — Relay Network:** Mice divide loads and tasks across short, visible handoffs. The player designs stations, micro-paths, and work neighborhoods so that small carrying capacities become an efficient collective chain.

**Strengths:** efficient use of food and space, stealth, access to small voids, rapid light-material construction.  
**Pressures:** low load capacity, vulnerability to wind shear and direct trauma, narrow-route congestion, individual fragility.

The rejected “pheromone macro-swarm” concept is not canonical. Mouse citizens are selected, named, and valued under the same character rules as rabbits and squirrels.

---

## 8. Citizens, aptitude, fear, wounds, and maiming

### 8.1 Citizen dossier

Every citizen has:

- Name, species, appearance, and portrait.
- Age/life stage and relationships.
- Broad visible aptitude descriptors.
- Traits and learned roles.
- Expedition and colony-work history.
- Wounds, permanent impairments, adaptive equipment, and fear memories.
- Notable acts, discoveries, relationships, and memorial links.

Underlying values may include movement, carrying, stealth/noise, perception, resilience, stress threshold, and social aptitude. Exact values remain hidden. Players see descriptive bands, clear consequences, and history rather than raw 1–100 ratings.

### 8.2 Fear and going tharn

Fear is a core system, not a cosmetic morale debuff.

Stress accumulates through exposure to traffic, predators, darkness, noise, injury, exhaustion, separation, and recalled trauma. When a citizen exceeds their threshold, they may go **tharn**: freezing, dropping carried items, failing to obey movement commands, and requiring rescue or calming intervention.

Tharn creates a rescue dilemma without guaranteeing death. A companion can return, guide, drag, shield, or rouse the frozen citizen, risking additional exposure. Retreat and abandonment remain possible, painful choices.

Survival can create a persistent fear memory associated with a trigger. Recovery, trusted companions, experience, a veteran leader, and certain Guest effects can mitigate future risk. Trauma does not simply transform into a numerical bonus; any growth must feel earned and character-specific.

### 8.3 Harm ladder

1. **Shaken / exhausted:** short recovery, reduced readiness.
2. **Wounded:** meaningful temporary impairment requiring rest, food, care, and multiple days to heal.
3. **Maimed:** permanent bodily change with lasting functional consequences.
4. **Death:** rare, final loss.

### 8.4 Valuing maimed citizens

Maiming has weight because it changes what a citizen can safely do, not because it converts them into dead weight.

- Physical limitations remain real and visible.
- Experience, relationships, knowledge, and emotional importance remain intact.
- Adaptive equipment can ameliorate—not erase—an impairment.
- Colony roles value judgment, teaching, crafting, logistics, watchkeeping, care, mapping, and leadership as well as speed.
- Some veterans become calm expedition anchors who reduce tharn risk in less experienced companions.
- Workplaces and paths can be adapted for accessibility.
- A maimed citizen may still expedition when the player judges the route and role appropriate.

The game must not imply that disability automatically grants genius or supernatural compensation. Veteran strengths emerge from lived history and role design, while adaptation expands access.

### 8.5 Optional dynamic portrait history

See Section 16. When enabled by the game designer and supported by the player’s setup, permanent appearance changes can update a citizen’s canonical portrait. The system records a specific factual change—such as “lost right foreleg in a weasel attack”—and produces a revised image derived from the prior canon image.

---

## 9. Expedition system

### 9.1 Expedition categories

#### Margin Raid

A short, cross-lane mission from Home Median to either adjacent Margin. Used for renewable forage, scrap, discoveries, encounters, and high-frequency advancement needs. A Margin beside a wild, uncolonized median can also be raided; it simply lacks Home Hub efficiencies.

#### Median Scout

A longitudinal journey into an unknown median segment. Reveals biome, routes, hazards, resources, encounter character, and outpost potential.

#### Establish Outpost

Carries people and material to a scouted segment to construct a satellite facility. The founding citizens are expedition participants, not permanently deleted colonists; exact construction duration and risk are tuning variables.

#### Outpost Visit / Deep Extraction

Returns to an established outpost for active play: secure a large haul, repair facilities, respond to an event, meet a Guest, exploit a temporary opportunity, or push the exploration frontier.

#### Special Journey

A story-specific expedition such as reaching the ancestral home, escorting a Guest, attending the Metropolis, negotiating with a faction, or completing the final caravan.

### 9.2 Dispatch principles

The Dispatch Screen communicates:

- Destination, mission purpose, distance, known terrain, and known route demands.
- Eligible citizens and their qualitative readiness.
- Known traffic and weather observations.
- Cargo capacity and required mission supplies.
- Past expedition notes and rumors.

It does **not** disclose whether a destination will be contested, exact encounter odds, exact victory percentages, or the complete hidden resolution table. The player learns through experience, scouting, history, Guests, and environmental signs.

### 9.3 Crossing action

The standard cross-lane sequence runs **Home → Away**:

1. The expedition gathers at a Staging Post in the Home Median.
2. The tactical view reveals the lanes between natural endpoints: safe Median cover behind and Margin vegetation ahead.
3. The player reads traffic density, vehicle types, audio, headlight cues, wind shear, lane islands, and micro-cover.
4. The player commits movement between temporary safe positions or across the full gap, depending on road geometry.
5. Citizen speed, fear, wounds, load, and formation affect responsiveness without replacing player skill.

The action must be tense, brief, comprehensible, and tolerant enough that ordinary play does not produce routine mass casualty. Accessibility options should include time scaling, stronger telegraphs, simplified input, audio visualization, and possibly an assisted strategic resolution.

### 9.4 Return logic

After the player has successfully crossed outward and resolved the Margin, most returns should avoid repeating the identical challenge. The current design target is:

- **Common clean return:** a short automatic or cinematic crossing.
- **Uncommon incident return:** citizens get home, but lose cargo, suffer a minor wound, gain fear, or trigger a rescue beat.
- **Rare manual return crisis:** changing traffic, Road Work, predator pressure, weather, fatigue, or a narrative event forces the player back into the crossing action.

The old thread proposed **80% clean / 10% incident / 10% manual redo**. Retain that as an initial prototype hypothesis, not a locked probability. The desired experience is “return usually respects the completed challenge; occasionally the world complicates it.”

### 9.5 Encounters and contest

Contest is revealed only after arrival. Chance generally rises with distance from the Home Hub. Establishing an outpost extends the colony’s effective secure radius, reducing distance pressure around that node.

When an expedition is contested:

- **Most contests are antagonistic:** predators, territorial rivals, desperate scavengers, or environmental obstruction.
- **A substantial minority are neutral:** trade, warning, negotiation, aid, mutual avoidance, or recruitment opportunity.
- **A minority of neutral contacts are open to joining:** followed by a final contextual recruitment check or player choice.

The thread’s working branch was 70% antagonistic / 30% neutral; 25% of neutrals potentially recruitable. These values describe intent, not final balance.

Resolution should form a bell-shaped outcome distribution:

- Most results: ordinary success, compromise, retreat, partial yield, minor fear, or modest wounds.
- Rare bad tail: maiming, major loss, capture, separation, or death.
- Rare good tail: exceptional artifact, powerful information, diplomatic breakthrough, resource cache, or Guest opportunity.

The engine can use hidden probability, but the fiction must explain the result. Combat is only one response. Others include display, evasion, bribery, negotiation, trickery, surrendering part of the haul, rescue, and withdrawal.

### 9.6 Early expedition onboarding

The first expeditions should establish tone deliberately:

- **First major expedition:** an unavoidable or strongly framed “red in tooth and claw” confrontation. It teaches that the world is physical, contested, and capable of wounding citizens. It should not be tuned to force permanent maiming every campaign.
- **Second or third expedition:** heavily weighted toward a Guest opportunity—the campaign’s “Kehaar moment.” The player encounters an outsider as an individual and learns that the world contains relationships as well as threats.

---

## 10. Outposts and longitudinal expansion

Outposts expand the Home Median’s reach without becoming replacement towns.

### 10.1 Functions

- Reset or reduce distance-based expedition pressure.
- Produce a modest passive trickle from the local biome.
- Stage deeper scouting and active extraction.
- Hold supplies, warnings, and route knowledge.
- Host an assigned Ambient Guest in the mid-game.
- Create events that invite return visits.

### 10.2 Emotional and mechanical scope

An outpost is a named place with a visible footprint and history, but it is not a fully simulated second colony. The Home Hub retains population, civic life, most construction depth, and sentimental gravity. Outpost automation protects the game from multi-base micromanagement.

### 10.3 Active versus passive value

Passive yield is reliable but modest. Visiting an outpost opens the local action map and can produce greater rewards, special encounters, repairs, rare resources, and story events. The player chooses when the additional attention is worthwhile.

---

## 11. Guest Citizens

Guest Citizens are rare, named, non-breeding animals from outside the colony’s core species. Inspired directly by Kehaar in *Watership Down*, the system brings a wide variety of animal life into a campaign without requiring every species to support a full civilization ruleset.

Guests may be met during expeditions, rescued from hazards, introduced by rumors, encountered through trade, or found at the Rest-Stop Metropolis. The Metropolis is not the sole recruitment source.

Guest capacity expands slowly with colony progression, making each campaign’s mix distinctive.

### 11.1 Catalyst Guests

**Catalysts** actively join expeditions. They occupy a valuable Guest slot and introduce a bounded ability, traversal option, defensive behavior, negotiation route, or information advantage. They do not replace the core citizens’ need to take risks.

Candidate Catalyst roles inherited from the early concept should be verified against the original v0.1 source before production. Strong archetypal examples include:

- **Hedgehog:** durable escort or cover specialist; slow but hard to intimidate.
- **Mink or weasel-type runner:** agile brush and water traversal, with political risk around prey species.
- **Crow or other corvid:** aerial scouting, route intelligence, and trade access rather than ordinary hauling.
- **Owl:** night perception and fear control, balanced by ecological tension and limited availability.
- **Opossum:** heavy salvage interaction, intimidation resistance, and unusual recovery behavior.

Species portrayals must remain ecologically and tonally credible; “guest” does not automatically mean harmless.

### 11.2 Ambient Guests

**Ambient Guests** live at the Home Median or, once unlocked, an outpost. They provide a spatial passive effect while remaining visible residents with needs, routines, and relationships.

Examples:

- A songbird whose dawn song improves recovery or work rhythm within an audible radius.
- A toad that improves water quality around a wet culvert while slowing traffic through its chosen space.
- A bat that improves night warning and insect control near its roost.
- A mole that reveals soil and structural information but disrupts planned tunnel layouts.
- A turtle that steadies nearby citizens during alarms and supports a slow defensive role.

When several Ambient Guests live at home, the player selects one effect for a temporary **Cultural Focus** boost. Other Guests continue providing their normal effects. Ambient Guests may later be assigned to compatible outposts.

### 11.3 Recruitment shape

Recruitment is contextual rather than a universal currency purchase:

1. Encounter and understand the outsider’s situation.
2. Resolve a need, establish trust, bargain, or demonstrate compatibility.
3. Make room in the colony’s Guest capacity and habitat.
4. Resolve a final choice or uncertain acceptance where appropriate.

If optional generative imagery is enabled, a Guest’s arrival can create a commemorative image of their integration into the actual settlement.

---

## 12. Progression tiers

The tier system expresses increasing security, spatial reach, institutional capability, and ecological integration. It is not a ladder toward human-style industrialization. Names below are canonical working names and may be refined for tone.

### Tier I — Scavenger Camp

**Fantasy:** A vulnerable settlement proving it can survive.  
**Range:** Home Median and adjacent Margins.  
**Capabilities:** basic shelters, food storage, simple repair, Staging Post, first expeditions, one Guest slot.  
**Pressures:** exposure, fragile construction, scarce scrap, unknown corridor, fear.

### Tier II — Fortified Warren

“Warren” is used generically in interface copy only if it does not over-identify the tier with rabbits; an alternate shared name may be required.

**Fantasy:** The colony is organized, defended, and able to prepare rather than merely react.  
**Range:** first longitudinal scouts and one nearby outpost.  
**Capabilities:** refined storage, stronger routes, recovery space, better tools, limited food preservation, second Guest capacity.  
**Pressures:** maintaining the first network, seasonal preparation, contested sites.

### Tier III — Independent Colony

**Fantasy:** A mature, self-governing home that can endure without external rescue.  
**Range:** multiple outposts and deeper biomes.  
**Capabilities:** durable anchored construction, outpost logistics, Ambient Guest assignment, adaptive equipment, advanced role specialization, larger expedition choices.  
**Pressures:** regional relationships, Road Work at multiple nodes, preparing a corridor connection.

Tier III must not be named for or structurally dependent on the Rest-Stop Metropolis.

### Tier IV — Sovereign Network

**Fantasy:** The Home Median becomes the protected heart of a connected corridor community.  
**Range:** a chain reaching the Rest-Stop Metropolis and other distant sites.  
**Capabilities:** resilient dead-zone sanctuary spaces, mature outpost routes, trade and intelligence networks, final Guest capacity, major civic works, grand caravan preparation.  
**Pressures:** completing the route, protecting legacy, deciding what the colony will become.

Tier IV does not electrify the animal settlement or turn it into a tiny human empire. Mastery means ecological invisibility, resilient routes, social connection, and intelligent use of overlooked infrastructure.

### 12.1 Advancement gates

Tier advancement should combine:

- A civic construction milestone at the Home Median.
- Sustained food and shelter capacity.
- A small amount of flexible and rigid scrap.
- A demonstrated expedition or network achievement.
- At selected tiers, a believable special artifact, relationship, or knowledge requirement.

Avoid arbitrary giant resource sacrifices. Advancement must visibly transform the colony and unlock a new kind of decision.

---

## 13. Rest-Stop Metropolis

The **Rest-Stop Metropolis** is a distant, revisit-able multi-species settlement hidden within the neglected ecological and structural margins of a human rest stop. It provides world-building, mythology, character encounters, trade, specialist services, and selected progression opportunities.

It should feel extraordinary but plausible: not a fantasy capital sitting openly beside human foot traffic, but an urban animal ecosystem distributed among drainage spaces, service voids, dumpster enclosures, embankments, roof edges, vents, and vegetation set back from the main buildings.

### 13.1 Core functions

- **Multi-species gathering place:** rumors, relationships, recruitable Guests, returning characters, and social story.
- **Trade:** exchange local abundance and rare artifacts for unfamiliar resources or services.
- **Craft and adaptation:** commission specialized tools and accessibility aids beyond the Home workshop’s knowledge.
- **Culture and mythology:** hear corridor legends, ecological memory, warnings, and competing interpretations of the human world.
- **Intelligence:** learn about Road Work, routes, biomes, rare opportunities, or political tensions.

### 13.2 Campaign role

The Metropolis belongs in the core campaign because the victory arc involves connecting the Home Median to the wider world. It must not overshadow the base-builder or become the player’s new primary town.

### 13.3 Victory and continuation

A campaign’s climactic objective is to establish a viable network of outposts and relationships to the Metropolis, then complete a **Grand Caravan** or equivalent final expedition that proves the corridor connection can endure.

Victory is an offered conclusion, not forced retirement. After the climax, the player may:

- Conclude and view a colony legacy chronicle.
- Continue indefinitely in the same world.

Post-victory play focuses on civic beautification, relationships, rare expeditions, long-term ecological events, veteran care, outpost refinement, trade, and the stories of later generations—not infinite vertical power scaling.

---

## 14. Interface and information design

### 14.1 Colony view

The default view prioritizes the settlement as a living miniature ecosystem. Work routes, storage, structural problems, fear, injury, weather, and congestion should be visually apparent.

### 14.2 Blueprint / ledger overlay

A toggle or hold input adds precise information for known systems:

- Resource totals, consumption, capacity, and expected reserve duration.
- Building function, durability state, repair need, and construction cost.
- Work assignment and route congestion.
- Healing, nursery, and scheduled event progress.
- Outpost status and known network flow.

It should not reveal hidden citizen ratings, unknown encounters, exact contest probabilities, or future RNG.

### 14.3 Citizen dossiers

Dossiers combine portrait, descriptive aptitude bands, current condition, relationships, assigned role, and a concise chronological history. The player can understand why a citizen is suitable without seeing raw hidden attributes.

### 14.4 Expedition launch screen

The launch screen is character-centered. It shows the chosen destination and purpose, then a small set of candidate citizens as portrait cards with qualitative readiness, relevant history, condition, relationship dynamics, and mission constraints.

Avoid a wall of stats. The question should feel like “Who do I trust with this?” rather than “Which array has the largest number?”

### 14.5 Controls and accessibility

The control target is PC/console with controller-first readability at television and handheld distance. Required considerations include:

- Scalable text and UI.
- Full remapping.
- Pause and time scaling.
- Color-independent signals.
- Directional audio visualization.
- Reduced input-speed crossing option.
- Strategic/assisted crossing alternative if feasible.
- Motion, flash, and camera-shake controls.
- Clear animal silhouettes and condition icons.

---

## 15. Art and audio direction

### 15.1 Visual identity

Grounded stylized realism at animal scale. The world combines soft organic material—fur, grass, roots, mud, bark, feathers—with harsh human infrastructure—wet asphalt, concrete, salt, rust, tire rubber, reflective signs, plastic, drainage metal.

The tone is atmospheric and tactile, not relentlessly grim. Home scenes may be warm, lively, and gently storybook-like. Expedition scenes become colder, larger, and more cinematic. Avoid cute anthropomorphic clothing as a default, sci-fi interfaces, neon technology, and brushed-metal title treatments that make the animal world feel manufactured.

### 15.2 Scale language

Scale should be communicated through recognizable infrastructure and material texture: lane paint, tire fragments, guardrail bolts, culvert mouths, drainage grates, barrier seams, and distant vehicle mass. Human bodies are unnecessary and often tonally wrong. Cars should not intrude impossibly close to safe colony compositions.

### 15.3 Audio

Audio is systemic:

- Traffic density and vehicle approach must be learnable by sound.
- Large vehicles produce low-frequency vibration and wind pressure.
- Night crossings use directional audio without becoming inaccessible.
- Home has species-specific movement, construction, conversation, weather shelter, and domestic rhythms.
- Tharn is communicated through narrowed sound, breath, pulse, and overwhelming threat—not only a UI icon.
- Adaptive devices and lasting injuries may alter movement sound respectfully and consistently.

---

## 16. Optional generative visual layer

This is a **game-designer-optional modular add-on**, not a dependency of the core game and not necessarily a player-facing option in the first design pass. The base game must be complete, coherent, and emotionally effective without it.

Potential functions:

### 16.1 Evolving canonical portraits

Each citizen has a canonical image and structured textual description. A permanent visible change updates the record with factual deltas and, through image-to-image generation, creates a revised canonical portrait. Continuity of identity, species anatomy, side/orientation, and existing scars is essential.

### 16.2 Expedition splash images

Selected high-value moments—first contest, rare encounter, Guest recruitment, major victory, catastrophic Road Work—can produce a cinematic loading-screen-style image using the actual participants, conditions, and location. The image celebrates a mechanically meaningful event; it does not substitute for gameplay.

### 16.3 Settlement milestone images

At tier advancement or civic milestones, the system interprets the actual Home Median layout and produces a ground-level storybook view of the player’s settlement.

### 16.4 Player ownership and fallback

Generated images become available to the player as exportable PNGs or a campaign scrapbook. Every trigger requires a non-generative fallback using standard art, text, and recorded game state. Cost, latency, moderation, privacy, API authentication, service continuity, reproducibility, and save-file portability must be evaluated separately.

---

## 17. Campaign onboarding

The tutorial should teach emotional priorities before revealing the full system.

1. **Find sanctuary:** Begin with a tiny species-specific founding group in a damaged but promising Home Median.
2. **Feed the group:** Gather obvious nearby sustenance and watch it move physically into storage.
3. **Build the first civic structure:** Establish shelter or a communal center and introduce colony view.
4. **Recognize a progression need:** A repair or construction problem requires material not available safely at home.
5. **Stage the first crossing:** Read traffic, select citizens, and make the Home-to-Margin run.
6. **Face the world:** Resolve an early physical contest that can wound and frighten without scripting an unavoidable permanent mutilation.
7. **Meet an outsider:** Weight the second or third expedition toward a Guest encounter, establishing social possibility.
8. **See the corridor:** Reveal the longitudinal median chain and the first scout target.

The founding setup must match the selected core species; the game does not always begin with a lone mouse.

---

## 18. Scope and roadmap

### 18.1 Vertical-slice priorities

A persuasive prototype should prove:

1. One species—preferably rabbits or mice—can build a visually readable small colony in one Home Median.
2. Named citizens create attachment through work, fear, wounds, history, and relationships.
3. The outbound highway crossing is tense, fair, and replayable.
4. One Margin supports renewable sustenance/scrap extraction and Road Work reset.
5. One contested encounter supports at least conflict, retreat, and negotiation.
6. Expedition consequences visibly return to the colony.

Do not prototype the Metropolis, full season cycle, every Guest, all three species, or generative imagery before this loop works.

### 18.2 V1 target

- Three core species using one shared system architecture.
- Four advancement tiers.
- Several Home Median seeds and a modest chain of distinct remote biomes.
- Margin Raids, Scouts, Outposts, Outpost Visits, and special journeys.
- Traffic, Highway Weather, seasons, and Road Work.
- Low-population citizen life cycle, fear, wounds, maiming, adaptation, death, and memorials.
- A curated Guest roster across Catalyst and Ambient roles.
- Rest-Stop Metropolis and a final connection/caravan arc.
- Endless continuation after victory.
- Strong non-generative presentation throughout.

### 18.3 Later expansion candidates

- More biomes, Rest Stops, Guests, event chains, and infrastructure types.
- A playable Metropolis-focused campaign with different constraints.
- Rival organized civilizations only if localized encounter and diplomacy systems prove insufficient. Do not add fully simulated distant AI colony economies by default.
- Optional generative portrait, expedition, and settlement imagery after the base game is stable.

---

## 19. Canonical decisions and explicit exclusions

The following supersede contradictory brainstorming in the source thread:

- The game is a **base builder first**, with expedition action as its paired risk system.
- The Home Median remains permanent; expansion uses outposts and a corridor network rather than migration.
- The geography is **Sound Wall / Margin / Highway / Median / Highway / Margin / Sound Wall**.
- The colony lives in the Median.
- “Margin” replaces “Shoulder Strip” as the preferred outer foraging-zone term.
- Nearby sustenance supports survival; expeditions are required for progression.
- Contest is hidden until arrival.
- Expedition risk and citizen core attributes are not shown as exact percentages.
- Known colony economics and construction state do have clear numerical ledger support.
- One expedition per citizen per day is canonical; a routine two-expedition day is not.
- Mouse gameplay retains named individuals and low population; no anonymous sacrificial swarm.
- Wounds heal; maiming persists but does not erase a citizen’s value.
- Tharn is a central fear state.
- Guest categories are **Catalyst** and **Ambient**.
- A Guest opportunity is strongly weighted into the second or third early expedition, after an initial physical confrontation.
- Rest-Stop Metropolis is part of V1 and supports the campaign climax, but is not the player’s replacement home.
- Victory can transition into endless play.
- Tier III does not name-check or require the Metropolis.
- Electricity is not the endpoint of progression.
- Optional LLM imagery is modular and nonessential.
- Full distant rival-civilization simulation is dropped from the core plan; localized contested factions remain.

---

## 20. Open design questions

These require prototype evidence or an explicit creative decision:

1. **Crossing embodiment:** real-time direct control, tactical commands with time dilation, or a selectable hybrid?
2. **Day duration:** what real-time length supports meaningful construction without making one expedition feel trivial or exhausting?
3. **Night departures:** rare special option, dedicated mission type, or unlocked strategic alternative?
4. **Population targets:** starting, mid-game, and mature ranges for each species.
5. **Species balance:** how different can spatial systems become before content production triples?
6. **Outpost representation:** visitable micro-map, compact diorama, or layered node with occasional active missions?
7. **Contest resolution:** how much direct tactical control occurs after an encounter reveal?
8. **Return probabilities:** validate the proposed clean/incident/manual proportions through pacing tests.
9. **Breeding abstraction:** life stages, time scale, heredity, and relationship requirements.
10. **Predator logic:** persistent individuals, systemic threat populations, or encounter-only presentation?
11. **Rest-Stop distance:** fixed campaign anchor or procedurally placed within a bounded range?
12. **Victory requirement:** exact caravan objective, civic prerequisites, and whether alternate endings exist.
13. **Canonical Guest roster:** recover and reconcile the active species list from v0.1 before naming it final.
14. **Resource granularity:** whether certain flavorful finds should remain mechanically distinct without undermining the three-resource economy.
15. **Road Work fairness:** forecasting, player counterplay, and acceptable damage ceilings.
16. **Generative layer feasibility:** service model, cost, latency, privacy, consistency, and offline fallback.

---

## 21. Prototype success criteria

The concept is working when players:

- Refer to citizens by name without prompting.
- Spend time improving the Home Median even when a purely optimal layout is available.
- Understand colony problems by looking, then use the ledger to confirm rather than discover everything.
- Want to launch expeditions for both progression and character story.
- Experience the outbound crossing as tense but fair.
- Accept wounds and changed plans without immediately reloading every failure.
- Continue valuing a maimed citizen and find a meaningful new or adapted role for them.
- Recognize the Margin, Highway, Median, and longitudinal chain without explanation.
- Feel relief on returning home.
- Choose to keep living in the colony after the formal campaign victory.

---

## 22. One-paragraph canonical summary

MEDIAN is a single-player PC/console animal colony builder set on the green islands between active highways. The player chooses rabbits, squirrels, or wood mice and builds a permanent, low-population Home Median whose named citizens forage, construct, form relationships, suffer fear, heal from wounds, adapt to permanent maiming, and accumulate personal histories. Local ecology can sustain life, but advancement requires expeditions: cross the highway to the renewable, resource-rich Margin or travel longitudinally through a chain of distinct median biomes to scout, establish lightweight outposts, meet contested factions and rare Guest Citizens, and extend the colony’s reach. Traffic behaves like weather; Road Work reshapes the ecosystem; hidden encounter risk preserves suspense while a clear ledger supports strategic colony management. Four progression tiers transform a vulnerable camp into a resilient sovereign network without turning animals into miniature industrial humans. The V1 campaign culminates in a durable connection to a distant Rest-Stop Metropolis and a Grand Caravan, after which the player may conclude the colony’s chronicle or continue indefinitely. Optional AI-generated portraits and milestone images can commemorate the actual citizens and settlement, but the game is designed to stand completely without them.
