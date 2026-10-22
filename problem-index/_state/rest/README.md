# _state/rest/ — machinery for the remaining-industries build

The run order and cursor live in `../../_remaining-industry-implementation-and-discovery-plan.md`.

| File | Purpose |
|---|---|
| `baseline-industries.txt` | The 257 industry slugs that existed when the plan was written. New slugs must not collide with these |
| `naics-triage.tsv` | Stage 0: one row per remaining NAICS code with its decision (`new`, `merge`, `covered`, `skip`), slug and reason |
| `stage0_triage.py` | Holds every Stage 0 decision (new, merge, covered, skip), reason and boundary sentence, and writes `naics-triage.tsv` and `queue.tsv`. Don't re-run it once any row is past `todo`: it resets statuses |
| `queue.tsv` | Stage 0: one row per industry to build, with batch, category, NAICS codes, status and boundary sentence |
| `check_queue.py` | Checks the triage and queue against `_rest-of-the-industries.md`. Prints `QUEUE-CLEAN` |
| `verify.sh` | Per-industry verifier. Runs `../phase4/verify.sh`, then this plan's extra checks: NAICS line, Type strings, ml and agent entry shape, axis balance, contested lines, lens scores and source log. Prints `REST-VERIFY-CLEAN` |
| `sources/<slug>.md` | Per-industry log of web-checked claims, estimates and empty searches |

Run from the vault root:

```bash
python3 _state/rest/check_queue.py
bash    _state/rest/verify.sh <slug> [slug ...]   # no args: every queue row marked done
```
