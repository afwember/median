from median_gate5.canonical import sha256_bytes
from median_gate5.legacy import canonical_jsonl_bytes, replay_record


def _block(block_id: str, text: str, start: int) -> dict:
    return {
        "block_id": block_id,
        "block_type": "list_item" if text.startswith("-") else "paragraph",
        "start": start,
        "end": start + len(text),
        "text": text,
    }


def _record(atom_id: str, location: str, quotation: str) -> dict:
    return {
        "atom_id": atom_id,
        "source_id": "SRC-1",
        "source_location": location,
        "exact_source_text": quotation,
    }


def test_replay_disambiguates_repeated_quote_with_line_location():
    source = "Alpha.\n\nRepeat here.\n\nRepeat here.\n"
    blocks = [
        _block("B1", "Alpha.", source.index("Alpha.")),
        _block("B2", "Repeat here.", source.index("Repeat here.")),
        _block("B3", "Repeat here.", source.rindex("Repeat here.")),
    ]
    result = replay_record(
        source_id="SRC-1",
        active_source_text=source,
        active_source_sha256="a" * 64,
        blocks=blocks,
        legacy_record=_record("A1", "L00005-L00005", "Repeat here."),
    )
    assert result["grounding_status"] == "exact_single_block_location_disambiguated"
    assert result["block_ids"] == ["B3"]
    assert result["line_location_applied"] is True
    assert result["migration_disposition"] == "eligible"


def test_replay_exposes_cross_block_compound_without_splitting_it():
    source = "- one\n- two\n"
    blocks = [
        _block("B1", "- one", source.index("- one")),
        _block("B2", "- two", source.index("- two")),
    ]
    result = replay_record(
        source_id="SRC-1",
        active_source_text=source,
        active_source_sha256="a" * 64,
        blocks=blocks,
        legacy_record=_record("A2", "L00001-L00002", "one\n- two"),
    )
    assert result["grounding_status"] == "exact_cross_block"
    assert result["block_ids"] == ["B1", "B2"]
    assert result["migration_disposition"] == "boundary_review_required"


def test_replay_preserves_legacy_only_grounding_for_reference_rewrite():
    result = replay_record(
        source_id="SRC-1",
        active_source_text="New reference.\n",
        active_source_sha256="a" * 64,
        blocks=[_block("B1", "New reference.", 0)],
        legacy_record=_record("A3", "L00001-L00001", "Old reference."),
        legacy_source_text="Old reference.\n",
        legacy_source_sha256="b" * 64,
    )
    assert result["grounding_status"] == "exact_legacy_source_only"
    assert result["grounding_source_role"] == "legacy_extraction_source"
    assert result["grounding_source_sha256"] == "b" * 64
    assert result["migration_disposition"] == "active_to_legacy_reference_rewrite_required"


def test_replay_fails_closed_when_quote_is_not_grounded():
    result = replay_record(
        source_id="SRC-1",
        active_source_text="Present text.\n",
        active_source_sha256="a" * 64,
        blocks=[_block("B1", "Present text.", 0)],
        legacy_record=_record("A4", "L00001-L00001", "Missing text."),
    )
    assert result["grounding_status"] == "not_grounded"
    assert result["migration_disposition"] == "grounding_failure"


def test_replay_ledger_bytes_are_canonical_and_deterministic():
    records = [{"b": 2, "a": 1}, {"value": "é"}]
    first = canonical_jsonl_bytes(records)
    second = canonical_jsonl_bytes(records)
    assert first == second
    assert first == b'{"a":1,"b":2}\n{"value":"\xc3\xa9"}\n'
    assert sha256_bytes(first) == sha256_bytes(second)
