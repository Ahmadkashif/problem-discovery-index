import json,os,datetime
tgt=json.load(open("_state/phase1.json"))
done=[]; todo=[]
for r in tgt:
    d=os.path.dirname(r["path"])
    (done if os.path.exists(d+"/build.md") else todo).append(r)
rows=[]
for i,r in enumerate(tgt,1):
    d=os.path.dirname(r["path"])
    mark="✅" if os.path.exists(d+"/build.md") else "⬜"
    rows.append("| %d | %s | `%s` | %s | %d |"%(i,mark,d,r["name"],r.get("fit", r.get("es",0))))
tmpl=open("_state/embedded_run_header.md").read()
open("_embedded-run.md","w").write(tmpl
  .replace("{{ROWS}}","\n".join(rows))
  .replace("{{NDONE}}",str(len(done))).replace("{{NTODO}}",str(len(todo)))
  .replace("{{NEXT}}", ("`"+os.path.dirname(todo[0]["path"])+"` — "+todo[0]["name"]) if todo else "— none, Phase 1 complete")
  .replace("{{TS}}",datetime.date.today().isoformat()))
print("cursor: %d done, %d remaining"%(len(done),len(todo)))
