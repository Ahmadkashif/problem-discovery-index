"""Stage 0 check: every remaining NAICS code is triaged once, and the queue matches the triage.

Usage (from the vault root): python3 _state/rest/check_queue.py [rest.md] [triage.tsv] [queue.tsv]
Prints QUEUE-CLEAN, or one line per problem.
"""
import csv, os, re, sys, collections

REST = sys.argv[1] if len(sys.argv) > 1 else "_rest-of-the-industries.md"
TRI = sys.argv[2] if len(sys.argv) > 2 else "_state/rest/naics-triage.tsv"
QUE = sys.argv[3] if len(sys.argv) > 3 else "_state/rest/queue.tsv"
BASE = set(open("_state/rest/baseline-industries.txt").read().split())
CATS = {"Agriculture & Food", "Mining & Extraction", "Utilities & Energy", "Construction & Trades",
        "Manufacturing & Industrial", "Wholesale & Distribution", "Retail & E-Commerce",
        "Transportation & Logistics", "Media, Telecom & Information", "Financial Services", "Insurance",
        "Real Estate, Rental & Leasing", "Professional Services", "Holding & Management Companies",
        "Business Support & Waste Services", "Education", "Healthcare & Clinical", "Social Assistance",
        "Arts, Entertainment & Recreation", "Hospitality & Food Service", "Specialty Services",
        "Nonprofit & Government"}
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
bad = []

text = open(REST).read().split("## Already covered")[0]
rest = dict(re.findall(r"^\| (\d{6}) \| (.*?) \| `", text, re.M))

if not os.path.exists(TRI):
    sys.exit(f"NO-TRIAGE {TRI}: run Stage 0.1 first")
rows = list(csv.DictReader(open(TRI), delimiter="\t"))
seen = collections.Counter(r["naics"] for r in rows)
for c in sorted(set(rest) - set(seen)):
    bad.append(f"UNTRIAGED {c} {rest[c]}")
for c, n in seen.items():
    if n > 1:
        bad.append(f"TRIAGED-{n}-TIMES {c}")
    if c not in rest:
        bad.append(f"NOT-IN-REST-FILE {c}")
codes = collections.defaultdict(set)
primary = collections.Counter()
for r in rows:
    c, d, s, why = r["naics"], r["decision"], r["slug"].strip(), r["reason"].strip()
    if d not in {"new", "merge", "covered", "skip"}:
        bad.append(f"BAD-DECISION {c} {d!r}")
        continue
    if d != "new" and not why:
        bad.append(f"NO-REASON {c} ({d})")
    if d == "skip":
        continue
    if not s:
        bad.append(f"NO-SLUG {c} ({d})")
        continue
    if d == "covered":
        if s not in BASE:
            bad.append(f"COVERED-BY-UNKNOWN {c} {s}")
        continue
    if s in BASE:
        bad.append(f"SLUG-COLLIDES-WITH-EXISTING {c} {s}")
    if not SLUG.match(s) or len(s) > 40:
        bad.append(f"BAD-SLUG {c} {s}")
    codes[s].add(c)
    primary[s] += d == "new"
for s in codes:
    if primary[s] != 1:
        bad.append(f"SLUG-NEEDS-ONE-NEW-ROW {s} (has {primary[s]})")

if not os.path.exists(QUE):
    bad.append(f"NO-QUEUE {QUE}")
else:
    q = list(csv.DictReader(open(QUE), delimiter="\t"))
    want_cols = ["order", "batch", "slug", "name", "category", "naics", "status", "boundary"]
    if q and list(q[0].keys()) != want_cols:
        bad.append(f"QUEUE-COLUMNS {list(q[0].keys())} (want {want_cols})")
    qs = collections.Counter(r["slug"] for r in q)
    for s in sorted(set(codes) - set(qs)):
        bad.append(f"NOT-QUEUED {s}")
    for s in sorted(set(qs) - set(codes)):
        bad.append(f"QUEUED-NOT-TRIAGED {s}")
    for s, n in qs.items():
        if n > 1:
            bad.append(f"QUEUED-{n}-TIMES {s}")
    orders = [r["order"] for r in q]
    if orders != [str(i) for i in range(1, len(q) + 1)]:
        bad.append("ORDER-NOT-1..N")
    for r in q:
        s = r["slug"]
        got = {x.strip() for x in r["naics"].split(",") if x.strip()}
        if s in codes and got != codes[s]:
            bad.append(f"NAICS-MISMATCH {s} queue={sorted(got)} triage={sorted(codes[s])}")
        if r["category"] not in CATS:
            bad.append(f"BAD-CATEGORY {s} {r['category']!r}")
        if r["status"] not in {"todo", "building", "done", "blocked"}:
            bad.append(f"BAD-STATUS {s} {r['status']!r}")
        if not r["name"].strip() or not r["boundary"].strip() or not r["batch"].strip():
            bad.append(f"EMPTY-FIELD {s}")
    tally = collections.Counter(r["decision"] for r in rows)
    print(f"codes {len(rest)} | triaged {len(seen)} | new {tally['new']} merge {tally['merge']} "
          f"covered {tally['covered']} skip {tally['skip']} | queue {len(q)} industries, "
          f"{sum(r['status'] == 'done' for r in q)} done")
print("\n".join(bad) if bad else "QUEUE-CLEAN")
sys.exit(1 if bad else 0)
