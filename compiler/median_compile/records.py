"""Phase 4 — atomic record schema.

Follows the compiler spec Appendix B4. Short keys are used in storage because
schemas and reports expand them for humans, and because every record carries a
full verbatim quotation that dominates the payload.

The load-bearing validation here is `quote`: it must appear verbatim in the
source block named by `loc`. That single check is what makes a record
falsifiable. A claim without a locatable quotation is an assertion the model
made, not a fact the corpus contains.
"""

from __future__ import annotations

import re
from enum import Enum
from pathlib import Path

import yaml
from pydantic import BaseModel, Field, field_validator

RECORD_SCHEMA_VERSION = "1.0"

RECORD_ID_RE = re.compile(r"^[A-Z]{3,4}_[A-Z0-9]{1,8}:\d{4}$")
#: Coordinates are opaque. `3.1#2` is a distinct location from `3.1`, and a
#: model that "tidies" the suffix away points the record at the wrong passage.
COORD_RE = re.compile(r"^[0-9A-Za-z.]+(?:#\d+)?(?:¶\d+(?:#\d+)?)?$")


class ContentType(str, Enum):
    """Compiler spec §A7 typed record IDs."""

    REQ = "REQ"          # an operative requirement
    GUARD = "GUARD"      # a guardrail, prohibition, or limit
    TERM = "TERM"        # a definition or terminology note
    UI = "UI"            # an interface or presentation instruction
    EXAMPLE = "EXAMPLE"  # illustrative, not canonical unless marked
    SAY = "SAY"          # in-world voice, folklore, compact truth
    TUNE = "TUNE"        # a tuning value or provisional number
    OPEN = "OPEN"        # an explicitly unresolved question
    HISTORY = "HISTORY"  # version archaeology or rejected alternative


class Weight(str, Enum):
    """Publication weight, kept separate from content type (spec §A7)."""

    STATE = "STATE"    # the GDD states this as fact about the world
    SHOW = "SHOW"      # the game must show it; not necessarily stated
    SAY = "SAY"        # in-world voice
    SILENT = "SILENT"  # internal only; never reaches the reader


class Status(str, Enum):
    canonical = "canonical"
    provisional = "provisional"
    example = "example"
    rationale = "rationale"
    historical = "historical"
    tuning = "tuning"
    unresolved = "unresolved"
    superseded = "superseded"
    rejected = "rejected"


#: Review flags. Extraction raises these; it never resolves them.
FLAGS = {
    "possible_collision",   # may contradict another record; do not resolve
    "owner_unclear",        # no namespace fits; a human must assign one
    "claim_exceeds_quote",  # normalized claim asserts more than the quotation
    "split_claim",          # the claim continues outside this block
    "table_derived",        # extracted from a table row rather than prose
    "non_state_marker",     # source explicitly marks this as not STATE
    "internal_supersession",  # a later passage in the same source overrides
}


class AtomicRecord(BaseModel):
    """One independently actionable claim from one source block."""

    model_config = {"extra": "forbid"}

    id: str
    src: str
    loc: str
    quote: str
    claim: str
    type: ContentType
    weight: Weight
    status: Status
    owner: str
    terms: list[str] = Field(default_factory=list)
    deps: list[str] = Field(default_factory=list)
    flags: list[str] = Field(default_factory=list)

    @field_validator("id")
    @classmethod
    def _id_shape(cls, v: str) -> str:
        if not RECORD_ID_RE.match(v):
            raise ValueError(f"record id {v!r} must be SOURCE:NNNN")
        return v

    @field_validator("loc")
    @classmethod
    def _loc_shape(cls, v: str) -> str:
        if not COORD_RE.match(v):
            raise ValueError(f"coordinate {v!r} is malformed")
        return v

    @field_validator("quote", "claim")
    @classmethod
    def _not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("quote and claim must be non-empty")
        return v

    @field_validator("flags")
    @classmethod
    def _known_flags(cls, v: list[str]) -> list[str]:
        unknown = set(v) - FLAGS
        if unknown:
            raise ValueError(f"unknown flag(s): {sorted(unknown)}")
        return v


def load_namespaces(path: Path) -> set[str]:
    """Flatten the namespace tree into dotted strings.

    The tree nests to three levels because the Mode/Register architecture is
    three levels deep: Home Mode contains DWELL and EMBODY, Away Mode contains
    FIELD and CROSSING, and MEET is universal. `home.dwell.roles` therefore has
    to be expressible.

    `_` names the bare namespace at that level: `home: {_: ...}` is `home`,
    and `home: {dwell: {_: ...}}` is `home.dwell`.
    """
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    out: set[str] = set()

    def walk(node: dict, prefix: str) -> None:
        for key, value in node.items():
            name = prefix if key == "_" else (f"{prefix}.{key}" if prefix else key)
            if isinstance(value, dict):
                walk(value, name)
            elif name:
                out.add(name)

    walk(doc.get("namespaces") or {}, "")
    return out


def load_namespace_descriptions(path: Path) -> dict[str, str]:
    """Dotted namespace -> its one-line description.

    Extraction receives these, not bare names. With 86 namespaces and seams as
    fine as `items.supplies` (using a Supply) against `economy.recipes` (making
    one), a bare list asks the model to guess. The descriptions cost roughly
    1.3k tokens per call and buy the accuracy of the field that Phase 7
    clusters on.
    """
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    out: dict[str, str] = {}

    def walk(node: dict, prefix: str) -> None:
        for key, value in node.items():
            name = prefix if key == "_" else (f"{prefix}.{key}" if prefix else key)
            if isinstance(value, dict):
                walk(value, name)
            elif name:
                out[name] = " ".join(str(value).split())

    walk(doc.get("namespaces") or {}, "")
    return out


def namespace_mode(owner: str) -> str | None:
    """Which Mode a namespace belongs to, or None if cross-cutting.

    MEET is universal by ruling and returns 'universal' rather than a Mode.
    """
    head = owner.split(".", 1)[0]
    if head in {"home", "away"}:
        return head
    if head == "meet":
        return "universal"
    return None


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def quote_is_grounded(quote: str, block: str) -> bool:
    """Is the quotation actually present in the block it claims to come from?

    Whitespace-insensitive, because Markdown wrapping is not semantic. Nothing
    else is relaxed: a paraphrase must fail.
    """
    return normalize_ws(quote) in normalize_ws(block)


def validate_records(
    records: list[AtomicRecord],
    blocks: dict[str, str],
    namespaces: set[str],
    source_id: str,
) -> list[str]:
    """Structural checks that do not need a model. Compiler spec §5.6."""
    errors: list[str] = []
    seen: set[str] = set()

    for r in records:
        if r.src != source_id:
            errors.append(f"{r.id}: src {r.src!r} does not match source {source_id!r}")
        if not r.id.startswith(f"{source_id}:"):
            errors.append(f"{r.id}: record id does not carry its source prefix")
        if r.id in seen:
            errors.append(f"{r.id}: duplicate record id")
        seen.add(r.id)

        if r.loc not in blocks:
            errors.append(f"{r.id}: coordinate {r.loc!r} is not a block in this source")
        elif not quote_is_grounded(r.quote, blocks[r.loc]):
            errors.append(
                f"{r.id}: quote is not present verbatim at {r.loc} "
                f"— {r.quote[:60]!r}"
            )

        if r.owner not in namespaces and "owner_unclear" not in r.flags:
            errors.append(
                f"{r.id}: owner {r.owner!r} is not a registered namespace "
                "(flag owner_unclear instead of inventing one)"
            )

        if r.type is ContentType.EXAMPLE and r.status is Status.canonical:
            errors.append(f"{r.id}: an EXAMPLE may not be status canonical")
        if r.type is ContentType.OPEN and r.status is not Status.unresolved:
            errors.append(f"{r.id}: an OPEN record must be status unresolved")
        if r.weight is Weight.STATE and r.status in {
            Status.rejected,
            Status.historical,
        }:
            errors.append(f"{r.id}: {r.status.value} material may not carry weight STATE")

    return errors


def coverage(records: list[AtomicRecord], owned: list[str]) -> dict:
    """Which owned blocks produced no record. Compiler spec §5.5 ledger."""
    covered = {r.loc for r in records}
    missing = [c for c in owned if c not in covered]
    return {
        "blocks": len(owned),
        "covered": len(owned) - len(missing),
        "uncovered": missing,
        "records": len(records),
    }


def json_schema() -> dict:
    schema = AtomicRecord.model_json_schema()
    schema["$id"] = f"median-record-{RECORD_SCHEMA_VERSION}"
    return schema


# ---------------------------------------------------------------------------
# Schema 2.0 — the model emits a span, the compiler reconstitutes the record
# ---------------------------------------------------------------------------

SPAN_SCHEMA_VERSION = "2.0"


class SpanRecord(BaseModel):
    """What extraction actually returns under prompt 2.0.

    Measured against a real v1.0 call, `quote` was 33% of every record and
    `id`/`src`/`terms`/`deps` another 14% — all of it either text the compiler
    already holds or values it can assign. v1.0 also omitted `src` on all 218
    observed records, which would have failed validation corpus-wide. Asking
    for less is both cheaper and harder to get wrong.
    """

    model_config = {"extra": "forbid"}

    loc: str
    q0: str
    q1: str
    claim: str
    type: ContentType
    weight: Weight
    status: Status
    owner: str
    flags: list[str] = Field(default_factory=list)

    @field_validator("flags")
    @classmethod
    def _known_flags(cls, v: list[str]) -> list[str]:
        unknown = set(v) - FLAGS
        if unknown:
            raise ValueError(f"unknown flag(s): {sorted(unknown)}")
        return v


class SpanUnresolvable(ValueError):
    """The span markers do not locate a passage in the cited block."""


#: Markdown table furniture. A row reads as "Risk | Failure mode", but the
#: literal text is "| **Risk** | **Failure mode** |" with padding. A model
#: quoting the row semantically produces markers that are not verbatim
#: substrings. All 34 span failures in the first Sonnet run were this.
_TABLE_FURNITURE = re.compile(r"[|*]+")


def _project(text: str) -> tuple[str, list[int]]:
    """Flatten table markup, keeping a map back to original offsets.

    Matching happens on the projection so a semantically-quoted table row
    resolves; the quotation returned is sliced from the ORIGINAL text, so it
    stays verbatim, pipes and all.
    """
    out: list[str] = []
    index: list[int] = []
    prev_space = True
    for i, ch in enumerate(text):
        c = " " if _TABLE_FURNITURE.match(ch) or ch.isspace() else ch
        if c == " ":
            if prev_space:
                continue
            prev_space = True
        else:
            prev_space = False
        out.append(c)
        index.append(i)
    while out and out[-1] == " ":
        out.pop()
        index.pop()
    return "".join(out), index


def resolve_span(block: str, q0: str, q1: str) -> str:
    """Recover the full quotation between two markers.

    Insensitive to whitespace and Markdown table furniture, because neither is
    semantic. Nothing else is relaxed: a paraphrased marker still fails loudly
    rather than producing an invented quotation.
    """
    proj, index = _project(block)
    a, _ = _project(q0)
    b, _ = _project(q1)
    if not a or not b:
        raise SpanUnresolvable("empty span marker")

    i = proj.find(a)
    if i < 0:
        raise SpanUnresolvable(f"q0 not found in block: {q0[:50]!r}")
    j = proj.find(b, i)
    if j < 0:
        raise SpanUnresolvable(f"q1 not found at or after q0: {q1[:50]!r}")

    start = index[i]
    end = index[j + len(b) - 1] + 1
    return normalize_ws(block[start:end])


def hydrate(
    spans: list[SpanRecord],
    blocks: dict[str, str],
    source_id: str,
    start_number: int = 1,
    lexicon: set[str] | None = None,
) -> tuple[list[AtomicRecord], list[str]]:
    """Turn span records into full atomic records. Deterministic.

    IDs are assigned here, in document order, so the model can neither reuse
    nor renumber them. `src` comes from the ID. `quote` is reconstituted from
    the block. `terms` are found by scanning the resolved quotation.
    """
    out: list[AtomicRecord] = []
    errors: list[str] = []
    n = start_number

    for s in spans:
        block = blocks.get(s.loc)
        if block is None:
            errors.append(f"{source_id}:{n:04d}: coordinate {s.loc!r} is not a block")
            n += 1
            continue
        try:
            quote = resolve_span(block, s.q0, s.q1)
        except SpanUnresolvable as exc:
            errors.append(f"{source_id}:{n:04d} at {s.loc}: {exc}")
            n += 1
            continue

        terms = sorted(t for t in (lexicon or set()) if t in quote)
        out.append(
            AtomicRecord(
                id=f"{source_id}:{n:04d}",
                src=source_id,
                loc=s.loc,
                quote=quote,
                claim=s.claim,
                type=s.type,
                weight=s.weight,
                status=s.status,
                owner=s.owner,
                terms=terms,
                deps=[],
                flags=s.flags,
            )
        )
        n += 1

    return out, errors
