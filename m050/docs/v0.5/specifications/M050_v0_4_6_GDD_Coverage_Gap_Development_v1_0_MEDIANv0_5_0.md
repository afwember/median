<!--@0¶1-->
**v0.5.0**

<!--@0¶2-->
v0.4.6 GDD Coverage-Gap Development

<!--@0¶3-->
Development-lock specification for the five cross-cutting areas resolved during v0.5 conceptualization.

<!--@0¶4-->
| **Document status** | Adopted baseline                                         |
| ------------------- | -------------------------------------------------------- |
| **Version**         | 1.0                                                      |
| **Scope**           | GDD architecture; numerical tuning deferred              |
| **Date**            | 31 July 2026                                             |
| **Precedence**      | Leads exploratory thread rulings where explicitly stated |

<!--@0¶5-->
|                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SCOPE DISCIPLINE:** v0.5 defines player-visible concepts, persistent state, major-system interactions, and authoring obligations. It does not numerically tune those systems or resolve the formal win condition. |

<!--@1-->
# Specification map

<!--@1¶1-->
| **Section** | **Coverage-gap area**                       | **Primary decisions**                                                                             |
| ----------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 1           | Culture, Memory, and Records                 | Record, Almanac, Chronicle, Citizen Tales, Distinctions, After-names, Keepsakes, laws and sayings |
| 2           | Places, Practices, and Projects              | Home spatial ontology, civic function, labor commitments, Roles, Beautification                   |
| 3           | Corridor, Outposts, Stopover, and Metropolis | Reach structure, exploration, Outposts, Away hierarchy, Stopover, recurring Metropolis fit        |
| 4           | Resources, Items, Equipment, and RENDER      | Resource taxonomy, Stock and Cargo, decay, Tools, Supplies, RENDER, Home/Away custody             |
| 5           | Guest Citizens                               | Guest architecture, Resident affordances, Expedition permissions, roster alignment and Stoat note |

<!--@1.1-->
## Global design constraints

<!--@1.1¶1-->
  - Conservation of System: new content must use existing Registers, state, and resolution grammars wherever possible.

<!--@1.1¶2-->
  - Named lives matter: Citizens, ownership, provenance, relationships, and memory remain visible rather than collapsing into anonymous bonuses.

<!--@1.1¶3-->
  - Asymmetry is permitted where species, Role, or ecology genuinely differ; symmetric complexity is not a goal.

<!--@1.1¶4-->
  - No hidden currencies, covert meters, generalized decay layers, or bespoke minigames are introduced without necessity.

<!--@1.1¶5-->
  - “Margin” is reserved for the World Zone. Capacity surplus is never called Margin.

<!--@1.1¶6-->
  - Home remains the center of civic management and emotional continuity.

<!--@2-->
# 1\. Culture, Memory, and Records

<!--@2¶1-->
The Colony remembers through authoritative state, maintained interpretation, and personal narrative. These layers cooperate without competing for canon.

<!--@1.1#2-->
## 1.1 Governing model

<!--@1.1#2¶1-->
| **Layer**     | **Function**                                                                    | **Authority**                                              |
| ------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Record        | Structured event history. Stores machine-readable facts about what occurred.    | Authoritative history                                      |
| Almanac       | Current Colony and world state. Answers what is true now.                       | Authoritative current state                                |
| Chronicle     | Maintained Colony-scale interpretation derived from the Record.                 | Authoritative interpretation; cannot contradict Record     |
| Citizen Tales | Maintained personal narratives derived from the Record and each Citizen’s life. | Authoritative personal interpretation; cannot invent state |

<!--@1.1#2¶2-->
|                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CANONICAL RULE:** The Record says what happened. The Almanac says what is true now. The Chronicle explains what the Colony believes its history means. Citizen Tales explain what that history meant within named lives. |

<!--@1.2-->
## 1.2 Homecoming write sequence

<!--@1.2¶1-->
1.  Homecoming resolves immediate material and civic consequences.

<!--@1.2¶2-->
2.  Authoritative events are written to the Record.

<!--@1.2¶3-->
3.  Persistent Colony and world state is updated in the Almanac.

<!--@1.2¶4-->
4.  Selective Chronicle evaluation determines whether the event changes Colony-scale historical interpretation.

<!--@1.2¶5-->
5.  Selective Citizen Tale evaluation determines whether the event changes one or more personal narratives.

<!--@1.2¶6-->
Not every logged event becomes Chronicle or Tale content. Selection preserves salience and avoids turning narrative into a transcript.

<!--@1.3-->
## 1.3 Canonical narrative minimum

<!--@1.3¶1-->
  - Authored modules and event clusters.

<!--@1.3¶2-->
  - Authored connective text.

<!--@1.3¶3-->
  - Authored titles, refrains, and quotations.

<!--@1.3¶4-->
  - Visible provenance linking interpretation to Record facts.

<!--@1.3¶5-->
Optional generative prose may elaborate presentation, but it is non-authoritative, Record-grounded, and forbidden from inventing facts, ownership, relationships, or world state.

<!--@1.4-->
## 1.4 Distinctions and After-names

<!--@1.4¶1-->
| **Term**    | **Definition**                                                                 | **Constraint**                                                |
| ----------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Distinction | A persistent named fact of demonstrated character, service, or accomplishment. | Not a generic counter or achievement currency                 |
| After-name  | A rare socially defining byname emerging from consequential history.           | Not routinely awarded; not player-selected from a reward list |

<!--@1.4¶2-->
Given names are drawn from curated cultural sets. After-names emerge only when a life has acquired a durable public meaning. Place names may be culturally authored where appropriate.

<!--@1.5-->
## 1.5 Keepsakes and embodied memory

<!--@1.5¶1-->
  - Keepsakes retain owner, provenance, transfer history, current location, and narrative meaning.

<!--@1.5¶2-->
  - Keepsakes are never silently reassigned, consumed, or erased.

<!--@1.5¶3-->
  - Transfer is visible and consequential.

<!--@1.5¶4-->
  - EMBODY accesses memory through present anchors: a Citizen, Place, Keepsake, Frill, or other current object that bears the past.

<!--@1.5¶5-->
|                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------- |
| **CANONICAL RULE:** Memory is accessed through what still exists in the Colony, not through a detached archive browser. |

<!--@1.6-->
## 1.6 Laws and Sayings

<!--@1.6¶1-->
| **Form** | **Status**                                            | **Use**                                                              |
| -------- | ----------------------------------------------------- | -------------------------------------------------------------------- |
| Law      | Authoritative civic rule.                             | Teaches or formalizes mechanics and obligations                      |
| Saying   | Folklore, custom, warning, joke, or inherited belief. | May be incomplete, situational, contradictory, or mechanically false |

<!--@1.6¶2-->
Record schemas and interface mockups belong in the Appendix. Chronicle and Citizen Tales philosophy belongs in the main GDD and Sourcebook architecture.

<!--@3-->
# 2\. Places, Practices, and Projects

<!--@3¶1-->
Home changes through claimed ground, civic purpose, and named commitments of Citizen time and Resources.

<!--@2.1-->
## 2.1 Core ontology

<!--@2.1¶1-->
| **Term** | **Definition**                                                                              | **Persistent state**                                          |
| -------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Place    | Permanent claimed or built ground within Home.                                              | Location, footprint, species-spatial relationship, hosted use |
| Practice | Repeated communal activity sustained by one or more Roles and hosted in a Place.            | Active civic purpose                                          |
| Project  | A named commitment of Citizen time and Resources producing a predictable persistent result. | Specific completed change                                     |

<!--@2.1¶2-->
|                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CANONICAL RULE:** Once ground becomes a Place, it remains part of the Colony. A Place may change use or stand vacant, but it cannot be demolished back into neutral ground. |

<!--@2.2-->
## 2.2 Place rules

<!--@2.2¶1-->
  - A Place may host a Residence, host a Practice, or remain vacant.

<!--@2.2¶2-->
  - Species spatial bonuses calculate against the Place itself, independent of hosted use.

<!--@2.2¶3-->
  - Mouse JOIN, Rabbit GATHER, and Squirrel CONNECT remain the governing spatial expressions.

<!--@2.2¶4-->
  - No universal adjacency-bonus puzzle, aura grid, or hidden optimization layer is added.

<!--@2.3-->
## 2.3 Practice rules

<!--@2.3¶1-->
  - A Practice is not necessarily one-to-one with a Role or Place.

<!--@2.3¶2-->
  - A Workshop may support Builder and Crafter activity.

<!--@2.3¶3-->
  - A Gathering Place hosts Teaching, Chronicle and Citizen Tale access, Keepsakes, naming, Laws and Sayings, cultural transmission, and accelerated rearing.

<!--@2.3¶4-->
  - The Community Board visually represents selected Almanac information in DWELL once constructed; the Almanac remains menu-accessible before and after it exists.

<!--@2.3¶5-->
| **Present Colony**                | **Colony through time**                             |
| --------------------------------- | --------------------------------------------------- |
| Community Board, Council, Almanac | Gathering Place, Teaching, Chronicle, Citizen Tales |

<!--@2.4-->
## 2.4 Project rules

<!--@2.4¶1-->
  - Projects consume predictable Citizen time and Resources.

<!--@2.4¶2-->
  - Projects construct or alter Places and Practices, create Away Tools and Supplies, perform repairs or Tier work, and establish specific persistent facts.

<!--@2.4¶3-->
  - The former Construction Queue is the Project Queue.

<!--@2.4¶4-->
  - Projects cannot be interrupted or cancelled after commitment.

<!--@2.4¶5-->
  - Normal Projects should not create excessively long lockouts; Tier work may be longer.

<!--@2.4¶6-->
  - Availability and scaling derive from Load, Readiness, Capacity, and player choice rather than a universal rigid slot count.

<!--@2.4¶7-->
  - Commitments are named rather than expressed as generic percentages.

<!--@2.4¶8-->
  - Project labor contributes to Role Load.

<!--@2.4¶9-->
  - All Roles contribute to Load and Readiness.

<!--@2.5-->
## 2.5 Role expressions

<!--@2.5¶1-->
| **Role**    | **Primary civic expression**                   | **Project/production alignment**                                                              |
| ----------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Builder     | Transforms the physical Colony.                | Places, structural changes, repair, Tier work                                                 |
| Crafter     | Makes functional Away equipment.               | Tools and ordinary Supplies                                                                   |
| Caretaker   | Preserves and receives.                        | Perishable-to-Durable conversion; relevant civic care                                         |
| Watchkeeper | Maintains vigilance and response.              | Watchtower or Watch Practice; no forced repeatable project                                    |
| Leader      | Coordinates civic decisions.                   | Community Board, Town Center, Tier Upgrade; no wildcard Capacity or cross-Role Load reduction |
| Gardener    | Produces ongoing Sustenance.                   | Harvest; Winter Garden upgrade                                                                |
| Healer      | Produces Remedy Supplies and provides care.    | Remedy Supplies and healing-related Projects                                                  |
| Teacher     | Supports rearing, transmission, and Gathering. | Teaching and Gathering upgrades; no labor charge for ordinary Chronicle/Tale maintenance      |

<!--@2.5¶2-->
There are no Home Tools. Tools are Away-function Items made by the Crafter. Buildings do not possess routine durability or decay; Load and Readiness express civic strain instead.

<!--@2.6-->
## 2.6 Non-Project civic acts

<!--@2.6¶1-->
  - Ceremonies, naming, Tale reflection, and Record writing are not Projects unless they physically construct a persistent material result.

<!--@2.6¶2-->
  - Shortfall exposes the Colony to a consequential Home MEET; it does not apply automatic attrition.

<!--@2.7-->
## 2.7 Beautification

<!--@2.7¶1-->
  - Beautification is driven by untasked Citizens.

<!--@2.7¶2-->
  - One Colony-wide clock advances according only to the number of untasked Citizens.

<!--@2.7¶3-->
  - Each threshold places one random minor authored Frill.

<!--@2.7¶4-->
  - Frills are cosmetic and inert: no Load, Readiness, Resource cost, Place use, or bonus.

<!--@2.7¶5-->
  - A new or refreshed Frill may create a low-stakes EMBODY opportunity.

<!--@2.7¶6-->
|                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CANONICAL RULE:** Beautification is a passive Home process driven by untasked Citizens. It advances a single Colony-wide clock, places minor cosmetic Frills at intervals, and may create temporary EMBODY opportunities. It creates no Load, grants no Readiness, uses no Project slot, and does not alter Place use. |

<!--@4-->
# 3\. Corridor, Outposts, Stopover, and Metropolis

<!--@4¶1-->
The Corridor is one continuous world. Home is its civic center; Outposts are persistent footholds; the Metropolis is a recurring destination rather than a replacement settlement or endpoint.

<!--@3.1-->
## 3.1 Corridor and Reach structure

<!--@3.1¶1-->
  - The Corridor is a line of authored or programmatically assembled Median Reaches.

<!--@3.1¶2-->
  - Reaches may vary in biome while preserving plausible regional continuity rather than strict local geography.

<!--@3.1¶3-->
  - Each Reach is approximately a long rectangle containing a central Median, two Highways, and two Margins.

<!--@3.1¶4-->
  - Longitudinal movement uses the modified Longitudinal Crossing grammar.

<!--@3.1¶5-->
  - Fog of War persists until exploration or Outpost establishment.

<!--@3.1¶6-->
  - Home appears as a shaded circle within its Median and does not consume an entire Reach.

<!--@3.1¶7-->
  - The Corridor continues beyond the Ancestral Home and Rest-Stop Metropolis; neither is terminal.

<!--@3.1¶8-->
Provisional geography places the Ancestral Home three Reaches downcorridor and the Rest-Stop Metropolis six Reaches upcorridor. Exact spacing remains adjustable.

<!--@3.2-->
## 3.2 Nodes and discovery

<!--@3.2¶1-->
  - Node is the blanket world category for all Resources and some Items.

<!--@3.2¶2-->
  - Median Nodes tend toward Sustenance; Margin Nodes are mixed.

<!--@3.2¶3-->
  - Highway opportunities belong to Crossing and MEET rather than a generic Highway Node layer.

<!--@3.2¶4-->
  - Authored Reaches may cluster ordinary Nodes without introducing a separate site or cluster system.

<!--@3.2¶5-->
  - Reach state uses the minimum useful vocabulary: Unknown, Explored, Outposted.

<!--@3.2¶6-->
  - TRAVEL reveals territory. Nodes open MEET. There is no Study meter or Knowledge currency.

<!--@3.3-->
## 3.3 Outposts

<!--@3.3¶1-->
  - An Outpost is a permanent Away installation within an explored Reach.

<!--@3.3¶2-->
  - It has no Residence and no permanent inhabitants.

<!--@3.3¶3-->
  - It hosts Shelter and staging functions but is not a second Home or remotely managed settlement.

<!--@3.3¶4-->
  - Establishment clears remaining Fog in the Reach.

<!--@3.3¶5-->
  - It supports Shelter, Launch and relaunch, Tool repair, partial Exposure reduction, Cargo offload, and local staging.

<!--@3.3¶6-->
  - Routine gathering and transport between established locations are abstracted beneath expedition scale.

<!--@3.3¶7-->
|                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CANONICAL RULE:** A Sustenance-bearing Outpost adds bounded Sustenance to the Gardener’s ongoing Harvest without increasing Gardening Load. Most Outposts contribute Perishable Sustenance, while certain authored Reaches or biomes may contribute Durable Sustenance or a mixed yield. Routine gathering and transport are abstracted beneath expedition scale. |

<!--@3.4-->
## 3.4 Away hierarchy

<!--@3.4¶1-->
Away is the umbrella mode for expedition play beyond Home. It may include Launch, TRAVEL, RISK, Crossing, MEET, Node interaction, exploration, Outpost establishment, Stopover, relaunch, and Return.

<!--@3.4¶2-->
|                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------- |
| **CANONICAL RULE:** Away is the umbrella. Stopover and Homecoming are the paired expedition-resolution concepts. |

<!--@3.5-->
## 3.5 Stopover

<!--@3.5¶1-->
Stopover is the restricted Outpost state entered when an expedition reaches an established Outpost. It partially resolves expedition needs while preserving Away continuity.

<!--@3.5¶2-->
  - Use Shelter and reduce part of Exposure.

<!--@3.5¶3-->
  - Repair damaged Tools through the Outpost affordance.

<!--@3.5¶4-->
  - Offload Cargo into the single Colony Stock through abstract routine transport.

<!--@3.5¶5-->
  - Inspect Citizens, Cargo, Tools, Supplies, Keepsakes, Artifacts, and other Items.

<!--@3.5¶6-->
  - Choose a route, destination, Return, or relaunch.

<!--@3.5.1-->
### Locked Outpost view

<!--@3.5.1¶1-->
After Stopover resolution, the camera settles into one fixed authored composition using the visual language of DWELL. The Shelter, staging ground, party, Tools, Items, weather, Day Band, and Reach conditions remain visible. The camera cannot pan, rotate, or move between Places.

<!--@3.5.1¶2-->
  - No Place claiming or spatial rearrangement.

<!--@3.5.1¶3-->
  - No Residence, Practice, Role, or Project management.

<!--@3.5.1¶4-->
  - No Beautification, rearing, ceremony, Council, Gathering Place, Chronicle/Tale evaluation, or EMBODY.

<!--@3.5.1¶5-->
  - No separate Outpost Stock or warehouse.

<!--@3.5.1¶6-->
|                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------- |
| **CANONICAL RULE:** The locked view communicates: the Colony has made a place here, but it has not made a Home. |

<!--@3.6-->
## 3.6 Stopover and Homecoming

<!--@3.6¶1-->
| **Function**                          | **Stopover**                                               | **Homecoming**                             |
| ------------------------------------- | ---------------------------------------------------------- | ------------------------------------------ |
| Location                              | Established Outpost                                        | Home                                       |
| Ends current Away expedition          | No                                                         | Yes                                        |
| Away continuity                       | Preserved                                                  | Concluded                                  |
| Presentation                          | Locked DWELL-like composition                              | Full DWELL                                 |
| Recovery and Tool repair              | Bounded                                                    | Full return resolution                     |
| Cargo to Colony Stock                 | Yes, through abstract transport                            | Yes, directly                              |
| Full Item reconciliation              | No                                                         | Yes                                        |
| Record and Almanac update             | Only where immediately required; full integration deferred | Yes                                        |
| Chronicle and Citizen Tale evaluation | No                                                         | Yes                                        |
| Civic management and EMBODY           | No                                                         | Yes                                        |
| Immediate relaunch                    | Yes                                                        | No; a later Launch begins a new expedition |

<!--@3.6¶2-->
|                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CANONICAL RULE:** Homecoming occurs only at Home. It ends the expedition and performs full material, civic, emotional, and historical reintegration. |

<!--@3.7-->
## 3.7 Rest-Stop Metropolis

<!--@3.7¶1-->
  - The Metropolis is a fixed authored destination within the same continuous Corridor.

<!--@3.7¶2-->
  - An ambitious Colony may reach it from Tier II onward through ordinary expedition play.

<!--@3.7¶3-->
  - First arrival opens a persistent recurring destination rather than concluding the campaign.

<!--@3.7¶4-->
  - Later journeys remain meaningful; the route does not collapse into a menu teleport.

<!--@3.7¶5-->
  - The Metropolis is not a replacement Home, a separately managed settlement, a generic market, or a victory state.

<!--@3.7¶6-->
  - Interaction belongs primarily to TRAVEL and authored MEET. Lasting effects return to Home as relationships, Promises, Records, Items, Practices, Projects, and changed world state.

<!--@3.7¶7-->
Detailed Metropolis geography, districts, factions, governance, economy, repeatable visit structure, and visual identity are deferred to v0.6.

<!--@3.8-->
## 3.8 Win condition

<!--@3.8¶1-->
|                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **EXPLICIT DEFERRAL:** Win Condition - Deferred beyond v0.5. v0.5 defines civic and geographic progression but does not define a formal victory trigger, required culmination sequence, or campaign-ending state. Tier advancement, Metropolis access, and network participation are progression structures rather than automatic win conditions. |

<!--@5-->
# 4\. Resources, Items, Equipment, and RENDER

<!--@5¶1-->
Resources are fungible quantities. Items are discrete objects. The distinction governs custody, production, memory, and Away equipment.

<!--@4.1-->
## 4.1 Resource taxonomy

<!--@4.1¶1-->
|                                                               |
| ------------------------------------------------------------- |
| **CANONICAL RULE:** Resources are counted. Items are tracked. |

<!--@4.1¶2-->
| **Resource family** | **Branch** | **Primary character**                                                    |
| ------------------- | ---------- | ------------------------------------------------------------------------ |
| Sustenance          | Perishable | Food subject to global Dawn decay                                        |
| Sustenance          | Durable    | Food not subject to routine decay                                        |
| Scrap               | Flexible   | Bendable, fibrous, sheet-like, cord-like, or otherwise yielding material |
| Scrap               | Rigid      | Hard, stiff, load-bearing, edged, or structurally resistant material     |

<!--@4.1¶3-->
No other universal Resource family is established in v0.5.

<!--@4.2-->
## 4.2 Item taxonomy

<!--@4.2¶1-->
| **Item** | **Definition**                                                                                             | **Custody**                                        |
| -------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Tool     | Permanent functional Item crafted by a Crafter from Resources for Away use.                                | Individually held; one Tool slot per Citizen       |
| Supply   | Consumable functional Item crafted from Resources. Remedy Supplies are made by Healer; others by Crafter.  | Individually carried Away; anonymous prepared unit |
| Keepsake | Permanent personal or historical Item with ownership, provenance, transfer history, location, and meaning. | Belongs to a named life                            |
| Artifact | Rare singular authored status or exception, usually expressed as a tag on a unique Item.                   | Individually tracked                               |

<!--@4.3-->
## 4.3 Cargo and Colony Stock

<!--@4.3¶1-->
  - Cargo refers only to Away-carried Resources: Perishable Sustenance, Durable Sustenance, Flexible Scrap, and Rigid Scrap.

<!--@4.3¶2-->
  - Items are tracked separately and are never Cargo.

<!--@4.3¶3-->
  - Colony Stock is the abstract numerical Home inventory of Resources, visible through Almanac and relevant Project, crafting, and preparation interfaces.

<!--@4.3¶4-->
  - No physical Store or warehouse is implied; “Store” is removed as a defined term.

<!--@4.3¶5-->
  - At Homecoming, Cargo enters Colony Stock. Items reconcile separately while retaining holder, owner, location, state, and provenance.

<!--@4.3¶6-->
  - At an Outpost Stopover, Cargo may enter Colony Stock through abstract routine transport. There is no second Outpost Stock.

<!--@4.4-->
## 4.4 Production and conversion

<!--@4.4¶1-->
  - Gardener Harvest produces Resources.

<!--@4.4¶2-->
  - Caretaker preservation converts declared Perishable Sustenance into Durable Sustenance.

<!--@4.4¶3-->
  - Crafter crafts Tools and ordinary Supplies.

<!--@4.4¶4-->
  - Healer crafts Remedy Supplies.

<!--@4.4¶5-->
  - Projects consume Resources and Citizen time.

<!--@4.4¶6-->
  - Nodes contain Resources and, where authored, discrete Items.

<!--@4.5-->
## 4.5 Perishable decay

<!--@4.5¶1-->
  - One aggregate global Dawn decay rule applies. There are no batches, ages, freshness values, or FIFO tracking.

<!--@4.5¶2-->
  - Consumption normally draws from Perishable before Durable.

<!--@4.5¶3-->
  - At Dawn, a tuned fraction of remaining Perishable is lost. Exact rate and rounding are deferred.

<!--@4.5¶4-->
  - Durable Sustenance does not decay.

<!--@4.5¶5-->
  - Caretaker preservation resolves before the next decay.

<!--@4.5¶6-->
  - Fresh Harvest receives one decision window before its first decay.

<!--@4.5¶7-->
  - Perishable Cargo follows the same Dawn decay rule; there is no separate travel-spoilage system.

<!--@4.5¶8-->
Exactly two canonical sources may reduce the global decay rate: the Toad Resident Affordance and an advanced Caretaking Practice upgrade. They do not stack; the strongest applicable rate is used. No Tool, Supply, ordinary Place, or other general bonus alters decay.

<!--@4.6-->
## 4.6 Core Tool classes

<!--@4.6¶1-->
| **Tool class** | **Primary function**                                                         |
| -------------- | ---------------------------------------------------------------------------- |
| Carry          | Increase or reorganize personal and party Cargo capacity                     |
| Reach          | Extend contact, probe, hook, retrieve, or operate across a gap               |
| Cut            | Sever, pierce, scrape, open, divide, or free                                 |
| Brace          | Support, block, wedge, shield, stabilize, reinforce, or hold                 |
| Render         | At an authored Node, process suitable material into the one specified Supply |

<!--@4.6¶2-->
Each Citizen has one Tool slot. Physical form remains species-specific, material-specific, and provenance-specific. Different objects are not separate Tool classes unless their function genuinely differs.

<!--@4.7-->
## 4.7 Tool use and strain

<!--@4.7¶1-->
  - A Tool appears only after the player chooses an Approach it can credibly affect.

<!--@4.7¶2-->
  - One Tool-derived mechanical advantage may apply to a Turn.

<!--@4.7¶3-->
  - Selecting the Tool places its holder in Focus for that Turn.

<!--@4.7¶4-->
  - Reach, Cut, Brace, and Render check Strain only after a Tool-supported Approach achieves its intended outcome.

<!--@4.7¶5-->
  - The current baseline is 90% Holds and 10% Damaged; this percentage remains subject to tuning.

<!--@4.7¶6-->
  - Damage occurs after the full benefit and never retracts the achieved outcome.

<!--@4.7¶7-->
  - A damaged Tool is unavailable for the rest of the expedition, then automatically unequips and repairs during early DWELL after Homecoming. Outposts may repair Tools during Stopover.

<!--@4.7¶8-->
  - Carry functions passively and does not check Strain.

<!--@4.8-->
## 4.8 Supplies

<!--@4.8¶1-->
  - Supplies are anonymous prepared units rather than named personal possessions.

<!--@4.8¶2-->
  - Each participating Citizen has one Supply slot.

<!--@4.8¶3-->
  - A relevant Supply appears as an inline synergy on a valid Approach.

<!--@4.8¶4-->
  - The player chooses whether to spend it; the interface states the contextual effect and consumption.

<!--@4.8¶5-->
  - Each Turn permits one active personal-item intervention: one Tool or one Supply.

<!--@4.8¶6-->
  - A Supply is normally stronger than a reusable Tool but never guarantees success.

<!--@4.8¶7-->
  - An unspent Supply returns to the Colony prepared-Supply pool at Homecoming.

<!--@4.9-->
## 4.9 RENDER

<!--@4.9¶1-->
|                                            |
| ------------------------------------------ |
| **CANONICAL RULE:** RENDER makes a Supply. |

<!--@4.9¶2-->
RENDER is a Node-authored process that consumes suitable material to create one specified Supply. The Node determines whether RENDER is available, which Supply is produced, what material is consumed, and what risk or consequence accompanies the process.

<!--@4.9¶3-->
  - The created Supply may enter any present and capable Citizen’s empty or already-spent Supply slot.

<!--@4.9¶4-->
  - It cannot displace an unspent Supply.

<!--@4.9¶5-->
  - Placement is part of the RENDER outcome rather than a separate transfer action.

<!--@4.9¶6-->
  - RENDER cannot freely choose among Supply classes.

<!--@4.9¶7-->
  - RENDER cannot create Resources, Tools, Keepsakes, Artifacts, inventory slots, or open-ended Away crafting.

<!--@4.9¶8-->
  - Cutting, scraping, wrapping, mixing, separating, or preparing may describe the fiction, but the sole mechanical output is the authored Supply.

<!--@6-->
# 5\. Guest Citizens

<!--@6¶1-->
Guests are full named Citizens. Their ecological difference appears as one equal civic contribution and one bounded qualitative permission, not as collectible bonuses or separate simulation layers.

<!--@5.1-->
## 5.1 Architecture

<!--@5.1¶1-->
  - The roster contains twelve Resident species and seven Expedition species.

<!--@5.1¶2-->
  - Every Guest contributes one equal Home Role Capacity and one qualitative Signature Permission or Affordance.

<!--@5.1¶3-->
  - Resident Home Roles are species-authored. Expedition Guest Home Roles are individual-authored.

<!--@5.1¶4-->
  - Firefly Family and Bumblebee Household are the only collective-bodied Citizen exceptions.

<!--@5.1¶5-->
  - Guest Houses are Residence Places and must respect JOIN, GATHER, CONNECT, and species body.

<!--@5.1¶6-->
  - Recruitment is relationship and hospitality, not collection.

<!--@5.1¶7-->
  - Guests fully count toward Roster, Residence, Load, Capacity, Tier proof, memory, EMBODY, Chronicle, and Citizen Tales.

<!--@5.1¶8-->
  - No essential system, Tier, or ending requires Guests.

<!--@5.2-->
## 5.2 Reader-facing species convention

<!--@5.2¶1-->
Reader-facing names use single-word species forms in the Wind in the Willows register. Two-name zoological forms may remain only in metadata, ecological notes, or art direction where distinction is necessary.

<!--@5.2¶2-->
| **Residents**                                                                                                 | **Expedition Guests**                             |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Owl; Sparrow; Toad; Firefly Family; Groundhog; Turtle; Bumblebee Household; Mole; Bat; Pigeon; Skunk; Opossum | Raccoon; Crow; Fox; Weasel; Hedgehog; Snake; Mink |

<!--@5.3-->
## 5.3 Resident Guest alignment

<!--@5.3¶1-->
| **Resident**        | **Home Role** | **Signature Affordance**          | **v0.5 expression**                                                                                                                                      |
| ------------------- | ------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Owl                 | Watchkeeper   | Night Sky-watch                   | Earlier and clearer Telegraph in eligible night Home MEET; no detection meter                                                                            |
| Sparrow             | Teacher       | Day Call                          | Learned through Teaching Practice and expressed through Gathering Place; no call-learning subsystem                                                      |
| Toad                | Caretaker     | Cool Keeping / Wet-Ground Keeping | While present and available, applies the reduced global Perishable decay rate; does not stack with advanced Caretaking                                   |
| Firefly Family      | Leader        | Lantern Procession                | Illuminates one bounded route or Place during an eligible night Home MEET; does not extend the workday                                                   |
| Groundhog           | Gardener      | Seasonal Telegraph                | Reads an existing authored or scheduled seasonal pressure; no weather simulation                                                                         |
| Turtle              | Caretaker     | Protected Receiving               | During an eligible crisis or Homecoming, protects one chosen bounded stake from an immediate consequence; event-specific, not storage                    |
| Bumblebee Household | Gardener      | Carry the Bloom                   | An exceptional flowering plant recovered Away may persist through a Garden Project; no baseline Harvest bonus or pollination simulation                  |
| Mole                | Builder       | Subsurface Diagnosis              | An event- or Telegraph-based diagnosis opens a better Builder response or Project; no soil simulation                                                    |
| Bat                 | Builder       | Dry-Dark Inspection               | In an eligible Home MEET involving an enclosed or inaccessible structure, reveals source or extent and opens a response; no structure-decay layer        |
| Pigeon              | Leader        | Correspondence                    | Send Word, Ask the Flock, delayed answers, Promises, MEETs, and destinations; not automatically a Project                                                |
| Skunk               | Watchkeeper   | Boundary Deterrence               | Nonlethal local response with descriptive aftermath; no universal Scent Condition                                                                        |
| Opossum             | Healer        | Aftermath Receiving               | At Homecoming or Home MEET, isolates one questionable Cargo quantity, returning Item, carcass, or affected Citizen; no contamination or quarantine meter |

<!--@5.4-->
## 5.4 Expedition Permission families

<!--@5.4¶1-->
| **Family** | **Function**                                                                           | **Limit**                                                |
| ---------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| HANDLE     | Interact effectively with a bounded object, mechanism, material, or carcass.           | Does not identify every hazard or guarantee yield        |
| READ       | Reveal bounded context, pattern, route state, movement, or sign.                       | Not omniscience, exact prediction, or remote exploration |
| INTERCEDE  | Create rescue, cover, escort, drive-off, or extraction possibilities.                  | Does not guarantee victory or erase danger               |
| SPEAK      | Open recognition, display, intimidation, mediation, or species-specific communication. | Does not translate all animals or force agreement        |
| REACH      | Enter a bodily domain inaccessible or unsafe for the ordinary party.                   | Does not ferry the party or negate the domain’s risks    |

<!--@5.5-->
## 5.5 Expedition roster

<!--@5.5.1-->
### Raccoon - HANDLE - Latchwork

<!--@5.5.1¶1-->
Opens a suitable sealed or latched human container or simple mechanism. The result may be Resources, an Item, a MEET, danger, contamination, nothing useful, or a later RENDER opportunity. Opening does not process contents, identify hazards, increase Cargo, bypass unrelated Tools, or auto-convert the object into Scrap.

<!--@5.5.2-->
### Crow - READ - Long View

<!--@5.5.2¶1-->
Reveals bounded distant context: Reach character, movement, route change, Crossing pressure, Outpost activity, approaching party or predator, or a likely Node function. It does not clear whole-Reach Fog, replace exploration, provide exact quantities, or grant aerial fast travel.

<!--@5.5.3-->
### Fox - HANDLE - Carcass Claim; embodied RENDER access

<!--@5.5.3¶1-->
Approaches and secures a suitable carcass opportunity and recovers its authored Sustenance yield. At a suitable carcass Node, Fox may perform the available Node-authored RENDER without carrying a conventional Render Tool. RENDER consumes the specified material and makes the named Supply. Fox does not preserve Sustenance, ignore Cargo, neutralize contamination, prevent rivals, or create a separate carcass-crafting system.

<!--@5.5.4-->
### Weasel - INTERCEDE - Drive Off

<!--@5.5.4¶1-->
Redirects or pursues a suitable threat, creates an escape interval, protects a vulnerable subject, or opens WITHDRAW. It uses ordinary RISK, MEET, injury, and separation. It creates no combat subsystem, chase minigame, or universal size table.

<!--@5.5.5-->
### Hedgehog - INTERCEDE - Living Cover

<!--@5.5.5¶1-->
Protects or escorts one vulnerable Citizen or one discrete Item during exposed movement or withdrawal. It does not protect the entire party, anonymous Cargo quantities, or negate traffic and danger.

<!--@5.5.6-->
### Snake - SPEAK - Display

<!--@5.5.6¶1-->
Opens intimidation, recognition, nonverbal communication, PARLEY, YIELD, or controlled withdrawal in narrowly authored contexts. It is not a translator, attack, forced surrender, or general social bonus.

<!--@5.5.7-->
### Mink - REACH - Water Reach

<!--@5.5.7¶1-->
Enters water, flooded culverts, drainage channels, submerged passages, and other authored water domains to inspect, retrieve, rescue, or access a Node. It does not ferry the party, create fast travel, remove Exposure, guarantee recovery, or automatically RENDER recovered matter.

<!--@5.6-->
## 5.6 Guest relationship to Tool grammar

<!--@5.6¶1-->
  - A Guest Permission may interact with an existing Tool-class grammar without creating a parallel system.

<!--@5.6¶2-->
  - A Guest bypasses a carried Tool only where the species body, behavior, and ecological knowledge directly perform the bounded function.

<!--@5.6¶3-->
  - Raccoon may expose a later RENDER opportunity; Crow may reveal one; Weasel may create time or space for another Citizen to act; Hedgehog may protect a Citizen or discrete Item; Snake may preserve social access; Mink may reach the Node.

<!--@5.6¶4-->
  - Fox is the only current Expedition Guest with standing embodied access to Node-authored RENDER.

<!--@5.7-->
## 5.7 Stoat note

<!--@5.7¶1-->
|                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PROVISIONAL ALTERNATIVE:** Stoat is recorded as a possible future roster substitution. No change is adopted for v0.5; Weasel and Mink remain canonical, and Stoat has no assigned mechanical package. |

<!--@7-->
# Adoption and deferral summary

<!--@7¶1-->
| **Area**                | **Adopted for v0.5**                                                                        | **Deferred**                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Culture and memory      | Four-layer authority model; Distinctions; After-names; Keepsake provenance; Laws/Sayings    | Detailed Record schemas and interface mockups                          |
| Home change             | Place-Practice-Project ontology; Role alignment; Beautification                             | Numerical Load, Readiness, Capacity, and Project tuning                |
| Corridor                | Reach model; Nodes; Outposts; Stopover; Metropolis fit                                      | Detailed Metropolis design; exact geography; formal win condition      |
| Resources and equipment | Four Resource branches; Item categories; Stock/Cargo; decay; Tool classes; Supplies; RENDER | Exact rates, recipes, quantities, and balance values                   |
| Guests                  | Resident and Expedition rosters; bounded affordances; Tool-grammar relationship             | Additional content packages, exact recruitment arcs, Stoat disposition |

<!--@7¶2-->
|                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **SOURCE CLAIM:** This development pass addresses five v0.4.6 coverage-gap areas. Its self-declared closure does not confer global authority; each claim remains subject to grand reconciliation. |
