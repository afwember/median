<!--@0¶1-->
MEDIAN v0.5.0

<!--@0¶2-->
POPULATION, GROWTH & COLONY TIERS

<!--@0¶3-->
NAMED CITIZENS, CONTINUITY, AND CIVIC MATURITY

<!--@0¶4-->
<table>
<tbody>
<tr class="odd">
<td><strong>CANONICAL PREMISE<br />
</strong>Population is the Colony's finite civic body, not a workforce score. Growth introduces named lives, new obligations, and new capacities. A Colony Tier records what scale of ordinary life the settlement can credibly sustain - not how many units the player has manufactured.</td>
</tr>
</tbody>
</table>

<!--@0¶5-->
SYSTEM ARCHITECTURE SPECIFICATION • VERSION 1.0 • 30 JULY 2026

<!--@0¶6-->
Target: MEDIAN v0.5.0 Concept Sourcebook / desktop-console manifestation

<!--@1-->
# 0\. Revision Summary

<!--@1.1-->
## Contents

<!--@1.1¶1-->
1\. Purpose, Source, and Precedence

<!--@1.1¶2-->
2\. Executive Summary and Canonical Population Doctrine

<!--@1.1¶3-->
3\. Population Units, Counts, and Presence States

<!--@1.1¶4-->
4\. Scale, Species Density, and Target Population Bands

<!--@1.1¶5-->
5\. Population Capacity, Residence, Load, and Overcrowding

<!--@1.1¶6-->
6\. The Three Growth Paths

<!--@1.1¶7-->
7\. Wanderers: Early Adult Growth

<!--@1.1¶8-->
8\. Hearths, the Nursery, and Nesting Season

<!--@1.1¶9-->
9\. Young Citizens, Dependence, and Maturity

<!--@1.1¶10-->
10\. Guest Citizens as Population Growth

<!--@1.1¶11-->
11\. Loss, Absence, Departure, and Memorial Continuity

<!--@1.1¶12-->
12\. Colony Tier Architecture

<!--@1.1¶13-->
13\. Tier I - Scavenger Camp

<!--@1.1¶14-->
14\. Tier II - Fortified Settlement

<!--@1.1¶15-->
15\. Tier III - Independent Colony

<!--@1.1¶16-->
16\. Tier IV - Sovereign Network

<!--@1.1¶17-->
17\. Tier Advancement Proofs and Graduation

<!--@1.1¶18-->
18\. Tier Retention, Stable Plateaus, and Post-Climax Growth

<!--@1.1¶19-->
19\. Interface and Information Requirements

<!--@1.1¶20-->
20\. Supersession Ledger, Open Questions, and Acceptance Tests

<!--@1.1¶21-->
Final System Statement

<!--@1.2-->
## Major v0.5 rulings

<!--@1.2¶1-->
  - Population is counted through named Citizen subjects. Away body-units do not replace the roster count.

<!--@1.2¶2-->
  - The player reads four distinct population facts: Colony Roster, Home Presence, Available Civic Population, and Dependents / Patients.

<!--@1.2¶3-->
  - Every present and available adult Citizen contributes one equal Home Role Capacity. Growth adds both capability and Load.

<!--@1.2¶4-->
  - A mature Colony remains a community of dozens, never hundreds. Mouse colonies are denser, not anonymous.

<!--@1.2¶5-->
  - Wanderers are the primary early adult-growth path. Nursery growth is rarer, seasonal, player-authorized, and emotionally weighted.

<!--@1.2¶6-->
  - The Nursery is a Residence-and-Care Place, not a population factory. There is no Nursery Tender Role or birth-production queue.

<!--@1.2¶7-->
  - Young Citizens count immediately as named population and obligation, but provide no Role Capacity until Maturity.

<!--@1.2¶8-->
  - Guest Citizens count fully toward population, Residence, Load, Role Capacity, and neutral Tier proofs. No Tier requires Guests.

<!--@1.2¶9-->
  - The four canonical Tier names are Scavenger Camp, Fortified Settlement, Independent Colony, and Sovereign Network.

<!--@1.2¶10-->
  - Tier advancement requires demonstrated civic maturity, not a giant resource payment or an Age-up button.

<!--@1.2¶11-->
  - Tier is retained after population loss. The Colony may become too small to carry its inherited institutions comfortably, but it does not forget what it became.

<!--@1.2¶12-->
  - Growth is optional. Tier III supports a long, stable campaign plateau; Tier IV does not begin infinite vertical scaling.

<!--@2-->
# 1\. Purpose, Source, and Precedence

<!--@2¶1-->
This specification defines the v0.5 population model, the three population-growth paths, the Nursery and young-Citizen lifecycle, and the four Colony Tiers. It replaces the older production-oriented idea that population is manufactured through a Nursery rate and then converted into scalable labor throughput.

<!--@2¶2-->
The document exists because population touches nearly every v0.5 system: global Home Roles, Residence Places, Load, Launch absence, Guest citizenship, Campaign Memory, Hearths, Homecoming, corridor expansion, and the player's ability to recognize every life in the Colony.

<!--@1.1#2-->
## 1.1 Precedence order

<!--@1.1#2¶1-->
| **Priority** | **Source**                           | **Use in this specification**                                                                                                                                  |
| ------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1**        | v0.5.0 Philosophical Specification   | Defines attachment-first base building, low-population stewardship, successful stillness, and the Home / Away growth split.                                    |
| **2**        | Home Mode, Colony, and DWELL Specification       | Defines equal Role Capacity, contextual Load, Quiet Equilibrium, Projects, and the Colony as the Home crunch subject.                                          |
| **3**        | Away Mode Specification              | Defines individual Citizen hazard, Launch subtraction, Homecoming, and the distinction between roster presence and Away participation.                         |
| **4**        | Guest Citizen Specification          | Defines full Guest citizenship, Role contribution, Hospitality Capacity, and optional recruitment.                                                             |
| **5**        | v0.4.7 Cross-System Attention, Persistence, and World-State Carryforward    | Defines Register / View doctrine, world-state ownership, and cross-system presentation rules.                                                                  |
| **6**        | GDD v0.4.6 and story-colony material | Historical source for Hearths, Wanderers, Nesting Season, the four Tier names, and low-population intent; superseded where this document states a v0.5 ruling. |

<!--@1.2#2-->
## 1.2 Canon status

<!--@1.2#2¶1-->
The structural rules in this document are canonical for v0.5. Numerical population bands and advancement thresholds are reference targets for sourcebook authoring and balance. They may move during implementation testing without changing the governing doctrine, provided the low-population ceiling and species-relative scale remain intact.

<!--@3-->
# 2\. Executive Summary and Canonical Population Doctrine

<!--@3¶1-->
MEDIAN is a low-population colony builder. The Colony is not a stream of replaceable workers but a finite set of named Citizens whose ordinary responsibilities, absences, injuries, relationships, births, arrivals, and deaths remain comprehensible.

<!--@3¶2-->
At Home, a present and available adult Citizen contributes one equal unit of Role Capacity. That equality does not make population growth automatically beneficial. Every new resident also requires a credible Place to live, consumes Sustenance, and may increase Caretaking, Stores, Watchkeeping, Teaching, Healing, Leadership, route, or structural Load. Population is therefore capability plus obligation.

<!--@3¶3-->
<table>
<tbody>
<tr class="odd">
<td><strong>GROWTH DOCTRINE<br />
</strong>A new adult may add one Capacity today. A young Citizen adds no Capacity yet. Both add a life the Colony must feed, shelter, teach, protect, and remember.</td>
</tr>
</tbody>
</table>

<!--@3¶4-->
Home grows the Colony: more inhabited Places, more civic commitments, more reserves, more relationships, and eventually a higher Tier. Away grows particular Citizens: equipment, wounds, Distinctions, fears, Tales, and After-names. Population growth belongs principally to Home and Homecoming, even when the first contact occurs Away.

<!--@2.1-->
## 2.1 Non-goals

<!--@2.1¶1-->
  - Hundreds of anonymous inhabitants or population represented primarily as labor throughput.

<!--@2.1¶2-->
  - A breeding optimizer, heredity system, bloodline ledger, genetics screen, or inherited aptitude.

<!--@2.1¶3-->
  - Automatic population growth driven by a percentage rate, idle timer, or Nursery upgrade ladder.

<!--@2.1¶4-->
  - Disposable replacement births intended to compensate for expedition losses.

<!--@2.1¶5-->
  - A single visible population-cap number that ignores housing form, Load, care, and seasonal support.

<!--@2.1¶6-->
  - Tier advancement as an RTS Age-up purchase, universal Citizen stat increase, or industrialization ladder.

<!--@2.1¶7-->
  - Mandatory Guest recruitment, specific species recruitment, or collection completion as progression.

<!--@4-->
# 3\. Population Units, Counts, and Presence States

<!--@3.1-->
## 3.1 The Citizen subject

<!--@3.1¶1-->
The roster counts Citizen subjects, not raw biological bodies and not Away body-units. For almost every Citizen, one subject is one named animal. An authored collective-bodied Guest household may exceptionally be treated as one Citizen subject when the group is the smallest living unit the Colony can meaningfully know; the detailed Guest roster defines those exceptions.

<!--@3.1¶2-->
Away body-units are a separate expedition abstraction. Several small Citizens may together occupy fewer Away body-units while remaining separately named, separately counted, and separately consequential at Home. A Mouse Colony with eight Citizens has eight Citizens even when a particular expedition assembles them into fewer body-units.

<!--@3.2-->
## 3.2 The four visible counts

<!--@3.2¶1-->
| **Count**                      | **Includes**                                                                                                      | **Primary player question**                                         |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Colony Roster**              | Every living named Citizen who belongs to the Colony: adults, young, Guests, Away parties, and outpost residents. | Who are all the lives for which this Colony is responsible?         |
| **Home Presence**              | Roster Citizens physically present at the Home Median.                                                            | Who is actually here today?                                         |
| **Available Civic Population** | Home-present adults currently able to hold Roles or commit Citizen-Days.                                          | How many civic shares can Home use now?                             |
| **Dependents / Patients**      | Young Citizens and present Citizens whose care state prevents ordinary Capacity.                                  | Who currently requires support without supplying ordinary Capacity? |

<!--@3.2¶2-->
The interface may show these counts together, but it must never collapse them into a single Workforce number. A Colony Roster of twelve might contain nine available adults, two young Citizens, and one recovering patient. That is a materially different Colony from twelve available adults.

<!--@3.3-->
## 3.3 Capacity is derived, not synonymous with population

<!--@3.3¶1-->
At Dawn, the Home Loop resolves presence and availability before Role Capacity. Each present and available adult assigned to a Role contributes one Capacity. A Citizen Away, stationed at an outpost, acutely injured, in intensive treatment, or otherwise unavailable remains on the Colony Roster but does not contribute current Home Capacity.

<!--@3.3¶2-->
Personal Away aptitude never changes Home contribution. Population growth does not create stronger or weaker workers. It creates another equal civic share that may be committed to one responsibility at a time.

<!--@5-->
# 4\. Scale, Species Density, and Target Population Bands

<!--@5¶1-->
The mature Colony is measured in dozens. It must become large enough to feel like a civilization and remain small enough that the player can still recognize a missing name, an empty House, or a changed relationship without consulting an anonymous demographic chart.

<!--@5¶2-->
Wood Mouse colonies are denser than Rabbit or Squirrel colonies - approximately one-and-a-half to two times the mature headcount at comparable Tier - but remain within the same fully named design ceiling. The difference is density, not reduced personhood.

<!--@4.1-->
## 4.1 Reference population bands

<!--@4.1¶1-->
| **Colony Tier**                    | **Rabbit / Squirrel roster** | **Wood Mouse roster** | **Typical Guests housed\*** |
| ---------------------------------- | ---------------------------- | --------------------- | --------------------------- |
| **Tier I - Scavenger Camp**        | 3-6                          | 3-8                   | 0-1                         |
| **Tier II - Fortified Settlement** | 7-11                         | 9-15                  | 1-2                         |
| **Tier III - Independent Colony**  | 12-17                        | 16-25                 | 2-3                         |
| **Tier IV - Sovereign Network**    | 18-24                        | 26-36                 | 3-5                         |

<!--@4.1¶2-->
\*Guest values are expectations, not slots, quotas, or requirements. A no-Guest Colony is valid at every Tier.

<!--@4.1¶3-->
These ranges serve four purposes: encounter authoring, concept-art population density, Residence and Load tuning, and Tier-readiness reference. The upper edge is not displayed as an arbitrary law of nature. The settlement communicates its limits through inhabited space, stores, routes, care, and readiness.

<!--@4.2-->
## 4.2 Reference advancement thresholds

<!--@4.2¶1-->
| **Graduation**           | **Rabbit / Squirrel population proof** | **Wood Mouse population proof** | **Status**          |
| ------------------------ | -------------------------------------- | ------------------------------- | ------------------- |
| **Tier I -\> Tier II**   | 7 named Citizens                       | 9 named Citizens                | Reference threshold |
| **Tier II -\> Tier III** | 12 named Citizens                      | 16 named Citizens               | Reference threshold |
| **Tier III -\> Tier IV** | 18 named Citizens                      | 26 named Citizens               | Reference threshold |

<!--@4.2¶2-->
Population proof is necessary but never sufficient. Reaching the threshold while housing is unsafe, ordinary Roles are broadly Thin, winter stores are inadequate, or the Colony cannot spare an expedition does not constitute civic maturity.

<!--@6-->
# 5\. Population Capacity, Residence, Load, and Overcrowding

<!--@5.1-->
## 5.1 No single abstract population cap

<!--@5.1¶1-->
Population support is distributed across the Colony rather than stored in one Town Center statistic. A resident needs a credible Residence Place or household accommodation, ordinary Sustenance, safe access, and a civic posture capable of absorbing the new Load.

<!--@5.1¶2-->
The UI may display Residence occupancy - for example, 10 of 12 credible sleeping places - but that number is only one constraint. Two unused beds do not make a Nesting commitment responsible if Caretaking and Stores are already Thin. Conversely, a strong Colony may temporarily shelter a Wanderer before permanent Residence is complete.

<!--@5.2-->
## 5.2 Growth changes both sides of the Home equation

<!--@5.2¶1-->
| **Arrival state**             | **Immediate Capacity**                                          | **Immediate Load and obligation**                                                                   |
| ----------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Healthy adult Wanderer**    | \+1 Role Capacity when integrated and available                 | Residence, Sustenance, newcomer integration, and possible new threshold Load.                       |
| **Young Citizen**             | 0 until Maturity                                                | Residence, Sustenance, Caretaking, Teaching, protection, and possible Healing.                      |
| **Adult Guest Citizen**       | \+1 fixed or ordinary Role Capacity while present and available | Guest House, Sustenance, Hospitality commitment, species-specific accommodation, and ordinary Load. |
| **Returning injured Citizen** | Usually 0 while a Patient                                       | Healing, Caretaking, treatment space, and reduced Home flexibility.                                 |

<!--@5.2¶2-->
Places can reduce a specific contextual Load, protect a Capacity from disruption, or make a response cheaper, but headcount provides the heavy civic lifting. Growth should therefore be previewed as a whole-colony posture change rather than advertised as a free worker gain.

<!--@5.3-->
## 5.3 Temporary overcrowding

<!--@5.3¶1-->
Emergency hospitality may exceed normal Residence comfort. A Wanderer can be accepted into provisional shelter, producing a visible Overcrowded or Provisional Shelter Condition and appropriate Load. This permits morally and narratively meaningful refuge without turning housing into an invisible hard gate.

<!--@5.3¶2-->
Planned growth is stricter. The Colony may not authorize a Nesting commitment without credible future habitation. A Guest Arrival does not complete until the promised Guest House exists. Temporary refuge and permanent welcome are different civic acts.

<!--@7-->
# 6\. The Three Growth Paths

<!--@7¶1-->
A Colony grows through three distinct channels. Each supplies a different relationship to time, risk, and belonging. They are not interchangeable buttons that merely add one to Population.

<!--@7¶2-->
| **Growth path**       | **Who joins**                     | **Timing**                            | **Capacity profile**                               | **Primary meaning**                                               |
| --------------------- | --------------------------------- | ------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------- |
| **Wanderer**          | Core-species named adult          | Opportunistic; most common early      | Capacity can arrive quickly after integration      | Refuge, adoption, displacement, survival beyond the Founding trio |
| **Nursery / Nesting** | Core-species named young          | Rare seasonal commitment              | Load arrives before Capacity                       | Continuity, lineage as story, later generations                   |
| **Guest recruitment** | Named non-Core adult or household | Rare relationship and hospitality arc | Adult Capacity plus qualitative species Affordance | Hospitality, difference, found family                             |

<!--@7¶3-->
<table>
<tbody>
<tr class="odd">
<td><strong>PACING RULE<br />
</strong>Wanderers establish the early civic body. Nesting makes the future. Guests make this Colony historically particular.</td>
</tr>
</tbody>
</table>

<!--@8-->
# 7\. Wanderers: Early Adult Growth

<!--@8¶1-->
A founding trio plus rare seasonal young produces too slow a curve for the Home system. Displaced same-species Wanderers are therefore the primary early-game source of adult population growth. A Wanderer is an ordinary Core Citizen from the moment of acceptance - never a Guest, recruitable unit, or subordinate refugee class.

<!--@7.1-->
## 7.1 Arrival routes

<!--@7.1¶1-->
| **Route**           | **System entry**                                                                                                  | **Typical dramatic question**                                                         |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Away encounter**  | A named non-antagonist or contested outsider appears during TRAVEL or MEET.                                       | Will the party recognize, assist, or invite this animal before everyone returns Home? |
| **Rescue**          | The party or Colony encounters a Citizen endangered by traffic, Road Work, weather, predator pressure, or injury. | What must be risked or left behind to bring them through?                             |
| **Arrival at Home** | A Home-origin MEET begins at the Colony edge.                                                                     | Can the Colony offer refuge now, and what becomes Thin if it does?                    |

<!--@7.2-->
## 7.2 Wanderer MEET and acceptance

<!--@7.2¶1-->
Wanderer arrival resolves through MEET rather than an amenability roll. The player may accept permanent citizenship, offer temporary refuge while preparing Residence, help the Wanderer continue toward another destination, or refuse. The available choices and costs depend on the actual circumstance.

<!--@7.2¶2-->
Refusal is allowed because growth must remain voluntary, but refusal becomes history. A Wanderer turned away may reach another settlement, return under worse conditions, carry the Colony's reputation, or be lost. The game does not convert every refusal into moral punishment, nor does it erase the act.

<!--@7.3-->
## 7.3 What arrives with a Wanderer

<!--@7.3¶1-->
  - A Given Name and complete Citizen Record.

<!--@7.3¶2-->
  - A life-stage and personality description, without inherited or efficiency statistics.

<!--@7.3¶3-->
  - A Tale explaining why this animal was alone or displaced.

<!--@7.3¶4-->
  - Possible injury, fear memory, relationship, Promise, knowledge, or unfinished circumstance.

<!--@7.3¶5-->
  - Full equal standing after acceptance and integration.

<!--@7.3¶6-->
The flagship authored case remains another survivor of the Founding Escape, encountered after the founding trio has already built a shared story around believing they alone survived. Wanderers can therefore revise the Colony's understanding of its own past, not merely its labor count.

<!--@7.4-->
## 7.4 Campaign cadence

<!--@7.4¶1-->
Wanderers are commonest in Tiers I and II, when the corridor still contains displaced animals and the Colony needs adults quickly. At Tier III, arrivals become less frequent and more narratively specific. At Tier IV, a Wanderer is usually a relationship between the Sovereign Network and the wider corridor rather than routine demographic delivery.

<!--@9-->
# 8\. Hearths, the Nursery, and Nesting Season

<!--@8.1-->
## 8.1 Hearth as lineage unit

<!--@8.1¶1-->
A Hearth is a named Core-species family unit. It may grow from Trusted Friendship and may include more than a breeding pair: an orphaned young Citizen, a maimed veteran, or another member taken into the household. Hearth is a social and narrative fact, not a heredity mechanic.

<!--@8.1¶2-->
A young Citizen's Tale records descent from a Hearth. Nothing mechanical is inherited. There is no bloodline score, genetic trait transmission, aptitude breeding, family-tech tree, or optimization reason to prefer one Hearth over another.

<!--@8.2-->
## 8.2 The Nursery is a Place, not a factory

<!--@8.2¶1-->
The Nursery is a Residence-and-Care Place supporting a Nesting Practice. It does not generate population by rate, contain a production queue, or improve births-per-season through upgrades. The former Nursery Tender profession is superseded; care is expressed through existing Roles and contextual Load.

<!--@8.2¶2-->
Multiple Nursery Places may improve safety, provide species-appropriate placement, reduce crowding, or give redundant evacuation paths. They do not multiply the number of seasonal births. The pacing unit is the Colony-wide Nesting commitment, not building throughput.

<!--@8.3-->
## 8.3 Nesting Season sequence

<!--@8.3¶1-->
| **Phase**                 | **System event**                                                                                   | **Player-facing consequence**                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **1. Season opens**       | Suitable seasonal and Colony conditions permit a Nesting commitment.                               | The option becomes available; nothing happens automatically.                 |
| **2. Hearth willingness** | An eligible Hearth expresses readiness.                                                            | The game names the household; the player does not pair anonymous breeders.   |
| **3. Capacity review**    | Residence, Stores, Caretaking, Healing, Teaching, Leadership, and seasonal forecast are previewed. | The player sees what will become Thin and which adults lose flexibility.     |
| **4. Authorization**      | The player begins a long civic commitment.                                                         | This is closer to authorizing a consequential Project than producing a unit. |
| **5. Critical period**    | The Hearth is protected from ordinary Away use and may lose flexible Home availability.            | The exact temporary cost is visible before commitment.                       |
| **6. Naming**             | A very small number of young enter the Roster and receive Given Names.                             | Population and Load rise immediately; Capacity does not.                     |

<!--@8.4-->
## 8.4 Default stylized outcome

<!--@8.4¶1-->
| **Core civilization** | **Default successful Nesting outcome** | **Design reason**                                                                         |
| --------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Rabbit**            | One named young Citizen                | Preserves rarity, individual attachment, and campaign pacing.                             |
| **Squirrel**          | One named young Citizen                | Preserves rarity, individual attachment, and campaign pacing.                             |
| **Wood Mouse**        | Two named littermates                  | Expresses denser Mouse population without simulating large litters or creating anonymity. |

<!--@8.4¶2-->
This is a sourcebook and balance rule, not a literal claim about animal biology. Exact biology is stylized consistently to protect the low-population design ceiling. Normally only one successful Nesting commitment resolves per Colony-wide seasonal window.

<!--@10-->
# 9\. Young Citizens, Dependence, and Maturity

<!--@9.1-->
## 9.1 Immediate status

<!--@9.1¶1-->
A young Citizen is fully named and fully counted from arrival. They receive a Citizen Record, relationships, a Residence association, and Campaign Memory. They may be present in DWELL, Home MEET, Story Circle life, and eligible forms of Home-only EMBODY. They are not an inventory item waiting to become a real character.

<!--@9.1¶2-->
Young Citizens provide no ordinary Role Capacity and may not Launch. They add Dependence Load first: Caretaking, Teaching, Sustenance, Residence, protection, and occasionally Healing or Leadership. Nursery growth therefore tests whether the Colony has actual margin rather than creating the labor needed to cover its own cost.

<!--@9.2-->
## 9.2 Maturity

<!--@9.2¶1-->
Maturity is a named campaign transition rather than a visible experience bar. After an appropriate number of seasons and authored life events, the Citizen enters adult civic standing, contributes one Role Capacity, and may later become eligible for Launch. Exact duration is a balance and story-pacing value, not a biological simulation.

<!--@9.2¶2-->
The Maturity event should enter the Tale and may be marked at the Story Circle or another species-appropriate Place. The game may distinguish civic maturity from immediate expedition readiness, but it must not create a stat-training ladder or Teacher-speed percentage.

<!--@9.3-->
## 9.3 Young Citizens are not replacement stock

<!--@9.3¶1-->
The Nursery must never be framed as the answer to death. A loss may make the future feel more urgent, but the game does not encourage the player to replace a named casualty with a new birth. The Colony remembers the dead, raises the young as particular people, and accepts that continuity is not equivalence.

<!--@11-->
# 10\. Guest Citizens as Population Growth

<!--@11¶1-->
Guest recruitment increases the actual Colony population. Guest is an origin and content category, not a separate demographic caste. Once welcomed, a Guest occupies a real House, consumes ordinary support, contributes one Role Capacity while present and available, participates in Home danger, and counts toward neutral Tier population and stability proofs.

<!--@11¶2-->
Guests differ from Wanderers and Nursery young because they do not extend the Core species lineage. They extend Colony membership. Their qualitative species Affordance and specialized House make the Colony more particular, but they remain equal Citizens rather than bonus modules.

<!--@10.1-->
## 10.1 Guest counting rules

<!--@10.1¶1-->
  - One named individual Guest normally counts as one Citizen subject.

<!--@10.1¶2-->
  - An explicitly authored collective-bodied Guest household counts as one Citizen subject and one civic share.

<!--@10.1¶3-->
  - An Expedition Guest Away remains on the Colony Roster but leaves Home Presence and Home Capacity.

<!--@10.1¶4-->
  - A Resident Guest is not discounted because they cannot Launch.

<!--@10.1¶5-->
  - A Guest House is Residence, not a slot socket; Hospitality Capacity is the Colony's credible ability to house and know Guests.

<!--@10.1¶6-->
  - No Tier, victory condition, or essential Home system requires a Guest or a particular species.

<!--@10.2-->
## 10.2 Population proof and optionality

<!--@10.2¶1-->
If a Tier requires twelve named Citizens, a Colony of nine Core Citizens and three Guests satisfies the population proof. Excluding Guests would quietly deny their equal standing. The other advancement proofs still apply: the Colony must actually sustain those lives and remain stable.

<!--@10.2¶2-->
The typical Guest counts in the Tier table are authoring expectations only. A Tier IV Colony with no Guests is valid. A Tier IV Colony with four Guests should feel unusually cosmopolitan, not incomplete because the roster contains more possible species.

<!--@12-->
# 11\. Loss, Absence, Departure, and Memorial Continuity

<!--@11.1-->
## 11.1 Presence changes without roster deletion

<!--@11.1¶1-->
| **State change**        | **Roster effect**                        | **Home effect**                                                   |
| ----------------------- | ---------------------------------------- | ----------------------------------------------------------------- |
| **Launch**              | No change                                | Citizen leaves Home Presence and Role Capacity until return.      |
| **Outpost stationing**  | No change                                | Citizen remains part of the Colony but is not Home-present.       |
| **Injury / treatment**  | No change                                | Citizen may move from Available Civic Population to Patient.      |
| **Young Citizen born**  | \+1 or +2 named Citizens by species rule | Dependents rise; no new Capacity yet.                             |
| **Permanent departure** | \-1 living Roster                        | House and relationships retain memory; Tale remains historical.   |
| **Death**               | \-1 living Roster                        | Citizen Record moves to memorial continuity rather than deletion. |

<!--@11.2-->
## 11.2 Population loss is not routine attrition

<!--@11.2¶1-->
Death is possible but uncommon outside catastrophic error or extreme circumstance. Ordinary expeditions are dangerous because particular Citizens may return changed, not because a stable population-loss percentage is expected. The growth system must not be tuned around replacing routine casualties.

<!--@11.2¶2-->
When a Citizen dies, the Tale closes but remains readable. Relationships, Keepsakes, memorials, empty Places, and future references preserve continuity. The Colony Roster decreases; the Colony's history does not.

<!--@13-->
# 12\. Colony Tier Architecture

<!--@13¶1-->
The four Tiers express increasing security, spatial reach, institutional capability, ecological integration, and the credible scale of ordinary life. They do not describe technological Ages, industrial output, military dominance, or a march toward human-style empire.

<!--@13¶2-->
| **Tier**                      | **Core fantasy**                                                    | **Population meaning**                                                                         | **Range meaning**                                              |
| ----------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **I - Scavenger Camp**        | A vulnerable settlement proves it can survive.                      | A founding group becomes a functioning household and small civic body.                         | Home Median and adjacent Margins.                              |
| **II - Fortified Settlement** | The Colony prepares rather than merely reacts.                      | Enough adults exist to distribute responsibility and sustain recovery.                         | First longitudinal scouts and a nearby outpost.                |
| **III - Independent Colony**  | A mature home can endure without external rescue.                   | The roster supports stable institutions, later generations, and meaningful expedition absence. | Multiple outposts and deeper Reaches.                          |
| **IV - Sovereign Network**    | Home becomes the protected heart of a connected corridor community. | The Colony can sustain legacy, hospitality, and a wider civic network without anonymity.       | A durable chain toward the Metropolis and other distant sites. |

<!--@13¶3-->
<table>
<tbody>
<tr class="odd">
<td><strong>TIER DOCTRINE<br />
</strong>A Tier records what the Colony has proved it can carry. It does not grant worth to the lives already there.</td>
</tr>
</tbody>
</table>

<!--@12.1-->
## 12.1 What Tier unlocks

<!--@12.1¶1-->
  - New Residence and Practice Place families appropriate to the Colony's growing responsibilities.

<!--@12.1¶2-->
  - Larger civic Projects and stronger expressions of JOIN, GATHER, or CONNECT.

<!--@12.1¶3-->
  - More durable preservation, recovery, warning, access, and seasonal preparation.

<!--@12.1¶4-->
  - Deeper corridor reach, outpost capability, and more demanding expedition choices.

<!--@12.1¶5-->
  - New institutional decisions, ceremonies, records, and ways to support later generations.

<!--@12.1¶6-->
  - A larger but still fully named supported-population band.

<!--@12.2-->
## 12.2 What Tier does not unlock automatically

<!--@12.2¶1-->
  - A universal stat increase for every Citizen.

<!--@12.2¶2-->
  - A fixed Guest slot or required Guest category.

<!--@12.2¶3-->
  - A new population-production rate.

<!--@12.2¶4-->
  - A queue slot as the principal reward for civic maturity.

<!--@12.2¶5-->
  - Free Role Capacity, abstract efficiency, or a percentage productivity bonus.

<!--@12.2¶6-->
  - Electrification, factory production, military escalation, or an empire aesthetic.

<!--@14-->
# 13\. Tier I - Scavenger Camp

<!--@14¶1-->
Tier I begins with the Founding survivors, normally three named adolescents or young adults. They possess a Home site but not yet a proven home. Population choices are stark because every absence can remove a third of the civic body.

<!--@14¶2-->
| **Dimension**         | **Tier I expression**                                                                                                               |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Population band**   | Rabbit / Squirrel 3-6; Wood Mouse 3-8.                                                                                              |
| **Growth emphasis**   | Wanderers. Nesting may become possible late in the Tier only after credible Residence and care exist.                               |
| **Home capability**   | Basic shelter, Stores, simple repair, the first stable Role posture, and the ability to survive a short absence.                    |
| **Away capability**   | Adjacent Margin work and first expeditions; corridor remains largely unknown.                                                       |
| **Primary pressures** | Fragile construction, scarce Scrap, limited redundancy, fear, and the inability to cover every responsibility at once.              |
| **Graduation proof**  | The settlement can house the larger roster, maintain ordinary coverage, and send a small party without immediate domestic collapse. |

<!--@15-->
# 14\. Tier II - Fortified Settlement

<!--@15¶1-->
Tier II is organized enough to prepare. The Colony has sufficient headcount to distribute responsibilities, maintain fallback routes, receive an injured Citizen, and make deliberate seasonal choices rather than living entirely from one emergency to the next.

<!--@15¶2-->
| **Dimension**         | **Tier II expression**                                                                                                                               |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Population band**   | Rabbit / Squirrel 7-11; Wood Mouse 9-15.                                                                                                             |
| **Growth emphasis**   | Wanderers remain important; the first emotionally significant Nursery cycle often occurs here; Guest hospitality becomes credible where encountered. |
| **Home capability**   | Stronger Residence, recovery space, preservation, route redundancy, and a dependable Story Circle / Council life.                                    |
| **Away capability**   | First longitudinal scouts, one nearby outpost, and regular planned Margin expeditions.                                                               |
| **Primary pressures** | Seasonal preparation, maintaining the first external network, contested sites, and the new Load created by young or Guests.                          |
| **Graduation proof**  | The Colony can sustain a full seasonal cycle, support a larger named population, and complete a defining civic Project.                              |

<!--@16-->
# 15\. Tier III - Independent Colony

<!--@16¶1-->
Tier III is the core mature-game plateau. The Colony is self-governing, can endure without external rescue, can absorb ordinary expedition absence, and has enough institutional depth for later generations, Guests, veteran care, and ambitious Projects without turning every day into emergency triage.

<!--@16¶2-->
| **Dimension**         | **Tier III expression**                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Population band**   | Rabbit / Squirrel 12-17; Wood Mouse 16-25.                                                                                                                             |
| **Growth emphasis**   | Growth becomes a choice rather than an urgent need. Wanderers are rarer; Nesting and hospitality express continuity and identity.                                      |
| **Home capability**   | Durable anchored construction, stable preservation, meaningful recovery, mature species topology, and credible Quiet Equilibrium.                                      |
| **Away capability**   | Multiple outposts, deeper Reaches, larger expedition choices, and sustained corridor relationships.                                                                    |
| **Primary pressures** | Regional obligations, Road Work at several nodes, legacy decisions, and the opportunity cost of maintaining a wider network.                                           |
| **Graduation proof**  | The Colony proves continuity beyond survival: stable institutions, spare expedition capacity, and a route or relationship achievement aimed toward the wider corridor. |

<!--@16¶3-->
Tier III must remain satisfying indefinitely. A player who prefers one mature, remembered Colony should not be forced toward Tier IV merely to keep systems functional or content available.

<!--@17-->
# 16\. Tier IV - Sovereign Network

<!--@17¶1-->
Tier IV does not turn the Colony into a tiny empire. Sovereignty means that Home is secure enough to become the remembered heart of a connected corridor community. Mastery is expressed through ecological invisibility, resilient routes, social relationships, and intelligent use of overlooked infrastructure.

<!--@17¶2-->
| **Dimension**          | **Tier IV expression**                                                                                                                 |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Population band**    | Rabbit / Squirrel 18-24; Wood Mouse 26-36.                                                                                             |
| **Growth emphasis**    | Growth is selective. The question is whom the Colony can responsibly welcome and what legacy later generations inherit.                |
| **Home capability**    | Major civic works, resilient dead-zone sanctuary spaces, mature preservation and care, and the ability to carry institutional history. |
| **Away capability**    | A durable outpost chain, distant relationships, trade and intelligence, and Grand Caravan or equivalent corridor proof.                |
| **Primary pressures**  | Protecting legacy, maintaining a network without hollowing Home, and deciding what the Colony will become after connection.            |
| **Completion meaning** | Tier IV supports the campaign climax and continuation; it is not the beginning of endless vertical scaling.                            |

<!--@18-->
# 17\. Tier Advancement Proofs and Graduation

<!--@18¶1-->
Tier advancement is a recognition event. Population supplies one proof, but the Colony must also demonstrate that it can sustain the scale it claims. The defining advancement costs should live inside visible civic Projects and preparations, not in a detached resource sacrifice.

<!--@17.1-->
## 17.1 The six proofs

<!--@17.1¶1-->
| **Proof**          | **What the Colony demonstrates**                                                      | **Typical evidence**                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Population**     | The living Roster has entered the next reference band.                                | Named Citizens, not anonymous housing capacity.                                                               |
| **Equilibrium**    | Ordinary Role posture can remain Covered for a meaningful interval.                   | No broad chronic Deficiency; acute MEET resolved.                                                             |
| **Seasonal**       | Shelter, Stores, care, and routes survive an appropriate seasonal challenge.          | Winter, flood, heat, wind, or comparable ecological proof.                                                    |
| **Civic**          | A defining Home Project materially changes the settlement.                            | Residence expansion, route redundancy, preservation, Council Place, recovery, or major species-topology work. |
| **Away / Network** | The Colony has achieved the relevant external reach.                                  | Margin mastery, walked Reach, outpost, relationship, Special Journey, or corridor connection.                 |
| **Continuity**     | The Colony can permit selected Citizens to leave without automatic domestic collapse. | Launch preview shows accepted risk rather than guaranteed failure.                                            |

<!--@17.2-->
## 17.2 Graduation event

<!--@17.2¶1-->
Once all proofs are satisfied, advancement becomes a Council-centered Home MEET or civic ceremony. The Colony does not press an Age-up button. It recognizes what has become true: it can preserve its stores, receive its wounded, teach its young, send a party, and remain a home.

<!--@17.2¶2-->
Graduation should visibly transform Home and unlock at least one new kind of decision. Exact Scrap, Artifact, knowledge, or relationship requirements may support a specific defining Project, but the game must avoid arbitrary giant payments that do not appear in the world.

<!--@19-->
# 18\. Tier Retention, Stable Plateaus, and Post-Climax Growth

<!--@18.1-->
## 18.1 Tier is historical and institutional

<!--@18.1¶1-->
A Tier III Colony reduced from fourteen Citizens to ten remains an Independent Colony. It retains its Places, Records, routes, knowledge, laws, relationships, and accumulated construction. It may now be too small to cover all of that inheritance comfortably, but automatic downgrade would erase history and turn Tier into a volatile score.

<!--@18.1¶2-->
Population loss may force the player to close a Place, consolidate a court, suspend a route, seek Wanderers, or accept temporary Thinness. Those are meaningful consequences of carrying institutions with fewer hands.

<!--@18.2-->
## 18.2 Growth is optional

<!--@18.2¶1-->
The player may decide that the Colony is large enough. Eleven Rabbits, sixteen Squirrels, or twenty-three Mice can be a complete civic world if the settlement is stable, remembered, and capable of chosen ambition. The game must not create a universal pressure to fill every Residence or authorize every Nesting Season.

<!--@18.2¶2-->
Tier III is a valid long plateau. Tier IV is a particular corridor ambition, not the only successful shape of play. After the campaign climax, continued growth focuses on relationships, veteran care, ecological events, later generations, Guest hospitality, outpost refinement, and civic beauty - not infinite population or power scaling.

<!--@18.3-->
## 18.3 Quiet Equilibrium and growth rhythm

<!--@18.3¶1-->
Growth should periodically disturb Quiet Equilibrium because new lives create real obligations. The intended rhythm is competence -\> stability -\> attention -\> attachment -\> chosen growth or accepted risk -\> restored stability. A Colony that never has to absorb the consequences of growth feels decorative; a Colony that can never become quiet leaves no attention available for attachment.

<!--@20-->
# 19\. Interface and Information Requirements

<!--@19.1-->
## 19.1 Population panel

<!--@19.1¶1-->
| **Display**           | **Required information**                                                                              | **Prohibited reading**                             |
| --------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Roster summary**    | Total named living Citizens, with Core / Guest and adult / young filters available.                   | A generic population score or worker icon stack.   |
| **Presence summary**  | Home, Away, Outpost, Patient, and Dependent counts.                                                   | Citizens disappearing from the count while absent. |
| **Residence summary** | Occupied, available, provisional, damaged, and species-specific accommodation.                        | One universal cap detached from actual Places.     |
| **Growth preview**    | Capacity gained, Load changes, Residence effect, temporary availability cost, and named participants. | A birth-rate percentage or unit-production ETA.    |
| **Tier readiness**    | The six proofs, shown as world facts and completed achievements.                                      | A single XP bar or resource-payment button.        |

<!--@19.2-->
## 19.2 Roster legibility

<!--@19.2¶1-->
Every count must resolve back to names. Selecting Home Presence should reveal who is Home. Selecting Patients should reveal who is receiving care and where. Selecting Dependents should reveal the young Citizens and their Hearths. The count is a way to navigate the civic body, not a substitute for it.

<!--@19.3-->
## 19.3 Growth communication

<!--@19.3¶1-->
Before accepting a Wanderer, authorizing Nesting, or completing Guest Arrival, the player receives a compact delta in plain language. Example:

<!--@19.3¶2-->
<table>
<tbody>
<tr class="odd">
<td><strong>REFERENCE UI<br />
</strong>Accepting Bracken adds one available Citizen. East Court Residence becomes full. Stores Load rises by one step. Caretaking remains Covered. Refusing Bracken will be remembered.</td>
</tr>
</tbody>
</table>

<!--@19.3¶3-->
The interface may calculate exact thresholds internally, but it should communicate whole civic consequences rather than decimal efficiency coefficients.

<!--@21-->
# 20\. Supersession Ledger, Open Questions, and Acceptance Tests

<!--@20.1-->
## 20.1 Superseded material

<!--@20.1¶1-->
| **Earlier concept**                                                  | **v0.5 ruling**                                                                                                      |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Nursery as population-production-rate building**                   | Nursery becomes a Residence-and-Care Place supporting a rare seasonal Nesting commitment.                            |
| **Nursery Tender Role**                                              | Superseded. Care is carried by existing Roles and contextual Load.                                                   |
| **Breeding throughput, heredity, or bloodline optimization**         | No heredity simulation. Descent is a Tale fact only.                                                                 |
| **Population cap held by a Town Center / generic Housing statistic** | Residence is physical and species-shaped; supported population also depends on Stores, care, routes, and readiness.  |
| **Tier-wide Citizen stat bump**                                      | Removed. Individual mechanical growth remains Away; Tier grows the Colony.                                           |
| **Automatic Guest slots by Tier**                                    | Removed as progression reward. Hospitality Capacity is expressed through actual Houses, Load, and civic integration. |
| **Construction Queue slots as principal Tier reward**                | Project capability follows civic margin and unlocked Place / Project families, not a gamey queue reward.             |
| **Industrial Hub / Sovereign Highway Empire names**                  | Superseded by Independent Colony / Sovereign Network.                                                                |
| **Automatic Tier downgrade after population loss**                   | Rejected. Tier is retained as institutional and historical fact.                                                     |
| **Population as scalable workforce throughput**                      | Rejected. Every name remains counted and population remains in the dozens.                                           |

<!--@20.2-->
## 20.2 Open tuning questions

<!--@20.2¶1-->
| **Question**                      | **Bounded design space**                                                                                                                             |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wanderer cadence**              | Exact arrival frequency by Tier, season, and corridor state remains for campaign pacing. Wanderers stay primary early and rarer later.               |
| **Young-Citizen duration**        | Exact number of seasons to Maturity remains tunable. The transition stays named, non-grindy, and story-paced.                                        |
| **Nesting availability**          | Exact seasonal windows and prerequisite thresholds remain tunable. The commitment stays rare, voluntary, and normally once per seasonal window.      |
| **Residence and Load thresholds** | Exact Place capacity and population-to-Load steps remain implementation values. No decimal optimization layer or invisible hard cap.                 |
| **Tier-proof duration**           | How long Equilibrium and Seasonal proofs must remain true is tunable. Advancement continues to require all six proof categories.                     |
| **Aging and retirement**          | Long-campaign aging pace and voluntary retirement need a later lifecycle specification. Aging must not turn Citizens into disposable decline curves. |

<!--@20.3-->
## 20.3 Acceptance tests

<!--@20.3¶1-->
| **Test**                  | **Pass condition**                                                                                                         |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Named-population test** | Every population increase creates named Citizen subjects with Records, Residence, and visible obligations.                 |
| **Scale test**            | A mature Colony remains in the specified low dozens and concept art can depict the full social body.                       |
| **Count test**            | Roster, Home Presence, Available Civic Population, and Dependents / Patients remain distinguishable.                       |
| **Capacity test**         | Every present available adult contributes one equal Home Capacity regardless of personal aptitude.                         |
| **Growth-cost test**      | Adding population can create Thin Roles, Residence pressure, or seasonal obligation rather than functioning as pure gain.  |
| **Wanderer test**         | Early adult growth primarily arrives through named same-species Wanderers and reuses MEET rather than an amenability roll. |
| **Nursery test**          | The Nursery cannot be optimized as a birth factory and multiple Nursery Places do not multiply output.                     |
| **Young-Citizen test**    | Young count as full named population and Load before they provide Capacity.                                                |
| **Guest-equality test**   | Guests count toward population and neutral Tier proofs without becoming mandatory.                                         |
| **Tier-proof test**       | Population alone cannot advance Tier; all six forms of civic evidence are required.                                        |
| **Retention test**        | Population loss may destabilize the Colony but does not erase its earned Tier.                                             |
| **Plateau test**          | Tier III can support satisfying indefinite play without forced population growth or Tier IV pursuit.                       |
| **Anti-industrial test**  | Tier IV reads as corridor connection, resilience, and legacy rather than factories, armies, or empire.                     |

<!--@22-->
# Final System Statement

<!--@22¶1-->
Population in MEDIAN is the number of lives the Colony has chosen, inherited, rescued, raised, or welcomed - and can still meaningfully know. Wanderers give the founding survivors a people. The Nursery makes later generations possible by asking the Colony to carry obligation before capacity. Guests enlarge citizenship through difference. None are produced as anonymous labor.

<!--@22¶2-->
The four Colony Tiers measure the widening scale of that responsibility. A Scavenger Camp proves it can survive. A Fortified Settlement learns to prepare. An Independent Colony can endure and choose. A Sovereign Network can remain Home while belonging to a larger corridor civilization. Advancement is not the accumulation of units; it is the demonstrated ability to shelter more history without losing sight of a single name.

<!--@22¶3-->
<table>
<tbody>
<tr class="odd">
<td><strong>FINAL DOCTRINE<br />
</strong>The Colony grows large enough to become a civilization, but never so large that a missing name becomes merely a statistic.</td>
</tr>
</tbody>
</table>

<!--@22¶4-->
END OF SPECIFICATION
