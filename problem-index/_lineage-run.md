# Run Order — The Lineage Sweep

**Standing operating order for a fresh orchestrator session.** The whole command is:

> Read `_lineage-run.md` and execute it.

Optionally: *"…for N batches"* (default 2). Nothing else needs to be pasted — scope comes from the CURSOR in `_lineage.md`, so this file stays correct as the run advances.

---

## 0. Orient

1. Confirm the working directory is the vault root (`industries/`, `niches/`, `problems/`, `metadata/` present).
2. Read `_lineage.md` **in full**. It is the complete spec — template, the three rails, link conventions, vault-safety rules, cursor. Follow it exactly. **Do not redesign the approach.**
3. Read the CURSOR block to find where the run stands. **The cursor is authoritative for position**, not any list in this file.
3a. **Read the GATE block directly under it.** If it says OPEN, **do not launch any batch** — report the pending decisions to the owner and wait. The cursor is regenerated from disk and will name a next batch regardless of whether that stage has been approved; the GATE is the only record of approval.
4. Read `lineage/payment-processors.md` — it is the reference implementation. Match its shape, density and honesty conventions.
5. Run `bash _state/verify-lineage.sh` before starting. If it is already failing, fix that first.

## 1. Scope this run

Batch size is **5 industries**. Default run length is **2 batches**, starting at the first uncompleted industry in the current stage. Order is by wave, alphabetical within wave:

```bash
awk -F'|' -v n=<stage> '$2==n{print $1}' series/_state/wave-assignment.txt | sort
```

Skip anything that already has a file in `lineage/`. **Never cross a stage boundary in the same run** — stop and report at the end of a wave.

## 2. The orchestration loop, per batch

**The orchestrator does not author notes.** It spawns, verifies, merges and reports.

1. **Derive the batch** — next 5 uncompleted slugs in the current stage.
2. **Spawn one fresh agent** with the brief in §4 below, filled in with those 5 slugs. One agent per batch. **Never two at once.**
3. **Verify from disk** when it returns — `bash _state/verify-lineage.sh`, plus read at least two of the five notes in full. **The agent's report is a claim, not evidence.**
4. **Merge** — regenerate the cursor and rollup (`python3 _state/lineage_advance.py`), append one bookmark line per industry to `lineage/_bookmark.md`, quote the `LINEAGE-OK` sentinel.
5. **Retire the agent.** Never reuse it. The next batch gets a new one with a clean context.
6. **Report to the owner** in a few lines: slugs done, tools and builders found, how many `unknown`, anything flagged.

If a batch comes back bad: delete the offending files, respawn a fresh agent against the same slugs with the specific failure named. Do not try to repair by conversation with the original agent.

## 3. Hard rules

- **Additive only.** Never edit `industries/`, `problems/`, `niches/`, `metadata/` or `plans/`. This workstream also does not edit `history/`, `origins/` or `series/` — the one logged exception is recorded in `_lineage.md` §8.
- **Do not parallelise across industries.** `_lineage.md`, `lineage/_bookmark.md` and `_builder-index.md` are shared files; concurrent writes corrupt the index and the cursor, and the cursor is what makes the run resumable.
- **Only the assignment-holder writes.** A batch agent may research however it likes but must not delegate its file writes.
- **Never run `_state/advance.py`** — see `_lineage.md` §9.
- **Log negative results honestly.** An industry with no tool and no builder is a finding. Never manufacture an origin event, never invent a builder, and never widen a definition to fill a field. If a batch produces four `unknown` builders, report four.

## 4. The batch-agent brief

Copy this verbatim into the agent prompt, substituting the five slugs and the wave. It is deliberately self-contained — the agent needs no conversation history.

---

> You are writing five notes in an Obsidian vault at `/Users/mac/Desktop/code/personal/problem-index`. Work sequentially, one industry at a time.
>
> **Read first, in this order:** `_lineage.md` (the complete spec — template, three rails, link conventions), then `lineage/payment-processors.md` (the reference implementation), then `history/dental-practices.md` (how to write the no-origin case).
>
> **Your slugs:** `<slug1>`, `<slug2>`, `<slug3>`, `<slug4>`, `<slug5>` — Wave `<N>`.
>
> **Write only** `lineage/<slug>.md` for those five. Write **nothing else** — not the bookmark, not the cursor, not `_builder-index.md`, not any file under `industries/`, `problems/`, `niches/`, `history/`, `origins/` or `series/`. Those belong to the orchestrator.
>
> **You may research with WebSearch/WebFetch, but you must not delegate your file writes to a sub-agent.** Nested delegation has previously caused forks to race and overwrite finished work.
>
> **The question each note answers:** which specific tool exists because of this industry's problem, and who built it and why them? Start from the artefact, work back to the business case. Do not write "this industry had a problem, so technology arrived" — that is the direction this sweep exists to reverse.
>
> **The three rails are non-negotiable:**
> 1. `**The tool:**` names a *specific artefact* — a product, schema, file format, code set, protocol or piece of hardware. "SaaS", "the cloud", "software", "automation", "AI" are rejected values.
> 2. If there is genuinely no single tool, say so and use a dated table of *tool · builder · place · year · purpose*. Absence is content, not licence to write less.
> 3. `**Builder:** unknown — searched, not established` is a first-class acceptable value with the search trail in Sources. **Never invent a founder, company, date or place.** A high `unknown` rate is honest; a suspiciously low one is not.
>
> **`**Builder:**` is an aggregation key, not a sentence.** Short canonical name only — `IBM`, `Visa`, `American Bankers Association`. Max 60 characters, no dates, no founder names, no commas, no parentheses. `_builder-index.md` aggregates on this exact string, so a prose value silently splits the count. The founder, date and story go in `## Who Built It, And Why Them`. The only non-name values are `no single builder` and `unknown — searched, not established`, spelled exactly.
>
> **Body length is 450–750 words**, measured excluding the `**Sources:**` paragraph. Sources are outside the band on purpose — never shorten a citation or drop a negative finding to hit a word count.
>
> **Verify dated claims only.** Anything you cannot confirm, write as an explicit negative finding rather than asserting it. If your search budget runs out, say so in-file.
>
> **Known myth — do not repeat it:** AWS was *not* built from Amazon's spare retail capacity. Werner Vogels has said so on record.
>
> **Before finishing**, run `bash _state/verify-lineage.sh` and fix anything it flags in your own five files.
>
> **Report back** in under 200 words: for each slug, the tool and the builder in one line each; the count of `unknown` builders; and anything you could not verify. Do not summarise the notes' contents — the orchestrator reads the files.

---

## 5. Reporting

Report to the owner after **every batch**, not at the end of the run. Keep it to a few lines — slugs, tools, builders, `unknown` count, flags.

**Stop and report immediately if** (a) verification fails twice on the same issue, (b) a stage boundary is reached, or (c) context is running low. In every case: finish the current industry, regenerate the cursor, append bookmark lines, verify, then report where the cursor sits. **Never leave the cursor stale. Never lower quality to cover more ground.**

## 6. Quality bar

The reference implementation is one note at roughly 550 words with a named artefact, a named builder, a dated origin and an explicit trade-off.

**Most industries will be thinner than that, and several will have no builder at all.** Across the 66 existing history notes, 46 name no builder anywhere — so `unknown` is the expected outcome in a large minority of cases, not a failure. The map's value is as much in the industries that built nothing as in the ones that built something.
