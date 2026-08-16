#!/usr/bin/env python3
"""Synchronise the skill's canonical templates into the visible Obsidian folder."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Vault root")
    parser.add_argument("--target", default="99_templates", help="Vault-relative template folder")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    source = Path(__file__).resolve().parent.parent / "assets" / "templates"
    target = root / args.target
    if not source.is_dir():
        parser.error(f"Template source does not exist: {source}")
    target.mkdir(parents=True, exist_ok=True)

    copied = 0
    for template in sorted(source.glob("*.md")):
        destination = target / template.name
        content = template.read_bytes()
        if not destination.exists() or destination.read_bytes() != content:
            destination.write_bytes(content)
            copied += 1
    print(f"Synchronised {len(list(source.glob('*.md')))} templates ({copied} changed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
