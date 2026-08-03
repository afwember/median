from __future__ import annotations

import importlib.metadata
import os
from pathlib import Path
import platform
import re
import stat
import sys
from typing import Any


REQUIRED_DISTRIBUTIONS = {
    "jsonschema": "4.23.0",
    "PyYAML": "6.0.1",
}

LOCK_LINE = re.compile(r"^([A-Za-z0-9_.-]+)==([^\s\\]+)")


def locked_requirements(path: Path) -> dict[str, str]:
    requirements: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = LOCK_LINE.match(line.strip())
        if match:
            requirements[match.group(1)] = match.group(2)
    return requirements


def runtime_report(
    credential_paths: list[Path] | None = None, lock_path: Path | None = None
) -> dict[str, Any]:
    packages: dict[str, str | None] = {}
    for name in REQUIRED_DISTRIBUTIONS:
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None

    credentials = []
    for path in credential_paths or []:
        exists = path.is_file()
        mode = stat.S_IMODE(path.stat().st_mode) if exists else None
        credentials.append(
            {
                "path": str(path),
                "exists": exists,
                "private_permissions": mode is not None and mode & 0o077 == 0,
                "mode": f"{mode:04o}" if mode is not None else None,
            }
        )

    lock_versions = locked_requirements(lock_path) if lock_path else {}
    lock_agreement: dict[str, dict[str, str | bool | None]] = {}
    for name, expected in lock_versions.items():
        try:
            actual = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            actual = None
        lock_agreement[name] = {
            "expected": expected,
            "actual": actual,
            "matches": actual == expected,
        }

    return {
        "schema_version": "M050-RUNTIME-PREFLIGHT-0.1",
        "python": {
            "implementation": platform.python_implementation(),
            "version": platform.python_version(),
            "executable": sys.executable,
            "virtual_environment": sys.prefix != sys.base_prefix,
        },
        "platform": {
            "system": platform.system(),
            "machine": platform.machine(),
            "release": platform.release(),
        },
        "dependencies": packages,
        "lock_path": str(lock_path) if lock_path else None,
        "lock_agreement": lock_agreement,
        "provider_modules_loaded": any(
            name == "openai" or name.startswith("openai.") or name == "anthropic" or name.startswith("anthropic.")
            for name in sys.modules
        ),
        "network_proxy_environment_present": any(
            key.lower() in {"http_proxy", "https_proxy", "all_proxy"} for key in os.environ
        ),
        "credentials": credentials,
    }


def runtime_errors(report: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    python = report["python"]
    major, minor, *_ = (int(part) for part in python["version"].split("."))
    if python["implementation"] != "CPython" or (major, minor) != (3, 12):
        errors.append("Gate 5 requires CPython 3.12")
    if report["platform"]["machine"] != "arm64":
        errors.append("initial Gate 5 host contract requires arm64")
    if not python["virtual_environment"]:
        errors.append("Gate 5 must run inside a virtual environment")
    for name, expected in REQUIRED_DISTRIBUTIONS.items():
        actual = report["dependencies"].get(name)
        if actual != expected:
            errors.append(f"dependency mismatch: {name} expected {expected}, found {actual}")
    for name, agreement in report.get("lock_agreement", {}).items():
        if not agreement["matches"]:
            errors.append(
                f"lock mismatch: {name} expected {agreement['expected']}, "
                f"found {agreement['actual']}"
            )
    if report["provider_modules_loaded"]:
        errors.append("offline core loaded a provider module")
    for credential in report["credentials"]:
        if credential["exists"] and not credential["private_permissions"]:
            errors.append(f"credential permissions are not private: {credential['path']}")
    return errors
