#!/usr/bin/env python3
"""Recreate client skill-folder symlinks from this unified skill library."""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path


LIBRARY_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = LIBRARY_ROOT / "manifest.json"
SOURCE_ROOTS = {
    "codex": Path.home() / ".codex" / "skills",
    "agents": Path.home() / ".agents" / "skills",
    "claude": Path.home() / ".claude" / "skills",
}


def target_from_manifest_path(path: str) -> Path:
    marker = "/skill-library/"
    if marker not in path:
        raise ValueError(f"Target is not inside skill-library: {path}")
    relative = path.split(marker, 1)[1]
    return LIBRARY_ROOT / relative


def replace_with_symlink(link_path: Path, target: Path) -> None:
    if not target.exists() or not (target / "SKILL.md").is_file():
        raise FileNotFoundError(f"Missing skill target: {target}")
    link_path.parent.mkdir(parents=True, exist_ok=True)
    if link_path.exists() or link_path.is_symlink():
        if link_path.is_symlink() or link_path.is_file():
            link_path.unlink()
        else:
            shutil.rmtree(link_path)
    os.symlink(str(target), str(link_path), target_is_directory=True)


def main() -> int:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    changed = 0
    for record in manifest["records"]:
        source = record["source"]
        skill_name = record["name"]
        root = SOURCE_ROOTS[source]
        target = target_from_manifest_path(record["central_target"])
        replace_with_symlink(root / skill_name, target)
        changed += 1
    print(f"Recreated {changed} skill links from {LIBRARY_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

