"""Set queue.tsv status for slugs or a whole batch. Coordinator only.

Usage: python3 _state/rest/set_status.py <status> --batch N
       python3 _state/rest/set_status.py <status> slug [slug ...]
"""
import csv, sys

status, args = sys.argv[1], sys.argv[2:]
assert status in {"todo", "building", "done", "blocked"}, status
path = "_state/rest/queue.tsv"
rows = list(csv.reader(open(path), delimiter="\t"))
head, body = rows[0], rows[1:]
if args[:1] == ["--batch"]:
    pick = lambda r: r[1] == args[1]
else:
    want = set(args)
    pick = lambda r: r[2] in want
n = 0
for r in body:
    if pick(r):
        r[6] = status
        n += 1
with open(path, "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar=None)
    w.writerows([head] + body)
print(f"{n} rows -> {status}")
