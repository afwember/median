<!--@0¶1-->
MEDIAN v0.5.0

<!--@0¶2-->
GUEST CITIZENS

<!--@0¶3-->
HOSPITALITY, DIFFERENCE, AND QUALITATIVE CIVIC CHANGE

<!--@0¶4-->
<table>
<tbody>
<tr class="odd">
<td><strong>CANONICAL PREMISE<br />
</strong>Core Citizens show what kind of civilization this is. Guest Citizens show whom this particular Colony chose to welcome. Every Guest contributes one equal civic share and one qualitative species signature. The Colony does not erase difference; it changes its own shape to make that difference livable.</td>
</tr>
</tbody>
</table>

<!--@0¶5-->
SYSTEM ARCHITECTURE SPECIFICATION • VERSION 2.0 • 30 JULY 2026

<!--@0¶6-->
Target: MEDIAN v0.5.0 Concept Sourcebook / desktop-console manifestation

<!--@1-->
# 0\. Revision Summary

<!--@1.1-->
## Contents

<!--@1.1¶1-->
1\. Purpose, Source, and Precedence

<!--@1.1¶2-->
2\. Executive Summary and Canonical Premise

<!--@1.1¶3-->
3\. Design Purpose: Kehaar, Difference, and Found Family

<!--@1.1¶4-->
4\. Definitions, Citizen Subjects, and Equal Status

<!--@1.1¶5-->
5\. The Two Guest Types

<!--@1.1¶6-->
6\. Equivalent but Not Equal: The Signature Function

<!--@1.1¶7-->
7\. Population, Growth, Hospitality Capacity, and Colony Tiers

<!--@1.1¶8-->
8\. Guest Citizens in DWELL: Roles, Practices, and Absence

<!--@1.1¶9-->
9\. Guest Houses: Hospitality as Architecture

<!--@1.1¶10-->
10\. Recruitment: From First MEET to Arrival

<!--@1.1¶11-->
11\. Expedition Guests and the Shared Away Framework

<!--@1.1¶12-->
12\. Resident Guests and the Home Affordance Framework

<!--@1.1¶13-->
13\. Collective-Bodied Citizen Households

<!--@1.1¶14-->
14\. Guest Citizens in EMBODY

<!--@1.1¶15-->
15\. Relationships, Records, and Campaign Memory

<!--@1.1¶16-->
16\. Departure, Injury, Death, and Vacant Houses

<!--@1.1¶17-->
17\. Hospitality Capacity, Availability, and Anti-Collection Doctrine

<!--@1.1¶18-->
18\. Detailed Expedition Guest Roster

<!--@1.1¶19-->
19\. Detailed Resident Guest Roster

<!--@1.1¶20-->
20\. Roster Balance and System Coverage

<!--@1.1¶21-->
21\. Carry-Forward and Supersession Ledger

<!--@1.1¶22-->
22\. Authoring Requirements, Open Questions, and Acceptance Tests

<!--@1.1¶23-->
Final System Statement

<!--@1.2-->
## Version 2.0 changes

<!--@1.2¶1-->
  - Integrates the v0.5 Population, Growth & Colony Tiers Specification: Guests count fully toward Roster, Residence, Load, Role Capacity, and neutral Tier proofs.

<!--@1.2¶2-->
  - Finalizes the working roster at seven Expedition species and twelve Resident species, with a detailed mechanical and expressive entry for each.

<!--@1.2¶3-->
  - Adds a sourcebook example Citizen for every species entry. These exemplars demonstrate the content contract and need not all appear in one campaign.

<!--@1.2¶4-->
  - Formalizes the equivalent-but-not-equal doctrine: every Guest species receives one qualitative Signature Permission or Resident Affordance in addition to ordinary civic contribution.

<!--@1.2¶5-->
  - Assigns every Resident species a fixed Guest Practice and Role contribution while deliberately avoiding overconcentration in Watchkeeping and Caretaking.

<!--@1.2¶6-->
  - Defines Firefly Family and Bumblebee Household as the only collective-bodied Citizen exceptions in the v0.5 roster.

<!--@1.2¶7-->
  - Replaces the remaining passive-buff, type-slot, and per-site micromanagement assumptions with situated choices, global Role abstraction, visible Houses, and remembered absence.

<!--@1.3-->
## Major v0.5 rulings

<!--@1.3¶1-->
  - Guest is an origin category, not a lower social rank. Every recruited Guest is named, housed, remembered, and treated as a full Citizen.

<!--@1.3¶2-->
  - The two content types are Expedition Guest and Resident Guest. Type defines where the species Signature is mechanically expressed, not how much the Citizen matters.

<!--@1.3¶3-->
  - Every present and available adult Guest contributes one equal Home Role Capacity. No Guest has a superior productivity coefficient.

<!--@1.3¶4-->
  - Every Guest species also changes the Colony qualitatively through one Signature Permission or Resident Affordance. Equivalent design importance does not require equal frequency, magnitude, or form.

<!--@1.3¶5-->
  - Resident Guest Roles are species-authored and fixed. Their Affordances may operate in a different situation family than the Role contribution.

<!--@1.3¶6-->
  - Firefly Family and Bumblebee Household count as one Citizen subject and one civic share despite being represented by several visible bodies.

<!--@1.3¶7-->
  - Guest Houses pass a double-fit test: the host civilization must still JOIN, GATHER, or CONNECT, while the occupant receives species-credible shelter and access.

<!--@1.3¶8-->
  - Guest recruitment is a relationship-and-hospitality sequence, never a random amenability roll, a perk purchase, or a collectible acquisition funnel.

<!--@1.3¶9-->
  - Resident Guests are mechanically complete. Their stable Home Capacity, Affordance, Place, vulnerability, relationships, Memory, and EMBODY must satisfy base-game logic before attachment is asked to carry the design.

<!--@1.3¶10-->
  - No Tier, victory condition, or essential system requires Guests, a particular species, or collection completion.

<!--@2-->
# 1\. Purpose, Source, and Precedence

<!--@2¶1-->
This specification revises and expands the Guest Citizen architecture for MEDIAN v0.5.0. Version 1.0 established the two-type structure, equal Citizen status, Guest Houses, recruitment through hospitality, shared Away Permissions, Resident Affordances, and universal EMBODY eligibility. Version 2.0 integrates the separate Population and Growth specification and resolves the working species roster in detail.

<!--@2¶2-->
The older Guest material remains useful as imaginative source: rare named outsiders broaden the animal world without requiring every species to support a complete civilization ruleset. Its passive bonuses, separate slot economies, random recruitment assumptions, and generic roster labels are superseded where this document states a v0.5 ruling.

<!--@1.1#2-->
## 1.1 Precedence order

<!--@1.1#2¶1-->
| **Priority** | **Authority**                                        | **Use in this specification**                                                                                      |
| ------------ | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **1**        | v0.5 Philosophical Specification                     | Sanctuary, attachment-first base building, the Home / Away growth split, and the five-Register architecture.       |
| **2**        | v0.5 Home Mode, Colony, and DWELL Specification                                | Roles, equal Capacity, contextual Load, Places, Practices, Projects, Readiness, Quiet Equilibrium, and Home MEET.  |
| **3**        | v0.5 Away Mode Specification                         | Launch, party composition, TRAVEL, RISK, Away MEET, Exposure, Return, Stopover, and Homecoming.                    |
| **4**        | Population, Growth & Colony Tiers Specification v1.0 | Citizen subjects, population counts, growth paths, Hospitality expectations, and neutral Tier proofs.              |
| **5**        | Embodiment Register Specification                    | EMBODY access, Practice / Presence structure, Home-only limits, and bodily expression.                             |
| **6**        | v0.4.7 Cross-System Attention, Persistence, and World-State Carryforward                    | Shared world-state, Register / View doctrine, MEET authoring, persistence, and presentation.                       |
| **7**        | This Guest Citizen Specification v2.0                | Guest types, Signature functions, Houses, recruitment, Resident Roles, collective households, and detailed roster. |
| **8**        | Pre-v0.5 Guest and GDD material                      | Historical rationale, candidate concepts, and names only; superseded where incompatible.                           |

<!--@1.1#2¶2-->
<table>
<tbody>
<tr class="odd">
<td><strong>REVISION MANDATE<br />
</strong>This is a governed revision. No older rule survives merely because it is not individually repeated. Where the Population specification and this document touch, Population leads counting and Tier integration; this document leads species content and Guest-specific expression.</td>
</tr>
</tbody>
</table>

<!--@1.2#2-->
## 1.2 Scope boundary

<!--@1.2#2¶1-->
This document finalizes the v0.5 Guest architecture and working species roster. Exact encounter frequency, resource cost, Load values, animation count, dialogue volume, and numerical balance remain implementation tuning. The example Citizens are sourcebook exemplars; the species contracts remain valid if a campaign uses another named individual.

<!--@3-->
# 2\. Executive Summary and Canonical Premise

<!--@3¶1-->
MEDIAN campaigns are culturally anchored in one Core species: Mouse, Rabbit, or Squirrel. Core Citizens carry the complete civilization grammar - JOIN, GATHER, or CONNECT - and the full population, construction, Home, Crossing, and Away assumptions of the campaign. Guest Citizens are rare named animals from beyond that Core society who may become part of the Colony through relationship and accommodation.

<!--@3¶2-->
The Guest system broadens the animal world while preserving design tractability. Expedition Guests use the shared Away architecture plus one bounded species Permission. Resident Guests remain at Home and use one situated Affordance. Both contribute one equal civic share, occupy real Residence, consume support, form relationships, face danger, produce Campaign Memory, and may be selected for EMBODY.

<!--@3¶3-->
<table>
<tbody>
<tr class="odd">
<td><strong>VERSION THESIS<br />
</strong>A Guest is mechanically credible before the player is asked to love them. Ordinary Role Capacity satisfies the base-game economy; the species Signature makes the welcome strategically distinctive; House, routine, relationship, Memory, and EMBODY allow utility to become attachment.</td>
</tr>
</tbody>
</table>

<!--@2.1-->
## 2.1 Four simultaneous purposes

<!--@2.1¶1-->
  - Animal breadth: expose the player to bodies, senses, habits, routes, and ecological relationships beyond the three Core species.

<!--@2.1¶2-->
  - Attachment: create a few unusually distinctive friends whose arrival, house, voice, and physical life remain memorable.

<!--@2.1¶3-->
  - Found family: make the Colony's history partly a record of whom it welcomed and how it changed itself to do so.

<!--@2.1¶4-->
  - Design economy: represent many non-Core species without building a second civilization game or unique Away ruleset for each.

<!--@4-->
# 3\. Design Purpose: Kehaar, Difference, and Found Family

<!--@4¶1-->
The principal designer-facing influence is Kehaar in Watership Down. The useful lesson is not merely that a bird helps rabbits. Kehaar expands the perceived world, remains unmistakably non-rabbit, contributes something the rabbits cannot, forms particular relationships, and joins the community without being flattened into it. MEDIAN pursues that structural effect without importing names, plot, or fiction.

<!--@3.1-->
## 3.1 Difference remains visible

<!--@3.1¶1-->
  - A Guest does not become a small reskin of the Core species.

<!--@3.1¶2-->
  - Body, movement, sensing, diet, shelter, habits, communication, and social style remain legible.

<!--@3.1¶3-->
  - The Colony accommodates difference rather than assimilating it out of existence.

<!--@3.1¶4-->
  - Equal status means equal dignity and consequence, not identical mechanics or interchangeable bodies.

<!--@3.2-->
## 3.2 Hospitality is the emotional verb

<!--@3.2¶1-->
The player does not collect an animal and receive a bonus. The Colony meets a particular outsider, learns what continued life together would require, spends real civic effort to make that possible, and then lives with the consequences of the relationship. Recruitment is an act of hospitality before it is a capability unlock.

<!--@3.3-->
## 3.3 Utility opens the door to attachment

<!--@3.3¶1-->
Many players will not treat a Resident Guest as emotionally complete if the base game first teaches them that only expedition-capable characters are useful. The design therefore provides every Guest with an ordinary civic share and a qualitative species Signature. The strategic reason to welcome WHOOT or the Goldwings is real; the later grief, affection, and memory become possible because the game never asked the player to accept a knowingly inferior option for sentiment alone.

<!--@5-->
# 4\. Definitions, Citizen Subjects, and Equal Status

<!--@5¶1-->
| **Term**                 | **Canonical meaning**                                                                          | **Not this**                                                                     |
| ------------------------ | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Core Citizen**         | Named Mouse, Rabbit, or Squirrel belonging to the campaign's civilization grammar.             | Default unit, generic worker, or moral standard against which Guests are lesser. |
| **Guest Citizen**        | Named non-Core Citizen welcomed through relationship and accommodation.                        | Pet, follower, companion slot, collectible, perk module, or temporary hireling.  |
| **Expedition Guest**     | Guest whose species Signature is a bounded Permission inside the shared Away systems.          | A bespoke class with its own Register, combat rules, or Exposure track.          |
| **Resident Guest**       | Guest whose species Signature is a situated Affordance inside DWELL / Home MEET.               | Ambient scenery, passive building bonus, or incomplete expedition character.     |
| **Citizen subject**      | The smallest living subject the Colony can meaningfully know and count.                        | Raw biological body count or Away body-unit.                                     |
| **Signature Permission** | Bounded Away option made possible by an Expedition Guest.                                      | Automatic solution, generic stat increase, or route bypass.                      |
| **Resident Affordance**  | Situated Home possibility made possible by a Resident Guest, their perception, or their House. | Permanent production multiplier or universal immunity.                           |
| **Guest Practice**       | Species-authored way a Resident Guest contributes one ordinary Role Capacity.                  | Personal aptitude score or superior worker tier.                                 |
| **Terms of Hospitality** | Visible conditions that make residence possible for one named Guest.                           | Price list, trust meter, or random recruitment threshold.                        |

<!--@4.1-->
## 4.1 Full Citizen status

<!--@4.1¶1-->
  - A recruited Guest receives a persistent Citizen Record and remains named in every relevant Register.

<!--@4.1¶2-->
  - Relationships, injuries, absence, memory, departure, and death matter at the same moral scale as Core Citizens.

<!--@4.1¶3-->
  - Guests may occupy Roles, require care, be mourned, be memorialized, and be selected for EMBODY.

<!--@4.1¶4-->
  - The game never calls them units, assets, pets, companions, followers, or bonuses in player-facing language.

<!--@4.2-->
## 4.2 Named before recruitment

<!--@4.2¶1-->
The player meets a named animal, not a candidate. If the same animal appears first as threat, neutral party, recurring outsider, and eventual Guest, the name and prior history persist. Antagonist is a position an animal occupies in a circumstance, not necessarily a permanent nature.

<!--@6-->
# 5\. The Two Guest Types

<!--@6¶1-->
| **System property**                         | **Expedition Guest**                | **Resident Guest**                                            |
| ------------------------------------------- | ----------------------------------- | ------------------------------------------------------------- |
| **Citizen status**                          | Full                                | Full                                                          |
| **Citizen Record / relationships / Memory** | Yes                                 | Yes                                                           |
| **Guest House and daily Home routine**      | Yes                                 | Yes                                                           |
| **One Home Role Capacity while present**    | Yes                                 | Yes                                                           |
| **EMBODY eligibility**                      | Yes                                 | Yes                                                           |
| **May be selected at Launch**               | Yes                                 | No                                                            |
| **Personal Away Exposure**                  | Yes                                 | No                                                            |
| **Qualitative Signature**                   | Away Permission                     | Home Affordance                                               |
| **Primary individual mechanical growth**    | Through Away hazard and consequence | Through Home history, situation, relationship, and embodiment |

<!--@5.1-->
## 5.1 Type is a content contract

<!--@5.1¶1-->
Type is not a player toggle, rarity tier, or social rank. A Resident Guest cannot be converted into an Expedition Guest merely because the player wants another party option. A particular Expedition Guest may later choose or be forced into Resident life through age, injury, or story, but that is an authored life change rather than a routine respec.

<!--@5.2-->
## 5.2 Neither type is lesser

<!--@5.2¶1-->
Resident Guests are complete Citizens. Their mechanical package is ordinary Capacity plus a Home Affordance; their expressive package may be richer in daily routine, House use, Home MEET, Presence EMBODY, and domestic relationship than an Expedition Guest whose signature emphasis lies Away. The comparison is equivalent but not equal.

<!--@7-->
# 6\. Equivalent but Not Equal: The Signature Function

<!--@7¶1-->
Every Guest species carries three layers. First, the Citizen contributes one ordinary Role Capacity. Second, the species provides one qualitative Signature Permission or Resident Affordance. Third, housing, routine, EMBODY, relationships, sound, animation, and Memory express the body as a life rather than a rule.

<!--@7¶2-->
<table>
<tbody>
<tr class="odd">
<td><strong>SIGNATURE DOCTRINE<br />
</strong>A Guest contributes like any Citizen, but changes what the Colony can do in a way only that species could. Equivalent design importance does not require equal frequency, magnitude, or tactical form.</td>
</tr>
</tbody>
</table>

<!--@6.1-->
## 6.1 Signature design tests

<!--@6.1¶1-->
  - Attribution: the interface names the Citizen or household responsible for the option.

<!--@6.1¶2-->
  - Situation: the Signature becomes relevant in a bounded circumstance rather than operating as a permanent percentage.

<!--@6.1¶3-->
  - Restraint: the Signature opens or changes a decision; it does not automatically solve the whole event.

<!--@6.1¶4-->
  - Presence: absence, injury, seasonal condition, or House damage may suspend the Signature when fictionally appropriate.

<!--@6.1¶5-->
  - Repeatable value: the Signature has enough recurring relevance that the player can respect it before attachment becomes the primary reward.

<!--@6.1¶6-->
  - Species necessity: the option follows from the animal's body, sensing, behavior, or social ecology rather than an arbitrary class assignment.

<!--@6.2-->
## 6.2 Ordinary Capacity and Signature do not stack into aptitude

<!--@6.2¶1-->
The Goldwings contribute one Gardener Capacity across all constructed Gardens and also possess Carry the Bloom. They are not 1.5 Gardeners. WHOOT contributes one Watchkeeper Capacity and also provides Night Sky-watch. The Affordance is a qualitative exception, not a hidden second worker.

<!--@8-->
# 7\. Population, Growth, Hospitality Capacity, and Colony Tiers

<!--@8¶1-->
Guest recruitment is one of the three population-growth paths, alongside Wanderers and Nursery young. Guests do not extend the Core species lineage; they extend Colony membership. Once welcomed, they occupy real Residence, consume support, add contextual Load, contribute one Capacity while present and available, and count toward neutral Tier proofs.

<!--@7.1-->
## 7.1 Counting rules

<!--@7.1¶1-->
  - One named individual Guest normally counts as one Citizen subject.

<!--@7.1¶2-->
  - Firefly Family and Bumblebee Household count as one Citizen subject and one civic share each.

<!--@7.1¶3-->
  - An Expedition Guest Away remains on the Colony Roster but leaves Home Presence and Home Capacity.

<!--@7.1¶4-->
  - A Resident Guest is never discounted because they cannot Launch.

<!--@7.1¶5-->
  - Guest Houses are Residence Places, not slot sockets.

<!--@7.1¶6-->
  - No Tier, victory condition, or essential system requires a Guest or a particular species.

<!--@7.2-->
## 7.2 Reference Hospitality expectations

<!--@7.2¶1-->
| **Colony Tier**                    | **Typical Guests housed** | **Interpretation**                                                                                |
| ---------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------- |
| **Tier I - Scavenger Camp**        | 0-1                       | A first act of hospitality may define the founding Colony, but no Guest is required.              |
| **Tier II - Fortified Settlement** | 1-2                       | The Colony can usually support one or two unusual Houses without losing legibility.               |
| **Tier III - Independent Colony**  | 2-3                       | A mature Colony may have several Guest histories while remaining a community of particular names. |
| **Tier IV - Sovereign Network**    | 3-5                       | Four or five Guests should feel unusually cosmopolitan, not like an incomplete collection.        |

<!--@7.2¶2-->
These values are authoring expectations, not quotas, visible slots, or automatic Tier rewards. Hospitality Capacity is the Colony's credible ability to house and know Guests through actual Places, Load, sustenance, access, and civic integration.

<!--@9-->
# 8\. Guest Citizens in DWELL: Roles, Practices, and Absence

<!--@8.1-->
## 8.1 Equal Role contribution

<!--@8.1¶1-->
Every present and available adult Guest contributes one Capacity to a Home Role. Role contribution remains global: one Gardener supports the Colony's constructed Gardens as a whole; one Builder supports routine structural responsibility across Home. The game does not route individual workers site by site.

<!--@8.2-->
## 8.2 Resident Guest Practices are fixed

<!--@8.2¶1-->
Resident Guests use a species-authored Guest Practice that fixes their Role contribution. This is a deliberate Guest exception to ordinary Core flexibility. A Bee Household cannot be reassigned from Gardener to Healer because Healing is Thin; the Colony welcomed a particular form of life, not a generic worker plus perk. The Role expresses ordinary civic contribution, while the Affordance expresses qualitative species difference.

<!--@8.3-->
## 8.3 Resident Role distribution

<!--@8.3¶1-->
| **Role**        | **Resident species**           | **Count** |
| --------------- | ------------------------------ | --------- |
| **Builder**     | Mole; Bat                      | 2         |
| **Caretaker**   | Toad; Turtle                   | 2         |
| **Watchkeeper** | Owl; Skunk                     | 2         |
| **Leader**      | Firefly Family; Pigeon         | 2         |
| **Gardener**    | Bumblebee Household; Groundhog | 2         |
| **Healer**      | Opossum                        | 1         |
| **Teacher**     | Songbird                       | 1         |
| **Crafter**     | No current Resident species    | 0         |

<!--@8.3¶2-->
The absent Resident Crafter is deliberate. No current species concept cleanly joins ordinary fabrication Practice with a distinct Crafter Affordance. Core Citizens remain sufficient to cover the Role; the roster is not a deck that must contain every suit.

<!--@8.4-->
## 8.4 Expedition Guest Home roles are individual-authored

<!--@8.4¶1-->
An Expedition species is defined primarily by its Away Permission. Each named example Citizen still has a Home Role and visible Practice, but another individual of that species may contribute differently when the fiction supports it. The detailed roster records the exemplar's Role without turning it into a universal species law.

<!--@8.5-->
## 8.5 Absence remains legible

<!--@8.5¶1-->
When an Expedition Guest launches, the named Citizen leaves Home, one Role Capacity disappears, the House becomes visibly unoccupied, and any routine that depended on their presence stops. Launch is subtraction before it is capability. Resident Guests remain stable Home contributors but may still become unavailable through injury, illness, seasonal condition, displacement, or actual Home danger.

<!--@10-->
# 9\. Guest Houses: Hospitality as Architecture

<!--@10¶1-->
Guest Houses make hospitality physical. The Colony changes its own shape to include a body its ordinary architecture did not anticipate. Every House is a Residence Place, a visual landmark, a routine anchor, an EMBODY entry point, and a possible future site of absence.

<!--@9.1-->
## 9.1 The double-fit test

<!--@9.1¶1-->
| **Host grammar**       | **Guest House requirement**                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mouse - JOIN**       | The unusual room, loft, earth, pool, or garden must join the Manor or its defended exterior circulation.                                       |
| **Rabbit - GATHER**    | The House must face, frame, or participate in communal ground while respecting the occupant's needed distance.                                 |
| **Squirrel - CONNECT** | The House must become a meaningful node with safe approaches, redundancy, and onward relation to the Web.                                      |
| **Guest body**         | Height, water, warmth, darkness, airflow, concealment, flowers, dampness, open sightline, flight access, or other bodily need remains visible. |

<!--@9.2-->
## 9.2 House rules

<!--@9.2¶1-->
  - The House is never a generic socket with an animal icon attached.

<!--@9.2¶2-->
  - Placement cannot violate the Core civilization's spatial identity merely to satisfy the Guest.

<!--@9.2¶3-->
  - Species accommodation may add real access, structure, food, warning, or environmental Load without increasing the Guest's Capacity above one.

<!--@9.2¶4-->
  - The occupied House acquires a folk name connected to the resident or household.

<!--@9.2¶5-->
  - A vacant House persists unless deliberately adapted or dismantled. Absence remains part of the Colony's geography.

<!--@11-->
# 10\. Recruitment: From First MEET to Arrival

<!--@11¶1-->
Recruitment begins with a named animal pursuing their own life. The player does not encounter a recruitable unit. Relationship precedes residence, and residence precedes Citizen integration.

<!--@10.1-->
## 10.1 Canonical sequence

<!--@10.1¶1-->
1.  First MEET: the party or Colony encounters the named animal in a circumstance that exists independently of recruitment.

<!--@10.1¶2-->
2.  Recognition: the outcome establishes a relationship, obligation, Promise, shared interest, or unresolved tension.

<!--@10.1¶3-->
3.  Terms of Hospitality: the animal identifies what continued residence would require in body, place, safety, habit, or relationship.

<!--@10.1¶4-->
4.  Guest House Project: the Colony constructs or adapts the needed Residence through ordinary Project rules.

<!--@10.1¶5-->
5.  Arrival Homecoming: the Guest enters Home, occupies the House, joins the Roster, begins the Role Practice, and establishes relationships.

<!--@10.2-->
## 10.2 Refusal and non-arrival

<!--@10.2¶1-->
The player may refuse, delay, or fail to fulfill the Terms. The named animal remains part of world-state and may depart, return, join another settlement, or remember the decision. Refusal must be a civic choice with consequence, not a hidden failure to collect content.

<!--@12-->
# 11\. Expedition Guests and the Shared Away Framework

<!--@12¶1-->
Expedition Guests use ordinary Launch, party composition, TRAVEL, RISK, Away MEET, Exposure, Return, and Homecoming. Species identity supplies one bounded Signature Permission and a small number of shared-system bodily exceptions. No species receives a separate action economy, combat model, or Exposure track.

<!--@11.1-->
## 11.1 Permission families

<!--@11.1¶1-->
| **Family**    | **Opens**                                                                                  | **Does not do**                                                               |
| ------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| **HANDLE**    | Interact safely or effectively with a category of object, carcass, mechanism, or material. | Identify every hazard, claim every reward, or erase carrying and consequence. |
| **READ**      | Reveal context, pattern, route state, movement, or sign before commitment.                 | Provide omniscience, exact future prediction, or aerial fast travel.          |
| **INTERCEDE** | Create rescue, escort, cover, drive-off, or extraction possibility.                        | Guarantee victory or remove the Guest's own exposure.                         |
| **SPEAK**     | Open recognition, display, intimidation, mediation, or animal-specific communication.      | Translate all species or force agreement.                                     |
| **REACH**     | Enter a bodily domain the ordinary party cannot safely use.                                | Carry the whole party through it or negate the domain's risk.                 |

<!--@11.2-->
## 11.2 Complete Expedition package

<!--@11.2¶1-->
  - One Signature Permission inside the shared Away systems.

<!--@11.2¶2-->
  - A clear Affinity describing where the animal is unusually comfortable or informative.

<!--@11.2¶3-->
  - An Independent Impulse used in authored situations, never as a random disobedience tax.

<!--@11.2¶4-->
  - Ordinary Exposure, injury, loss, gear limits, Return Burden, and Homecoming consequence.

<!--@11.2¶5-->
  - A Home Role, House, absence consequence, relationships, Memory, and EMBODY content.

<!--@13-->
# 12\. Resident Guests and the Home Affordance Framework

<!--@13¶1-->
Resident Guests are authored around domestic behavior, architecture, ritual, weather, care, warning, continuity, receiving, and EMBODY rather than Away traversal. They are complete Citizens without expedition eligibility.

<!--@12.1-->
## 12.1 Complete Resident package

<!--@12.1¶1-->
  - One fixed species-authored Guest Practice and Role Capacity.

<!--@12.1¶2-->
  - One Resident Affordance that opens or changes a situated Home possibility.

<!--@12.1¶3-->
  - A named Guest House and visible daily routine.

<!--@12.1¶4-->
  - Participation in relevant Home MEET as adviser, stake, witness, vulnerable resident, or decision-maker.

<!--@12.1¶5-->
  - Relationships, Campaign Memory, arrival history, and possible injury, departure, or death.

<!--@12.1¶6-->
  - At least one meaningful EMBODY experience.

<!--@12.2-->
## 12.2 Resident utility floor

<!--@12.2¶1-->
A Resident Affordance must be strong enough to satisfy strategic logic before story and attachment carry the choice. It should alter information timing, open a response, preserve or redirect a stake, contain aftermath, sustain continuity, or create social connection. It need not equal an Expedition Permission turn for turn, but the player must be able to name why the Colony is qualitatively different because this Guest lives there.

<!--@12.3-->
## 12.3 No passive-buff fallback

<!--@12.3¶1-->
| **Rejected expression**       | **v0.5 expression**                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------ |
| **+20% predator detection**   | WHOOT gives a nocturnal threat earlier or clearer Telegraph.                                     |
| **-15% spoilage**             | Sump opens a wet-store separation or protection response in a relevant situation.                |
| **Longer workday**            | The Lanterns illuminate one bounded route or Place during a night response.                      |
| **+10% garden yield**         | The Goldwings contribute one Gardener Capacity and may Carry the Bloom into lasting cultivation. |
| **Structural decay immunity** | Velvet reveals damp, rot, insect pressure, or airflow change before damage becomes obvious.      |

<!--@14-->
# 13\. Collective-Bodied Citizen Households

<!--@14¶1-->
For almost every MEDIAN Citizen, one Citizen subject is one named animal. The v0.5 Guest roster contains exactly two exceptions: Firefly Family and Bumblebee Household. This is a closed category, not a general size-class rule.

<!--@14¶2-->
<table>
<tbody>
<tr class="odd">
<td><strong>BODY-UNIT PRINCIPLE<br />
</strong>A Citizen is the smallest living subject the Colony can meaningfully know, not necessarily one biological body. Collective citizenship is used only when the group is more legible, mechanically truthful, and emotionally memorable than a single representative body.</td>
</tr>
</tbody>
</table>

<!--@13.1-->
## 13.1 Shared rules

<!--@13.1¶1-->
  - One collective family or household name and one Citizen Record.

<!--@13.1¶2-->
  - One Colony Roster entry, one Home Presence entry, one Role Capacity, one House, one Affordance, and one Hospitality commitment.

<!--@13.1¶3-->
  - Several visible bodies with recurring formation, circulation, timing, and behavioral identity.

<!--@13.1¶4-->
  - Conditions and major consequences apply to the household; visual thinning may record loss without creating separate administrative Citizens.

<!--@13.1¶5-->
  - Seasonal continuity may change visible membership while the named household persists through Campaign Memory.

<!--@13.2-->
## 13.2 Firefly Family

<!--@13.2¶1-->
A Firefly Family is animated as a loose, recognizable cloud of approximately five or six lights. The family is known by formation, pulse, and route. Its civic action is shared illumination.

<!--@13.3-->
## 13.3 Bumblebee Household

<!--@13.3¶1-->
A Bumblebee Household is represented by several prominently animated bees and known by circulation, hum, and repeated return to one House. Its one Gardener Capacity is global across constructed Gardens. The game does not simulate individual pollination routes or diagnose each Garden separately.

<!--@15-->
# 14\. Guest Citizens in EMBODY

<!--@15¶1-->
When Quiet Equilibrium exists, any present and available Guest may be selected for Home-only EMBODY. Guest EMBODY is a primary means of making bodily difference emotionally legible without designing a complete civilization control scheme for every species.

<!--@14.1-->
## 14.1 Practice and Presence

<!--@14.1¶1-->
| **Form**     | **Guest expression**                                                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Practice** | Participate in a bounded species activity: basking, listening, sorting, swimming, working flowers, tracing a route, tending a House, or guiding light. |
| **Presence** | Accompany the Guest in a characteristic state: warm rain, dark roost, high listening, still water, evening hum, scent-reading, or a household waking.  |

<!--@14.2-->
## 14.2 Control doctrine

<!--@14.2¶1-->
The player should not control every Guest through the same reskinned locomotion. Guest EMBODY may use guided camera attention, body-specific movement, collective flow, sensory emphasis, small gestures, or cinematic accompaniment. The purpose is not traversal mastery; it is to understand how a friend inhabits Home.

<!--@16-->
# 15\. Relationships, Records, and Campaign Memory

<!--@16¶1-->
Every Guest requires at least two plausible relationship directions with Core Citizens: bond, tension, mentorship, fear, obligation, rivalry, dependence, or shared Practice. Species difference creates social material but must not reduce the Guest to a stereotype.

<!--@15.1-->
## 15.1 Citizen Record fields

<!--@15.1¶1-->
  - Name or collective household name, species, Guest type, visual silhouette, and communication register.

<!--@15.1¶2-->
  - Arrival history, Terms of Hospitality, House name, and Role Practice.

<!--@15.1¶3-->
  - Signature Permission or Resident Affordance and its current availability.

<!--@15.1¶4-->
  - Relationships, Conditions, important possessions, and Campaign Memories.

<!--@15.1¶5-->
  - For Expedition Guests: Away history, Distinctions, fears, wounds, Tales, and possible After-name.

<!--@15.1¶6-->
  - For Resident Guests: Home crises, protected Places, seasonal continuity, household change, and EMBODY memories.

<!--@15.2-->
## 15.2 Memory is spatial

<!--@15.2¶1-->
The House, route, perch, scent lane, garden, pool, or hollow should retain signs of the Guest's life. A later vacancy is not only a roster fact. Home sounds, movement, light, and use change. The Colony remembers through the world it built.

<!--@17-->
# 16\. Departure, Injury, Death, and Vacant Houses

<!--@17¶1-->
Guests are not permanent unlocks. Expedition Guests may be injured or killed Away. Resident Guests may be endangered by actual Home circumstances. Either type may leave through choice, unresolved relationship, seasonal need, or changing life. Irreversible named loss does not occur off-screen merely because the player was attending another Register.

<!--@16.1-->
## 16.1 Vacant Houses persist

<!--@16.1¶1-->
  - The House may remain intact as memory or memorial.

<!--@16.1¶2-->
  - It may be maintained for a possible return.

<!--@16.1¶3-->
  - It may become a minor Refuge, lookout, garden, or civic Place when fictionally appropriate.

<!--@16.1¶4-->
  - It may be adapted for a compatible future Guest through a visible Project.

<!--@16.1¶5-->
  - It may be deliberately dismantled, but never disappears automatically as a consumed recruitment token.

<!--@16.2-->
## 16.2 Classification changes

<!--@16.2¶1-->
An Expedition Guest may become Resident after maiming, age, or choice if a complete Home package is authored for that life. The classification change preserves name, relationships, House history, and Memories. It does not reset the Citizen into a new unit.

<!--@18-->
# 17\. Hospitality Capacity, Availability, and Anti-Collection Doctrine

<!--@18¶1-->
The full roster is wider than any one Colony should normally house. Scarcity is valuable because each act of hospitality should alter the settlement and its relationships. The game must not convert that scarcity into rarity colors, completion anxiety, or optimal loadout collection.

<!--@17.1-->
## 17.1 Availability principles

<!--@17.1¶1-->
  - Campaigns encounter more named outsiders than they ultimately welcome.

<!--@17.1¶2-->
  - A Guest may remain a recurring ally, neighbor, rival, visitor, Metropolis resident, or Citizen of another Colony.

<!--@17.1¶3-->
  - No Guest is strictly superior in a linear tier ladder.

<!--@17.1¶4-->
  - No essential route, crop, defense, or ending requires one particular Guest.

<!--@17.1¶5-->
  - A no-Guest campaign remains fully viable at every Colony Tier.

<!--@17.1¶6-->
  - A player may stop growing and decline hospitality without being told the roster is incomplete.

<!--@17.2-->
## 17.2 Anti-collection presentation

<!--@17.2¶1-->
  - No Guest rarity colors, capture language, collection percentages, or recruit-all reward.

<!--@17.2¶2-->
  - No separate Expedition and Resident slot bars presented as sockets to fill.

<!--@17.2¶3-->
  - No disposable replacement with a mechanically superior later specimen.

<!--@17.2¶4-->
  - The roster is presented as possible lives and relationships, not inventory.

<!--@19-->
# 18\. Detailed Expedition Guest Roster

<!--@19¶1-->
The seven Expedition species cover the shared Permission families without requiring an eighth species merely for symmetry. Two INTERCEDE entries are retained because their verbs are materially different: Weasel acts against the threat; Hedgehog acts around the vulnerable party. Each entry includes an illustrative named Citizen and Home Role, but Expedition Home Roles remain individual-authored rather than universal species locks.

<!--@19¶2-->
| **Species**         | **Permission**           | **Example Citizen** | **Example Home Role** | **House**                             |
| ------------------- | ------------------------ | ------------------- | --------------------- | ------------------------------------- |
| Raccoon             | HANDLE - Latchwork       | Latch               | Crafter               | Raised Box / Salvage Loft             |
| Crow                | READ - Long View         | Slate               | Teacher               | High Perch / Open Nest                |
| Red Fox             | HANDLE - Carcass Claim   | Bracken             | Caretaker             | Perimeter Earth / Meat-Handling Apron |
| Weasel              | INTERCEDE - Drive Off    | Rill                | Watchkeeper           | Bank Den / Narrow Patrol Run          |
| Hedgehog            | INTERCEDE - Living Cover | Burdock             | Healer                | Hedge Hollow / Leaf Run               |
| Common Garter Snake | SPEAK - Display          | Sedge               | Teacher               | Warm-Stone Shelter / Scent Threshold  |
| American Mink       | REACH - Water Reach      | Reed                | Builder               | Waterline Lodge / High-Water Refuge   |

<!--@18.1-->
## 18.1. Raccoon

<!--@18.1¶1-->
| **Type**              | Expedition Guest               |
| --------------------- | ------------------------------ |
| **Citizen form**      | Individual Citizen             |
| **Role contribution** | Example Citizen: Crafter       |
| **Signature**         | HANDLE - Latchwork             |
| **Guest House**       | Raised Box / Salvage Loft      |
| **EMBODY focus**      | Dexterous handling and sorting |

<!--@18.1¶2-->
**Species identity.** Dexterous forepaws, comfort with human refuse, curiosity, material intelligence, and a socially canny relationship to possession make the Raccoon the roster's clearest human-object specialist.

<!--@18.1¶3-->
**Mechanical expression.** Latchwork opens sealed or latched human containers and mechanisms at a Node: coolers, capped vessels, tied bags, bin lids, simple catches, and similar objects. The Raccoon makes handling possible; the party still decides whether the object is worth opening and bears whatever the contents attract or release.

<!--@18.1¶4-->
**Limits.** Latchwork does not identify contamination, guarantee useful contents, remove carrying cost, or turn every human mechanism into a solvable puzzle. The Independent Impulse is first inspection: in authored moments the Raccoon may be drawn to test the shut thing before the party has fully settled the surrounding risk.

<!--@18.1¶5-->
**Housing and colony flavor.** A dry raised box, reclaimed human container, or trunk-mounted loft includes a sorting shelf and direct exterior access. Mouse JOIN makes it a receiving loft attached to the Manor; Rabbit GATHER faces it toward the outer court; Squirrel CONNECT makes it a stable box-node. Clicks, lids, sorted objects, and a visible personal collection alter Home.

<!--@18.1¶6-->
**EMBODY.** Test a latch with forepaws, rotate an unfamiliar object, sort a collection by touch, or rest inside the raised box while traffic light passes across the opening.

<!--@18.1¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - LATCH<br />
</strong>Latch is first met inside a service-area waste bin, trapped after opening a lid that will not release from within. The Terms require a dry raised box and one shelf that no Council inventory may claim. Quick-handed and suspicious of waste, Latch contributes as a Crafter at Home. A Core Crafter admires the object fluency; the Leader resents Latch's habit of opening before asking. The remembered image is a row of carefully cleaned useless keys above the House entrance.</td>
</tr>
</tbody>
</table>

<!--@18.2-->
## 18.2. Crow

<!--@18.2¶1-->
| **Type**              | Expedition Guest             |
| --------------------- | ---------------------------- |
| **Citizen form**      | Individual Citizen           |
| **Role contribution** | Example Citizen: Teacher     |
| **Signature**         | READ - Long View             |
| **Guest House**       | High Perch / Open Nest       |
| **EMBODY focus**      | Distant observation and call |

<!--@18.2¶2-->
**Species identity.** Aerial perspective, location memory, call-based communication, curiosity, and the ability to connect distant signs give the Crow a view of the corridor that no ground-bound Citizen possesses.

<!--@18.2¶3-->
**Mechanical expression.** Long View reveals context before commitment: movement beyond cover, the rough shape of a Node, a changed route, an approaching party, or the fact that an apparent opening ends in danger. The Permission gives the expedition a better question to answer rather than the answer itself.

<!--@18.2¶4-->
**Limits.** The Crow does not provide omniscience, exact future prediction, aerial fast travel, or a safe Crossing bypass. The Independent Impulse is widening the look: an unusual glint, call, or movement may draw the Crow beyond the strict briefing and create a new piece of context with its own cost.

<!--@18.2¶5-->
**Housing and colony flavor.** A high open perch or nest needs broad sightlines, safe landing, and no enclosing roof. Mouse JOIN reaches it through a protected wall loft; Rabbit GATHER lets it overlook the common court; Squirrel CONNECT makes it a high node with redundant approaches. Calls become part of the Colony clock.

<!--@18.2¶6-->
**EMBODY.** Turn among distant sounds, watch traffic patterns from above, make a short safe circuit between perches, preen, or sit through a weather change while Home moves below.

<!--@18.2¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - SLATE<br />
</strong>Slate is first met on a sound-wall cap, watching truck rhythm to recover a dropped bright ring. The Terms require a west-facing perch with an unobstructed launch and permission to be absent for solitary day flights. Slate contributes as a Teacher, turning route memory into lessons rather than serving as a permanent alarm. A young Citizen becomes an eager student; an established Watchkeeper dislikes Slate's unscheduled departures. The House is known as Slate's High Room.</td>
</tr>
</tbody>
</table>

<!--@18.3-->
## 18.3. Red Fox

<!--@18.3¶1-->
| **Type**              | Expedition Guest                      |
| --------------------- | ------------------------------------- |
| **Citizen form**      | Individual Citizen                    |
| **Role contribution** | Example Citizen: Caretaker            |
| **Signature**         | HANDLE - Carcass Claim                |
| **Guest House**       | Perimeter Earth / Meat-Handling Apron |
| **EMBODY focus**      | Scent, digging, and boundary rest     |

<!--@18.3¶2-->
**Species identity.** Large body, scent-led perception, predator silhouette, and competence around carcasses make the Fox both materially valuable and socially difficult. The Colony must welcome the individual without pretending inherited prey fear has vanished.

<!--@18.3¶3-->
**Mechanical expression.** Carcass Claim allows the expedition to approach, portion, and make use of a major roadkill or carcass windfall that smaller animals cannot safely handle. It opens decisions about what to take, what to leave, how long to remain, and what attention the work may draw.

<!--@18.3¶4-->
**Limits.** The Fox does not automatically carry the windfall, make it safe to eat, prevent rival scavengers, or remove the moral and social consequences of the scene. The Independent Impulse is claim: the Fox expects a fair share and resists abandoning usable food without reason.

<!--@18.3¶5-->
**Housing and colony flavor.** A substantial earth at the Colony boundary requires direct outer access, drainage, and a handling surface away from Nursery and clean stores. Mouse JOIN uses a defended outer passage; Rabbit GATHER includes the entrance in social frontage without centering it; Squirrel CONNECT links a low earth node to upper refuge routes.

<!--@18.3¶6-->
**EMBODY.** Read the outer edge by scent, dig and arrange bedding, carry food to the apron, curl into the earth, or learn which Colony smells now mean safety.

<!--@18.3¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - BRACKEN<br />
</strong>Bracken is first met at a deer carcass during a lean autumn, initially refusing the expedition any share. A successful PARLEY creates a recurring division of the windfall and eventually an invitation. The Terms require a perimeter earth, a clean handling apron, and a rule against surprise entry through the young Citizens' path. Bracken contributes as a Caretaker. One household trusts the careful food work; another still freezes when the Fox crosses the court. That unresolved bodily truth is part of the relationship.</td>
</tr>
</tbody>
</table>

<!--@18.4-->
## 18.4. Weasel

<!--@18.4¶1-->
| **Type**              | Expedition Guest               |
| --------------------- | ------------------------------ |
| **Citizen form**      | Individual Citizen             |
| **Role contribution** | Example Citizen: Watchkeeper   |
| **Signature**         | INTERCEDE - Drive Off          |
| **Guest House**       | Bank Den / Narrow Patrol Run   |
| **EMBODY focus**      | Fast bank movement and pursuit |

<!--@18.4¶2-->
**Species identity.** Narrow body, explosive speed, intense attention, and willingness to press a smaller predator outward define the Weasel as an active intercessor rather than a general combat unit.

<!--@18.4¶3-->
**Mechanical expression.** Drive Off opens a response against a small predator or aggressive animal: pursue, force away from the vulnerable party, pin attention elsewhere, or create an interval for escape. The action changes the geometry of danger; it does not erase it.

<!--@18.4¶4-->
**Limits.** The Permission does not guarantee victory and exposes the Weasel to injury or separation. The Independent Impulse is pursuit: once committed, the Weasel may carry the chase farther than the party prefers, creating a real WITHDRAW or recovery decision.

<!--@18.4¶5-->
**Housing and colony flavor.** A narrow bank den needs compact tunnels, several exits, and a readable shared threshold. Mouse JOIN attaches it to an exterior run; Rabbit GATHER places the entrance at a court edge; Squirrel CONNECT makes it a low patrol node linked to escape routes. Sudden movement becomes part of Home life.

<!--@18.4¶6-->
**EMBODY.** Move through a bank run, inspect small openings, burst across a short patrol route, play within a safe corridor, or groom after returning to the den.

<!--@18.4¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - RILL<br />
</strong>Rill is first met driving rats from a drainage seam that the expedition needs to cross. The Terms require a bank den with freedom to patrol beyond the immediate boundary and no promise to ignore every rival scent. Rill contributes as a Watchkeeper at Home. The senior Watchkeeper values the patrol instincts; the Healer is exhausted by preventable cuts. The den is called the Quick Bank.</td>
</tr>
</tbody>
</table>

<!--@18.5-->
## 18.5. Hedgehog

<!--@18.5¶1-->
| **Type**              | Expedition Guest             |
| --------------------- | ---------------------------- |
| **Citizen form**      | Individual Citizen           |
| **Role contribution** | Example Citizen: Healer      |
| **Signature**         | INTERCEDE - Living Cover     |
| **Guest House**       | Hedge Hollow / Leaf Run      |
| **EMBODY focus**      | Protected movement and trust |

<!--@18.5¶2-->
**Species identity.** Spines, deliberate pace, low protected body, and a vulnerable face and underside create a form of defense based on sheltering and escort rather than aggression.

<!--@18.5¶3-->
**Mechanical expression.** Living Cover allows the Hedgehog to escort an injured or very small Citizen, shield fragile cargo, or create cover during a withdrawal across exposed ground. The Permission keeps vulnerability moving when ordinary retreat would leave it behind.

<!--@18.5¶4-->
**Limits.** The Hedgehog cannot ignore traffic, protect an entire party, or attack every threat. The Independent Impulse is refusal to abandon: once committed to a vulnerable companion, the Hedgehog may accept delay rather than leave them.

<!--@18.5¶5-->
**Housing and colony flavor.** A dense hedge hollow needs leaf litter, concealment, a quiet run, and enough shared access for care. Mouse JOIN makes it an exterior hedge room; Rabbit GATHER uses it as protective court fringe; Squirrel CONNECT links the low refuge to several routes upward.

<!--@18.5¶6-->
**EMBODY.** Forage beneath leaves, test a hedge passage, curl and slowly relax, or walk beside a smaller friend through protected ground.

<!--@18.5¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - BURDOCK<br />
</strong>Burdock is first met sheltering an injured Mouse beneath a roadside hedge after a failed Crossing. The Terms require a dense leaf hollow and a path wide enough for another Citizen to walk beside it. Burdock contributes as a Healer, especially in recovery companionship. A timid young Rabbit becomes inseparable; a hurried expedition veteran struggles with Burdock's refusal to leave anyone behind. The House is simply Burdock Hedge.</td>
</tr>
</tbody>
</table>

<!--@18.6-->
## 18.6. Common Garter Snake

<!--@18.6¶1-->
| **Type**              | Expedition Guest                     |
| --------------------- | ------------------------------------ |
| **Citizen form**      | Individual Citizen                   |
| **Role contribution** | Example Citizen: Teacher             |
| **Signature**         | SPEAK - Display                      |
| **Guest House**       | Warm-Stone Shelter / Scent Threshold |
| **EMBODY focus**      | Basking and scent-reading            |

<!--@18.6¶2-->
**Species identity.** Limbless movement, scent-led perception, warmth dependence, silent display, and inherited prey fear make the Garter Snake a powerful test of whether equal citizenship can preserve bodily difference.

<!--@18.6¶3-->
**Mechanical expression.** Display opens intimidation, recognition, or nonverbal communication with animals that understand snake posture and threat. It may create a PARLEY, YIELD, or withdrawal option where ordinary speech has no force.

<!--@18.6¶4-->
**Limits.** Display is not a venom attack, universal translator, or guaranteed surrender. The Independent Impulse is stillness and presentation: when pressed, the Snake may choose to hold ground and become unmistakable rather than flee.

<!--@18.6¶5-->
**Housing and colony flavor.** A south-facing warm-stone shelter needs protected cracks, basking surface, and a visible approach that prevents surprise encounters. Mouse JOIN attaches a heated wall chamber; Rabbit GATHER places a sunny shelf at the court edge; Squirrel CONNECT links the low warm node into safe routes.

<!--@18.6¶6-->
**EMBODY.** Follow a sun patch, move through warm grass, test scent, coil inside a sheltered crack, or rest beside a trusted Citizen who has learned not to startle.

<!--@18.6¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - SEDGE<br />
</strong>Sedge is first met basking across the expedition's only safe concrete seam and refuses to move until the party acknowledges the territory. The Terms require a warm stone House and a Colony custom of announcing movement near its entrance. Sedge contributes as a Teacher, sharing scent and ground knowledge rather than becoming a Watchkeeper. One young Citizen is fascinated; several Rabbits remain visibly uneasy. The custom of calling "warm side" before passing becomes part of Home etiquette.</td>
</tr>
</tbody>
</table>

<!--@18.7-->
## 18.7. American Mink

<!--@18.7¶1-->
| **Type**              | Expedition Guest                     |
| --------------------- | ------------------------------------ |
| **Citizen form**      | Individual Citizen                   |
| **Role contribution** | Example Citizen: Builder             |
| **Signature**         | REACH - Water Reach                  |
| **Guest House**       | Waterline Lodge / High-Water Refuge  |
| **EMBODY focus**      | Swimming, diving, and waterline rest |

<!--@18.7¶2-->
**Species identity.** Water competence, sleek speed, culvert familiarity, and a powerful rescue impulse make the Mink the expedition's access to water as a lived domain rather than a generic terrain modifier.

<!--@18.7¶3-->
**Mechanical expression.** Water Reach allows the Mink to enter water, flooded culverts, drainage channels, or waterlogged spaces to retrieve, inspect, or rescue where the ordinary party cannot safely go.

<!--@18.7¶4-->
**Limits.** The Mink does not ferry the party, eliminate cold or current, make floodwater clean, or guarantee recovery. The Independent Impulse is immediate rescue: when a life is visibly in danger, the Mink may enter before the Council has finished deciding.

<!--@18.7¶5-->
**Housing and colony flavor.** A waterline lodge needs direct water entry, a dry interior, and refuge above ordinary flood rise. Mouse JOIN attaches it to a culvert annex; Rabbit GATHER places it beside a protected pool; Squirrel CONNECT treats it as a low water node with several routes upward.

<!--@18.7¶6-->
**EMBODY.** Swim a protected channel, dive beneath roots, groom at the lodge entrance, or float quietly while watching Home from water level.

<!--@18.7¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - REED<br />
</strong>Reed is first met pulling a stranded Squirrel from runoff before either Colony or expedition has chosen sides. The Terms require a lodge with direct water access and a high-water chamber that remains connected to Home. Reed contributes as a Builder, taking responsibility for waterline structures. The Builder trusts Reed's reading of current; the Leader fears the rescue impulse will someday outrun the party. Wet tracks between the lodge and Council become an ordinary part of dawn.</td>
</tr>
</tbody>
</table>

<!--@20-->
# 19\. Detailed Resident Guest Roster

<!--@20¶1-->
The twelve Resident species are distributed across seven Home Roles and each receives one Affordance. The roster intentionally contains only two Watchkeepers and two Caretakers. It also includes three later additions - Pigeon, Skunk, and Opossum - which fill external relationship, nonlethal defense, and Homecoming-aftermath needs not covered by the earlier roster.

<!--@20¶2-->
| **Species**         | **Fixed Role** | **Affordance**                  | **Example Citizen** | **Citizen form**          |
| ------------------- | -------------- | ------------------------------- | ------------------- | ------------------------- |
| Barred Owl          | Watchkeeper    | Night Sky-watch                 | WHOOT               | Individual Citizen        |
| Song Sparrow        | Teacher        | Day Call                        | Lilt                | Individual Citizen        |
| American Toad       | Caretaker      | Wet-Ground and Store Protection | Sump                | Individual Citizen        |
| Firefly Family      | Leader         | Lantern Procession              | The Lanterns        | Collective-bodied Citizen |
| Groundhog           | Gardener       | Seasonal Telegraph              | Rootwake            | Individual Citizen        |
| Painted Turtle      | Caretaker      | Protected Receiving             | Stillwater          | Individual Citizen        |
| Bumblebee Household | Gardener       | Carry the Bloom                 | The Goldwings       | Collective-bodied Citizen |
| Eastern Mole        | Builder        | Subsurface Diagnosis            | Marl                | Individual Citizen        |
| Little Brown Bat    | Builder        | Dry-Dark Structure Care         | Velvet              | Individual Citizen        |
| Rock Pigeon         | Leader         | Correspondence                  | Gable               | Individual Citizen        |
| Striped Skunk       | Watchkeeper    | Boundary Deterrence             | Sable               | Individual Citizen        |
| Virginia Opossum    | Healer         | Aftermath Receiving             | Morrow              | Individual Citizen        |

<!--@19.1-->
## 19.1. Barred Owl

<!--@19.1¶1-->
| **Type**              | Resident Guest                        |
| --------------------- | ------------------------------------- |
| **Citizen form**      | Individual Citizen                    |
| **Role contribution** | Watchkeeper - fixed Guest Practice    |
| **Signature**         | Night Sky-watch                       |
| **Guest House**       | High Hollow / Accessible Roost        |
| **EMBODY focus**      | Nocturnal listening and high presence |

<!--@19.1¶2-->
**Species identity.** Nocturnal hearing, high perspective, quiet patience, and a body built for night establish the Owl as a resident whose warning is sensory rather than numerical.

<!--@19.1¶3-->
**Mechanical expression.** Night Sky-watch gives a nocturnal predator or unusual night movement earlier or clearer Telegraph when the Owl is present and the High Hollow is usable. The Affordance may identify direction, behavior, or the fact that the movement is not ordinary weather.

<!--@19.1¶4-->
**Limits.** The Owl does not provide universal detection, daytime coverage, exact distance, or automatic defense. If injury, weather, disturbance, or House damage prevents listening, the Affordance is unavailable.

<!--@19.1¶5-->
**Housing and colony flavor.** A dry dark high hollow needs a broad listening opening and species-appropriate access. Mouse JOIN reaches it through a protected loft or ramp; Rabbit GATHER lets it overlook the common ground without dominating it; Squirrel CONNECT makes it a high stable node. The Colony's night soundscape changes around the resident calls.

<!--@19.1¶6-->
**EMBODY.** Listen while the Colony settles, turn toward sounds other Citizens cannot hear, groom within the hollow, or watch moonlit traffic from a safe opening.

<!--@19.1¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - WHOOT<br />
</strong>WHOOT is a barred owl with a permanently weak wing, first met grounded after a storm and surviving by listening from a broken sign cavity. The Terms require an accessible high hollow that can be reached without full flight. WHOOT contributes one Watchkeeper Capacity and provides Night Sky-watch. A young Citizen learns the night calls; an older Watchkeeper initially resents advice from someone who cannot patrol. The first winter in which WHOOT hears a fox before anyone else becomes a defining Tale.</td>
</tr>
</tbody>
</table>

<!--@19.2-->
## 19.2. Song Sparrow

<!--@19.2¶1-->
| **Type**              | Resident Guest                                |
| --------------------- | --------------------------------------------- |
| **Citizen form**      | Individual Citizen                            |
| **Role contribution** | Teacher - fixed Guest Practice                |
| **Signature**         | Day Call                                      |
| **Guest House**       | Circle Nest / Court-Side Shrub                |
| **EMBODY focus**      | Song, call recognition, and seasonal presence |

<!--@19.2¶2-->
**Species identity.** Learned calls, seasonal song, repeated perches, and the gradual ability of other Citizens to understand one named bird make the Songbird a cultural resident rather than another generic alarm.

<!--@19.2¶3-->
**Mechanical expression.** Day Call opens an alarm or rally response during aerial danger or sudden daylight disruption. Scattered Citizens recognize that the same situation is occurring and may gather, shelter, or follow a coordinated instruction before confusion separates them.

<!--@19.2¶4-->
**Limits.** Day Call does not detect every threat, prevent panic automatically, or create a colony-wide morale modifier. It depends on the Songbird being present and the Colony having learned the calls through ordinary life.

<!--@19.2¶5-->
**Housing and colony flavor.** A small nest needs concealment, a clear singing perch, and social proximity. Mouse JOIN uses a planted wall room or exterior niche; Rabbit GATHER places the nest above the Story Circle; Squirrel CONNECT makes it a modest branch node near a shared junction. Seasonal songs enter the memory of Home.

<!--@19.2¶6-->
**EMBODY.** Sing from familiar points, bathe in shallow water, gather nesting material, or sit with the Colony as individual calls acquire shared meaning.

<!--@19.2¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - LILT<br />
</strong>Lilt returns to the same thorn shrub for three springs before a storm destroys the old nesting ground. The Terms require a concealed nest overlooking the Story Circle and a quiet interval at dawn. Lilt contributes as Teacher. Young Citizens learn the difference between food call, alarm, and ordinary song; an Elder remembers the first season by which melody was heard. If the nest later falls silent, the whole court feels the absence before the roster is opened.</td>
</tr>
</tbody>
</table>

<!--@19.3-->
## 19.3. American Toad

<!--@19.3¶1-->
| **Type**              | Resident Guest                                |
| --------------------- | --------------------------------------------- |
| **Citizen form**      | Individual Citizen                            |
| **Role contribution** | Caretaker - fixed Guest Practice              |
| **Signature**         | Wet-Ground and Store Protection               |
| **Guest House**       | Rain Niche / Culvert House with Dry Refuge    |
| **EMBODY focus**      | Warm rain, stillness, and wet-ground movement |

<!--@19.3¶2-->
**Species identity.** Dampness, stillness, runoff familiarity, and a body that moves between wet ground and dry refuge make the Toad a domestic interpreter of water where it meets stores and inhabited space.

<!--@19.3¶3-->
**Mechanical expression.** During runoff, damp-storage, culvert, or contamination situations, the Toad opens a response that separates threatened stores, redirects shallow water, identifies what remains safe, or protects one domestic stake from spreading wet damage.

<!--@19.3¶4-->
**Limits.** The Affordance is not a permanent spoilage reduction, water purification aura, or flood immunity. It applies only where wetness and domestic consequence meaningfully meet.

<!--@19.3¶5-->
**Housing and colony flavor.** A damp niche needs leaf cover, a shallow wet approach, and an elevated dry refuge. Mouse JOIN builds it into a culvert-facing exterior room; Rabbit GATHER places it beside controlled wet ground at the court edge; Squirrel CONNECT makes it a low rain node with routes upward.

<!--@19.3¶6-->
**EMBODY.** Sit in warm rain, move through wet leaves, wait in stillness, or make a small feeding movement as dusk reaches the House.

<!--@19.3¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - SUMP<br />
</strong>Sump is first met in a flooded drainage hollow, repeatedly returning to the same dry bottle-cap ledge as water rises. The Terms require a damp chamber and a dry shelf above the ordinary runoff line. Sump contributes as Caretaker and provides Wet-Ground and Store Protection. A household Cook trusts Sump's judgment about wet food; a Gardener finds the stillness unnerving. The Rain Niche becomes the Place where children first learn that water has several different sounds.</td>
</tr>
</tbody>
</table>

<!--@19.4-->
## 19.4. Firefly Family

<!--@19.4¶1-->
| **Type**              | Resident Guest                                                                   |
| --------------------- | -------------------------------------------------------------------------------- |
| **Citizen form**      | Collective-bodied Citizen - one named family, usually five or six visible lights |
| **Role contribution** | Leader - fixed Guest Practice                                                    |
| **Signature**         | Lantern Procession                                                               |
| **Guest House**       | Dusk Hollow / Lantern Garden                                                     |
| **EMBODY focus**      | Loose constellation and shared illumination                                      |

<!--@19.4¶2-->
**Species identity.** The Firefly Family is known as one small luminous household whose formation, pulse, and route are more legible than any single tiny body. Their civic identity is coordinated light.

<!--@19.4¶3-->
**Mechanical expression.** Lantern Procession illuminates one bounded route or small Place during a night Home MEET: an evacuation path, Healing Place, urgent Council, flood edge, or final dark approach for a returning party. The family allows scattered Citizens to act together in darkness.

<!--@19.4¶4-->
**Limits.** The Affordance does not extend the universal workday, light several Places at once, remove night pressure, or behave as permanent infrastructure. The lights gather and go somewhere; choosing one route means leaving another dark.

<!--@19.4¶5-->
**Housing and colony flavor.** A protected grass hollow needs damp leaf litter, darkness by day, an open evening flight space, and freedom from harsh artificial light. Mouse JOIN creates a planted dark court attached to the Manor; Rabbit GATHER places it at the common's quiet edge; Squirrel CONNECT makes it a ground-level glow node linked to higher routes.

<!--@19.4¶6-->
**EMBODY.** Guide the family as a loose constellation, widen or narrow the formation, pause above one Place, accompany first emergence, or follow one lagging light until it rejoins the others.

<!--@19.4¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - THE LANTERNS<br />
</strong>The Lanterns are six recurring lights first seen gathering around a lost young Citizen at the edge of the median, making the safe grass route visible. The Terms require a protected Dusk Hollow and a Colony rule against bright flame near it. They contribute as one Leader Capacity and provide Lantern Procession. Young Citizens learn each light's habitual place in the formation. After a hard storm, only five lights return; the missing space becomes visible Campaign Memory without creating a separate roster death.</td>
</tr>
</tbody>
</table>

<!--@19.5-->
## 19.5. Groundhog

<!--@19.5¶1-->
| **Type**              | Resident Guest                     |
| --------------------- | ---------------------------------- |
| **Citizen form**      | Individual Citizen                 |
| **Role contribution** | Gardener - fixed Guest Practice    |
| **Signature**         | Seasonal Telegraph                 |
| **Guest House**       | Deep Perimeter Burrow / Lookout    |
| **EMBODY focus**      | Soil, lookout, and seasonal change |

<!--@19.5¶2-->
**Species identity.** Deep burrowing, upright weather-reading, seasonal rhythm, and attention to changing ground make the Groundhog a Gardener whose knowledge concerns the timing of green life rather than individual plots.

<!--@19.5¶3-->
**Mechanical expression.** Seasonal Telegraph identifies the family of an approaching pressure before the Council commits its posture: hard frost rather than an ordinary cold night, flood rather than ordinary rain, heat stress, disruptive human work, or another major seasonal turn.

<!--@19.5¶4-->
**Limits.** The Groundhog does not provide an exact forecast, countdown, guaranteed severity, or universal warning. The information remains qualitative and may still leave difficult choices.

<!--@19.5¶5-->
**Housing and colony flavor.** A deep perimeter burrow needs drainage, more than one safe entrance, an undisturbed ground volume, and a visible lookout. Mouse JOIN links it through a defended outer passage; Rabbit GATHER places the lookout toward the court; Squirrel CONNECT makes the burrow a low seasonal node tied to several routes.

<!--@19.5¶6-->
**EMBODY.** Stand upright to read weather, clear a burrow entrance, sun on the lookout, or accompany the first bodily response to seasonal change.

<!--@19.5¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - ROOTWAKE<br />
</strong>Rootwake is first met repeatedly filling a shallow trench before a road crew arrives, behavior the expedition initially mistakes for territorial fussing. The Terms require a deep burrow, a lookout mound, and a promise that no later Project will build across the tunnels. Rootwake contributes as Gardener and provides Seasonal Telegraph. The Builder sometimes resents the protected ground; the Colony learns that Rootwake changes routine before the sky explains why.</td>
</tr>
</tbody>
</table>

<!--@19.6-->
## 19.6. Painted Turtle

<!--@19.6¶1-->
| **Type**              | Resident Guest                       |
| --------------------- | ------------------------------------ |
| **Citizen form**      | Individual Citizen                   |
| **Role contribution** | Caretaker - fixed Guest Practice     |
| **Signature**         | Protected Receiving                  |
| **Guest House**       | Stonewater Chamber / Basking Shelf   |
| **EMBODY focus**      | Patience, basking, and shallow water |

<!--@19.6¶2-->
**Species identity.** Shell, deliberate movement, water access, and temporal patience make the Turtle a resident of continuity and safe holding rather than speed or output.

<!--@19.6¶3-->
**Mechanical expression.** Protected Receiving allows one explicitly chosen reserve, fragile Record, medicine stock, unusual returning object, or other bounded stake to be held safely during a relevant crisis. The selection is made before impact or as part of Telegraph and response.

<!--@19.6¶4-->
**Limits.** The chamber is not automatic insurance for all stores, a generic armor bonus, or unlimited secure inventory. Protecting one stake may mean leaving another exposed.

<!--@19.6¶5-->
**Housing and colony flavor.** A sunk stone chamber needs shallow water access, a basking shelf, and a protected dry interior. Mouse JOIN attaches a pool chamber to the Manor edge; Rabbit GATHER makes it part of a quiet communal water garden; Squirrel CONNECT treats it as a stable low node with routes to higher refuge.

<!--@19.6¶6-->
**EMBODY.** Bask, enter shallow water, move slowly through a garden path, or watch highway light travel across the surface.

<!--@19.6¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - STILLWATER<br />
</strong>Stillwater is first met stranded in a drainage pool that is drying faster than the Turtle can leave it. The Terms require a shallow permanent pool, warm stone, and a chamber that remains dry through ordinary rain. Stillwater contributes as Caretaker and provides Protected Receiving. A Teacher values the unhurried presence; impatient Citizens learn that some decisions can be held without being forgotten. The Stonewater Chamber later protects the first written Colony Record during a flood.</td>
</tr>
</tbody>
</table>

<!--@19.7-->
## 19.7. Bumblebee Household

<!--@19.7¶1-->
| **Type**              | Resident Guest                                                                      |
| --------------------- | ----------------------------------------------------------------------------------- |
| **Citizen form**      | Collective-bodied Citizen - one named household represented by several visible bees |
| **Role contribution** | Gardener - fixed Guest Practice                                                     |
| **Signature**         | Carry the Bloom                                                                     |
| **Guest House**       | Moss House / Bee Garden                                                             |
| **EMBODY focus**      | Hum, warmth, and coordinated flower work                                            |

<!--@19.7¶2-->
**Species identity.** A Bumblebee Household is known through circulation, hum, repeated return, and collective work. Several visible bodies produce one legible civic subject without creating a hidden bee civilization or honey economy.

<!--@19.7¶3-->
**Mechanical expression.** The household contributes one global Gardener Capacity across all constructed Gardens. Carry the Bloom allows an exceptional flowering plant recovered Away to become a persistent cultivated line through an ordinary Garden Project, or allows a threatened rare line to survive by sacrificing present yield and committing civic effort.

<!--@19.7¶4-->
**Limits.** The game does not assign bees to individual Gardens, simulate pollination routes, diagnose plot health, increase all yields, or make ordinary farming dependent on Guests. Carry the Bloom applies to exceptional continuity, not baseline agriculture.

<!--@19.7¶5-->
**Housing and colony flavor.** A protected moss-lined cavity needs warmth, shelter from hard rain and flooding, a clear flight opening, and broad non-mechanical access to flowering space. Mouse JOIN places it in a planted exterior chamber; Rabbit GATHER uses a flower bank at the court edge; Squirrel CONNECT makes it a garden node linked through the Web.

<!--@19.7¶6-->
**EMBODY.** Accompany the household through an impressionistic sequence of Gardens, feel vibration and warmth at first emergence, shelter as wind rises, or return to the House through the familiar opening.

<!--@19.7¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - THE GOLDWINGS<br />
</strong>The Goldwings are first met working a rare roadside flower after mowing destroys their former nest. The Terms require a warm Moss House, protected flower access, and no smoke near the opening. They contribute one Gardener Capacity across all Gardens and provide Carry the Bloom. A Gardener later brings home the same roadside flower; with the Goldwings it becomes a lasting Colony planting. Years later the bloom beside the Nursery remembers both household and expedition.</td>
</tr>
</tbody>
</table>

<!--@19.8-->
## 19.8. Eastern Mole

<!--@19.8¶1-->
| **Type**              | Resident Guest                             |
| --------------------- | ------------------------------------------ |
| **Citizen form**      | Individual Citizen                         |
| **Role contribution** | Builder - fixed Guest Practice             |
| **Signature**         | Subsurface Diagnosis                       |
| **Guest House**       | Visible Cutaway Tunnel House / Mound Court |
| **EMBODY focus**      | Soil listening and bounded digging         |

<!--@19.8¶2-->
**Species identity.** Ground vibration, soil movement, hidden voids, and a body adapted to digging make the Mole a Builder who reveals what the Colony cannot see beneath its Places.

<!--@19.8¶3-->
**Mechanical expression.** Subsurface Diagnosis may reveal saturated soil, hidden void, undercutting water, severed root structure, frost-heaved ground, or buried obstruction before visible collapse. The information can make a preventive Builder Project or different MEET response possible.

<!--@19.8¶4-->
**Limits.** The Mole does not create a hidden underground civilization, automatically excavate new rooms, reveal arbitrary treasure, or make structures immune to failure.

<!--@19.8¶5-->
**Housing and colony flavor.** The House is a bounded, readable cutaway tunnel system with visible entrances and mounds. Mouse JOIN integrates it beside an exterior foundation; Rabbit GATHER lets mounds define a court edge; Squirrel CONNECT makes the low soil Place part of several surface routes. The no-underground doctrine remains intact because the resident stays visually legible.

<!--@19.8¶6-->
**EMBODY.** Dig a short safe run, listen through soil, shape loose earth, or emerge through a familiar sheltered opening.

<!--@19.8¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - MARL<br />
</strong>Marl is first met when a new tunnel breaks into an undercut bank and the Mole repeatedly blocks the expedition from crossing it. The Terms require a defined ground volume and visible entrances that Colony construction will respect. Marl contributes as Builder and provides Subsurface Diagnosis. A Builder learns to trust the sudden appearance of fresh mounds; a Squirrel finds the unseen movement deeply uncomfortable. The House is called Marl Below, though it remains visible in cutaway.</td>
</tr>
</tbody>
</table>

<!--@19.9-->
## 19.9. Little Brown Bat

<!--@19.9¶1-->
| **Type**              | Resident Guest                    |
| --------------------- | --------------------------------- |
| **Citizen form**      | Individual Citizen                |
| **Role contribution** | Builder - fixed Guest Practice    |
| **Signature**         | Dry-Dark Structure Care           |
| **Guest House**       | High Dry Roost / Flight Aperture  |
| **EMBODY focus**      | Echo, hanging, and dusk departure |

<!--@19.9¶2-->
**Species identity.** Echolocation, sensitivity to enclosed air, roosting in dry darkness, and local flight make the Bat a structural resident of spaces other Citizens rarely inspect.

<!--@19.9¶3-->
**Mechanical expression.** Dry-Dark Structure Care reveals damp, rot, insect pressure, obstructed airflow, or another change inside high enclosed structure before the resulting damage becomes obvious. It may open inspection, ventilation, or localized repair responses.

<!--@19.9¶4-->
**Limits.** The Bat does not eliminate structural decay, monitor the entire Colony at once, replace Builder Capacity, or become a night Watchkeeper merely because flight occurs after dusk.

<!--@19.9¶5-->
**Housing and colony flavor.** A high dry dark roost needs hanging space, stable temperature, a clear flight aperture, and freedom from smoke. Mouse JOIN makes it an upper wall chamber; Rabbit GATHER places it above the court with flight kept clear of busy ground; Squirrel CONNECT integrates it as a sheltered high node.

<!--@19.9¶6-->
**EMBODY.** Hang and groom, turn toward returning echoes, make a short dusk circuit, or experience Home through sound and changing air.

<!--@19.9¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - VELVET<br />
</strong>Velvet is first met roosting inside a cracked highway reflector box after human work seals the former cavity. The Terms require a smoke-free high roost and an unobstructed evening aperture. Velvet contributes as Builder and provides Dry-Dark Structure Care. A Crafter is fascinated by echolocation; a young Citizen fears the silent returns until a repeated dusk routine becomes familiar. Velvet is the first to hear water moving inside a wall after winter thaw.</td>
</tr>
</tbody>
</table>

<!--@19.10-->
## 19.10. Rock Pigeon

<!--@19.10¶1-->
| **Type**              | Resident Guest                             |
| --------------------- | ------------------------------------------ |
| **Citizen form**      | Individual Citizen                         |
| **Role contribution** | Leader - fixed Guest Practice              |
| **Signature**         | Correspondence                             |
| **Guest House**       | Ledge Loft / Open Flight Shelf             |
| **EMBODY focus**      | Built-environment flight and social signal |

<!--@19.10¶2-->
**Species identity.** Landmark memory, social signaling, comfort with human structures, and movement among distant flock sites give the Pigeon a civic relationship to outside communities rather than a combat or scouting package.

<!--@19.10¶3-->
**Mechanical expression.** Correspondence opens a Send Word, Ask the Flock, or identify-the-origin response in situations involving Wanderers, known settlements, the Metropolis, or unusual built-environment activity. The result may create a delayed answer, Promise, or short civic Project.

<!--@19.10¶4-->
**Limits.** Correspondence is not instant communication, guaranteed delivery, a permanent world map, or a substitute for expedition travel. The Pigeon may know routes and social traces without knowing every message's meaning.

<!--@19.10¶5-->
**Housing and colony flavor.** A dry ledge loft needs stable landing, open flight, and visibility to distant structures. Mouse JOIN attaches it to a wall or sign loft; Rabbit GATHER places it above communal frontage; Squirrel CONNECT makes it a broad stable node. Cooing, circling, and occasional visitors enlarge the Colony's social horizon.

<!--@19.10¶6-->
**EMBODY.** Warm on a ledge, dust-bathe, head-bob through a shared Place, or make a short circle above Home and return to the same landmark.

<!--@19.10¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - GABLE<br />
</strong>Gable is first met at an overpass carrying colored thread tied by another settlement, though the message is not immediately understood. The Terms require a dry ledge loft and a clear western flight lane. Gable contributes as Leader and provides Correspondence. The Council depends on the social reach; an expedition veteran distrusts answers that arrive through flock rumor. The first successful Send Word prevents a Wanderer family from reaching a closed route.</td>
</tr>
</tbody>
</table>

<!--@19.11-->
## 19.11. Striped Skunk

<!--@19.11¶1-->
| **Type**              | Resident Guest                            |
| --------------------- | ----------------------------------------- |
| **Citizen form**      | Individual Citizen                        |
| **Role contribution** | Watchkeeper - fixed Guest Practice        |
| **Signature**         | Boundary Deterrence                       |
| **Guest House**       | Downwind Den / Perimeter Lane             |
| **EMBODY focus**      | Deliberate dusk patrol and scent boundary |

<!--@19.11¶2-->
**Species identity.** Deliberate nocturnal movement, unmistakable warning, nonlethal deterrence, and a body that forces the Colony to negotiate proximity and airflow make the Skunk a Watchkeeper by boundary presence rather than surveillance.

<!--@19.11¶3-->
**Mechanical expression.** Boundary Deterrence opens a nonlethal drive-off response during predator or aggressive-scavenger Home MEET. The response can prevent direct Contest but usually creates a localized Scented Home aftermath affecting one Place, approach, or social situation.

<!--@19.11¶4-->
**Limits.** The Affordance is not automatic perfect defense, cannot be used without consequence in crowded interior space, and may be unavailable when wind, injury, or placement makes the response unsafe for the Colony.

<!--@19.11¶5-->
**Housing and colony flavor.** A well-drained den needs a downwind perimeter position, clear approach, and separation from Nursery, food stores, and the Story Circle. Mouse JOIN uses a defended outer bank; Rabbit GATHER keeps the entrance visible from communal ground at respectful distance; Squirrel CONNECT links it as a low boundary node.

<!--@19.11¶6-->
**EMBODY.** Walk a dusk boundary, root through leaves, test wind, mark a safe edge, or groom outside the den while Home keeps a respectful lane open.

<!--@19.11¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - SABLE<br />
</strong>Sable is first met standing between a young Rabbit and a coyote, holding the threat long enough for escape without fighting. The Terms require a downwind den and a clear perimeter lane no household will block. Sable contributes as Watchkeeper and provides Boundary Deterrence. The Watchkeepers respect the calm; Caretakers complain whenever the wind shifts after a response. The Colony eventually treats "Sable weather" as a practical civic phrase rather than a joke.</td>
</tr>
</tbody>
</table>

<!--@19.12-->
## 19.12. Virginia Opossum

<!--@19.12¶1-->
| **Type**              | Resident Guest                                 |
| --------------------- | ---------------------------------------------- |
| **Citizen form**      | Individual Citizen                             |
| **Role contribution** | Healer - fixed Guest Practice                  |
| **Signature**         | Aftermath Receiving                            |
| **Guest House**       | Dry Receiving Cavity / Dirty Edge              |
| **EMBODY focus**      | Nocturnal cleanup, balance, and deep stillness |

<!--@19.12¶2-->
**Species identity.** Nocturnal scavenging, careful handling of unpleasant remains, climbing, and the ability to become deeply still under danger make the Opossum a Healer of boundaries between injury, contamination, and ordinary Home.

<!--@19.12¶3-->
**Mechanical expression.** Aftermath Receiving opens an isolation-and-cleanup response when Homecoming or Home MEET brings contaminated salvage, spoiled stores, a carcass, an unknown substance, or a potentially infectious patient. Broad contamination becomes a contained Cleanup, treatment, or temporary Place problem.

<!--@19.12¶4-->
**Limits.** The Affordance does not erase illness, make contaminated material safe, grant biological immunity, or remove Caretaking and Healing Load. It changes the shape and spread of consequence.

<!--@19.12¶5-->
**Housing and colony flavor.** A dry cavity or reclaimed box needs a climbing route, ventilation, and placement near the receiving or refuse edge but apart from clean stores. Mouse JOIN makes it a controlled exterior receiving room; Rabbit GATHER places it at the court's service edge; Squirrel CONNECT links it to both receiving ground and upper retreat.

<!--@19.12¶6-->
**EMBODY.** Move along a nocturnal receiving route, balance with the tail, arrange a sleeping cavity, inspect debris, or wake slowly while the Colony remains quiet.

<!--@19.12¶7-->
<table>
<tbody>
<tr class="odd">
<td><strong>EXAMPLE CITIZEN - MORROW<br />
</strong>Morrow is first met after a storm, calmly separating edible remains from contaminated debris while other scavengers avoid the site. The Terms require a dry box near the receiving edge and a firm separation from clean stores. Morrow contributes as Healer and provides Aftermath Receiving. The Healer values the calm during ugly work; a Crafter repeatedly brings questionable salvage too close. Morrow becomes the Citizen who meets returning parties before celebration begins.</td>
</tr>
</tbody>
</table>

<!--@21-->
# 20\. Roster Balance and System Coverage

<!--@20.1-->
## 20.1 Expedition Permission coverage

<!--@20.1¶1-->
| **Permission family** | **Species**  | **Distinct use**                                |
| --------------------- | ------------ | ----------------------------------------------- |
| **HANDLE**            | Raccoon      | Human containers and simple mechanisms.         |
| **HANDLE**            | Red Fox      | Major carcass and roadkill windfall.            |
| **READ**              | Crow         | Distant context and changed route state.        |
| **INTERCEDE**         | Weasel       | Drive threat outward or create escape interval. |
| **INTERCEDE**         | Hedgehog     | Escort, cover, and protect vulnerable movement. |
| **SPEAK**             | Garter Snake | Display, intimidation, and animal recognition.  |
| **REACH**             | Mink         | Water, culvert, and flooded-space access.       |

<!--@20.2-->
## 20.2 Resident need coverage

<!--@20.2¶1-->
| **Colony need**                   | **Principal Resident** | **Qualitative change**                                       |
| --------------------------------- | ---------------------- | ------------------------------------------------------------ |
| **Night warning**                 | Owl                    | Earlier or clearer nocturnal Telegraph.                      |
| **Day rally and learned signal**  | Songbird               | Scattered Citizens recognize one shared event.               |
| **Wet stores and runoff**         | Toad                   | Protect, separate, or redirect a domestic wet consequence.   |
| **Localized night coordination**  | Firefly Family         | One bounded route or Place becomes usable in darkness.       |
| **Seasonal preparation**          | Groundhog              | The family of an approaching pressure becomes known.         |
| **Protected reserve / receiving** | Turtle                 | One selected stake can be held safely.                       |
| **Cultivated continuity**         | Bumblebee Household    | Exceptional flowering life may persist in the Colony.        |
| **Subsurface structure**          | Mole                   | Hidden ground failure becomes diagnosable.                   |
| **High enclosed structure**       | Bat                    | Dry-dark decay becomes legible before failure.               |
| **External relationship**         | Pigeon                 | Send Word or Ask the Flock becomes possible.                 |
| **Nonlethal boundary defense**    | Skunk                  | A threat may be deterred with a local aftermath.             |
| **Contaminated aftermath**        | Opossum                | Broad contamination becomes contained reception and cleanup. |

<!--@20.3-->
## 20.3 Why Resident Guests are not lesser

<!--@20.3¶1-->
Expedition utility is concentrated in selected journeys and creates a visible Home absence. Resident utility is stable in Home life and changes warning, coordination, preservation, receiving, diagnosis, cultivation, defense, or relationship whenever the relevant situation occurs. The Resident package also carries a fixed civic Role, a distinctive House, EMBODY, vulnerability, and deeper domestic continuity. The two types answer different strategic questions rather than sharing one linear value scale.

<!--@22-->
# 21\. Carry-Forward and Supersession Ledger

<!--@22¶1-->
| **Earlier proposition**                           | **v0.5 disposition**               | **Leading replacement**                                                                       |
| ------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------- |
| **Active / Ambient Guests**                       | Renamed and reframed               | Expedition / Resident; neither type is socially lesser.                                       |
| **Separate capped slot pools**                    | Superseded as primary presentation | Physical Houses, Load, Residence, and civic integration express Hospitality Capacity.         |
| **Ambient passive buffs**                         | Superseded                         | Situated Resident Affordances and one fixed Role Capacity.                                    |
| **Every Guest freely assigned to any Role**       | Revised for Residents              | Resident species use fixed Guest Practices; Expedition Home Roles remain individual-authored. |
| **One biological body always equals one Citizen** | Two explicit exceptions            | Firefly Family and Bumblebee Household are collective-bodied Citizen subjects.                |
| **Bee increases Garden yield / diagnoses plots**  | Superseded                         | One global Gardener Capacity plus Carry the Bloom; no per-Garden simulation.                  |
| **Firefly extends work hours**                    | Superseded                         | Lantern Procession illuminates one bounded route or Place.                                    |
| **Accommodation consumed on departure or death**  | Superseded                         | Vacant Guest House persists as Place, absence, memorial, or adaptation.                       |
| **Outpost Guest residence**                       | Superseded                         | Outposts remain Away Stopovers and do not support DWELL or EMBODY.                            |
| **Guest recruitment by amenability roll**         | Superseded                         | First MEET, recognition, Terms, Project, and Arrival Homecoming.                              |
| **Guest rarity / power cost**                     | Superseded                         | Actual material complexity, placement, access, support, and Load.                             |
| **Roster completion as progression**              | Rejected                           | Optional hospitality; no-Guest play and refusal remain valid.                                 |

<!--@23-->
# 22\. Authoring Requirements, Open Questions, and Acceptance Tests

<!--@22.1-->
## 22.1 Required content fields for every Guest

<!--@22.1¶1-->
| **Field**                | **Requirement**                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Identity**             | Given or household name, species, silhouette, communication register, and character thesis.            |
| **Type**                 | Expedition or Resident, selected for play-experience reasons rather than social worth.                 |
| **Citizen form**         | Individual or one of the two authorized collective-bodied households.                                  |
| **First MEET**           | A circumstance in which the animal exists for its own reasons before recruitment is discussed.         |
| **Terms of Hospitality** | Concrete visible residence condition tied to body, place, safety, habit, or relationship.              |
| **Guest House**          | Mouse, Rabbit, and Squirrel translations; placement needs; folk naming direction.                      |
| **Home life**            | Role Practice, routine, House use, absence consequence, relationships, and Home MEET hooks.            |
| **Signature**            | Permission or Affordance with attribution, situation, limit, and suspension conditions.                |
| **Away package**         | For Expedition Guests: Permission family, Affinity, Independent Impulse, and shared-system exceptions. |
| **EMBODY**               | At least one meaningful Presence concept and Practice / Flow where appropriate.                        |
| **Memory**               | Arrival, relationship, injury, departure, House history, loss, and Chronicle language.                 |

<!--@22.2-->
## 22.2 Open tuning questions

<!--@22.2¶1-->
  - Exact encounter frequency and campaign-level availability of each example Citizen.

<!--@22.2¶2-->
  - Whether any implementation safety ceiling beyond physical Hospitality Capacity is necessary, and how completely it remains hidden.

<!--@22.2¶3-->
  - How seasonal inactivity for Snake, Bat, Firefly, Bee, and Groundhog affects Role Capacity without making the Guest punitive.

<!--@22.2¶4-->
  - Which Expedition life changes justify a permanent transition into Resident classification.

<!--@22.2¶5-->
  - How much individual variation a species template permits before its Signature identity becomes unreadable.

<!--@22.2¶6-->
  - How collective household loss and generational continuity are presented without introducing a separate reproduction subsystem.

<!--@22.2¶7-->
  - Whether any Resident Guest may receive an After-name after exceptional Home history, and how rare that exception remains.

<!--@22.3-->
## 22.3 Non-goals

<!--@22.3¶1-->
  - A full civilization grammar, population tree, or placement verb for every Guest species.

<!--@22.3¶2-->
  - A separate Guest Register, action economy, Exposure track, or bespoke Away minigame.

<!--@22.3¶3-->
  - Passive buff stacking, optimal Guest loadouts, or rarity tiers.

<!--@22.3¶4-->
  - A trust bar, random loyalty check, or recruitment minigame.

<!--@22.3¶5-->
  - Resident Guests treated as immortal furniture or weaker characters.

<!--@22.3¶6-->
  - Underground Guest settlements hidden from play.

<!--@22.3¶7-->
  - Per-Garden Bee routing, per-light Firefly control, or raw-body census management.

<!--@22.3¶8-->
  - Collectible-animal completion as the emotional purpose of the roster.

<!--@22.4-->
## 22.4 Acceptance tests

<!--@22.4¶1-->
| **Test**                      | **Pass condition**                                                                                                     |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Equality test**             | The interface and prose describe a recruited Guest as a Citizen by name, never as a pet, asset, follower, or bonus.    |
| **Two-type test**             | A Resident feels mechanically complete without Away eligibility; an Expedition Guest uses shared Away rules.           |
| **Capacity test**             | Every present adult Guest contributes exactly one Home Role Capacity and no personal Home aptitude modifier.           |
| **Equivalent-not-equal test** | Every species has a strategically legible Signature, but Signatures need not share frequency, magnitude, or form.      |
| **Resident utility test**     | The player can state a concrete Home reason to welcome each Resident before relying on charm or story alone.           |
| **Role-balance test**         | The Resident roster contains no more than two Watchkeepers and two Caretakers and retains the documented distribution. |
| **Collective-body test**      | Only Firefly Family and Bumblebee Household count several visible bodies as one Citizen subject.                       |
| **Global-role test**          | Bee and other Role contributions remain global; no site-by-site worker or pollination micromanagement appears.         |
| **Affordance test**           | A Resident Signature opens or changes a situated response rather than adding a general percentage modifier.            |
| **Permission test**           | An Expedition Signature opens one bounded option and does not solve the entire encounter.                              |
| **Double-fit test**           | Every Guest House is recognizably shaped by both host grammar and occupant body.                                       |
| **Launch test**               | Taking an Expedition Guest Away creates visible named absence and a legible Home consequence.                          |
| **Recruitment test**          | The player can describe the relationship and accommodation that led to arrival, not merely a price or roll.            |
| **EMBODY test**               | Every Guest has at least one emotionally meaningful Home-scale embodied experience.                                    |
| **Memory test**               | Departure, injury, death, collective thinning, and vacant Houses remain part of visible Colony history.                |
| **Anti-collection test**      | The system remains satisfying without completion percentages, rarity tiers, or recruiting every species.               |
| **No-Guest test**             | The main campaign remains fully viable when the player recruits no Guests.                                             |

<!--@24-->
# Final System Statement

<!--@24¶1-->
Guest Citizens are how MEDIAN turns ecological variety into hospitality and hospitality into attachment. The Core species defines the Colony's civilizational shape. A Guest arrives with another body, another way of reading the world, and another set of needs. The Colony learns those needs, builds a visible Place for them, accepts the opportunity cost of their presence, and eventually experiences their ordinary life through DWELL, MEET, Memory, and EMBODY.

<!--@24¶2-->
The two-type architecture keeps that promise tractable. Expedition Guests become individually consequential through shared Away systems and one bounded Permission. Resident Guests remain fully realized at Home through one fixed civic Practice and one qualitative Affordance. Firefly and Bee demonstrate that a Citizen subject may occasionally be a known household rather than one body, while every other roster entry remains a particular individual.

<!--@24¶3-->
<table>
<tbody>
<tr class="odd">
<td><strong>CANONICAL CLOSE<br />
</strong>Expedition Guests give the party another way to meet the world. Resident Guests give the Colony another way to understand, protect, receive, and remember it. Neither type is a module. Both are friends the Colony has made room to know.</td>
</tr>
</tbody>
</table>

<!--@24¶4-->
END OF SPECIFICATION
