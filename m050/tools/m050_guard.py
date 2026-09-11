#!/usr/bin/env python3
"""Validate the current MEDIAN v0.5.0 compile without historical guard chains."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path
from typing import Iterable
from zoneinfo import ZoneInfo

try:
    from m050.tools.m050_atom_triage import (
        DEFAULT_DECISIONS as TRIAGE_DECISIONS,
        TriageError,
    )
except ModuleNotFoundError:  # Direct execution from m050/tools.
    from m050_atom_triage import (
        DEFAULT_DECISIONS as TRIAGE_DECISIONS,
        TriageError,
    )

try:
    from m050.tools.m050_msid_mapping import (
        DEFAULT_MAPPINGS,
        DEFAULT_VOCABULARY,
        SCHEMA_VERSION as MAPPING_SCHEMA_VERSION,
        VOCABULARY_SCHEMA_VERSION,
    )
except ModuleNotFoundError:
    from m050_msid_mapping import (
        DEFAULT_MAPPINGS,
        DEFAULT_VOCABULARY,
        SCHEMA_VERSION as MAPPING_SCHEMA_VERSION,
        VOCABULARY_SCHEMA_VERSION,
    )

try:
    from m050.tools.m050_reconciliation import (
        DEFAULT_RECONCILIATIONS,
        RECONCILIATION_LIFECYCLE,
        RUNS as RECONCILIATION_RUNS,
        SCHEMA_VERSION as RECONCILIATION_SCHEMA_VERSION,
        ReconciliationCorpus,
        ReconciliationStore,
        _ledger_events as reconciliation_ledger_events,
    )
except ModuleNotFoundError:
    from m050_reconciliation import (
        DEFAULT_RECONCILIATIONS,
        RECONCILIATION_LIFECYCLE,
        RUNS as RECONCILIATION_RUNS,
        SCHEMA_VERSION as RECONCILIATION_SCHEMA_VERSION,
        ReconciliationCorpus,
        ReconciliationStore,
        _ledger_events as reconciliation_ledger_events,
    )

try:
    from m050.tools.m050_atom_rewrite import (
        DEFAULT_REWRITES,
    )
except ModuleNotFoundError:  # Direct execution from m050/tools.
    from m050_atom_rewrite import (
        DEFAULT_REWRITES,
    )


ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json"
STATUS = ROOT / "STATUS.md"
AGENTS = ROOT / "AGENTS.md"
OVERRIDE = ROOT / "AGENTS.override.md"
FROZEN = ROOT / "m050/extraction/control/M050_Frozen_Corpus_Manifest_v0_1_MEDIANv0_5_0.json"
GATE_2 = ROOT / "m050/extraction/audit/M050_Extraction_Gate_2_Source_Disposition_v0_1_MEDIANv0_5_0.yaml"
MATRIX = ROOT / "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.json"
ORDER = ROOT / "m050/extraction/control/M050_Compile_Source_Processing_Order_v0_1_MEDIANv0_5_0.json"
HUMAN_EVIDENCE = ROOT / "m050/extraction/evidence/human-rulings"
STOPDOWN_NOTIFIER = ROOT / "m050/tools/m050_notify_supervisor.py"

LIVE_EXTRACTION_DIRS = {
    "accepted",
    "audit",
    "calibration",
    "control",
    "engine",
    "evidence",
    "runs",
}
CORPUS = {
    "registered_sources": 24,
    "atomic_compile_exclusions": 2,
    "compile_scope_sources": 22,
    "atomized_legacy_seed_sources": 4,
    "outstanding_compile_scope_sources": 18,
    "outstanding_pre_reconciliation_sources": 14,
    "outstanding_later_or_conditional_sources": 4,
}
IGNORED_NAMES = {".DS_Store"}
IGNORED_RUNTIME_DIRS = {"__pycache__", ".pytest_cache", "build", "median_gate5.egg-info"}
RETIRED_PATTERNS = (
    "m050/extraction/control/M050_Active_Control_Index_v0_*_MEDIANv0_5_0.json",
    "m050/extraction/control/M050_Current_State_Checkpoint_v0_*_MEDIANv0_5_0.json",
    "m050/extraction/control/M050_Current_State_Checkpoint_v0_*_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_New_Task_Bootstrap_v0_*_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Compile_Execution_Standard_v0_*_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Repository_Write_Authority_and_Freeze_Policy_v0_1_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Compile_Source_State_Matrix_v0_1_MEDIANv0_5_0.md",
    "m050/extraction/control/M050_Source_Atomization_Pilot_Calibration_Protocol_v0_*_MEDIANv0_5_0.md",
    "m050/tools/m050_guard_v0_*.py",
    "m050/extraction/audit/M050_*_Active_Lifecycle_Receipt_MEDIANv0_5_0.json",
    "m050/extraction/audit/spend-envelopes/*",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read JSON {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root is not an object: {path.relative_to(ROOT)}")
        return {}
    return value


def relative_files(roots: Iterable[str]) -> set[str]:
    found: set[str] = set()
    for root_text in roots:
        source_root = ROOT / root_text
        if not source_root.is_dir():
            continue
        for item in source_root.rglob("*"):
            if item.is_file() and item.name not in IGNORED_NAMES:
                found.add(item.relative_to(ROOT).as_posix())
    return found


def is_live_file(path: Path) -> bool:
    return path.name not in IGNORED_NAMES and not (set(path.parts) & IGNORED_RUNTIME_DIRS)


def gate2_registered_sources() -> dict[str, tuple[str, str]]:
    records: dict[str, tuple[str, str]] = {}
    current: dict[str, str] = {}
    in_sources = False
    for raw_line in GATE_2.read_text(encoding="utf-8").splitlines():
        if raw_line == "sources:":
            in_sources = True
            continue
        if in_sources and raw_line and not raw_line.startswith(" "):
            break
        if not in_sources:
            continue
        stripped = raw_line.strip()
        if stripped.startswith("- source_id: "):
            if {"source_id", "path", "sha256"} <= current.keys():
                records[current["source_id"]] = (current["path"], current["sha256"])
            current = {"source_id": stripped.split(": ", 1)[1]}
        elif stripped.startswith("path: "):
            current["path"] = stripped.split(": ", 1)[1]
        elif stripped.startswith("sha256: "):
            current["sha256"] = stripped.split(": ", 1)[1]
    if {"source_id", "path", "sha256"} <= current.keys():
        records[current["source_id"]] = (current["path"], current["sha256"])
    return records


def validate_frozen_corpus(errors: list[str]) -> tuple[int, int]:
    manifest = read_json(FROZEN, errors)
    frozen_files = manifest.get("frozen_files", [])
    expected = {item.get("path"): item.get("sha256") for item in frozen_files}
    registered = {
        item.get("source_id"): (item.get("path"), item.get("sha256"))
        for item in frozen_files
        if item.get("kind") == "registered_source"
    }
    if gate2_registered_sources() != registered:
        errors.append("Gate 2 source disposition disagrees with the frozen manifest")
    actual = relative_files(manifest.get("source_roots", []))
    for relative in sorted(set(expected) - actual):
        errors.append(f"missing frozen source: {relative}")
    for relative in sorted(actual - set(expected)):
        errors.append(f"unregistered file in frozen source root: {relative}")
    for relative, expected_hash in expected.items():
        target = ROOT / str(relative)
        if target.is_file() and sha256_file(target) != expected_hash:
            errors.append(f"frozen source hash mismatch: {relative}")

    immutable = manifest.get("immutable_accepted_files", [])
    for binding in immutable:
        target = ROOT / binding.get("path", "")
        if not target.is_file() or sha256_file(target) != binding.get("sha256"):
            errors.append(f"immutable accepted artifact drifted: {binding.get('path')}")

    return len(expected), len(immutable)


def validate_live_topology(errors: list[str]) -> None:
    extraction = ROOT / "m050/extraction"
    active_dirs = {
        item.relative_to(extraction).parts[0]
        for item in extraction.rglob("*")
        if item.is_file() and is_live_file(item)
    }
    if active_dirs != LIVE_EXTRACTION_DIRS:
        errors.append(
            "live extraction topology drifted: "
            f"expected {sorted(LIVE_EXTRACTION_DIRS)}, found {sorted(active_dirs)}"
        )
    for item in extraction.rglob("*.md"):
        if not item.is_file() or not is_live_file(item):
            continue
        relative = item.relative_to(extraction)
        allowed = (
            relative.as_posix() in {
                "engine/README.md",
                "control/source-identities/README.md",
            }
            or relative.parts[:1] == ("calibration",)
            or relative.parts[:3] == ("control", "source-identities", "cards")
            or (relative.parts[:1] == ("evidence",) and "source" in relative.parts)
        )
        if not allowed:
            errors.append(f"unclassified process-facing Markdown: {item.relative_to(ROOT)}")
    if (ROOT / "m050/archive").exists():
        errors.append("retired m050/archive directory has returned")


def validate_human_evidence(errors: list[str]) -> None:
    reconstruction = HUMAN_EVIDENCE / "reconstruction"
    report_path = reconstruction / "M050_Human_Rulings_Reconstruction_Report_v0_1_MEDIANv0_5_0.json"
    report = read_json(report_path, errors)
    expected = {
        "coordinate_ledger": reconstruction / "M050_Human_Rulings_Legacy_Atom_Coordinate_Ledger_v0_1_MEDIANv0_5_0.jsonl",
        "reference_rewrite_map": reconstruction / "M050_Human_Rulings_Active_to_Legacy_Reference_Rewrite_Map_v0_1_MEDIANv0_5_0.json",
        "registry": reconstruction / "M050_Human_Rulings_Section_and_Field_Registry_v0_1_MEDIANv0_5_0.json",
    }
    if (
        report.get("passed") is not True
        or report.get("legacy_record_count") != 173
        or report.get("ruling_count") != 41
        or report.get("complete_ruling_coverage") is not True
    ):
        errors.append("Human Rulings reconstruction boundary drifted")
    for name, target in expected.items():
        binding = report.get(name, {})
        if (
            binding.get("path") != target.relative_to(ROOT).as_posix()
            or not target.is_file()
            or binding.get("sha256") != sha256_file(target)
        ):
            errors.append(f"Human Rulings reconstruction binding drifted: {name}")


def validate_source_registry(errors: list[str]) -> None:
    matrix = read_json(MATRIX, errors)
    order = read_json(ORDER, errors)
    if matrix.get("summary") != CORPUS or len(matrix.get("sources", [])) != 24:
        errors.append("source matrix corpus vector drifted")
    sequence = order.get("sequence", [])
    matrix_by_id = {item.get("source_id"): item for item in matrix.get("sources", [])}
    if [item.get("order") for item in sequence] != list(range(1, 25)):
        errors.append("processing order ordinals drifted")
    if len({item.get("source_id") for item in sequence}) != 24 or set(matrix_by_id) != {
        item.get("source_id") for item in sequence
    }:
        errors.append("processing order source coverage drifted")
    allowed_keys = {"order", "source_id", "label", "pre_candidate_acceptance_control"}
    for item in sequence:
        if not set(item) <= allowed_keys:
            errors.append(f"processing order duplicates source state: {item.get('source_id')}")
        if not item.get("label"):
            errors.append(f"processing order label is absent: {item.get('source_id')}")


def expected_status(state: dict) -> str:
    dashboard = state.get("dashboard", {})
    progress_label = "PROGRESS" if "progress" in dashboard else "CHUNK"
    progress_value = dashboard.get("progress", dashboard.get("chunk", ""))
    try:
        remaining_display = Decimal(
            state.get("spend", {}).get("remaining_usd", "")
        ).quantize(
            Decimal("0.01"), rounding=ROUND_FLOOR
        )
    except Exception:
        remaining_display = ""
    return (
        "# MEDIAN COMPILE — v0.5.0\n\n"
        f"{dashboard.get('updated_human', '')}<br>\n\n"
        "<!-- Derived dashboard only; M050_Compile_State_MEDIANv0_5_0.json is authoritative. -->\n\n"
        f"**STATUS:** {dashboard.get('status', '')}<br>\n"
        f"**PHASE:** {dashboard.get('phase', '')}<br>\n"
        f"**SOURCE:** {dashboard.get('source', '')}<br>\n"
        f"**{progress_label}:** {progress_value}<br>\n"
        f"**NOW:** {dashboard.get('now', '')}<br>\n"
        f"**NEXT:** {dashboard.get('next', '')}<br>\n"
        f"**{'PROVIDER SPEND (INACTIVE)' if state.get('spend', {}).get('active') is False else 'SPEND REMAINING'}:** ${remaining_display}\n"
    )


def validate_timestamp(state: dict, errors: list[str]) -> None:
    try:
        exact = datetime.fromisoformat(state.get("updated", ""))
    except ValueError:
        errors.append("canonical state timestamp is not ISO-8601 to the second")
        return
    if exact.microsecond:
        errors.append("canonical state timestamp is not rounded to the nearest second")
    eastern = exact.astimezone(ZoneInfo("America/New_York"))
    expected = (
        f"{eastern.strftime('%B')} {eastern.day}, {eastern.year} at "
        f"{eastern.strftime('%I').lstrip('0')}:{eastern.strftime('%M:%S %p %Z')}"
    )
    if state.get("dashboard", {}).get("updated_human") != expected:
        errors.append("human STATUS timestamp disagrees with canonical ISO timestamp")


def validate_spend_and_status(
    state: dict,
    errors: list[str],
    *,
    active_required: bool = True,
) -> None:
    state_spend = state.get("spend", {})
    if "record" in state_spend:
        errors.append("canonical spend points to a redundant successor spend file")
    try:
        refresh_window = Decimal(state_spend.get("refresh_window_usd", ""))
        authorized = Decimal(state_spend.get("authorized_usd", ""))
        cumulative = Decimal(state_spend.get("cumulative_spent_usd", ""))
        remaining = Decimal(state_spend.get("remaining_usd", ""))
        rounded = cumulative.quantize(Decimal("0.01"), rounding=ROUND_CEILING)
    except Exception:
        errors.append("canonical cumulative budget is not decimal")
    else:
        if state_spend.get("active") is not active_required:
            errors.append("canonical cumulative budget activity disagrees with the active phase")
        if (
            refresh_window <= 0
            or cumulative < 0
            or authorized < 0
            or remaining < 0
            or authorized - cumulative != remaining
            or remaining > refresh_window
        ):
            errors.append("canonical cumulative budget arithmetic is inconsistent")
        if state_spend.get("display_usd_rounded_up") != f"{rounded:.2f}":
            errors.append("dashboard cost is not rounded upward to the cent")

    validate_timestamp(state, errors)
    if STATUS.read_text(encoding="utf-8") != expected_status(state):
        errors.append("STATUS does not exactly mirror canonical compile state")


def validate_reconciliation_profile(errors: list[str]) -> None:
    state = read_json(STATE, errors)
    status = state.get("status")
    lifecycle = RECONCILIATION_LIFECYCLE.get(status)
    if lifecycle is None or state.get("execution_state") != status:
        errors.append("canonical Stage 5 lifecycle state is invalid")
        reconciliation_status, dashboard_status, active = None, None, False
    else:
        reconciliation_status, dashboard_status, active = lifecycle
    try:
        corpus = ReconciliationCorpus(ROOT)
        store = ReconciliationStore(ROOT / DEFAULT_RECONCILIATIONS, corpus)
    except TriageError as exc:
        errors.append(f"canonical Stage 5 machinery is invalid: {exc}")
        return

    if state.get("mapping", {}).get("status") != "COMPLETE":
        errors.append("Stage 5 requires completed Stage 4 mapping")
    expected_mapping = {
        "status": "COMPLETE",
        "input_scope": "triage-retained claims plus authorially accepted rewrite outcomes",
        "input_triage_record": TRIAGE_DECISIONS.as_posix(),
        "input_triage_sha256": corpus.triage_sha256,
        "input_rewrite_record": DEFAULT_REWRITES.as_posix(),
        "input_rewrite_sha256": corpus.rewrite_sha256,
        "vocabulary_record": DEFAULT_VOCABULARY.as_posix(),
        "vocabulary_sha256": corpus.vocabulary_sha256,
        "vocabulary_schema_version": VOCABULARY_SCHEMA_VERSION,
        "mapping_record": DEFAULT_MAPPINGS.as_posix(),
        "mapping_schema_version": MAPPING_SCHEMA_VERSION,
        "input_atom_count": 5382,
        "input_source_count": 18,
    }
    if state.get("mapping") != expected_mapping:
        errors.append("completed Stage 4 mapping binding drifted")

    reconciliation = state.get("reconciliation", {})
    required_reconciliation_keys = {
        "status", "input_scope", "input_mapping_record", "input_mapping_sha256",
        "input_vocabulary_record", "input_vocabulary_sha256", "input_triage_sha256",
        "input_rewrite_sha256", "reconciliation_record",
        "reconciliation_schema_version", "input_atom_count", "input_source_count",
        "target", "completed_tranche_ids", "provider",
    }
    if set(reconciliation) != required_reconciliation_keys:
        errors.append("canonical Stage 5 binding shape drifted")
    expected_bindings = {
        "status": reconciliation_status,
        "input_scope": "all 5,382 Stage 4 eligible atoms as one unitary corpus",
        "input_mapping_record": DEFAULT_MAPPINGS.as_posix(),
        "input_mapping_sha256": corpus.mapping_sha256,
        "input_vocabulary_record": DEFAULT_VOCABULARY.as_posix(),
        "input_vocabulary_sha256": corpus.vocabulary_sha256,
        "input_triage_sha256": corpus.triage_sha256,
        "input_rewrite_sha256": corpus.rewrite_sha256,
        "reconciliation_record": DEFAULT_RECONCILIATIONS.as_posix(),
        "reconciliation_schema_version": RECONCILIATION_SCHEMA_VERSION,
        "input_atom_count": 5382,
        "input_source_count": 18,
    }
    for key, value in expected_bindings.items():
        if reconciliation.get(key) != value:
            errors.append(f"canonical Stage 5 binding drifted: {key}")
    target = reconciliation.get("target")
    if not isinstance(target, dict) or set(target) != {"tranche_id", "msid_prefix", "selector"}:
        errors.append("canonical Stage 5 target shape drifted")
    elif (
        not isinstance(target.get("tranche_id"), str)
        or not target["tranche_id"]
        or not isinstance(target.get("msid_prefix"), str)
        or target.get("selector") not in {"exact", "subtree"}
    ):
        errors.append("canonical Stage 5 target is invalid")
    completed = reconciliation.get("completed_tranche_ids")
    if (
        not isinstance(completed, list)
        or len(completed) != len(set(completed))
        or any(not isinstance(item, str) or not item for item in completed)
    ):
        errors.append("canonical Stage 5 completed-tranche boundary is invalid")

    provider = reconciliation.get("provider")
    required_provider_keys = {
        "enabled", "name", "model", "reasoning_effort", "cache_ttl",
        "maximum_output_tokens", "pricing", "proposal_review_required",
    }
    provider_enabled = isinstance(provider, dict) and provider.get("enabled") is True
    if not isinstance(provider, dict) or set(provider) != required_provider_keys:
        errors.append("canonical Stage 5 provider configuration shape drifted")
    elif provider_enabled:
        output_limits = provider.get("maximum_output_tokens")
        pricing = provider.get("pricing")
        required_pricing = {
            "input_usd_per_million_tokens", "output_usd_per_million_tokens",
            "cache_read_multiplier", "cache_5m_write_multiplier",
            "cache_1h_write_multiplier",
        }
        expected_pricing = {
            "input_usd_per_million_tokens": "3",
            "output_usd_per_million_tokens": "15",
            "cache_read_multiplier": "0.1",
            "cache_5m_write_multiplier": "1.25",
            "cache_1h_write_multiplier": "2",
        }
        if (
            provider.get("name") != "Anthropic"
            or provider.get("model") != "claude-sonnet-5"
            or provider.get("reasoning_effort") != "high"
            or provider.get("cache_ttl") != "1h"
            or not isinstance(output_limits, dict)
            or set(output_limits) != {"proposal", "review"}
            or any(not isinstance(value, int) or value < 1 for value in output_limits.values())
            or not isinstance(pricing, dict)
            or set(pricing) != required_pricing
            or pricing != expected_pricing
            or provider.get("proposal_review_required") is not True
        ):
            errors.append("enabled Stage 5 provider configuration is invalid")
        else:
            try:
                rates = [Decimal(pricing[key]) for key in required_pricing]
                invalid_rate = any(
                    not value.is_finite() or value <= 0 for value in rates
                )
            except Exception:
                errors.append("enabled Stage 5 provider pricing is invalid")
            else:
                if invalid_rate:
                    errors.append("enabled Stage 5 provider pricing is invalid")
    elif (
        provider.get("name") != "Anthropic"
        or provider.get("model") is not None
        or provider.get("maximum_output_tokens") is not None
        or provider.get("pricing") is not None
        or provider.get("proposal_review_required") is not True
    ):
        errors.append("disabled Stage 5 provider configuration carries call capability")

    authority = state.get("authority", {})
    prohibited = {
        "source_work_authorized", "triage_authorized", "rewrite_authorized",
        "google_sheets_interaction_authorized", "mapping_authorized",
        "compiled_prose_authorized",
    }
    if any(authority.get(key) is not False for key in prohibited):
        errors.append("canonical Stage 5 retains prohibited authority")
    if (
        authority.get("reconciliation_authorized") is not active
        or authority.get("semantic_acceptance_authorized") is not active
        or authority.get("repository_writes_authorized") is not active
        or authority.get("provider_calls_authorized") is not (active and provider_enabled)
    ):
        errors.append("canonical Stage 5 authority disagrees with lifecycle")
    if state.get("spend", {}).get("active") is not (active and provider_enabled):
        errors.append("canonical Stage 5 spend disagrees with call authority")
    if state.get("dashboard", {}).get("status") != dashboard_status:
        errors.append("canonical Stage 5 dashboard status disagrees with lifecycle")
    expected_progress = (
        f"{len(store.primary_members):,} / {len(corpus.atoms):,} atoms assigned to canonical semantic units"
    )
    if state.get("dashboard", {}).get("progress") != expected_progress:
        errors.append("Stage 5 dashboard progress is stale")
    unit_ids = {unit["unit_id"] for unit in store.units}
    run_root = ROOT / RECONCILIATION_RUNS
    packet_hashes: set[str] = set()
    response_hashes: set[str] = set()
    for path in run_root.rglob("*.json") if run_root.exists() else ():
        try:
            response_hashes.add(sha256_file(path))
            value = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(value, dict) and isinstance(value.get("packet_sha256"), str):
                packet_hashes.add(value["packet_sha256"])
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid Stage 5 run evidence {path.relative_to(ROOT)}: {exc}")
    for ledger in run_root.rglob("run_ledger.jsonl") if run_root.exists() else ():
        try:
            events = reconciliation_ledger_events(ledger)
        except TriageError as exc:
            errors.append(f"invalid Stage 5 run ledger {ledger.relative_to(ROOT)}: {exc}")
            continue
        for event in events:
            if event.get("result") == "token_count_failure":
                continue
            relative = event.get("token_count")
            claimed = event.get("token_count_sha256")
            if not isinstance(relative, str) or not isinstance(claimed, str):
                errors.append(f"Stage 5 run event lacks token-count evidence: {ledger.relative_to(ROOT)}")
                continue
            evidence_path = ROOT / relative
            if not evidence_path.is_file() or sha256_file(evidence_path) != claimed:
                errors.append(f"Stage 5 token-count evidence drifted: {relative}")
    for unit in store.units:
        if not set(unit["related_unit_ids"]) <= unit_ids - {unit["unit_id"]}:
            errors.append(f"Stage 5 unit has an unresolved related-unit link: {unit['unit_id']}")
        if unit["decision_origin"] == "provider_reviewed":
            evidence = unit["evidence"]
            if evidence["packet_sha256"] not in packet_hashes:
                errors.append(f"Stage 5 unit lacks its preserved packet: {unit['unit_id']}")
            for key in ("proposal_response_sha256", "review_response_sha256"):
                if evidence[key] not in response_hashes:
                    errors.append(f"Stage 5 unit lacks preserved response evidence: {unit['unit_id']}")
    validate_spend_and_status(state, errors, active_required=active and provider_enabled)


def validate_active_phase(errors: list[str]) -> None:
    """Single replaceable phase-specific validation seam."""
    state = read_json(STATE, errors)
    phase = state.get("dashboard", {}).get("phase", "")
    validate_human_evidence(errors)
    if phase.startswith("Semantic reconciliation"):
        validate_reconciliation_profile(errors)
    else:
        errors.append("canonical state does not name a supported active phase profile")


def validate_operating_contract(errors: list[str]) -> None:
    if OVERRIDE.exists() or OVERRIDE.is_symlink():
        errors.append("AGENTS.override.md exists")
    text = AGENTS.read_text(encoding="utf-8")
    for heading in (
        "## Conservation of System",
        "## Task roles and phase handoff",
        "## Phase model",
        "## Canonical controls",
        "## Authority model",
        "## Active phase profile — Stage 5 semantic reconciliation",
        "## STATUS contract",
    ):
        if heading not in text:
            errors.append(f"AGENTS omits required structural section: {heading}")
    if len(text.encode("utf-8")) > 32 * 1024:
        errors.append("AGENTS exceeds the 32 KiB root-instruction discovery limit")
    notifier_path = STOPDOWN_NOTIFIER.relative_to(ROOT).as_posix()
    if notifier_path not in text:
        errors.append("AGENTS omits the sole Stopdown notifier")
    if not STOPDOWN_NOTIFIER.is_file():
        errors.append("sole Stopdown notifier is missing")
    for retired_task_tool in (
        "codex_app__list_threads",
        "codex_app__send_message_to_thread",
    ):
        if retired_task_tool in text:
            errors.append(
                f"AGENTS retains retired Stopdown task tool: {retired_task_tool}"
            )
    for pattern in RETIRED_PATTERNS:
        for target in ROOT.glob(pattern):
            errors.append(f"retired supervisory file remains active: {target.relative_to(ROOT)}")


def validate_json_integrity(errors: list[str]) -> tuple[int, int]:
    json_count = 0
    jsonl_count = 0
    for root in (ROOT / "m050/extraction", ROOT / "m050/reconciliation"):
        for target in root.rglob("*.json"):
            if not is_live_file(target):
                continue
            try:
                json.loads(target.read_text(encoding="utf-8"))
                json_count += 1
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"invalid JSON {target.relative_to(ROOT)}: {exc}")
        for target in root.rglob("*.jsonl"):
            if not is_live_file(target):
                continue
            try:
                for line in target.read_text(encoding="utf-8").splitlines():
                    if line.strip():
                        json.loads(line)
                jsonl_count += 1
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"invalid JSONL {target.relative_to(ROOT)}: {exc}")
    return json_count, jsonl_count


def validate_work_order(path: Path | None, errors: list[str]) -> None:
    if path is None:
        return
    data = read_json(path.resolve(), errors)
    candidates: list[str] = []
    for key in ("source_path", "path", "input_path"):
        if isinstance(data.get(key), str):
            candidates.append(data[key])
    if isinstance(data.get("input_paths"), list):
        candidates.extend(item for item in data["input_paths"] if isinstance(item, str))
    contaminated = [item for item in candidates if item == "m051" or item.startswith("m051/")]
    if contaminated:
        errors.append("work order contains prohibited m051 input")


def run_tests() -> int:
    # The release guard follows the replaceable active phase. The complete
    # cross-phase regression suite remains available through ordinary pytest.
    return subprocess.run(
        [
            str(ROOT / ".venv/bin/python"),
            "-m",
            "pytest",
            "m050/tools/tests/test_m050_stage5_guard.py",
            "m050/tools/tests/test_m050_reconciliation.py",
            "m050/tools/tests/test_m050_render_status.py",
            "-q",
        ],
        cwd=ROOT,
        check=False,
    ).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-order", type=Path)
    parser.add_argument("--with-tests", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    frozen_count, immutable_count = validate_frozen_corpus(errors)
    validate_live_topology(errors)
    validate_source_registry(errors)
    validate_operating_contract(errors)
    validate_active_phase(errors)
    json_count, jsonl_count = validate_json_integrity(errors)
    validate_work_order(args.work_order, errors)
    if args.with_tests and run_tests():
        errors.append("offline regression suite failed")

    if errors:
        print("M050 COMPILE GUARD: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("M050 COMPILE GUARD: PASS")
    state = read_json(STATE, [])
    spend = state.get("spend", {})
    corpus = state.get("corpus", {})
    print(
        "- corpus: "
        f"{corpus.get('registered_sources')} / {corpus.get('compile_scope_sources')} / "
        f"{corpus.get('atomized_legacy_seed_sources')} / "
        f"{corpus.get('outstanding_compile_scope_sources')} = "
        f"{corpus.get('outstanding_pre_reconciliation_sources')} + "
        f"{corpus.get('outstanding_later_or_conditional_sources')}"
    )
    print(f"- frozen files: {frozen_count}; immutable accepted artifacts: {immutable_count}")
    print("- live extraction topology: 7 directories; retired process families absent")
    print("- Human Rulings evidence: 173 reconstructed records across 41 rulings")
    if str(state.get("status", "")).startswith("RECONCILIATION_"):
        reconciliation_corpus = ReconciliationCorpus(ROOT)
        reconciliation_store = ReconciliationStore(
            ROOT / DEFAULT_RECONCILIATIONS, reconciliation_corpus
        )
        target = state.get("reconciliation", {}).get("target", {})
        print(
            f"- active reconciliation boundary: {target.get('msid_prefix')} "
            f"({target.get('tranche_id')}); {len(reconciliation_store.primary_members)} / "
            f"{len(reconciliation_corpus.atoms)} atoms assigned"
        )
    print(
        f"- spend: ${spend.get('cumulative_spent_usd')} exact; "
        f"${spend.get('remaining_usd')} remaining; "
        f"${spend.get('display_usd_rounded_up')} display"
    )
    print(f"- JSON integrity: {json_count} JSON files and {jsonl_count} JSONL files")
    if args.with_tests:
        print("- offline regression suite: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
