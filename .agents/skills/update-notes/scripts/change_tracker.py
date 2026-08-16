#!/usr/bin/env python3
"""Track committed note inputs without reprocessing generated output."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any


STATE_VERSION = 1
IGNORED_PATHS = {
    ".obsidian/workspace.json",
    "AGENTS.md",
    "CLAUDE.md",
    "_interview_update_notes.md",
    "00_dashboard/Knowledge Dashboard.md",
    "00_dashboard/Learning Log.md",
}
IGNORED_PARTS = {
    ".git",
    ".agents",
    ".update-notes",
    ".cache",
    ".obsidian",
    "99_templates",
    "__pycache__",
    ".codelite",
    "build",
    "CMakeFiles",
}
IGNORED_SUFFIXES = {".a", ".dll", ".exe", ".o", ".obj", ".pyc", ".so", ".tags"}
PROTECTED_PARTS = {"assessment", "assessments", "exercise", "exercises", "workspace", "workspaces"}
CODE_SUFFIXES = {".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".ino", ".py", ".rs"}
DOCUMENT_SUFFIXES = {".bmp", ".gif", ".jpeg", ".jpg", ".pdf", ".png", ".svg", ".webp"}


class TrackerError(RuntimeError):
    pass


def git(root: Path, *args: str, binary: bool = False, check: bool = True) -> bytes | str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise TrackerError(message or f"git {' '.join(args)} failed")
    return result.stdout if binary else result.stdout.decode("utf-8", errors="surrogateescape")


def repository_root(value: str | None) -> Path:
    start = Path(value or ".").resolve()
    output = git(start, "rev-parse", "--show-toplevel")
    return Path(str(output).strip()).resolve()


def resolve_path(root: Path, value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (root / path).resolve()


def relative_path(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as exc:
        raise TrackerError(f"Path is outside the repository: {path}") from exc


def read_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise TrackerError(f"State file does not exist: {path}. Run the init command first.")
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise TrackerError(f"Cannot read state file {path}: {exc}") from exc
    if state.get("version") != STATE_VERSION or not state.get("checkpoint"):
        raise TrackerError(f"Unsupported or incomplete state file: {path}")
    state.setdefault("processed", {})
    return state


def atomic_json_write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def head_bytes(root: Path, revision: str, path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{revision}:{path}"],
        cwd=root,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise TrackerError(f"Cannot read {path} at {revision}")
    return result.stdout


def parse_name_status(raw: bytes) -> list[tuple[str, str, str | None]]:
    fields = raw.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    changes: list[tuple[str, str, str | None]] = []
    index = 0
    while index < len(fields):
        status = fields[index].decode("ascii", errors="replace")
        index += 1
        if status.startswith(("R", "C")):
            if index + 1 >= len(fields):
                raise TrackerError("Malformed Git rename record")
            old = fields[index].decode("utf-8", errors="surrogateescape")
            new = fields[index + 1].decode("utf-8", errors="surrogateescape")
            index += 2
            changes.append((status, new, old))
        else:
            if index >= len(fields):
                raise TrackerError("Malformed Git change record")
            path = fields[index].decode("utf-8", errors="surrogateescape")
            index += 1
            changes.append((status, path, None))
    return changes


def dirty_paths(root: Path) -> set[str]:
    raw = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all", binary=True)
    assert isinstance(raw, bytes)
    fields = raw.split(b"\0")
    dirty: set[str] = set()
    index = 0
    while index < len(fields):
        field = fields[index]
        index += 1
        if not field:
            continue
        text = field.decode("utf-8", errors="surrogateescape")
        if len(text) < 4:
            continue
        status = text[:2]
        dirty.add(text[3:])
        if "R" in status or "C" in status:
            if index < len(fields) and fields[index]:
                dirty.add(fields[index].decode("utf-8", errors="surrogateescape"))
                index += 1
    return dirty


def ignored(path: str) -> bool:
    pure = PurePosixPath(path)
    return (
        path in IGNORED_PATHS
        or any(part in IGNORED_PARTS for part in pure.parts)
        or any(part.lower().startswith("build-") for part in pure.parts)
        or pure.suffix.lower() in IGNORED_SUFFIXES
    )


def protected_by_path(path: str) -> bool:
    return any(part.lower() in PROTECTED_PARTS for part in PurePosixPath(path).parts)


def protected_by_frontmatter(content: bytes) -> bool:
    if not content.startswith(b"---"):
        return False
    header = content[:8192].decode("utf-8", errors="replace").lower()
    return "\nassessment: true" in header or "\nai_edit: false" in header


def kind_for(path: str, protected: bool) -> str:
    suffix = PurePosixPath(path).suffix.lower()
    if protected:
        return "protected-context"
    if suffix == ".md":
        return "editable-markdown"
    if suffix in CODE_SUFFIXES:
        return "code-context"
    if suffix in DOCUMENT_SUFFIXES:
        return "document-context"
    return "configuration-context"


def scan(args: argparse.Namespace) -> int:
    root = repository_root(args.root)
    state_path = resolve_path(root, args.state)
    state = read_state(state_path)
    base = str(state["checkpoint"])
    head = str(git(root, "rev-parse", args.head).strip())
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", base, head], cwd=root, check=False
    )
    if ancestor.returncode:
        raise TrackerError(f"Checkpoint {base} is not an ancestor of {head}")

    raw_changes = git(root, "diff", "--name-status", "-z", "-M", base, head, binary=True)
    assert isinstance(raw_changes, bytes)
    dirty = dirty_paths(root)
    candidates: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    processed: dict[str, str] = state.get("processed", {})

    for status, path, old_path in parse_name_status(raw_changes):
        if status.startswith("D"):
            skipped.append({"path": path, "status": status, "reason": "deleted", "blocking": False})
            continue
        if status.startswith("R") and old_path in processed:
            skipped.append(
                {
                    "path": path,
                    "old_path": old_path,
                    "status": status,
                    "reason": "previously-processed-rename",
                    "blocking": False,
                }
            )
            continue
        if ignored(path):
            skipped.append({"path": path, "status": status, "reason": "ignored-path", "blocking": False})
            continue
        if path in dirty:
            skipped.append(
                {"path": path, "status": status, "reason": "uncommitted-overlap", "blocking": True}
            )
            continue

        content = head_bytes(root, head, path)
        digest = sha256(content)
        if processed.get(path) == digest:
            skipped.append(
                {"path": path, "status": status, "reason": "recorded-output-unchanged", "blocking": False}
            )
            continue
        is_protected = protected_by_path(path) or (
            PurePosixPath(path).suffix.lower() == ".md" and protected_by_frontmatter(content)
        )
        candidates.append(
            {
                "path": path,
                "old_path": old_path,
                "status": status,
                "kind": kind_for(path, is_protected),
                "protected": is_protected,
                "head_sha256": digest,
            }
        )

    ignored_uncommitted = sorted(path for path in dirty if not ignored(path))
    payload = {
        "version": STATE_VERSION,
        "root": root.as_posix(),
        "base": base,
        "head": head,
        "candidates": candidates,
        "skipped": skipped,
        "ignored_uncommitted": ignored_uncommitted,
        "has_blockers": any(item["blocking"] for item in skipped),
    }
    output_path = resolve_path(root, args.output)
    atomic_json_write(output_path, payload)
    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 2 if payload["has_blockers"] else 0


def initialise(args: argparse.Namespace) -> int:
    root = repository_root(args.root)
    state_path = resolve_path(root, args.state)
    if state_path.exists() and not args.force:
        raise TrackerError(f"State file already exists: {state_path}")
    checkpoint = str(git(root, "rev-parse", args.checkpoint).strip())
    atomic_json_write(
        state_path,
        {
            "version": STATE_VERSION,
            "checkpoint": checkpoint,
            "last_run": None,
            "processed": {},
        },
    )
    print(f"Initialised {relative_path(root, state_path)} at {checkpoint}")
    return 0


def finalise(args: argparse.Namespace) -> int:
    root = repository_root(args.root)
    state_path = resolve_path(root, args.state)
    state = read_state(state_path)
    scan_path = resolve_path(root, args.scan)
    try:
        scan_data = json.loads(scan_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise TrackerError(f"Cannot read scan file {scan_path}: {exc}") from exc

    current_head = str(git(root, "rev-parse", "HEAD").strip())
    if scan_data.get("head") != current_head:
        raise TrackerError("HEAD changed after the scan; scan again before finalising")
    blockers = [item for item in scan_data.get("skipped", []) if item.get("blocking")]
    if blockers:
        paths = ", ".join(item["path"] for item in blockers)
        raise TrackerError(f"Cannot finalise with blocking conflicts: {paths}")

    paths = {item["path"] for item in scan_data.get("candidates", [])}
    paths.update(args.path)
    processed = dict(state.get("processed", {}))
    for value in sorted(paths):
        resolved = resolve_path(root, value)
        relative = relative_path(root, resolved)
        if resolved.is_file():
            processed[relative] = sha256(resolved.read_bytes())

    state.update(
        {
            "version": STATE_VERSION,
            "checkpoint": current_head,
            "last_run": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "processed": processed,
        }
    )
    atomic_json_write(state_path, state)
    print(f"Finalised {len(paths)} paths at {current_head}")
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--root", help="Repository root or a path inside it")
    subparsers = result.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create the initial state file")
    init_parser.add_argument("--state", required=True)
    init_parser.add_argument("--checkpoint", default="HEAD")
    init_parser.add_argument("--force", action="store_true")
    init_parser.set_defaults(function=initialise)

    scan_parser = subparsers.add_parser("scan", help="List committed inputs since the checkpoint")
    scan_parser.add_argument("--state", required=True)
    scan_parser.add_argument("--head", default="HEAD")
    scan_parser.add_argument("--output", required=True)
    scan_parser.set_defaults(function=scan)

    finalise_parser = subparsers.add_parser("finalise", help="Record a successful update run")
    finalise_parser.add_argument("--state", required=True)
    finalise_parser.add_argument("--scan", required=True)
    finalise_parser.add_argument("--path", action="append", default=[])
    finalise_parser.set_defaults(function=finalise)
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        return int(args.function(args))
    except TrackerError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
