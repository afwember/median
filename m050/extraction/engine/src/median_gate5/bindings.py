from __future__ import annotations

import json
from pathlib import Path

from .canonical import sha256_file


RELOCATION_MANIFEST = Path(
    "m050/extraction/evidence/legacy/"
    "M050_Legacy_Evidence_Relocation_Manifest_v0_1_MEDIANv0_5_0.json"
)


def _contained_file(repo_root: Path, relative: str) -> Path | None:
    if not relative or Path(relative).is_absolute():
        return None
    base = repo_root.resolve()
    target = (base / relative).resolve()
    try:
        target.relative_to(base)
    except ValueError:
        return None
    if relative == "m051" or relative.startswith("m051/"):
        return None
    return target if target.is_file() else None


def repository_file(repo_root: Path, relative: str) -> Path | None:
    """Resolve a live path or an explicitly relocated legacy archive binding."""
    direct = _contained_file(repo_root, relative)
    if direct is not None:
        return direct
    if not relative.startswith("m050/archive/"):
        return None

    manifest_path = _contained_file(repo_root, RELOCATION_MANIFEST.as_posix())
    if manifest_path is None:
        return None
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if manifest.get("status") != "ACTIVE_ARCHIVE_RETIRED":
        return None

    matches = [
        item
        for item in manifest.get("relocations", [])
        if item.get("original_path") == relative
    ]
    if len(matches) != 1:
        return None
    relocation = matches[0]
    relocated = _contained_file(repo_root, relocation.get("relocated_path", ""))
    if relocated is None:
        return None
    if sha256_file(relocated) != relocation.get("sha256"):
        return None
    return relocated
