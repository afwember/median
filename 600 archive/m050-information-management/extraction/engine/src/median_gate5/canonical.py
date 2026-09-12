from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any

from .errors import IntegrityError


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize JSON deterministically for hashes and content-derived IDs."""
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def content_id(prefix: str, value: Any, length: int = 24) -> str:
    if not prefix or not prefix.replace("_", "").isalnum():
        raise ValueError("prefix must contain only letters, digits, and underscores")
    return f"{prefix}_{sha256_bytes(canonical_json_bytes(value))[:length]}"


def write_new_bytes(path: Path, data: bytes, mode: int = 0o644) -> None:
    """Create a new file atomically enough for the sole-writer repository model.

    Existing targets are never overwritten. Data is flushed before the handle is
    closed so a receipt cannot be reported as written while still only buffered.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    fd = os.open(path, flags, mode)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        try:
            path.unlink(missing_ok=True)
        finally:
            raise


def write_new_json(path: Path, value: Any) -> str:
    data = canonical_json_bytes(value) + b"\n"
    write_new_bytes(path, data)
    return sha256_bytes(data)


def verify_manifest(base: Path, entries: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for entry in entries:
        relative = entry.get("path", "")
        expected = entry.get("sha256", "")
        if relative in seen:
            errors.append(f"duplicate manifest path: {relative}")
            continue
        seen.add(relative)
        target = (base / relative).resolve()
        try:
            target.relative_to(base.resolve())
        except ValueError:
            errors.append(f"manifest path escapes base: {relative}")
            continue
        if not target.is_file():
            errors.append(f"missing manifest file: {relative}")
        elif sha256_file(target) != expected:
            errors.append(f"manifest hash mismatch: {relative}")
    return errors


def require_manifest(base: Path, entries: list[dict[str, str]]) -> None:
    errors = verify_manifest(base, entries)
    if errors:
        raise IntegrityError("; ".join(errors))
