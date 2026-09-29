#!/usr/bin/env python3
"""Regenerate the Ranked table and Coverage line in _scorecard-index.md from
the Insight Layer profiles on disk. The 'case, per finding' prose is preserved
and renumbered/reordered to match the ranking."""
import re, glob, os, sys

ROOT = "/Users/mac/Desktop/code/personal/problem-index"
os.chdir(ROOT)

SHORT = {
 "accounting-firms-smb":"Accounting","acupuncture-practices":"Acupuncture",
 "alterations-tailoring":"Tailoring","auto-body-shops":"Auto Body",
 "auto-dealers-independent":"Indep. Auto Dealers","auto-repair-shops":"Auto Repair",
 "behavioral-health-clinics":"Behavioral Health","catering-companies":"Catering",
 "charter-bus-operators":"Charter Bus","childcare-centers":"Childcare",
 "chiropractic-practices":"Chiropractic","cleaning-companies":"Cleaning",
 "cloud-infrastructure-consultants":"Cloud Consulting","coffee-shops-independent":"Coffee Shops",
 "cold-chain-logistics":"Cold Chain","collections-agencies":"Collections",
 "commercial-real-estate":"CRE","compliance-consulting":"Compliance Consulting",
 "contract-manufacturing":"Contract Mfg","corporate-training":"Corp Training",
 "credit-unions":"Credit Unions","crop-farming":"Crop Farming",
 "customs-brokers":"Customs Brokerage","cybersecurity-mssp":"Cyber MSSP",
 "data-analytics-consultants":"Data Consulting",
}  # slug -> short industry label

def parse(path):
    t = open(path).read()
    if "**Category:** Insight Layer" not in t:
        return None
    title = re.search(r"^# (.+)$", t, re.M).group(1).strip()
    ind = re.search(r"\*\*Parent Industry:\*\* \[\[industries/([^|\]]+)\|([^\]]+)\]\]", t)
    slug, disp = ind.group(1), ind.group(2)
    size = re.search(r"\*\*Size:\*\* (.+)$", t, re.M)
    size = size.group(1).strip() if size else "?"
    m = re.match(r"^([\d,]+(?:\s*-\s*[\d,]+)?\+?)", size)
    if m: size = m.group(1)
    qs = re.findall(r"\| Q\d [^|]+\| ×\d \| ([\d—-]+) \|", t)
    tot = re.search(r"\*\*Weighted total\*\*\s*\|\s*\|\s*\*\*([\d—-]+)(?:/60)?\*\*", t)
    tot = tot.group(1) if tot else "—"
    verdict = re.search(r"\*\*Verdict:\*\* (.+)$", t, re.M).group(1).strip()
    return dict(path=path, dir=os.path.dirname(path), title=title, slug=slug,
                disp=disp, size=size, qs=qs, total=tot, verdict=verdict)

rows = []
for p in sorted(glob.glob("niches/*/*/profile.md")):
    r = parse(p)
    if r: rows.append(r)

qual = [r for r in rows if r["verdict"].startswith("Qualified")]
qual.sort(key=lambda r: (-int(r["total"]), r["slug"], r["title"]))

below = [r for r in rows if r["verdict"].startswith("Logged — below")]
gate  = [r for r in rows if "fails gate" in r["verdict"]]
other = [r for r in rows if r not in qual and r not in below and r not in gate]

idx = open("_scorecard-index.md").read()

# --- rebuild Ranked table ---
tbl = ["| # | Pocket | Industry | Insight Fn | Q1 | Q2 | Q3 | Q4 | Q5 | Score |",
       "|---|---|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(qual, 1):
    link = f"[[{r['dir']}/profile\\|{r['title']}]]"
    short = SHORT.get(r["slug"], r["disp"])
    tbl.append(f"| {i} | {link} | {short} | {r['size']} | " +
               " | ".join(r["qs"]) + f" | **{r['total']}** |")
tbl = "\n".join(tbl)

idx = re.sub(r"(## Ranked\n\n).*?(\n\n---\n\n## The case)", lambda m: m.group(1)+tbl+m.group(2),
             idx, flags=re.S)

# --- reorder + renumber case sections ---
cases = re.findall(r"### \d+\. (.+?) — (\d+)/60\n(.*?)(?=\n### \d+\. |\n---\n\n## Coverage)", idx, re.S)
cmap = {t: body.rstrip() for t, _s, body in cases}
missing = [r["title"] for r in qual if r["title"] not in cmap]
newcases = []
for i, r in enumerate(qual, 1):
    if r["title"] in cmap:
        newcases.append(f"### {i}. {r['title']} — {r['total']}/60\n{cmap[r['title']]}")
if newcases:
    block = "\n\n".join(newcases) + "\n"
    idx = re.sub(r"(## The case, per finding\n\n).*?(\n---\n\n## Coverage)",
                 lambda m: m.group(1)+block+m.group(2), idx, flags=re.S)

# --- coverage ---
swept = len({r["slug"] for r in rows})
cov = (f"**Industries swept:** {swept} of 118 · **Pockets logged:** {len(rows)} · "
       f"**Qualified:** {len(qual)} · **Below threshold:** {len(below)+len(other)} · "
       f"**Failed gate:** {len(gate)}")
idx = re.sub(r"\*\*Industries swept:\*\*.*", cov, idx)

open("_scorecard-index.md","w").write(idx)
print(f"swept={swept} logged={len(rows)} qual={len(qual)} below={len(below)+len(other)} gate={len(gate)}")
if missing: print("MISSING CASE PROSE:", missing)
