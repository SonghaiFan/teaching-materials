#!/usr/bin/env python3
"""
validate_phase1.py — Simple checks for Phase 1 output CSV formatting rules.

Rules validated:
1) Five text columns (Title, City, Country, Tags, Description) are lowercase (ignores exact 'NaN').
2) No XML/JSON tags, emojis, or non-English characters present in any column text.
3) Only valid UTF-8 characters (ASCII letters/digits/punctuation/whitespace) remain in text fields.
4) All null-like values are the string 'NaN'.
5) Integer-like fields (Is_Public, Is_Friend, Is_Family, Farm, Server) have no decimals.

Usage: python validate_phase1.py /path/to/Group<group>_dataset.csv
Exit code: 0 on success; 1 on any violation. Prints first few examples for each violation.
"""
from __future__ import annotations
import sys
import re
import pandas as pd
from pathlib import Path

TARGET_COLUMNS = [
    'Post_ID', 'User_ID', 'Secret', 'Server', 'Title', 'Is_Public', 'Is_Friend', 'Is_Family', 'Farm',
    'City', 'Country', 'Post_Date', 'Taken_Date', 'Tags', 'Latitude', 'Longitude', 'Description', 'Min_Taken_Date'
]
TEXT_COLS = ['Title', 'City', 'Country', 'Tags', 'Description']
INTLIKE = ['Is_Public', 'Is_Friend', 'Is_Family', 'Farm', 'Server']

# same allowlist as notebook
ALLOWED_TEXT = re.compile(r"[^A-Za-z0-9\s\.,;:!\?\-_'\(\)\[\]/&]+")
LOWER_RE = re.compile(r"[A-Z]")
TAG_RE = re.compile(r"<[^>]+>")


def main(path: str) -> int:
    p = Path(path)
    if not p.exists():
        print(f"File not found: {p}")
        return 1

    df = pd.read_csv(p, dtype=str, keep_default_na=False)

    # 0) schema check
    if list(df.columns) != TARGET_COLUMNS:
        print("Schema mismatch\n Expected:",
              TARGET_COLUMNS, "\n Got:", list(df.columns))
        return 1

    ok = True

    # 1) lowercase in five text columns (excluding exact 'NaN')
    for c in TEXT_COLS:
        viol = df[(df[c] != 'NaN') & df[c].str.contains(LOWER_RE, na=False)]
        if not viol.empty:
            ok = False
            print(f"[LOWERCASE] {c}: {len(viol)} rows not lowercase. Example:")
            print(viol[[c]].head(5).to_string(index=False))

    # 2) no tags/emojis/non-English: using the allowlist — anything removed implies presence
    for c in TEXT_COLS:
        series = df[c].fillna('NaN')
        # skip explicit NaN marker
        mask = (series != 'NaN')
        raw = series[mask]
        # tag check
        tags_bad = raw[raw.str.contains(TAG_RE, na=False)]
        if not tags_bad.empty:
            ok = False
            print(f"[TAGS] {c}: found potential tag patterns. Example:")
            print(tags_bad.head(5).to_string(index=False))
        # emoji/non-English check via allowlist
        non_english = raw[raw.str.contains(ALLOWED_TEXT, na=False)]
        if not non_english.empty:
            ok = False
            print(f"[NON-ENGLISH/EMOJI] {c}: found disallowed chars. Example:")
            print(non_english.head(5).to_string(index=False))

    # 3) all nulls represented by 'NaN': check common columns
    # we loaded with dtype=str and keep_default_na=False, so any missing should be exact 'NaN'
    for c in df.columns:
        s = df[c]
        # non-standard nulls: actual NaN, empty string, or case-insensitive 'nan' that isn't exactly 'NaN'
        mask = s.isna() | (s == '') | ((s.str.lower() == 'nan') & (s != 'NaN'))
        if mask.any():
            ok = False
            print(f"[NULLS] {c}: found non-standard null markers. Examples:")
            print(s[mask].head(5).to_string(index=False))

    # 4) integer-like fields must be digits only (or 'NaN')
    for c in INTLIKE:
        vals = df[c].fillna('NaN')
        mask = (vals != 'NaN')
        bad = vals[mask][~vals[mask].str.fullmatch(r"\d+")]
        if not bad.empty:
            ok = False
            print(f"[INTLIKE] {c}: non-integer values present. Example:")
            print(bad.head(5).to_string(index=False))

    if ok:
        print("All Phase 1 formatting rules passed.")
        return 0
    else:
        return 1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_phase1.py /path/to/Group<group>_dataset.csv")
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
