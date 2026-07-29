# Review — MEDIAN_Civilization_Spatial_Design_Spec.docx

A ChatGPT-session spatial design spec for how the three species build (Mouse = Manor House / Join, Rabbit = Cul-de-Sac / Gather, Squirrel = Web / Connect), reviewed against three concept-art images and against `100 canon/MEDIAN_GDD_v0.4.6.md`. Not canon; a review, for whoever picks this up next.

**Update:** the open questions this review raised have decisions against them now — see `500 log/v0.4.7_decisions.md` (V6-1 through V6-4). Noted inline below rather than rewritten out of the original review, so the reasoning that led to each call stays visible.

---

## What the spec gets right

**The core move is sound.** One shared build menu, one placement verb per species, no adjacency percentages or service-radius tuning — this is a clean, almost literal execution of Pillar 2.6 (mechanical restraint, expressive variety) and Pillar 2.3 (ledger and legible: state visible in the world first). "The player should identify the civilization from the shape of the base before seeing the inhabitants" is close to a paraphrase of the ledger-and-legible pillar. → **Confirmed as the shared grammar across all three species** (V6-1).

**Squirrel is close to ready.** Web / Connect — separated nodes joined by routes that "cross real gaps" — is a faithful, better-worded gloss on the existing Cache Network (dispersal vs. centralization, redundancy against raids, Section 4.2). Reference Image C matches both the spec and canon: Lookout, Repair Perch, Meeting Branch, and three named Homes on visible rope spans read as a web at a glance, and nothing in it contradicts canon. → Squirrel is also now the likely home for relay/shuttle behavior coming off Mouse (V6-4, proposed).

**The Shoulder Strip / Median Interior split is functionally, if not terminologically, correct.** "Permanent domestic form stays inside the Median Interior" and the Shoulder "does not become ordinary residential land" match the Margin's canon guarantee almost exactly: never buildable, under any circumstance (Section 7.4). → **Terms retired in favor of canon's own** (V6-2); the functional split stands.

---

## Where it conflicted with canon — now resolved or in progress

### Territory vocabulary — resolved (V6-2)

The spec's **Median Interior / Shoulder Strip / Carriageway Gap / Chain of Median Strips** described the same geography as canon's **Home Median / Margin / Highway / Median Reach chain**, as a second, unintegrated vocabulary. **Decision: MEDIAN's existing terms are used everywhere** — in the spec, any art brief drawn from it, and all future assembly. The Crossing-vs.-longitudinal-travel conflation (treating "cross the carriageway" and "reach a new Reach" as the same act) still needs fixing wherever the spec's expansion language gets carried forward; that wasn't itself the subject of V6-2 and is worth catching in the next pass.

### Rabbit — resolved, and it's a bigger change than a reconciliation (V6-1)

Canon's **Warren Flow** (Section 4.1) was a depth-and-flow puzzle: chambers and tunnels beneath the terrain, with a readable signature of multiplicity of exits — half a dozen-plus bolt holes and one distant **Far-hole**. The spec's **Cul-de-Sac** is a surface neighborhood around a shared green — a different building. **Decision: Rabbit's signature moves above ground.** The Cul-de-Sac — including outdoor-use space like grazing ground as part of the identity, not just the court itself — replaces Warren Flow outright, not just its presentation. Reference Image A, which reads as a genuinely appealing above-ground court, is now the closer model of the two.

This is a real reversal of a settled canon item, not a reconciliation of two compatible layers, and it leaves debt: Section 4.1's underground prose, the Far-hole's promised appearance "in the Field layer as well," and the `OPEN — Warren Flow` callout all describe the model this closes. They need rewriting in the next assembly pass, and the new signature still needs its own name (Warren Flow no longer fits an above-ground court).

### Building taxonomy — resolved (V6-3)

The spec's six-to-seven universal functions were missing families with real mechanical weight: **Staging Post** (Tools, the departure threshold — Section 20), **Guest House** (the building the Guest Citizens system hangs off — Section 21), and the deliberately-unmerged **Story Circle** / **Community Board** (ceremonial vs. ambient-operational — Section 16.3). **Decision: all four are written back into the spec's building set.**

One correction surfaced in the process, already fixed directly in the GDD rather than logged as a design call: the Staging Post's old description — "the place a party dresses for the road" — was leftover text that the v0.4.6 assembly should have removed when gear became worn-always (C-98) but didn't catch. Fixed in `100 canon/MEDIAN_GDD_v0.4.6.md`, Sections 16.1 and 20: Staging Post is now just the departure threshold and where Tools are kept and drawn.

### Mouse — proposed, not settled (V6-4)

Canon's **Relay Network** (Section 4.3) — short visible carrying handoffs, cooperative relay of load — was flagged as not resonant for a Mouse colony *at home*. Two threads now on the table, not yet reconciled: Squirrel picking up relay/shuttle behavior instead (it already fits Cache Network's dispersal logic), and Mouse's home signature becoming the spec's Manor House / Join model, with Relay Network surviving, if at all, as an expedition-specific Mouse quirk rather than the colony's readable at-home identity. Reference Image B ("one estate, many labeled wings, jammed into highway infrastructure") is the visual argument for the Manor; it still doesn't show a relay economy, which is fine if Mouse's economy isn't a relay anymore — but that's the open half of V6-4.

*(Separately, a production note rather than a design one: the "Rules of Thimblehold" signage in Image B has garbled text — a known image-gen artifact, not a canon issue.)*

---

## Summary table

| | Spec's answer | Canon's prior answer | Status |
|---|---|---|---|
| **Squirrel** | Web / Connect, distributed nodes + routes | Cache Network, dispersal vs. centralization | **Aligned**, and likely gains relay/shuttle duty (V6-4, proposed) |
| **Mouse** | Manor House / Join, one accumulating structure | Relay Network, short visible carrying handoffs | **Front-runner for home signature** (V6-4, proposed); Relay's fate as an expedition quirk still open |
| **Rabbit** | Cul-de-Sac / Gather, surface court + outdoor space | Warren Flow, underground depth-and-flow, multiplicity of exits | **Decided** (V6-1) — Cul-de-Sac replaces Warren Flow; rewrite of Section 4.1 and the Far-hole material still owed |
| **Territory** | Median Interior / Shoulder Strip / Carriageway Gap | Home Median / Margin / Highway / Reach chain | **Decided** (V6-2) — canon terms used everywhere |
| **Buildings** | 6–7 universal functions | 12+ structure families incl. Staging Post, Guest House, Story Circle, Community Board | **Decided** (V6-3) — missing families written back in; Staging Post's dressing beat corrected as a bug, not a call |

---

## What's still open

1. **Mouse's home economy.** Does Relay Network survive at all, and if so where — an expedition-only quirk, as raised, or something else? What replaces it as the mechanical substance behind the Manor House's silhouette?
2. **Squirrel's relay duty.** If Squirrel picks up shuttle/relay behavior, how does it sit alongside Cache Network without the two becoming two names for one thing?
3. **Rabbit's new signature needs a name** now that "Warren Flow" no longer describes it, plus a decision on what (if anything) replaces the Far-hole's Field-layer payoff.
4. **The Crossing-vs.-Reach conflation** in the spec's expansion language (treating a carriageway crossing and a new-Reach founding as the same event) wasn't part of V6-1 through V6-4 and still needs a fix wherever this spec's language gets carried forward.

None of the above is executed against the v0.4.6 GDD yet, except the Staging Post bug fix. It waits for its own change guide and assembly pass, same as this whole project always has.
