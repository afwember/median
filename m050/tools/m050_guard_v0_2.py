#!/usr/bin/env python3
"""Verify Gate 4 integrity plus the active MEDIAN Gate 5 offline foundation."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import pathlib
import re
import subprocess
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
LEGACY_GUARD = REPO_ROOT / "m050/tools/m050_guard.py"
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_3_MEDIANv0_5_0.json"
IDENTITY_APPROVAL_RECEIPT = REPO_ROOT / "m050/extraction/audit/M050_Extraction_Gate_5_Legacy_Source_Identity_Approval_Receipt_v0_1_MEDIANv0_5_0.json"
ENGINE_ROOT = REPO_ROOT / "m050/extraction/engine"
LOCK_PATH = ENGINE_ROOT / "requirements.lock"
SCHEMA_PATH = ENGINE_ROOT / "src/median_gate5/schemas/gate5-artifacts.schema.json"
REGRESSION_PATH = ENGINE_ROOT / "fixtures/regression/manifest.json"
IGNORED_PARTS = {"__pycache__", ".pytest_cache"}
PROVIDER_MODULES = {"openai", "anthropic"}
LOCK_REQUIREMENT = re.compile(r"^[A-Za-z0-9_.-]+==[^\s\\]+\s*\\$")
LOCK_HASH = re.compile(r"^--hash=sha256:[0-9a-f]{64}$")


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def content_id(prefix: str, value: object) -> str:
    canonical = json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return f"{prefix}_{hashlib.sha256(canonical).hexdigest()[:24]}"


def engine_snapshot() -> tuple[int, str]:
    digest = hashlib.sha256()
    files = sorted(
        path
        for path in ENGINE_ROOT.rglob("*")
        if path.is_file()
        and not any(part in IGNORED_PARTS or part.endswith(".egg-info") for part in path.parts)
        and path.suffix != ".pyc"
    )
    for path in files:
        relative = path.relative_to(REPO_ROOT).as_posix()
        digest.update(relative.encode("utf-8") + b"\0" + sha256_file(path).encode("ascii") + b"\n")
    return len(files), digest.hexdigest()


def validate_active_index(errors: list[str]) -> None:
    try:
        index = json.loads(ACTIVE_INDEX.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"active control index cannot be read: {exc}")
        return
    if index.get("execution_state") != "GATE_5_LEGACY_IDENTITIES_APPROVED_REPLAY_AUTHORIZED":
        errors.append("active control index has unexpected execution state")
    if index.get("provider_call_authorized") is not False:
        errors.append("active control index does not explicitly prohibit provider calls")
    for control in index.get("current_controls", []):
        relative = control.get("path")
        if not isinstance(relative, str) or not relative:
            errors.append("active control entry lacks a path")
            continue
        target = REPO_ROOT / relative
        if relative.endswith("/"):
            if not target.is_dir():
                errors.append(f"missing active control directory: {relative}")
        elif not target.is_file():
            errors.append(f"missing active control file: {relative}")


def validate_identity_approval(errors: list[str]) -> int:
    try:
        aggregate = json.loads(IDENTITY_APPROVAL_RECEIPT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"identity approval receipt cannot be read: {exc}")
        return 0
    if aggregate.get("status") != "FOUR_LEGACY_SOURCE_IDENTITIES_APPROVED":
        errors.append("identity approval receipt has unexpected status")
    if aggregate.get("author_decision") != "approve all four":
        errors.append("identity approval receipt does not preserve the exact author decision")
    if aggregate.get("authority") != "Asa Wember":
        errors.append("identity approval receipt lacks author authority")
    if aggregate.get("provider_call_authorized") is not False:
        errors.append("identity approval receipt does not prohibit provider calls")
    cards = aggregate.get("approved_cards", [])
    if not isinstance(cards, list) or len(cards) != 4:
        errors.append("identity approval receipt must bind exactly four approved cards")
        return 0
    seen_sources: set[str] = set()
    for entry in cards:
        source_id = entry.get("source_id")
        if not isinstance(source_id, str) or source_id in seen_sources:
            errors.append(f"invalid or duplicate approved source ID: {source_id}")
            continue
        seen_sources.add(source_id)
        card_path = REPO_ROOT / entry.get("path", "")
        try:
            card = json.loads(card_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"approved identity card cannot be read for {source_id}: {exc}")
            continue
        if sha256_file(card_path) != entry.get("sha256"):
            errors.append(f"approved identity card hash mismatch: {source_id}")
        if (
            card.get("source_id") != source_id
            or card.get("card_id") != entry.get("card_id")
            or card.get("status") != "approved"
            or card.get("version") != 3
        ):
            errors.append(f"approved identity card metadata mismatch: {source_id}")
        card_body = {key: value for key, value in card.items() if key != "card_id"}
        if card.get("card_id") != content_id("sic", card_body):
            errors.append(f"approved identity card content ID mismatch: {source_id}")
        receipt_values: dict[str, dict] = {}
        for key, prior_state, new_state in (
            ("review_receipt", "draft", "reviewed"),
            ("approval_receipt", "reviewed", "approved"),
        ):
            binding = entry.get(key, {})
            receipt_path = REPO_ROOT / binding.get("path", "")
            try:
                receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"{key} cannot be read for {source_id}: {exc}")
                continue
            receipt_values[key] = receipt
            if sha256_file(receipt_path) != binding.get("sha256"):
                errors.append(f"{key} hash mismatch: {source_id}")
            receipt_body = {name: value for name, value in receipt.items() if name != "receipt_id"}
            if receipt.get("receipt_id") != binding.get("receipt_id") or receipt.get(
                "receipt_id"
            ) != content_id("tr", receipt_body):
                errors.append(f"{key} content ID mismatch: {source_id}")
            if (
                receipt.get("machine") != "identity_card"
                or receipt.get("prior_state") != prior_state
                or receipt.get("new_state") != new_state
                or receipt.get("authority") != "Asa Wember"
            ):
                errors.append(f"{key} transition metadata mismatch: {source_id}")
        reviewed = entry.get("review_receipt", {})
        reviewed_receipt = receipt_values.get("review_receipt", {})
        approval = receipt_values.get("approval_receipt", {})
        if card.get("supersedes_card_id") != reviewed_receipt.get("artifact_id"):
            errors.append(f"approved card does not supersede the reviewed receipt target: {source_id}")
        if approval.get("artifact_id") != card.get("card_id"):
            errors.append(f"approval receipt targets the wrong card: {source_id}")
        if approval.get("predecessor_receipt_hash") != reviewed.get("sha256"):
            errors.append(f"approval receipt predecessor hash mismatch: {source_id}")
    return len(seen_sources)


def validate_lock(errors: list[str]) -> None:
    if not LOCK_PATH.is_file():
        errors.append("Gate 5 requirements lock is missing")
        return
    significant = [
        line.strip()
        for line in LOCK_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if len(significant) % 2:
        errors.append("requirements lock has an incomplete requirement/hash pair")
        return
    for index in range(0, len(significant), 2):
        requirement = significant[index]
        hash_line = significant[index + 1]
        if not LOCK_REQUIREMENT.match(requirement):
            errors.append(f"unlocked or malformed requirement: {requirement}")
        if not LOCK_HASH.match(hash_line):
            errors.append(f"missing or malformed requirement hash: {hash_line}")
        name = requirement.split("==", 1)[0].lower().replace("_", "-")
        if name in PROVIDER_MODULES:
            errors.append(f"provider SDK is prohibited in offline-core lock: {name}")


def validate_json_controls(errors: list[str]) -> int:
    count = 0
    for path in (SCHEMA_PATH, REGRESSION_PATH):
        try:
            json.loads(path.read_text(encoding="utf-8"))
            count += 1
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid Gate 5 JSON control {path.relative_to(REPO_ROOT)}: {exc}")
    return count


def validate_offline_imports(errors: list[str]) -> None:
    package_root = ENGINE_ROOT / "src/median_gate5"
    for path in sorted(package_root.glob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as exc:
            errors.append(f"cannot parse offline core module {path.name}: {exc}")
            continue
        for node in ast.walk(tree):
            imported: str | None = None
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".", 1)[0] in PROVIDER_MODULES:
                        imported = alias.name
                        break
            elif isinstance(node, ast.ImportFrom) and node.module:
                if node.module.split(".", 1)[0] in PROVIDER_MODULES:
                    imported = node.module
            if imported:
                errors.append(f"offline core imports provider module {imported}: {path.name}")


def run_legacy_guard(skip_archive: bool, work_order: pathlib.Path | None) -> int:
    command = [sys.executable, str(LEGACY_GUARD)]
    if skip_archive:
        command.append("--skip-archive")
    if work_order:
        command.extend(["--work-order", str(work_order)])
    result = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=False)
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)
    return result.returncode


def run_tests() -> int:
    python = REPO_ROOT / ".venv/bin/python"
    if not python.is_file():
        print("Gate 5 test environment is missing: .venv/bin/python", file=sys.stderr)
        return 1
    result = subprocess.run(
        [str(python), "-m", "pytest", "m050/extraction/engine/tests", "-q"],
        cwd=REPO_ROOT,
        check=False,
    )
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=pathlib.Path)
    parser.add_argument("--skip-archive", action="store_true")
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()

    if run_legacy_guard(args.skip_archive, args.work_order):
        print("M050 GATE 5 GUARD: FAIL — Gate 4 guard failed")
        return 1

    errors: list[str] = []
    validate_active_index(errors)
    approved_identity_cards = validate_identity_approval(errors)
    validate_lock(errors)
    json_controls = validate_json_controls(errors)
    validate_offline_imports(errors)
    file_count, digest = engine_snapshot()

    if args.with_tests and run_tests():
        errors.append("Gate 5 offline regression suite failed")

    if errors:
        print("M050 GATE 5 GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("M050 GATE 5 GUARD: PASS")
    print(f"- engine files: {file_count}")
    print(f"- engine digest: {digest}")
    print(f"- parsed JSON controls: {json_controls}")
    print(f"- approved identity cards: {approved_identity_cards}")
    print("- offline provider imports: 0")
    print("- provider calls: prohibited")
    if args.with_tests:
        print("- offline regression suite: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
