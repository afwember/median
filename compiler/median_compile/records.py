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


class Voice(str, Enum):
    """The lantern test — the only part of publication weight that is knowable
    from the passage alone.

    Extraction can see whether a sentence describes MEDIAN or describes the
    act of designing MEDIAN. It cannot see whether the finished book will state
    it, show it, or keep it internal: SAY comes from the Stage 9 harvest and
    SHOW from Stage 10 Section Contracts, neither of which exists yet.

    Asked for the full STATE/SHOW/SAY/SILENT vocabulary, extraction produced a
    noisy restatement of `type`: across 297 pilot records it marked 8 GUARDs
    and 10 OPENs as SILENT — conflating "not yet settled", which is `status`,
    with "not published", which is weight.
    """

    world = "world"      # describes MEDIAN
    process = "process"  # describes designing MEDIAN


class Weight(str, Enum):
    """Publication weight. Assigned after the architecture is frozen, never at
    extraction. Retained here because the Migration Ledger and Section
    Contracts need the vocabulary."""

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
    "span_end_inferred",    # q1 was approximate; the endpoint was located by suffix
    "manual",               # authored by hand, not by extraction
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
    voice: Voice
    #: Assigned at Stage 9/10, not here. None until then.
    weight: Weight | None = None
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
        if r.weight is not None:
            errors.append(
                f"{r.id}: weight is assigned after the architecture is frozen, "
                "not at extraction"
            )

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

SPAN_SCHEMA_VERSION = "3.0"


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
    voice: Voice
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
_TABLE_FURNITURE = "|*"

#: Typography the model silently normalises and the source does not. Curly
#: apostrophes (U+2019) and HTML entities left by the DOCX conversion caused
#: seven span failures across the two v3.0 pilots: the source holds
#: "Crow’s own result" and "-&gt;", the model writes "Crow's own result" and
#: "->". None of this is semantic, so none of it should decide whether a
#: quotation is grounded.
_FOLD = {
    "\u2018": "'", "\u2019": "'", "\u201a": "'", "\u201b": "'",
    "\u201c": '"', "\u201d": '"', "\u201e": '"',
    "\u2013": "-", "\u2014": "-", "\u2212": "-", "\u2010": "-", "\u2011": "-",
    "\u00a0": " ", "\u2009": " ", "\u202f": " ", "\u200b": "",
    "\u2026": "...",
}

_ENTITIES = {
    "&gt;": ">", "&lt;": "<", "&amp;": "&", "&quot;": '"',
    "&apos;": "'", "&nbsp;": " ", "&#39;": "'", "&#8217;": "'",
}


def _project(text: str) -> tuple[str, list[int], list[int]]:
    """Fold away everything non-semantic, keeping a map back to the original.

    Matching happens on the projection, so a table row quoted across cells, or
    a passage whose curly quotes the model straightened, still resolves. The
    quotation returned is sliced from the ORIGINAL text and stays verbatim.

    Returns the projected string plus, per projected character, the start and
    end offsets it came from. Entities fold several source characters into one,
    so a single index is not enough.
    """
    out: list[str] = []
    starts: list[int] = []
    ends: list[int] = []
    prev_space = True
    i = 0
    n = len(text)

    while i < n:
        # HTML entities first: they are several characters standing for one.
        matched = None
        if text[i] == "&":
            for ent, rep in _ENTITIES.items():
                if text.startswith(ent, i):
                    matched = (ent, rep)
                    break
        if matched:
            ent, rep = matched
            span_end = i + len(ent)
            for ch in rep:
                out.append(ch)
                starts.append(i)
                ends.append(span_end)
            prev_space = rep.endswith(" ")
            i = span_end
            continue

        ch = _FOLD.get(text[i], text[i])
        if not ch:  # zero-width
            i += 1
            continue
        if ch in _TABLE_FURNITURE or ch.isspace():
            ch = " "
        if ch == " ":
            if prev_space:
                i += 1
                continue
            prev_space = True
        else:
            prev_space = False
        for c in ch:  # ellipsis folds to three characters
            out.append(c)
            starts.append(i)
            ends.append(i + 1)
        i += 1

    while out and out[-1] == " ":
        out.pop()
        starts.pop()
        ends.pop()
    return "".join(out), starts, ends


def resolve_span(block: str, q0: str, q1: str) -> str:
    """Recover the full quotation between two markers.

    Insensitive to whitespace and Markdown table furniture, because neither is
    semantic. Nothing else is relaxed: a paraphrased marker still fails loudly
    rather than producing an invented quotation.
    """
    proj, starts, ends = _project(block)
    a, _, _ = _project(q0)
    b, _, _ = _project(q1)
    if not a or not b:
        raise SpanUnresolvable("empty span marker")

    i = proj.find(a)
    if i < 0:
        raise SpanUnresolvable(f"q0 not found in block: {q0[:50]!r}")
    j = proj.find(b, i)
    if j < 0:
        raise SpanUnresolvable(f"q1 not found at or after q0: {q1[:50]!r}")

    return normalize_ws(block[starts[i] : ends[j + len(b) - 1]])


def _ends_block(quote: str, block: str) -> bool:
    """Does the quotation reach the end of its block?

    Only then can a claim plausibly continue into the next one.
    """
    b, q = normalize_ws(block), normalize_ws(quote)
    return bool(q) and b.endswith(q[-40:] if len(q) > 40 else q)


#: Fewest words, and fewest characters, a q1 suffix may shrink to before the
#: match stops being trustworthy. Below this a fragment like "day." could land
#: almost anywhere in the block.
_MIN_SUFFIX_WORDS = 2
_MIN_SUFFIX_CHARS = 8


def load_manual(path: Path) -> dict[str, list["SpanRecord"]]:
    """Human-authored span records, keyed by source.

    Extraction fails on a block occasionally — a paraphrased marker, an
    inflection changed. Coverage shows the hole, but there was no way to fill
    it. These records hydrate exactly like extracted ones, are grounded against
    the source the same way, and carry the `manual` flag so they are never
    mistaken for machine output.
    """
    if not path.exists():
        return {}
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    out: dict[str, list[SpanRecord]] = {}
    for row in doc.get("records") or []:
        row = dict(row)
        src = row.pop("source")
        row.setdefault("flags", [])
        if "manual" not in row["flags"]:
            row["flags"] = [*row["flags"], "manual"]
        out.setdefault(src, []).append(SpanRecord.model_validate(row))
    return out


def resolve_span_with_fallback(block: str, q0: str, q1: str) -> tuple[str, bool]:
    """Resolve a span, retrying with progressively shorter tails of `q1`.

    Extraction sometimes reconstructs the closing marker instead of copying it,
    dropping a word from the middle: it wrote "or two Citizens in one day."
    where the source says "or by two Citizens in one day." The final words are
    still verbatim and still in the right place, so the endpoint is locatable
    without inventing anything.

    Returns the quotation and whether the endpoint was inferred. An inferred
    endpoint is flagged on the record; it is not silently accepted.
    """
    try:
        return resolve_span(block, q0, q1), False
    except SpanUnresolvable as exact_failure:
        if "q0 not found" in str(exact_failure):
            raise  # the location itself is wrong; a shorter tail cannot help

    words = normalize_ws(q1).split()
    for take in range(len(words) - 1, _MIN_SUFFIX_WORDS - 1, -1):
        tail = " ".join(words[-take:])
        if len(tail) < _MIN_SUFFIX_CHARS:
            break
        try:
            return resolve_span(block, q0, tail), True
        except SpanUnresolvable:
            continue
    raise SpanUnresolvable(
        f"q1 not found at or after q0, and no trustworthy tail of it either: {q1[:50]!r}"
    )


def hydrate(
    spans: list[SpanRecord],
    blocks: dict[str, str],
    source_id: str,
    start_number: int = 1,
    lexicon: set[str] | None = None,
) -> tuple[list[AtomicRecord], list[str], int]:
    """Turn span records into full atomic records. Deterministic.

    IDs are assigned here, in document order, so the model can neither reuse
    nor renumber them. `src` comes from the ID. `quote` is reconstituted from
    the block. `terms` are found by scanning the resolved quotation.

    Returns the next free record number as well as the records. A failed span
    still consumes its ID, so a caller that restarts from the record count
    reissues numbers — which produced five duplicate IDs on SPEC_HOME.
    """
    out: list[AtomicRecord] = []
    errors: list[str] = []
    corrected: list[str] = []
    n = start_number

    for s in spans:
        block = blocks.get(s.loc)
        if block is None:
            errors.append(f"{source_id}:{n:04d}: coordinate {s.loc!r} is not a block")
            n += 1
            continue
        try:
            quote, inferred = resolve_span_with_fallback(block, s.q0, s.q1)
        except SpanUnresolvable as exc:
            errors.append(f"{source_id}:{n:04d} at {s.loc}: {exc}")
            n += 1
            continue

        flags = list(s.flags)
        if inferred and "span_end_inferred" not in flags:
            flags.append("span_end_inferred")
        # A span that ends before the end of its block cannot continue into
        # another block. Extraction applied split_claim to 27 such records on
        # SPEC_CROSS, reading it as "this block holds other claims too" — the
        # ordinary case. Dropping it here keeps the flag meaningful for Phase 5,
        # which uses it to find genuinely truncated rules.
        if "split_claim" in flags and not _ends_block(quote, block):
            flags.remove("split_claim")
            corrected.append(f"{source_id}:{n:04d}")

        terms = sorted(t for t in (lexicon or set()) if t in quote)
        out.append(
            AtomicRecord(
                id=f"{source_id}:{n:04d}",
                src=source_id,
                loc=s.loc,
                quote=quote,
                claim=s.claim,
                type=s.type,
                voice=s.voice,
                status=s.status,
                owner=s.owner,
                terms=terms,
                deps=[],
                flags=flags,
            )
        )
        n += 1

    if corrected:
        errors.append(
            f"{source_id}: dropped split_claim from {len(corrected)} record(s) "
            "whose span ends mid-block (advisory, not a failure)"
        )
    return out, errors, n
