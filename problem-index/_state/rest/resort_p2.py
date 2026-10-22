"""Re-sort and renumber a Pass 2 table after a coordinator fix. Coordinator only.

Usage: python3 _state/rest/resort_p2.py <slug>
Order: qualifiers first, then scored pockets by score (high to low), then gate failures; numbering restarts at 9.
"""
import re, sys

p = f"niches/{sys.argv[1]}/_overview.md"
lines = open(p).read().split("\n")
i = next(n for n, l in enumerate(lines) if l.startswith("| # | Pocket |"))
j = i + 2
while j < len(lines) and lines[j].startswith("|"):
    j += 1
rows = lines[i + 2:j]

def key(row):
    cells = [c.strip() for c in row.strip("|").split("|")]
    score = re.sub(r"[^0-9]", "", cells[4])
    if "✅" in cells[5]:
        return (0, -int(score))
    if score:
        return (1, -int(score))
    return (2, 0)

rows.sort(key=key)
out = []
for n, row in enumerate(rows, 9):
    cells = row.strip("|").split("|")
    cells[0] = f" {n} "
    out.append("|" + "|".join(cells) + "|")
lines[i + 2:j] = out
open(p, "w").write("\n".join(lines))
print(f"{len(out)} rows re-sorted in {p}")
