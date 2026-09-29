#!/bin/bash
# Lineage Sweep verification. Run from anywhere: bash _state/verify-lineage.sh
# Spec: _lineage.md · Run order: _lineage-run.md
cd "$(dirname "$0")/.." || exit 1
fail=0
say(){ printf "%-46s %s\n" "$1" "$2"; }

shopt -s nullglob
NOTES=(lineage/*.md)
# _bookmark.md is a tracker, not a note
FILES=()
for f in "${NOTES[@]}"; do
  [ "$(basename "$f")" = "_bookmark.md" ] && continue
  FILES+=("$f")
done
N=${#FILES[@]}

# --- vault safety: the tripwire that actually matters ---
a=$(find industries problems niches metadata plans -name '*.md' | wc -l | tr -d ' ')
[ "$a" = 13335 ] && say "protected content layers (13335)" "OK" \
  || { say "protected content layers" "CHANGED: $a"; fail=1; }

if [ "$N" = 0 ]; then
  say "notes on disk" "0 — nothing to check yet"
  echo "LINEAGE-OK (empty)"
  exit $fail
fi
say "notes on disk" "$N"

# --- exactly five required headings, none renamed ---
bad=""
for f in "${FILES[@]}"; do
  h=$(grep -c '^## ' "$f")
  [ "$h" = 5 ] || bad="$bad HEADCOUNT($h):$f"
done
for want in 'The Problem That Came First' 'What Got Built' 'Who Built It, And Why Them' \
            'What It Cost' 'What You Still Touch'; do
  for f in "${FILES[@]}"; do
    grep -qF "## $want" "$f" || bad="$bad NOHEAD[$want]:$f"
  done
done
[ -z "$bad" ] && say "heading set" "OK" || { say "heading set" "BAD:$bad"; fail=1; }

# --- full metadata block ---
bad=""
for f in "${FILES[@]}"; do
  for k in 'Industry:' 'Wave:' 'The tool:' 'Builder:' 'Builder in vault:' 'Verification:'; do
    grep -qF "**$k**" "$f" || bad="$bad NOMETA[$k]:$f"
  done
done
[ -z "$bad" ] && say "metadata block" "OK" || { say "metadata block" "BAD:$bad"; fail=1; }

# --- Builder is an aggregation key: short canonical name, not a sentence ---
# _builder-index.md aggregates on this exact string, so a prose value silently
# splits the count and destroys the nomination gate.
bad=""
for f in "${FILES[@]}"; do
  b=$(grep -m1 '^\*\*Builder:\*\*' "$f" | sed 's/^\*\*Builder:\*\* *//')
  [ ${#b} -le 60 ] || bad="$bad LONG(${#b}):$(basename "$f" .md)"
  case "$b" in
    *" — "*) [ "$b" = "unknown — searched, not established" ] || bad="$bad PROSE:$(basename "$f" .md)";;
    *","*|*"("*) bad="$bad PROSE:$(basename "$f" .md)";;
  esac
done
[ -z "$bad" ] && say "builder is a clean key" "OK" || { say "builder is a clean key" "BAD:$bad"; fail=1; }

# --- Rail 1: the specificity rule ---
vague=$(grep -liE '^\*\*The tool:\*\* *\*?\*?(SaaS|the cloud|cloud|software|automation|AI|digit[ia][sz]ation|technology)\*?\*?\.?$' "${FILES[@]}" 2>/dev/null)
[ -z "$vague" ] && say "Rail 1 — tool is specific" "OK" \
  || { say "Rail 1 — tool is specific" "TOOVAGUE: $vague"; fail=1; }

# --- sources on every note ---
miss=$(grep -L '^\*\*Sources:\*\*' "${FILES[@]}")
[ -z "$miss" ] && say "sources cited" "OK" || { say "sources cited" "MISSING: $miss"; fail=1; }

# --- word band (soft: warn, do not fail) ---
# Measured on the BODY, excluding the **Sources:** paragraph. Counting Sources would
# penalise honest citation and negative findings, which is exactly backwards: the
# reference note's Sources block is 100 words because it records two things it could
# not establish. Band applies to prose the reader reads.
warn=""
for f in "${FILES[@]}"; do
  w=$(sed '/^\*\*Sources:/,$d' "$f" | wc -w | tr -d ' ')
  { [ "$w" -ge 450 ] && [ "$w" -le 750 ]; } || warn="$warn $(basename "$f" .md)=$w"
done
[ -z "$warn" ] && say "body word band 450-750" "OK" || say "body word band 450-750" "SOFT-WARN:$warn"

# --- every note links back into the vault ---
bad=""
for f in "${FILES[@]}"; do
  grep -qE '\[\[(problems|niches)/' "$f" || bad="$bad $f"
done
[ -z "$bad" ] && say "links back into vault" "OK" || { say "links back into vault" "NOVAULTLINK:$bad"; fail=1; }

# --- wikilinks resolve ---
bad=""
while read -r t; do
  [ -z "$t" ] && continue
  [ -e "$t.md" ] || [ -e "$t" ] || bad="$bad $t"
done < <(grep -ho '\[\[[^]|]*' "${FILES[@]}" | sed 's/\[\[//' | sort -u)
[ -z "$bad" ] && say "wikilinks resolve" "OK" || { say "wikilinks resolve" "BROKEN:$bad"; fail=1; }

# --- tags: safety net, expected to be vacuous ---
bt=$(grep -rhoE '(^|\s)#[a-z][a-z0-9-]{2,}' lineage --include='*.md' 2>/dev/null \
     | tr -d ' ' | sort -u | comm -23 - <(sort -u _state/safe-tags.txt))
[ -z "$bt" ] && say "tags canonical" "OK" || { say "tags canonical" "BADTAG: $bt"; fail=1; }

# --- cursor freshness ---
claimed=$(grep -m1 '^| \*\*Completed\*\* |' _lineage.md | grep -oE '[0-9]+ of 250' | grep -oE '^[0-9]+')
[ "$claimed" = "$N" ] && say "cursor matches disk ($N)" "OK" \
  || { say "cursor vs disk" "STALE: cursor=$claimed disk=$N"; fail=1; }

[ $fail = 0 ] && echo "LINEAGE-OK ($N notes)" || echo "LINEAGE-VERIFY-FAILED"
exit $fail
