# Run Order — Embedded-Research Phases

**Standing operating order for a fresh agent.** The whole command is:

> Read `_embedded-run.md` and execute it.

This is a **second thesis** over the same vault, run after the 118-industry Pass 2 sweep completed. It does not replace `_run.md`, which is finished (`_direction.md` CURSOR reads `Status: complete`, 118/118).

---

## 0. Orient

1. Confirm working directory is the vault root.
2. Read `_embedded-index.md` in full — it carries the method, the rubric and the ranked candidates.
3. Read the PHASE 1 CURSOR below to find where the run stands. **The cursor is authoritative.**
4. Skim any completed pocket's `build.md` / `buy.md` / `fix.md` (e.g. `niches/crop-farming/ag-retail-agronomy-networks/`) — those are the reference implementation for this thesis.

## 1. The thesis

The primary index (`_scorecard-index.md`) asks *is the insight the invoice?* and rejects, by design, every business where **research is a required step in delivering something else**. This work recovers that population.

- **Eligibility gate: Q1 = 3 exactly.** Not 5 (that is a research firm — primary index), not ≤2 (internal cost centre, no external customer for the work).
- **Fit score = Q2×3 + Q3×2 + Q4×2 + Q5×2, max 45.** Threshold 36.
- **Scores are never recomputed.** A pocket's `_scorecard-index.md` score stands unchanged. This is a different question asked of the same evidence.
- Kill switches apply exactly as in Pass 2. Cross-referenced duplicates are excluded.

## 2. Phase plan

| Phase | Status | What |
|---|---|---|
| **0 — Re-score & index** | ✅ done | `_embedded-index.md` generated from all 1,530 Pass 2 scorecards |
| **1 — Work the top 20** | ✅ done | 20/20 written; 21 pockets now carry worked `build.md` / `buy.md` / `fix.md` (the 21st, Roadside Assistance Network Analytics, already qualified on the primary rubric) |
| **2 — Enterprise tier** | ⏸ awaiting go/no-go | Add new industries where the operator's own delivery requires research. **Do not start without explicit approval from the vault owner** — the scope agreed was "Phase 0 + 1 first, then decide on 2." |

**Phase 2 structural decision, already made by the vault owner: FULL PARITY.** New industries get the complete treatment — `industries/<slug>.md`, `problems/<slug>/` (7 files), `niches/<slug>/_overview.md` + 8 Pass 1 niches × 4 files, then the Pass 2 sweep. No invariant is relaxed; 1:1:1 parity and the exactly-8-niches rule hold for new industries exactly as they do for the existing 118. Roughly 55 files per industry.

Phase 2 candidate first batch (not yet started): P&C insurance carriers · health plans & payers · commercial bank credit underwriting · testing, inspection & certification groups · audit & assurance firms · clinical research organisations · reinsurance & specialty lines · management consulting.

## 3. Phase 1 method, per pocket

1. Read the pocket's existing `profile.md` — it already carries What They Do, Insight Function, scorecard and verdict. **Do not rewrite it or re-score it.**
2. Write `build.md`, `buy.md`, `fix.md` against the fixed templates in `CLAUDE.md`. Wikilinks from `niches/**` use the prefixed form: `[[industries/<slug>|Display]]`.
3. Frame for **this** thesis, not the primary one: the research is a cost of delivery, so the Build case is usually *the by-product corpus is a product* or *the gating judgment is unmodelled*; the Fix case is usually *the research the delivery depends on is undocumented or uncalibrated*.
4. Canonical tags only (`metadata/tags.md`), and **no deprecated tags** — check the Deprecated section, several common tags are retired.
5. Append to the profile: an `**Embedded-research fit:**` line under the existing Verdict, and a `## Problems` link list. Script: `_state/annotate.py` (see Phase 1 close-out below).
6. Regenerate: `python3 <scratchpad>/embedded_index.py` then `python3 <scratchpad>/cursor.py`.
7. Run the Pass 2 verification block from §7 of `_direction.md`.

## 4. Hard rules

- **Additive only.** Never edit a Pass 1 niche, anything under `problems/`, or any `industries/*.md`. Never alter an existing Pass 2 `profile.md` scorecard.
- **No re-scoring.** If a pocket looks better under this thesis, that is what the fit score is for. The `/60` never moves.
- **Log negative results honestly.** If a pocket turns out to have no worked case worth writing, say so in the index rather than manufacturing one.
- Do not parallelise across pockets — `_embedded-index.md` and this cursor are shared files.

## 5. Reporting

Work straight through. Report once at the end with: pockets completed, notable patterns across the worked cases, verification status, and where the cursor sits.

---

## PHASE 1 CURSOR

**Last updated:** {{TS}}
**Status:** {{NDONE}} of 20 worked · {{NTODO}} remaining
**Resume at:** {{NEXT}}

| # | | Directory | Pocket | Fit |
|---|---|---|---|---|
{{ROWS}}

**To resume:** read `_embedded-index.md` → read this cursor → continue at the first ⬜ row → regenerate index and cursor after each pocket.

---

## Phase 1 close-out (run once, when all 20 are ⬜→✅)

1. `python3 _state/annotate.py` — appends the embedded-fit line and `## Problems` list to all 20 profiles.
2. Regenerate `_embedded-index.md` (worked-case prose is preserved across regenerations).
3. Run the full verification block from `_direction.md` §7 plus the tag check in `CLAUDE.md`.
4. Report, then stop for a Phase 2 go/no-go.
