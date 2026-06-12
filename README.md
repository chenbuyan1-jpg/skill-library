# Skill Library

This is the unified skill library for this machine.

- `skills/`: shared skills with one canonical copy.
- `variants/<source>/`: same-name skills that differ between Codex, Claude, or agents, preserved separately so existing behavior does not change.
- `manifest.json`: source paths, link targets, hashes, and counts.

Original client directories are expected to contain symlinks back to this library:

- Codex: `/Users/chenbuyan/.codex/skills`
- Claude: `/Users/chenbuyan/.claude/skills`
- Agents: `/Users/chenbuyan/.agents/skills`

Created: 2026-06-12 11:08:11

## Counts

- Skill records across source roots: 203
- Unique skill names: 148
- Shared canonical skills: 131
- Source-specific variant skills: 35

## Migration

To back up or move machines, put this whole `skill-library` directory in GitHub or copy it to the new computer, then run:

```bash
python3 scripts/relink_from_library.py
```

The script recreates links in:

- `~/.codex/skills`
- `~/.claude/skills`
- `~/.agents/skills`

It uses this library's current location, so it can run from a different username or machine path after cloning.
