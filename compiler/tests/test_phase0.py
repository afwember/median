"""Phase 0 and Phase 1 acceptance tests.

Each test here corresponds to a failure that actually occurred during
development, or to a guarantee the compiler spec requires before the
normalization pipeline may be frozen and tagged.
"""

from __future__ import annotations

import dataclasses
import json
import re

import pytest
from pydantic import ValidationError

from median_compile import normalize as nz
from median_compile import probe as pb
from median_compile.models import SourceEntry

# --------------------------------------------------------------------------
# Probe — regression on the CATCHALL_3 misclassification
# --------------------------------------------------------------------------

RULING_FRONT = """# MEDIAN v0.5 — Baseline Disposition Ledger
## Checkpoint: Material Economy, Civic Production, Supplies, Tools

**Checkpoint date:** 30 July 2026
**Status:** Authoritative working ledger for later specification authoring
**Scope:** Adopted baseline rulings through BSA-11A, plus supersessions

## Document Doctrine

This ledger preserves adopted rulings at specification-level detail. It is not
the final polished STATE specification, but it is the controlling working
record for subsequent synthesis.

# BSA-01 — Laws and Sayings

**Adopted in full.**

# BSA-02 — Deep Laws

**Adopted.**

**Designer commentary only. Not STATE material.**
"""


def test_probe_flags_ruling_document_declared_as_pass():
    """The original error: CATCHALL_3 classed by filename as a supplementary pass.

    The probe must disagree loudly enough that a human looks at the doctrine
    block before the source is compiled.
    """
    p = pb.probe_text(RULING_FRONT, "RULE_BSA", "supplementary_pass")
    assert p.flags, "a ruling document declared as a pass must be flagged"
    assert any("claims authority" in f for f in p.flags)


def test_probe_accepts_correctly_declared_ruling():
    p = pb.probe_text(RULING_FRONT, "RULE_BSA", "human_ruling")
    assert not any("claims authority" in f for f in p.flags)


def test_probe_always_reports_non_state_markers():
    """Non-STATE blocks must reach Phase 4 whatever the document's class."""
    for declared in ("human_ruling", "detailed_spec", "supplementary_pass"):
        p = pb.probe_text(RULING_FRONT, "X", declared)
        assert any("non-STATE" in f for f in p.flags)


def test_governing_alone_does_not_flag():
    """'governing premise' is ordinary prose and flagged five documents falsely."""
    text = "# Spec\n\nThis document defines the version boundary and governing principles.\n"
    p = pb.probe_text(text, "SPEC_X", "detailed_spec")
    assert not any("claims authority" in f for f in p.flags)


def test_stub_is_flagged_as_not_a_specification():
    p = pb.probe_text("# Plan\n\nSkeleton only.\n", "SPEC_AUG", "detailed_spec")
    assert any("stub" in f for f in p.flags)


# --------------------------------------------------------------------------
# Normalizer — structure accounting
# --------------------------------------------------------------------------


def test_heading_tight_against_thematic_break_is_not_swallowed():
    """Every Part boundary in the v0.4.6 baseline is written this way."""
    text = "Some closing text.\n\n---\n# PART I — WHAT MEDIAN IS\n\nOpening line.\n"
    result = nz.annotate(text, "BASE_046")
    assert result.headings == 1, "the Part heading must be recognised"
    assert "<!--@1-->" in result.text


def test_all_headings_are_counted():
    text = "\n\n".join(f"# H{i}\n\nbody {i}" for i in range(1, 21))
    assert nz.annotate(text, "X").headings == 20


def test_every_block_receives_a_coordinate():
    text = "# One\n\nalpha\n\nbeta\n\n## Two\n\ngamma\n"
    result = nz.annotate(text, "X")
    coords = nz.coordinates(result.text)
    assert "1¶1" in coords and "1¶2" in coords
    assert result.blocks == len([c for c in coords if "¶" in c])


def test_document_numbering_is_preferred_over_positional():
    text = "# 4. Core Ontology\n\nalpha\n\n## 4.2 Roles\n\nbeta\n"
    coords = nz.coordinates(nz.annotate(text, "X").text)
    assert "4¶1" in coords
    assert "4.2¶1" in coords


def test_tables_are_kept_whole():
    text = "# T\n\n| a | b |\n| --- | --- |\n| 1 | 2 |\n| 3 | 4 |\n"
    result = nz.annotate(text, "X")
    assert result.tables == 1
    assert result.blocks == 1, "a table must not be split across blocks"


def test_annotation_adds_no_content():
    text = "# One\n\nalpha beta\n\n| a | b |\n| --- | --- |\n| 1 | 2 |\n"
    result = nz.annotate(text, "X")
    stripped = nz.strip_anchors(result.text)
    assert re.sub(r"\s+", "", stripped) == re.sub(r"\s+", "", text)


# --------------------------------------------------------------------------
# Pseudo-headings — opt-in, and lossless apart from markup
# --------------------------------------------------------------------------


def test_pseudo_headings_are_off_by_default():
    text = "**Purpose**\n\nbody text here\n"
    assert nz.annotate(text, "X").headings == 0
    assert nz.annotate(text, "X").promoted == 0


def test_pseudo_headings_promote_when_enabled():
    text = "**Purpose**\n\nbody text here\n\n**Scope**\n\nmore body\n"
    result = nz.annotate(text, "PHIL_SPEC", pseudo_headings=True)
    assert result.promoted == 2
    assert result.headings == 2


def test_pseudo_heading_promotion_only_removes_markup():
    text = "**Purpose**\n\nbody text here\n"
    result = nz.annotate(text, "X", pseudo_headings=True)
    words_in = set(re.findall(r"[A-Za-z]+", text))
    words_out = set(re.findall(r"[A-Za-z]+", nz.strip_anchors(result.text)))
    assert words_in == words_out, "promotion must not drop or invent words"


@pytest.mark.parametrize(
    "line",
    [
        "**This is a full sentence that ends with a period.**",
        "**a very long bolded run of text that goes well past the eighty character ceiling for headings**",
        "**bold** and **more bold**",
        "not bold at all",
    ],
)
def test_pseudo_heading_rejects_non_headings(line):
    assert nz._is_pseudo_heading([line]) is None


# --------------------------------------------------------------------------
# Manifest models — controlled vocabularies and naming scheme rules
# --------------------------------------------------------------------------

BASE = {
    "path": "x.docx",
    "title": "T",
    "status": "active",
    "disposition": "compile",
}


def test_id_prefix_must_match_declared_class():
    with pytest.raises(ValidationError, match="implies source_class"):
        SourceEntry(id="SPEC_HOME", source_class="human_ruling", **BASE)


def test_malformed_id_is_rejected():
    for bad in ("spec_home", "SPEC HOME", "SPEC-HOME", "SPEC_TOOLONGTOPIC", "HOME"):
        with pytest.raises(ValidationError):
            SourceEntry(id=bad, source_class="detailed_spec", **BASE)


def test_unknown_prefix_is_rejected():
    with pytest.raises(ValidationError, match="unknown class prefix"):
        SourceEntry(id="XXXX_A", source_class="detailed_spec", **BASE)


def test_superseded_source_may_not_be_compiled():
    """Naming scheme rule 4 — record IDs are minted only from compiled rows."""
    payload = {**BASE, "status": "superseded"}
    with pytest.raises(ValidationError, match="must not carry disposition"):
        SourceEntry(id="SPEC_GUEST", source_class="detailed_spec", **payload)


def test_unknown_field_is_rejected():
    with pytest.raises(ValidationError):
        SourceEntry(
            id="SPEC_HOME", source_class="detailed_spec", includ_in_compile=True, **BASE
        )


# --------------------------------------------------------------------------
# Coordinate uniqueness — 95 duplicates appeared corpus-wide before this
# --------------------------------------------------------------------------


def test_repeated_section_numbers_get_unique_coordinates():
    """Appendices restart numbering; several sources reuse `3.1` under Parts."""
    text = "# 3.1 Alpha\n\nbody one\n\n# Part Two\n\n# 3.1 Beta\n\nbody two\n"
    coords = nz.coordinates(nz.annotate(text, "X").text)
    assert len(coords) == len(set(coords)), f"duplicate coordinates: {coords}"
    assert "3.1" in coords and "3.1#2" in coords


def test_coordinates_unique_across_a_long_document():
    text = "\n\n".join(
        f"# {n}. Section\n\nalpha\n\nbeta" for n in ([1, 2, 3] * 4)
    )
    coords = nz.coordinates(nz.annotate(text, "X").text)
    assert len(coords) == len(set(coords))


def test_media_paths_are_not_absolute(tmp_path):
    """Absolute sandbox paths must not leak into a committed artifact."""
    md = tmp_path / "s.md"
    md.write_text("# T\n\n![alt](img.png)\n", encoding="utf-8")
    result = nz.normalize(md, "X", tmp_path / ".media")
    assert str(tmp_path) not in result.text


# --------------------------------------------------------------------------
# Phase 2 — lean ruleset
# --------------------------------------------------------------------------

from median_compile import lean as ln  # noqa: E402


def _annotated(*blocks: str) -> str:
    return "\n".join(f"<!--@{i}-->\n{b}\n" for i, b in enumerate(blocks, 1))


def test_contents_section_is_removed():
    text = _annotated("## Contents", "- 1. Thesis\n- 2. Pillars", "## 1. Thesis", "Real canon.")
    r = ln.lean(text, "X")
    assert {x.rule for x in r.removals} == {"contents"}
    assert "Real canon." in r.text


def test_contents_removal_stops_at_the_next_heading():
    text = _annotated("## Contents", "- 1. Thesis", "## 1. Thesis", "body after contents")
    r = ln.lean(text, "X")
    assert "body after contents" in r.text
    assert "## 1. Thesis" in r.text


@pytest.mark.parametrize(
    "body",
    [
        "This specification supersedes v0.4.6.",
        "Precedence: the domain owner controls.",
        "Open question — deferred to Phase 10.",
        "**Adopted in full.**",
        "| a | b |\n| --- | --- |",
        "Capacity = Citizens × 1",
        "Non-goal: MEDIAN does not model combat.",
    ],
)
def test_protected_blocks_are_never_removed(body):
    """Compiler spec §6.3. The guard runs before the rules, not after."""
    r = ln.lean(_annotated("## Contents", body), "X")
    assert body in r.text, f"protected content removed: {body!r}"
    assert r.spared, "a spared block must be logged, not silently kept"


def test_every_removal_is_reversible():
    text = _annotated("## Contents", "- 1. Thesis", "---", "kept")
    r = ln.lean(text, "X")
    for x in r.removals:
        assert x.sha256 and x.coord and x.lines


def test_lean_is_a_strict_subsequence_of_full():
    text = _annotated("## Contents", "- 1. Thesis", "## Real", "canon", "---", "more")
    r = ln.lean(text, "X")
    full = re.findall(r"<!--@([^>]+)-->", text)
    kept = re.findall(r"<!--@([^>]+)-->", r.text)
    it = iter(full)
    assert all(c in it for c in kept), "lean must not reorder or invent blocks"


def test_lean_never_invents_text():
    text = _annotated("## Real", "alpha beta gamma")
    r = ln.lean(text, "X")
    assert set(re.findall(r"[a-z]+", r.text)) <= set(re.findall(r"[a-z]+", text))


def test_ordinary_prose_is_untouched():
    text = _annotated("## 1. Home", "Each Citizen contributes one unit of Capacity.")
    r = ln.lean(text, "X")
    assert not r.removals
    assert r.reduction == 0.0


# --------------------------------------------------------------------------
# Phase 3 — chunker
# --------------------------------------------------------------------------

from median_compile import chunk as ck  # noqa: E402


def _doc(n_blocks: int, block_chars: int = 400) -> str:
    parts = ["<!--@1-->\n# 1. Section\n"]
    for i in range(1, n_blocks + 1):
        parts.append(f"<!--@1¶{i}-->\n{'word ' * (block_chars // 5)}\n")
    return "\n".join(parts)


def test_every_block_is_owned_exactly_once():
    text = _doc(300)
    r = ck.chunk(text, "X", target_tokens=2000, max_tokens=3000)
    assert len(r.chunks) > 1, "test needs multiple chunks to be meaningful"
    assert not ck.validate(r, text)


def test_overlap_context_is_never_also_owned():
    text = _doc(300)
    r = ck.chunk(text, "X", target_tokens=2000, max_tokens=3000, overlap_tokens=400)
    for c in r.chunks:
        assert not (set(c.context) & set(c.owned))
    assert any(c.context for c in r.chunks[1:]), "overlap should carry context forward"


def test_tables_are_never_split():
    """A table far over the ceiling still lands in exactly one chunk, whole.

    The chunker may close a preceding chunk to make room — that is correct —
    but the table's own block must never be divided.
    """
    table = "| a | b |\n" + "\n".join(f"| {i} | {i} |" for i in range(400))
    text = f"<!--@1-->\n# T\n\n<!--@1¶1-->\n{table}\n"
    r = ck.chunk(text, "X", target_tokens=200, max_tokens=300)

    holders = [c for c in r.chunks if "1¶1" in c.owned]
    assert len(holders) == 1, "the table must be owned by exactly one chunk"
    assert holders[0].text.count("| 399 | 399 |") == 1
    assert holders[0].text.count("| 0 | 0 |") == 1, "first and last row in one place"
    assert not ck.validate(r, text)


def test_oversized_block_is_reported_not_broken():
    text = f"<!--@1-->\n# T\n\n<!--@1¶1-->\n{'word ' * 5000}\n"
    r = ck.chunk(text, "X", target_tokens=200, max_tokens=300)
    assert r.oversized, "an oversized chunk must be reported"
    assert not ck.validate(r, text), "and must still own its block"


def test_chunk_ids_are_stable_and_well_formed():
    text = _doc(120)
    a = ck.chunk(text, "SPEC_HOME", target_tokens=2000, max_tokens=3000)
    b = ck.chunk(text, "SPEC_HOME", target_tokens=2000, max_tokens=3000)
    assert [c.id for c in a.chunks] == [c.id for c in b.chunks]
    assert [c.sha256 for c in a.chunks] == [c.sha256 for c in b.chunks]
    assert all(re.fullmatch(r"SPEC_HOME:C\d{3}", c.id) for c in a.chunks)


def test_ownership_follows_document_order():
    text = _doc(200)
    r = ck.chunk(text, "X", target_tokens=1500, max_tokens=2500)
    owned = [c for chunk_ in r.chunks for c in chunk_.owned]
    expected = [b.coord for b in ck.parse_blocks(text)]
    assert owned == expected


def test_heading_path_is_recorded():
    text = (
        "<!--@1-->\n# 1. Home\n\n<!--@1¶1-->\nalpha\n\n"
        "<!--@1.1-->\n## 1.1 Roles\n\n<!--@1.1¶1-->\nbeta\n"
    )
    r = ck.chunk(text, "X")
    assert r.chunks[0].heading_path == ("1. Home",)


def test_validate_catches_a_dropped_block():
    text = _doc(50)
    r = ck.chunk(text, "X")
    r.chunks[0].owned.pop()
    assert any("owned by no chunk" in e for e in ck.validate(r, text))


# --------------------------------------------------------------------------
# Build Record — provenance and staleness
# --------------------------------------------------------------------------

from median_compile import record as rec  # noqa: E402
from median_compile.config import Build  # noqa: E402


@pytest.fixture()
def build(tmp_path):
    b = Build(tmp_path / "build" / "v0.5")
    b.init()
    return b


def test_run_is_recorded_with_provenance(build):
    with rec.record(build, "chunk", "chunk", {"chunker": "1.0"}) as run:
        run.metrics = {"chunks": 39}
    (entry,) = rec.history(build)
    assert entry["phase"] == "chunk"
    assert entry["status"] == "ok"
    assert entry["versions"]["chunker"] == "1.0"
    assert entry["metrics"]["chunks"] == 39
    assert entry["timestamp"] and entry["operator"] and entry["python"]


def test_failed_runs_are_recorded_too():
    """A record containing only successes hides the history worth keeping."""


def test_failed_run_is_logged_and_reraised(build):
    with pytest.raises(ValueError):
        with rec.record(build, "manifest", "manifest"):
            raise ValueError("boom")
    (entry,) = rec.history(build)
    assert entry["status"] == "error"
    assert "boom" in entry["notes"]


def test_record_is_append_only(build):
    for i in range(3):
        with rec.record(build, "chunk", "chunk") as run:
            run.metrics = {"n": i}
    assert [e["metrics"]["n"] for e in rec.history(build)] == [0, 1, 2]


def test_clean_build_is_not_stale(build):
    with rec.record(build, "chunk", "chunk") as run:
        run.inputs = {"SPEC_HOME": "aaa", "SPEC_AWAY": "bbb"}
    current = {"chunk": {"SPEC_HOME": "aaa", "SPEC_AWAY": "bbb"}}
    assert rec.staleness(build, current) == {}


def test_changed_input_is_detected(build):
    with rec.record(build, "chunk", "chunk") as run:
        run.inputs = {"SPEC_HOME": "aaa"}
    stale = rec.staleness(build, {"chunk": {"SPEC_HOME": "zzz"}})
    assert stale["chunk"] == ["SPEC_HOME (changed)"]


def test_partial_runs_accumulate(build):
    """`--source X` records one input; the rest must not then look new."""
    with rec.record(build, "normalize-lean", "normalize-lean") as run:
        run.inputs = {"A": "1", "B": "2"}
    with rec.record(build, "normalize-lean", "normalize-lean") as run:
        run.inputs = {"A": "9"}
    assert rec.accumulated_inputs(build, "normalize-lean") == {"A": "9", "B": "2"}
    assert rec.staleness(build, {"normalize-lean": {"A": "9", "B": "2"}}) == {}


def test_errored_runs_do_not_count_as_provenance(build):
    with pytest.raises(RuntimeError):
        with rec.record(build, "chunk", "chunk") as run:
            run.inputs = {"A": "1"}
            raise RuntimeError("failed midway")
    assert rec.accumulated_inputs(build, "chunk") == {}


def test_chunk_text_carries_coordinate_anchors():
    """Extraction must report the `loc` of every record.

    If the chunk handed to the model has no `<!--@coord-->` markers, that is
    impossible — the model cannot cite what it cannot see. This was only
    caught when Pass A returned zero records against the fake provider.
    """
    text = "<!--@1-->\n# H\n\n<!--@1¶1-->\nalpha\n\n<!--@1¶2-->\nbeta\n"
    r = ck.chunk(text, "X")
    body = r.chunks[0].text
    for coord in r.chunks[0].owned:
        assert f"<!--@{coord}-->" in body, f"{coord} unciteable in chunk text"


def test_context_blocks_are_also_anchored():
    text = "\n\n".join(f"<!--@1¶{i}-->\n{'word ' * 200}" for i in range(1, 60))
    r = ck.chunk(text, "X", target_tokens=1000, max_tokens=1500, overlap_tokens=400)
    later = [c for c in r.chunks if c.context]
    assert later, "test needs a chunk with carried context"
    for c in later:
        for coord in c.context:
            assert f"<!--@{coord}-->" in c.text


# --------------------------------------------------------------------------
# Namespaces — Mode / Register architecture
# --------------------------------------------------------------------------

from pathlib import Path  # noqa: E402

from median_compile import records as rc  # noqa: E402


def test_namespace_tree_nests_to_three_levels(tmp_path):
    p = tmp_path / "ns.yaml"
    p.write_text(
        "namespaces:\n"
        "  home:\n"
        "    _: Home Mode\n"
        "    dwell:\n"
        "      _: DWELL\n"
        "      roles: Roles\n"
        "  meet:\n"
        "    _: MEET\n",
        encoding="utf-8",
    )
    assert rc.load_namespaces(p) == {"home", "home.dwell", "home.dwell.roles", "meet"}


@pytest.mark.parametrize(
    "owner,mode",
    [
        ("home.dwell.roles", "home"),
        ("home.embody.access", "home"),
        ("away.field.travel", "away"),
        ("away.crossing.risk", "away"),
        ("meet.choice", "universal"),
        ("items.tools", None),
        ("citizen.record", None),
    ],
)
def test_mode_is_derivable_from_owner(owner, mode):
    """Home encompasses DWELL and EMBODY; Away encompasses FIELD and CROSSING;
    MEET is universal. The owner string must carry that without a lookup."""
    assert rc.namespace_mode(owner) == mode


def test_all_five_registers_are_present():
    ns = rc.load_namespaces(
        Path(__file__).parents[2] / "build/v0.5/architecture/owner_namespaces.yaml"
    )
    for register in ("home.dwell", "home.embody", "away.field", "away.crossing", "meet"):
        assert register in ns, f"{register} missing from the namespace tree"


def test_extraction_may_not_invent_a_namespace():
    r = rc.AtomicRecord(
        id="SPEC_HOME:0001", src="SPEC_HOME", loc="1¶1",
        quote="alpha beta", claim="Alpha beta.", type="REQ",
        voice="world", status="canonical", owner="home.invented.thing",
    )
    errs = rc.validate_records([r], {"1¶1": "alpha beta"}, {"home.dwell"}, "SPEC_HOME")
    assert any("not a registered namespace" in e for e in errs)


def test_owner_unclear_flag_excuses_an_unknown_namespace():
    r = rc.AtomicRecord(
        id="SPEC_HOME:0001", src="SPEC_HOME", loc="1¶1",
        quote="alpha beta", claim="Alpha beta.", type="REQ",
        voice="world", status="canonical", owner="home",
        flags=["owner_unclear"],
    )
    errs = rc.validate_records([r], {"1¶1": "alpha beta"}, {"home.dwell"}, "SPEC_HOME")
    assert not any("namespace" in e for e in errs)


def test_quote_must_be_grounded_in_the_block():
    """A claim without a locatable quotation is an assertion, not a fact."""
    r = rc.AtomicRecord(
        id="SPEC_HOME:0001", src="SPEC_HOME", loc="1¶1",
        quote="a sentence that is not in the source", claim="X.", type="REQ",
        voice="world", status="canonical", owner="home.dwell",
    )
    errs = rc.validate_records([r], {"1¶1": "alpha beta"}, {"home.dwell"}, "SPEC_HOME")
    assert any("not present verbatim" in e for e in errs)


def test_grounding_ignores_whitespace_only():
    r = rc.AtomicRecord(
        id="SPEC_HOME:0001", src="SPEC_HOME", loc="1¶1",
        quote="Each  Citizen\ncontributes one unit.", claim="X.", type="REQ",
        voice="world", status="canonical", owner="home.dwell",
    )
    block = "Each Citizen contributes one unit."
    errs = rc.validate_records([r], {"1¶1": block}, {"home.dwell"}, "SPEC_HOME")
    assert not errs


def test_namespace_descriptions_are_loaded_for_the_prompt():
    """Bare names ask the model to guess; descriptions carry the seams."""
    d = rc.load_namespace_descriptions(
        Path(__file__).parents[2] / "build/v0.5/architecture/owner_namespaces.yaml"
    )
    assert "using a supply" in d["items.supplies"].lower()
    assert "making item units" in d["economy.recipes"].lower()
    assert set(d) == rc.load_namespaces(
        Path(__file__).parents[2] / "build/v0.5/architecture/owner_namespaces.yaml"
    )


def test_use_make_seam_is_stated_in_the_prompt():
    """Asa's ruling: items.* is using the unit, economy.recipes is building it."""
    prompt = (
        Path(__file__).parents[1] / "prompts" / "extract-1.0.md"
    ).read_text(encoding="utf-8")
    assert "use/make seam" in prompt
    assert "economy.recipes" in prompt and "items.supplies" in prompt


# --------------------------------------------------------------------------
# Extraction failure handling — a paid call must never be lost
# --------------------------------------------------------------------------

from median_compile import extract as ex  # noqa: E402


@dataclasses.dataclass
class _StubProvider:
    text: str
    stop_reason: str = "end_turn"
    name: str = "stub"
    model: str = "stub-1"

    def complete(self, system, user, max_tokens):
        return self.text, {
            "input_tokens": 100,
            "output_tokens": 200,
            "stop_reason": self.stop_reason,
        }


_CHUNK = {
    "id": "SPEC_HOME:C001",
    "source": "SPEC_HOME",
    "sha256": "abc123",
    "owned": ["1¶1"],
    "context": [],
    "heading_path": [],
    "text": "<!--@1¶1-->\nalpha beta",
    "tokens": 10,
}


def test_truncated_response_is_named_not_a_json_traceback(tmp_path):
    """The first real run died in json.loads with no hint of the cause."""
    truncated = '{"records": [{"id": "SPEC_HOME:0001", "quote": "unterminat'
    with pytest.raises(ex.Truncated, match="output ceiling"):
        ex.extract_chunk(
            _CHUNK, {}, [], 1, "sys",
            _StubProvider(truncated, stop_reason="max_tokens"),
            tmp_path, max_tokens=12_000,
        )


def test_raw_response_survives_a_truncation(tmp_path):
    """Tokens are charged before parsing. Losing the text wastes the money."""
    with pytest.raises(ex.Truncated):
        ex.extract_chunk(
            _CHUNK, {}, [], 1, "sys",
            _StubProvider('{"records": [trunc', stop_reason="max_tokens"),
            tmp_path,
        )
    raws = list(tmp_path.glob("*.raw.txt"))
    assert raws, "the raw response must be kept for diagnosis"
    assert "trunc" in raws[0].read_text()


def test_malformed_json_is_named_and_kept(tmp_path):
    with pytest.raises(ex.MalformedResponse, match="not valid record JSON"):
        ex.extract_chunk(
            _CHUNK, {}, [], 1, "sys", _StubProvider("I'm afraid I can't do that"),
            tmp_path,
        )
    assert list(tmp_path.glob("*.raw.txt"))


def test_a_failed_call_is_not_cached_as_success(tmp_path):
    """A bad response must not poison the cache and suppress a later retry."""
    with pytest.raises(ex.ExtractionError):
        ex.extract_chunk(
            _CHUNK, {}, [], 1, "sys", _StubProvider("nonsense"), tmp_path
        )
    assert not [p for p in tmp_path.glob("*.json")]


def test_a_good_response_caches_and_replays_free(tmp_path):
    payload = json.dumps({"records": [{"id": "SPEC_HOME:0001"}]})
    p = _StubProvider(payload)
    raw, call = ex.extract_chunk(_CHUNK, {}, [], 1, "sys", p, tmp_path)
    assert call.cached is False and raw
    raw2, call2 = ex.extract_chunk(_CHUNK, {}, [], 1, "sys", p, tmp_path)
    assert call2.cached is True and raw2 == raw


def test_default_ceiling_clears_observed_need():
    """12,000 truncated a real 9k-token chunk. The default must be well above."""
    assert ex.DEFAULT_MAX_OUTPUT_TOKENS >= 24_000


# --------------------------------------------------------------------------
# Schema 2.0 — span records, hydrated by the compiler
# --------------------------------------------------------------------------

BLOCK = (
    "Each present and available Citizen contributes one unit of Role Capacity, "
    "except while Away, in which case they contribute none."
)


def _span(**kw):
    base = dict(
        loc="4.2¶3", q0="Each present and available Citizen",
        q1="they contribute none.", claim="X.", type="REQ",
        voice="world", status="canonical", owner="home.dwell.roles",
    )
    base.update(kw)
    return rc.SpanRecord(**base)


def test_span_resolves_to_the_full_quotation():
    assert rc.resolve_span(BLOCK, "Each present and available", "contribute none.") == BLOCK


def test_span_is_whitespace_insensitive_only():
    assert rc.resolve_span(BLOCK, "Each  present\nand available", "contribute  none.")


def test_a_paraphrased_marker_fails_loudly():
    """The whole point: the compiler must not invent a quotation."""
    with pytest.raises(rc.SpanUnresolvable, match="q0 not found"):
        rc.resolve_span(BLOCK, "Every available Citizen provides", "contribute none.")


def test_q1_before_q0_is_rejected():
    with pytest.raises(rc.SpanUnresolvable, match="q1 not found"):
        rc.resolve_span(BLOCK, "except while Away", "Each present")


def test_hydrate_assigns_ids_and_derives_src():
    """v1.0 omitted `src` on all 218 observed records. Now it cannot."""
    recs, errs, _ = rc.hydrate([_span(), _span()], {"4.2¶3": BLOCK}, "SPEC_HOME", 7)
    assert not errs
    assert [r.id for r in recs] == ["SPEC_HOME:0007", "SPEC_HOME:0008"]
    assert all(r.src == "SPEC_HOME" for r in recs)


def test_hydrated_quote_is_grounded_by_construction():
    recs, _, _ = rc.hydrate([_span()], {"4.2¶3": BLOCK}, "SPEC_HOME")
    assert rc.quote_is_grounded(recs[0].quote, BLOCK)


def test_hydrate_finds_terms_from_the_lexicon():
    recs, _, _ = rc.hydrate(
        [_span()], {"4.2¶3": BLOCK}, "SPEC_HOME", lexicon={"Citizen", "Role Capacity", "Reach"}
    )
    assert recs[0].terms == ["Citizen", "Role Capacity"]


def test_unresolvable_span_becomes_an_error_not_a_record():
    recs, errs, _ = rc.hydrate(
        [_span(q0="not in the block at all")], {"4.2¶3": BLOCK}, "SPEC_HOME"
    )
    assert not recs and errs


def test_span_record_rejects_the_dropped_fields():
    """quote/id/src/terms/deps are the compiler's to supply, not the model's."""
    for extra in ("quote", "id", "src", "terms", "deps"):
        with pytest.raises(ValidationError):
            _span(**{extra: "x"})


def test_env_refs_in_config_are_expanded(tmp_path, monkeypatch):
    """config.yaml ships ${ANTHROPIC_EXTRACTION_MODEL} per the spec's rule that
    model IDs are configuration. Unexpanded, that literal was sent as a model
    name."""
    from median_compile.config import expand_env

    monkeypatch.setenv("ANTHROPIC_EXTRACTION_MODEL", "claude-sonnet-5")
    got = expand_env({"providers": {"extraction": {"model": "${ANTHROPIC_EXTRACTION_MODEL}"}}})
    assert got["providers"]["extraction"]["model"] == "claude-sonnet-5"


def test_missing_env_ref_expands_to_empty_not_the_literal():
    from median_compile.config import expand_env

    assert expand_env("${DEFINITELY_NOT_SET_12345}") == ""


def test_cache_key_separates_models():
    """Sonnet output must not be served from the Opus cache, or the comparison
    is meaningless."""
    a = ex.cache_key("sha", "2.0", "2.0", "anthropic", "claude-opus-5")
    b = ex.cache_key("sha", "2.0", "2.0", "anthropic", "claude-sonnet-5")
    assert a != b


def test_cache_key_separates_prompt_versions():
    a = ex.cache_key("sha", "1.0", "2.0", "anthropic", "m")
    b = ex.cache_key("sha", "2.0", "2.0", "anthropic", "m")
    assert a != b


TABLE_BLOCK = (
    "| **Risk**              | **Failure mode**                          |\n"
    "| --------------------- | ----------------------------------------- |\n"
    "| Entropy treadmill     | Deficiency-driven Encounters arrive daily |"
)


def test_table_row_span_resolves_across_cells():
    """All 34 failures in the first Sonnet run were this: a row quoted
    semantically, whose markers are not verbatim substrings because of pipes."""
    got = rc.resolve_span(TABLE_BLOCK, "Entropy treadmill Deficiency-driven", "arrive daily")
    assert "Entropy treadmill" in got and "arrive daily" in got


def test_resolved_table_quote_is_real_source_text():
    got = rc.resolve_span(TABLE_BLOCK, "Entropy treadmill", "arrive daily")
    assert rc.normalize_ws(got) in rc.normalize_ws(TABLE_BLOCK)


def test_bold_markers_do_not_block_a_span():
    got = rc.resolve_span("| **Named Citizen** | **occupies** | **Role** |",
                          "Named Citizen occupies", "Role")
    assert "Named Citizen" in got


def test_paraphrase_still_fails_after_table_tolerance():
    """Tolerating markup must not become tolerating invention."""
    with pytest.raises(rc.SpanUnresolvable):
        rc.resolve_span(TABLE_BLOCK, "Entropy spiral causes", "arrive daily")


def test_split_claim_dropped_when_span_ends_mid_block():
    """27 of 45 SPEC_CROSS records flagged split_claim on spans that ended
    mid-block, where the claim provably cannot continue anywhere."""
    block = "First rule here. Second rule here. Third rule ends the block."
    s = rc.SpanRecord(
        loc="1¶1", q0="First rule here.", q1="First rule here.", claim="X.",
        type="REQ", voice="world", status="canonical", owner="home.dwell",
        flags=["split_claim"],
    )
    recs, errs, _ = rc.hydrate([s], {"1¶1": block}, "SPEC_X")
    assert recs[0].flags == []
    assert any("dropped split_claim" in e for e in errs)


def test_split_claim_kept_when_span_reaches_the_block_end():
    """A genuinely truncated rule must keep the flag for Phase 5."""
    block = "A Citizen contributes one unit of Capacity, except"
    s = rc.SpanRecord(
        loc="1¶1", q0="A Citizen contributes", q1="Capacity, except", claim="X.",
        type="REQ", voice="world", status="canonical", owner="home.dwell",
        flags=["split_claim"],
    )
    recs, _, _ = rc.hydrate([s], {"1¶1": block}, "SPEC_X")
    assert recs[0].flags == ["split_claim"]


def test_other_flags_survive_the_correction():
    block = "First rule here. Second rule ends the block."
    s = rc.SpanRecord(
        loc="1¶1", q0="First rule here.", q1="First rule here.", claim="X.",
        type="REQ", voice="world", status="canonical", owner="home.dwell",
        flags=["split_claim", "table_derived"],
    )
    recs, _, _ = rc.hydrate([s], {"1¶1": block}, "SPEC_X")
    assert recs[0].flags == ["table_derived"]


# --------------------------------------------------------------------------
# Schema 3.0 — voice replaces weight at extraction
# --------------------------------------------------------------------------


def test_extraction_asks_only_the_lantern_test():
    """STATE/SHOW/SAY/SILENT depends on an architecture that does not exist at
    extraction. SAY is a Stage 9 harvest; SHOW comes from Section Contracts."""
    with pytest.raises(ValidationError):
        rc.SpanRecord(
            loc="1¶1", q0="a", q1="b", claim="X.", type="REQ",
            weight="STATE", status="canonical", owner="home.dwell",
        )


@pytest.mark.parametrize("voice", ["world", "process"])
def test_voice_accepts_both_values(voice):
    r = rc.SpanRecord(
        loc="1¶1", q0="a", q1="b", claim="X.", type="REQ",
        voice=voice, status="canonical", owner="home.dwell",
    )
    assert r.voice.value == voice


def test_hydrated_record_carries_voice_and_no_weight():
    block = "A Citizen contributes one unit."
    s = rc.SpanRecord(
        loc="1¶1", q0="A Citizen contributes", q1="one unit.", claim="X.",
        type="REQ", voice="world", status="canonical", owner="home.dwell",
    )
    recs, errs, _ = rc.hydrate([s], {"1¶1": block}, "SPEC_X")
    assert not errs
    assert recs[0].voice is rc.Voice.world
    assert recs[0].weight is None, "weight is assigned after architecture freeze"


def test_weight_set_at_extraction_is_an_error():
    r = rc.AtomicRecord(
        id="SPEC_X:0001", src="SPEC_X", loc="1¶1", quote="alpha beta",
        claim="X.", type="REQ", voice="world", weight="STATE",
        status="canonical", owner="home.dwell",
    )
    errs = rc.validate_records([r], {"1¶1": "alpha beta"}, {"home.dwell"}, "SPEC_X")
    assert any("after the architecture is frozen" in e for e in errs)


# --------------------------------------------------------------------------
# Typography folding — seven span failures across the v3.0 pilots
# --------------------------------------------------------------------------


def test_curly_apostrophe_matches_a_straight_one():
    """Source: "Crow’s own result". Model wrote: "Crow's own result"."""
    block = "Crow’s own result is independent of the ground party’s result."
    got = rc.resolve_span(block, "Crow's own result", "party's result.")
    assert "Crow’s" in got, "the stored quote must keep the source's own typography"


def test_html_entities_match_their_characters():
    """Source: "Stabilize -&gt; inhabit". Model wrote: "Stabilize -> inhabit"."""
    block = "<em>Stabilize -&gt; inhabit -&gt; desire something more</em>"
    got = rc.resolve_span(block, "Stabilize -> inhabit", "something more")
    assert "-&gt;" in got


def test_em_dash_and_ellipsis_fold():
    block = "The party commits — fully — and the run resolves…"
    assert rc.resolve_span(block, "The party commits - fully", "run resolves...")


def test_folding_does_not_excuse_a_paraphrase():
    block = "Crow’s own result is independent."
    with pytest.raises(rc.SpanUnresolvable):
        rc.resolve_span(block, "Crow decides the outcome", "independent.")


def test_hydrate_reports_the_next_free_id():
    """A failed span still consumes its ID. Restarting from the record count
    reissued numbers and produced five duplicate IDs on SPEC_HOME."""
    block = "A Citizen contributes one unit."
    ok = rc.SpanRecord(
        loc="1¶1", q0="A Citizen contributes", q1="one unit.", claim="X.",
        type="REQ", voice="world", status="canonical", owner="home.dwell",
    )
    bad = rc.SpanRecord(
        loc="1¶1", q0="not in the block", q1="one unit.", claim="X.",
        type="REQ", voice="world", status="canonical", owner="home.dwell",
    )
    recs, errs, nxt = rc.hydrate([ok, bad, ok], {"1¶1": block}, "SPEC_X", 1)
    assert len(recs) == 2 and len(errs) == 1
    assert nxt == 4, "three spans consumed IDs 1-3, so the next chunk starts at 4"


def test_ids_do_not_collide_across_chunks_with_failures():
    block = "A Citizen contributes one unit."
    ok = rc.SpanRecord(
        loc="1¶1", q0="A Citizen contributes", q1="one unit.", claim="X.",
        type="REQ", voice="world", status="canonical", owner="home.dwell",
    )
    bad = rc.SpanRecord(
        loc="1¶1", q0="absent marker", q1="one unit.", claim="X.",
        type="REQ", voice="world", status="canonical", owner="home.dwell",
    )
    a, _, nxt = rc.hydrate([ok, bad], {"1¶1": block}, "SPEC_X", 1)
    b, _, _ = rc.hydrate([ok], {"1¶1": block}, "SPEC_X", nxt)
    ids = [r.id for r in a + b]
    assert len(ids) == len(set(ids)), f"duplicate ids: {ids}"


# --------------------------------------------------------------------------
# Approximate q1 — the model reconstructs the closing marker
# --------------------------------------------------------------------------

DROPPED_WORD = (
    "Projects are measured in integer Citizen-Days. A Project costing 2 "
    "Citizen-Days may be completed by one available Citizen in two game days "
    "or by two Citizens in one day."
)


def test_dropped_word_in_q1_is_recovered_by_suffix():
    """Model wrote 'or two Citizens in one day.'; source says 'or by two ...'."""
    quote, inferred = rc.resolve_span_with_fallback(
        DROPPED_WORD, "Projects are measured in integer", "or two Citizens in one day."
    )
    assert inferred is True
    assert quote.endswith("in one day.")


def test_an_inferred_endpoint_is_flagged_not_hidden():
    s = rc.SpanRecord(
        loc="1¶1", q0="Projects are measured in integer",
        q1="or two Citizens in one day.", claim="X.", type="REQ",
        voice="world", status="canonical", owner="home.dwell.projects",
    )
    recs, errs, _ = rc.hydrate([s], {"1¶1": DROPPED_WORD}, "SPEC_X")
    assert not errs
    assert "span_end_inferred" in recs[0].flags


def test_exact_q1_is_not_flagged():
    quote, inferred = rc.resolve_span_with_fallback(
        DROPPED_WORD, "Projects are measured", "in one day."
    )
    assert inferred is False


def test_a_wrong_q0_is_never_rescued_by_a_shorter_tail():
    """If the location is wrong, no amount of tail-shortening helps — and
    pretending otherwise would attach a real quote to the wrong claim."""
    with pytest.raises(rc.SpanUnresolvable, match="q0 not found"):
        rc.resolve_span_with_fallback(DROPPED_WORD, "Supplies are prepared by", "one day.")


def test_a_tail_too_short_to_trust_is_refused():
    block = "One day the Citizen departs. Another day they return."
    with pytest.raises(rc.SpanUnresolvable):
        rc.resolve_span_with_fallback(block, "One day", "xx yy.")


def test_inflection_change_is_still_refused():
    """'inhabits it' for 'inhabit it' is a rewrite, not a dropped word."""
    block = "The player is asked to notice the Citizens who inhabit it."
    with pytest.raises(rc.SpanUnresolvable):
        rc.resolve_span_with_fallback(block, "The player is asked", "who inhabits it.")
