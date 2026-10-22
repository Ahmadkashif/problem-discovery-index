#!/bin/bash
# Rebuild the lens rankings while later batches are still being built. Coordinator only.
# Same three steps as plan §5 step 5.3, but queue slugs that are not `done` are left out of both
# the digests and the scores, so a half-built industry can't break verify.py or reach the rankings.
cd "$(dirname "$0")/../.." || exit 1
D=$(mktemp -d); S=$(mktemp -d)
python3 lenses/_state/digest.py "$D" || exit 1
mapfile -t SKIP < <(awk -F'\t' 'NR>1 && $7!="done" {print $3}' _state/rest/queue.tsv)
for s in "${SKIP[@]}"; do rm -f "$D/$s.md"; done
for f in lenses/_state/scores/*.jsonl; do
  b=$(basename "$f" .jsonl)
  printf '%s\n' "${SKIP[@]}" | grep -qx "$b" || ln -s "$PWD/$f" "$S/"
done
out=$(python3 lenses/_state/verify.py "$D" "$S"); echo "$out" | tail -3
echo "$out" | grep -q VERIFY-CLEAN || { echo "LENS-REBUILD-ABORTED"; exit 1; }
python3 lenses/_state/build.py "$D" "$S" && echo "LENS-REBUILD-DONE"
