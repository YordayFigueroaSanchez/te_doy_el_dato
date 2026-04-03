#!/usr/bin/env python3
"""Normalize the top Markdown table in fauna/README.md.

Strategy:
- Detect the table between the first '|' header and the '# Pendiente' section.
- Recombine broken/multi-line rows so each logical row is a single table row.
- Ensure every row has the same number of columns as the header.
- Overflows (extra '|' splits) are merged into the last column.
"""
from pathlib import Path
import sys


README = Path('fauna') / 'README.md'
if not README.exists():
    print('ERROR: fauna/README.md not found')
    sys.exit(1)

text = README.read_text(encoding='utf-8')
lines = text.splitlines()

# Find header start
header_start = None
for i, ln in enumerate(lines):
    if ln.lstrip().startswith('|'):
        header_start = i
        break
if header_start is None:
    print('No table header found, aborting.')
    sys.exit(0)

# Find the end of the table (look for the Pendiente section)
pend_idx = None
for i in range(header_start, len(lines)):
    if lines[i].strip().lower().startswith('# pendiente'):
        pend_idx = i
        break
if pend_idx is None:
    # fallback: first blank line after header block
    for i in range(header_start + 1, len(lines)):
        if lines[i].strip() == '':
            pend_idx = i
            break
    if pend_idx is None:
        pend_idx = len(lines)

block_lines = lines[header_start:pend_idx]
if len(block_lines) < 2:
    print('Table block too small, aborting.')
    sys.exit(0)

header_line = block_lines[0].strip()
# Extract header cells (ignore empty splits)
header_parts = [p.strip() for p in header_line.split('|') if p.strip() != '']
num_cols = len(header_parts)

new_header = '| ' + ' | '.join(header_parts) + ' |'
sep = '| ' + ' | '.join(['---'] * num_cols) + ' |'

# Body is everything after the separator (assume second line is separator)
body_lines = block_lines[2:] if len(block_lines) > 2 else []

rows = []
buf = ''
for ln in body_lines:
    # accumulate into buffer (join broken lines)
    if buf == '':
        buf = ln.rstrip()
    else:
        buf = buf + ' ' + ln.strip()

    tmp = buf.strip()
    if not tmp.startswith('|'):
        tmp = '|' + tmp
    if not tmp.endswith('|'):
        tmp = tmp + '|'

    parts = [p.strip() for p in tmp.split('|')]
    cells = parts[1:-1]

    if len(cells) < num_cols:
        # need more lines to complete this logical row
        continue

    # Merge overflow columns into the last cell
    if len(cells) > num_cols:
        cells = cells[: num_cols - 1] + [' | '.join(cells[num_cols - 1 :])]

    # Pad or trim to exact num_cols
    if len(cells) < num_cols:
        cells = (cells + [''] * num_cols)[:num_cols]
    elif len(cells) > num_cols:
        cells = cells[:num_cols]

    row_line = '| ' + ' | '.join(cells) + ' |'
    rows.append(row_line)
    buf = ''

# handle leftover buffer
if buf:
    tmp = buf.strip()
    if not tmp.startswith('|'):
        tmp = '|' + tmp
    if not tmp.endswith('|'):
        tmp = tmp + '|'
    parts = [p.strip() for p in tmp.split('|')]
    cells = parts[1:-1]
    if cells:
        if len(cells) > num_cols:
            cells = cells[: num_cols - 1] + [' | '.join(cells[num_cols - 1 :])]
        cells = (cells + [''] * num_cols)[:num_cols]
        rows.append('| ' + ' | '.join(cells) + ' |')

new_block = [new_header, sep] + rows
new_lines = lines[:header_start] + new_block + [''] + lines[pend_idx:]
README.write_text('\n'.join(new_lines), encoding='utf-8')
print(f'Wrote normalized table with {len(rows)} rows to {README}')
