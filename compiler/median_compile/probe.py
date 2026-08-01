"""Phase 0 — classification probe.

Deterministic evidence for the human classification ruling. Extracts front
matter, the level 1-2 heading tree, closing lines, and authority-marker
frequencies from every registered source, then flags rows whose textual
evidence disagrees with their declared source_class.

Exists because CATCHALL_3 was initially misclassified from its filename alone.
No model calls. Roughly 21k tokens across the v0.5 corpus, against ~277k for
full reads.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

#: Textual signals that indicate what kind of document this actually is.
MARKERS: dict[str, str] = {
    "adopted": r"\*\*Adopted|^Adopted\b",
    "ruling": r"[Rr]uling|[Rr]esolved by",
    "not_state": r"[Nn]ot STATE|Designer commentary|commentary only",
    "state": r"\bSTATE\b",
    "supersede": r"[Ss]upersed",
    "provisional": r"[Pp]rovisional",
    "deferred": r"[Dd]eferred?\b",
    "open_question": r"[Oo]pen question|remains unresolved|[Uu]nresolved",
    "audit": r"[Aa]udit",
    "recommend": r"[Rr]ecommend",
    "canon": r"[Cc]anon",
    "normative": r"\bmust\b|\bmay not\b|\bshall\b",
}

#: Phrases by which a document declares its own authority. Scanned against front
#: matter only. This is the signal that identified CATCHALL_3 as a ruling
#: document; a bare marker count would not have.
#:
#: "governing" was removed after it matched ordinary spec prose ("governing
#: premise", "governing principles") in five documents. Every phrase here must
#: be one a document uses about *itself*, not about its subject matter.
FRONT_AUTHORITY = re.compile(
    r"authoritative|controlling (?:working )?record|working ledger|"
    r"adopted (?:baseline )?ruling|not the final|supersedes all|"
    r"source of truth",
    re.IGNORECASE,
)

#: Marker counts are noisy across this corpus and are reported rather than
#: flagged, except where a threshold has been calibrated against real spread.
#: 'supersede' (0-15 in ordinary specs) and 'normative' (this corpus states
#: rules declaratively, not with "must") were removed as flags after producing
#: 13 flags of which 11 were noise.
ADOPTED_RULING_MIN = 5
RULING_WITHOUT_ADOPTION_MAX = 3
AUDIT_PER_1K_MAX = 1.5
STUB_WORDS = 300

FRONT_LINES = 45
FRONT_KEEP = 22
TAIL_LINES = 25
TAIL_KEEP = 8
HEAD_KEEP = 45


@dataclass
class Probe:
    source_id: str
    declared_class: str
    words: int
    front: list[str]
    headings: list[str]
    tail: list[str]
    markers: dict[str, int]
    flags: list[str] = field(default_factory=list)

    def render(self) -> str:
        marks = ", ".join(
            f"{k}:{v}" for k, v in sorted(self.markers.items(), key=lambda x: -x[1]) if v
        )
        parts = [
            f"### {self.source_id}  [declared: {self.declared_class}]  ({self.words:,} words)",
        ]
        if self.flags:
            parts.append("!! " + "\n!! ".join(self.flags))
        parts += [
            "[FRONT]",
            "\n".join(self.front),
            "[HEADINGS]",
            "\n".join(self.headings) or "(none)",
            "[TAIL]",
            "\n".join(self.tail),
            f"[MARKERS] {marks or '(none)'}",
        ]
        return "\n".join(parts) + "\n"


def _classify_flags(
    declared: str, markers: dict[str, int], words: int, front: list[str]
) -> list[str]:
    """Cheap disagreement detector. Advisory only; the human rules.

    Tuned to be quiet. A report where most flags are noise trains the reader to
    skip flags, which defeats the purpose of running the probe at all.
    """
    flags: list[str] = []
    per_1k = {k: (v * 1000 / words if words else 0) for k, v in markers.items()}
    adopted = markers.get("adopted", 0)

    claims = sorted({m.group(0).lower() for m in FRONT_AUTHORITY.finditer("\n".join(front))})
    if claims and declared not in {"human_ruling", "baseline"}:
        flags.append(
            f"front matter claims authority ({', '.join(claims)}) but declared "
            f"{declared!r} - read the doctrine block before compiling"
        )

    if adopted >= ADOPTED_RULING_MIN and declared != "human_ruling":
        flags.append(
            f"{adopted} 'Adopted' markers but declared {declared!r} - this reads "
            "as a ruling document"
        )
    if declared == "human_ruling" and adopted < RULING_WITHOUT_ADOPTION_MAX:
        flags.append(
            f"declared human_ruling but only {adopted} adoption marker(s) - "
            "confirm this document actually rules"
        )
    if markers.get("not_state", 0):
        flags.append(
            f"{markers['not_state']} explicit non-STATE marker(s) - extraction must "
            "honour these as weight SILENT, not STATE"
        )
    if per_1k.get("audit", 0) >= AUDIT_PER_1K_MAX and declared == "detailed_spec":
        flags.append("audit language is dense for a detailed_spec")
    if words < STUB_WORDS and declared == "detailed_spec":
        flags.append(f"only {words} words - a stub, not a specification")
    return flags


def probe_text(text: str, source_id: str, declared_class: str) -> Probe:
    lines = text.split("\n")
    front = [l.rstrip() for l in lines[:FRONT_LINES] if l.strip()][:FRONT_KEEP]
    headings = [l.rstrip() for l in lines if re.match(r"^#{1,2} ", l)][:HEAD_KEEP]
    tail = [l.rstrip() for l in lines[-TAIL_LINES:] if l.strip()][-TAIL_KEEP:]
    markers = {
        k: len(re.findall(p, text, re.MULTILINE)) for k, p in MARKERS.items()
    }
    words = len(text.split())
    return Probe(
        source_id=source_id,
        declared_class=declared_class,
        words=words,
        front=front,
        headings=headings,
        tail=tail,
        markers={k: v for k, v in markers.items() if v},
        flags=_classify_flags(declared_class, markers, words, front),
    )


def render_report(probes: list[Probe], edition: str, probe_version: str) -> str:
    flagged = [p for p in probes if p.flags]
    head = [
        f"# MEDIAN v{edition} — Phase 0 Classification Probe",
        "",
        f"Probe version {probe_version}. Deterministic; no model calls.",
        "",
        f"{len(probes)} sources probed. {len(flagged)} carry advisory flags.",
        "",
        "Flags are evidence for a human ruling, not a ruling. Confirm or override "
        "each one in `sources.yaml`, then re-run.",
        "",
        "## Flag summary",
        "",
    ]
    if flagged:
        for p in flagged:
            for f in p.flags:
                head.append(f"- **{p.source_id}** — {f}")
    else:
        head.append("- none")
    head += ["", "---", "", "## Evidence", ""]
    return "\n".join(head) + "\n" + "\n".join(p.render() for p in probes)
