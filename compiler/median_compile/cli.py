"""median-compile — command line interface.

Each phase is a separate, independently rerunnable command. There is
deliberately no "run everything" action.
"""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path
from typing import Optional

from typing_extensions import Annotated

import typer
from rich.console import Console
from rich.table import Table

from . import chunk as ck
from . import lean as ln
from . import manifest as mf
from . import normalize as nz
from . import probe as pb
from . import extract as ex
from . import record as rec
from . import records as rc
from .config import Build
from .models import Disposition

app = typer.Typer(
    add_completion=False,
    help="Phase-gated compiler for the MEDIAN GDD.",
    no_args_is_help=True,
)
console = Console()

BuildArg = Annotated[Path, typer.Argument(help="Build directory, e.g. build/v0.5")]


def _load(build_dir: Path) -> tuple[Build, list]:
    build = Build(build_dir)
    return build, mf.load_entries(build)


def _sha(path: Path) -> str:
    import hashlib

    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _report_validation(v: mf.Validation) -> None:
    for w in v.warnings:
        console.print(f"[yellow]warn[/yellow]  {w}")
    for e in v.errors:
        console.print(f"[red]error[/red] {e}")


@app.command()
def init(build_dir: BuildArg) -> None:
    """Create the build directory skeleton and default config."""
    build = Build(build_dir)
    made = build.init()
    for p in made:
        console.print(f"[green]created[/green] {p.relative_to(build.repo)}")
    if not made:
        console.print("[dim]already initialised[/dim]")
    if not build.sources_yaml.exists():
        console.print(f"[yellow]next[/yellow] author {build.sources_yaml.name}")


@app.command()
def manifest(
    build_dir: BuildArg,
    check: Annotated[bool, typer.Option(help="Validate without writing.")] = False,
) -> None:
    """Phase 0 — hash, validate, and write manifest.csv."""
    build, entries = _load(build_dir)
    cfg = build.load_config()
    with rec.record(build, "manifest", "manifest", {"naming_scheme": "0.3"}) as run:
        v = mf.validate(entries, build)
        _report_validation(v)
        if not v.ok:
            run.status = "error"
            run.notes = f"{len(v.errors)} validation error(s)"
            console.print(f"\n[red]{len(v.errors)} error(s); manifest not written[/red]")
            raise typer.Exit(1)

        rows = mf.build_rows(entries, build)
        if not check:
            path = mf.write(rows, build)
            console.print(f"[green]wrote[/green] {path.relative_to(build.repo)}")
        run.inputs = {f"{r.id}@{r.version}": r.sha256 for r in rows}
        run.metrics = {
            "rows": len(rows),
            "distinct_ids": len({r.id for r in rows}),
            "warnings": len(v.warnings),
        }

    counts: dict[str, int] = {}
    for r in rows:
        counts[r.disposition] = counts.get(r.disposition, 0) + 1
    table = Table(show_header=True, header_style="bold")
    for col in ("id", "ver", "class", "status", "disp", "target", "bytes"):
        table.add_column(col)
    for r in rows:
        table.add_row(
            r.id,
            r.version,
            r.source_class,
            r.status,
            r.disposition,
            r.intended_target,
            f"{r.bytes:,}",
        )
    console.print(table)
    console.print(
        "  ".join(f"[bold]{k}[/bold] {n}" for k, n in sorted(counts.items()))
        + f"   [dim]{len(rows)} rows, {len({r.id for r in rows})} distinct ids[/dim]"
    )


@app.command()
def probe(build_dir: BuildArg) -> None:
    """Phase 0 — classification evidence report for human ruling."""
    build, entries = _load(build_dir)
    cfg = build.load_config()
    media = build.dir / ".media"
    probes = []
    for e in sorted(entries, key=lambda x: (x.processing_order, x.id)):
        if e.disposition is Disposition.superseded:
            continue
        src = build.resolve(e.path)
        result = nz.normalize(src, e.id, media, e.pseudo_headings)
        probes.append(
            pb.probe_text(nz.strip_anchors(result.text), e.id, e.source_class.value)
        )

    report = pb.render_report(probes, cfg.edition, cfg.versions.probe)
    out = build.reports / "probe" / "classification_probe.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")

    flagged = [p for p in probes if p.flags]
    with rec.record(build, "probe", "probe", {"probe": cfg.versions.probe}) as run:
        run.outputs = {str(out.relative_to(build.repo)): _sha(out)}
        run.metrics = {
            "sources": len(probes),
            "flagged": len(flagged),
            "tokens": len(report) // 4,
        }
        run.notes = "; ".join(f"{p.source_id}: {f}" for p in flagged for f in p.flags)[:300]
    console.print(f"[green]wrote[/green] {out.relative_to(build.repo)}")
    console.print(
        f"{len(probes)} probed, [bold]{len(flagged)}[/bold] flagged, "
        f"~{len(report) // 4:,} tokens"
    )
    for p in flagged:
        for f in p.flags:
            console.print(f"  [yellow]{p.source_id}[/yellow] {f}")


@app.command("normalize-full")
def normalize_full(
    build_dir: BuildArg,
    source: Annotated[Optional[str], typer.Option(help="Single source id.")] = None,
) -> None:
    """Phase 1 — faithful, coordinate-annotated Markdown for every source."""
    build, entries = _load(build_dir)
    build.full.mkdir(parents=True, exist_ok=True)
    media = build.dir / ".media"

    todo = [
        e
        for e in sorted(entries, key=lambda x: (x.processing_order, x.id))
        if e.disposition is not Disposition.superseded
        and (source is None or e.id == source)
    ]
    if not todo:
        console.print("[red]no matching sources[/red]")
        raise typer.Exit(1)

    figures: list[dict] = []
    table = Table(show_header=True, header_style="bold")
    for col in ("id", "headings", "promoted", "blocks", "tables", "figs", "char drift"):
        table.add_column(col, justify="right")

    for e in todo:
        result = nz.normalize(build.resolve(e.path), e.id, media, e.pseudo_headings)
        (build.full / f"{e.id}.md").write_text(result.text, encoding="utf-8")
        figures.extend(f.__dict__ for f in result.figures)
        drift = f"{result.char_delta:+.2%}"
        table.add_row(
            e.id,
            str(result.headings),
            str(result.promoted) if result.promoted else "-",
            str(result.blocks),
            str(result.tables),
            str(len(result.figures)),
            drift if abs(result.char_delta) > 0.001 else "0.00%",
        )

    with rec.record(
        build, "normalize-full", "normalize-full",
        {"normalizer_full": build.load_config().versions.normalizer_full},
    ) as run:
        run.inputs = {e.id: mf.sha256(build.resolve(e.path)) for e in todo}
        run.outputs = {e.id: _sha(build.full / f"{e.id}.md") for e in todo}
        run.metrics = {
            "sources": len(todo),
            "figures": len(figures),
            "coordinates": sum(
                len(nz.coordinates((build.full / f"{e.id}.md").read_text(encoding="utf-8")))
                for e in todo
            ),
        }

    reg = build.reports / "figure_registry.jsonl"
    reg.parent.mkdir(parents=True, exist_ok=True)
    reg.write_text(
        "\n".join(json.dumps(f, ensure_ascii=False) for f in figures) + "\n",
        encoding="utf-8",
    )
    console.print(table)
    console.print(
        f"[green]wrote[/green] {len(todo)} file(s) to "
        f"{build.full.relative_to(build.repo)}  ·  {len(figures)} figures registered"
    )


@app.command("normalize-lean")
def normalize_lean(
    build_dir: BuildArg,
    source: Annotated[Optional[str], typer.Option(help="Single source id.")] = None,
) -> None:
    """Phase 2 — deterministic boilerplate removal with a reversible ledger."""
    build, entries = _load(build_dir)
    build.lean.mkdir(parents=True, exist_ok=True)
    ledger_dir = build.reports / "lean"
    ledger_dir.mkdir(parents=True, exist_ok=True)

    todo = [
        e
        for e in sorted(entries, key=lambda x: (x.processing_order, x.id))
        if e.disposition is not Disposition.superseded
        and (source is None or e.id == source)
    ]
    rows, tot_full, tot_lean, tot_spared = [], 0, 0, 0
    table = Table(show_header=True, header_style="bold")
    for col in ("id", "full tok", "lean tok", "removed", "spared", "reduction"):
        table.add_column(col, justify="right")

    for e in todo:
        src = build.full / f"{e.id}.md"
        if not src.exists():
            console.print(f"[red]missing[/red] {src.name}; run normalize-full first")
            raise typer.Exit(1)
        r = ln.lean(src.read_text(encoding="utf-8"), e.id)
        (build.lean / f"{e.id}.md").write_text(r.text, encoding="utf-8")

        (ledger_dir / f"{e.id}.removals.jsonl").write_text(
            "".join(
                json.dumps(
                    {"ruleset": ln.RULESET_VERSION, **x.__dict__}, ensure_ascii=False
                )
                + "\n"
                for x in r.removals
            ),
            encoding="utf-8",
        )
        tot_full += r.chars_full
        tot_lean += r.chars_lean
        tot_spared += len(r.spared)
        rows.append(
            {
                "id": e.id,
                "chars_full": r.chars_full,
                "chars_lean": r.chars_lean,
                "tokens_full": r.chars_full // 4,
                "tokens_lean": r.chars_lean // 4,
                "removed": len(r.removals),
                "spared": len(r.spared),
                "reduction": f"{r.reduction:.4f}",
                "ruleset": ln.RULESET_VERSION,
            }
        )
        table.add_row(
            e.id,
            f"{r.chars_full // 4:,}",
            f"{r.chars_lean // 4:,}",
            str(len(r.removals)) if r.removals else "-",
            str(len(r.spared)) if r.spared else "-",
            f"{r.reduction:.2%}" if r.reduction else "-",
        )

    with rec.record(
        build, "normalize-lean", "normalize-lean", {"lean_ruleset": ln.RULESET_VERSION}
    ) as run:
        run.inputs = {e.id: _sha(build.full / f"{e.id}.md") for e in todo}
        run.outputs = {e.id: _sha(build.lean / f"{e.id}.md") for e in todo}
        run.metrics = {
            "sources": len(todo),
            "tokens_full": tot_full // 4,
            "tokens_lean": tot_lean // 4,
            "removed": sum(r["removed"] for r in rows),
            "spared": tot_spared,
            "reduction": round((tot_full - tot_lean) / tot_full, 4) if tot_full else 0,
        }

    summary = ledger_dir / "corpus_summary.csv"
    with summary.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    console.print(table)
    overall = (tot_full - tot_lean) / tot_full if tot_full else 0
    console.print(
        f"[green]wrote[/green] {len(todo)} lean file(s)  ·  ruleset "
        f"v{ln.RULESET_VERSION}  ·  corpus reduction [bold]{overall:.2%}[/bold]  ·  "
        f"{tot_spared} block(s) spared by protected patterns"
    )


@app.command("chunk")
def chunk_cmd(
    build_dir: BuildArg,
    source: Annotated[Optional[str], typer.Option(help="Single source id.")] = None,
) -> None:
    """Phase 3 — deterministic chunking of lean sources."""
    build, entries = _load(build_dir)
    cfg = build.load_config()
    ch = cfg.chunking or {}
    out_dir = build.dir / "chunks"
    out_dir.mkdir(parents=True, exist_ok=True)

    todo = [
        e
        for e in sorted(entries, key=lambda x: (x.processing_order, x.id))
        if e.disposition is not Disposition.superseded
        and (source is None or e.id == source)
    ]
    table = Table(show_header=True, header_style="bold")
    for col in ("id", "blocks", "chunks", "tokens", "largest", "oversized"):
        table.add_column(col, justify="right")

    errors: list[str] = []
    total_chunks = 0
    for e in todo:
        src = build.lean / f"{e.id}.md"
        if not src.exists():
            console.print(f"[red]missing[/red] {src.name}; run normalize-lean first")
            raise typer.Exit(1)
        text = src.read_text(encoding="utf-8")
        r = ck.chunk(
            text,
            e.id,
            target_tokens=ch.get("target_tokens", 10000),
            max_tokens=ch.get("max_tokens", 14000),
            overlap_tokens=ch.get("overlap_tokens", 400),
            respect_headings=ch.get("respect_headings", True),
            seam_fraction=ch.get("seam_fraction", ck.DEFAULT_SEAM_FRACTION),
        )
        errors.extend(ck.validate(r, text))
        (out_dir / f"{e.id}.jsonl").write_text(
            "".join(json.dumps(c.to_dict(), ensure_ascii=False) + "\n" for c in r.chunks),
            encoding="utf-8",
        )
        total_chunks += len(r.chunks)
        largest = max((c.tokens for c in r.chunks), default=0)
        table.add_row(
            e.id,
            str(r.blocks),
            str(len(r.chunks)),
            f"{r.tokens:,}",
            f"{largest:,}",
            str(len(r.oversized)) if r.oversized else "-",
        )

    with rec.record(build, "chunk", "chunk", {"chunker": ck.CHUNKER_VERSION}) as run:
        run.inputs = {e.id: _sha(build.lean / f"{e.id}.md") for e in todo}
        run.outputs = {e.id: _sha(out_dir / f"{e.id}.jsonl") for e in todo}
        run.metrics = {
            "sources": len(todo),
            "chunks": total_chunks,
            "errors": len(errors),
            "seam_fraction": ch.get("seam_fraction", ck.DEFAULT_SEAM_FRACTION),
            "target_tokens": ch.get("target_tokens", 10000),
        }
        if errors:
            run.status = "error"
            run.notes = "; ".join(errors)[:300]

    console.print(table)
    for err in errors:
        console.print(f"[red]error[/red] {err}")
    if errors:
        raise typer.Exit(1)
    console.print(
        f"[green]ok[/green] {total_chunks} chunks from {len(todo)} sources  ·  "
        f"chunker v{ck.CHUNKER_VERSION}  ·  every block owned exactly once"
    )


@app.command("extract")
def extract_cmd(
    build_dir: BuildArg,
    source: Annotated[Optional[str], typer.Option(help="Source id. Omit for all.")] = None,
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Estimate only; no calls.")] = False,
    fake: Annotated[bool, typer.Option("--fake", help="Deterministic provider, no network.")] = False,
) -> None:
    """Phase 4 — Claude extraction, Pass A. Bounded, cached, schema-constrained."""
    build, entries = _load(build_dir)
    cfg = build.load_config()
    ns_path = build.dir / "architecture" / "owner_namespaces.yaml"
    if not ns_path.exists():
        console.print(f"[red]missing[/red] {ns_path.name}; namespaces must be ruled first")
        raise typer.Exit(1)
    namespaces = sorted(rc.load_namespaces(ns_path))

    todo = [
        e for e in sorted(entries, key=lambda x: (x.processing_order, x.id))
        if e.disposition is Disposition.compile and (source is None or e.id == source)
    ]
    if not todo:
        console.print("[red]no matching compiled sources[/red]")
        raise typer.Exit(1)

    chunks: list[dict] = []
    for e in todo:
        path = build.dir / "chunks" / f"{e.id}.jsonl"
        if not path.exists():
            console.print(f"[red]missing[/red] {path.name}; run chunk first")
            raise typer.Exit(1)
        chunks.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)

    if dry_run:
        est = ex.estimate(chunks)
        table = Table(show_header=False)
        table.add_column("k")
        table.add_column("v", justify="right")
        for k, v in est.items():
            table.add_row(k.replace("_", " "), f"{v:,}" if isinstance(v, int) else str(v))
        console.print(table)
        console.print(
            f"[dim]estimate only — records/1k and output/record are seeded guesses "
            f"refined after the pilot. Prompt v{ex.PROMPT_VERSION}, "
            f"schema v{rc.RECORD_SCHEMA_VERSION}, {len(namespaces)} namespaces.[/dim]"
        )
        return

    prompt_path = build.repo / "compiler" / "prompts" / f"extract-{ex.PROMPT_VERSION}.md"
    system_prompt = prompt_path.read_text(encoding="utf-8")

    if fake:
        provider = ex.FakeProvider()
    else:
        from .providers.anthropic import AnthropicProvider, ProviderUnavailable

        model = (cfg.model_dump().get("providers") or {}).get("extraction", {}).get("model")
        model = model or os.environ.get("ANTHROPIC_EXTRACTION_MODEL", "")
        if not model:
            console.print(
                "[red]no extraction model configured[/red] — set providers.extraction.model "
                "in config.yaml or ANTHROPIC_EXTRACTION_MODEL"
            )
            raise typer.Exit(1)
        try:
            provider = AnthropicProvider(model=model)
        except ProviderUnavailable as exc:
            console.print(f"[red]provider unavailable[/red] {exc}")
            raise typer.Exit(1)

    cache_dir = build.dir / ".cache" / "extract"
    meta = {e.id: e for e in todo}
    results: dict[str, ex.ExtractResult] = {}

    with rec.record(
        build, "extract", "extract",
        {"prompt": ex.PROMPT_VERSION, "schema": rc.RECORD_SCHEMA_VERSION,
         "provider": provider.name, "model": provider.model},
    ) as run:
        for c in chunks:
            e = meta[c["source"]]
            res = results.setdefault(c["source"], ex.ExtractResult(source_id=c["source"]))
            start = len(res.records) + 1
            raw, call = ex.extract_chunk(
                c,
                {"source_class": e.source_class.value,
                 "wording_fidelity": e.wording_fidelity.value,
                 "notes": e.notes},
                namespaces, start, system_prompt, provider, cache_dir,
            )
            res.calls.append(call)
            for item in raw:
                try:
                    res.records.append(rc.AtomicRecord.model_validate(item))
                except Exception as exc:  # noqa: BLE001
                    res.errors.append(f"{c['id']}: schema — {str(exc)[:160]}")

        table = Table(show_header=True, header_style="bold")
        for col in ("id", "chunks", "records", "cached", "in tok", "out tok", "errors"):
            table.add_column(col, justify="right")

        total_records = total_errors = 0
        for sid, res in results.items():
            lean = (build.lean / f"{sid}.md").read_text(encoding="utf-8")
            blocks = {b.coord: b.text for b in ck.parse_blocks(lean)}
            res.errors.extend(
                rc.validate_records(res.records, blocks, set(namespaces), sid)
            )
            out = build.dir / "records" / f"{sid}.jsonl"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(
                "".join(r.model_dump_json() + "\n" for r in res.records), encoding="utf-8"
            )
            total_records += len(res.records)
            total_errors += len(res.errors)
            table.add_row(
                sid, str(len(res.calls)), str(len(res.records)),
                str(sum(c.cached for c in res.calls)),
                f"{res.input_tokens:,}", f"{res.output_tokens:,}",
                str(len(res.errors)) if res.errors else "-",
            )

        calls_log = build.logs / "calls.jsonl"
        with calls_log.open("a", encoding="utf-8") as fh:
            for res in results.values():
                for c in res.calls:
                    fh.write(json.dumps(c.__dict__, ensure_ascii=False) + "\n")

        run.metrics = {
            "sources": len(results),
            "chunks": len(chunks),
            "records": total_records,
            "errors": total_errors,
            "input_tokens": sum(r.input_tokens for r in results.values()),
            "output_tokens": sum(r.output_tokens for r in results.values()),
            "cost_usd": round(sum(r.cost for r in results.values()), 2),
        }
        if total_errors:
            run.status = "error"

    console.print(table)
    for res in results.values():
        for err in res.errors[:10]:
            console.print(f"  [red]{err}[/red]")
    cost = sum(r.cost for r in results.values())
    console.print(
        f"[green]wrote[/green] {total_records} records  ·  ${cost:.2f} spent  ·  "
        f"prompt v{ex.PROMPT_VERSION}  ·  {total_errors} validation error(s)"
    )


@app.command("log")
def log_cmd(
    build_dir: BuildArg,
    limit: Annotated[int, typer.Option(help="Most recent N runs.")] = 20,
) -> None:
    """Show the Build Record — every phase run, in order."""
    build = Build(build_dir)
    runs = rec.history(build)
    if not runs:
        console.print("[dim]no runs recorded[/dim]")
        return
    for r in runs[-limit:]:
        mark = "[green]ok   [/green]" if r["status"] == "ok" else "[red]error[/red]"
        when = r["timestamp"].replace("+00:00", "").replace("T", " ")
        ver = ",".join(str(v) for v in r.get("versions", {}).values()) or "-"
        console.print(
            f"{mark} [bold]{r['phase']:<15}[/bold] {when}  "
            f"v{ver}  {r.get('git', '-')}  {r.get('duration_s', 0)}s"
        )
        metrics = r.get("metrics", {})
        if metrics:
            console.print(
                "        " + "  ".join(f"[dim]{k}[/dim]={v}" for k, v in metrics.items())
            )
        if r.get("notes"):
            console.print(f"        [yellow]{r['notes'][:150]}[/yellow]")
    console.print(f"[dim]{len(runs)} run(s) recorded[/dim]")


@app.command("check-stale")
def check_stale(build_dir: BuildArg) -> None:
    """Report phases whose inputs have changed since they last ran (spec §7)."""
    build, entries = _load(build_dir)
    live = [e for e in entries if e.disposition is not Disposition.superseded]

    def _existing(paths: dict) -> dict:
        return {k: _sha(v) for k, v in paths.items() if v.exists()}

    stale = rec.staleness(
        build,
        {
            "manifest": {
                f"{e.id}@{e.version}": mf.sha256(build.resolve(e.path))
                for e in entries
                if build.resolve(e.path).exists()
            },
            "normalize-full": {
                e.id: mf.sha256(build.resolve(e.path))
                for e in live
                if build.resolve(e.path).exists()
            },
            "normalize-lean": _existing({e.id: build.full / f"{e.id}.md" for e in live}),
            "chunk": _existing({e.id: build.lean / f"{e.id}.md" for e in live}),
        },
    )
    if not stale:
        console.print("[green]fresh[/green] every recorded phase matches its inputs")
        return
    for phase, changed in stale.items():
        console.print(
            f"[yellow]stale[/yellow] {phase}: {len(changed)} input(s) changed "
            f"— {', '.join(changed[:5])}"
        )


@app.command()
def status(build_dir: BuildArg) -> None:
    """Show which phase artifacts exist."""
    build = Build(build_dir)
    checks = [
        ("Phase 0  registry", build.sources_yaml),
        ("Phase 0  manifest", build.manifest),
        ("Phase 0  probe", build.reports / "probe" / "classification_probe.md"),
        ("Phase 1  normalized_full", build.full),
        ("Phase 2  normalized_lean", build.lean),
        ("Phase 3  chunks", build.dir / "chunks"),
    ]
    for label, path in checks:
        if path.exists():
            n = len(list(path.glob("*.*"))) if path.is_dir() else 1
            mark = "[green]ok[/green]  " if n else "[yellow]empty[/yellow]"
            extra = f"{n} file(s)" if path.is_dir() else ""
            console.print(f"{mark} {label:28} {extra}")
        else:
            console.print(f"[dim]--[/dim]   {label:28} [dim]absent[/dim]")


if __name__ == "__main__":
    app()
