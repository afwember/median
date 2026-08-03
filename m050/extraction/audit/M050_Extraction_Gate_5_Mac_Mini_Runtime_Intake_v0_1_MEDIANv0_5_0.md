# MEDIAN v0.5.0 Extraction — Gate 5 Mac Mini Runtime Intake

**Status:** Initial read-only intake
**Date:** 2026-08-02
**Host role:** Dedicated MEDIAN operating host
**External installations or upgrades:** None

## Result

The Mac Mini has sufficient local resources for Gate 5, but the default shell environment is not a suitable reproducible project runtime.

The recommended foundation is a repository-local `.venv` created from the native Apple-Silicon Anaconda CPython 3.12 interpreter. MEDIAN should not depend on the Apple system Python, the mutable global Anaconda package set, or the Codex app's bundled runtime.

## Observed host baseline

- Hardware architecture: `arm64`
- macOS: 26.4, build 25E246
- Git: `/usr/bin/git`
- Default shell `python3`: `/usr/bin/python3`
- Default Python: 3.9.6
- Default pip: 21.2.4
- Anaconda Python: `/opt/anaconda3/bin/python3.12`
- Anaconda Python version: 3.12.7
- Anaconda pip: 24.2
- Conda: 24.11.1
- Existing repository `.venv`: none
- `uv`: not installed

The Codex desktop runtime also provides an app-owned arm64 CPython 3.12.13 environment and document-processing libraries. Those resources are useful for rendering and inspection but are coupled to the Codex runtime bundle and should not define MEDIAN's compiler environment.

## Existing package observations

The Apple Python environment contains unrelated globally installed packages, including provider SDKs. Its observed versions include Anthropic 0.40.0 and OpenAI 2.43.0. Their presence is incidental and does not make that environment approved.

The base Anaconda environment includes JSON Schema, pytest, Pydantic, and Rich, but it does not contain the OpenAI or Anthropic SDKs. This is preferable as a bootstrap interpreter, but its global package set remains broader and more mutable than MEDIAN requires.

The archived abandoned compiler declared Python `>=3.10` with Typer, Pydantic, Rich, PyYAML, and optional Anthropic support. Those declarations are historical evidence only. Gate 5 will select dependencies from the new technical contract rather than inheriting that stack.

## Recommended environment policy

1. Require CPython `>=3.12,<3.13` on arm64 macOS for the initial supported host.
2. Create `.venv` from `/opt/anaconda3/bin/python3.12`.
3. Declare direct dependencies in a new project `pyproject.toml` and pin exact transitive versions in a reviewed lock file.
4. Keep the deterministic core small: standard library plus JSON Schema and YAML parsing where required.
5. Keep testing dependencies separate from runtime dependencies.
6. Keep each provider SDK in an optional extra and outside the offline-core import graph.
7. Make every test and offline command run without reading API credentials or importing provider clients.
8. Add an idempotent environment preflight and bootstrap procedure.
9. Never modify `/usr/bin/python3`, the base Conda environment, global pip packages, or shell startup files as part of MEDIAN setup.
10. Disclose and approve any network installation before it occurs.

## Remaining work

This intake records the available host resources; it does not create the virtual environment or choose final package versions. Those actions belong to Gate 5 implementation slice 1 after the technical contract is reviewed.
