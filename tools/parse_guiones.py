#!/usr/bin/env python3
"""Parse fauna short scripts and generate a manifest CSV.

Creates: aidlc-docs/units/guiones/manifest.csv
"""
import re
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FAUNA = ROOT / 'fauna'
OUT_DIR = ROOT / 'aidlc-docs' / 'units' / 'guiones'
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / 'manifest.csv'


def read_text(path: Path) -> str:
    for enc in ('utf-8', 'utf-8-sig', 'cp1252', 'latin-1'):
        try:
            return path.read_text(encoding=enc)
        except Exception:
            continue
    return path.read_text(errors='ignore')


def extract_titles(text: str):
    lines = text.splitlines()
    titles = []
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('titles') or line.strip().lower().startswith('title'):
            j = i + 1
            while j < len(lines):
                s = lines[j].strip()
                if not s:
                    break
                titles.append(s)
                j += 1
            if titles:
                return titles
    # fallback: collect short candidate lines near top
    for line in lines[:30]:
        s = line.strip()
        if s and not s.lower().startswith('short') and 'http' not in s and len(s) < 200:
            titles.append(s)
            if len(titles) >= 3:
                break
    return titles


def extract_media(text: str) -> str:
    m = re.search(r"(\S+\.(?:mp4|mov|mkv|avi))", text, flags=re.IGNORECASE)
    return m.group(1) if m else ''


def count_words(text: str) -> int:
    words = re.findall(r"\w+", text, flags=re.UNICODE)
    return len(words)


def has_link(text: str) -> bool:
    return bool(re.search(r'https?://', text))


def has_youtube(text: str) -> bool:
    t = text.lower()
    return 'youtube.com' in t or 'youtu.be' in t


def has_facebook(text: str) -> bool:
    return 'facebook.com' in text.lower()


def find_files():
    files = set()
    if not FAUNA.exists():
        return []
    for p in FAUNA.rglob('*'):
        if p.is_file() and p.suffix.lower() in ('.txt', '.md') and 'short' in p.name.lower():
            files.add(p)
    return sorted(files)


def main():
    files = find_files()
    rows = []
    for p in files:
        text = read_text(p)
        titles = extract_titles(text)
        primary = titles[0] if titles else ''
        alt_count = max(0, len(titles) - 1)
        wc = count_words(text)
        est_seconds = int(round(wc / 2.5))
        recommended = '30' if wc <= 75 else '60' if wc <= 150 else str(est_seconds)
        yt = has_youtube(text)
        fb = has_facebook(text)
        media = extract_media(text)
        links = has_link(text)
        suggested_titles = ' | '.join(titles[:3])
        rows.append({
            'species': p.parent.name,
            'path': p.as_posix(),
            'file': p.name,
            'primary_title': primary,
            'alt_titles_count': alt_count,
            'suggested_titles': suggested_titles,
            'word_count': wc,
            'estimated_seconds': est_seconds,
            'recommended_duration': recommended,
            'has_youtube': 'yes' if yt else 'no',
            'has_facebook': 'yes' if fb else 'no',
            'has_media': 'yes' if media else 'no',
            'media_filename': media,
            'has_links': 'yes' if links else 'no',
            'notes': '',
        })

    fieldnames = ['species','path','file','primary_title','alt_titles_count','suggested_titles','word_count','estimated_seconds','recommended_duration','has_youtube','has_facebook','has_media','media_filename','has_links','notes']
    with OUT_FILE.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    print(f'Wrote {len(rows)} rows to {OUT_FILE}')


if __name__ == '__main__':
    main()
