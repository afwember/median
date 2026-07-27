# Review — MEDIAN_Civilization_Spatial_Design_Spec.docx

A ChatGPT-session spatial design spec for how the three species build (Mouse = Manor House / Join, Rabbit = Cul-de-Sac / Gather, Squirrel = Web / Connect), reviewed against three concept-art images and against `100 canon/MEDIAN_GDD_v0.4.6.md`. Not canon; a review, for whoever picks this up next.

---

## What the spec gets right

**The core move is sound.** One shared build menu, one placement verb per species, no adjacency percentages or service-radius tuning — this is a clean, almost literal execution of Pillar 2.6 (mechanical restraint, expressive variety) and Pillar 2.3 (ledger and legible: state visible in the world first). "The player should identify the civilization from the shape of the base before seeing the inhabitants" is close to a paraphrase of the ledger-and-legible pillar.

**Squirrel is close to ready.** Web / Connect — separated nodes joined by routes that "cross real gaps" — is a faithful, better-worded gloss on the existing Cache Network (dispersal vs. centralization, redundancy against raids, Section 4.2). Reference Image C matches both the spec and canon: Lookout, Repair Perch, Meeting Branch, and three named Homes on visible rope spans read as a web at a glance, and nothing in it contradicts canon.

**The Shoulder Strip / Median Interior split is functionally, if not terminologically, correct.** "Permanent domestic form stays inside the Median Interior" and the Shoulder "does not become ordinary residential land" match the Margin's canon guarantee almost exactly: never buildable, under any circumstance (Section 7.4).

---

## Where it conflicts with canon, not just diverges from it

### Territory vocabulary is a parallel invention

The spec's **Median Interior / Shoulder Strip / Carriageway Gap / Chain of Median Strips** describes the same geography as canon's **Home Median / Margin / Highway / Median Reach chain**, but as a second, unintegrated vocabulary. Worse, it conflates two things canon deliberately keeps separate (Section 7.3): a **transverse Crossing** (Median → Margin, same Reach) and **longitudinal travel** to a **new Reach** (a different Median segment up or down the corridor). The spec's "crossing the carriageway founds a new Manor" reads as if a new settlement sits on the far side of the same road a colony already raids across. It doesn't — the corridor chain is reached by traveling *along* the highway, not by walking straight across it a second time.

### Rabbit is a real conflict, not a gap

Canon's **Warren Flow** (Section 4.1) is a depth-and-flow puzzle: chambers and tunnels fit *beneath* limited terrain, and its readable signature — settled specifically to close a long-open design item — is **multiplicity of exits**: half a dozen-plus bolt holes and one distant **Far-hole**, a warren read from its scattered mouths above ground while the structure itself stays hidden below.

The spec's **Cul-de-Sac** is a surface neighborhood organized around a shared green. That's a different building. Reference Image A executes the spec's own vision well — a genuinely charming above-ground court with a fire circle and lookout towers — but it does not show what canon actually asks for: no legible exit-count, no Far-hole set apart from the rest. This needs an owned decision, not a quiet merge:

- **Option 1:** the Cul-de-Sac becomes the *social* layer sitting visibly atop an unseen depth-and-flow warren, and the multiplicity-of-exits payoff moves to where canon already promises it — the Field layer (Section 4.1: "that distant exit appears in the Field layer as well").
- **Option 2:** Cul-de-Sac replaces Warren Flow's readable signature outright. That's a design change to a settled item, not something an art-direction pass should decide by default.

### The building taxonomy drops load-bearing families

The spec's six-to-seven universal functions (Home, Pantry, Workshop, Gathering, Care, Watch, optional Nursery) are thinner than canon's structure list (Section 16.1), and what's missing isn't decorative:

- **No Staging Post** — where Tools live and a party dresses for the road; the literal threshold between home and away (Section 20).
- **No Guest House** — the building the entire Guest Citizens system hangs off, with per-occupant skin and placement (Section 21).
- **No separate Story Circle / Community Board** — canon keeps these unmerged on purpose, because they run at different tempos: ceremonial vs. ambient-operational (Section 16.3). Folding both into a single "Gathering" function would undo that split.

None of this breaks the spec's grammar — it means the spec is an art/placement layer sitting *above* a structure list it hasn't fully accounted for yet.

### Mouse is silent on the thing canon already answered

Canon's **Relay Network** (Section 4.3) is about logistics: short visible handoffs, stations, cooperative carrying, because mice have the lowest individual capacity of the three species. The spec's **Manor House** is a spatial answer — one accumulating structure, rooms becoming wings — that says nothing about how goods move through it. Reference Image B nails the feeling ("one estate, many labeled wings, jammed into highway infrastructure") but reads as a manor *economy*, not a relay *economy*. The two aren't contradictory — the Manor could simply be the building the Relay happens inside — but the spec doesn't make that connection, so right now they're two unconnected answers to two different questions.

*(Separately, a production note rather than a design one: the "Rules of Thimblehold" signage in Image B has garbled text — a known image-gen artifact, not a canon issue.)*

---

## Summary table

| | Spec's answer | Canon's existing answer | Status |
|---|---|---|---|
| **Squirrel** | Web / Connect, distributed nodes + routes | Cache Network, dispersal vs. centralization | **Aligned** — ready to fold in |
| **Mouse** | Manor House / Join, one accumulating structure | Relay Network, short visible carrying handoffs | **Unconnected** — needs the Manor wired to the Relay explicitly |
| **Rabbit** | Cul-de-Sac / Gather, surface court | Warren Flow, underground depth-and-flow, multiplicity of exits | **Conflicting** — needs an owned decision (see Option 1 / Option 2 above) |
| **Territory** | Median Interior / Shoulder Strip / Carriageway Gap | Home Median / Margin / Highway / Reach chain | **Parallel vocabulary** — needs remapping onto existing terms |
| **Buildings** | 6–7 universal functions | 12+ structure families incl. Staging Post, Guest House, Story Circle, Community Board | **Thinner** — missing families carry real mechanical weight elsewhere |

---

## Open questions for whoever picks this up

1. Does Rabbit keep Warren Flow's underground multiplicity-of-exits as the mechanical signature, with the Cul-de-Sac as its visible social face — or does the Cul-de-Sac replace it?
2. Where does the Relay Network's handoff-chain logistics actually show up inside a Manor House silhouette?
3. Should the spec's territory terms be retired in favor of canon's, or does canon's Margin/Highway/Reach vocabulary need a plain-language pass of its own?
4. Where do Staging Post, Guest House, Story Circle, and Community Board sit in the spec's six-function grammar — folded into existing functions, or kept as the additional "connective spatial element" the spec already allows for per species (Section 9 of the spec)?
