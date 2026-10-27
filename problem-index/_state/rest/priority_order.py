"""Owner's priority order for the rest of the run: five industries a day, the ones most useful
for an engineering placement first (see `_short-term-placement-filter.md` § Priority order).

Usage (from the vault root): python3 _state/rest/priority_order.py [--dry-run]
Keeps done rows, the P batches and batch 9b's built rows in place, then writes, in order:
the Q batches; the remaining sector batches sorted by mean placement score (highest first);
the government batches G1..Gn; and batch X, the industries the owner skipped (status blocked).
Row contents are untouched apart from `order`, `batch` and, for SKIP, `status`. Safe to re-run.
"""
import csv, sys, statistics

# 2026-10-27: Q1-Q7, five a day, desk-ranked (each batch is web-checked before its builders).
# Same day the owner said no gambling and no alcohol, which took beverage-alcohol-distributors
# out of Q5, and to put government last, which took courts and highway-contractors out of Q5;
# three Q7 reserves moved up and three new reserves joined Q7.
Q = {
    "Q1": ["renewable-power-producers", "wholesale-auto-auctions", "community-health-centers",
           "parking-operators", "auto-parts-distributors"],
    "Q2": ["sports-teams", "self-storage-operators", "psychiatric-hospitals",
           "consumer-goods-wholesalers", "ambulance-services"],
    "Q3": ["electronic-component-distributors", "air-cargo-carriers", "heavy-equipment-dealers",
           "plastic-molders", "specialty-hospitals"],
    "Q4": ["medical-supply-distributors", "residential-treatment-centers", "aircraft-and-railcar-lessors",
           "biologics-manufacturers", "ltl-carriers"],
    "Q5": ["metal-service-centers", "pcb-fabricators", "manufacturers-reps",
           "aviation-parts-distributors", "fuel-distributors"],
    "Q6": ["auto-salvage-yards", "thrift-and-resale-stores", "transmission-operators",
           "nuclear-power-plants", "cosmetics-manufacturers"],
    "Q7": ["weight-loss-centers", "dental-laboratories", "passenger-airlines",
           "charter-air-operators", "auto-glass-shops"],
}
# Owner, 2026-10-27: "skip casinos and racetracks too, no gambling, no alcohol". Racing stables
# live on wagering-funded purses, so they go with the racetracks. gambling-operators was already
# blocked on 2026-10-24 and stays in batch P4.
SKIP = ["casinos", "racetracks", "racing-stables", "beverage-alcohol-distributors", "liquor-stores",
        "bars-and-taverns", "breweries", "wineries", "distilleries"]
# Owner, 2026-10-27: deprioritise industries that are part of US government or directly serve
# it. Batches 48-49 (public administration) plus public institutions and firms whose customer is
# an agency.
GOV_BATCHES = {"48", "49"}
GOV = ["courts", "community-colleges", "transit-agencies", "airport-operators", "toll-road-operators",
       "highway-contractors", "school-bus-contractors", "youth-group-homes",
       "avionics-and-defense-electronics-makers", "shipyards", "waste-to-energy-plants"]
GOV_BATCH_SIZE = 7
WASTE_UNBUILT = ["waste-to-energy-plants", "recycling-facilities", "septic-service-companies"]

QUE = "_state/rest/queue.tsv"
rows = list(csv.DictReader(open(QUE), delimiter="\t"))
cols = list(rows[0].keys())
by = {r["slug"]: r for r in rows}
score = {r["slug"]: int(r["score"]) for r in csv.DictReader(open("_state/rest/placement-filter.tsv"), delimiter="\t")}

picked = [s for b in Q.values() for s in b]
for s in picked + SKIP + GOV:
    assert s in by, s
assert len(picked) == len(set(picked)), "slug picked twice"
assert not set(picked) & (set(SKIP) | set(GOV)), set(picked) & (set(SKIP) | set(GOV))
for s in SKIP:
    assert by[s]["status"] in ("todo", "blocked"), (s, by[s]["status"])

def fixed(r):
    return r["status"] == "done" or r["batch"].startswith("P") or (r["batch"] == "9b" and r["status"] == "building")

head = [r for r in rows if fixed(r)]
for b, slugs in Q.items():
    for s in slugs:
        if not fixed(by[s]):
            by[s]["batch"] = b
qrows = [by[s] for b in Q for s in Q[b] if not fixed(by[s])]
for s in WASTE_UNBUILT:
    if by[s]["status"] == "todo":
        by[s]["batch"] = "9c"
for s in SKIP:
    by[s]["status"], by[s]["batch"] = "blocked", "X"
seen = {id(r) for r in head + qrows}
xrows = [r for r in rows if r["batch"] == "X" and id(r) not in seen]
gov = [r for r in rows if id(r) not in seen and r["batch"] != "X" and
       (r["slug"] in GOV or r["batch"] in GOV_BATCHES or r["batch"].startswith("G"))]
gov.sort(key=lambda r: (-score[r["slug"]], rows.index(r)))
for i, r in enumerate(gov):
    r["batch"] = f"G{i // GOV_BATCH_SIZE + 1}"
seen |= {id(r) for r in xrows + gov}
tail = [r for r in rows if id(r) not in seen]
groups = {}
for r in tail:
    groups.setdefault(r["batch"], []).append(r)
first = {b: min(rows.index(r) for r in g) for b, g in groups.items()}
mean = {b: statistics.mean(score[r["slug"]] for r in g) for b, g in groups.items()}
order = sorted(groups, key=lambda b: (-mean[b], first[b]))
out = head + qrows + [r for b in order for r in groups[b]] + gov + xrows
assert len(out) == len(rows) and len({r["slug"] for r in out}) == len(rows)
for i, r in enumerate(out, 1):
    r["order"] = str(i)

print(f"head {len(head)} | Q {len(qrows)} | sector tail {len(tail)} in {len(order)} batches | "
      f"government {len(gov)} in G1-G{(len(gov) - 1) // GOV_BATCH_SIZE + 1} | skipped {len(xrows)}")
if "--dry-run" not in sys.argv:
    with open(QUE, "w", newline="") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("QUEUE-REORDERED")
