cd /Users/mac/Desktop/code/personal/problem-index
find niches -mindepth 2 -maxdepth 2 -type d | while read d; do grep -q '^\*\*Category:\*\* Insight Layer' "$d/profile.md" 2>/dev/null && continue; echo "P1BAD $(ls $d | wc -l) $d"; done | grep -v ' 4 '
grep -rl '^\*\*Category:\*\* Insight Layer' niches --include='profile.md' | xargs -n1 dirname | while read d; do n=$(ls $d | wc -l); [ "$n" -eq 1 ] || [ "$n" -eq 4 ] || echo "P2BAD($n) $d"; done
grep -rhoE '(^|\s)#[a-z][a-z0-9-]{2,}' niches problems --include='*.md' | tr -d ' ' | sort -u > /tmp/used.txt
grep -o '^#[a-z0-9-]\+' metadata/tags.md | sort -u > /tmp/canon.txt
comm -23 /tmp/used.txt /tmp/canon.txt | grep -v foodtruckfriday | sed 's/^/BADTAG /'
IND=$(ls industries/*.md | wc -l | tr -d ' '); echo "INDUSTRIES: $IND (118 base + Phase 2)"
[ "$(grep -rL '^\*\*Category:\*\* Insight Layer' niches --include='profile.md' | wc -l | tr -d ' ')" -ge 944 ] || echo "PASS1 COUNT WRONG"
comm -3 <(ls industries | sed 's/\.md$//' | sort) <(ls problems | sort)
# Stage A (Phase 2): a slug present in industries/+problems/ but not yet in niches/ is pending, not a fault.
comm -13 <(ls industries | sed 's/\.md$//' | sort) <(ls niches | grep -v '_bookmark' | sort) | sed 's/^/ORPHAN-NICHE /'
PEND=$(comm -23 <(ls industries | sed 's/\.md$//' | sort) <(ls niches | grep -v '_bookmark' | sort) | wc -l | tr -d ' ')
[ "$PEND" = 0 ] || echo "STAGE-A-PENDING: $PEND industries awaiting niche layer"
grep -rho '\[\[niches/[^|\]*' niches/*/_overview.md _scorecard-index.md 2>/dev/null | sed 's/\[\[//; s/\\$//' | sort -u | while read -r l; do [ -f "$l.md" ] || echo "BROKEN: $l"; done
echo "VERIFY-CLEAN"
