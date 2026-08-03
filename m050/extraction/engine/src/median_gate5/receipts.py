from __future__ import annotations

from pathlib import Path
from typing import Any

from .canonical import canonical_json_bytes, sha256_bytes, write_new_json
from .errors import IntegrityError


def artifact_hash(artifact: dict[str, Any]) -> str:
    return sha256_bytes(canonical_json_bytes(artifact))


def verify_receipt_chain(receipts: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    previous_hash: str | None = None
    seen_ids: set[str] = set()
    for index, receipt in enumerate(receipts):
        receipt_id = receipt.get("receipt_id")
        if not receipt_id:
            errors.append(f"receipt {index} has no receipt_id")
        elif receipt_id in seen_ids:
            errors.append(f"duplicate receipt_id: {receipt_id}")
        else:
            seen_ids.add(receipt_id)
        if receipt.get("predecessor_receipt_hash") != previous_hash:
            errors.append(
                f"receipt {receipt_id or index} predecessor mismatch: "
                f"expected {previous_hash}, found {receipt.get('predecessor_receipt_hash')}"
            )
        previous_hash = artifact_hash(receipt)
    return errors


def require_receipt_chain(receipts: list[dict[str, Any]]) -> None:
    errors = verify_receipt_chain(receipts)
    if errors:
        raise IntegrityError("; ".join(errors))


def append_receipt(directory: Path, sequence: int, receipt: dict[str, Any]) -> Path:
    if sequence < 1:
        raise ValueError("receipt sequence must be positive")
    receipt_id = receipt.get("receipt_id")
    if not receipt_id:
        raise IntegrityError("receipt_id is required")
    target = directory / f"{sequence:06d}_{receipt_id}.json"
    write_new_json(target, receipt)
    return target
