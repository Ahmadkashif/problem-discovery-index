#!/bin/bash
# emit wikilink list for a wave: kids.sh <wave> <primary|secondary>
W="$(dirname "$0")/wave-assignment.txt"
col=2; [ "$2" = "secondary" ] && col=3
awk -F'|' -v n="$1" -v c="$col" '$c==n{print $1}' "$W" | while read s; do
  t=$(head -1 "industries/$s.md" | sed 's/^# //')
  echo "- [[industries/$s|$t]]"
done
