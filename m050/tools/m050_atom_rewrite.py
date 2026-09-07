#!/usr/bin/env python3
"""Authorial rewrite interface for the canonical MEDIAN rewrite list.

The completed triage record selects the immutable input atoms. Rewrites are
saved atomically outside Git and promoted into one canonical record only at
source checkpoints. A submitted rewrite is authorially accepted expression;
it never mutates the accepted extraction evidence it replaces downstream.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from urllib.parse import parse_qs, urlparse
import uuid

try:
    from m050.tools.m050_atom_triage import (
        DEFAULT_DECISIONS as TRIAGE_DECISIONS,
        DecisionStore as TriageDecisionStore,
        TriageError,
        _display_source_text,
        _read_json,
        _read_jsonl,
        _sha256,
        _short_block,
        _web_host_allowed,
        load_corpus,
    )
except ModuleNotFoundError:  # Direct execution from m050/tools.
    from m050_atom_triage import (
        DEFAULT_DECISIONS as TRIAGE_DECISIONS,
        DecisionStore as TriageDecisionStore,
        TriageError,
        _display_source_text,
        _read_json,
        _read_jsonl,
        _sha256,
        _short_block,
        _web_host_allowed,
        load_corpus,
    )


STATE = Path("m050/extraction/control/M050_Compile_State_MEDIANv0_5_0.json")
DEFAULT_REWRITES = Path(
    "m050/reconciliation/rewrite/M050_Authorial_Rewrites_MEDIANv0_5_0.jsonl"
)
WORKING_REWRITES_NAME = "M050_Authorial_Rewrite_Working_MEDIANv0_5_0.jsonl"
SCHEMA_VERSION = "M050-AUTHORIAL-REWRITE-0.1"
REWRITE_EXCLUSION_REASON = "other_authorial_exclusion"


def _text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class RewriteCorpus:
    """The ordered subset selected by canonical rewrite-list decisions."""

    def __init__(self, repo_root: Path):
        self.full_corpus = load_corpus(repo_root)
        self.triage_path = repo_root / TRIAGE_DECISIONS
        triage = TriageDecisionStore(self.triage_path, self.full_corpus)
        if len(triage.decisions) != len(self.full_corpus.atoms):
            raise TriageError("authorial triage is not canonically complete")
        self.triage_sha256 = _sha256(self.triage_path)
        self.atoms = tuple(
            atom
            for atom in self.full_corpus.atoms
            if (decision := triage.decisions.get(atom.key, {})).get("decision") == "uncertain"
            and decision.get("review_route") == "rewrite_list"
        )
        if not self.atoms:
            raise TriageError("canonical triage contains no rewrite-list atoms")
        if any(
            decision.get("decision") == "uncertain"
            and decision.get("review_route") != "rewrite_list"
            for decision in triage.decisions.values()
        ):
            raise TriageError("canonical triage contains an unsupported uncertain route")
        self.by_key = {atom.key: atom for atom in self.atoms}
        self.source_labels = {
            atom.source_id: atom.source_label for atom in self.atoms
        }
        self.source_totals: dict[str, int] = {}
        for atom in self.atoms:
            self.source_totals[atom.source_id] = self.source_totals.get(atom.source_id, 0) + 1
        self.block_members: dict[str, tuple] = {}
        for atom in self.atoms:
            members = tuple(item for item in self.atoms if item.block_key == atom.block_key)
            self.block_members[atom.block_key] = members


class RewriteStore:
    """One current, authorially accepted rewrite per selected atom."""

    def __init__(self, path: Path, corpus: RewriteCorpus):
        self.path = path
        self.corpus = corpus
        self.rewrites: dict[str, dict] = {}
        self._order = {atom.key: index for index, atom in enumerate(corpus.atoms)}
        if path.exists():
            self._load()

    def _validate(self, record: dict) -> None:
        required = {
            "schema_version", "event_id", "atom_key", "atom_id", "source_id",
            "block_key", "candidate_sha256", "triage_decision_sha256",
            "original_claim_sha256", "replacement_claim", "rewritten_at",
            "authorially_accepted",
        }
        allowed = required | {"resolution", "exclusion_reason"}
        if not required.issubset(record) or not set(record).issubset(allowed):
            raise TriageError("authorial rewrite shape is invalid")
        atom = self.corpus.by_key.get(record.get("atom_key"))
        if atom is None:
            raise TriageError(f"rewrite references an unknown atom: {record.get('atom_key')}")
        if (
            record.get("schema_version") != SCHEMA_VERSION
            or record.get("atom_id") != atom.atom_id
            or record.get("source_id") != atom.source_id
            or record.get("block_key") != atom.block_key
            or record.get("candidate_sha256") != atom.candidate_sha256
            or record.get("triage_decision_sha256") != self.corpus.triage_sha256
            or record.get("original_claim_sha256") != _text_sha256(atom.normalized_claim)
            or record.get("authorially_accepted") is not True
        ):
            raise TriageError(f"authorial rewrite binding drifted: {atom.key}")
        resolution = record.get("resolution", "rewrite")
        replacement = record.get("replacement_claim")
        exclusion_reason = record.get("exclusion_reason")
        if resolution in {"accept", "rewrite"}:
            if exclusion_reason is not None:
                raise TriageError("an accepted claim cannot carry an exclusion reason")
            if not isinstance(replacement, str) or not replacement.strip():
                raise TriageError("accepted claim must be nonempty")
            if replacement != replacement.strip():
                raise TriageError("accepted claim must not have outer whitespace")
            if resolution == "rewrite" and replacement == atom.normalized_claim:
                raise TriageError("replacement claim must revise the original normalized claim")
            if resolution == "accept" and replacement != atom.normalized_claim:
                raise TriageError("unchanged acceptance must equal the original normalized claim")
        elif resolution == "exclude":
            if replacement is not None or exclusion_reason != REWRITE_EXCLUSION_REASON:
                raise TriageError("authorial rewrite exclusion is malformed")
        else:
            raise TriageError(f"invalid authorial rewrite resolution: {resolution}")

    def _load(self) -> None:
        for record in _read_jsonl(self.path):
            self._validate(record)
            key = record["atom_key"]
            if key in self.rewrites:
                raise TriageError(f"duplicate current rewrite for {key}")
            self.rewrites[key] = record

    def _write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary_name = tempfile.mkstemp(
            dir=self.path.parent, prefix=f".{self.path.name}."
        )
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                for key in sorted(self.rewrites, key=self._order.__getitem__):
                    handle.write(json.dumps(self.rewrites[key], ensure_ascii=False, sort_keys=True))
                    handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self.path)
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise

    def replace(self, rewrites: dict[str, dict]) -> None:
        replacement: dict[str, dict] = {}
        for key, record in rewrites.items():
            self._validate(record)
            if key != record["atom_key"] or key in replacement:
                raise TriageError("replacement rewrite records are inconsistent")
            replacement[key] = record
        self.rewrites = replacement
        self._write()

    def apply(self, atom_key: str, replacement_claim: str) -> None:
        atom = self.corpus.by_key.get(atom_key)
        if atom is None:
            raise TriageError("rewrite references an unknown atom")
        claim = replacement_claim.strip() if isinstance(replacement_claim, str) else ""
        record = {
            "schema_version": SCHEMA_VERSION,
            "event_id": f"rewrite_{uuid.uuid4().hex}",
            "atom_key": atom.key,
            "atom_id": atom.atom_id,
            "source_id": atom.source_id,
            "block_key": atom.block_key,
            "candidate_sha256": atom.candidate_sha256,
            "triage_decision_sha256": self.corpus.triage_sha256,
            "original_claim_sha256": _text_sha256(atom.normalized_claim),
            "resolution": "accept" if claim == atom.normalized_claim else "rewrite",
            "replacement_claim": claim,
            "rewritten_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
            "authorially_accepted": True,
        }
        self._validate(record)
        self.rewrites[atom.key] = record
        self._write()

    def exclude(self, atom_key: str) -> None:
        atom = self.corpus.by_key.get(atom_key)
        if atom is None:
            raise TriageError("exclusion references an unknown rewrite-list atom")
        record = {
            "schema_version": SCHEMA_VERSION,
            "event_id": f"rewrite_{uuid.uuid4().hex}",
            "atom_key": atom.key,
            "atom_id": atom.atom_id,
            "source_id": atom.source_id,
            "block_key": atom.block_key,
            "candidate_sha256": atom.candidate_sha256,
            "triage_decision_sha256": self.corpus.triage_sha256,
            "original_claim_sha256": _text_sha256(atom.normalized_claim),
            "resolution": "exclude",
            "replacement_claim": None,
            "exclusion_reason": REWRITE_EXCLUSION_REASON,
            "rewritten_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
            "authorially_accepted": True,
        }
        self._validate(record)
        self.rewrites[atom.key] = record
        self._write()

    def undo_latest(self, source_id: str) -> str | None:
        eligible = [
            record for record in self.rewrites.values() if record["source_id"] == source_id
        ]
        if not eligible:
            return None
        latest = max(eligible, key=lambda item: item["rewritten_at"])
        key = latest["atom_key"]
        self.rewrites.pop(key)
        self._write()
        return key

    def next_unwritten(self, source_id: str, *, after: int = -1) -> int | None:
        for index in range(after + 1, len(self.corpus.atoms)):
            atom = self.corpus.atoms[index]
            if atom.source_id == source_id and atom.key not in self.rewrites:
                return index
        return None

    def counts(self) -> dict[str, int]:
        rewritten = sum(
            record.get("resolution", "rewrite") == "rewrite"
            for record in self.rewrites.values()
        )
        accepted = sum(
            record.get("resolution", "rewrite") in {"accept", "rewrite"}
            for record in self.rewrites.values()
        )
        excluded = sum(
            record.get("resolution") == "exclude" for record in self.rewrites.values()
        )
        return {
            "rewritten": rewritten,
            "accepted": accepted,
            "excluded": excluded,
            "resolved": len(self.rewrites),
            "remaining": len(self.corpus.atoms) - len(self.rewrites),
            "total": len(self.corpus.atoms),
        }


def default_working_rewrites(repo_root: Path) -> Path:
    documents = next((parent for parent in repo_root.parents if parent.name == "Documents"), None)
    if documents is None:
        raise TriageError("cannot locate Documents/Codex/median-support from repository root")
    return documents / "Codex/median-support/rewrite-working" / WORKING_REWRITES_NAME


def prepare_working_store(canonical_path: Path, working_path: Path, corpus: RewriteCorpus) -> RewriteStore:
    canonical = RewriteStore(canonical_path, corpus)
    if not working_path.exists():
        working = RewriteStore(working_path, corpus)
        working.replace(canonical.rewrites)
        return working
    working = RewriteStore(working_path, corpus)
    for key, record in canonical.rewrites.items():
        if working.rewrites.get(key) != record:
            raise TriageError(f"working rewrite record does not preserve canonical checkpoint: {key}")
    return working


def _source_ids(corpus: RewriteCorpus) -> tuple[str, ...]:
    return tuple(corpus.source_labels)


def _source_complete(store: RewriteStore, source_id: str) -> bool:
    return all(
        atom.key in store.rewrites for atom in store.corpus.atoms if atom.source_id == source_id
    )


def _active_source(corpus: RewriteCorpus, canonical: RewriteStore) -> str | None:
    return next(
        (source_id for source_id in _source_ids(corpus) if not _source_complete(canonical, source_id)),
        None,
    )


def _lifecycle(corpus: RewriteCorpus, canonical: RewriteStore, working: RewriteStore) -> dict:
    for key, record in canonical.rewrites.items():
        if working.rewrites.get(key) != record:
            raise TriageError(f"working rewrite record does not preserve canonical checkpoint: {key}")
    source_id = _active_source(corpus, canonical)
    if source_id is None:
        return {"active_source_id": None, "checkpoint_required": False, "phase_complete": True}
    return {
        "active_source_id": source_id,
        "checkpoint_required": _source_complete(working, source_id),
        "phase_complete": False,
    }


def checkpoint_working(canonical_path: Path, working_path: Path, corpus: RewriteCorpus) -> dict:
    canonical = RewriteStore(canonical_path, corpus)
    working = prepare_working_store(canonical_path, working_path, corpus)
    source_id = _active_source(corpus, canonical)
    if source_id is None:
        raise TriageError("all rewrite sources are already checkpointed")
    if not _source_complete(working, source_id):
        raise TriageError(f"working rewrite source is not complete: {source_id}")
    order = _source_ids(corpus)
    active_index = order.index(source_id)
    forbidden = {
        record["source_id"] for record in working.rewrites.values()
        if order.index(record["source_id"]) > active_index
    }
    if forbidden:
        raise TriageError("working rewrites cross the required source checkpoint boundary: " + ", ".join(sorted(forbidden)))
    canonical.replace(working.rewrites)
    next_source = _active_source(corpus, canonical)
    return {
        "checkpointed_source_id": source_id,
        "canonical_dispositions": len(canonical.rewrites),
        "next_source_id": next_source,
        "phase_complete": next_source is None,
    }


def _canonical_published(repo_root: Path, canonical_path: Path) -> bool:
    try:
        result = subprocess.run(
            ["git", "show", f"origin/main:{DEFAULT_REWRITES.as_posix()}"],
            cwd=repo_root, check=True, capture_output=True,
        )
        return result.stdout == canonical_path.read_bytes()
    except (OSError, subprocess.CalledProcessError):
        return False


def _require_authority(repo_root: Path, corpus: RewriteCorpus) -> None:
    state = _read_json(repo_root / STATE)
    rewrite = state.get("rewrite", {})
    authority = state.get("authority", {})
    if (
        state.get("status") != "AUTHORIAL_REWRITE_ACTIVE"
        or state.get("execution_state") != "AUTHORIAL_REWRITE_ACTIVE"
        or rewrite.get("status") != "ACTIVE"
        or rewrite.get("rewrite_record") != DEFAULT_REWRITES.as_posix()
        or rewrite.get("rewrite_schema_version") != SCHEMA_VERSION
        or rewrite.get("input_atom_count") != len(corpus.atoms)
        or rewrite.get("input_triage_sha256") != corpus.triage_sha256
        or authority.get("repository_writes_authorized") is not False
        or authority.get("source_work_authorized") is not False
        or authority.get("triage_authorized") is not False
        or authority.get("rewrite_authorized") is not True
    ):
        raise TriageError("working rewrite authority is inactive or inconsistent")


def _atom_payload(corpus: RewriteCorpus, store: RewriteStore, index: int | None) -> dict:
    payload = {"stats": store.counts(), "atom": None}
    if index is None:
        return payload
    atom = corpus.atoms[index]
    full_siblings = corpus.full_corpus.block_members[atom.block_key]
    payload["atom"] = {
        "atom_key": atom.key,
        "atom_id": atom.atom_id,
        "source_id": atom.source_id,
        "source_label": atom.source_label,
        "section": atom.section,
        "rewrite_position": index + 1,
        "source_rewrite_position": sum(1 for item in corpus.atoms[: index + 1] if item.source_id == atom.source_id),
        "source_rewrite_total": corpus.source_totals[atom.source_id],
        "exact_source_text": _display_source_text(atom.exact_source_text),
        "normalized_claim": atom.normalized_claim,
        "source_text": _display_source_text(atom.source_text),
        "block_display": _short_block(atom.block_key),
        "siblings": [
            {
                "atom_key": sibling.key,
                "normalized_claim": sibling.normalized_claim,
                "current": sibling.key == atom.key,
                "on_rewrite_list": sibling.key in corpus.by_key,
            }
            for sibling in full_siblings
        ],
    }
    return payload


WEB_PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>MEDIAN Authorial Rewrite</title>
<style>
:root{color-scheme:dark;--bg:#11110f;--panel:#1d1d1a;--ink:#f2eee5;--muted:#aaa69c;--gold:#c9973b;--green:#4aa476;--red:#b95d57;--line:#393832}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:system-ui,-apple-system,sans-serif}.wrap{max-width:720px;margin:auto;padding:18px 16px 180px}h1{font-size:18px;letter-spacing:.12em;color:var(--gold)}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.stat,.card{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:16px}.stat{text-align:center;padding:14px 6px}.stat strong{display:block;font-size:20px}.label{font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);font-weight:700}.source{margin:14px 0}.source strong{display:block;margin-top:5px}.claim{font:700 25px/1.35 Georgia,serif}.normalized,.sourceText{white-space:pre-wrap;line-height:1.5}.siblings{font-size:14px;color:var(--muted)}textarea{width:100%;min-height:180px;margin-top:10px;padding:14px;border-radius:12px;border:1px solid #5b584f;background:#11110f;color:var(--ink);font:18px/1.45 system-ui;resize:vertical}.bar{position:fixed;left:0;right:0;bottom:0;background:#151512ee;border-top:1px solid var(--line);padding:12px max(16px,calc((100vw - 720px)/2));display:grid;grid-template-columns:1fr 1fr;gap:10px}button{min-height:54px;border:0;border-radius:15px;color:white;font-size:17px;font-weight:800;background:#292824}#save{background:var(--green)}#exclude{background:var(--red)}.complete{text-align:center;padding:40px 15px;color:var(--gold)}.toast{position:fixed;top:12px;left:50%;transform:translateX(-50%);background:#7b332f;color:white;padding:10px 15px;border-radius:12px;display:none;z-index:3}select{width:100%;padding:12px;border-radius:12px;background:var(--panel);color:var(--ink);border:1px solid var(--line)}
</style></head><body><div id="toast" class="toast"></div><main class="wrap"><h1>MEDIAN v0.5.0 — Authorial Rewrite</h1><select id="source"></select><div class="stats"><div class="stat"><strong id="position">—</strong><span class="label">Item</span></div><div class="stat"><strong id="done">—</strong><span class="label">Accepted</span></div><div class="stat"><strong id="excluded">—</strong><span class="label">Excluded</span></div><div class="stat"><strong id="remaining">—</strong><span class="label">Remaining</span></div></div><section id="content"></section></main><div class="bar"><button id="save">Accept claim</button><button id="exclude">Exclude</button><button id="skip">Skip</button><button id="undo">Undo</button></div>
<script>
const $=id=>document.getElementById(id);let ui={atom:null,sourceId:"",busy:false};
function toast(msg){$("toast").textContent=msg;$("toast").style.display="block";setTimeout(()=>$("toast").style.display="none",2600)}
async function api(path,body){const r=await fetch(path,{method:body?"POST":"GET",headers:body?{"Content-Type":"application/json"}:{},body:body?JSON.stringify(body):undefined,cache:"no-store"});const data=await r.json();if(!r.ok)throw new Error(data.error||"Request failed");return data}
function esc(v){return String(v??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}
function render(data){ui.atom=data.atom;$("done").textContent=data.stats.accepted;$("excluded").textContent=data.stats.excluded;$("remaining").textContent=data.stats.remaining;$("position").textContent=data.atom?`${data.atom.rewrite_position}/${data.stats.total}`:"—";if(data.checkpoint_required){$("content").innerHTML=`<div class="complete"><h2>Source checkpoint required</h2><p>${esc(data.completed_source_label)} is complete. The next source opens after its validated Git checkpoint.</p></div>`;return}if(data.phase_complete){$("content").innerHTML='<div class="complete"><h2>Rewrite list complete</h2><p>All authorial rewrite dispositions have been checkpointed.</p></div>';return}if(!data.atom){$("content").innerHTML='<div class="complete">No rewrite available.</div>';return}const a=data.atom;ui.sourceId=a.source_id;$("source").value=ui.sourceId;$("content").innerHTML=`<div class="card source"><span class="label">${esc(a.section)}</span><strong>${esc(a.source_label)}</strong><small>${a.source_rewrite_position}/${a.source_rewrite_total} in source</small></div><div class="card"><span class="label">Original atom</span><p class="claim">“${esc(a.exact_source_text)}”</p><hr><span class="label">Normalized claim</span><p class="normalized">${esc(a.normalized_claim)}</p></div><div class="card"><span class="label">Source text</span><p class="sourceText">${esc(a.source_text)}</p></div><div class="card"><label class="label" for="replacement">Authorially accepted claim</label><textarea id="replacement" autocomplete="off" spellcheck="true" placeholder="Edit only if needed."></textarea></div><div class="card siblings"><span class="label">Other atoms from this source block</span>${a.siblings.map(s=>`<p>${s.current?"CURRENT — ":s.on_rewrite_list?"REWRITE — ":""}${esc(s.normalized_claim)}</p>`).join("")}</div>`;$("replacement").value=a.normalized_claim}
async function load(){try{render(await api("/api/state"))}catch(e){toast(e.message)}}
async function post(path,extra={}){if(!ui.atom)return;try{render(await api(path,{source_id:ui.sourceId,atom_key:ui.atom.atom_key,...extra}))}catch(e){toast(e.message)}}
$("save").onclick=()=>post("/api/rewrite",{replacement_claim:$("replacement")?.value||""});$("exclude").onclick=()=>post("/api/exclude");$("skip").onclick=()=>post("/api/skip");$("undo").onclick=()=>post("/api/undo",{visible_atom_key:ui.atom?.atom_key});$("source").onchange=e=>{ui.sourceId=e.target.value;load()};
(async()=>{try{const d=await api("/api/sources");d.sources.forEach(s=>{const o=document.createElement("option");o.value=s.source_id;o.textContent=`${s.label} (${s.atoms})`;o.disabled=!s.available;$("source").append(o)});ui.sourceId=d.active_source_id||"";$("source").value=ui.sourceId;await load();setInterval(()=>{if(!ui.atom)load()},5000)}catch(e){toast(e.message)}})();
</script></body></html>"""


def create_web_server(corpus: RewriteCorpus, store: RewriteStore, *, canonical_path: Path | None = None, repo_root: Path | None = None, host: str = "127.0.0.1", port: int = 8766) -> HTTPServer:
    if host in {"0.0.0.0", "::"}:
        raise TriageError("wildcard web binding is prohibited; use the exact Tailscale address")
    if not _web_host_allowed(host):
        raise TriageError("web access requires loopback or an exact Tailscale address")
    index_by_key = {atom.key: index for index, atom in enumerate(corpus.atoms)}
    last_undo = {"signature": None}

    def lifecycle() -> dict:
        if canonical_path is None:
            first = _source_ids(corpus)[0]
            return {"active_source_id": first, "checkpoint_required": False, "phase_complete": False, "publication_pending": False}
        canonical = RewriteStore(canonical_path, corpus)
        value = _lifecycle(corpus, canonical, store)
        value["publication_pending"] = bool(repo_root and not _canonical_published(repo_root, canonical_path))
        return value

    def payload(source_id: str | None, index: int | None = None) -> dict:
        current = lifecycle()
        active = current["active_source_id"]
        if current["checkpoint_required"] or current["publication_pending"]:
            result = _atom_payload(corpus, store, None)
            result.update({"checkpoint_required": True, "phase_complete": False, "completed_source_label": corpus.source_labels.get(active, "Completed rewrite source")})
            return result
        if current["phase_complete"]:
            result = _atom_payload(corpus, store, None)
            result.update({"checkpoint_required": False, "phase_complete": True})
            return result
        if source_id not in (None, active):
            raise TriageError("source awaits its preceding checkpoint")
        source_id = active
        if index is None:
            index = store.next_unwritten(source_id)
        result = _atom_payload(corpus, store, index)
        result.update({"checkpoint_required": False, "phase_complete": False})
        return result

    class Handler(BaseHTTPRequestHandler):
        server_version = "MEDIANRewrite/0.1"
        def log_message(self, format: str, *args: object) -> None:
            sys.stderr.write(f"REWRITE WEB: {format % args}\n")
        def send_json(self, value: dict, status: int = 200) -> None:
            body = json.dumps(value, ensure_ascii=False).encode(); self.send_response(status); self.send_header("Content-Type", "application/json; charset=utf-8"); self.send_header("Cache-Control", "no-store"); self.send_header("X-Content-Type-Options", "nosniff"); self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
        def body(self) -> dict:
            try: length = int(self.headers.get("Content-Length", "0"))
            except ValueError as exc: raise TriageError("invalid request length") from exc
            if length <= 0 or length > 65536: raise TriageError("request body is empty or too large")
            try: value = json.loads(self.rfile.read(length))
            except json.JSONDecodeError as exc: raise TriageError("request body is not valid JSON") from exc
            if not isinstance(value, dict): raise TriageError("request body must be an object")
            return value
        def source(self, value: object) -> str | None:
            if value in (None, ""): return None
            if not isinstance(value, str) or value not in corpus.source_labels: raise TriageError("unknown source filter")
            return value
        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            try:
                if parsed.path == "/":
                    body = WEB_PAGE.encode(); self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Cache-Control", "no-store"); self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'"); self.send_header("X-Content-Type-Options", "nosniff"); self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body); return
                current = lifecycle()
                if parsed.path == "/api/state": self.send_json(payload(self.source((parse_qs(parsed.query).get("source_id") or [None])[0])))
                elif parsed.path == "/api/sources":
                    active = current["active_source_id"]
                    self.send_json({"active_source_id": active, "sources": [{"source_id": sid, "label": corpus.source_labels[sid], "atoms": corpus.source_totals[sid], "available": sid == active} for sid in _source_ids(corpus)]})
                else: self.send_json({"error": "not found"}, 404)
            except TriageError as exc: self.send_json({"error": str(exc)}, 400)
        def do_POST(self) -> None:
            origin = self.headers.get("Origin")
            if origin and urlparse(origin).netloc != self.headers.get("Host"): self.send_json({"error": "cross-origin write rejected"}, 403); return
            try:
                request = self.body(); source_id = self.source(request.get("source_id")); current = lifecycle(); active = current["active_source_id"]
                if current["checkpoint_required"] or current["publication_pending"] or current["phase_complete"]: raise TriageError("rewrites are held at a source checkpoint")
                if source_id not in (None, active): raise TriageError("source awaits its preceding checkpoint")
                source_id = active; atom = corpus.by_key.get(request.get("atom_key"))
                if atom is None or atom.source_id != source_id: raise TriageError("request atom is outside the active rewrite source")
                if self.path == "/api/rewrite":
                    store.apply(atom.key, request.get("replacement_claim")); last_undo["signature"] = None; self.send_json(payload(source_id))
                elif self.path == "/api/exclude":
                    store.exclude(atom.key); last_undo["signature"] = None; self.send_json(payload(source_id))
                elif self.path == "/api/skip":
                    next_index = store.next_unwritten(source_id, after=index_by_key[atom.key]);
                    if next_index is None: next_index = store.next_unwritten(source_id)
                    self.send_json(payload(source_id, next_index))
                elif self.path == "/api/undo":
                    signature = (source_id, request.get("visible_atom_key"))
                    if signature == last_undo["signature"]:
                        result = payload(source_id); result.update({"undone": 0, "duplicate": True}); self.send_json(result); return
                    key = store.undo_latest(source_id); last_undo["signature"] = signature
                    result = payload(source_id, index_by_key[key] if key else None); result.update({"undone": 1 if key else 0, "duplicate": False}); self.send_json(result)
                else: self.send_json({"error": "not found"}, 404)
            except TriageError as exc: self.send_json({"error": str(exc)}, 400)
    return HTTPServer((host, port), Handler)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--rewrites", type=Path)
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--serve", action="store_true")
    parser.add_argument("--checkpoint-working", action="store_true")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8766)
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve(); canonical_path = repo_root / DEFAULT_REWRITES
    working_path = (args.rewrites or default_working_rewrites(repo_root)).resolve()
    try:
        corpus = RewriteCorpus(repo_root)
        if args.checkpoint_working:
            print(json.dumps(checkpoint_working(canonical_path, working_path, corpus), indent=2)); return 0
        store = prepare_working_store(canonical_path, working_path, corpus)
        if args.stats: print(json.dumps(store.counts(), indent=2)); return 0
        if args.preview:
            canonical = RewriteStore(canonical_path, corpus); source = _active_source(corpus, canonical)
            index = store.next_unwritten(source) if source else None
            print(json.dumps(_atom_payload(corpus, store, index), indent=2, ensure_ascii=False)); return 0
        _require_authority(repo_root, corpus)
        if not args.serve: raise TriageError("use --serve, --stats, --preview, or --checkpoint-working")
        server = create_web_server(corpus, store, canonical_path=canonical_path, repo_root=repo_root, host=args.host, port=args.port)
        print(f"MEDIAN rewrite interface available at http://{server.server_address[0]}:{server.server_address[1]}/")
        try: server.serve_forever()
        except KeyboardInterrupt: pass
        finally: server.server_close()
        return 0
    except TriageError as exc:
        print(f"REWRITE ERROR: {exc}", file=sys.stderr); return 2


if __name__ == "__main__":
    raise SystemExit(main())
