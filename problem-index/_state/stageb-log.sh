#!/bin/bash
# Usage: bash _state/stageb-log.sh <slug> "<note>"
cd /Users/mac/Desktop/code/personal/problem-index
S="$1"; NOTE="$2"
F=$(find "niches/$S" -name '*.md' | wc -l | tr -d ' ')
printf -- "- **%s** — %s, %s files\n" "$S" "$NOTE" "$F" >> niches/_bookmark.md
DONE=$(while read -r s; do [ -d "niches/$s" ] && echo "$s"; done < _state/p2slugs.txt | wc -l | tr -d ' ')
TOT=$(while read -r s; do [ -d "niches/$s" ] && find "niches/$s" -name '*.md'; done < _state/p2slugs.txt | wc -l | tr -d ' ')
B1=$(head -11 _state/p2slugs.txt >/dev/null; echo "$DONE")
python3 - "$DONE" "$TOT" <<'PY'
import re,sys
done,tot=sys.argv[1],sys.argv[2]
p='_phase2-plan.md'; t=open(p).read()
b1=min(int(done),11)
t=re.sub(r'\| 1 \| Vertical SaaS \| \d+ / 11 \| \d+ \|', f'| 1 | Vertical SaaS | {b1} / 11 | — |', t, count=1)
t=re.sub(r'\| \| \*\*Total\*\* \| \*\*\d+ / 132\*\* \| \*\*[\d,]+\*\* \|', f'| | **Total** | **{done} / 132** | **{tot}** |', t, count=1)
open(p,'w').write(t)
print(f"cursor: {done}/132 industries, {tot} Stage B files")
PY
