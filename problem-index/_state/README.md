# _state/ — resumable machinery

Scripts and data that make the vault's sweeps resumable across sessions. Previously these
lived only in a session scratchpad and would have been lost on a new session.

| File | Purpose |
|---|---|
| `pockets.json` | Parsed scorecards for all 1,530 Pass 2 pockets (name, industry, Q1-Q5, kill switch, verdict) |
| `phase1.json` | The 20 Phase 1 target pockets, ranked by embedded-research fit |
| `embedded_index.py` | Regenerates `_embedded-index.md`. Preserves hand-written worked-case prose. |
| `embedded_header.md` | Template for `_embedded-index.md` |
| `cursor.py` | Regenerates `_embedded-run.md` including the live PHASE 1 CURSOR |
| `embedded_run_header.md` | Template for `_embedded-run.md` |
| `annotate.py` | Phase 1 close-out: appends embedded-fit line + `## Problems` list to worked profiles |
| `reindex.py` | Regenerates `_scorecard-index.md` (primary Pass 2 index) |
| `advance.py` | Regenerates the CURSOR in `_direction.md` and the Pass 2 section of `niches/_bookmark.md` |
| `verify.sh` | Pass 2 verification block — prints `VERIFY-CLEAN` |

Run everything from the vault root:

```bash
python3 _state/embedded_index.py    # rebuild the embedded index
python3 _state/cursor.py            # rebuild the run order + cursor
bash    _state/verify.sh            # structural verification
```

`pockets.json` is derived — regenerate it by re-parsing `niches/*/*/profile.md` if profiles change.
