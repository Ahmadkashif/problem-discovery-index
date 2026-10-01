# Phase 4 — Capital Markets & Investment Research

**Status:** ✅ Stages A, B and C complete for all 7 core industries (2026-10-02). 503 files, `PHASE4-VERIFY-CLEAN`. Stage E (merge into shared registers) not run.
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

Same layer order as Phase 2: **Stage A → Stage B → Stage C**. **No approval gates** (owner instruction, 2026-10-02): every stage runs through, and the verifier is the gate. The owner reviews the finished build. Stage E (merging into shared registers) is the only step held back, because it edits existing files.

| Stage | What | Per industry | Files (7 core) | Threading | Gate |
|---|---|---|---|---|---|
| **0** | Setup: write `_state/phase4/verify.sh` (wraps `verify-stageb.sh` and the parity checks, scoped to Phase 4 slugs, no hard-coded paths), lock slugs | — | 1–2 | single | — |
| **A** | `industries/<slug>.md` + `problems/<slug>/` (7 files) for the remaining 6 | 8 | 48 | parallel, one builder per slug | verifier |
| **B** | Niche layer: `_overview.md` + 8 level-1 niches × 4 files + contested sub-niches × 4, under the `_phase2-plan.md` §2 filter | ~41 | ~246 | same builder, after A | verifier |
| **C** | Pass 2 insight-layer sweep (`_direction.md` method): ≥10 pockets per industry, gate, rubric, `build/buy/fix` only for ≥50/60 with no kill switch. Qualifiers go to `_scorecard-index-phase4.md` | ~13–25 | ~90–150 | same builder, after B | verifier |
| **E** | **Merge gate.** List exactly which shared registers would change (rows appended or regenerated: `_bookmark.md`, `niches/_bookmark.md`, `_scorecard-index.md` via `reindex.py`, `series/_eras.md` wave assignment) and apply them **only on explicit approval**, as a separate commit | — | diff only | single | **Owner approves or declines the merge** |

**Rough total for the 7 core industries:** ~450–520 new files. Adding the optional 4 brings it to ~750–800.

### Execution

There is one builder per industry, and each runs A → B → C for its own slug only. Running them in parallel is safe because each builder writes only `industries/<slug>.md`, `problems/<slug>/` and `niches/<slug>/`, all disjoint. Shared Phase 4 state (this cursor and `_scorecard-index-phase4.md`) is written by the coordinating session alone, after the builders finish.

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

**2026-10-02, reported by the Stage A–C builders (none fixed):**
- Vault `CLAUDE.md` gives `ai-agents-platforms.md` fields as *What it does / Who uses it / Decisions / Why an agent / Compounding value*. Every Phase 2 file uses *Concept / Inputs / Outputs / Why now / Market*. Phase 4 follows Phase 2.
- Vault `CLAUDE.md` says the vault "is not a git repository"; it is one.
- 137 existing `ml-opportunity.md` files (including the `neobanks` reference) have no `#tacit-knowledge-ml` entry, against the repo-level rule. All Phase 4 files carry one, listed first.
- `problems/neobanks/ai-agents-platforms.md` has no `**Derived from:**` line.
- The `_direction.md` §7 verification block and `_state/verify.sh` / `verify-stageb.sh` hard-code `/Users/mac/...`.
- Repo-level `../CLAUDE.md` lists deprecated tags (`#cnn`, `#llm`, `#nlp`…) and repeats queue items 7–35.
- Pass 2 qualifiers in `wealth-management-rias` carry no `**Contested on:**` line, although `_phase2-plan.md` §2 says the filter applies to pockets. Some Phase 4 qualifiers carry it and some don't.

**Cross-industry scoring disagreements inside Phase 4:** see `_scorecard-index-phase4.md` § Cross-industry overlaps. There are six pockets (QoE, distressed credit intelligence, ESG ratings, index methodology, estimates/consensus, portfolio valuation) where parallel builders scored the same population under two industries. Reconcile them before Stage E.

**Unverified claims:** each builder web-checked 1–5 headline figures. All market sizes, niche shares and insight-function headcounts are estimates written with "~". Recalled-but-unchecked facts are listed per industry in the build reports. Fact-check anything before it is used in published content.

---

## CURSOR

**Stage:** A+B+C ✅ complete. Next would be Stage E (merge), held back because it edits existing files
**Stage 0:** ✅ `_state/phase4/verify.sh` written and calibrated against `neobanks`, `payment-fraud-vendors` and `wealth-management-rias`
**Completed:** 7 / 7: hedge-funds (75 files, 3 qualifiers) · asset-managers (71, 2) · sell-side-equity-research (67, 1) · private-equity-firms (71, 2) · investment-banking-boutiques (74, 3) · financial-data-vendors (81, 3) · expert-networks (64, 1)
**Qualifiers:** 15, in `_scorecard-index-phase4.md`
**Optional 4:** not included, since the gap diagnostic didn't prove them
**Verifier:** `bash _state/phase4/verify.sh`
