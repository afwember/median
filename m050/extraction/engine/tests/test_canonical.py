import json

import pytest

from median_gate5.canonical import (
    canonical_json_bytes,
    content_id,
    require_manifest,
    sha256_bytes,
    write_new_json,
)
from median_gate5.errors import IntegrityError


def test_canonical_json_and_id_are_order_independent():
    left = {"b": 2, "a": "é"}
    right = {"a": "é", "b": 2}
    assert canonical_json_bytes(left) == canonical_json_bytes(right)
    assert content_id("item", left) == content_id("item", right)


def test_append_writer_refuses_overwrite(tmp_path):
    target = tmp_path / "record.json"
    write_new_json(target, {"version": 1})
    with pytest.raises(FileExistsError):
        write_new_json(target, {"version": 2})
    assert json.loads(target.read_text()) == {"version": 1}


def test_manifest_fails_closed(tmp_path):
    target = tmp_path / "evidence.txt"
    target.write_text("preserved", encoding="utf-8")
    entries = [{"path": "evidence.txt", "sha256": sha256_bytes(b"preserved")}]
    require_manifest(tmp_path, entries)
    target.write_text("changed", encoding="utf-8")
    with pytest.raises(IntegrityError):
        require_manifest(tmp_path, entries)
