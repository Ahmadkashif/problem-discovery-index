"""Build the three lens rankings from verified scores.

Usage: python3 lenses/_state/build.py <digests dir> <scores dir>
Run from the vault root. Writes lenses/scores.csv, lenses/ai-proof.md,
lenses/value-clarity.md, lenses/digital-nature.md and lenses/_state/stats.json.
"""
import csv, json, os, re, statistics, sys

DIG, SCO = sys.argv[1], sys.argv[2]
OUT = "lenses"

LENSES = {
    "ai_proof": {"file": "ai-proof.md", "title": "AI-proof ranking", "factors": ["Phys", "Liab", "Trust", "Judg", "Dur"],
                 "why": "why_ai", "order": "Most protected from AI first, most exposed last",
                 "formula": "physical, liability, trust, judgment and durability, each scored 1-5 against a 2031 horizon"},
    "clarity": {"file": "value-clarity.md", "title": "Value clarity ranking", "factors": ["What", "How", "Rep", "Fb"],
                "why": "why_clarity", "order": "Clearest work first, least defined last",
                "formula": "what, how, repetition and feedback, each scored 1-5"},
    "digital": {"file": "digital-nature.md", "title": "Digital nature ranking", "factors": ["In", "Prod", "Deliv", "Buy"],
                "why": "why_digital", "order": "Most digital first, most hands-on last",
                "formula": "input, production, delivery and buying, each scored 1-5"},
}
ANCHORS = {  # from _method.md
    "plumbing-contractors": ([5, 4, 3, 3, 5], [4, 3, 3, 4], [1, 1, 1, 2]),
    "funeral-homes": ([4, 4, 5, 2, 5], [3, 4, 4, 2], [1, 1, 1, 2]),
    "childcare-centers": ([5, 5, 5, 3, 5], [3, 3, 4, 2], [1, 1, 1, 2]),
    "tattoo-studios": ([5, 2, 5, 3, 5], [2, 2, 2, 2], [1, 1, 1, 2]),
    "crop-farming": ([5, 2, 1, 3, 5], [4, 3, 3, 1], [1, 1, 1, 2]),
    "private-equity-firms": ([1, 3, 5, 5, 4], [3, 2, 2, 1], [4, 3, 3, 2]),
    "personal-injury-law": ([1, 5, 4, 4, 4], [4, 3, 3, 2], [4, 4, 3, 2]),
    "penetration-testing-firms": ([1, 3, 3, 4, 4], [3, 3, 3, 3], [5, 5, 5, 5]),
    "software-dev-agencies": ([1, 1, 3, 3, 2], [3, 4, 3, 4], [5, 5, 5, 5]),
    "tax-prep-firms": ([1, 3, 3, 2, 2], [5, 5, 5, 4], [4, 5, 5, 3]),
    "medical-billing": ([1, 2, 2, 2, 2], [5, 4, 5, 4], [5, 5, 5, 4]),
    "seo-tooling-vendors": ([1, 1, 2, 3, 1], [3, 2, 3, 3], [5, 5, 5, 5]),
    "localization-services": ([1, 1, 2, 2, 1], [4, 4, 5, 3], [5, 5, 5, 5]),
    "data-labeling-services": ([1, 1, 1, 2, 2], [5, 5, 5, 4], [5, 5, 5, 5]),
    "tattoo-studios/appointment-deposit-mgmt": ([1, 1, 2, 1, 2], [5, 5, 5, 5], [4, 4, 4, 4]),
    "charter-bus-operators/driver-risk-data-providers": ([1, 3, 2, 2, 4], [4, 4, 5, 3], [5, 5, 5, 5]),
}


def scale(v):
    return round((statistics.mean(v) - 1) / 4 * 100)


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def spearman(a, b):
    def ranks(x):
        order = sorted(range(len(x)), key=lambda i: x[i])
        r = [0.0] * len(x)
        i = 0
        while i < len(x):
            j = i
            while j + 1 < len(x) and x[order[j + 1]] == x[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2 + 1
            i = j + 1
        return r
    ra, rb = ranks(a), ranks(b)
    return round(statistics.correlation(ra, rb), 2)


# names and parents from the digests
names = {}
for f in os.listdir(DIG):
    if f.endswith(".md"):
        for i, kind, name in re.findall(r"^=== ITEM (\S+) === \((industry|sub-niche): (.*)\)$", open(os.path.join(DIG, f)).read(), re.M):
            names[i] = name.strip()

# reviewer corrections override first-pass scores, field by field
fixes = {}
FIX = os.path.join(OUT, "_state", "corrections.jsonl")
if os.path.exists(FIX):
    for line in open(FIX):
        if line.strip():
            c = json.loads(line)
            fixes.setdefault(c["id"], {}).update({k: v for k, v in c.items() if k in LENSES or k.startswith("why_")})

items = []
for f in sorted(os.listdir(SCO)):
    for line in open(os.path.join(SCO, f)):
        if line.strip():
            r = json.loads(line)
            r.update(fixes.get(r["id"], {}))
            r["level"] = "subniche" if "/" in r["id"] else "industry"
            r["industry"] = r["id"].split("/")[0]
            r["name"] = names.get(r["id"], r["id"])
            for k in LENSES:
                r[k + "_score"] = scale(r[k])
            items.append(r)


def link(r):
    if r["level"] == "industry":
        return f"[[industries/{r['id']}|{cell(r['name'])}]]"
    return f"[[niches/{r['id']}/profile|{cell(r['name'])}]]"


def ranked(rows, key):
    rows = sorted(rows, key=lambda r: (-r[key], r["name"]))
    out, prev, rank = [], None, 0
    for n, r in enumerate(rows, 1):
        if r[key] != prev:
            rank, prev = n, r[key]
        out.append((rank, r))
    return out


inds = [r for r in items if r["level"] == "industry"]
subs = [r for r in items if r["level"] == "subniche"]

for k, L in LENSES.items():
    key = k + "_score"
    fac = " | ".join(L["factors"])
    sep = "|".join(["---"] * len(L["factors"]))
    lines = [f"# {L['title']}", "",
             f"{L['order']}. Score 0-100 is the mean of {L['formula']}. Method and anchors: [[lenses/_method|Method]].", "",
             f"## Industries ({len(inds)})", "",
             f"| Rank | Industry | Score | {fac} | Why |", f"|---|---|---|{sep}|---|"]
    for rank, r in ranked(inds, key):
        lines.append(f"| {rank} | {link(r)} | {r[key]} | {' | '.join(map(str, r[k]))} | {cell(r[L['why']])} |")
    lines += ["", f"## Sub-niches ({len(subs)})", "",
              f"| Rank | Sub-niche | Industry | Score | {fac} | Why |", f"|---|---|---|---|{sep}|---|"]
    for rank, r in ranked(subs, key):
        parent = f"[[industries/{r['industry']}|{cell(names.get(r['industry'], r['industry']))}]]"
        lines.append(f"| {rank} | {link(r)} | {parent} | {r[key]} | {' | '.join(map(str, r[k]))} | {cell(r[L['why']])} |")
    open(os.path.join(OUT, L["file"]), "w").write("\n".join(lines) + "\n")

with open(os.path.join(OUT, "scores.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["id", "level", "industry", "name", "ai_proof", "clarity", "digital",
                "physical", "liability", "trust", "judgment", "durability", "what", "how", "repetition", "feedback",
                "input", "production", "delivery", "buying", "why_ai", "why_clarity", "why_digital"])
    for r in sorted(items, key=lambda r: r["id"]):
        w.writerow([r["id"], r["level"], r["industry"], r["name"], r["ai_proof_score"], r["clarity_score"], r["digital_score"],
                    *r["ai_proof"], *r["clarity"], *r["digital"], r["why_ai"], r["why_clarity"], r["why_digital"]])

# stats for the overview
def brief(r):
    return {"id": r["id"], "name": r["name"], "industry": names.get(r["industry"], r["industry"]),
            "ai_proof": r["ai_proof_score"], "clarity": r["clarity_score"], "digital": r["digital_score"],
            "why_ai": r["why_ai"], "why_clarity": r["why_clarity"], "why_digital": r["why_digital"]}

stats = {"n_industries": len(inds), "n_subniches": len(subs)}
for lvl, rows in (("industries", inds), ("subniches", subs)):
    s = stats[lvl] = {}
    for k in LENSES:
        vals = [r[k + "_score"] for r in rows]
        s[k] = {"median": statistics.median(vals), "mean": round(statistics.mean(vals), 1),
                "top": [brief(r) for _, r in ranked(rows, k + "_score")[:15]],
                "bottom": [brief(r) for _, r in ranked(rows, k + "_score")[-15:]]}
    s["rho_clarity_ai_proof"] = spearman([r["clarity_score"] for r in rows], [r["ai_proof_score"] for r in rows])
    s["rho_digital_ai_proof"] = spearman([r["digital_score"] for r in rows], [r["ai_proof_score"] for r in rows])
    s["rho_digital_clarity"] = spearman([r["digital_score"] for r in rows], [r["clarity_score"] for r in rows])

by_id = {r["id"]: r for r in items}
drift = {k: [] for k in LENSES}
for aid, vals in ANCHORS.items():
    if aid in by_id:
        for k, v in zip(LENSES, vals):
            drift[k].append(abs(by_id[aid][k + "_score"] - scale(v)))
stats["anchor_drift"] = {k: {"mean_abs": round(statistics.mean(v), 1), "max": max(v), "n": len(v)} for k, v in drift.items() if v}
json.dump(stats, open(os.path.join(OUT, "_state", "stats.json"), "w"), indent=1, ensure_ascii=False)
print(f"built {len(inds)} industries, {len(subs)} sub-niches; rho(clarity, ai_proof) industries={stats['industries']['rho_clarity_ai_proof']} subniches={stats['subniches']['rho_clarity_ai_proof']}")
