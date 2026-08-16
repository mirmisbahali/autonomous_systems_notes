#!/usr/bin/env python3
"""Regression tests for the deterministic update-notes tools."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRACKER = HERE / "change_tracker.py"
AUDITOR = HERE / "audit_notes.py"


def run(*command: str, cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=check)


class ChangeTrackerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        run("git", "init", "-q", cwd=self.root)
        run("git", "config", "user.email", "test@example.com", cwd=self.root)
        run("git", "config", "user.name", "Update Notes Test", cwd=self.root)
        (self.root / "base.md").write_text("# Base\n", encoding="utf-8")
        run("git", "add", "base.md", cwd=self.root)
        run("git", "commit", "-qm", "base", cwd=self.root)
        run(sys.executable, str(TRACKER), "init", "--state", ".update/state.json", cwd=self.root)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def scan(self, check: bool = True) -> tuple[subprocess.CompletedProcess[str], dict]:
        result = run(
            sys.executable,
            str(TRACKER),
            "scan",
            "--state",
            ".update/state.json",
            "--output",
            "scan.json",
            cwd=self.root,
            check=check,
        )
        return result, json.loads((self.root / "scan.json").read_text(encoding="utf-8"))

    def test_committed_only_and_output_hash(self) -> None:
        (self.root / "rough.md").write_text("rough\n", encoding="utf-8")
        run("git", "add", "rough.md", cwd=self.root)
        run("git", "commit", "-qm", "rough notes", cwd=self.root)
        _, payload = self.scan()
        self.assertEqual(["rough.md"], [item["path"] for item in payload["candidates"]])

        (self.root / "rough.md").write_text("organised\n", encoding="utf-8")
        run(
            sys.executable,
            str(TRACKER),
            "finalise",
            "--state",
            ".update/state.json",
            "--scan",
            "scan.json",
            cwd=self.root,
        )
        run("git", "add", "rough.md", cwd=self.root)
        run("git", "commit", "-qm", "organised output", cwd=self.root)

        _, payload = self.scan()
        self.assertEqual([], payload["candidates"])
        self.assertEqual("recorded-output-unchanged", payload["skipped"][0]["reason"])

    def test_uncommitted_overlap_blocks_finalise(self) -> None:
        (self.root / "rough.md").write_text("committed\n", encoding="utf-8")
        run("git", "add", "rough.md", cwd=self.root)
        run("git", "commit", "-qm", "rough notes", cwd=self.root)
        (self.root / "rough.md").write_text("later local edit\n", encoding="utf-8")
        result, payload = self.scan(check=False)
        self.assertEqual(2, result.returncode)
        self.assertTrue(payload["has_blockers"])
        self.assertEqual("uncommitted-overlap", payload["skipped"][0]["reason"])
        finalise = run(
            sys.executable,
            str(TRACKER),
            "finalise",
            "--state",
            ".update/state.json",
            "--scan",
            "scan.json",
            cwd=self.root,
            check=False,
        )
        self.assertNotEqual(0, finalise.returncode)

    def test_processed_rename_and_deletion_are_ignored(self) -> None:
        (self.root / "rough.md").write_text("rough\n", encoding="utf-8")
        run("git", "add", "rough.md", cwd=self.root)
        run("git", "commit", "-qm", "rough notes", cwd=self.root)
        self.scan()
        run(
            sys.executable,
            str(TRACKER),
            "finalise",
            "--state",
            ".update/state.json",
            "--scan",
            "scan.json",
            cwd=self.root,
        )
        run("git", "mv", "rough.md", "renamed.md", cwd=self.root)
        run("git", "commit", "-qm", "rename", cwd=self.root)
        _, renamed = self.scan()
        self.assertEqual([], renamed["candidates"])
        self.assertEqual("previously-processed-rename", renamed["skipped"][0]["reason"])
        run("git", "rm", "renamed.md", cwd=self.root)
        run("git", "commit", "-qm", "delete", cwd=self.root)
        _, deleted = self.scan()
        self.assertEqual([], deleted["candidates"])
        self.assertTrue(all(item["reason"] == "deleted" for item in deleted["skipped"]))


class AuditorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def concept(self, mastery: int = 0, evidence: str = "[]", status: str = "studied-theoretically") -> str:
        sections = [
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
        ]
        body = "\n".join(f"## {section}\n\nText.\n" for section in sections)
        return f"""---
type: concept
domain: cpp
tags: [\"note/concept\"]
aliases: []
confidence: null
mastery: {mastery}
knowledge_status: {status}
evidence: {evidence}
last_reviewed: null
prerequisites: []
related: []
contrasts: []
examples: []
implemented_in: []
used_by: []
ai_edit: true
---

# Ownership

{body}"""

    def test_valid_concept_and_dashboard(self) -> None:
        (self.root / "Ownership.md").write_text(self.concept(), encoding="utf-8")
        result = run(
            sys.executable,
            str(AUDITOR),
            "--root",
            ".",
            "--dashboard",
            "Dashboard.md",
            cwd=self.root,
        )
        summary = json.loads(result.stdout)
        self.assertEqual(0, summary["errors"])
        self.assertEqual(1, summary["concepts"])
        self.assertIn("[[Ownership|Ownership]]", (self.root / "Dashboard.md").read_text(encoding="utf-8"))

    def test_mastery_above_two_requires_evidence(self) -> None:
        (self.root / "Ownership.md").write_text(
            self.concept(mastery=3, status="independently-implemented"), encoding="utf-8"
        )
        result = run(sys.executable, str(AUDITOR), "--root", ".", cwd=self.root, check=False)
        self.assertEqual(1, result.returncode)
        self.assertEqual(1, json.loads(result.stdout)["errors"])


if __name__ == "__main__":
    unittest.main()
