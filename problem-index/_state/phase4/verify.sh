#!/bin/bash
# Phase 4 verifier. Usage: bash _state/phase4/verify.sh [slug ...]   (default: all Phase 4 slugs)
# Read-only. Checks only Phase 4 slugs; never touches the rest of the vault.
cd "$(dirname "$0")/../.." || exit 1
SLUGS=("$@"); [ ${#SLUGS[@]} -eq 0 ] && SLUGS=(hedge-funds asset-managers sell-side-equity-research private-equity-firms investment-banking-boutiques financial-data-vendors expert-networks)
CANON=$(mktemp); sort -u _state/safe-tags.txt > "$CANON"
FAIL=0; bad(){ echo "$*"; FAIL=1; }
for S in "${SLUGS[@]}"; do
  H="industries/$S.md"; P="problems/$S"; D="niches/$S"
  [ -f "$H" ] || { bad "MISSING-HUB $S"; continue; }
  for h in Profile "Key Pain Themes" "Current Tech Landscape" Problems Analysis; do grep -q "^## $h\$" "$H" || bad "HUB-NO-HEADING($h) $S"; done
  [ "$(grep -c '^- \[\[problems/'"$S"'/' "$H")" = 7 ] || bad "HUB-PROBLEM-LINKS!=7 $S"
  for f in high-impact low-impact-1 low-impact-2 worker-life-1 worker-life-2 ml-opportunity ai-agents-platforms; do [ -f "$P/$f.md" ] || bad "MISSING $P/$f.md"; done
  [ "$(ls "$P" 2>/dev/null | wc -l)" = 7 ] || bad "PROBLEMS-NOT-7 $S"
  for f in high-impact low-impact-1 low-impact-2 worker-life-1 worker-life-2; do
    for k in Industry Type One-liner Tags; do grep -q "^\*\*$k:\*\*" "$P/$f.md" 2>/dev/null || bad "NO-$k $P/$f.md"; done
  done
  chk(){ grep -h '^## ' $1 2>/dev/null | sed 's/^## //' | sort -u | grep -vxF -f <(printf '%s\n' "${@:2}") | sed "s|^|BADHEAD $1: |"; }
  out=$(chk "$P/high-impact.md" "The Problem" "Why It's Unsolved" "What a Solution Looks Like" "Impact If Solved"; chk "$P/low-impact-[12].md" "The Problem" "What Already Exists" "The Customisation Gap" "Impact If Solved"; chk "$P/worker-life-[12].md" "The Problem" "Why It Matters to the Worker" "What a Solution Looks Like" "Impact If Solved"); [ -n "$out" ] && bad "$out"
  grep -q '#tacit-knowledge-ml' "$P/ml-opportunity.md" 2>/dev/null || bad "ML-NO-TACIT $S"
  [ -f "$D/_overview.md" ] || { bad "MISSING-OVERVIEW $S"; continue; }
  L1=$(grep '^- \[\[niches/'"$S"'/' "$D/_overview.md" | grep -vc '🔍'); [ "$L1" = 8 ] || bad "OVERVIEW-L1=$L1 (want 8) $S"
  grep -q '^## Filter Notes' "$D/_overview.md" || bad "NO-FILTER-NOTES $S"
  grep -q '^## Pass 2 — Insight-Layer Discovery' "$D/_overview.md" || bad "NO-PASS2 $S"
  NP2=0
  for d in "$D"/*/; do
    n=$(ls "$d" | wc -l)
    if grep -q '^\*\*Category:\*\* Insight Layer' "$d/profile.md" 2>/dev/null; then
      NP2=$((NP2+1))
      { [ "$n" = 1 ] || [ "$n" = 4 ]; } || bad "P2-NOT-1-OR-4($n) $d"
      for k in "## Scorecard" "\*\*Verdict:\*\*" "\*\*Kill switches:\*\*"; do grep -q "^$k" "$d/profile.md" || bad "P2-NO($k) $d"; done
      grep -q '^\*\*Tags:\*\*' "$d/profile.md" && bad "PROFILE-HAS-TAGS $d"
      if [ "$n" = 4 ]; then grep -q 'Qualified' "$d/profile.md" || bad "P2-4FILES-NOT-QUALIFIED $d"; fi
    else
      [ "$n" = 4 ] || bad "NOT4($n) $d"
      grep -q '^\*\*Contested on:\*\*' "$d/profile.md" || bad "NO-CONTESTED $d/profile.md"
      grep -q '^\*\*Tags:\*\*' "$d/profile.md" && bad "PROFILE-HAS-TAGS $d"
      out=$(chk "$d/profile.md" "Profile" "What Makes This a Distinct Niche" "Current Tools & Gaps" "Problems"); [ -n "$out" ] && bad "$out"
    fi
    [ -f "$d/build.md" ] || continue
    for f in build buy fix; do
      grep -q '^\*\*Tags:\*\*' "$d$f.md" || bad "NO-TAGS $d$f.md"
      c=$(grep '^\*\*Tags:\*\*' "$d$f.md" | grep -oE '#[a-z0-9-]+' | wc -l); { [ "$c" -ge 5 ] && [ "$c" -le 10 ]; } || bad "TAGCOUNT=$c $d$f.md"
    done
    grep -qx '\*\*Type:\*\* Build (Greenfield Opportunity)' "$d/build.md" || bad "BADTYPE $d/build.md"
    grep -qx '\*\*Type:\*\* Buy & Customize (Vertical Adaptation)' "$d/buy.md" || bad "BADTYPE $d/buy.md"
    grep -qx '\*\*Type:\*\* Fix (Pain Point)' "$d/fix.md" || bad "BADTYPE $d/fix.md"
    out=$(chk "$d/build.md" "The Problem" "Why Nobody Has Built This" "What to Build" "Target Customer" "Impact If Built"; chk "$d/buy.md" "The Problem" "What Already Exists" "The Customization Gap" "Target Customer" "Impact If Solved"; chk "$d/fix.md" "The Problem" "Why It's Still Broken" "What a Fix Looks Like" "Who Feels the Pain" "Impact If Fixed"); [ -n "$out" ] && bad "$out"
  done
  [ "$NP2" -ge 10 ] || bad "PASS2-POCKETS=$NP2 (want >=10) $S"
  # canonical tags across all of this slug's files
  grep -rhoE '(^|\s)#[a-z][a-z0-9-]{2,}' "$H" "$P" "$D" --include='*.md' | tr -d ' ' | sort -u | comm -23 - "$CANON" | sed "s|^|BADTAG($S) |" | while read -r l; do echo "$l"; done | grep . && FAIL=1
  # wikilinks resolve (bare-slug links in problems/ resolve to industries/)
  grep -rho '\[\[[^]|#]*' "$H" "$P" "$D" --include='*.md' | sed 's/\[\[//; s/\\$//' | sort -u | while read -r l; do
    case "$l" in */*) [ -f "$l.md" ] || echo "BROKEN($S) $l";; *) [ -f "industries/$l.md" ] || echo "BROKEN($S) $l";; esac
  done | grep . && FAIL=1
  echo "OK? $S: $(find "$H" "$P" "$D" -name '*.md' | wc -l) files, $L1 level-1, $NP2 Pass-2 pockets"
done
rm -f "$CANON"
[ $FAIL = 0 ] && echo "PHASE4-VERIFY-CLEAN" || echo "PHASE4-VERIFY-FAIL"
