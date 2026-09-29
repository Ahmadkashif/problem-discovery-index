#!/usr/bin/env python3
"""Regenerate the CURSOR block in _lineage.md and the ranked table in _builder-index.md
from what is actually on disk.

The cursor is a RENDERED VIEW OF DISK, never an independent counter. If it is lost or
stale, running this reconstructs it exactly. That property is what makes the sweep
resumable and is why a crash mid-batch loses nothing that has been written.

Run from anywhere:  python3 _state/lineage_advance.py
"""
import os, re, glob, datetime, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)

SCOPE = 250
BATCH = 5
WAVE_NAMES = {
    1: "Mainframe & Batch", 2: "Departmental & Item-Level", 3: "PC & the Spreadsheet",
    4: "Client–Server & ERP", 5: "The Commercial Web", 6: "Cloud & SaaS",
    7: "Big Data", 8: "Mobile & GPS", 9: "Programmatic",
    10: "The Creator Platform", 11: "The COVID Dislocation", 12: "Transformers",
}

# ---- the total, deterministic work order: by wave, alphabetical within wave ----
wave = {}
with open("series/_state/wave-assignment.txt") as fh:
    for line in fh:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("|")
        wave[parts[0]] = int(parts[1])

order = sorted(wave, key=lambda s: (wave[s], s))
assert len(order) == SCOPE, f"expected {SCOPE} slugs, got {len(order)}"


def field(text, key):
    m = re.search(r"^\*\*%s:\*\*\s*(.+?)\s*$" % re.escape(key), text, re.M)
    return m.group(1).strip() if m else ""


# ---- read what exists ----
notes = {}
for p in sorted(glob.glob("lineage/*.md")):
    slug = os.path.basename(p)[:-3]
    if slug == "_bookmark":
        continue
    t = open(p, encoding="utf-8").read()
    notes[slug] = {
        "tool": field(t, "The tool"),
        "builder": field(t, "Builder"),
        "in_vault": field(t, "Builder in vault"),
        "verification": field(t, "Verification"),
        "wave": wave.get(slug, 0),
        "words": len(t.split()),
    }

done = [s for s in order if s in notes]
todo = [s for s in order if s not in notes]
ndone = len(done)

# ---- current stage = wave of the next uncompleted industry ----
stage = wave[todo[0]] if todo else 12
stage_slugs = [s for s in order if wave[s] == stage]
stage_done = [s for s in stage_slugs if s in notes]
stage_todo = [s for s in stage_slugs if s not in notes]
nxt = stage_todo[:BATCH]

if not todo:
    status = "COMPLETE — all 250 industries"
elif stage_done:
    status = f"Stage {stage} in progress ({len(stage_done)} of {len(stage_slugs)})"
else:
    status = f"Stage {stage} not started"

cur = " · ".join(f"{s} ✅" for s in stage_done[-BATCH:]) or "—"
nxt_s = " · ".join(nxt) or "—"

cursor = f"""## CURSOR

**Status:** {status}
**Stage:** {stage} of 12 — Wave {stage}, {WAVE_NAMES[stage]}
**Batch size:** {BATCH} industries
**Scope:** {SCOPE} industries, all waves

| | |
|---|---|
| **Completed** | {ndone} of {SCOPE} |
| **Current stage** | W{stage} — {len(stage_done)} of {len(stage_slugs)} done |
| **Recently done** | {cur} |
| **Next up** | {nxt_s} |
| **Order** | By wave (chronological, W1→W12), alphabetical within wave. Position is always recoverable from `ls lineage/`. |
| **Rollup** | See `_builder-index.md` |
| **Last regenerated** | {datetime.date.today().isoformat()} |
"""

d = open("_lineage.md", encoding="utf-8").read()
d2, n = re.subn(r"## CURSOR\n\n.*?(?=\n\*\*To resume:)", cursor, d, flags=re.S)
if n != 1:
    raise SystemExit("CURSOR block not found in _lineage.md — sentinel '**To resume:' missing?")
open("_lineage.md", "w", encoding="utf-8").write(d2)

# ---- the rollup: builders the vault does not own ----
NONE_VALUES = ("no single builder", "unknown")
agg = collections.OrderedDict()
for s in done:
    n_ = notes[s]
    if "ABSENT" not in n_["in_vault"]:
        continue
    b = n_["builder"].strip().strip("*")
    if not b or b.lower().startswith(NONE_VALUES):
        continue
    rec = agg.setdefault(b, {"inds": [], "waves": set()})
    rec["inds"].append(s)
    rec["waves"].add(n_["wave"])

rows = sorted(agg.items(), key=lambda kv: (-len(kv[1]["inds"]), kv[0]))
GATE_INDS, GATE_WAVES = 5, 2
lines, nominated = [], 0
for i, (b, rec) in enumerate(rows, 1):
    ok = len(rec["inds"]) >= GATE_INDS and len(rec["waves"]) >= GATE_WAVES
    nominated += 1 if ok else 0
    waves = ", ".join(f"W{w}" for w in sorted(rec["waves"]))
    lines.append(f"| {i} | {b} | {len(rec['inds'])} | {waves} | `{rec['inds'][0]}` | "
                 f"{'✅' if ok else '—'} |")

unknown = sum(1 for s in done if notes[s]["builder"].lower().startswith("unknown"))
nosingle = sum(1 for s in done if notes[s]["builder"].lower().startswith("no single"))

idx = f"""# Builder Index — Who Built the Tools, and Whether the Vault Owns Them

Regenerated from disk by `_state/lineage_advance.py`. **Never hand-edit.**

**Method and cursor:** `_lineage.md` · **To launch a run:** `Read _lineage-run.md and execute it.`

Every `lineage/<slug>.md` whose `**Builder in vault:**` is `ABSENT` contributes a row here.
A builder named by **≥{GATE_INDS} industries across ≥{GATE_WAVES} waves** is a candidate
`origins/` entry. Below that it is logged and left alone.

> This file is the evidence that replaces a guess. `_assessment.md` proposed six `origins/`
> entries by argument; this table proposes them by count.

---

## Ranked

| # | Builder | Industries demanding it | Waves | First demanded | Nominated? |
|---|---|---|---|---|---|
""" + ("\n".join(lines) if lines else "| — | *no absent builders logged yet* | | | | |") + f"""

---

## Coverage

**Industries swept:** {ndone} of {SCOPE} · **Distinct absent builders:** {len(rows)} · **Nominated:** {nominated}
**Builder unknown:** {unknown} · **No single builder:** {nosingle}

**Last regenerated:** {datetime.date.today().isoformat()}
"""
open("_builder-index.md", "w", encoding="utf-8").write(idx)

print(f"cursor: {ndone}/{SCOPE} done · stage {stage} ({len(stage_done)}/{len(stage_slugs)}) "
      f"· next: {nxt_s}")
print(f"builders: {len(rows)} absent, {nominated} nominated, {unknown} unknown, {nosingle} no-single")
