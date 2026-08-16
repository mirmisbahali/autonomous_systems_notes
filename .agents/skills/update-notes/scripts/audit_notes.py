#!/usr/bin/env python3
"""Audit managed learning notes and generate a core-Markdown dashboard."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Callable


MANAGED_TYPES = {"concept", "interview-question", "lecture", "moc", "project-design"}
COMMON_TRACKED_FIELDS = {"confidence", "evidence", "knowledge_status", "last_reviewed", "mastery"}
RELATIONSHIP_FIELDS = {"contrasts", "examples", "implemented_in", "prerequisites", "related", "used_by"}
KNOWLEDGE_STATUSES = {
    "studied-theoretically",
    "assisted",
    "independently-implemented",
    "independently-debugged",
    "integrated",
}
CONCEPT_SECTIONS = {
    "Why it matters",
    "In simple terms",
    "How it works",
    "Concrete example",
    "Common failure modes",
    "Active recall",
    "Interview check",
    "Intuitive example",
    "Connections and exercises",
    "Sources",
}
LINK_RE = re.compile(r"!?\[\[([^\]|#]+)")
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class Note:
    path: Path
    relative: str
    text: str
    metadata: dict[str, Any]

    @property
    def note_type(self) -> str:
        return str(self.metadata.get("type", ""))

    @property
    def domain(self) -> str:
        value = self.metadata.get("domain")
        return str(value).strip() if value not in (None, "") else "unassigned"

    @property
    def wikilink(self) -> str:
        target = self.relative.removesuffix(".md")
        return f"[[{target}|{self.path.stem}]]"


def scalar(value: str) -> Any:
    value = value.strip()
    if value in {"", "null", "~"}:
        return None
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, list) else value
        except json.JSONDecodeError:
            inner = value[1:-1].strip()
            return [] if not inner else [part.strip().strip("'\"") for part in inner.split(",")]
    lowered = value.lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value.strip("'\"")


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    metadata: dict[str, Any] = {}
    current: str | None = None
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if match:
            current = match.group(1)
            metadata[current] = scalar(match.group(2) or "")
            continue
        item = re.match(r"^\s+-\s*(.*)$", line)
        if item and current:
            if not isinstance(metadata.get(current), list):
                metadata[current] = []
            metadata[current].append(scalar(item.group(1)))
    return metadata


def excluded(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    return (
        any(part.startswith(".") for part in relative.parts)
        or (relative.parts and relative.parts[0] == "99_templates")
        or relative.as_posix() in {
        "00_dashboard/Knowledge Dashboard.md",
        "00_dashboard/Learning Log.md",
        }
    )


def load_notes(root: Path) -> list[Note]:
    notes: list[Note] = []
    for path in sorted(root.rglob("*.md")):
        if excluded(path, root):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        notes.append(
            Note(
                path=path,
                relative=path.relative_to(root).as_posix(),
                text=text,
                metadata=parse_frontmatter(text),
            )
        )
    return notes


def list_value(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def issue(severity: str, note: Note, message: str) -> dict[str, str]:
    return {"severity": severity, "path": note.relative, "message": message}


def resolve_link(note: Note, target: str, root: Path, stems: dict[str, list[Note]]) -> bool:
    cleaned = target.strip().removesuffix(".md")
    if not cleaned:
        return True
    direct = root / f"{cleaned}.md"
    relative = note.path.parent / f"{cleaned}.md"
    return direct.exists() or relative.exists() or cleaned.casefold() in stems


def audit(root: Path) -> tuple[list[Note], list[dict[str, str]], dict[str, list[Note]]]:
    notes = load_notes(root)
    managed = [note for note in notes if note.note_type in MANAGED_TYPES]
    issues: list[dict[str, str]] = []
    stems: dict[str, list[Note]] = defaultdict(list)
    for note in notes:
        stems[note.path.stem.casefold()].append(note)

    for duplicates in stems.values():
        if len(duplicates) > 1:
            joined = ", ".join(note.relative for note in duplicates)
            issues.append({"severity": "warning", "path": joined, "message": "Duplicate note title"})

    inbound: dict[str, int] = defaultdict(int)
    for source in notes:
        for target in LINK_RE.findall(source.text):
            inbound[target.strip().split("/")[-1].casefold()] += 1

    orphans: list[Note] = []
    for note in managed:
        metadata = note.metadata
        if metadata.get("ai_edit") is False:
            continue
        if not metadata.get("domain"):
            issues.append(issue("error", note, "Missing domain"))
        if note.note_type != "moc":
            missing = sorted(field for field in COMMON_TRACKED_FIELDS if field not in metadata)
            if missing:
                issues.append(issue("error", note, f"Missing tracked fields: {', '.join(missing)}"))

            confidence = metadata.get("confidence")
            if confidence is not None and (not isinstance(confidence, int) or not 0 <= confidence <= 4):
                issues.append(issue("error", note, "confidence must be null or an integer from 0 to 4"))

            mastery = metadata.get("mastery")
            if not isinstance(mastery, int) or not 0 <= mastery <= 4:
                issues.append(issue("error", note, "mastery must be an integer from 0 to 4"))
            else:
                evidence = list_value(metadata.get("evidence"))
                status = metadata.get("knowledge_status")
                if mastery > 2 and not evidence:
                    issues.append(issue("error", note, "mastery above 2 requires linked evidence"))
                if mastery == 3 and status not in {
                    "independently-implemented",
                    "independently-debugged",
                    "integrated",
                }:
                    issues.append(issue("error", note, "mastery 3 requires independent implementation status"))
                if mastery == 4 and status != "integrated":
                    issues.append(issue("error", note, "mastery 4 requires integrated status"))
            if metadata.get("knowledge_status") not in KNOWLEDGE_STATUSES:
                issues.append(issue("error", note, "Invalid knowledge_status"))

        if note.note_type == "concept":
            missing_relationships = sorted(field for field in RELATIONSHIP_FIELDS if field not in metadata)
            if missing_relationships:
                issues.append(issue("error", note, f"Missing relationship fields: {', '.join(missing_relationships)}"))
            headings = set(HEADING_RE.findall(note.text))
            missing_sections = sorted(CONCEPT_SECTIONS - headings)
            if missing_sections:
                issues.append(issue("error", note, f"Missing concept sections: {', '.join(missing_sections)}"))
            relationships = sum((list_value(metadata.get(field)) for field in RELATIONSHIP_FIELDS), [])
            if not relationships and inbound[note.path.stem.casefold()] == 0:
                orphans.append(note)

        for target in LINK_RE.findall(note.text):
            if not resolve_link(note, target, root, stems):
                issues.append(issue("warning", note, f"Unresolved wikilink: [[{target}]]"))

        if "AI-added" in note.text:
            callouts = [line for line in note.text.splitlines() if "AI-added" in line]
            for line in callouts:
                if "verified" not in line.lower() and "needs verification" not in line.lower():
                    issues.append(issue("error", note, "AI-added callout lacks verification status"))

    groups = {
        "managed": managed,
        "concepts": [note for note in managed if note.note_type == "concept"],
        "orphans": orphans,
        "pending": [note for note in managed if "AI-added — needs verification" in note.text],
    }
    return notes, issues, groups


def value_label(value: Any) -> str:
    return "not rated" if value is None else str(value)


def bullets(notes: list[Note], suffix: Callable[[Note], str] | None = None) -> list[str]:
    if not notes:
        return ["- None."]
    result = []
    for note in sorted(notes, key=lambda item: (item.domain.casefold(), item.path.stem.casefold())):
        extra = f" — {suffix(note)}" if suffix else ""
        result.append(f"- {note.wikilink}{extra}")
    return result


def dashboard(root: Path, output: Path, issues: list[dict[str, str]], groups: dict[str, list[Note]]) -> None:
    concepts = groups["concepts"]
    domains: dict[str, list[Note]] = defaultdict(list)
    for note in concepts:
        domains[note.domain].append(note)
    never_reviewed = [note for note in concepts if note.metadata.get("last_reviewed") is None]
    low_confidence = [
        note
        for note in concepts
        if note.metadata.get("confidence") is None
        or (isinstance(note.metadata.get("confidence"), int) and note.metadata["confidence"] <= 1)
    ]

    lines = [
        "# Knowledge Dashboard",
        "",
        "> [!info] Core Markdown dashboard",
        "> Regenerated by `$update-notes`; no Dataview plugin is required.",
        "",
        "## Concepts by domain",
        "",
    ]
    if domains:
        for domain in sorted(domains, key=str.casefold):
            lines.extend([f"### {domain}", ""])
            lines.extend(
                bullets(
                    domains[domain],
                    lambda note: (
                        f"mastery {value_label(note.metadata.get('mastery'))}, "
                        f"confidence {value_label(note.metadata.get('confidence'))}"
                    ),
                )
            )
            lines.append("")
    else:
        lines.extend(["- No managed concept notes yet.", ""])

    lines.extend(["## Recall priorities", "", "### Never reviewed", ""])
    lines.extend(bullets(never_reviewed))
    lines.extend(["", "### Low or unrated confidence", ""])
    lines.extend(bullets(low_confidence, lambda note: f"confidence {value_label(note.metadata.get('confidence'))}"))
    lines.extend(["", "## Weak connections", ""])
    lines.extend(bullets(groups["orphans"]))
    lines.extend(["", "## AI additions needing verification", ""])
    lines.extend(bullets(groups["pending"]))
    lines.extend(["", "## Audit issues", ""])
    if issues:
        for item in sorted(issues, key=lambda value: (value["severity"], value["path"], value["message"])):
            lines.append(f"- **{item['severity'].title()}:** `{item['path']}` — {item['message']}")
    else:
        lines.append("- None.")
    lines.extend(
        [
            "",
            "## Recent activity",
            "",
            "See [[00_dashboard/Learning Log|Learning Log]].",
            "",
            f"_Generated {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')}._",
            "",
        ]
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--dashboard")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    _, issues, groups = audit(root)
    if args.dashboard:
        output = Path(args.dashboard)
        if not output.is_absolute():
            output = root / output
        dashboard(root, output, issues, groups)
    summary = {
        "managed_notes": len(groups["managed"]),
        "concepts": len(groups["concepts"]),
        "errors": sum(item["severity"] == "error" for item in issues),
        "warnings": sum(item["severity"] == "warning" for item in issues),
        "orphans": len(groups["orphans"]),
        "needs_verification": len(groups["pending"]),
    }
    json.dump(summary, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 1 if summary["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
