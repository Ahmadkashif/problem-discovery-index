import json,os,re,glob,collections
D="_state"
rows=[]
for p in glob.glob("niches/*/*/profile.md"):
    t=open(p).read()
    if "**Category:** Insight Layer" not in t: continue
    name=t.split("\n")[0].lstrip("# ").strip(); ind=p.split("/")[1]
    q={}
    for k,lab in [(1,"Insight is the invoice"),(2,"Labor mass"),(3,"Proprietary data"),(4,"External clock"),(5,"Buyer \\+ market")]:
        m=re.search(r"\| Q%d %s[^|]*\|[^|]*\| (\d) \|"%(k,lab),t); q[k]=int(m.group(1)) if m else None
    if any(v is None for v in q.values()): continue
    ks=re.search(r"\*\*Kill switches:\*\* ([^\n]+)",t); ks=ks.group(1) if ks else ""
    v=re.search(r"\*\*Verdict:\*\* ([^\n]+)",t); v=v.group(1) if v else ""
    fn=re.search(r"\*\*Size:\*\* ([^\n]+)",t); fn=fn.group(1) if fn else ""
    tot=re.search(r"\*\*Weighted total\*\*.*?\*\*(\d+|—)/60\*\*",t)
    rows.append(dict(name=name,ind=ind,path=p,q=q,fn=fn,
        tot=tot.group(1) if tot else "—",
        killed=not ks.strip().lower().startswith("none"),
        xref="same pocket as" in v,
        worked=os.path.exists(os.path.join(os.path.dirname(p),"build.md")),
        fit=q[2]*3+q[3]*2+q[4]*2+q[5]*2))
elig=[r for r in rows if r["q"][1]==3 and not r["killed"] and not r["xref"]]
elig.sort(key=lambda r:(-r["fit"],-r["q"][2],r["name"]))
THRESH=36
qual=[r for r in elig if r["fit"]>=THRESH]
ACR={"hoa":"HOA","rv":"RV","it":"IT","smb":"SMB","3pl":"3PL","k12":"K-12","mssp":"MSSP","tpa":"TPA","hr":"HR","ria":"RIA","rias":"RIAs","cre":"CRE"}
def indname(s):
    return " ".join(ACR.get(w, w.title()) for w in s.split("-"))
def hdr(r):
    m=re.match(r"([\d,]+\s*[-–]\s*[\d,]+)\s+(\w+(?:\s+\w+)?)", r["fn"])
    fnn = (m.group(1)+" "+m.group(2)) if m else re.split(r"[,;]",r["fn"])[0].strip()[:44]
    return "| %d | [[%s\\|%s]] | %s | %s | %d | %d | %d | %d | **%d** |"%(
        0, r["path"][:-len("/profile.md")]+"/profile", r["name"], indname(r["ind"]),
        fnn, r["q"][2],r["q"][3],r["q"][4],r["q"][5], r["fit"])
lines=[]
for i,r in enumerate(qual,1):
    lines.append(hdr(r).replace("| 0 |","| %d |"%i,1))
SH=[("Underwriting & risk pricing",r"underwrit|actuar|rating bureau"),
    ("Claims adjudication & review",r"claim|adjudicat|bill review|utili[sz]ation management"),
    ("Verification, inspection & certification",r"audit|inspect|verif|certif|screening|condition report|testing"),
    ("Technical advisory attached to product",r"advisor|agronom|applications lab|education|technical team|formulation|coverage engineering"),
    ("Programme & network administration",r"implementer|administration|programme|program |network analytics|document services")]
cl=[]
for lab,pat in SH:
    sel=[r for r in elig if re.search(pat,r["name"],re.I)]
    if not sel: continue
    cl.append("| %s | %d | %d | %.0f |"%(lab,len(sel),sum(1 for r in sel if r["fit"]>=THRESH),sum(r["fit"] for r in sel)/len(sel)))
pool_all=[r for r in rows if r["q"][1]<=3 and not r["killed"]]
tmpl=open("_state/embedded_header.md").read()
out=tmpl.replace("{{CLUSTERS}}","\n".join(cl))\
   .replace("{{TABLE}}","\n".join(lines))\
   .replace("{{NQUAL}}",str(len(qual))).replace("{{NELIG}}",str(len(elig)))\
   .replace("{{NPOOL}}",str(len(pool_all))).replace("{{NWORKED}}",str(sum(1 for r in qual if r["worked"])))\
   .replace("{{THRESH}}",str(THRESH))
# preserve hand-written case prose
if os.path.exists("_embedded-index.md"):
    old=open("_embedded-index.md").read()
    m=re.search(r"\n## Worked Cases\n(.*?)\n---\n\n## Coverage",old,re.S)
    if m: out=out.replace("{{CASES}}",m.group(1).strip())
out=out.replace("{{CASES}}","*Phase 1 in progress — worked cases appear here as they are written.*")
open("_embedded-index.md","w").write(out)
print("eligible=%d qualifying(fit>=%d)=%d worked=%d pool(Q1<=3 unfenced)=%d"%(len(elig),THRESH,len(qual),sum(1 for r in qual if r["worked"]),len(pool_all)))
