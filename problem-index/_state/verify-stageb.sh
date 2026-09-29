#!/bin/bash
# Stage B per-industry structural check. Usage: bash _state/verify-stageb.sh <slug>
cd /Users/mac/Desktop/code/personal/problem-index
S="$1"; D="niches/$S"
[ -f "$D/_overview.md" ] || echo "MISSING OVERVIEW $S"
L1=$(grep -c '^- \[\[niches/'"$S"'/' "$D/_overview.md")
SUB=$(grep -c '^  - \[\[niches/'"$S"'/' "$D/_overview.md")
[ "$L1" = 8 ] || echo "OVERVIEW-L1-LINKS=$L1 (want 8) $S"
for d in "$D"/*/; do
  n=$(ls "$d" | wc -l | tr -d ' ')
  [ "$n" = 4 ] || echo "NOT4($n) $d"
  for f in profile build buy fix; do [ -f "$d$f.md" ] || echo "MISSING $d$f.md"; done
  grep -q '^\*\*Contested on:\*\*' "$d/profile.md" || echo "NO-CONTESTED $d/profile.md"
  for f in build buy fix; do grep -q '^\*\*Contested on:\*\*' "$d$f.md" || echo "NO-CONTESTED $d$f.md"; done
  grep -q '^\*\*Tags:\*\*' "$d/profile.md" && echo "PROFILE-HAS-TAGS $d"
  for f in build buy fix; do grep -q '^\*\*Tags:\*\*' "$d$f.md" || echo "NO-TAGS $d$f.md"; done
done
# headings
grep -h '^## ' "$D"/*/profile.md | sort | uniq -c | grep -vE 'Profile|What Makes This a Distinct Niche|Current Tools & Gaps|Problems' | sed 's/^/BADHEAD-PROFILE /'
grep -h '^## ' "$D"/*/build.md | sort | uniq -c | grep -vE 'The Problem|Why Nobody Has Built This|What to Build|Target Customer|Impact If Built' | sed 's/^/BADHEAD-BUILD /'
grep -h '^## ' "$D"/*/buy.md | sort | uniq -c | grep -vE 'The Problem|What Already Exists|The Customization Gap|Target Customer|Impact If Solved' | sed 's/^/BADHEAD-BUY /'
grep -h '^## ' "$D"/*/fix.md | sort | uniq -c | grep -vE "The Problem|Why It's Still Broken|What a Fix Looks Like|Who Feels the Pain|Impact If Fixed" | sed 's/^/BADHEAD-FIX /'
# types
grep -h '^\*\*Type:\*\*' "$D"/*/build.md | sort -u | grep -v '^\*\*Type:\*\* Build (Greenfield Opportunity)$' | sed 's/^/BADTYPE /'
grep -h '^\*\*Type:\*\*' "$D"/*/buy.md | sort -u | grep -v '^\*\*Type:\*\* Buy & Customize (Vertical Adaptation)$' | sed 's/^/BADTYPE /'
grep -h '^\*\*Type:\*\*' "$D"/*/fix.md | sort -u | grep -v '^\*\*Type:\*\* Fix (Pain Point)$' | sed 's/^/BADTYPE /'
# tag canon + count
grep -rhoE '(^|\s)#[a-z][a-z0-9-]{2,}' "$D" --include='*.md' | tr -d ' ' | sort -u > /tmp/sb_used.txt
comm -23 /tmp/sb_used.txt <(sort _state/safe-tags.txt) | sed 's/^/BADTAG /'
for f in "$D"/*/build.md "$D"/*/buy.md "$D"/*/fix.md; do
  c=$(grep '^\*\*Tags:\*\*' "$f" | grep -oE '#[a-z0-9-]+' | wc -l | tr -d ' ')
  [ "$c" -ge 5 ] && [ "$c" -le 10 ] || echo "TAGCOUNT=$c $f"
done
# wikilinks resolve
grep -rho '\[\[[^]|]*' "$D" --include='*.md' | sed 's/\[\[//' | sort -u | while read -r l; do
  case "$l" in industries/*|niches/*|problems/*) [ -f "$l.md" ] || echo "BROKEN $l";; esac
done
echo "STAGEB-OK $S ($(find "$D" -name '*.md' | wc -l | tr -d ' ') files, $L1 level-1 + $SUB sub-niche links)"
