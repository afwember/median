#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import urllib.error
import urllib.request

from median_gate5.canonical import content_id, sha256_file, write_new_bytes, write_new_json
from median_gate5.errors import ContractError, IntegrityError
from median_gate5.extraction_machine import (
    append_run_ledger_event,
    anthropic_usage_cost,
    build_anthropic_request,
    build_chunk_payload,
    build_generic_response_schema,
    build_generic_source_prompt,
    canonical_json_bytes,
    classify_anthropic_http_error,
    conservative_call_ceiling,
    debit_compile_state_spend,
    draft_block_dispositions,
    extract_anthropic_structured_response,
    read_run_ledger,
    plan_source_chunks,
    provider_preflight,
    require_run_ready_for_next_call,
    validate_extraction_response,
)
from median_gate5.schema import validate_artifact
from median_gate5.structure import parse_markdown


ENDPOINT = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"
SHELL_INTERPOLATION_ARTIFACT = re.compile(
    r"(?:^|\s)/(?:usr/)?bin/(?:ba|da|z)?sh(?:[.\s]|$)",
    re.IGNORECASE,
)


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError(f"JSON root must be an object: {path}")
    return value


def read_jsonl(path: Path) -> list[dict]:
    values = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if any(not isinstance(value, dict) for value in values):
        raise ContractError(f"JSONL entries must be objects: {path}")
    return values


def repo_file(repo_root: Path, supplied: str) -> Path:
    relative = Path(supplied)
    if relative.is_absolute():
        raise IntegrityError(f"configuration path must be repository-relative: {supplied}")
    target = (repo_root / relative).resolve()
    try:
        target.relative_to(repo_root)
    except ValueError as exc:
        raise IntegrityError(f"configuration path escapes repository: {supplied}") from exc
    if not target.is_file():
        raise IntegrityError(f"configuration input is not a file: {supplied}")
    if target == repo_root / "m051" or (repo_root / "m051") in target.parents:
        raise IntegrityError(f"m051 input is prohibited: {supplied}")
    return target


def require_approved_identity_card(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="strict")
    if "Status: `APPROVED`" not in text:
        raise ContractError("identity card is not marked APPROVED")
    if "Author/root of authority: Asa Wember" not in text:
        raise ContractError("identity card lacks Asa Wember as authorial authority")


def load_config(repo_root: Path, path: Path) -> tuple[dict, dict[str, Path]]:
    config = read_json(path)
    if config.get("schema_version") != "M050-EXTRACTION-MACHINE-CONFIG-0.1":
        raise ContractError("unsupported extraction-machine configuration")
    artifact_paths = config.get("artifacts")
    if not isinstance(artifact_paths, dict):
        raise ContractError("configuration lacks artifact paths")
    required = {
        "identity_card", "block_manifest",
        "disposition_ledger", "chunk_plan", "prompt", "response_schema"
    }
    missing = sorted(required - set(artifact_paths))
    if missing:
        raise ContractError("configuration artifact paths are incomplete: " + ", ".join(missing))
    resolved = {key: repo_file(repo_root, artifact_paths[key]) for key in required}
    hashes = config.get("artifact_sha256", {})
    for key, target in resolved.items():
        expected = hashes.get(key)
        if not expected or sha256_file(target) != expected:
            raise IntegrityError(f"configuration hash mismatch: {key}")
    require_approved_identity_card(resolved["identity_card"])
    if "_Prompt_v" not in resolved["prompt"].name:
        expected_prompt = build_generic_source_prompt(
            config.get("source_id", ""),
            config.get("allowed_streams", []),
            resolved["identity_card"].read_text(encoding="utf-8", errors="strict"),
        )
        if (
            resolved["prompt"].read_text(encoding="utf-8", errors="strict")
            != expected_prompt
        ):
            raise IntegrityError("active prompt differs from generic prompt builder")
    return config, resolved


def new_repo_output(repo_root: Path, supplied: str) -> Path:
    relative = Path(supplied)
    if relative.is_absolute():
        raise IntegrityError(f"scaffold output must be repository-relative: {supplied}")
    target = (repo_root / relative).resolve()
    extraction_root = (repo_root / "m050/extraction").resolve()
    try:
        target.relative_to(extraction_root)
    except ValueError as exc:
        raise IntegrityError(f"scaffold output escapes m050/extraction: {supplied}") from exc
    if target.exists() or target.is_symlink():
        raise IntegrityError(f"refusing to overwrite scaffold output: {supplied}")
    return target


def select_chunk(plan: dict, selector: str) -> dict:
    matches = [
        chunk
        for chunk in plan.get("chunks", [])
        if str(chunk.get("chunk_id", "")) == selector
        or str(chunk.get("ordinal", "")) == selector
        or f"C{int(chunk.get('ordinal', 0)):04d}" == selector
    ]
    if len(matches) != 1:
        raise ContractError(f"chunk selector did not resolve exactly once: {selector}")
    return matches[0]


def verify_packet(packet: dict) -> None:
    expected = packet.get("packet_sha256")
    body = dict(packet)
    body.pop("packet_sha256", None)
    actual = hashlib.sha256(canonical_json_bytes(body)).hexdigest()
    if not expected or expected != actual:
        raise IntegrityError("call packet internal SHA-256 mismatch")


def build_packet(repo_root: Path, config_path: Path, selector: str) -> dict:
    config, paths = load_config(repo_root, config_path)
    manifest = read_json(paths["block_manifest"])
    if manifest.get("source_id") != config.get("source_id"):
        raise ContractError("configuration and block manifest source IDs differ")
    if manifest.get("source_sha256") != config.get("source_sha256"):
        raise ContractError("configuration and block manifest source hashes differ")
    dispositions = read_jsonl(paths["disposition_ledger"])
    chunk = select_chunk(read_json(paths["chunk_plan"]), selector)
    payload = build_chunk_payload(manifest, dispositions, chunk)
    response_schema = read_json(paths["response_schema"])
    prompt = paths["prompt"].read_text(encoding="utf-8")
    provider = config.get("provider", {})
    request = build_anthropic_request(
        prompt=prompt,
        response_schema=response_schema,
        payload=payload,
        model=provider.get("model", ""),
        reasoning_effort=provider.get("reasoning_effort", ""),
        maximum_output_tokens=provider.get("maximum_output_tokens", 0),
        cache_ttl=provider.get("cache_ttl", ""),
    )
    pricing = config.get("pricing", {})
    ceiling = conservative_call_ceiling(request, pricing)
    body = {
        "schema_version": "M050-EXTRACTION-CALL-PACKET-0.1",
        "source_id": config["source_id"],
        "source_sha256": config["source_sha256"],
        "chunk_id": payload["chunk_id"],
        "configuration_path": str(config_path.relative_to(repo_root)),
        "configuration_sha256": sha256_file(config_path),
        "binding": {
            "artifact_sha256": config["artifact_sha256"],
            "model": provider["model"],
            "reasoning_effort": provider["reasoning_effort"],
            "cache_ttl": provider["cache_ttl"],
            "cache_required": provider.get("cache_required", True),
            "read_timeout_seconds": provider.get("read_timeout_seconds", 180),
        },
        "allowed_streams": config.get("allowed_streams", []),
        "pricing": pricing,
        "payload": payload,
        "provider_request": request,
        "cache_miss_call_ceiling_usd": format(ceiling, "f"),
    }
    body["packet_sha256"] = hashlib.sha256(canonical_json_bytes(body)).hexdigest()
    return body


def build_outcome(packet: dict, raw_response: dict, raw_sha256: str) -> dict:
    structured = extract_anthropic_structured_response(raw_response)
    config_schema = packet["provider_request"]["output_config"]["format"]["schema"]
    validation = validate_extraction_response(
        payload=packet["payload"],
        response=structured,
        response_schema=config_schema,
        allowed_streams=packet["allowed_streams"],
    )
    usage = raw_response.get("usage", {})
    cache_creation = int(usage.get("cache_creation_input_tokens", 0) or 0)
    cache_read = int(usage.get("cache_read_input_tokens", 0) or 0)
    cache_effective = cache_creation > 0 or cache_read > 0
    if packet["binding"].get("cache_required") is True and not cache_effective:
        validation["passed"] = False
        validation["decision_required"] = True
        validation["errors"].append(
            "required Claude prompt caching was neither created nor read"
        )
    cost = anthropic_usage_cost(
        usage,
        packet["pricing"],
        cache_ttl=packet["binding"]["cache_ttl"],
    )
    return {
        "schema_version": "M050-EXTRACTION-CALL-OUTCOME-0.1",
        "source_id": packet["source_id"],
        "chunk_id": packet["chunk_id"],
        "packet_sha256": packet["packet_sha256"],
        "raw_response_sha256": raw_sha256,
        "provider_message_id": raw_response.get("id"),
        "model": raw_response.get("model"),
        "stop_reason": raw_response.get("stop_reason"),
        "usage": usage,
        "cost": cost,
        "cache": {
            "requested_ttl": packet["binding"]["cache_ttl"],
            "required": packet["binding"].get("cache_required", True),
            "effective": cache_effective,
            "creation_input_tokens": cache_creation,
            "read_input_tokens": cache_read,
        },
        "mechanical_validation": validation,
        "structured_proposal": structured,
        "substantive_review": "pending",
        "review_required": True,
    }


def command_prepare(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    config_path = repo_file(repo_root, args.config)
    output = Path(args.output)
    if not output.is_absolute():
        output = (repo_root / output).resolve()
    packet = build_packet(repo_root, config_path, args.chunk)
    write_new_json(output, packet)
    packet_file_sha256 = sha256_file(output)
    print(json.dumps({
        "source_id": packet["source_id"],
        "chunk_id": packet["chunk_id"],
        "packet_sha256": packet["packet_sha256"],
        "packet_file_sha256": packet_file_sha256,
        "cache_ttl": packet["binding"]["cache_ttl"],
        "cache_miss_call_ceiling_usd": packet["cache_miss_call_ceiling_usd"],
        "target_blocks": packet["payload"]["required_target_disposition_count"],
    }, sort_keys=True))
    return 0


def command_scaffold(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    source_path = repo_file(repo_root, args.source_path)
    card_path = repo_file(repo_root, args.identity_card)
    require_approved_identity_card(card_path)
    if not args.allowed_stream or len(args.allowed_stream) != len(set(args.allowed_stream)):
        raise ContractError("scaffold requires one or more unique allowed streams")
    outputs = {
        "block_manifest": new_repo_output(repo_root, args.output_block_manifest),
        "disposition_ledger": new_repo_output(repo_root, args.output_disposition_ledger),
        "chunk_plan": new_repo_output(repo_root, args.output_chunk_plan),
        "prompt": new_repo_output(repo_root, args.output_prompt),
        "response_schema": new_repo_output(repo_root, args.output_response_schema),
        "config": new_repo_output(repo_root, args.output_config),
    }
    if len(set(outputs.values())) != len(outputs):
        raise ContractError("scaffold output paths must be distinct")

    raw = source_path.read_text(encoding="utf-8", errors="strict")
    blocks = parse_markdown(args.source_id, raw)
    manifest_body = {
        "source_id": args.source_id,
        "source_sha256": sha256_file(source_path),
        "normalization_version": "M050-NORMALIZATION-0.1",
        "blocks": [block.to_dict() for block in blocks],
    }
    manifest = {
        "schema_version": "M050-BLOCK-MANIFEST-0.1",
        "manifest_id": content_id("bm", manifest_body),
        **manifest_body,
    }
    validate_artifact("block_manifest", manifest)
    dispositions = draft_block_dispositions(manifest)
    plan = plan_source_chunks(
        manifest,
        dispositions,
        max_input_tokens=args.max_input_tokens,
        target_blocks_per_chunk=args.target_blocks_per_chunk,
        quantization_basis="provisional_pre_pilot_scaffold",
    )
    prompt = build_generic_source_prompt(
        args.source_id,
        args.allowed_stream,
        card_path.read_text(encoding="utf-8", errors="strict"),
    )
    schema = build_generic_response_schema(args.source_id, args.allowed_stream)

    write_new_json(outputs["block_manifest"], manifest)
    disposition_bytes = b"".join(canonical_json_bytes(item) for item in dispositions)
    write_new_bytes(outputs["disposition_ledger"], disposition_bytes)
    write_new_json(outputs["chunk_plan"], plan)
    write_new_bytes(outputs["prompt"], prompt.encode("utf-8"))
    write_new_json(outputs["response_schema"], schema)

    relative = {
        key: path.relative_to(repo_root).as_posix()
        for key, path in outputs.items()
        if key != "config"
    }
    relative.update({
        "identity_card": card_path.relative_to(repo_root).as_posix(),
    })
    artifact_sha256 = {
        key: sha256_file(repo_root / path)
        for key, path in relative.items()
    }
    config = {
        "schema_version": "M050-EXTRACTION-MACHINE-CONFIG-0.1",
        "status": "DRAFT_REQUIRES_SOURCE_REVIEW_AND_PILOT_CALIBRATION",
        "source_id": args.source_id,
        "source_path": source_path.relative_to(repo_root).as_posix(),
        "source_sha256": sha256_file(source_path),
        "allowed_streams": args.allowed_stream,
        "artifacts": relative,
        "artifact_sha256": artifact_sha256,
        "provider": {
            "name": "Anthropic",
            "model": args.model,
            "reasoning_effort": args.reasoning_effort,
            "maximum_output_tokens": args.maximum_output_tokens,
            "cache_ttl": "1h",
            "cache_required": True,
            "cache_boundary": "stable_system_prefix",
            "read_timeout_seconds": 180,
        },
        "pricing": {
            "input_usd_per_million_tokens": "2",
            "output_usd_per_million_tokens": "10",
            "cache_read_multiplier": "0.1",
            "cache_5m_write_multiplier": "1.25",
            "cache_1h_write_multiplier": "2",
        },
        "execution": {
            "cadence": "sequential_one_call_review",
            "next_chunk_requires_substantive_review_of_prior_chunk": True,
        },
    }
    write_new_json(outputs["config"], config)
    print(json.dumps({
        "source_id": args.source_id,
        "source_sha256": config["source_sha256"],
        "blocks": len(blocks),
        "chunks": len(plan["chunks"]),
        "status": config["status"],
        "provider_permission": "derived_from_canonical_source_work_and_budget",
    }, sort_keys=True))
    return 0


def command_replan(args: argparse.Namespace) -> int:
    """Re-apportion a complete approved source after quantization calibration."""
    repo_root = Path(args.repo_root).resolve()
    manifest_path = repo_file(repo_root, args.block_manifest)
    disposition_path = repo_file(repo_root, args.disposition_ledger)
    output = new_repo_output(repo_root, args.output_chunk_plan)
    manifest = read_json(manifest_path)
    dispositions = read_jsonl(disposition_path)
    plan = plan_source_chunks(
        manifest,
        dispositions,
        max_input_tokens=args.max_input_tokens,
        target_blocks_per_chunk=args.target_blocks_per_chunk,
        quantization_basis=args.calibration_basis,
    )
    plan["status"] = "OFFLINE_RECALIBRATION_REQUIRES_PILOT"
    plan["predecessor_chunk_plan"] = args.predecessor_chunk_plan
    write_new_json(output, plan)
    print(json.dumps({
        "source_id": plan["source_id"],
        "target_blocks_per_chunk": args.target_blocks_per_chunk,
        "generated_chunk_count": len(plan["chunks"]),
        "chunk_count_is_input": False,
        "output_sha256": sha256_file(output),
    }, sort_keys=True))
    return 0


def command_replay(args: argparse.Namespace) -> int:
    packet_path = Path(args.packet).resolve()
    raw_path = Path(args.response).resolve()
    packet = read_json(packet_path)
    verify_packet(packet)
    raw_bytes = raw_path.read_bytes()
    raw = json.loads(raw_bytes)
    outcome = build_outcome(packet, raw, hashlib.sha256(raw_bytes).hexdigest())
    output = Path(args.output).resolve()
    write_new_json(output, outcome)
    print(json.dumps({
        "source_id": outcome["source_id"],
        "chunk_id": outcome["chunk_id"],
        "mechanical_passed": outcome["mechanical_validation"]["passed"],
        "decision_required": outcome["mechanical_validation"]["decision_required"],
        "cost_usd": outcome["cost"]["total_usd"],
        "cache_read_tokens": outcome["cache"]["read_input_tokens"],
    }, sort_keys=True))
    return 0 if outcome["mechanical_validation"]["passed"] else 1


def _require_state_matches_latest_call(
    repo_root: Path, state: dict, events: list[dict]
) -> None:
    captured = [event for event in events if event.get("state") == "call_captured"]
    if not captured:
        return
    latest_capture = captured[-1]
    outcome_path = repo_file(
        repo_root, state.get("calibration", {}).get("latest_outcome", "")
    )
    if sha256_file(outcome_path) != latest_capture.get("outcome_sha256"):
        raise ContractError("canonical state has not reconciled the latest captured call")
    latest = state.get("latest_provider_attempt", {})
    if (
        latest.get("chunk_id") != latest_capture.get("chunk_id")
        or (
            latest_capture.get("exact_cost_usd") is not None
            and latest.get("exact_cost_usd") != latest_capture.get("exact_cost_usd")
        )
    ):
        raise ContractError("canonical latest-attempt state disagrees with the run ledger")
    if events[-1].get("state") in {"review_passed", "review_failed"}:
        if latest.get("review_state") != events[-1].get("state"):
            raise ContractError("canonical review state disagrees with the run ledger")


def _preflight(
    packet: dict,
    packet_file_hash: str,
    state: dict,
    ledger_path: Path,
    repo_root: Path,
) -> dict:
    calibration = state.get("calibration", {})
    if packet.get("source_id") != state.get("source", {}).get("id"):
        raise ContractError("packet does not belong to the active source")
    if packet.get("chunk_id") != calibration.get("pilot_chunk_id"):
        raise ContractError("packet is not the current canonical chunk")
    if packet.get("configuration_path") != calibration.get("configuration"):
        raise ContractError("packet does not use the active source configuration")
    config_path = repo_file(repo_root, packet["configuration_path"])
    if packet.get("configuration_sha256") != sha256_file(config_path):
        raise IntegrityError("packet configuration binding is stale")
    rebuilt = build_packet(repo_root, config_path, packet["chunk_id"])
    if rebuilt.get("packet_sha256") != packet.get("packet_sha256"):
        raise IntegrityError("packet is not the deterministic current configuration output")
    if packet.get("cache_miss_call_ceiling_usd") != calibration.get(
        "cache_miss_call_ceiling_usd"
    ):
        raise ContractError("packet call ceiling disagrees with canonical state")

    events = read_run_ledger(ledger_path)
    _require_state_matches_latest_call(repo_root, state, events)
    require_run_ready_for_next_call(
        events,
        packet["source_id"],
        packet["chunk_id"],
        packet_file_hash,
    )
    return provider_preflight(
        compile_state=state,
        source_id=packet["source_id"],
        call_ceiling_usd=Decimal(packet["cache_miss_call_ceiling_usd"]),
    )


def command_preflight(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    packet_path = Path(args.packet).resolve()
    packet = read_json(packet_path)
    verify_packet(packet)
    result = _preflight(
        packet,
        sha256_file(packet_path),
        read_json(repo_file(repo_root, args.compile_state)),
        Path(args.run_ledger),
        repo_root,
    )
    print(json.dumps(result, sort_keys=True))
    return 0


def command_send(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve()
    packet_path = Path(args.packet).resolve()
    packet_bytes = packet_path.read_bytes()
    packet_file_hash = hashlib.sha256(packet_bytes).hexdigest()
    if packet_file_hash != args.expected_packet_sha256:
        raise IntegrityError("bound packet file SHA-256 mismatch")
    packet = json.loads(packet_bytes)
    if not isinstance(packet, dict):
        raise ContractError("call packet root must be an object")
    verify_packet(packet)
    state = read_json(repo_file(repo_root, args.compile_state))
    ledger_path = Path(args.run_ledger).resolve()
    preflight = _preflight(packet, packet_file_hash, state, ledger_path, repo_root)

    raw_output = Path(args.raw_response).resolve()
    outcome_output = Path(args.outcome).resolve()
    for output in (raw_output, outcome_output):
        if output.exists():
            raise IntegrityError(f"refusing to overwrite: {output}")

    key = Path(args.api_key_file).read_text(encoding="utf-8").strip()
    if not key or "\n" in key:
        raise ContractError("API key file must contain one non-empty raw key")
    request_bytes = canonical_json_bytes(packet["provider_request"])
    request = urllib.request.Request(
        ENDPOINT,
        data=request_bytes,
        method="POST",
        headers={
            "anthropic-version": ANTHROPIC_VERSION,
            "content-type": "application/json",
            "x-api-key": key,
        },
    )
    submitted_at = datetime.now(timezone.utc).isoformat()
    status = None
    response_headers: dict[str, str] = {}
    raw_bytes = b""
    transport_error = None
    try:
        with urllib.request.urlopen(
            request, timeout=packet["binding"].get("read_timeout_seconds", 180)
        ) as response:
            status = response.status
            raw_bytes = response.read()
            response_headers = dict(response.headers.items())
    except urllib.error.HTTPError as exc:
        status = exc.code
        raw_bytes = exc.read()
        response_headers = dict(exc.headers.items())
        transport_error = classify_anthropic_http_error(exc.code, raw_bytes)
    except Exception as exc:
        transport_error = f"{type(exc).__name__}:{exc}"
    if raw_bytes:
        write_new_bytes(raw_output, raw_bytes)
    if status is None or not 200 <= status < 300 or not raw_bytes:
        failure = {
            "schema_version": "M050-EXTRACTION-CALL-OUTCOME-0.1",
            "source_id": packet["source_id"],
            "chunk_id": packet["chunk_id"],
            "packet_sha256": packet["packet_sha256"],
            "submitted_at_utc": submitted_at,
            "provider_call_made": True,
            "http_status": status,
            "request_id": response_headers.get("request-id"),
            "transport_error": transport_error,
            "raw_response_sha256": hashlib.sha256(raw_bytes).hexdigest() if raw_bytes else None,
            "preflight": preflight,
            "substantive_review": "blocked_transport_failure",
            "spend_reconciliation_required": True,
        }
        write_new_json(outcome_output, failure)
        append_run_ledger_event(
            ledger_path,
            {
                "state": "call_captured",
                "source_id": packet["source_id"],
                "chunk_id": packet["chunk_id"],
                "packet_file_sha256": packet_file_hash,
                "outcome_sha256": sha256_file(outcome_output),
                "mechanical_passed": False,
                "decision_required": True,
                "transport_error": transport_error,
                "canonical_spend_update_required": True,
            },
        )
        return 1

    raw: dict = {}
    try:
        candidate = json.loads(raw_bytes)
        if not isinstance(candidate, dict):
            raise ContractError("provider response root is not an object")
        raw = candidate
        outcome = build_outcome(packet, raw, hashlib.sha256(raw_bytes).hexdigest())
    except Exception as exc:
        failure = {
            "schema_version": "M050-EXTRACTION-CALL-OUTCOME-0.1",
            "source_id": packet["source_id"],
            "chunk_id": packet["chunk_id"],
            "packet_sha256": packet["packet_sha256"],
            "submitted_at_utc": submitted_at,
            "provider_call_made": True,
            "http_status": status,
            "request_id": response_headers.get("request-id"),
            "raw_response_sha256": hashlib.sha256(raw_bytes).hexdigest(),
            "provider_message_id": raw.get("id"),
            "usage": raw.get("usage"),
            "capture_error": f"{type(exc).__name__}:{exc}",
            "preflight": preflight,
            "substantive_review": "blocked_invalid_provider_response",
        }
        cost_reconciled = False
        updated_state = state
        usage = raw.get("usage")
        if isinstance(usage, dict):
            try:
                cost = anthropic_usage_cost(
                    usage,
                    packet["pricing"],
                    cache_ttl=packet["binding"]["cache_ttl"],
                )
                failure["cost"] = cost
                updated_state = debit_compile_state_spend(state, cost["total_usd"])
                cost_reconciled = True
            except (ContractError, KeyError, TypeError, ValueError):
                pass
        failure["cost_reconciled"] = cost_reconciled
        failure["canonical_spend_update_required"] = cost_reconciled
        write_new_json(outcome_output, failure)
        ledger_event = {
            "state": "call_captured",
            "source_id": packet["source_id"],
            "chunk_id": packet["chunk_id"],
            "packet_file_sha256": packet_file_hash,
            "outcome_sha256": sha256_file(outcome_output),
            "mechanical_passed": False,
            "decision_required": True,
            "capture_error": failure["capture_error"],
            "cost_reconciled": cost_reconciled,
            "canonical_spend_update_required": cost_reconciled,
        }
        if cost_reconciled:
            ledger_event["exact_cost_usd"] = failure["cost"]["total_usd"]
        append_run_ledger_event(
            ledger_path,
            ledger_event,
        )
        if cost_reconciled:
            print(json.dumps({
                "cost_usd": failure["cost"]["total_usd"],
                "remaining_spend_usd": updated_state["spend"]["remaining_usd"],
                "canonical_spend_update_required": True,
            }, sort_keys=True))
        return 1
    outcome.update({
        "submitted_at_utc": submitted_at,
        "provider_call_made": True,
        "http_status": status,
        "request_id": response_headers.get("request-id"),
        "preflight": preflight,
        "canonical_spend_update_required": True,
    })
    updated_state = debit_compile_state_spend(state, outcome["cost"]["total_usd"])
    write_new_json(outcome_output, outcome)
    append_run_ledger_event(
        ledger_path,
        {
            "state": "call_captured",
            "source_id": outcome["source_id"],
            "chunk_id": outcome["chunk_id"],
            "packet_file_sha256": packet_file_hash,
            "outcome_sha256": sha256_file(outcome_output),
            "mechanical_passed": outcome["mechanical_validation"]["passed"],
            "decision_required": outcome["mechanical_validation"]["decision_required"],
            "exact_cost_usd": outcome["cost"]["total_usd"],
            "display_cost_usd_rounded_up": outcome["cost"]["display_usd_rounded_up"],
            "cache_effective": outcome["cache"]["effective"],
            "cache_creation_input_tokens": outcome["cache"]["creation_input_tokens"],
            "cache_read_input_tokens": outcome["cache"]["read_input_tokens"],
            "canonical_spend_update_required": True,
        },
    )
    print(json.dumps({
        "http_status": status,
        "source_id": outcome["source_id"],
        "chunk_id": outcome["chunk_id"],
        "mechanical_passed": outcome["mechanical_validation"]["passed"],
        "decision_required": outcome["mechanical_validation"]["decision_required"],
        "cost_usd": outcome["cost"]["total_usd"],
        "remaining_spend_usd": updated_state["spend"]["remaining_usd"],
        "canonical_spend_update_required": True,
        "cache_read_tokens": outcome["cache"]["read_input_tokens"],
    }, sort_keys=True))
    return 0 if outcome["mechanical_validation"]["passed"] else 1


def command_review(args: argparse.Namespace) -> int:
    ledger_path = Path(args.run_ledger).resolve()
    events = read_run_ledger(ledger_path)
    outcome_path = Path(args.outcome).resolve()
    outcome = read_json(outcome_path)
    outcome_sha256 = sha256_file(outcome_path)
    transport_classification = getattr(args, "transport_classification", None)
    if transport_classification:
        if args.result != "failed":
            raise ContractError("transport classification requires a failed review")
        if not events or events[-1].get("state") != "review_failed":
            raise ContractError("transport classification requires a reviewed failure")
        if events[-1].get("outcome_sha256") != outcome_sha256:
            raise IntegrityError("transport classification outcome is not the latest review")
        if events[-1].get("transport_classification"):
            raise ContractError("transport failure is already classified")
        captured = next(
            (
                event for event in reversed(events)
                if event.get("state") == "call_captured"
                and event.get("outcome_sha256") == outcome_sha256
            ),
            None,
        )
        if captured is None or captured.get("transport_error") != "HTTPError:400":
            raise ContractError("only a preserved generic HTTP 400 may be classified")
        raw_response = getattr(args, "raw_response", None)
        if not raw_response:
            raise ContractError("transport classification requires the preserved raw response")
        raw_bytes = Path(raw_response).resolve().read_bytes()
        if hashlib.sha256(raw_bytes).hexdigest() != outcome.get("raw_response_sha256"):
            raise IntegrityError("transport classification raw response binding drifted")
        if classify_anthropic_http_error(400, raw_bytes) != (
            "HTTPError:400:anthropic_credit_balance_too_low"
        ):
            raise ContractError("preserved HTTP 400 is not the exact Anthropic credit error")
    else:
        if not events or events[-1].get("state") != "call_captured":
            raise ContractError("run ledger has no captured call awaiting review")
        captured = events[-1]
        if captured.get("outcome_sha256") != outcome_sha256:
            raise IntegrityError("review outcome does not match the pending ledger event")
    if SHELL_INTERPOLATION_ARTIFACT.search(args.reason):
        raise ContractError(
            "review reason contains a likely shell-interpolation artifact; "
            "resubmit it with literal-safe quoting"
        )
    if args.result == "passed":
        validation = outcome.get("mechanical_validation", {})
        if validation.get("passed") is not True:
            raise ContractError("substantive review cannot pass a mechanically invalid outcome")
        state = "review_passed"
    else:
        state = "review_failed"
    event_body = {
        "state": state,
        "source_id": captured["source_id"],
        "chunk_id": captured["chunk_id"],
        "outcome_sha256": outcome_sha256,
        "reviewer": args.reviewer,
        "reason": args.reason,
    }
    if transport_classification:
        event_body["transport_classification"] = transport_classification
    event = append_run_ledger_event(ledger_path, event_body)
    print(json.dumps({
        "event_id": event["event_id"],
        "state": state,
        "source_id": event["source_id"],
        "chunk_id": event["chunk_id"],
        "next_step": "reconcile canonical state, then derive readiness from source work, offline gates, and budget",
    }, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="m050-extraction-machine")
    sub = parser.add_subparsers(dest="command", required=True)

    prepare = sub.add_parser("prepare")
    prepare.add_argument("--repo-root", default=".")
    prepare.add_argument("--config", required=True)
    prepare.add_argument("--chunk", required=True)
    prepare.add_argument("--output", required=True)
    prepare.set_defaults(func=command_prepare)

    scaffold = sub.add_parser("scaffold")
    scaffold.add_argument("--repo-root", default=".")
    scaffold.add_argument("--source-id", required=True)
    scaffold.add_argument("--source-path", required=True)
    scaffold.add_argument("--identity-card", required=True)
    scaffold.add_argument("--allowed-stream", action="append", required=True)
    scaffold.add_argument("--max-input-tokens", type=int, default=12000)
    scaffold.add_argument("--target-blocks-per-chunk", type=int, required=True)
    scaffold.add_argument("--model", default="claude-sonnet-5")
    scaffold.add_argument("--reasoning-effort", default="low")
    scaffold.add_argument("--maximum-output-tokens", type=int, default=6000)
    scaffold.add_argument("--output-block-manifest", required=True)
    scaffold.add_argument("--output-disposition-ledger", required=True)
    scaffold.add_argument("--output-chunk-plan", required=True)
    scaffold.add_argument("--output-prompt", required=True)
    scaffold.add_argument("--output-response-schema", required=True)
    scaffold.add_argument("--output-config", required=True)
    scaffold.set_defaults(func=command_scaffold)

    replan = sub.add_parser("replan")
    replan.add_argument("--repo-root", default=".")
    replan.add_argument("--block-manifest", required=True)
    replan.add_argument("--disposition-ledger", required=True)
    replan.add_argument("--max-input-tokens", type=int, default=12000)
    replan.add_argument("--target-blocks-per-chunk", type=int, required=True)
    replan.add_argument("--calibration-basis", required=True)
    replan.add_argument("--predecessor-chunk-plan", required=True)
    replan.add_argument("--output-chunk-plan", required=True)
    replan.set_defaults(func=command_replan)

    replay = sub.add_parser("replay")
    replay.add_argument("--packet", required=True)
    replay.add_argument("--response", required=True)
    replay.add_argument("--output", required=True)
    replay.set_defaults(func=command_replay)

    preflight = sub.add_parser("preflight")
    preflight.add_argument("--repo-root", default=".")
    preflight.add_argument("--packet", required=True)
    preflight.add_argument(
        "--compile-state",
        default="m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json",
    )
    preflight.add_argument("--run-ledger", required=True)
    preflight.set_defaults(func=command_preflight)

    send = sub.add_parser("send")
    send.add_argument("--repo-root", default=".")
    send.add_argument("--packet", required=True)
    send.add_argument("--expected-packet-sha256", required=True)
    send.add_argument(
        "--compile-state",
        default="m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json",
    )
    send.add_argument("--run-ledger", required=True)
    send.add_argument("--api-key-file", required=True)
    send.add_argument("--raw-response", required=True)
    send.add_argument("--outcome", required=True)
    send.set_defaults(func=command_send)

    review = sub.add_parser("review")
    review.add_argument("--run-ledger", required=True)
    review.add_argument("--outcome", required=True)
    review.add_argument("--result", choices=["passed", "failed"], required=True)
    review.add_argument("--reviewer", required=True)
    review.add_argument("--reason", required=True)
    review.add_argument("--raw-response")
    review.add_argument(
        "--transport-classification",
        choices=["anthropic_credit_balance_too_low"],
    )
    review.set_defaults(func=command_review)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return args.func(args)
    except (ContractError, IntegrityError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"M050 EXTRACTION MACHINE: FAIL: {exc}") from exc


if __name__ == "__main__":
    raise SystemExit(main())
