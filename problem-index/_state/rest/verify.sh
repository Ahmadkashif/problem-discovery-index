#!/bin/bash
# Verifier for industries added under _remaining-industry-implementation-and-discovery-plan.md.
# Usage: bash _state/rest/verify.sh [slug ...]   (default: every queue row with status done)
# Read-only. Runs the Phase 4 structural checks, then the checks this plan adds.
cd "$(dirname "$0")/../.." || exit 1
Q=_state/rest/queue.tsv
SLUGS=("$@")
if [ ${#SLUGS[@]} -eq 0 ]; then
  [ -f "$Q" ] || { echo "NO-QUEUE $Q (run Stage 0 first)"; echo "REST-VERIFY-FAIL"; exit 1; }
  mapfile -t SLUGS < <(awk -F'\t' 'NR>1 && $7=="done" {print $3}' "$Q")
  [ ${#SLUGS[@]} -eq 0 ] && { echo "nothing marked done in $Q"; echo "REST-VERIFY-CLEAN"; exit 0; }
fi
FAIL=0; bad(){ echo "$*"; FAIL=1; }

# 1. Structure, headings, tags, wikilinks, Pass 2 rules (shared with Phase 4)
P4=$(bash _state/phase4/verify.sh "${SLUGS[@]}")
echo "$P4" | grep -v '^PHASE4-VERIFY-'
echo "$P4" | grep -q '^PHASE4-VERIFY-CLEAN' || FAIL=1

for S in "${SLUGS[@]}"; do
  H="industries/$S.md"; P="problems/$S"; D="niches/$S"
  [ -f "$H" ] || continue
  # 2. Hub profile block, including the NAICS codes the industry covers
  for k in Category "NAICS 2022" "Market Size" "Tech Maturity" Workforce; do grep -q "^\*\*$k:\*\*" "$H" || bad "HUB-NO-$k $S"; done
  if [ -f "$Q" ]; then
    want=$(awk -F'\t' -v s="$S" 'NR>1 && $3==s {print $6}' "$Q" | tr -d ' ' | tr ',' '\n' | sort -u | paste -sd,)
    got=$(grep -m1 '^\*\*NAICS 2022:\*\*' "$H" | grep -oE '[0-9]{6}' | sort -u | paste -sd,)
    [ -n "$want" ] && [ "$want" != "$got" ] && bad "NAICS-MISMATCH $S hub=[$got] queue=[$want]"
  fi
  # 3. Problem Type strings
  grep -qx '\*\*Type:\*\* High Impact' "$P/high-impact.md" || bad "BADTYPE $P/high-impact.md"
  for f in low-impact-1 low-impact-2; do grep -qx '\*\*Type:\*\* Low Impact (Customisation Opportunity)' "$P/$f.md" || bad "BADTYPE $P/$f.md"; done
  for f in worker-life-1 worker-life-2; do grep -qx '\*\*Type:\*\* Worker Life Changing' "$P/$f.md" || bad "BADTYPE $P/$f.md"; done
  # 4. ml-opportunity: 4-5 entries, tacit entry first, all seven fields per entry
  M="$P/ml-opportunity.md"; n=$(grep -c '^## [0-9]' "$M")
  { [ "$n" -ge 4 ] && [ "$n" -le 5 ]; } || bad "ML-ENTRIES=$n (want 4-5) $S"
  awk '/^## 1\./{getline; print; exit}' "$M" | grep -q '#tacit-knowledge-ml' || bad "ML-TACIT-NOT-FIRST $S"
  grep -q '^\*\*Derived from:\*\*' "$M" || bad "ML-NO-DERIVED $S"
  for k in "Problem statement" "ML task" "Input data" Target "Evaluation metric" Scope "Data availability"; do
    [ "$(grep -c "^\*\*$k:\*\*" "$M")" = "$n" ] || bad "ML-FIELD($k)!=$n $S"
  done
  # 5. ai-agents-platforms: 3-4 entries, Phase 2/4 field set
  A="$P/ai-agents-platforms.md"; n=$(grep -c '^## [0-9]' "$A")
  { [ "$n" -ge 3 ] && [ "$n" -le 4 ]; } || bad "AGENT-ENTRIES=$n (want 3-4) $S"
  for k in Concept Inputs "Outputs / Actions" "Why now" Market; do
    [ "$(grep -c "^\*\*$k:\*\*" "$A")" = "$n" ] || bad "AGENT-FIELD($k)!=$n $S"
  done
  # 6. Niche layer: two level-1 niches per axis, emoji matches axis, contested lines everywhere
  [ -f "$D/_overview.md" ] || continue
  O="$D/_overview.md"
  for ax in "High Market Share:🔵" "Low Digitized:🟠" "Underserved Audience:🟣" "Highly Automatable:⚡"; do
    c=$(grep -l "^\*\*Category:\*\* ${ax%%:*}\$" "$D"/*/profile.md 2>/dev/null | wc -l)
    [ "$c" = 2 ] || bad "AXIS(${ax%%:*})=$c (want 2) $S"
    for p in $(grep -l "^\*\*Category:\*\* ${ax%%:*}\$" "$D"/*/profile.md 2>/dev/null); do
      grep -q "^- \[\[${p%.md}|${ax##*:} " "$O" || bad "OVERVIEW-LINK-OR-EMOJI ${p%.md}"
    done
  done
  for p in $(grep -l '^\*\*Category:\*\* Contested Sub-Niche$' "$D"/*/profile.md 2>/dev/null); do
    grep -q "^  - \[\[${p%.md}|🎯 " "$O" || bad "SUBNICHE-NOT-LINKED-INDENTED ${p%.md}"
  done
  for d in "$D"/*/; do
    d=${d%/}
    [ "$(grep -c "\[\[$d/profile|" "$O")" = 1 ] || bad "DIR-NOT-LINKED-ONCE $d"
    if grep -q '^\*\*Category:\*\* Insight Layer' "$d/profile.md" 2>/dev/null; then
      grep -q '^\*\*Value-Chain Position:\*\*' "$d/profile.md" || bad "P2-NO-POSITION $d"
      if [ -f "$d/build.md" ]; then
        for f in profile build buy fix; do grep -q '^\*\*Contested on:\*\*' "$d/$f.md" || bad "QUALIFIER-NO-CONTESTED $d/$f.md"; done
      fi
    else
      for f in build buy fix; do grep -q '^\*\*Contested on:\*\*' "$d/$f.md" 2>/dev/null || bad "NO-CONTESTED $d/$f.md"; done
    fi
  done
  # 7. Source log
  L="_state/rest/sources/$S.md"
  if [ -f "$L" ]; then [ "$(grep -oE 'https?://' "$L" | wc -l)" -ge 3 ] || bad "SOURCES<3-URLS $S"; else bad "NO-SOURCE-LOG $S"; fi
done

# 8. Lens scores: one line per item (the industry and every niche dir), factors are ints 1-5
python3 - "${SLUGS[@]}" <<'PY' || FAIL=1
import json, os, sys
bad = []
for s in sys.argv[1:]:
    if not os.path.isdir(f"niches/{s}"):
        continue
    want = {s} | {f"{s}/{d}" for d in os.listdir(f"niches/{s}") if os.path.isdir(f"niches/{s}/{d}")}
    path = f"lenses/_state/scores/{s}.jsonl"
    if not os.path.exists(path):
        bad.append(f"NO-LENS-SCORES {s}"); continue
    got = []
    for n, line in enumerate(open(path), 1):
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            bad.append(f"LENS-BAD-JSON {path}:{n}"); continue
        got.append(r.get("id"))
        for k, ln in (("ai_proof", 5), ("clarity", 4), ("digital", 4)):
            v = r.get(k)
            if not (isinstance(v, list) and len(v) == ln and all(isinstance(x, int) and 1 <= x <= 5 for x in v)):
                bad.append(f"LENS-BAD-{k} {path}:{n}")
        for k in ("why_ai", "why_clarity", "why_digital"):
            if not str(r.get(k, "")).strip():
                bad.append(f"LENS-NO-{k} {path}:{n}")
    if len(got) != len(set(got)):
        bad.append(f"LENS-DUPLICATE-IDS {s}")
    for i in sorted(want - set(got)):
        bad.append(f"LENS-UNSCORED {i}")
    for i in sorted(set(got) - want):
        bad.append(f"LENS-UNKNOWN-ID {i}")
if bad:
    print("\n".join(bad))
sys.exit(1 if bad else 0)
PY

[ $FAIL = 0 ] && echo "REST-VERIFY-CLEAN" || echo "REST-VERIFY-FAIL"
