import json
from pathlib import Path

import pytest

from median_gate5.canonical import sha256_bytes
from median_gate5.capture import capture_raw_bytes, parse_json_response
from median_gate5.errors import ContractError, IntegrityError
from median_gate5.workorders import verify_work_order


def offline_work_order(source_hash):
    return {
        "schema_version": "M050-WORK-ORDER-0.1",
        "work_order_id": "wo-offline-1",
        "version": 1,
        "state": "offline_verified",
        "source_id": "SRC",
        "source_path": "m050/docs/v0.5/source.md",
        "source_sha256": source_hash,
        "identity_card_id": "card-1",
        "block_manifest_id": "blocks-1",
        "chunk_plan_id": "chunks-1",
        "allowed_block_ids": ["SRC__B00001_abc"],
        "allowed_streams": ["evidence_game_semantic"],
        "prompt_version": "prompt-0.1",
        "schema_id": "proposal-0.1",
        "engine_version": "0.1.0",
        "provider": "offline",
        "model": "none",
        "request_token_limit": 1000,
        "output_token_limit": 1000,
        "claim_block_limit": 10,
        "maximum_spend_cents": 0,
        "maximum_requests": 0,
        "retry_allowance": 0,
        "stop_conditions": ["integrity_failure"],
        "expected_output_paths": ["m050/extraction/runs/wo-offline-1/report.json"],
        "authorization_receipt_id": None,
    }


def test_offline_work_order_verifies_exact_source_and_scope(tmp_path):
    source_dir = tmp_path / "m050" / "docs" / "v0.5"
    source_dir.mkdir(parents=True)
    source = source_dir / "source.md"
    source.write_text("frozen", encoding="utf-8")
    work_order = offline_work_order(sha256_bytes(b"frozen"))
    assert verify_work_order(tmp_path, work_order)["passed"]
    source.write_text("changed", encoding="utf-8")
    with pytest.raises(ContractError, match="hash mismatch"):
        verify_work_order(tmp_path, work_order)


def test_work_order_rejects_future_source_and_output_escape(tmp_path):
    future_dir = tmp_path / "m051"
    future_dir.mkdir()
    future = future_dir / "future.md"
    future.write_text("future", encoding="utf-8")
    work_order = offline_work_order(sha256_bytes(b"future"))
    work_order["source_path"] = "m051/future.md"
    with pytest.raises(IntegrityError, match="forbidden"):
        verify_work_order(tmp_path, work_order)

    source_dir = tmp_path / "m050" / "docs" / "v0.5"
    source_dir.mkdir(parents=True)
    source = source_dir / "source.md"
    source.write_text("future", encoding="utf-8")
    work_order["source_path"] = "m050/docs/v0.5/source.md"
    work_order["expected_output_paths"] = ["outside/report.json"]
    with pytest.raises(IntegrityError, match="escapes"):
        verify_work_order(tmp_path, work_order)


def test_provider_work_order_requires_authorization_receipt(tmp_path):
    source_dir = tmp_path / "m050" / "docs" / "v0.5"
    source_dir.mkdir(parents=True)
    source = source_dir / "source.md"
    source.write_text("frozen", encoding="utf-8")
    work_order = offline_work_order(sha256_bytes(b"frozen"))
    work_order.update(
        provider="example-provider",
        model="example-model",
        state="authorized",
        maximum_spend_cents=100,
        maximum_requests=1,
    )
    with pytest.raises(ContractError, match="authorization receipt"):
        verify_work_order(tmp_path, work_order)


def test_capture_is_append_only_and_parser_fails_closed(tmp_path):
    raw = json.dumps({"dispositions": []}).encode()
    target = tmp_path / "raw-response.json"
    assert capture_raw_bytes(target, raw) == sha256_bytes(raw)
    assert parse_json_response(raw) == {"dispositions": []}
    with pytest.raises(FileExistsError):
        capture_raw_bytes(target, raw)
    with pytest.raises(ContractError, match="possibly truncated"):
        parse_json_response(b'{"dispositions": [')
    with pytest.raises(ContractError, match="root must be an object"):
        parse_json_response(b"[]")
