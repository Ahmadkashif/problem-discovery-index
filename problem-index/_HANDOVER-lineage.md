# Handover — The Lineage Sweep

**Date:** 2026-09-24 · **For:** a fresh session taking over as orchestrator.
**Supersedes for current work:** `_HANDOVER.md`, which describes the *previous* task (a vault assessment). That task is finished — its output is `_assessment.md`. Do not redo it.

**Status right now (updated 2026-09-25):** **SWEEP COMPLETE — 250 of 250 notes written.** Both verifiers clean, no agents running. Nothing left to launch; see the Stage 12 gate in `lineage/_bookmark.md` for the owner decisions. Everything below this line is historical.

---

## First action

Read `_lineage-run.md` and execute it. It will send you to `_lineage.md`, whose **GATE block is OPEN (Stage 3 gate, set 2026-09-22 when Wave 3 finished)** — so the correct first move is to report the pending decisions to the owner and **wait**, not to launch a batch.

The cursor will name a Wave 4 batch anyway. That is not approval. Only the GATE block records approval.

Everything below is context that existed only in the conversations that produced this file. The durable state is all on disk.

---

## Where the state lives

| What | Where | Notes |
|---|---|---|
| Spec, **CURSOR**, **GATE** | `_lineage.md` | Single source of truth. Cursor is regenerated from disk; GATE is hand-edited |
| Run order + the batch-agent brief | `_lineage-run.md` | §4 is the prompt you give each batch agent, verbatim |
| Build log, conventions, every stage-gate finding | `lineage/_bookmark.md` | Append-only. ~294 lines; the three gate sections are the substance |
| Evidence rollup | `_builder-index.md` | Regenerated, never hand-edited |
| The notes | `lineage/<slug>.md` | **42 of 250 done** — all of Waves 1–3 |
| Regenerate cursor + index | `python3 _state/lineage_advance.py` | Safe to run any time |
| Verify | `bash _state/verify-lineage.sh` → `LINEAGE-OK` | After every batch |
| Verify vault safety | `bash series/_state/verify-phase3.sh` → `PHASE3-VERIFY-CLEAN` | At every stage boundary |

**State verified 2026-09-24:** `LINEAGE-OK (42 notes)` · `PHASE3-VERIFY-CLEAN` · `content layers (13335) OK` · `protected surface (13352) OK` · no agents running · no partial files.

### Run history

| Stage | Wave | Notes | Gate |
|---|---|---|---|
| 1 | W1 Mainframe & Batch | 10 | closed 2026-09-21 — owner approved W2; word band and nomination gate left unchanged |
| 2 | W2 Departmental & Item-Level | 16 | closed 2026-09-22 — owner said "start with 3"; Rail 3 and keying precedents left unchanged |
| 3 | W3 PC & the Spreadsheet | 16 | closed 2026-09-25 — Wave 4 approved |
| 4 | W4 Client–Server & ERP | 18 | closed 2026-09-25 — owner said "run wave 4 end to end" |
| 5 | W5 The Commercial Web | 45 | **Stage 4 gate OPEN** — 9 batches, awaiting a go |

Waves 2 and 3 were each run as 4 sequential agents (3 batches of 5 + 1 remainder). Roughly 80 minutes of agent time and ~390 tool calls per wave of 16.

---

## The three open decisions at the Stage 3 gate

Full reasoning is in `lineage/_bookmark.md` § Stage 3 gate. Report these and wait.

1. **Proceed to Wave 4?** 18 industries, 4 batches. The only one that blocks work.
2. **The joint builder key `Fannie Mae & Freddie Mac`** (`real-estate-appraisers`). It will not merge with a later note keyed to either GSE alone. Keep joint, or require a single key and accept `unknown` for which GSE designed the URAR. Non-blocking; joint stands until changed.
3. **Rail 3 sits at zero `unknown` builders after 42 notes** — three gates running. Accept, or add a builder-level spot audit per stage. Non-blocking.

The owner has twice approved a wave with a one-word go and left the non-blocking items alone. Expect the same; do not block on them.

---

## What the sweep has found so far (42 of 250)

This is the payload — the reason the run exists. `_builder-index.md` is the machine-readable version.

| Kind of builder | W1 (10) | W2 (16) | W3 (16) | Total |
|---|---|---|---|---|
| Trade association / standards body / SRO | 8 | 6 | 6 | 20 |
| User-funded nonprofit | 0 | 0 | 1 | 1 |
| Government / legislature / GSE | 0 | 1 | 3 | 4 |
| Company | 2 | 6 | 4 | 12 |
| Named individuals | 0 | 0 | 1 | 1 |
| No single builder | 0 | 3 | 1 | 4 |

- **The consortium is the dominant builder, not the vendor.** Roughly half of all builders so far are bodies that convened competitors to agree a format none of them owned. This is the finding that killed `_assessment.md`'s vendor-shaped guess.
- **It is a tendency, not a law.** Wave 2's item-level industries (counters, shops, kitchens, dealerships) were built for by vendors and operators. The split tracks the problem: a format shared between rivals needs a convenor; a machine on one counter needs a manufacturer.
- **Government builds where it is the biggest buyer or the regulator** — Congress, the IRS, the GSEs. New in Wave 3 and rising.
- **Wave 3's headline:** the "PC & Spreadsheet" wave's tools are mostly **not software**. Only 2 of 16 are PC programs; 11 are forms, standards or code sets that predate the PC. The appraiser note says it plainly — *the software filled in the GSEs' grid faster; it did not change the grid.*
- **36 distinct absent builders, and only one has repeated:** `US Congress`, at 2 industries across 2 waves. The ≥5 nomination gate has not fired and probably will not until the horizontal waves (W5–W6).
- **Zero `unknown` builders in 42 notes.** On inspection this is honest rather than lazy: doubt lands at claim level, and every note carries explicit negative findings in its Sources block. The genuinely unattributable industries land in `no single builder` (4).

---

## Keying precedents — apply these to every future note

`**Builder:**` is an aggregation key, not a sentence (`_lineage.md` §2). These decisions were made mid-run and must be followed so the rollup does not silently split:

- **Originator over inheritor.** `specialty-food-retail` is keyed `Computing Scale Company`, not IBM, which acquired the scale by merger in 1911 and sold it in 1934.
- **Standard owner over first vendor** — when the named artefact *is* the interoperable standard. `video-production-smb` is keyed `SMPTE`, not EECO, whose 1967 proprietary code came first. Same logic as BSI over MIL-Q.
- **Build-time name, not today's name.** `Square` not Block · `Convention Industry Council` not Events Industry Council · `Foundation Center` not Candid.
- **Statutes are keyed to `US Congress`.** The administering agency goes in the body.
- **Named individuals are acceptable** when no firm is established at build time — `Leimberg & LeClair` (1984). The later company name contains commas, which the verifier rejects.
- **Joint keys are acceptable but do not merge** — `Fannie Mae & Freddie Mac`. See open decision 2.

---

## How the owner wants this run — decisions from the conversation

- **You orchestrate; agents do all the writing.** One fresh `general-purpose` agent per batch of ≤5 industries, given `_lineage-run.md` §4 verbatim with the slugs filled in. The agent is retired after its batch and never reused — that is how context is managed. The owner wants to be able to talk to you for updates while agents work.
- **Strictly sequential. Never run two agents at once.** The owner's stated reason is fear of exhausting resources, and they are explicitly fine with this taking a long time. Smaller chunks spread out are preferred over speed.
- **Stop at every wave boundary** and get an explicit go before the next stage.
- **Verify from disk after every batch; never trust the agent's report.** Run the verifier, **read at least two of the batch's notes in full**, check nothing was written outside `lineage/`, then regenerate the cursor, append bookmark lines, report to the owner.
- **One-line update to the owner after every batch** — slugs, tools, builders, `unknown` count, flags.
- When told to run a wave "end to end", do not pause between batches for approval; keep going to the wave boundary, then stop.
- **Scope is all 250**, straight through. **Verification is dated claims only.**

### What the batch agents reliably do well, and where they need watching

- They hit the word band (most notes land 730–750) and they flag blocked sources honestly. 403s on vendor pages are the most common blocker.
- They correctly leave the cursor alone, so **every batch ends with `cursor vs disk STALE` and `LINEAGE-VERIFY-FAILED`** until you run `lineage_advance.py`. That is expected, not a failure.
- Watch for builder-side facts resting only on search summaries of pages that would not load (`Xactware`'s founder, NumberCruncher's VisiCalc origin). So far agents have kept these out of the `**Builder:**` key and flagged them "not read at source" — keep checking that they do.
- Nearly every `## Who Built It, And Why Them` argument is the agent's own inference. They have been labelling it as such in-file. That is correct; keep enforcing it.

## How the owner wants to be spoken to

**One short line, point first, plain English.** No headings, bullets or recaps unless they say "explain". An earlier conversation got *"dude, what is your point?"* twice — both times for leading with process and findings instead of the answer. Lead with the answer or the decision you need.

---

## One thing not to act on

**`_assessment.md` recommends six vendor-shaped `origins/` entries** (cloud hyperscalers, packaged software, platform gatekeepers, scientific management, recommenders, accelerated compute). **That list is superseded — do not build it.**

Three waves have now contradicted it: 37 of 42 builders are absent from the vault, and the largest single group is trade associations and standards bodies, not vendors. The owner has been told the assessment was wrong about the *shape* of the gap and accepted that. The sweep exists to replace that guess with a count; `_builder-index.md` is the answer when it is done.

---

## Known hazards (also in `_lineage.md` §9)

- **Never run `_state/advance.py`** — its regex would delete most of `niches/_bookmark.md`.
- **Adding any root `_*.md` file** moves the "protected surface" literal in `series/_state/verify-phase3.sh` (currently 13352). Recompute and update that one number; the `content layers (13335)` tripwire is the one that matters and must never change. *Updating this handover in place, rather than adding a new file, is why that number has not moved.*
- Batch agents must not delegate their file writes — nested delegation caused overwrites in an earlier phase.
- Agent reports are claims, not evidence. One agent in an earlier phase reported content that was not on disk.
