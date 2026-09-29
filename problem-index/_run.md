# Run Order — Insight-Layer Discovery

**Standing operating order for a fresh agent.** The whole command is:

> Read `_run.md` and execute it.

Optionally: *"…for N batches"* (default 5). Nothing else needs to be pasted — scope comes from the CURSOR in `_direction.md`, so this file stays correct as the run advances.

---

## 0. Orient

1. Confirm working directory is the vault root (`industries/`, `niches/`, `problems/`, `metadata/` present).
2. Read `_direction.md` **in full**. It is the complete spec — method, rubric, write format, vault-safety rules, cursor. Follow it exactly. Do not redesign the approach.
3. Read the CURSOR block to find where the run stands. **The cursor is authoritative**, not any list in this file.
4. Skim `niches/accounting-firms-smb/` — it is the reference implementation. Match its `profile.md` format, its scorecard tables, and its `_overview.md` Pass 2 section exactly.

## 1. Scope this run

Batch size is 5 industries. Default run length is **5 batches (25 industries)**, starting at the first uncompleted industry in the cursor. Order is alphabetical:

```bash
ls industries/*.md | sed 's|industries/||; s|\.md$||'
```

Skip anything already listed as Completed in the cursor.

## 2. Per industry, in order

1. **Sweep all seven value-chain positions** (§5 of `_direction.md`). Find **at least 10 pockets**. Go granular — small, specific sub-pockets are wanted.
2. **Apply the gate before scoring anything.** Does the pocket plausibly hold a dedicated research/insight function of **10+ people**? Gate failures still get a plain profile and `Verdict: Logged — fails gate`. They are never scored and never indexed.
3. **Score survivors** on the five-question rubric. Kill switches are binary and assessed separately — never averaged into the score.
4. **Write files.** `profile.md` for every pocket, written **plainly**: what they do, insight function size, output, proprietary data, clock, buyer, then the scorecard. `build.md`/`buy.md`/`fix.md` **only** for pockets scoring ≥50 with no live kill switch.
5. **Append** the `## Pass 2 — Insight-Layer Discovery` section to that industry's `_overview.md`, below a `---`. Never touch the Pass 1 half.
6. **Add qualifiers** to `_scorecard-index.md` — ranked table row plus a short case.
7. **Update the CURSOR** in `_direction.md` and the Pass 2 section of `niches/_bookmark.md`.
8. **Run the verification block** from §7 of `_direction.md`. If it fails, fix before moving on.

Steps 7 and 8 run after **every industry**, not every batch. An interrupted run must never lose more than one industry.

## 3. Hard rules

- **Additive only.** Never edit, move, or delete any Pass 1 niche, anything under `problems/`, or any `industries/*.md`. The 944 Pass 1 niches stay at exactly 4 files each.
- **Canonical tags only** (`metadata/tags.md`). No deprecated tags. `profile.md` carries no Tags line.
- **Prior deployments (agriculture, sports, private equity) carry ZERO scoring weight.** They are credibility references, not a pattern to match. Do not reintroduce adjacency as a criterion.
- **Log negative results honestly.** An industry yielding mostly gate-failures is a valid finding, not a shortfall. Never inflate a score, never move the ICP goalposts, and never widen the gate to manufacture candidates. If a whole batch produces two qualifiers, report two.
- **Do not parallelize across industries.** `_direction.md`, `_scorecard-index.md`, `niches/_bookmark.md`, and each `_overview.md` are shared files; concurrent writes corrupt the index and the cursor, and the cursor is what makes the run resumable.

## 4. Reporting

Work straight through. **Do not check in between industries or batches.** Report once at the end with:

- Industries completed this run
- Total pockets logged; split by qualified / below threshold / failed gate
- New index entries: name + score
- Notable gate-failure patterns — which value-chain positions came up empty, and in which kinds of industry
- Verification status
- Where the cursor now sits

**Stop early and report ONLY if** (a) verification fails twice on the same issue, or (b) context is running low. In either case: finish the current industry, update cursor and bookmark, run verification, then report where you stopped. Never leave the cursor stale. Never lower quality to cover more ground.

## 5. Quality bar

The reference industry produced 15 pockets: 7 qualified, 5 below threshold, 3 failed the gate. Accounting is unusually rich because tax law is a permanent externally-driven research burden — **most industries will yield fewer qualifiers, and several will yield none.** That is the expected and correct result. The map's value is as much in the empty positions as the full ones.
