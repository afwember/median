<!--@0¶1-->
**MEDIAN v0.5.0**

<!--@0¶2-->
Personal Items, Focus, and  
Expedition Equipment

<!--@0¶3-->
Baseline Specification v1.0

<!--@0¶4-->
<table>
<tbody>
<tr class="odd">
<td><strong>STATUS<br />
COMPLETE</strong></td>
<td><strong>AUTHORITY<br />
BSA-11</strong></td>
<td><strong>DATE<br />
31 JULY 2026</strong></td>
</tr>
</tbody>
</table>

<!--@0¶5-->
> *This specification consolidates the v0.5 baseline for personal equipment, Keepsakes, Supplies, Focus, and Expedition Launch. It supersedes the exploratory rulings of the development thread wherever this document speaks directly.*

<!--@0¶6-->
|                                                     |
| --------------------------------------------------- |
| Tabletop clarity beneath; lived civilization above. |

<!--@0¶7-->
Design rule: do not create state for an action the interface never offers.

<!--@1-->
# 1\. Purpose and Governing Principles

<!--@1¶1-->
**Purpose.** This system gives each named Citizen a small, legible Away identity while preserving group-based Encounter resolution. It is attachment-forward: persistent objects help the player know who a Citizen is, remember what they have done, and understand who a moment belongs to.

<!--@1¶2-->
**Compression rule.** The specification defines meaningful state transitions and design invariants. It does not enumerate every impossible action. Where there is no button, slot, or authored choice, no hidden parallel rule is implied.

<!--@1¶3-->
**Domain rule.** Home Role and Away equipment are independent. Items remain visible at Home for continuity and attachment, but their mechanical functions belong to Away Encounter play unless this specification states otherwise.

<!--@1¶4-->
|                                                                     |
| ------------------------------------------------------------------- |
| Focus is a following mechanic. It never leads the Encounter choice. |

<!--@1¶5-->
| **PRINCIPLE**                  | **BASELINE MEANING**                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **Identity persists**          | Tools and Keepsakes remain attached to Citizens across Home and Away.                                                     |
| **Preparation is temporary**   | Supplies are anonymous, Expedition-specific consumables drawn from the Colony pool.                                       |
| **The party resolves**         | Approaches and outcomes remain collective; personal items color and modify the chosen action.                             |
| **Focus follows**              | The chosen Approach exists first. A relevant Tool, Keepsake, or authored circumstance may then determine the protagonist. |
| **Equal Citizen architecture** | Core and Guest species use the same slots, item rules, Focus rules, and history rules.                                    |

<!--@2-->
# 2\. Personal Item Architecture

<!--@2¶1-->
**Every Expedition-capable Citizen has exactly three personal item boxes:**

<!--@2¶2-->
| **SLOT**     | **IDENTITY**                  | **CUSTODY**                          | **MECHANICAL ROLE**                                       |
| ------------ | ----------------------------- | ------------------------------------ | --------------------------------------------------------- |
| **Keepsake** | Persistent emotional anchor   | Citizen-specific; normally permanent | Encounter-only passive or Focus-linked effect             |
| **Tool**     | Persistent working capability | Freely equipped at Home              | Reusable contextual intervention; may assign Focus        |
| **Supply**   | Prepared consumable           | Assigned for one Expedition          | Stronger contextual intervention; consumed when committed |

<!--@2¶3-->
> **•** Empty Tool and Supply boxes are valid states, not errors or incomplete loadouts.
> 
> **•** The Citizen View is authoritative for the equipped Tool and Keepsake.
> 
> **•** A Tool and Keepsake automatically accompany their Citizen when the Launch MEET is executed.
> 
> **•** Away assignments remain fixed. Tools and Supplies are not transferred or reassigned between Encounters.

<!--@2.1-->
## 2.1 Citizen View at Home

<!--@2.1¶1-->
The Citizen View presents a large Citizen image beside the three item boxes. A filled Tool or Keepsake opens a compact record of function and provenance. Supplies show only class and function; they never receive individual identity or an Item Tale.

<!--@2.1¶2-->
At Home, the Supply box may display a random, untracked incidental object - a harmonica, seed, length of string, or similar characterful frill. Clicking it produces a brief character moment. It is not a possession, Supply, Keepsake, or persistent state. The box becomes the actual assigned Supply box when the Citizen is prepared for Away.

<!--@2.1¶3-->
If dynamic Citizen image generation is later available, Home scenes may include a Role-appropriate implement as visual frill. That prop is not the equipped Away Tool and has no mechanical or historical identity.

<!--@3-->
# 3\. Tools

<!--@3¶1-->
A Tool is a persistent, named working object carried by one Citizen. The Tool supplies a narrow capability; its owner supplies identity, presentation, and history. Tools have no levels, aptitude modifiers, or unique mechanical riders beyond their class.

<!--@3¶2-->
| **CLASS**  | **CAPABILITY**                                                                   |
| ---------- | -------------------------------------------------------------------------------- |
| **Carry**  | Increase or reorganize Cargo capacity while the holder is present and capable.   |
| **Reach**  | Extend contact or control distance; probe, hook, retrieve, or work across a gap. |
| **Cut**    | Sever, pierce, scrape, open, divide, or free.                                    |
| **Brace**  | Support, block, wedge, shield, stabilize, reinforce, or hold.                    |
| **Render** | Process suitable matter at an authored Node into a specified usable result.      |

<!--@3.1-->
## 3.1 Eligibility, ownership, and identity

<!--@3.1¶1-->
> **•** Any Citizen may equip any Tool class when the physical manifestation is credible for their body. Home Role, species, and prior profession do not gate Tool use.
> 
> **•** Several Citizens may carry the same Tool class. Duplicate classes provide redundancy and different remembered protagonists; they never stack on one Turn.
> 
> **•** A Tool normally remains equipped to its holder at Home and appears in Citizen View even when unrelated to the Citizen's Home Role.
> 
> **•** The player may freely leave, clear, or reassign Tools through Citizen View while Home. Routine reassignment is equipment management, not history.
> 
> **•** A Tool brought by an arrival from prior life becomes an ordinary Colony Tool. Provenance is preserved; ownership rules are not special.

<!--@3.1¶2-->
|                                                                                              |
| -------------------------------------------------------------------------------------------- |
| Tool choice belongs first to the Citizen's assumed identity, not to a party-coverage puzzle. |

<!--@3.2-->
## 3.2 Tool-supported Approaches and Focus

<!--@3.2¶1-->
A Tool appears as an option only after the player has chosen an Approach that it can credibly affect. Selecting the Tool provides one contextual Tool effect and places its holder in Focus for that Turn. A Tool cannot be selected merely to force Focus, Tale attribution, or a Keepsake rider.

<!--@3.2¶2-->
> **•** Only one Tool-derived mechanical advantage may apply to a Turn.
> 
> **•** When several Tools are credible, the interface presents them as alternative ways of expressing the chosen Approach. The player may choose none or one.
> 
> **•** If the selected Tool holder also has an applicable Focus Keepsake, that Keepsake rider may apply because the same Citizen holds Focus.
> 
> **•** Tools made for ordinary work may offer slight, contextual defensive utility in Conflicted MEETs. There is no Weapon class, combat loadout, attack statistic, or separate martial progression.

<!--@3.3-->
## 3.3 Tool Strain, Damage, and Carry

<!--@3.3¶1-->
Reach, Cut, Brace, and Render check Strain only after a Tool-supported Approach achieves its intended outcome. One check is made per achieved Approach: 90% Holds, 10% Damaged. Damage occurs after the full benefit and never retracts the outcome.

<!--@3.3¶2-->
> **•** A Damaged Tool remains visible in its holder's Tool box, marked unavailable, for the rest of the Expedition.
> 
> **•** At Homecoming it automatically unequips, repairs during early DWELL, and returns to Home availability. The former holder's Tool box remains empty until the player equips it again.
> 
> **•** Permanent Tool destruction occurs only as an explicit authored stake, not from ordinary Strain.

<!--@3.3¶3-->
Carry Tools operate as standing Cargo augmentation rather than active MEET interventions. They do not assign Focus or check Strain. If an authored event removes one, Cargo capacity is immediately reconciled; only fungible Cargo is lost to overflow unless the event explicitly stakes a singular object.

<!--@3.4-->
## 3.4 Render

<!--@3.4¶1-->
Render is Node-authored conversion, not an open crafting system. A successful Render Approach may create the indicated Supply, make matter safer to transport, separate usable material, or expose yield. It cannot create arbitrary Supplies, Tools, Keepsakes, or Special Artifacts.

<!--@3.4¶2-->
A Render-created Supply may be placed into any present and capable Citizen's empty or already-spent Supply box. It cannot displace an unspent Supply. Placement is part of the Render outcome, not a transfer action, and the new carrier remains fixed for the rest of the Expedition.

<!--@4-->
# 4\. Supplies

<!--@4¶1-->
Supplies are anonymous prepared units drawn from the Colony pool for one Expedition. They are broad physical capabilities rather than prepaid copies of Turn verbs or encounter-specific keys. They have no maker, personal name, provenance record, or Item Tale.

<!--@4¶2-->
The current functional classes are Binding, Remedy, Distraction, and Device. Their definitive names and recipes are controlled by the Supply specification; this document governs how all Supply classes behave in personal equipment and Encounter play.

<!--@4.1-->
## 4.1 Use inside Encounter MEETs

<!--@4.1¶1-->
> **•** A relevant Supply appears as a small inline synergy on a valid Approach. The interface states the contextual effect and that the item will be consumed.
> 
> **•** A Supply is committed only when it can credibly affect the chosen Approach or its consequences.
> 
> **•** The Supply is consumed when committed, whether or not the Approach achieves its intended outcome. Its stated effect still modifies the final resolution.
> 
> **•** A Supply is normally stronger than a reusable Tool: it may decisively soften a consequence, preserve an additional stake, extend an achieved result, or enable a credible alternate resolution. It never replaces the Turn or guarantees success.
> 
> **•** Supply availability follows its carrier. Separation, incapacity, tharn, or inability to bring the item makes it unavailable.

<!--@4.2-->
## 4.2 One active intervention

<!--@4.2¶1-->
Each Encounter MEET Turn permits one active personal-item intervention: select one Tool or spend one Supply. Keepsakes do not count as active interventions because they are present rather than used.

<!--@4.3-->
## 4.3 Away custody and Homecoming

<!--@4.3¶1-->
> **•** Each Citizen has one Supply box. Party capacity is simply the number of participating Citizens; there is no transferable abstract Supply capacity.
> 
> **•** Outside an Encounter, TRAVEL -\> Party View -\> Citizen View allows the player to discard a carried Supply at will. It leaves play and does not return to the Colony pool.
> 
> **•** An unspent Supply returns to the Colony prepared-Supply pool at Homecoming, and every Citizen's Supply box clears.

<!--@5-->
# 5\. Keepsakes

<!--@5¶1-->
A Keepsake is a persistent emotional anchor with provenance and personal meaning. It belongs to one Citizen's life rather than to a Colony-wide equipment pool. A current Keepsake remains equipped and automatically accompanies the Citizen Away.

<!--@5¶2-->
|                                                                                               |
| --------------------------------------------------------------------------------------------- |
| A Keepsake may be endangered by the world, but only the player may sever it from the Citizen. |

<!--@5.1-->
## 5.1 Eligibility and succession

<!--@5.1¶1-->
> **•** Keepsake eligibility is Citizen-specific and may arise from prior life, an acquisition event, inheritance, relationship, or an existing Hearth gift.
> 
> **•** An arrival may already possess a functioning Keepsake from their Prior-Life Tale. Colony contact is not required to validate its meaning.
> 
> **•** A new Keepsake may replace the current one only through a consequential meaning-making event with player confirmation. Accepting the new object retires the old; declining creates no reserve or backlog.
> 
> **•** A Keepsake cannot be cleared or discarded through ordinary Citizen View or TRAVEL controls. Separation occurs only through an explicit authored choice such as succession, gifting, sacrifice, or surrender.
> 
> **•** A Hearth replacement may defer the former Keepsake to a Homecoming disposition: retire it or gift it to the Hearthmate. A gift may replace the recipient's current Keepsake; the recipient's former object retires without a transfer cascade.

<!--@5.2-->
## 5.2 Mechanical operation

<!--@5.2¶1-->
Keepsakes are present, not used. They are never activated, spent, refreshed, charged, or placed on cooldown. Their mechanical effects function only inside Encounter MEETs. There are two ordinary modes:

<!--@5.2¶2-->
> **1.** Focus Keepsake - associated with one Turn category. When the player independently chooses an Approach in that domain, the holder may take Focus and receive a narrow rider grounded in the same meaning.
> 
> **2.** Standing Keepsake - tied to one narrow Encounter condition. It applies automatically to the holder when that condition occurs and does not require Focus.

<!--@5.2¶3-->
Both modes use the shared operations Soften, Preserve, and Permit. Effects remain holder-centered, bounded, and expressed through existing resolution systems. A Keepsake cannot create an Approach, reopen an unavailable Approach, or add a Turn category merely so that it can function.

<!--@5.2¶4-->
> **•** A Standing Keepsake may coexist with a Tool or Supply intervention, but multiple Standing effects do not stack onto one shared party consequence or stake.
> 
> **•** A Focus Keepsake rider may recur whenever its conditions recur; there is no frequency counter.
> 
> **•** A Damaged Keepsake remains equipped and identity-visible while its effect is suspended. Damage clears automatically at the beginning of DWELL without cost, action, or de-equipping.

<!--@6-->
# 6\. Focus

<!--@6¶1-->
Focus is a situational protagonist-selection mechanic inside a MEET. The party still chooses and resolves the Approach collectively. Focus determines which Citizen the camera, animation, principal speech or action, resolution prose, and any consequential Tale attribution follow for that Turn.

<!--@6¶2-->
|                                                                                   |
| --------------------------------------------------------------------------------- |
| The party resolves the encounter. Focus decides whose life the moment belongs to. |

<!--@6.1-->
## 6.1 Causal order

<!--@6.1¶1-->
> **1.** The Encounter presents valid choices.
> 
> **2.** The player chooses an Approach.
> 
> **3.** Relevant item expressions or authored circumstances become available.
> 
> **4.** The player may choose one active intervention.
> 
> **5.** Focus follows from the mechanically valid choice or framing.

<!--@6.2-->
## 6.2 Sources and limits

<!--@6.2¶1-->
> **•** Focus is never selected directly. There is no choose-any-Citizen command.
> 
> **•** Selecting a relevant Tool places its holder in Focus.
> 
> **•** Choosing an Approach in a Focus Keepsake's domain may place that holder in Focus, unless a different valid mechanical expression is selected.
> 
> **•** An authored circumstance may foreground a Citizen. Where no source identifies one, narration remains collective and no formal Focus is assigned.
> 
> **•** Focus does not independently change Approach availability, success, aptitude, party composition, consequence targeting, Exposure assignment, or hidden contribution.
> 
> **•** A Focused action enters a Citizen Tale only when the underlying event already crosses the normal consequence threshold. There is no Focus tally, Job experience, or automatic progression track.

<!--@6.3-->
## 6.3 Framing and Focus

<!--@6.3¶1-->
Authored framing and Focus are distinct. Framing identifies what or whose history the entire MEET concerns; Focus identifies whom the current Turn follows. Framing persists, but it never restricts the player's valid mechanical options. A scene may be about Bracken while a selected Tool makes Snip the Citizen through whom one Turn is resolved.

<!--@6.3¶2-->
UI signaling remains restrained: a brief note such as “Twig takes focus - Sire’s Hat” or “Preserved - Hazel’s Brass Button” may appear when needed. There is no persistent Focus badge, meter, portrait frame, sound cue, history counter, or formal title.

<!--@7-->
# 7\. Expedition Launch

<!--@7¶1-->
The Launch MEET begins the road toward Away but does not achieve departure until executed. Launch receives each Citizen as they already are; its personal-item choice is Supply preparation.

<!--@7.1-->
## 7.1 Launch interface

<!--@7.1¶1-->
> **•** Each proposed party member displays their equipped Tool and Keepsake read-only.
> 
> **•** The player clicks a Citizen's Supply box to open the current Colony prepared-Supply pool. Selecting a Supply places it in that box and immediately removes it from the pool display.
> 
> **•** Removing or replacing an assigned Supply updates the pool immediately. Removing a Citizen from the proposed party automatically returns that Citizen's Supply to the pool.
> 
> **•** Tool reassignment is not a top-level Launch function. The player may cancel the unexecuted Launch, change the Tool in Citizen View, and begin Launch again.

<!--@7.2-->
## 7.2 Execution and cancellation

<!--@7.2¶1-->
> **•** Before execution, party membership and Supply assignments remain editable.
> 
> **•** Executing Launch fixes party membership and all Tool, Keepsake, and Supply assignments under Away rules.
> 
> **•** Cancelling an unexecuted Launch returns all assigned Supplies to the Colony pool, clears the proposed party and Supply boxes, and stores no draft loadout or Campaign Memory event.

<!--@7.2¶2-->
|                                                       |
| ----------------------------------------------------- |
| Launch begins the road. Execution achieves departure. |

<!--@8-->
# 8\. Away State, Discard, and Loss

<!--@8.1-->
## 8.1 Fixed party and changing availability

<!--@8.1¶1-->
The Expedition party does not gain members Away. A Wanderer or Guest encountered on the road may become a future resident, but appears at the Colony only after Homecoming or after their required home is built. The active party remains the party that departed.

<!--@8.1¶2-->
Separation, incapacity, temporary tharn, or another fictional barrier changes a Citizen's availability, not their membership. Their Tool and Supply are unavailable and their boxes do not transfer. The roster changes only through extreme permanent loss: named Citizen death or Tharn abandonment.

<!--@8.2-->
## 8.2 Voluntary discard during TRAVEL

<!--@8.2¶1-->
Outside an Encounter, the player may open TRAVEL -\> Party View -\> Citizen View and voluntarily discard a Tool or Supply. A Keepsake cannot be discarded through this interface.

<!--@8.2¶2-->
> **•** A discarded Supply simply leaves play.
> 
> **•** A discarded Tool leaves play, cannot be viewed afterward under the current interface, and receives a final provenance sentence recording its holder, Expedition, and deliberate abandonment.

<!--@8.3-->
## 8.3 Permanent Citizen loss

<!--@8.3¶1-->
When a named Citizen dies or is permanently abandoned tharn, their Tool and unspent Supply leave play without a recovery, salvage, or redistribution prompt. The event follows the Citizen, not their inventory.

<!--@8.3¶2-->
A non-flight aftermath may later create a player-controlled Keepsake opportunity for a survivor, using the deceased Citizen's Keepsake or another object from the remains. The procedure is intentionally deferred; nothing transfers automatically.

<!--@9-->
# 9\. Arrivals and Equal Citizen Architecture

<!--@9¶1-->
Every named arrival already has a life. Core and Guest species use one Citizen architecture; arrival status does not create lesser slots, restricted Tool classes, special ownership, or delayed Keepsake validity.

<!--@9¶2-->
> **•** An arrival may bring a Tool grounded in their Prior-Life Tale. It enters as an ordinary named Tool and may later be reassigned like any other Tool.
> 
> **•** An arrival may bring an established Keepsake grounded in prior life. It is already bonded and mechanically valid under ordinary Keepsake rules.
> 
> **•** An arrival does not bring a tracked Supply. Consumable preparation begins when the player sends them on their first Expedition.

<!--@9¶3-->
|                                                         |
| ------------------------------------------------------- |
| An arrival brings a life, not an empty character sheet. |

<!--@10-->
# 10\. Item Records and Historical Thresholds

<!--@10¶1-->
| **OBJECT**           | **RECORD**                | **THRESHOLD**                                                                                                                                                          |
| -------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tool**             | Concise Item Tale         | Origin, maker or recovery, notable holders, consequential uses, Damage/repair history, final discard or destruction. Routine reassignment and routine use are omitted. |
| **Keepsake**         | Full emotional provenance | Origin, personal meaning, succession or gift, and the relationships carried through it.                                                                                |
| **Supply**           | None                      | Only class and function are shown. Supplies are anonymous units.                                                                                                       |
| **Special Artifact** | Fuller civic record       | Controlled by the Special Artifact specification.                                                                                                                      |

<!--@10¶2-->
Citizen Tales remain the record of one life; Item Tales remain the record of one object. The Chronicle records only civic-threshold events. Campaign Memory underlies all three without forcing every mechanically valid action into permanent prose.

<!--@10¶3-->
|                                                               |
| ------------------------------------------------------------- |
| An Item is simple to use, but it is never entirely anonymous. |

<!--@11-->
# 11\. Baseline Boundaries

<!--@11¶1-->
The following are deliberate absences, not incomplete subsystems:

<!--@11¶2-->
> **•** No inventory grid, encumbrance puzzle, item passing action, Field inventory, or between-Encounter loadout management.
> 
> **•** No direct Focus selector, Focus meter, Focus progression, or individual skill-check layer.
> 
> **•** No equipment proficiencies, Role-gated Tool classes, species aptitude bonuses, Tool levels, or unique ordinary Tool riders.
> 
> **•** No Weapon class or separate combat economy.
> 
> **•** No Colony-wide Keepsake pool, Keepsake optimization loadout, charge, cooldown, or use command.
> 
> **•** No Supply identity, maker record, or persistent carrier relationship.
> 
> **•** No mid-Expedition recruitment or replacement party-member procedure.

<!--@11.1-->
## 11.1 Explicitly deferred work

<!--@11.1¶1-->
> **•** Canonical extensible Keepsake-effect registry.
> 
> **•** Keepsake aftermath procedure following named Citizen death.
> 
> **•** Investigation of a genuinely continuous Standing effect that is not a passive stat bonus or disguised trigger.
> 
> **•** Authored Focus conditions inside Home MEETs; personal items remain mechanically inactive at Home.
> 
> **•** Detailed Node Study procedure and its relationship to Render.
> 
> **•** Final Supply class names and recipe table under the dedicated Supply specification.

<!--@11.1¶2-->
**Baseline status.** BSA-11 is complete for MEDIAN v0.5. Further edge cases should be resolved only when an authored Encounter, manifestation, or implementation requirement creates a real state not already governed here.

<!--@12-->
# 12\. Canonical Design Lines

<!--@12¶1-->
“Tabletop clarity beneath; lived civilization above.”

<!--@12¶2-->
“The party resolves the encounter. Focus decides whose life the moment belongs to.”

<!--@12¶3-->
“Focus is a following mechanic. It never leads the Encounter choice.”

<!--@12¶4-->
“The Tool answers how the party acts. Its owner answers who the player remembers doing it.”

<!--@12¶5-->
“Tools are made for work, not violence. When violence reaches the Colony, Citizens may defend themselves with the implements of ordinary life.”

<!--@12¶6-->
“A Keepsake may be endangered by the world, but only the player may sever it from the Citizen.”

<!--@12¶7-->
“Launch receives the Citizen as they already are. It decides only what the Colony sends with them for this road.”

<!--@12¶8-->
“The Tool and Keepsake leave because the Citizen leaves. The Supply leaves because the Colony prepared it.”

<!--@12¶9-->
“When a Citizen is lost, the game follows the loss - not the inventory.”

<!--@12¶10-->
“An arrival brings a life, not an empty character sheet.”

<!--@12¶11-->
**END OF BASELINE SPECIFICATION**
