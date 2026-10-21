"""Check lens scores against the digests: every item scored once, every factor an int 1-5.

Usage: python3 lenses/_state/verify.py <digests dir> <scores dir>
Prints VERIFY-CLEAN, or one line per problem.
"""
import json, os, re, sys

DIG, SCO = sys.argv[1], sys.argv[2]
SHAPE = {"ai_proof": 5, "clarity": 4, "digital": 4}
WHY = ("why_ai", "why_clarity", "why_digital")
problems, total = [], 0

for f in sorted(os.listdir(DIG)):
    if not f.endswith(".md"):
        continue
    ind = f[:-3]
    want = re.findall(r"^=== ITEM (\S+) ===", open(os.path.join(DIG, f)).read(), re.M)
    path = os.path.join(SCO, ind + ".jsonl")
    if not os.path.exists(path):
        problems.append(f"{ind}: no scores file")
        continue
    got = []
    for n, line in enumerate(open(path), 1):
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError as e:
            problems.append(f"{ind}:{n}: bad JSON ({e.msg})")
            continue
        got.append(r.get("id"))
        for k, size in SHAPE.items():
            v = r.get(k)
            if not (isinstance(v, list) and len(v) == size and all(isinstance(x, int) and 1 <= x <= 5 for x in v)):
                problems.append(f"{ind}:{n}: {r.get('id')} bad {k} {v}")
        for k in WHY:
            if not str(r.get(k, "")).strip():
                problems.append(f"{ind}:{n}: {r.get('id')} missing {k}")
    for i in sorted(set(want) - set(got)):
        problems.append(f"{ind}: missing {i}")
    for i in sorted(set(got) - set(want)):
        problems.append(f"{ind}: unknown id {i}")
    dupes = {i for i in got if got.count(i) > 1}
    for i in sorted(dupes):
        problems.append(f"{ind}: duplicate {i}")
    total += len(want)

print("\n".join(problems) if problems else f"VERIFY-CLEAN ({total} items)")
sys.exit(1 if problems else 0)
