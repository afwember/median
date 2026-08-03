#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import Any

from median_gate5.calibration import require_source_readiness


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_new_json(path: Path, value: Any, *, jsonl: bool = False) -> None:
    if path.exists():
        raise SystemExit(f"refusing to overwrite: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    if jsonl:
        payload = "".join(
            json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n"
            for item in value
        )
    else:
        payload = json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"
    path.write_text(payload, encoding="utf-8")


def require_binding(repo_root: Path, binding: dict[str, str]) -> Path:
    path = (repo_root / binding["path"]).resolve()
    if not path.is_file() or sha256_file(path) != binding["sha256"]:
        raise SystemExit(f"binding mismatch: {binding['path']}")
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--policy", required=True)
    parser.add_argument("--output-ledger", required=True)
    parser.add_argument("--output-profile", required=True)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    policy_path = (repo_root / args.policy).resolve()
    policy = read_json(policy_path)
    source_path = (repo_root / policy["source_path"]).resolve()
    if sha256_file(source_path) != policy["source_sha256"]:
        raise SystemExit("source hash mismatch")
    for key in ("identity_card", "identity_approval_receipt", "block_manifest", "chunk_plan"):
        require_binding(repo_root, policy[key])

    manifest = read_json(repo_root / policy["block_manifest"]["path"])
    if (manifest["source_id"], manifest["source_sha256"]) != (
        policy["source_id"], policy["source_sha256"]
    ):
        raise SystemExit("manifest source binding mismatch")
    if "".join(block["text"] for block in manifest["blocks"]) != source_path.read_text(encoding="utf-8"):
        raise SystemExit("manifest does not preserve complete source")

    change_start = next(
        block["ordinal"]
        for block in manifest["blocks"]
        if block["text"].strip() == policy["excluded_region_heading"]
    )
    eligible_code = set(policy["eligible_code_fence_ordinals"])
    ledger: list[dict[str, Any]] = []
    for block in manifest["blocks"]:
        ordinal = block["ordinal"]
        stripped = block["text"].strip()
        if ordinal >= change_start:
            disposition, reason = "excluded", "change_record"
        elif ordinal <= policy["document_furniture_through_ordinal"]:
            disposition, reason = "excluded", "document_furniture"
        elif stripped in policy["exact_document_furniture"]:
            disposition, reason = "excluded", "document_furniture"
        elif block["block_type"] == "whitespace":
            disposition, reason = "excluded", "whitespace_separator"
        elif block["block_type"] == "heading":
            disposition, reason = "context_only", "structural_heading"
        elif block["block_type"] == "code_fence":
            if ordinal in eligible_code:
                disposition, reason = "eligible", "semantic_code_or_reference_inventory"
            else:
                disposition, reason = policy["other_code_fence_disposition"], "supporting_example_or_template"
        else:
            disposition, reason = "eligible", "claim_bearing_source_content"
        ledger.append(
            {
                "block_id": block["block_id"],
                "block_sha256": block["raw_sha256"],
                "block_type": block["block_type"],
                "disposition": disposition,
                "reason_code": reason,
                "status_markers": block["status_markers"],
            }
        )

    if len(ledger) != len(manifest["blocks"]) or len({item["block_id"] for item in ledger}) != len(ledger):
        raise SystemExit("structural ledger coverage failure")
    counts = Counter(item["disposition"] for item in ledger)
    profile = {
        "schema_version": "M050-SOURCE-OFFLINE-READINESS-PROFILE-0.1",
        "state": "offline_dry_run",
        "source_id": policy["source_id"],
        "source_path": policy["source_path"],
        "source_sha256": policy["source_sha256"],
        "source_selection_authority": "Asa Wember",
        "identity_card": policy["identity_card"],
        "identity_approval_receipt": policy["identity_approval_receipt"],
        "gate_2_disposition": policy["gate_2_disposition"],
        "output_streams": policy["allowed_streams"],
        "stream_routing_complete": True,
        "model_extraction_prohibited": False,
        "execution_mode": "provider_calibrated",
        "provider_call_limit": 0,
        "prompt_extractable_source_ids": policy["prompt_extractable_source_ids"],
        "foreign_evidence_record_count": policy["foreign_evidence_record_count"],
        "block_manifest": policy["block_manifest"],
        "chunk_plan": policy["chunk_plan"],
        "disposition_policy": {
            "path": str(policy_path.relative_to(repo_root)),
            "sha256": sha256_file(policy_path),
        },
        "structural_accounting": {
            "total_blocks": len(ledger),
            "eligible_blocks": counts["eligible"],
            "excluded_blocks": counts["excluded"],
            "context_only_blocks": counts["context_only"],
            "embedded_media_count": len(policy["media_dispositions"]),
        },
        "media_dispositions": policy["media_dispositions"],
        "provider_calls": 0,
        "accounted_cost_cents": 0,
        "google_sheets_interactions": 0,
    }
    require_source_readiness(profile)
    write_new_json((repo_root / args.output_ledger).resolve(), ledger, jsonl=True)
    write_new_json((repo_root / args.output_profile).resolve(), profile)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
