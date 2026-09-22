#!/usr/bin/env python3
"""Install the persona-luoxiang skill bundle into a DSH skill root.

Distilly's own installer copies only a self-contained SKILL.md and renames the
installed command from the engine's canonical name (celebrity-luoxiang). This
skill is meant to keep its resources (`references/research/`, `knowledge/`) and
its own command name, so it is installed as a folder bundle instead.

DSH discovers folder bundles only at depth 1: <root>/<name>/SKILL.md.

Usage:
    python install_to_dsh.py [--skills-dir <dir>] [--force] [--dry-run]

Default target: <workspace>/.agents/skills/persona-luoxiang
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

SKILL_NAME = "persona-luoxiang"
EXCLUDED_TOP_LEVEL = {".build", "versions", "__pycache__"}
REQUIRED_FILES = ("SKILL.md", "skill.yaml", "README.md")


def find_workspace_root(start: Path) -> Path:
    """Walk up to the nearest ancestor containing .agents or .dsh, else use start."""
    for candidate in (start, *start.parents):
        if (candidate / ".agents").is_dir() or (candidate / ".dsh").is_dir():
            return candidate
    return start


def copy_bundle(source: Path, target: Path) -> list[str]:
    copied: list[str] = []
    target.mkdir(parents=True, exist_ok=True)
    for entry in sorted(source.iterdir()):
        if entry.name in EXCLUDED_TOP_LEVEL:
            continue
        destination = target / entry.name
        if entry.is_dir():
            shutil.copytree(entry, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(entry, destination)
        copied.append(entry.name)
    return copied


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", default=None, help="Override the DSH skill root")
    parser.add_argument("--force", action="store_true", help="Replace an existing install")
    parser.add_argument("--dry-run", action="store_true", help="Resolve paths without writing")
    args = parser.parse_args()

    source = Path(__file__).resolve().parent.parent
    missing = [name for name in REQUIRED_FILES if not (source / name).exists()]
    if missing:
        print(f"refusing to install: missing {', '.join(missing)} in {source}")
        return 2

    workspace = find_workspace_root(source)
    skills_root = (
        Path(args.skills_dir).expanduser().resolve()
        if args.skills_dir
        else workspace / ".agents" / "skills"
    )
    target = skills_root / SKILL_NAME

    print(f"source:      {source}")
    print(f"skills root: {skills_root}")
    print(f"target:      {target}")

    if args.dry_run:
        print("dry run: nothing written")
        return 0

    if target.exists():
        if not args.force:
            print("target already exists; re-run with --force to replace it")
            return 1
        shutil.rmtree(target)

    copied = copy_bundle(source, target)
    (target / ".dsh-install.json").write_text(
        json.dumps(
            {
                "host": "deepseek-harness",
                "skill_id": "persona_luoxiang",
                "command_name": SKILL_NAME,
                "version": "1.0.0",
                "source_skill_dir": str(source),
                "installed_at": datetime.now(timezone.utc).isoformat(),
                "discovery": "folder bundle at <root>/<name>/SKILL.md, depth 1 only",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"installed {len(copied)} entries: {', '.join(copied)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())