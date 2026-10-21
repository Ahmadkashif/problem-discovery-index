"""Compress every industry and sub-niche into a short digest for the lens scorers.

Reads the vault (read-only) and writes one markdown digest per industry into OUT_DIR,
each item headed by an `=== ITEM <id> ===` line, plus batches.json, which deals the
industries round-robin into N_BATCHES mixed batches. Run from the vault root.
"""
import json, os, re, sys
from collections import defaultdict

OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "lenses/_state/digests"
IND_CHARS, SUB_CHARS, N_BATCHES = 1500, 1000, 20


def clean(md):
    md = re.split(r"\n## Problems\b", md)[0]           # drop problem link lists
    md = re.sub(r"\n## Scorecard\n(\|.*\n)+", "\n", md)  # drop pass-2 scorecard tables
    md = re.sub(r"\*\*Parent Industry:\*\*.*\n", "", md)
    md = re.sub(r"\[\[[^|\]]*\|([^\]]*)\]\]", r"\1", md)  # wiki-links -> label
    md = re.sub(r"\n{2,}", "\n", md)
    return md.strip()


def title(md):
    m = re.match(r"#\s+(.*)", md)
    return m.group(1).strip() if m else ""


os.makedirs(OUT_DIR, exist_ok=True)
n_sub, batches, inds = 0, defaultdict(list), []
for ind in sorted(os.listdir("niches")):
    ndir = os.path.join("niches", ind)
    ifile = os.path.join("industries", ind + ".md")
    if not os.path.isdir(ndir) or not os.path.exists(ifile):
        continue
    imd = open(ifile).read()
    parts = [f"=== ITEM {ind} === (industry: {title(imd)})", clean(imd)[:IND_CHARS]]
    subs = 0
    for sub in sorted(os.listdir(ndir)):
        p = os.path.join(ndir, sub, "profile.md")
        if not os.path.exists(p):
            continue
        smd = open(p).read()
        parts += ["", f"=== ITEM {ind}/{sub} === (sub-niche: {title(smd)})", clean(smd)[:SUB_CHARS]]
        subs += 1
    n_sub += subs
    open(os.path.join(OUT_DIR, ind + ".md"), "w").write("\n".join(parts) + "\n")
    inds.append((ind, subs))
for i, (ind, subs) in enumerate(inds):
    batches[f"b{i % N_BATCHES:02d}"].append(ind)
json.dump(batches, open(os.path.join(OUT_DIR, "batches.json"), "w"), indent=1)
print(f"industries={len(inds)} subniches={n_sub} batches={len(batches)}")
