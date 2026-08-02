<!--@1-->
# MEDIAN v0.4.6 → v0.5 v0.4.7 Development Survivorship Review

<!--@1¶1-->
**Audit purpose:** Identify significant v0.4.6 GDD content that is not already dispositioned by the ten controlling v0.5 specification documents before the v0.5 architecture is frozen.

<!--@1¶2-->
**Historical comparison named by the model-authored document:** v0.4.6 GDD  
**Controlling v0.5 corpus:** Philosophical; Home Mode, Colony, and DWELL Specification; Embodiment Register v2.0; Ecological Influences v1.0; Manifestations; Market Position v1.1; Away Mode v1.0; v0.4.7 Cross-System Carryforward v1.0; Population, Growth & Colony Tiers v1.0; Guest Citizens v2.0.

<!--@1.1-->
## Executive verdict

<!--@1.1¶1-->
The audit does **not** reveal a missing core identity or a missing primary loop. The v0.5 corpus comprehensively covers the architectural redesign of Home, Away, the five Registers, MEET, EMBODY, species spatial identity, population and Tiers, and Guest Citizens.

<!--@1.1¶2-->
It does reveal a set of important **supporting canon domains that the v0.5 specifications frequently assume but do not fully re-rule**. These are concentrated in six clusters:

<!--@1.1¶3-->
1. culture, folklore, names, Records, and Campaign Memory;
2. corridor geography, biomes, and Anchor Points;
3. day structure, traffic ecology, seasons, and Road Work;
4. resources, carrying, Artifacts, and personal equipment;
5. construction/Projects, Place families, and diegetic civic interfaces;
6. corridor progression, the Metropolis, and the campaign climax.

<!--@1.1¶4-->
Most of these do not require another conceptual reinvention. They require an explicit **retain / revise / supersede / defer ledger** so that silence is not mistaken either for deletion or for automatic inheritance.

<!--@1.1¶5-->
A seventh cluster—interface, art/audio, accessibility, and tutorialization—is significant but should mostly be routed into later presentation and implementation passes rather than allowed to delay the conceptual architecture lock.

<!--@1.1¶6-->
---

<!--@2-->
# Status key

<!--@2¶1-->
- **CLOSED** — A controlling v0.5 specification clearly covers or supersedes the baseline material.
- **DECISION REQUIRED** — Significant baseline material remains only partially covered, assumed, or internally contradicted.
- **CARRY-FORWARD REVIEW** — The material appears compatible and valuable, but its placement and authority should be confirmed.
- **DEFER** — Important implementation, production, or presentation work, but not a blocker for conceptual architecture.

<!--@2¶2-->
---

<!--@3-->
# I. Findings requiring explicit pre-lock disposition

<!--@3.1-->
## A. Culture, folklore, names, Records, and Campaign Memory

<!--@3.1.1-->
### Baseline sources

<!--@3.1.1¶1-->
- §6 — Laws of the Median, Sayings, and vocabulary for the human world
- §17 — Citizen Record
- §22 — Colony Record, Citizen Record, Almanac, Chronicle, Likeness, Tale, Rating, Report and Share
- §23 — Given Names, After-names, folk place-name grammar, and the single player-authored colony name
- Appendix B — Folk place-name component banks
- Appendix C — Hyphen-compounds
- Appendix D — Descriptive bands

<!--@3.1.2-->
### What v0.5 covers

<!--@3.1.2¶1-->
The v0.5 corpus repeatedly invokes Campaign Memory, Tales, Keepsakes, Distinctions, After-names, memorial continuity, and the Chronicle. It also explicitly abolishes the generic Expedition Rating.

<!--@3.1.3-->
### What remains unresolved

<!--@3.1.3¶1-->
The v0.4.7 Cross-System Carryforward specification expressly leaves open:

<!--@3.1.3¶2-->
- the formal scope of Distinctions, After-names, Keepsakes, fear memories, Tales, and memorial records;
- what replaces summary Ratings as the Chronicle’s compact expedition account;
- how EMBODY retrieves or leaves prior events.

<!--@3.1.3¶3-->
The following v0.4.6 rules are not comprehensively revalidated:

<!--@3.1.3¶4-->
- Laws as functional tutorialization and Sayings as non-instructional folklore;
- the Giants / Roaring Iron / Rivers of Thunder vocabulary;
- the Teacher’s role in transmitting folklore;
- the exact Almanac / Chronicle and Likeness / Tale architecture;
- Keepsake provenance and inheritance;
- first-Distinction After-name assignment;
- one player-authored name, curated choice, no free text, no renaming;
- generated Reach and Place names derived from physical character and later history;
- descriptive aptitude bands.

<!--@3.1.4-->
### Required ruling

<!--@3.1.4¶1-->
Create one **Culture and Memory carry-forward decision packet**. Do not merely paste §6, §22, and §23 forward, because several of their mechanical anchors have changed.

<!--@3.1.4¶2-->
At minimum decide:

<!--@3.1.4¶3-->
1. whether Laws remain a functional teaching layer;
2. which Laws survive after the v0.5 redesign and which require rewriting;
3. whether Sayings remain a distinct additive inventory;
4. whether the human-world vocabulary remains canonical;
5. the authoritative Citizen and Colony Record schema;
6. the compact post-expedition memory object replacing Rating;
7. Keepsake acquisition, permanence, transfer, and inheritance;
8. the After-name trigger and whether exceptional Home history can grant one;
9. whether the one-name/no-free-text doctrine survives;
10. which name grammars belong in the v0.5 Appendix.

<!--@3.1.4¶4-->
**Assessment:** Architecture blocker, but primarily a confirmation-and-reconciliation pass rather than a new design project.

<!--@3.1.4¶5-->
---

<!--@3.2-->
## B. Corridor geography, biomes, and Anchor Points

<!--@3.2.1-->
### Baseline sources

<!--@3.2.1¶1-->
- §7 — corridor cross-section, Home Median, Highway, Margin, Median Reach, service crossovers, ancestral ruin, Metropolis
- §8 — eight biomes and Anchor Points

<!--@3.2.2-->
### What v0.5 covers

<!--@3.2.2¶1-->
Away Mode establishes TRAVEL, RISK, Nodes, Reaches, route texture, Home Reach traversal, Held Reaches, Stopovers, and the qualitative ancestral-home / Metropolis orientation. Ecological Influences establishes species-relative topology, road-edge gradients, water, drainage, seasons, sound, and human infrastructure as naturalized terrain.

<!--@3.2.3-->
### What remains unresolved

<!--@3.2.3¶1-->
The corpus does not comprehensively re-rule:

<!--@3.2.3¶2-->
- the exact cross-section: Sound Wall → Margin → Highway → Home Median → Highway → Margin → Sound Wall;
- Sound Walls as permanent playable boundaries;
- the distinction between the Home Median’s generated place name and the colony’s player-selected name;
- service crossovers as Reach boundaries;
- the road-edge / wall-edge dual character of each Margin;
- Margin renewability and permanent non-buildability;
- whether Reaches remain whole-biome units without internal subdivisions;
- the exact eight-biome roster;
- lane count remaining independent of biome richness;
- Anchor Points as a fixed mixed bonus layer rather than gates;
- the first Home Reach’s guaranteed species suitability.

<!--@3.2.3¶3-->
The Ecology specification uses “anchors” in the squirrel-topology sense, but does not clearly re-establish the v0.4.6 procedural Anchor Point system or the eight named biomes.

<!--@3.2.4-->
### Required ruling

<!--@3.2.4¶1-->
Create one **World and Corridor canon packet** that lists every v0.4.6 geography proposition and assigns:

<!--@3.2.4¶2-->
- retain unchanged;
- retain with new terminology;
- revise for v0.5;
- move to content authoring;
- or retire.

<!--@3.2.4¶3-->
The eight biomes should be audited after the v0.5 economy decision, because several baseline biome identities are expressed through now-uncertain resource categories such as Rigid Scrap.

<!--@3.2.4¶4-->
**Assessment:** Architecture blocker. This determines the map ontology to which Away Mode, species topology, corridor progression, and eventual Sourcebook art all attach.

<!--@3.2.4¶5-->
---

<!--@3.3-->
## C. Day structure, traffic ecology, seasons, and Road Work

<!--@3.3.1-->
### Baseline sources

<!--@3.3.1¶1-->
- §9 — daily beats, traffic cycles, traffic-as-weather, Wind Draft, River’s Spume, Litter
- §10 — Choice-Event Cards
- §11 — seasons and Road Work

<!--@3.3.2-->
### What v0.5 covers

<!--@3.3.2¶1-->
- Home replaces the old Dawn resolution with a formal Dawn adjudication.
- v0.4.7 Cross-System Carryforward establishes Choice Events, shared world state, and Telegraph → Impact → Persistence → Aftermath.
- Away establishes sparse Field Cards and makes traffic readable during RISK.
- Ecology establishes road noise, seasonal transformation, predators, drainage, and resource gradients.

<!--@3.3.3-->
### What is already closed

<!--@3.3.3¶1-->
The old “unified event card layer” is not an untouched gap. v0.4.7 Cross-System Carryforward and Away have already restructured it:

<!--@3.3.3¶2-->
- Choice Events are authored state-changing packets;
- generic event-deck texture is rejected;
- Field Cards stay sparse;
- Road Work Impact does not necessarily open a full choice strip.

<!--@3.3.4-->
### What remains unresolved

<!--@3.3.4¶1-->
- whether Morning Rush / Midday / Evening Rush / Night Velocity remain the game-day cadence;
- whether one expedition per citizen per day remains canonical under multi-day Away journeys;
- the traffic-cycle taxonomy and Anomaly state;
- Wind Draft, the River’s Spume, and its six seasonal/traffic manifestations;
- the specific road-edge intensity model;
- exact seasonal identities beyond the Home seasonal rhythm;
- Road Work cadence, local strike versus corridor-wide disruption, Margin wipe, Anchor interaction, bounded persistence, and recovery;
- how Road Work and other environmental pressure connect to the new Home Deficiency/MEET architecture without becoming a parallel event system.

<!--@3.3.5-->
### Required ruling

<!--@3.3.5¶1-->
Create one **Temporal and Environmental Pressure packet**. It should distinguish:

<!--@3.3.5¶2-->
- system architecture that must be in the GDD;
- content families that can remain authoring canon;
- named environmental flavor that can be carried forward;
- and tuning values that remain provisional.

<!--@3.3.5¶3-->
**Assessment:** Architecture blocker. The new Home and Away systems now have clearer event grammars, but the world-pressure generator feeding those grammars is not fully specified.

<!--@3.3.5¶4-->
---

<!--@3.4-->
## D. Resources, carrying, Artifacts, and equipment

<!--@3.4.1-->
### Baseline sources

<!--@3.4.1¶1-->
- §14 — Sustenance, Perishable/Durable split, Flexible Scrap, Rigid Scrap, weight ladder, Colony and Carried Artifacts
- §20 — Keepsake, Tool, and Supply

<!--@3.4.2-->
### What v0.5 covers

<!--@3.4.2¶1-->
Home now names:

<!--@3.4.2¶2-->
- Perishable Sustenance;
- Durable Sustenance;
- Flexible Scrap;
- Supply Items;
- Medical Stores.

<!--@3.4.2¶3-->
Away retains:

<!--@3.4.2¶4-->
- public party-scale carrying;
- standing Tools as Colony assignments;
- at most one deliberate Supply choice per departing Citizen;
- salvage, equipment, and Artifacts as possible returns.

<!--@3.4.2¶5-->
Manifestations continues to assume Tool / Keepsake / Supply as a meaningful cross-medium distinction.

<!--@3.4.3-->
### What remains unresolved

<!--@3.4.3¶1-->
This is the clearest mechanical survivorship gap.

<!--@3.4.3¶2-->
The new Home resource table does not include Rigid Scrap, while the baseline construction/material system depends heavily upon the Flexible/Rigid distinction. No controlling specification explicitly says whether Rigid Scrap was intentionally removed, folded into Flexible Scrap, renamed, or simply omitted.

<!--@3.4.3¶3-->
Also not fully re-ruled:

<!--@3.4.3¶4-->
- the weight ladder and cooperative carrying thresholds;
- whether carry values still use the same shared public scale;
- Colony Artifact versus Carried Artifact;
- Carried Artifacts occupying the Tool slot;
- Keepsake permanence and inheritance;
- Tool assignment and reassignment;
- Supply consumption and encounter use;
- crafting boundaries;
- adaptive equipment’s exact relation to slots;
- the anti-weapon terminology and mechanics.

<!--@3.4.4-->
### Required ruling

<!--@3.4.4¶1-->
Create one **Material Economy and Personal Equipment specification or compact decision packet**.

<!--@3.4.4¶2-->
This one should be more formal than a simple carry-forward ledger because resource categories, construction costs, carrying, crafting, expedition preparation, Homecoming, and Citizen Records all depend on it.

<!--@3.4.4¶3-->
**Assessment:** Strong architecture blocker and the most clearly missing mechanical module.

<!--@3.4.4¶4-->
---

<!--@3.5-->
## E. Projects, construction, Places, and civic interfaces

<!--@3.5.1-->
### Baseline sources

<!--@3.5.1¶1-->
- §15 — decay, maintenance, Construction Queue
- §16 — structure families, upgrade ladders, functional icons, Community Board, Story Circle
- Appendix A — upgrade-name ladders

<!--@3.5.2-->
### What v0.5 covers

<!--@3.5.2¶1-->
Home clearly reframes construction as named Projects measured in Citizen-Days. It retains a queue only as an implementation concept and rejects player-facing slot/progress-bar logic. Population removes Construction Queue slots as a principal Tier reward.

<!--@3.5.3-->
### What remains unresolved

<!--@3.5.3¶1-->
The following baseline details have no complete v0.5 disposition:

<!--@3.5.3¶2-->
- broad durability states and event-based wear;
- whether resources are committed at Project start;
- refunds and cancellation;
- interruptibility;
- whether a Place is offline while transformed;
- speed-up prohibition;
- how many simultaneous Projects civic Margin can support;
- the canonical Place/structure family roster;
- whether named internal upgrade ladders survive;
- the relationship between Tier and Place-family/rung access;
- persistent functional icons;
- Community Board as operational information object;
- Story Circle as ceremonial and memory-bearing Place;
- Welcome sign and other former “building families.”

<!--@3.5.3¶3-->
Several old families are already incompatible:

<!--@3.5.3¶4-->
- Staging Posts are now improvised edge ground, not buildable structures;
- Guest Houses are independently redesigned;
- Nursery and population structures are redefined;
- outposts no longer use the old satellite-building model.

<!--@3.5.4-->
### Required ruling

<!--@3.5.4¶1-->
Create one **Place and Project reconciliation ledger** keyed to every §15–16 family and rule.

<!--@3.5.4¶2-->
This does not require another Home redesign. It requires translating the inherited catalogue into the new ontology:

<!--@3.5.4¶3-->
- Place;
- Practice;
- Project;
- Residence;
- species spatial grammar;
- contextual Load;
- and Campaign Memory.

<!--@3.5.4¶4-->
**Assessment:** Architecture blocker because the final TOC and Home chapter structure depend on what the built environment actually contains.

<!--@3.5.4¶5-->
---

<!--@3.6-->
## F. Corridor progression, outposts, the Metropolis, and campaign climax

<!--@3.6.1-->
### Baseline sources

<!--@3.6.1¶1-->
- §29 — Unknown / Walked / Held Reaches, outpost buildings, stationed Citizens, passive yield
- §30 — Rest-Stop Metropolis
- §31 — campaign role, victory, continuation
- parts of §7, §28, and §32

<!--@3.6.2-->
### What v0.5 covers

<!--@3.6.2¶1-->
Outpost identity is substantially re-ruled:

<!--@3.6.2¶2-->
- Held Reaches remain Away;
- Stopovers provide refuge, Rest, Care, Watch, and Store functions;
- outposts are not second Colonies;
- passive resource engines and portable Home Mode are rejected.

<!--@3.6.2¶3-->
The qualitative campaign orientation survives:

<!--@3.6.2¶4-->
- one direction leads toward the ancestral ruin and the past;
- the other leads toward the Rest-Stop Metropolis and a civic future.

<!--@3.6.3-->
### What remains unresolved

<!--@3.6.3¶1-->
v0.4.7 Cross-System Carryforward explicitly leaves corridor and frontier progression open:

<!--@3.6.3¶2-->
- multi-day focus switching;
- Reaches per day;
- outpost-chain length;
- ancestral-home and Metropolis journey pacing;
- direction names and cultural meaning;
- mature Squirrel-network effects.

<!--@3.6.3¶3-->
The controlling corpus also does not fully re-rule the Metropolis itself:

<!--@3.6.3¶4-->
- whether it remains the only city;
- whether it remains a Field territory with venues as Nodes;
- trade, specialized craft, intelligence, and culture functions;
- the raccoon founding heritage;
- contradictory Laws;
- its relationship to Guest recruitment;
- whether the Grand Caravan remains the campaign climax;
- whether corridor connection remains the victory condition;
- post-victory continuation.

<!--@3.6.3¶5-->
Population confirms Tier IV as Sovereign Network, but that does not by itself confirm the complete Metropolis arc.

<!--@3.6.4-->
### Required ruling

<!--@3.6.4¶1-->
Create one **Corridor Progression and Metropolis packet**.

<!--@3.6.4¶2-->
First settle the campaign macro-structure. Then distinguish:

<!--@3.6.4¶3-->
- core architectural facts;
- content to be authored later;
- provisional pacing values;
- and Sourcebook/worldbuilding details.

<!--@3.6.4¶4-->
**Assessment:** Architecture blocker. The GDD architecture cannot confidently order progression, Reaches, Stopovers, Metropolis, and victory chapters until this is settled.

<!--@3.6.4¶5-->
---

<!--@4-->
# II. Significant material that should not block conceptual architecture

<!--@4.1-->
## G. Interface, art/audio, accessibility, and onboarding

<!--@4.1.1-->
### Baseline sources

<!--@4.1.1¶1-->
- §33 — interface and information design
- §34 — art and sound
- §35 — Founding Escape and tutorial
- Appendices E–H

<!--@4.1.2-->
### Current status

<!--@4.1.2¶1-->
The v0.5 corpus establishes many higher-level presentation laws:

<!--@4.1.2¶2-->
- numerical restraint;
- native information versus MEET;
- one shared world state;
- species-relative spatial legibility;
- no visual invention establishing canon;
- road-forward market identity;
- register translation across manifestations.

<!--@4.1.2¶3-->
However, it does not comprehensively revalidate:

<!--@4.1.2¶4-->
- the old three-hotspot Colony UI;
- Community Board / Story Circle / species hub navigation;
- every accessibility requirement;
- the no-visible-human rule;
- cloth and scavenged-material culture;
- exact prohibitions on armor, harnesses, livery, and forged objects;
- traffic and tharn audio language;
- the old tutorial order.

<!--@4.1.3-->
### Recommended handling

<!--@4.1.3¶1-->
Do not hold the conceptual architecture open while redesigning the tutorial, final UI, or complete art/audio bible.

<!--@4.1.3¶2-->
Instead:

<!--@4.1.3¶3-->
1. create a **presentation carry-forward ledger**;
2. preserve compatible hard constraints;
3. mark anything dependent on unresolved system canon;
4. rewrite onboarding only after the architecture and systems are frozen;
5. route Sourcebook-specific imagery and narrative manifestation out of the GDD process.

<!--@4.1.3¶4-->
The Founding Escape may remain canonical as campaign premise, but the v0.4.6 tutorial sequence is no longer directly executable because Home, Staging Posts, Guests, MEET, progression, and Records have changed.

<!--@4.1.3¶5-->
**Assessment:** Significant, but generally post-lock work.

<!--@4.1.3¶6-->
---

<!--@5-->
# III. Section-by-section survivorship ledger

<!--@5¶1-->
| v0.4.6 section | Status | Audit result |
|---|---|---|
| 1. Creative thesis | CLOSED | Reframed and strengthened by Philosophical and Market Position. |
| 2. Design pillars | CLOSED | Attachment-first stewardship and restraint are central to v0.5. |
| 3. Four registers | CLOSED | Explicitly superseded by five Registers including EMBODY. |
| 4. Three species | CLOSED | Rebuilt through Ecology, Home, Away, Population, and spatial grammar. |
| 5. Two loops | CLOSED | Home/Away split and complete cycle are now stronger and explicit. |
| 6. One folklore | DECISION REQUIRED | Laws, Sayings, vocabulary, and tutorial function are not comprehensively re-ruled. |
| 7. World geography and terminology | DECISION REQUIRED | Core terms survive by use, but the full corridor ontology lacks a v0.5 ledger. |
| 8. Biomes and Anchor Points | DECISION REQUIRED | Eight-biome roster and procedural Anchor Points are not clearly re-established. |
| 9. Day, traffic, and traffic as weather | DECISION REQUIRED | Traffic and Dawn survive in pieces; the complete temporal/environment model does not. |
| 10. Choice-Event Cards | CLOSED / REFRAMED | v0.4.7 Cross-System Carryforward Choice Events and Away Field Cards replace the old unified card formulation. |
| 11. Seasons and Road Work | DECISION REQUIRED | Event-phase grammar is covered; exact system content and cadence are not. |
| 12. Scale and colony shape | CLOSED | Population specification leads. |
| 13. Roles and daily work | CLOSED | Home specification leads; final Role roster is already explicitly preserved as an open question. |
| 14. Resources and economy | DECISION REQUIRED | Resource taxonomy now conflicts or has omissions, especially Rigid Scrap. |
| 15. Construction, decay, Queue | DECISION REQUIRED | Queue is reframed as Projects, but operational Project/decay rules need disposition. |
| 16. Structures and ladders | DECISION REQUIRED | Must be translated into Places/Practices/Projects; several families are obsolete. |
| 17. Citizen Record | DECISION REQUIRED | Formal schema remains an explicit v0.5 open question. |
| 18. Bonds, Hearths, growth | CLOSED | Population, Guest, Home, and Embodiment cover the architecture. |
| 19. Harm, fear, tharn | CLOSED | Away and Embodiment lead. |
| 20. Equipment | DECISION REQUIRED | Tool/Supply assumptions survive, but the complete three-slot system is not formally re-established. |
| 21. Guest Citizens | CLOSED | Guest v2.0 is authoritative and includes the species roster. |
| 22. Records | DECISION REQUIRED | Rating is superseded; its replacement and full Record architecture remain open. |
| 23. Names | DECISION REQUIRED | Naming concepts are referenced but not comprehensively revalidated. |
| 24. Crossing | CLOSED | Away RISK leads. |
| 25. Field Mode | CLOSED | Away TRAVEL and Node doctrine lead. |
| 26. Encounters | CLOSED | Home MEET, Away MEET, and v0.4.7 Cross-System Carryforward jointly replace the old model. |
| 27. Contest, recruitment, Base Defense | CLOSED | Guest recruitment and Home-origin MEET replace the old funnel/combat framing. |
| 28. Expeditions and Launcher | CLOSED | Away Launch/Homecoming architecture leads. |
| 29. Outposts | DECISION REQUIRED | Old satellite model is superseded; corridor progression and Stopover scope remain open. |
| 30. Metropolis | DECISION REQUIRED | Still referenced as destination, but not formally re-specified. |
| 31. Metropolis in campaign | DECISION REQUIRED | Victory, Grand Caravan, and continuation require confirmation. |
| 32. Progression Tiers | CLOSED | Population and Tiers specification leads and explicitly supersedes old rewards. |
| 33. Interface | CARRY-FORWARD REVIEW | Distributed v0.5 requirements exist; detailed UI should follow architecture lock. |
| 34. Art and sound | CARRY-FORWARD REVIEW | Ecology and market identity cover principles; retain compatible hard constraints separately. |
| 35. Campaign onboarding | DEFER | Founding premise may survive; tutorial sequence must be rewritten after systems freeze. |
| 36. Suggested scope and roadmap | DEFER | Production recommendation, not architecture canon. |
| 37. Prototype criteria | DEFER | Update after v0.5 is compiled. |
| 38. Canonical summary | CLOSED / SUPERSEDED | Replace with v0.5 thesis and final summary. |

<!--@5¶2-->
---

<!--@6-->
# IV. Explicitly closed changes that should not be reopened in this audit

<!--@6¶1-->
The audit found clear v0.5 dispositions for the following major baseline assumptions:

<!--@6¶2-->
- four-Register ceiling → five Registers including EMBODY;
- generic expedition Rating → removed;
- buildable Staging Post → improvised, impermanent crossing ground;
- Held Reach as partial Home → rejected;
- outpost as passive resource engine or second Colony → rejected;
- automatic Tier-wide Citizen stat bump → removed;
- automatic Guest slots by Tier → removed;
- Construction Queue slots as Tier reward → removed;
- Nursery as population-production building → replaced;
- Nursery Tender as fixed Role → superseded;
- old Active/Ambient Guest system → fully replaced by Guest v2.0;
- old random amenability and Guest-slot recruitment funnel → replaced;
- Home individual productivity coefficients → rejected;
- old Role-output model → replaced by equal Capacity, contextual Load, and Practices;
- generic event deck as normal domestic texture → rejected;
- Road Work Impact as ordinary full choice strip → superseded.

<!--@6¶3-->
These should appear in the eventual migration ledger, but they do not need another design debate unless a new contradiction is discovered.

<!--@6¶4-->
---

<!--@7-->
# V. Recommended final operation before architecture lock

<!--@7¶1-->
Do **not** create six more 40-page specifications by default.

<!--@7¶2-->
Run one bounded final decisions operation with six chapters:

<!--@7¶3-->
1. **Culture and Memory**
2. **World and Corridor**
3. **Temporal and Environmental Pressure**
4. **Material Economy and Equipment**
5. **Places and Projects**
6. **Corridor Progression and Metropolis**

<!--@7¶4-->
For every proposition, choose only:

<!--@7¶5-->
- **RETAIN** — valid without substantive change;
- **REVISE** — concept survives, v0.5 wording/mechanics required;
- **SUPERSEDE** — incompatible with controlling v0.5 canon;
- **DEFER** — implementation, tuning, Sourcebook, or content-authoring work;
- **OPEN** — genuine decision still required.

<!--@7¶6-->
The output should be a compact `MEDIAN_v0.5_Final_Baseline_Disposition.md`, not another persuasive design essay.

<!--@7.1-->
## Lock condition

<!--@7.1¶1-->
The v0.5 architecture is ready to freeze when:

<!--@7.1¶2-->
- every item in the six packets has a disposition;
- the resource/equipment taxonomy is mechanically coherent;
- the Place/Project catalogue is known well enough to structure the Home chapters;
- Record and naming authority is known well enough to structure Citizen/Memory chapters;
- the world ontology is known well enough to structure corridor/biome chapters;
- the Metropolis and victory arc have a settled architectural status;
- unresolved tuning is clearly separated from unresolved design.

<!--@7.1¶3-->
---

<!--@8-->
# VI. Appendix implications

<!--@8¶1-->
The v0.5 Appendix update should follow the six decisions above.

<!--@8¶2-->
Likely Appendix destinations:

<!--@8¶3-->
- building/Place family and rung vocabulary;
- folk place-name component banks;
- hyphen-compound style and glossary;
- descriptive aptitude/condition bands;
- resource and carrying reference;
- Record schemas;
- Tier proof reference;
- Guest species contracts and roster references where appropriate;
- unresolved implementation values clearly marked as tuning.

<!--@8¶4-->
Manifestation-specific material formerly associated with Appendices E–H should be reconciled against the four-form manifestation framework rather than automatically retained as GDD appendices.
