import sys

import pytest
from jsonschema import Draft202012Validator

from median_gate5.errors import ContractError
from median_gate5.runtime import locked_requirements, runtime_errors, runtime_report
from median_gate5.schema import artifact_schema, validate_artifact


def test_complete_schema_is_valid():
    Draft202012Validator.check_schema(artifact_schema())


def test_schema_rejects_uncontrolled_extra_fields():
    artifact = {
        "schema_version": "M050-BLOCK-MANIFEST-0.1",
        "manifest_id": "bm_test",
        "source_id": "M050-SRC-TEST-001",
        "source_sha256": "0" * 64,
        "normalization_version": "M050-NORMALIZATION-0.1",
        "blocks": [],
        "surprise": True,
    }
    with pytest.raises(ContractError, match="Additional properties"):
        validate_artifact("block_manifest", artifact)


def test_runtime_is_isolated_and_credentials_are_not_opened(tmp_path):
    credential = tmp_path / "key"
    credential.write_text("must-not-be-read", encoding="utf-8")
    credential.chmod(0o600)
    before = credential.stat().st_atime_ns
    report = runtime_report([credential])
    after = credential.stat().st_atime_ns
    assert runtime_errors(report) == []
    assert not report["provider_modules_loaded"]
    assert "openai" not in sys.modules
    assert "anthropic" not in sys.modules
    assert before == after


def test_lock_parser_and_agreement(tmp_path):
    lock = tmp_path / "requirements.lock"
    lock.write_text(
        "jsonschema==4.23.0 \\\n+    --hash=sha256:" + "a" * 64 + "\nPyYAML==6.0.1 \\\n+    --hash=sha256:" + "b" * 64 + "\n",
        encoding="utf-8",
    )
    assert locked_requirements(lock) == {
        "jsonschema": "4.23.0",
        "PyYAML": "6.0.1",
    }
    assert runtime_errors(runtime_report(lock_path=lock)) == []
