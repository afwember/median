import json
from pathlib import Path


ENGINE_ROOT = Path(__file__).resolve().parents[1]


def test_regression_manifest_is_unique_and_resolves_to_tests():
    manifest_path = ENGINE_ROOT / "fixtures" / "regression" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cases = manifest["cases"]
    ids = [case["case_id"] for case in cases]
    assert len(ids) == len(set(ids))
    assert len(cases) >= 30
    for case in cases:
        test_path = ENGINE_ROOT / case["test_path"]
        assert test_path.is_file(), case["case_id"]
        source = test_path.read_text(encoding="utf-8")
        assert f"def {case['test_name']}(" in source, case["case_id"]
        assert case["expected"] in {"pass", "pass_with_receipt", "fail_closed", "review_required"}
