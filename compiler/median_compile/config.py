"""Build configuration and path resolution."""

from __future__ import annotations

from pathlib import Path

import os
import re

import yaml
from pydantic import BaseModel

_ENV_REF = re.compile(r"\$\{([A-Z_][A-Z0-9_]*)\}")


def expand_env(value):
    """Expand ${VAR} references in loaded config.

    config.yaml ships `model: "${ANTHROPIC_EXTRACTION_MODEL}"` per the compiler
    spec's rule that model IDs are configuration, not code. Without expansion
    that literal string was passed to the API as a model name.
    """
    if isinstance(value, str):
        return _ENV_REF.sub(lambda m: os.environ.get(m.group(1), ""), value).strip()
    if isinstance(value, dict):
        return {k: expand_env(v) for k, v in value.items()}
    if isinstance(value, list):
        return [expand_env(v) for v in value]
    return value

DEFAULT_CONFIG = {
    "edition": "0.5",
    "versions": {
        "normalizer_full": "1.0",
        "lean_ruleset": "1.0",
        "chunker": "1.0",
        "extraction_prompt": "1.0",
        "record_schema": "1.0",
        "judgment_prompt": "1.0",
        "probe": "1.0",
    },
    "human_gates": {
        "conflict_rulings": True,
        "terminology": True,
        "architecture": True,
        "release": True,
    },
    "chunking": {
        "target_tokens": 10000,
        "max_tokens": 14000,
        "overlap_tokens": 400,
        "respect_headings": True,
        "seam_fraction": 0.9,
    },
}


class Versions(BaseModel):
    normalizer_full: str = "1.0"
    lean_ruleset: str = "1.0"
    chunker: str = "1.0"
    extraction_prompt: str = "1.0"
    record_schema: str = "1.0"
    judgment_prompt: str = "1.0"
    probe: str = "1.0"


class Config(BaseModel):
    model_config = {"extra": "allow"}

    edition: str = "0.5"
    providers: dict = {}
    versions: Versions = Versions()
    human_gates: dict = {}
    chunking: dict = {}


class Build:
    """Resolves every path in a build directory. Repo root is its grandparent."""

    def __init__(self, build_dir: str | Path) -> None:
        self.dir = Path(build_dir).resolve()
        self.repo = self.dir.parent.parent

    # -- inputs ------------------------------------------------------------
    @property
    def sources_yaml(self) -> Path:
        return self.dir / "sources.yaml"

    @property
    def config_yaml(self) -> Path:
        return self.dir / "config.yaml"

    # -- outputs -----------------------------------------------------------
    @property
    def manifest(self) -> Path:
        return self.dir / "manifest.csv"

    @property
    def raw(self) -> Path:
        return self.dir / "sources" / "raw"

    @property
    def full(self) -> Path:
        return self.dir / "sources" / "normalized_full"

    @property
    def lean(self) -> Path:
        return self.dir / "sources" / "normalized_lean"

    @property
    def reports(self) -> Path:
        return self.dir / "reports"

    @property
    def logs(self) -> Path:
        return self.dir / "logs"

    SUBDIRS = (
        "sources/raw",
        "sources/normalized_full",
        "sources/normalized_lean",
        "chunks",
        "records",
        "conflicts",
        "rulings",
        "architecture",
        "migration",
        "packets",
        "drafts",
        "audits",
        "reports/lean",
        "reports/probe",
        "logs",
        "release",
    )

    def init(self) -> list[Path]:
        made = []
        for sub in self.SUBDIRS:
            p = self.dir / sub
            if not p.exists():
                p.mkdir(parents=True)
                made.append(p)
        if not self.config_yaml.exists():
            self.config_yaml.write_text(
                yaml.safe_dump(DEFAULT_CONFIG, sort_keys=False), encoding="utf-8"
            )
            made.append(self.config_yaml)
        return made

    def load_config(self) -> Config:
        if not self.config_yaml.exists():
            return Config()
        raw = yaml.safe_load(self.config_yaml.read_text(encoding="utf-8")) or {}
        return Config.model_validate(expand_env(raw))

    def resolve(self, rel: str) -> Path:
        """Resolve a source path recorded relative to the repository root."""
        return (self.repo / rel).resolve()
