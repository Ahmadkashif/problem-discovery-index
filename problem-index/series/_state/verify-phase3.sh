#!/bin/bash
# Phase 3 verification. Run from vault root: bash series/_state/verify-phase3.sh
cd "$(dirname "$0")/../.." || exit 1
fail=0
say(){ printf "%-46s %s\n" "$1" "$2"; }

# --- vault safety ---
a=$(find industries problems niches metadata plans -name '*.md' | wc -l | tr -d ' ')
# NB: 'lineage/' excluded from 2026-09-21 — it is the Lineage Sweep's own additive layer
# (spec: _lineage.md), not protected surface. The literal below moves whenever a ROOT
# tracker is added; the 'content layers' count above is the tripwire that actually matters.
b=$(find . -name '*.md' -not -path './.obsidian/*' -not -path './series/*' \
      -not -path './origins/*' -not -path './history/*' -not -path './lineage/*' | wc -l | tr -d ' ')
[ "$a" = 13335 ] && say "content layers (13335)" "OK" || { say "content layers" "CHANGED: $a"; fail=1; }
[ "$b" = 13352 ] && say "protected surface (13352)" "OK" || { say "protected surface" "CHANGED: $b"; fail=1; }
p1=$(comm -3 <(ls industries | sed 's/\.md$//' | sort) <(ls problems | sort) | wc -l | tr -d ' ')
p2=$(comm -3 <(ls industries | sed 's/\.md$//' | sort) <(ls niches | grep -v '_bookmark' | sort) | wc -l | tr -d ' ')
[ "$p1" = 0 ] && [ "$p2" = 0 ] && say "1:1:1 parity" "OK" || { say "1:1:1 parity" "BROKEN"; fail=1; }

# --- origins completeness ---
inc=0
for d in origins/*/; do
  [ "$(ls "$d" 2>/dev/null | wc -l | tr -d ' ')" = 5 ] || { echo "  incomplete: $d"; inc=1; }
done
[ "$inc" = 0 ] && say "origins at 5 files each" "OK" || { say "origins completeness" "INCOMPLETE"; fail=1; }
n=$(ls -d origins/*/ 2>/dev/null | wc -l | tr -d ' ')
say "origin count" "$n"

# --- sources on every phase-3 content file ---
miss=$(grep -L '^\*\*Sources:\*\*' origins/*/*.md series/eras/*.md history/*.md 2>/dev/null)
[ -z "$miss" ] && say "every file cites sources" "OK" || { say "missing Sources"; echo "$miss"; fail=1; }

# --- wikilink integrity ---
bad=0
for s in $(grep -rhoE '\[\[industries/[a-z0-9-]+' series origins history 2>/dev/null | sed 's#\[\[industries/##' | sort -u); do
  [ -f "industries/$s.md" ] || { echo "  broken industries link: $s"; bad=1; }
done
# NB: match only real era slugs (wave-NN-name). The bare pattern also matches the
# template placeholder [[series/eras/wave-NN-name|...]] in series/_plan.md — a false positive.
for e in $(grep -rhoE '\[\[series/eras/wave-[0-9]{2}-[a-z-]+' series origins history 2>/dev/null | sed 's#\[\[series/eras/##' | sort -u); do
  [ -f "series/eras/$e.md" ] || { echo "  broken era link: $e"; bad=1; }
done
for o in $(grep -rhoE '\[\[origins/[a-z0-9-]+/[a-z-]+' series origins history 2>/dev/null | sed 's#\[\[origins/##' | sort -u); do
  [ -f "origins/$o.md" ] || { echo "  broken origin link: $o"; bad=1; }
done
[ "$bad" = 0 ] && say "wikilinks resolve" "OK" || { say "wikilinks" "BROKEN"; fail=1; }

# --- tags canonical ---
t=$(grep -rhoE '(^|\s)#[a-z][a-z0-9-]{2,}' series origins history --include='*.md' 2>/dev/null \
    | tr -d ' ' | sort -u | comm -23 - <(sort -u _state/safe-tags.txt))
[ -z "$t" ] && say "tags canonical" "OK" || { say "NON-CANONICAL TAGS"; echo "$t"; fail=1; }

echo
[ "$fail" = 0 ] && echo "PHASE3-VERIFY-CLEAN" || echo "PHASE3-VERIFY-FAILED"
exit $fail
