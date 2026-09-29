#!/usr/bin/env python3
"""Regenerate the CURSOR block in _direction.md and the Completed/Queue in
niches/_bookmark.md from what is actually on disk."""
import re, glob, os, collections
ROOT="/Users/mac/Desktop/code/personal/problem-index"; os.chdir(ROOT)
SCOPE=118; BATCH=5

order=[os.path.basename(p)[:-3] for p in sorted(glob.glob("industries/*.md"))][:SCOPE]
cnt=collections.Counter(); qual=collections.Counter(); below=collections.Counter(); gate=collections.Counter()
for p in glob.glob("niches/*/*/profile.md"):
    t=open(p).read()
    if "**Category:** Insight Layer" not in t: continue
    slug=p.split("/")[1]; cnt[slug]+=1
    v=re.search(r"\*\*Verdict:\*\* (.+)$",t,re.M).group(1)
    (qual if v.startswith("Qualified") else gate if "fails gate" in v else below)[slug]+=1
done=[s for s in order if cnt[s]]
nxt=[s for s in order if not cnt[s]]
files=collections.Counter()
for d in glob.glob("niches/*/*/profile.md"):
    if "**Category:** Insight Layer" in open(d).read():
        files[d.split("/")[1]]+=len(os.listdir(os.path.dirname(d)))

batches=[order[i:i+BATCH] for i in range(0,len(order),BATCH)]
cur_i=min(len(done)//BATCH, len(batches)-1)
if done and len(done)%BATCH==0: cur_i=min(len(done)//BATCH, len(batches)-1)
def render(b): return " · ".join(f"{s} ✅" if cnt[s] else s for s in b)

done_in_cur = [s for s in batches[cur_i] if cnt[s]]
if not nxt:
    status = "complete"
elif not done_in_cur:
    status = f"Batch {cur_i} complete — batch {cur_i+1} not started"
else:
    status = f"Batch {cur_i+1} in progress ({len(done_in_cur)} of {len(batches[cur_i])})"
cursor=f"""## CURSOR

**Status:** {status}
**Batch size:** {BATCH} industries
**Scope:** {SCOPE} industries

| | |
|---|---|
| **Completed** | {len(done)} of {SCOPE} — {', '.join(f'`{s}` ({cnt[s]})' for s in done)} |
| **Current batch ({cur_i+1})** | {render(batches[cur_i])} |
| **Next batch ({cur_i+2})** | {render(batches[cur_i+1]) if cur_i+1 < len(batches) else '—'} |
| **Order** | Alphabetical by `ls industries/`, so position is always recoverable |
| **Index entries so far** | See `_scorecard-index.md` |
"""
d=open("_direction.md").read()
d=re.sub(r"## CURSOR\n\n.*?(?=\n\*\*To resume:)", cursor, d, flags=re.S)
open("_direction.md","w").write(d)

lines=[]
for i,b in enumerate(batches):
    got=[s for s in b if cnt[s]]
    if not got: continue
    lines.append(f"**Batch {i+1}:**")
    for s in got:
        lines.append(f"- **{s}** — {cnt[s]} pockets ({qual[s]} qualified, {below[s]} below threshold, {gate[s]} failed gate), {files[s]} files")
    lines.append("")
q=[]
rem=[s for s in batches[cur_i] if not cnt[s]]
if rem:
    label = "not started" if len(rem) == len(batches[cur_i]) else "remaining"
    q.append(f"**Batch {cur_i+1} ({label}):** {', '.join(rem)}")
if cur_i+1<len(batches): q.append(f"**Batch {cur_i+2}:** {', '.join(batches[cur_i+1])}")
if not q: q.append("(none — scope complete)")
bm=open("niches/_bookmark.md").read()
bm=re.sub(r"## Completed\n\*\*Batch 1.*?(?=\Z)", "## Completed\n"+"\n".join(lines).rstrip()+
          "\n\n## In Progress\n- (none)\n\n## Queue\n"+"\n".join(q)+"\n", bm, flags=re.S)
open("niches/_bookmark.md","w").write(bm)
print(f"done={len(done)} remaining_in_scope={len(nxt)} status={status}")
