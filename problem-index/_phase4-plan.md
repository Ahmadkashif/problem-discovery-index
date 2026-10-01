# Phase 4 — Capital Markets & Investment Research

**Status:** plan drafted 2026-10-01 · awaiting owner approval · nothing built
**Branch:** `phase4/capital-markets-research`. Never committed to `main` directly.
**Standing run order:** this file. A fresh agent is launched with *"Read `_phase4-plan.md` and execute it."*

---

## 1. Why this phase exists

A content-strategy diagnostic (2026-10-01) looked for vault material on **workflow automation for research teams in finance**. It found strong coverage next to finance and a hole at the centre:

| Present | Absent |
|---|---|
| `wealth-management-rias` (incl. manager research, fund data, filing data pockets), `credit-unions` (investment research, model validation), `robo-advisors`, `data-marketplace-brokers` (the sourcing analyst), `web-data-extraction-firms`, origins `exchanges-market-makers` and `credit-bureaus` | **No industry** for hedge funds, asset managers, sell-side equity research, private equity or investment banking. FactSet **0** files, expert networks **0**, earnings calls **0**, PitchBook 2, Capital IQ 2 |

The firms with the largest research teams in finance aren't in the vault. This phase adds them using the vault's existing method and nothing new.

## 2. The rule: additive only

- **No existing file is edited.** That covers all 250 industries, their problems and niches, `series/`, `history/`, `lineage/`, `origins/`, and every shared index and bookmark.
- Every Phase 4 file is a **new file** under an existing layer (`industries/`, `problems/`, `niches/`) or under `_state/phase4/`.
- Phase 4 keeps its **own state**: the CURSOR in this file, `_scorecard-index-phase4.md` and `_state/phase4/verify.sh`. Shared registers (`_bookmark.md`, `niches/_bookmark.md`, `_scorecard-index.md`, `_direction.md` cursor, `series/_eras.md` wave table) are **not touched** while the phase runs. Folding them in is a separate, gated Stage E.
- Templates, heading sets, metadata blocks, canonical tags (`_state/safe-tags.txt`) and the contested filter come from `CLAUDE.md`, `_phase2-plan.md` §2 and §5, and `_direction.md` **unchanged**.

## 3. The industries — Batch 13

### Core: the proven gap (7)

| # | Slug | Boundary with existing vault |
|---|---|---|
| 1 | `hedge-funds` | Not `crypto-exchanges` and not `robo-advisors`. Covers discretionary and systematic funds, analyst pods and alt-data consumption |
| 2 | `asset-managers` | Runs pooled products. `wealth-management-rias` advises individuals and *buys* these products; its `manager-research-due-diligence` pocket is the buyer side, so link to it rather than duplicate it |
| 3 | `sell-side-equity-research` | Broker research departments, initiations and earnings models, plus the post-MiFID II unbundling economics |
| 4 | `private-equity-firms` | Deal sourcing, diligence, portfolio monitoring. **PE is a prior deployment and carries zero scoring weight** (`_phase2-plan.md` §6) |
| 5 | `investment-banking-boutiques` | Mid-market M&A advisory: pitch books, comps, CIMs. Not bulge-bracket trading |
| 6 | `financial-data-vendors` | Terminal and fundamentals vendors (Bloomberg/FactSet/Capital IQ/PitchBook class). Not `data-marketplace-brokers` (alt-data brokerage) and not the RIA `investment-research-fund-data` pocket (fund-only) |
| 7 | `expert-networks` | Primary-research calls, compliance screening, transcript libraries |

### Optional: owner decision before Stage A (4)

`venture-capital-firms` · `credit-rating-agencies` · `family-offices` · `independent-research-providers`

Each is research-heavy and finance-facing, but none was shown missing by the diagnostic. Add them only on an explicit yes. Otherwise the batch stays at 7.

## 4. Stages

Same layer order as Phase 2: **Stage A → Stage B → Stage C**, plus a pilot first and a merge gate at the end. **The owner reviews at every gate.**

| Stage | What | Per industry | Files (7 core) | Threading | Gate |
|---|---|---|---|---|---|
| **0** | Setup: write `_state/phase4/verify.sh` (wraps `verify-stageb.sh` and the parity checks, scoped to Phase 4 slugs, no hard-coded paths), lock slugs | — | 1–2 | single | — |
| **P** | **Pilot.** Run A + B + C end to end on **one** industry (`hedge-funds`) | ~65–75 | ~70 | single | **Owner reviews the pilot.** Go, revise template use, or stop |
| **A** | `industries/<slug>.md` + `problems/<slug>/` (7 files) for the remaining 6 | 8 | 48 | 2 threads OK (disjoint slugs) | Owner skims the hubs |
| **B** | Niche layer: `_overview.md` + 8 level-1 niches × 4 files + contested sub-niches × 4, under the `_phase2-plan.md` §2 filter | ~41 | ~246 | **single thread** | Owner reviews `## Filter Notes` per industry |
| **C** | Pass 2 insight-layer sweep (`_direction.md` method): ≥10 pockets per industry, gate, rubric, `build/buy/fix` only for ≥50/60 with no kill switch. Qualifiers go to `_scorecard-index-phase4.md` | ~13–25 | ~90–150 | **single thread** | Owner reviews the Phase 4 scorecard |
| **E** | **Merge gate.** List exactly which shared registers would change (rows appended or regenerated: `_bookmark.md`, `niches/_bookmark.md`, `_scorecard-index.md` via `reindex.py`, `series/_eras.md` wave assignment) and apply them **only on explicit approval**, as a separate commit | — | diff only | single | **Owner approves or declines the merge** |

**Rough total for the 7 core industries:** ~450–520 new files. Adding the optional 4 brings it to ~750–800.

### Batching inside stages

- **A:** one batch of 6, done in a single session.
- **B:** batches of 2 industries, with the cursor and the verifier run **after every industry**, so an interrupted run loses at most one.
- **C:** batches of 3, with the same per-industry close-out.

## 5. Per-industry method

The steps are the same as `_phase2-plan.md` §5. Only the bookkeeping changes:

1. Hub: Profile, Key Pain Themes, Current Tech Landscape, Problems, Analysis.
2. `problems/<slug>/`, all 7 files. `ml-opportunity.md` lists a tacit-knowledge entry first. Finance has plenty: the analyst who *knows* a management team is sandbagging guidance, or a PM's read of positioning.
3. Niche layer, with `**Contested on:**` on every niche note, `## Filter Notes` logging negative results honestly, and 🎯 contested sub-niches as sibling dirs.
4. Pass 2 pockets appended under `---` in the industry's **own new** `_overview.md`.
5. Update **this file's** CURSOR, then run `bash _state/phase4/verify.sh` and fix any failure before continuing.

**Research:** market sizes and named tools get a web check where WebSearch is available. Anything unverified is written as an estimate, never as a fact. This matters more here than elsewhere because this material feeds published content.

## 6. Out of scope for this phase

- `history/`, `lineage/`, `origins/` and `series/` entries for these industries. That's a possible Phase 4b, proposed only if the content work shows a need.
- Fixing anything found wrong in the existing vault. Log it in §8 below and leave the file alone.
- The content topics themselves. Those draw on this phase but live outside the vault.

## 7. Known hazards, inherited

- `_state/verify.sh` hard-codes `cd /Users/mac/...` and fails on this machine. Phase 4 uses its own verifier and doesn't edit that one.
- Phase 2 **Stage C was never run** for its 132 industries, so Pass 2 coverage is 118/250. Phase 4 runs Stage C for its own slugs only; the Phase 2 backlog stays untouched.
- Audit tags against `_state/safe-tags.txt` (138), **not** `metadata/tags.md` (190), which includes deprecated tags and would let them pass silently.

## 8. Findings log

*(Append-only. Defects or contradictions found in existing files go here, not into those files.)*

---

## CURSOR

**Stage:** — awaiting owner approval of this plan (incl. the §3 optional-industry decision)
**Completed:** 0 / 7
**Next:** Stage 0 → Pilot (`hedge-funds`)
**Verifier:** `bash _state/phase4/verify.sh` (not yet written)
