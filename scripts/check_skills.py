#!/usr/bin/env python3
"""Check that every skills/<name>/ folder has a valid SKILL.md (name + description)."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RESERVED = {"synced", "anthropic-skills"}


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields, key = {}, None
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            key = m.group(1)
            fields[key] = m.group(2).strip().strip("\"'")
        elif key and line.startswith((" ", "\t")):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def check(folder):
    errors = []
    skill = folder / "SKILL.md"
    if not skill.is_file():
        return [f"{folder.name}: missing SKILL.md"]
    fm = frontmatter(skill.read_text(encoding="utf-8"))
    if fm is None:
        return [f"{folder.name}: SKILL.md must start with --- frontmatter ---"]
    text = skill.read_text(encoding="utf-8")
    for n, line in enumerate(text.splitlines(), 1):
        if re.search(r"(?<!\\)\$[0-9]", line):
            errors.append(f"{folder.name}/SKILL.md:{n}: '$' + digit gets replaced with an argument; write \\$ or rephrase (e.g. '300 dollars')")
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name:
        errors.append(f"{folder.name}: frontmatter needs a name")
    elif name != folder.name:
        errors.append(f"{folder.name}: name '{name}' should match the folder name")
    if name and (not NAME_RE.match(name) or len(name) > 64):
        errors.append(f"{folder.name}: name must be lowercase letters, numbers and dashes (max 64)")
    if folder.name in RESERVED:
        errors.append(f"{folder.name}: that folder name is reserved")
    if not desc:
        errors.append(f"{folder.name}: frontmatter needs a description")
    elif len(desc) > 1024:
        errors.append(f"{folder.name}: description is {len(desc)} chars (max 1024)")
    return errors


def main():
    folders = sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith("."))
    errors = [e for f in folders for e in check(f)]
    stray = [p.name for p in ROOT.iterdir() if p.is_file() and p.name != ".gitkeep"]
    errors += [f"{s}: put skills in their own folder, skills/<name>/SKILL.md" for s in stray]
    for e in errors:
        print(f"x {e}")
    if errors:
        sys.exit(1)
    print(f"ok: {len(folders)} skills look good :)")


if __name__ == "__main__":
    main()
