#!/usr/bin/env python3
"""Append the embedded-research fit line and Problems list to worked Phase 1 profiles."""
import json,os,re
tgt=json.load(open("_state/phase1.json"))
n=0
for r in tgt:
    d=os.path.dirname(r["path"])
    if not os.path.exists(d+"/build.md"): continue
    t=open(r["path"]).read()
    if "Embedded-research fit" in t: continue
    fit=r.get("fit", r.get("es",0))
    slug=d[len("niches/"):]
    titles={}
    for f in ("build","buy","fix"):
        titles[f]=open(f"{d}/{f}.md").readline().lstrip("# ").strip()
    add=(f"\n**Embedded-research fit:** {fit}/45 — qualifies on the delivery-gating rubric; "
         f"see `_embedded-index.md`. The `/60` score above is unchanged.\n"
         f"## Problems\n"
         f"- [[niches/{slug}/build|🔨 Build: {titles['build']}]]\n"
         f"- [[niches/{slug}/buy|🛒 Buy: {titles['buy']}]]\n"
         f"- [[niches/{slug}/fix|🔧 Fix: {titles['fix']}]]\n")
    open(r["path"],"a").write(add); n+=1
print("annotated",n,"profiles")
