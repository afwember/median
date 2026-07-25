# Illustration prompts

One per plate, numbered in build order.

## The three utility files

Underscore-prefixed, pure prompt text with no commentary, so they can be dragged straight into ChatGPT or Nano Banana alongside a target image.

| File | Use |
|---|---|
| `_house_style.md` | Paste at the **top of every new plate prompt**, and attach the current reference plate as the first image. The plate-specific brief follows it |
| `_op_text_removal.md` | Drag in **with a finished plate** to produce a stripped base for recompositing type |
| `_op_upscale.md` | Drag in **with any image** to raise resolution without redrawing it |

**The house style travels as text plus an attached style plate.** An earlier version of this note claimed a visual style guide would not work — that models imitate pictures and cannot parse specification sheets. **That was wrong**, and a year of image-to-image practice on this project's other work disproves it: a reference plate carrying both a rendered subject *and* an annotated breakdown holds its specification across wildly varying framing, lighting, pose and occlusion.

**The real rule is narrower: annotation works when it is anchored to a depiction.** A palette swatch beside a garment rendered in that colour is reinforcement. A palette swatch alone is abstract, and abstract is what fails. So the style plate must **depict its own components** — the actual paper, a real panel with its hairline rule and badge, a fragment of illustration at working scale, the header and footer bars as drawn objects — each labelled, rather than described in the void.

**Include a type specimen on it.** A heading, a label, a body line and a caption in the actual faces. The one place drift is still expected is typography, because a plate carrying different words each time is not *preserving* lettering as an image feature — it is setting new text in a matching face, which is a harder task. A rendered specimen gives the model something to match rather than infer.

**Both operation prompts are written against observed failures.** The removal prompt fights reflow, because the strip pass reliably preserves text zones beside and below artwork and destroys the ones above it. The upscale prompt fights element drift and text corruption, because a resolution pass re-generates rather than enlarges — one quietly reduced a warren's bolt holes, and another turned *Low load* into *Low food*.

**Any upscale gets a full canon re-check afterward**, including a read of every text string.

**Never name a file inside a prompt.** Every reference is to *"the image attached to this message,"* explicitly disregarding filenames. Naming a specific plate broke a run once: the file had been renamed, the model went looking for a name that no longer existed, and the reference was ignored even though the right image was attached. This applies to the notes at the top of each prompt file too — those get read along with everything else when the file is dragged in, so they must never point at something the model cannot see.

**Method, three passes.** Generate with every string specified verbatim —
that is what makes generated text render legibly rather than as gibberish.
Reskin in one short oppositional line if the register is wrong. Strip text
only if the plate needs a recompositable base.

**State the downstream use, not just the constraint.** Telling the model an
asset will be "recomposited offline as editable vector type" improves
compliance, because it can then make sensible calls in cases the instruction
does not cover.

`_superseded/` holds prompts that were replaced, with a header on each
explaining what went wrong. They are kept deliberately: one records that
asking for blank reserved panels instead of specified text produces a
canon-clean, completely lifeless page.
