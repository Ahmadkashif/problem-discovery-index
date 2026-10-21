# lenses/_state/ — how the rankings are rebuilt

| File | Purpose |
|---|---|
| `digest.py` | Compresses every industry and sub-niche into the short digests the scorers read, and deals them into 20 batches |
| `scores/` | First-pass scores, one `<industry>.jsonl` per industry (factor arrays plus a one-line reason per lens) |
| `corrections.jsonl` | Reviewer corrections, each tagged with its reviewer. They override first-pass scores field by field, and a later line wins |
| `verify.py` | Confirms every item has every factor as an integer from 1 to 5. Prints `VERIFY-CLEAN` |
| `build.py` | Writes `../ai-proof.md`, `../value-clarity.md`, `../digital-nature.md`, `../scores.csv` and `stats.json` |
| `agreement.json` | Blind re-score of 80 random items compared with the first pass |

Run from the vault root:

```bash
python3 lenses/_state/digest.py /tmp/lens-digests
python3 lenses/_state/verify.py /tmp/lens-digests lenses/_state/scores
python3 lenses/_state/build.py  /tmp/lens-digests lenses/_state/scores
```
