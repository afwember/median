# MEDIAN source-bounded atomic extraction

Allowed source: `M050-SRC-POPULATION-001` only
Allowed streams: `evidence_game_semantic`

Emit exactly one grounded disposition object per target block ID; never repeat
an ID. The
disposition block-ID set must exactly equal the supplied `target_blocks` block-ID
set. Context blocks never receive dispositions. Excluded blocks are omitted
offline. Use only `SOURCE_BLOCKS`; import no other sources, prior atoms, or
external knowledge.

Use supplied source and request IDs exactly. Never emit placeholder or invented
IDs or metadata. Do not return a sample object: complete the full target set.

## Approved content/provenance boundary

# MEDIAN v0.5.0 Population Content/Provenance Identity Card v0.1

Date: 2026-08-04  
Status: `APPROVED`  
Lifecycle state: `identity_card_approved`  
Author/root of authority: Asa Wember  
Scope: source identity only; provider transmission, spend, and later-phase authority remain separate

## 1. Source identity

| Field | Bound value |
|---|---|
| Source ID | `M050-SRC-POPULATION-001` |
| Label | Population, Growth & Colony Tiers — Named Citizens, Continuity, and Civic Maturity |
| Path | `m050/docs/v0.5/specifications/M050_Population_Growth_and_Colony_Tiers_Specification_v1_0_MEDIANv0_5_0.md` |
| SHA-256 | `c818a5e13617835e0b6f18095b2ca69128028cd26406bbea6a11c0eeeb4c0981` |
| Displayed document version | `1.0` |
| Displayed date | `30 July 2026` |
| Displayed type | `System Architecture Specification` |
| Displayed target | `MEDIAN v0.5.0 Concept Sourcebook / desktop-console manifestation` |
| Gate 2 content role | `dedicated_population_and_tiers_game_specification` |
| Gate 2 disposition | `source_bounded_atomic_extraction` |
| Allowed output stream | `evidence_game_semantic` only |
| Existing extraction evidence | No accepted Population candidate or active Population extraction artifacts exist |
| Current compile position | Ordinal 9; next outstanding source after completed Away and legacy-seed Crossing |

The source ID, path, hash, role, disposition, output stream, and position agree
across the frozen source-state matrix and canonical processing order.

## 2. Source-declared role, scope, and status

The source says it defines the v0.5 population model, three population-growth
paths, the Nursery and young-Citizen lifecycle, and four Colony Tiers. It says
it replaces an older production-oriented population model.

The source declares its structural rules canonical for v0.5. It separately
qualifies numerical population bands and advancement thresholds as reference
targets that may move during implementation testing, subject to the stated
low-population and species-relative constraints. Its open-tuning section leaves
specified pacing, duration, threshold, and lifecycle values unresolved. These
status distinctions must remain attached to extracted evidence and do not
constitute Layer E semantic acceptance.

## 3. Provenance and declared lineage

Repository history first contains the frozen Markdown in commit
`d294d4c528f98dd0790804b0b305a053a90af17e` on 2026-08-02. Two unregistered
same-title representations exist:

- `500 log/MEDIAN_v0_5_0_Population_Growth_and_Colony_Tiers_Specification_v1_0.pdf`,
  SHA-256 `4a0952a99a66e6bac146a10353e1528c6e03191a0bca05039c2263a3f9a98326`;
- `500 log/old/MEDIAN_v0_5_0_Population_Growth_and_Colony_Tiers_Specification_v1_0.docx`,
  SHA-256 `6ab69bfa5e4b630e39201edd675dcdf3f480d29bed18677ff7524c73b3cb543c`.

Those files establish repository lineage only. The frozen registered Markdown
is the sole extraction source.

The source declares a precedence relationship to the following registered
sources. These IDs record unresolved traceability only; no external content,
meaning, precedence, or conformance conclusion is imported into this card or a
provider payload:

- `M050-SRC-PA-001`
- `M050-SRC-HOME-001`
- `M050-SRC-AWAY-001`
- `M050-SRC-GUEST-001`
- `M050-SRC-047-CROSS-SYSTEM-CARRYFORWARD-001`
- `M050-SRC-GDD-046-001`

The source also names “story-colony material” without a unique canonical source
ID. That reference remains unresolved and supplies no extraction content.

## 4. Extraction boundary and qualification handling

- Extract only game-semantic evidence present in the frozen Population
  Markdown.
- Preserve substantive rules, definitions, distinctions, procedures, tables,
  examples, negative rules, supersession claims, non-goals, acceptance tests,
  and final statements.
- Preserve the source's exact canonical, reference-target, tunable, optional,
  provisional, normally, may, and unresolved force wherever applicable.
- Treat the declared precedence table as source-bounded provenance evidence,
  not as permission to consult other sources or adjudicate cross-source
  authority.
- Do not infer MSID validity, external conformance, tuned implementation,
  authorial rules, manifestation-wide requirements, publication decisions, or
  reconciliation outcomes.
- Source-bounded candidate acceptance will not be semantic acceptance, mapping,
  reconciliation, canonization, or compiled prose.

## 5. Media disposition

The frozen Markdown contains no embedded image, audio, video, external URL, or
repository-media reference. There are zero media occurrences and zero
media-associated captions requiring disposition. HTML and Markdown tables are
source text, not media.

The unregistered PDF and DOCX are excluded representations. Their binaries,
layout, images, OCR or pixel-contained text, metadata, and text are prohibited
from the derived extraction representation and provider payload.

## 6. Exclusions

Use the established source-agnostic disposition vocabulary for document-control
furniture, Contents navigation, nonsemantic whitespace, source-position
comments, pure structural headings, and table delimiters. Do not exclude
substantive qualified or unresolved material merely because it is not final
positive canon.

The Population extraction must contain no content imported from another source,
no external media or representation content, no credentials, and no work from
a later compile stage.

## 7. Approval resolution and transition boundary

Asa Wember approved this source identity, provenance, qualification handling,
allowed stream, media disposition, and exclusion boundary. Git records the
transition; no separate approval receipt exists.

This approval permits the established offline scaffold and representative
pilot preparation under the active Population-only source grant and cumulative
budget. Provider readiness still derives from validated frozen bindings,
completed offline and replay gates, sequential review, and sufficient budget.
It does not authorize another source, semantic acceptance, mapping,
reconciliation, canonization, compiled prose, or Google Sheets interaction.

## Extraction contract

Split independent claims into separate atoms and keep dependent qualifications
with the claims they qualify. Every `exact_source_text` must be a byte-for-byte
contiguous substring of its target block after JSON decoding. Exact spans retain
markup and escaping. If markup interrupts prose, include it or split the atom.

Obey target constraints exactly. `required_disposition` fixes `kind`; when it
is `no_substantive_claim`, emit empty `atoms`. `allowed_dispositions` restricts
kind, and `minimum_atoms` is a floor. Pure structural headings, labels, table headers, delimiters, and
document-control metadata carry no substantive atom; never turn a label into a tautological
claim that its section discusses the announced topic. Structural context never
excuses a dependent substantive target from receiving its own disposition.

For every substantive table row, cover every nonempty semantic cell. Ground
independent properties, functions, effects, examples, interpretations, stages,
actions, and results as separate atoms. Combine cells only when one qualifies
another or the relationship is indivisible. Preserve both endpoints of
categorical mappings.
Independently headed descriptive columns and semicolon-separated effects require
separate atoms.
Each independent table-cell assertion requires exact source text from its own
cell; never ground a ruling or consequence only in another cell.

Preserve provisional, historical, rejected, example, negative, conditional,
scope, ownership, and authority qualifiers. Use `review_required` instead of
guessing. Never silently repair source text or invent identifiers, statuses,
definitions, owners, or authorities.

## Output check

Verify count equals `required_target_disposition_count`, coverage, no context dispositions, grounding, and
cardinality. Return JSON only under the bound
response schema. `atoms` must be nonempty only when kind is `atoms`; it must be
empty otherwise. Every atom must use supplied source and target block IDs, an
allowed stream, exact source text, a concise normalized claim, and a
source-faithful claim kind. Derive each proposal ID from its target block ID plus
a local atom ordinal so proposal IDs remain unique across the source.
