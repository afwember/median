from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml

from .bundles import build_reconciliation_bundles, orphaned_mapped_evidence
from .canonical import content_id, sha256_file, write_new_json
from .errors import ContractError, Gate5Error
from .identity import identity_card_errors, transition_identity_card
from .runtime import runtime_errors, runtime_report
from .schema import validate_artifact
from .scope import require_input_paths, require_new_output_path
from .states import transition_receipt
from .structure import Block, parse_markdown, plan_chunks
from .validation import validate_atoms, validate_block_dispositions
from .workorders import verify_work_order


def _preflight(args: argparse.Namespace) -> int:
    report = runtime_report(
        [Path(path) for path in args.credential_path],
        Path(args.lock) if args.lock else None,
    )
    errors = runtime_errors(report)
    report["result"] = "PASS" if not errors else "FAIL"
    report["errors"] = errors
    if args.output:
        output = require_new_output_path(Path(args.repo_root), Path(args.output))
        write_new_json(output, report)
    else:
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


def _read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError(f"JSON root must be an object: {path}")
    return value


def _read_yaml(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError(f"YAML root must be an object: {path}")
    return value


def _profile(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    supplied = {
        "card": Path(args.card),
        "block_manifest": Path(args.block_manifest),
        "frozen_manifest": Path(args.frozen_manifest),
        "source_disposition": Path(args.source_disposition),
        "reuse_disposition": Path(args.reuse_disposition),
    }
    require_input_paths(
        repo_root,
        supplied.values(),
        [Path("m050/extraction/control"), Path("m050/extraction/audit")],
    )
    resolved = {
        key: (repo_root / path).resolve() if not path.is_absolute() else path.resolve()
        for key, path in supplied.items()
    }
    card = _read_json(resolved["card"])
    block_manifest = _read_json(resolved["block_manifest"])
    frozen_manifest = _read_json(resolved["frozen_manifest"])
    source_disposition = _read_yaml(resolved["source_disposition"])
    reuse_disposition = _read_yaml(resolved["reuse_disposition"])
    errors = identity_card_errors(
        repo_root,
        card,
        block_manifest,
        frozen_manifest,
        source_disposition,
        reuse_disposition,
    )
    report = {
        "schema_version": "M050-IDENTITY-CARD-VALIDATION-0.1",
        "card_id": card["card_id"],
        "source_id": card["source_id"],
        "passed": not errors,
        "errors": errors,
    }
    if args.output:
        output = require_new_output_path(repo_root, Path(args.output))
        write_new_json(output, report)
    else:
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


def _profile_transition(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    supplied = {
        "card": Path(args.card),
        "block_manifest": Path(args.block_manifest),
        "frozen_manifest": Path(args.frozen_manifest),
        "source_disposition": Path(args.source_disposition),
        "reuse_disposition": Path(args.reuse_disposition),
    }
    if args.predecessor_receipt:
        supplied["predecessor_receipt"] = Path(args.predecessor_receipt)
    require_input_paths(
        repo_root,
        supplied.values(),
        [Path("m050/extraction/control"), Path("m050/extraction/audit")],
    )
    resolved = {
        key: (repo_root / path).resolve() if not path.is_absolute() else path.resolve()
        for key, path in supplied.items()
    }
    card = _read_json(resolved["card"])
    block_manifest = _read_json(resolved["block_manifest"])
    frozen_manifest = _read_json(resolved["frozen_manifest"])
    source_disposition = _read_yaml(resolved["source_disposition"])
    reuse_disposition = _read_yaml(resolved["reuse_disposition"])
    errors = identity_card_errors(
        repo_root,
        card,
        block_manifest,
        frozen_manifest,
        source_disposition,
        reuse_disposition,
    )
    if errors:
        raise ContractError("identity card failed pre-transition validation: " + "; ".join(errors))
    transitioned = transition_identity_card(card, args.new_status)
    transitioned_errors = identity_card_errors(
        repo_root,
        transitioned,
        block_manifest,
        frozen_manifest,
        source_disposition,
        reuse_disposition,
    )
    if transitioned_errors:
        raise ContractError(
            "transitioned identity card failed validation: " + "; ".join(transitioned_errors)
        )
    predecessor_hash = (
        sha256_file(resolved["predecessor_receipt"])
        if "predecessor_receipt" in resolved
        else None
    )
    receipt = transition_receipt(
        machine="identity_card",
        artifact_id=transitioned["card_id"],
        prior_state=card["status"],
        new_state=transitioned["status"],
        authority=args.authority,
        reason=args.reason,
        tool_version="median-gate5-0.1.0",
        predecessor_receipt_hash=predecessor_hash,
        timestamp=args.timestamp,
    )
    validate_artifact("transition_receipt", receipt)
    card_output = require_new_output_path(repo_root, Path(args.output_card))
    receipt_output = require_new_output_path(repo_root, Path(args.output_receipt))
    write_new_json(card_output, transitioned)
    write_new_json(receipt_output, receipt)
    print(
        json.dumps(
            {
                "card_id": transitioned["card_id"],
                "receipt_id": receipt["receipt_id"],
                "status": transitioned["status"],
                "source_id": transitioned["source_id"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def _block(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    source_path = Path(args.source_path)
    require_input_paths(
        repo_root,
        [source_path],
        [Path("m050/docs/baseline"), Path("m050/docs/v0.5")],
    )
    resolved = (repo_root / source_path).resolve()
    raw = resolved.read_text(encoding="utf-8", errors="strict")
    blocks = parse_markdown(args.source_id, raw)
    body = {
        "source_id": args.source_id,
        "source_sha256": sha256_file(resolved),
        "normalization_version": "M050-NORMALIZATION-0.1",
        "blocks": [block.to_dict() for block in blocks],
    }
    artifact = {
        "schema_version": "M050-BLOCK-MANIFEST-0.1",
        "manifest_id": content_id("bm", body),
        **body,
    }
    validate_artifact("block_manifest", artifact)
    output = require_new_output_path(repo_root, Path(args.output))
    write_new_json(output, artifact)
    return 0


def _plan(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    block_manifest = _read_json(Path(args.block_manifest))
    validate_artifact("block_manifest", block_manifest)
    blocks = [
        Block(**{**block, "status_markers": tuple(block["status_markers"])})
        for block in block_manifest["blocks"]
    ]
    chunks = plan_chunks(
        blocks,
        max_tokens=args.max_tokens,
        max_claim_blocks=args.max_claim_blocks,
    )
    body = {
        "source_id": block_manifest["source_id"],
        "block_manifest_id": block_manifest["manifest_id"],
        "max_tokens": args.max_tokens,
        "max_claim_blocks": args.max_claim_blocks,
        "chunks": chunks,
    }
    artifact = {
        "schema_version": "M050-CHUNK-PLAN-0.1",
        "plan_id": content_id("cp", body),
        **body,
    }
    validate_artifact("chunk_plan", artifact)
    output = require_new_output_path(repo_root, Path(args.output))
    write_new_json(output, artifact)
    return 0


def _verify_work_order(args: argparse.Namespace) -> int:
    work_order = _read_json(Path(args.work_order))
    report = verify_work_order(Path(args.repo_root).resolve(), work_order)
    report.update(
        schema_version="M050-WORK-ORDER-VERIFICATION-0.1",
        work_order_id=work_order["work_order_id"],
    )
    if args.output:
        output = require_new_output_path(Path(args.repo_root), Path(args.output))
        write_new_json(output, report)
    else:
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0


def _validate_proposal(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    block_manifest = _read_json(Path(args.block_manifest))
    proposal = _read_json(Path(args.proposal))
    validate_artifact("block_manifest", block_manifest)
    validate_artifact("proposal", proposal)
    if block_manifest["source_id"] != proposal["source_id"]:
        raise ContractError("proposal and block manifest source IDs differ")
    dispositions = validate_block_dispositions(
        block_manifest["blocks"], proposal["dispositions"]
    )
    atoms = validate_atoms(
        proposal["source_id"], block_manifest["blocks"], proposal["dispositions"]
    )
    body = {
        "proposal_set_id": proposal["proposal_set_id"],
        "validator_version": "0.1.0",
        "passed": dispositions["passed"] and atoms["passed"],
        "checks": {"block_dispositions": dispositions, "atoms": atoms},
        "normalization_events": [
            {
                "proposal_id": result["proposal_id"],
                "events": result["normalization_events"],
            }
            for result in atoms["atom_results"]
            if result["normalization_events"]
        ],
        "anomalies": [
            {"kind": "low_yield", "block_id": block_id}
            for block_id in atoms["low_yield_review"]
        ],
    }
    report = {
        "schema_version": "M050-VALIDATION-REPORT-0.1",
        "report_id": content_id("vr", body),
        **body,
    }
    validate_artifact("validation_report", report)
    output = require_new_output_path(repo_root, Path(args.output))
    write_new_json(output, report)
    return 0 if report["passed"] else 1


def _bundle(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    mapping_value = json.loads(Path(args.mappings).read_text(encoding="utf-8"))
    if not isinstance(mapping_value, list):
        raise ContractError("mapping input root must be an array")
    aliases = (
        json.loads(Path(args.aliases).read_text(encoding="utf-8")) if args.aliases else {}
    )
    if not isinstance(aliases, dict):
        raise ContractError("alias input root must be an object")
    bundles, exceptional = build_reconciliation_bundles(mapping_value, aliases)
    artifact = {
        "schema_version": "M050-BUNDLE-BUILD-REPORT-0.1",
        "bundles": bundles,
        "exceptional_mappings": exceptional,
        "orphaned_mapped_evidence": orphaned_mapped_evidence(mapping_value, bundles),
    }
    output = require_new_output_path(repo_root, Path(args.output))
    write_new_json(output, artifact)
    return 0 if not artifact["orphaned_mapped_evidence"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="median-gate5")
    subparsers = parser.add_subparsers(dest="command", required=True)
    preflight = subparsers.add_parser("preflight", help="verify the local offline runtime")
    preflight.add_argument(
        "--credential-path",
        action="append",
        default=[],
        help="check existence and mode only; file contents are never read",
    )
    preflight.add_argument(
        "--lock",
        help="verify every exact package version recorded in this requirements lock",
    )
    preflight.add_argument("--output", help="append the preflight report at this new path")
    preflight.add_argument("--repo-root", default=".")
    preflight.set_defaults(func=_preflight)

    block = subparsers.add_parser("block", help="create a frozen-source block manifest")
    block.add_argument("--repo-root", default=".")
    block.add_argument("--source-id", required=True)
    block.add_argument("--source-path", required=True)
    block.add_argument("--output", required=True)
    block.set_defaults(func=_block)

    profile = subparsers.add_parser("profile", help="validate a source identity card")
    profile.add_argument("--repo-root", default=".")
    profile.add_argument("--card", required=True)
    profile.add_argument("--block-manifest", required=True)
    profile.add_argument("--frozen-manifest", required=True)
    profile.add_argument("--source-disposition", required=True)
    profile.add_argument("--reuse-disposition", required=True)
    profile.add_argument("--output")
    profile.set_defaults(func=_profile)

    profile_transition = subparsers.add_parser(
        "profile-transition", help="issue a new identity-card state revision and receipt"
    )
    profile_transition.add_argument("--repo-root", default=".")
    profile_transition.add_argument("--card", required=True)
    profile_transition.add_argument("--block-manifest", required=True)
    profile_transition.add_argument("--frozen-manifest", required=True)
    profile_transition.add_argument("--source-disposition", required=True)
    profile_transition.add_argument("--reuse-disposition", required=True)
    profile_transition.add_argument("--new-status", required=True, choices=["reviewed", "approved"])
    profile_transition.add_argument("--authority", required=True)
    profile_transition.add_argument("--reason", required=True)
    profile_transition.add_argument("--timestamp")
    profile_transition.add_argument("--predecessor-receipt")
    profile_transition.add_argument("--output-card", required=True)
    profile_transition.add_argument("--output-receipt", required=True)
    profile_transition.set_defaults(func=_profile_transition)

    plan = subparsers.add_parser("plan", help="create a dual-limit chunk plan")
    plan.add_argument("--repo-root", default=".")
    plan.add_argument("--block-manifest", required=True)
    plan.add_argument("--max-tokens", type=int, required=True)
    plan.add_argument("--max-claim-blocks", type=int, required=True)
    plan.add_argument("--output", required=True)
    plan.set_defaults(func=_plan)

    work_order = subparsers.add_parser("verify-work-order")
    work_order.add_argument("--repo-root", default=".")
    work_order.add_argument("--work-order", required=True)
    work_order.add_argument("--output")
    work_order.set_defaults(func=_verify_work_order)

    proposal = subparsers.add_parser("validate-proposal")
    proposal.add_argument("--repo-root", default=".")
    proposal.add_argument("--block-manifest", required=True)
    proposal.add_argument("--proposal", required=True)
    proposal.add_argument("--output", required=True)
    proposal.set_defaults(func=_validate_proposal)

    bundle = subparsers.add_parser("bundle")
    bundle.add_argument("--repo-root", default=".")
    bundle.add_argument("--mappings", required=True)
    bundle.add_argument("--aliases")
    bundle.add_argument("--output", required=True)
    bundle.set_defaults(func=_bundle)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        code = args.func(args)
    except (Gate5Error, json.JSONDecodeError, OSError, ValueError) as exc:
        print(f"MEDIAN GATE 5: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    raise SystemExit(code)


if __name__ == "__main__":
    main()
