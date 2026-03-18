#!/usr/bin/env python3
"""Validate RSA character limits in a CSV file.

Usage: python validate.py output/rsa_campaign_adgroup_20260314.csv
"""

import csv
import sys

HEADLINE_MAX = 30
DESCRIPTION_MAX = 90
PATH_MAX = 15

def validate(filepath: str) -> bool:
    errors = []
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row_num, row in enumerate(reader, start=2):
            for i in range(1, 16):
                key = f"Headline {i}"
                val = row.get(key, "")
                if val and len(val) > HEADLINE_MAX:
                    errors.append(f"Row {row_num}: {key} = {len(val)} chars (max {HEADLINE_MAX}): \"{val}\"")

            for i in range(1, 5):
                key = f"Description {i}"
                val = row.get(key, "")
                if val and len(val) > DESCRIPTION_MAX:
                    errors.append(f"Row {row_num}: {key} = {len(val)} chars (max {DESCRIPTION_MAX}): \"{val}\"")

            for p in ("Path 1", "Path 2"):
                val = row.get(p, "")
                if val and len(val) > PATH_MAX:
                    errors.append(f"Row {row_num}: {p} = {len(val)} chars (max {PATH_MAX}): \"{val}\"")

    if errors:
        print(f"FAILED — {len(errors)} issue(s):\n")
        for e in errors:
            print(f"  ✗ {e}")
        return False
    else:
        print("PASSED — all character limits OK.")
        return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <csv_file>")
        sys.exit(1)
    ok = validate(sys.argv[1])
    sys.exit(0 if ok else 1)
