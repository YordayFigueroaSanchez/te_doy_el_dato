#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[2]
report_path = root / 'aidlc-docs' / 'markdownlint-report.json'

ignore_dirs = {'node_modules', '.git', 'aidlc-docs'}

issues = {}

for p in root.rglob('*.md'):
    rel = p.relative_to(root)
    # skip ignored dirs
    if any(part in ignore_dirs for part in rel.parts):
        continue
    try:
        text = p.read_text(encoding='utf-8')
    except Exception:
        text = p.read_text(encoding='utf-8', errors='ignore')
    lines = text.splitlines()
    file_issues = []

    # final newline
    if not text.endswith('\n'):
        file_issues.append({'line': len(lines) or 0, 'rule': 'final-newline', 'message': 'File does not end with a newline'})

    # line length and trailing spaces
    for i, line in enumerate(lines, start=1):
        if len(line) > 120:
            file_issues.append({'line': i, 'rule': 'line-length', 'message': f'Line {i} longer than 120 chars ({len(line)})'})
        if re.search(r'\s+$', line):
            file_issues.append({'line': i, 'rule': 'trailing-space', 'message': 'Trailing whitespace'})

    # consecutive blank lines
    blank_streak = 0
    for i, line in enumerate(lines, start=1):
        if line.strip() == '':
            blank_streak += 1
            if blank_streak > 2:
                file_issues.append({'line': i, 'rule': 'consecutive-blank-lines', 'message': 'More than two consecutive blank lines'})
        else:
            blank_streak = 0

    # title check (first non-empty line should be H1)
    first_non_empty = None
    for i, line in enumerate(lines, start=1):
        if line.strip():
            first_non_empty = (i, line)
            break
    if first_non_empty:
        i, line = first_non_empty
        if not line.strip().startswith('# '):
            file_issues.append({'line': i, 'rule': 'title-h1', 'message': 'First non-empty line is not an H1 header (# )'})

    if file_issues:
        issues[str(rel).replace('\\','/')] = file_issues

report_path.parent.mkdir(parents=True, exist_ok=True)
report_path.write_text(json.dumps(issues, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"Wrote {report_path} with {len(issues)} files containing issues.")
