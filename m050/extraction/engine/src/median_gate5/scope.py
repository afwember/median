from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .errors import ContractError, IntegrityError


def _within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def validate_input_paths(
    repo_root: Path,
    paths: Iterable[Path],
    allowed_roots: Iterable[Path],
    forbidden_roots: Iterable[Path] | None = None,
) -> list[str]:
    base = repo_root.resolve()
    allowed = [(base / root).resolve() if not root.is_absolute() else root.resolve() for root in allowed_roots]
    forbidden = [
        (base / root).resolve() if not root.is_absolute() else root.resolve()
        for root in (forbidden_roots or [Path("m051")])
    ]
    errors: list[str] = []
    for supplied in paths:
        target = (base / supplied).resolve() if not supplied.is_absolute() else supplied.resolve()
        if not _within(target, base):
            errors.append(f"input escapes repository: {supplied}")
        elif any(_within(target, root) for root in forbidden):
            errors.append(f"forbidden input root: {supplied}")
        elif not any(_within(target, root) for root in allowed):
            errors.append(f"input outside allowlist: {supplied}")
        elif not target.is_file():
            errors.append(f"input is not a file: {supplied}")
    return errors


def require_input_paths(
    repo_root: Path,
    paths: Iterable[Path],
    allowed_roots: Iterable[Path],
    forbidden_roots: Iterable[Path] | None = None,
) -> None:
    errors = validate_input_paths(repo_root, paths, allowed_roots, forbidden_roots)
    if errors:
        raise IntegrityError("; ".join(errors))


def require_new_output_path(repo_root: Path, supplied: Path) -> Path:
    base = repo_root.resolve()
    extraction_root = (base / "m050/extraction").resolve()
    target = (base / supplied).resolve() if not supplied.is_absolute() else supplied.resolve()
    if not _within(target, extraction_root):
        raise IntegrityError(f"output escapes m050/extraction: {supplied}")
    if target.exists() or target.is_symlink():
        raise IntegrityError(f"output already exists: {supplied}")
    parent = target.parent
    while not parent.exists() and parent != extraction_root:
        parent = parent.parent
    if not _within(parent.resolve(), extraction_root):
        raise IntegrityError(f"output parent escapes m050/extraction: {supplied}")
    return target


def require_zero_cost_for_offline(maximum_spend_cents: int, provider: str) -> None:
    if provider == "offline" and maximum_spend_cents != 0:
        raise ContractError("offline work orders must have a zero cost cap")
