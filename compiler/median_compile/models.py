"""Controlled vocabularies and validated models for the MEDIAN GDD compiler.

Vocabularies follow MEDIAN_GDD_Compiler_Python_Process_v1.0 Appendix B, extended
per MEDIAN_v0.5.0_Compiler_Naming_Scheme v0.3 (disposition replaces the
include_in_compile boolean; intended_target added as a non-binding Phase 10 hint).
"""

from __future__ import annotations

import re
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field, field_validator, model_validator

SOURCE_ID_RE = re.compile(r"^[A-Z]{3,4}_[A-Z0-9]{1,8}$")

#: Class prefix -> permitted source classes. Enforced so an ID cannot lie
#: about what kind of document it points at.
PREFIX_CLASS = {
    "BASE": "baseline",
    "SPEC": "detailed_spec",
    "PASS": "supplementary_pass",
    "PHIL": "philosophy",
    "RSCH": "research",
    "MANI": "manifestation",
    "APDX": "appendix",
    "LOG": "decision_log",
    "RULE": "human_ruling",
}


class SourceClass(str, Enum):
    baseline = "baseline"
    detailed_spec = "detailed_spec"
    supplementary_pass = "supplementary_pass"
    philosophy = "philosophy"
    research = "research"
    manifestation = "manifestation"
    appendix = "appendix"
    decision_log = "decision_log"
    human_ruling = "human_ruling"


class SourceStatus(str, Enum):
    active = "active"
    provisional = "provisional"
    review_required = "review_required"
    superseded = "superseded"
    archive = "archive"


class Disposition(str, Enum):
    compile = "compile"
    deferred = "deferred"
    superseded = "superseded"


class Target(str, Enum):
    body = "body"
    appendix = "appendix"
    tbd = "tbd"


class WordingFidelity(str, Enum):
    """How closely compiled prose may follow this source's phrasing."""

    exact = "EXACT"
    semantic = "SEMANTIC"
    editorial = "EDITORIAL"


class SourceEntry(BaseModel):
    """One row of the human-authored source registry (sources.yaml)."""

    model_config = {"extra": "forbid"}

    id: str
    path: str
    title: str
    version: str = "—"
    source_class: SourceClass
    status: SourceStatus
    disposition: Disposition
    intended_target: Target = Target.tbd
    wording_fidelity: WordingFidelity = WordingFidelity.semantic
    supersedes: str | None = None
    dependencies: list[str] = Field(default_factory=list)
    processing_order: int = 999
    pseudo_headings: bool = False
    notes: str = ""

    @field_validator("id")
    @classmethod
    def _id_shape(cls, v: str) -> str:
        if not SOURCE_ID_RE.match(v):
            raise ValueError(
                f"source id {v!r} must be CLASS_TOPIC, uppercase ASCII, "
                "topic <= 8 chars (naming scheme rules 6-7)"
            )
        return v

    @model_validator(mode="after")
    def _prefix_matches_class(self) -> SourceEntry:
        prefix = self.id.split("_", 1)[0]
        expected = PREFIX_CLASS.get(prefix)
        if expected is None:
            raise ValueError(f"unknown class prefix {prefix!r} in id {self.id!r}")
        if expected != self.source_class.value:
            raise ValueError(
                f"id {self.id!r} implies source_class {expected!r} "
                f"but declares {self.source_class.value!r}"
            )
        return self

    @model_validator(mode="after")
    def _superseded_not_compiled(self) -> SourceEntry:
        if self.status is SourceStatus.superseded and self.disposition is Disposition.compile:
            raise ValueError(
                f"{self.id}: superseded sources must not carry disposition 'compile' "
                "(naming scheme rule 4 - record IDs are minted only from compiled rows)"
            )
        return self


class ManifestRow(BaseModel):
    """A SourceEntry after hashing and path resolution. Written to manifest.csv."""

    model_config = {"extra": "forbid"}

    id: str
    path: str
    title: str
    version: str
    source_class: str
    status: str
    disposition: str
    intended_target: str
    wording_fidelity: str
    supersedes: str
    dependencies: str
    processing_order: int
    sha256: str
    bytes: int
    notes: str

    @classmethod
    def from_entry(cls, entry: SourceEntry, resolved: Path, sha256: str) -> ManifestRow:
        return cls(
            id=entry.id,
            path=entry.path,
            title=entry.title,
            version=entry.version,
            source_class=entry.source_class.value,
            status=entry.status.value,
            disposition=entry.disposition.value,
            intended_target=entry.intended_target.value,
            wording_fidelity=entry.wording_fidelity.value,
            supersedes=entry.supersedes or "",
            dependencies=";".join(entry.dependencies),
            processing_order=entry.processing_order,
            sha256=sha256,
            bytes=resolved.stat().st_size,
            notes=entry.notes,
        )


MANIFEST_COLUMNS = list(ManifestRow.model_fields.keys())
