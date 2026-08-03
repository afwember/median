from __future__ import annotations

from pathlib import Path
from typing import Any

from .canonical import sha256_file
from .errors import ContractError
from .schema import validate_artifact
from .scope import require_input_paths, require_new_output_path, require_zero_cost_for_offline


FROZEN_SOURCE_ROOTS = [
    Path("m050/docs/baseline"),
    Path("m050/docs/v0.5"),
]


def verify_work_order(repo_root: Path, work_order: dict[str, Any]) -> dict[str, Any]:
    validate_artifact("work_order", work_order)
    source_path = Path(work_order["source_path"])
    require_input_paths(repo_root, [source_path], FROZEN_SOURCE_ROOTS)
    resolved = (repo_root / source_path).resolve()
    actual_hash = sha256_file(resolved)
    if actual_hash != work_order["source_sha256"]:
        raise ContractError(
            f"source hash mismatch: expected {work_order['source_sha256']}, found {actual_hash}"
        )
    require_zero_cost_for_offline(work_order["maximum_spend_cents"], work_order["provider"])
    if work_order["provider"] == "offline":
        if work_order["model"] != "none":
            raise ContractError("offline work order model must be 'none'")
        if work_order["maximum_requests"] != 0:
            raise ContractError("offline work order cannot authorize requests")
        if work_order.get("authorization_receipt_id") is not None:
            raise ContractError("offline work order cannot carry provider authorization")
    elif work_order["state"] in {"authorized", "active", "closed"}:
        if not work_order.get("authorization_receipt_id"):
            raise ContractError("provider work order lacks author authorization receipt")
    for output in work_order["expected_output_paths"]:
        require_new_output_path(repo_root, Path(output))
    return {
        "passed": True,
        "source_path": str(source_path),
        "source_sha256": actual_hash,
        "provider": work_order["provider"],
        "maximum_spend_cents": work_order["maximum_spend_cents"],
    }
