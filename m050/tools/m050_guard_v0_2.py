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
ACTIVE_INDEX = REPO_ROOT / "m050/extraction/control/M050_Active_Control_Index_v0_2_MEDIANv0_5_0.json"
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
    if index.get("execution_state") != "GATE_5_OFFLINE_IMPLEMENTATION_AUTHORIZED":
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
    print("- offline provider imports: 0")
    print("- provider calls: prohibited")
    if args.with_tests:
        print("- offline regression suite: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
