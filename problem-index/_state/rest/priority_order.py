"""Owner's priority order for the rest of the run (2026-10-27): five industries a day, the ones
most useful for an engineering placement first (see `_short-term-placement-filter.md`).

Usage (from the vault root): python3 _state/rest/priority_order.py [--dry-run]
Puts the Q batches right after the done rows and batch 9b's three built rows, moves 9b's three
unbuilt rows to batch 9c, and sorts the remaining sector batches by their mean placement score
(highest first). Row contents are untouched; only `order` and `batch` change.
"""
import csv, sys, statistics

Q = {
    "Q1": ["renewable-power-producers", "wholesale-auto-auctions", "community-health-centers",
           "parking-operators", "auto-parts-distributors"],
    "Q2": ["sports-teams", "self-storage-operators", "psychiatric-hospitals",
           "consumer-goods-wholesalers", "ambulance-services"],
    "Q3": ["electronic-component-distributors", "air-cargo-carriers", "heavy-equipment-dealers",
           "plastic-molders", "specialty-hospitals"],
    "Q4": ["medical-supply-distributors", "residential-treatment-centers", "aircraft-and-railcar-lessors",
           "biologics-manufacturers", "ltl-carriers"],
    "Q5": ["beverage-alcohol-distributors", "metal-service-centers", "pcb-fabricators", "courts",
           "highway-contractors"],
    "Q6": ["auto-salvage-yards", "thrift-and-resale-stores", "transmission-operators",
           "nuclear-power-plants", "cosmetics-manufacturers"],
    "Q7": ["manufacturers-reps", "aviation-parts-distributors", "fuel-distributors",
           "weight-loss-centers", "dental-laboratories"],
}
WASTE_UNBUILT = ["waste-to-energy-plants", "recycling-facilities", "septic-service-companies"]

QUE = "_state/rest/queue.tsv"
rows = list(csv.DictReader(open(QUE), delimiter="\t"))
cols = list(rows[0].keys())
by = {r["slug"]: r for r in rows}
score = {r["slug"]: int(r["score"]) for r in csv.DictReader(open("_state/rest/placement-filter.tsv"), delimiter="\t")}

picked = [s for b in Q.values() for s in b]
assert len(picked) == len(set(picked)), "slug picked twice"
for s in picked:
    assert s in by, s
    assert by[s]["status"] == "todo", (s, by[s]["status"])

head = [r for r in rows if r["status"] in ("done", "blocked") or (r["batch"] == "9b" and r["status"] == "building")]
for b, slugs in Q.items():
    for s in slugs:
        by[s]["batch"] = b
qrows = [by[s] for b in Q for s in Q[b]]
for s in WASTE_UNBUILT:
    if by[s]["status"] == "todo":
        by[s]["batch"] = "9c"
seen = {id(r) for r in head + qrows}
tail = [r for r in rows if id(r) not in seen]
groups = {}
for r in tail:
    groups.setdefault(r["batch"], []).append(r)
first = {b: min(rows.index(r) for r in g) for b, g in groups.items()}
mean = {b: statistics.mean(score[r["slug"]] for r in g) for b, g in groups.items()}
order = sorted(groups, key=lambda b: (-mean[b], first[b]))
out = head + qrows + [r for b in order for r in groups[b]]
assert len(out) == len(rows) and len({r["slug"] for r in out}) == len(rows)
for i, r in enumerate(out, 1):
    r["order"] = str(i)

for b in order:
    print(f"{b:>3} {len(groups[b]):>2} mean {mean[b]:.1f} {groups[b][0]['category']}")
if "--dry-run" not in sys.argv:
    with open(QUE, "w", newline="") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("QUEUE-REORDERED")
