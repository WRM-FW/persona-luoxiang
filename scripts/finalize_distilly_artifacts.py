#!/usr/bin/env python3
"""Reconcile Distilly's generated metadata with this skill's canonical identity.

Distilly's writer derives some fields from its own conventions:

* `lifecycle.version` is forced to `v1` and mirrored into the legacy top-level
  `version`, even when a version is supplied through the input meta.
* artifact command names stay `<character>-<slug>` (`celebrity-luoxiang`).
* the manifest's artifact list only names Distilly's primary artifact set.

This project's canonical identity is Skill ID `persona_luoxiang`, name
`LuoXiang`, version `1.0.0`, DSH command `persona-luoxiang`. This script applies
that identity to `meta.json` and `manifest.json` without touching `work.md`,
`persona.md` or `SKILL.md` content.

Usage:
    python finalize_distilly_artifacts.py <skill_dir>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SKILL_ID = "persona_luoxiang"
DISPLAY_NAME = "LuoXiang"
VERSION = "1.0.0"
COMMAND = "persona-luoxiang"

EXTRA_ARTIFACTS = [
    "skill.yaml",
    "README.md",
    "work_skill.md",
    "persona_skill.md",
    "references/research",
    "knowledge/research/merged/summary.md",
]


def patch_meta(skill_dir: Path) -> list[str]:
    path = skill_dir / "meta.json"
    meta = json.loads(path.read_text(encoding="utf-8"))
    changes: list[str] = []

    def set_field(container: dict, key: str, value: object, label: str) -> None:
        if container.get(key) != value:
            container[key] = value
            changes.append(label)

    set_field(meta, "version", VERSION, f"meta.version -> {VERSION}")
    set_field(meta, "id", SKILL_ID, f"meta.id -> {SKILL_ID}")
    set_field(meta, "display_name", DISPLAY_NAME, f"meta.display_name -> {DISPLAY_NAME}")
    set_field(meta, "name", DISPLAY_NAME, f"meta.name -> {DISPLAY_NAME}")

    lifecycle = meta.setdefault("lifecycle", {})
    set_field(lifecycle, "version", VERSION, f"meta.lifecycle.version -> {VERSION}")

    artifacts = meta.setdefault("artifacts", {})
    for key, value in (
        ("combined_name", COMMAND),
        ("work_name", f"{COMMAND}-work"),
        ("persona_name", f"{COMMAND}-persona"),
    ):
        set_field(artifacts, key, value, f"meta.artifacts.{key} -> {value}")

    path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changes


def patch_manifest(skill_dir: Path) -> list[str]:
    path = skill_dir / "manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    changes: list[str] = []

    def set_field(container: dict, key: str, value: object, label: str) -> None:
        if container.get(key) != value:
            container[key] = value
            changes.append(label)

    set_field(manifest, "id", SKILL_ID, f"manifest.id -> {SKILL_ID}")
    set_field(manifest, "display_name", DISPLAY_NAME, f"manifest.display_name -> {DISPLAY_NAME}")
    set_field(manifest, "version", VERSION, f"manifest.version -> {VERSION}")
    set_field(manifest, "skill_id_alias", "persona_luoxiang", "manifest.skill_id_alias added")

    entrypoints = manifest.setdefault("entrypoints", {})
    if isinstance(entrypoints, dict):
        for key, value in entrypoints.items():
            if isinstance(value, str) and value.startswith("celebrity-luoxiang"):
                entrypoints[key] = value.replace("celebrity-luoxiang", COMMAND)
                changes.append(f"manifest.entrypoints.{key} -> {entrypoints[key]}")

    artifacts = manifest.get("artifacts")
    if isinstance(artifacts, list):
        for name in EXTRA_ARTIFACTS:
            if name not in artifacts:
                artifacts.append(name)
                changes.append(f"manifest.artifacts += {name}")

    install = manifest.get("install")
    if isinstance(install, dict):
        commands = install.get("slash_commands")
        if isinstance(commands, dict):
            for key, value in list(commands.items()):
                if isinstance(value, str) and value.startswith("celebrity-luoxiang"):
                    commands[key] = value.replace("celebrity-luoxiang", COMMAND)
                    changes.append(f"manifest.install.slash_commands.{key} -> {commands[key]}")
        install.setdefault(
            "dsh_discovery",
            "<projectRoot>/.agents/skills/persona-luoxiang/SKILL.md (folder bundle, depth 1)",
        )

    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changes


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    skill_dir = Path(argv[0]).expanduser()
    if not (skill_dir / "meta.json").exists():
        print(f"meta.json not found in {skill_dir}")
        return 1
    for change in patch_meta(skill_dir) + patch_manifest(skill_dir):
        print(f"patched {change}")
    print(f"identity reconciled in {skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))