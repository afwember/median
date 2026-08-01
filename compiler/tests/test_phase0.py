"""Phase 0 and Phase 1 acceptance tests.

Each test here corresponds to a failure that actually occurred during
development, or to a guarantee the compiler spec requires before the
normalization pipeline may be frozen and tagged.
"""

from __future__ import annotations

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
        weight="STATE", status="canonical", owner="home.invented.thing",
    )
    errs = rc.validate_records([r], {"1¶1": "alpha beta"}, {"home.dwell"}, "SPEC_HOME")
    assert any("not a registered namespace" in e for e in errs)


def test_owner_unclear_flag_excuses_an_unknown_namespace():
    r = rc.AtomicRecord(
        id="SPEC_HOME:0001", src="SPEC_HOME", loc="1¶1",
        quote="alpha beta", claim="Alpha beta.", type="REQ",
        weight="STATE", status="canonical", owner="home",
        flags=["owner_unclear"],
    )
    errs = rc.validate_records([r], {"1¶1": "alpha beta"}, {"home.dwell"}, "SPEC_HOME")
    assert not any("namespace" in e for e in errs)


def test_quote_must_be_grounded_in_the_block():
    """A claim without a locatable quotation is an assertion, not a fact."""
    r = rc.AtomicRecord(
        id="SPEC_HOME:0001", src="SPEC_HOME", loc="1¶1",
        quote="a sentence that is not in the source", claim="X.", type="REQ",
        weight="STATE", status="canonical", owner="home.dwell",
    )
    errs = rc.validate_records([r], {"1¶1": "alpha beta"}, {"home.dwell"}, "SPEC_HOME")
    assert any("not present verbatim" in e for e in errs)


def test_grounding_ignores_whitespace_only():
    r = rc.AtomicRecord(
        id="SPEC_HOME:0001", src="SPEC_HOME", loc="1¶1",
        quote="Each  Citizen\ncontributes one unit.", claim="X.", type="REQ",
        weight="STATE", status="canonical", owner="home.dwell",
    )
    block = "Each Citizen contributes one unit."
    errs = rc.validate_records([r], {"1¶1": block}, {"home.dwell"}, "SPEC_HOME")
    assert not errs
