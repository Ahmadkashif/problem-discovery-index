# The Lineage Sweep — Spec and Cursor

Single source of truth for this workstream. A fresh session should be able to read only this file and continue correctly.

**To launch a run:** tell a fresh agent `Read _lineage-run.md and execute it.` — `_lineage-run.md` is the standing operating order and takes its scope from the CURSOR below.

**Build log:** `lineage/_bookmark.md` · **Rollup:** `_builder-index.md` · **Verifier:** `bash _state/verify-lineage.sh`

---

## CURSOR

**Status:** COMPLETE — all 250 industries
**Stage:** 12 of 12 — Wave 12, Transformers
**Batch size:** 5 industries
**Scope:** 250 industries, all waves

| | |
|---|---|
| **Completed** | 250 of 250 |
| **Current stage** | W12 — 8 of 8 done |
| **Recently done** | ai-red-teaming-firms ✅ · data-labeling-services ✅ · llm-application-tooling ✅ · synthetic-data-providers ✅ · vector-search-vendors ✅ |
| **Next up** | — |
| **Order** | By wave (chronological, W1→W12), alphabetical within wave. Position is always recoverable from `ls lineage/`. |
| **Rollup** | See `_builder-index.md` |
| **Last regenerated** | 2026-09-25 |

**To resume:** read this file → read `lineage/_bookmark.md` → run `bash _state/verify-lineage.sh` → **check the GATE below** → continue at the first uncompleted industry in the current stage.

## GATE

> **SWEEP COMPLETE 2026-09-25 — 250 of 250.** All waves W1–W12 run (W5–W12 under the owner's standing approval of 2026-09-25). No batch may be launched; the remaining work is owner decisions.
>
> **History:** Stage 1 gate closed 2026-09-21. Stage 2 closed 2026-09-22. Stage 3 closed 2026-09-25 (Wave 4 approved). Stage 4 closed 2026-09-25 with standing approval for W5–W12; stages 5–12 were record-and-continue, findings in `lineage/_bookmark.md`.
>
> **Pending owner decisions** (full list in `lineage/_bookmark.md` § Stage 12 gate): build `origins/` entries for the two nominated builders (`US Congress`, `Amazon`)?; keying rulings (Fannie Mae joint key, YouTube vs Google, IAB Tech Lab vs IAB); possible key moves; a spot re-check of the fetch-only notes (W6 batch C onward) with WebSearch restored.
>
> **When the owner decides:** record the decision and date here, change OPEN to CLOSED, and only then launch the next batch.

---

## 1. What this is, and why it exists

The vault has 250 industries. 66 have a `history/<slug>.md` note; 184 have nothing but a wave assignment. But coverage is not the real problem.

**The real problem is direction.** The existing notes are industry-first — *"here is what happened to this industry."* The series runs the other way: start from a tool the audience already uses, work back to the business case that dictated its shape.

Measured: across all 66 history notes, the phrases `founded by | built by | created by | shipped by` appear **25 times in total, and 46 of the 66 contain none at all.** The corpus names tools freely and names *builders* almost never.

So this is **new research, not a reframing** — and naming the builder is both the most valuable field and the one most likely to tempt fabrication. Rail 3 exists for that reason.

**The second purpose.** `_assessment.md` argued that the vault contains only *buyers* of computing and no *sellers*, and proposed six `origins/` entries to fix it. That list was a guess. This sweep replaces it with evidence: every builder the vault does not own gets logged, and `_builder-index.md` ranks them by how many industries demanded them. The nomination list is an output, not an assumption.

---

## 2. The unit of work

One file per industry: `lineage/<slug>.md`, **450–750 words of body** — measured excluding the `**Sources:**` paragraph, which typically adds another 60–130.

Sources are deliberately outside the band. Counting them would penalise honest citation and negative findings, which is exactly backwards: the reference note's Sources block runs 100 words *because* it records two things it could not establish.

The ceiling is soft, inherited from `series/_plan.md` H4 rule 5: **do not cut sourced, load-bearing material to hit it, and do not pad to reach it.** The reference note's first draft came in at 923 and was trimmed to 733 without losing a claim — expect to overwrite and cut rather than write to length.

### Template — rigid, no conditional headings

```markdown
# Lineage: <Industry Name>

**Industry:** [[industries/<slug>|<Name>]]
**Wave:** [[series/eras/wave-NN-slug|N — Wave Name]]
**The tool:** <a specific named artefact — see Rail 1>
**Builder:** <SHORT CANONICAL NAME ONLY — see below>
**Builder in vault:** <origins/<slug> · industries/<slug> · **ABSENT** · n/a>
**Verification:** <verified · partial · unverified>

## The Problem That Came First
What the work was, and the constraint that made it expensive. Pre-tool.

## What Got Built
The tool or mechanic, named concretely. What it actually did.

## Who Built It, And Why Them
The commercial reason *this* party solved it and not someone else.
The load-bearing section — where the business case dictates the artefact's shape.

## What It Cost
The trade-off taken. What was given up to make the tool work.

## What You Still Touch
The part a person alive today uses without knowing why it is shaped that way.
Links into problems/ and niches/ where the descendant pain lives.

**Sources:**
```

**All five `##` headings are required and none may be renamed.** `history/` allowed renaming and produced 203 distinct heading strings across 66 files, 189 occurring exactly once. That licence is right at 1,500 words and wrong at 500.

**No tags.** Not one of the 66 history notes carries a tag. Lineage notes follow the same rule and the `profile.md` precedent — no `**Tags:**` line, no inline tags.

### `**Builder:**` is an aggregation key, not a sentence

**It must be a short canonical name and nothing else** — `IBM`, `Visa`, `American Bankers Association`, `Bank of America`. Maximum 60 characters, no dates, no founder names, no clauses.

This is load-bearing. `_builder-index.md` aggregates on this string, so `IBM` and `IBM — invented by Forrest Parry (1960), industrialised by…` are two different builders and the count silently splits. The whole point of the rollup is that five industries naming the same builder add up to a nomination; a prose field destroys that.

The founder, the date and the story go in `## Who Built It, And Why Them`, where they belong.

The three non-name values, spelled exactly:
- `no single builder`
- `unknown — searched, not established`
- a short canonical name

*(Caught while writing the reference implementation, before any delegation — which is what writing it by hand was for.)*

---

## 3. The three rails

### Rail 1 — the specificity rule

`**The tool:**` must name a **specific artefact**: a product, a schema, a file format, a mandated code set, a protocol, a piece of hardware. Never a category.

**Rejected values:** "SaaS", "the cloud", "software", "automation", "AI", "digitisation".
**Accepted values:** "the magnetic stripe on a payment card", "ANSI X12 EDI transaction set 204", "CDT procedure codes", "the CLIA certificate", "DICOM".

This rail exists because of a concrete risk. **Wave 6 is 83 industries — a third of the vault — and they all share one mechanic**, the capex→opex pricing shift. Without this rule, 83 notes converge on the same non-answer and the sweep produces nothing. Forcing a named artefact is what makes each note carry information.

If an industry genuinely has no specific artefact, that is Rail 2, not an excuse to write a category.

### Rail 2 — the honest-negative rule

Many industries have no single tool and no single builder. `history/dental-practices.md` models the response — *"There is no moment here. No SABRE, no 8:01am in Troy Ohio."* — and it is **1,945 words, the 7th longest of the 66.** Absence is treated as content, never as licence to write less.

Where there is no single tool, use dental's structure inside `## What Got Built`: a **dated table** of *tool · builder · place · year · what it was for*. That table is already the most tool-first passage anywhere in the vault.

Expect roughly a third of the 250 to resolve this way. Per `_run.md` §5, **that is the expected and correct result, not a shortfall.**

### Rail 3 — the anti-fabrication rule

`**Builder:** unknown — searched, not established` is a **first-class, fully acceptable value**, with the search trail recorded in Sources. This matches the vault's existing *"searched and not corroborated"* convention, which is a stronger status than "unverified".

**Never invent a founder, a company, a date or a place to fill the field.** Given that 46 of 66 existing files name no builder at all, a high `unknown` rate in early batches is honest. A suspiciously low one is the thing to worry about.

---

## 4. Reference implementations

Match these by example rather than by re-reading this spec.

- **`lineage/payment-processors.md`** — this workstream's own reference. Written by hand before any delegation.
- **`history/dental-practices.md`** — the dated table, and how to write the no-origin case at full length.
- **`history/freight-brokerage.md`** — three named layers (Truckstop.com / Scott Moscrip / 1995; TMW Systems / 1983; McLeod Software / 1985; EDI 204, 990, 214, 210), plus its closing move — *"What none of it solved: pricing"* — which names the tool that was **not** built.

---

## 5. Link conventions

All links are `[[path|Display Text]]` — always piped, vault-root-relative, never bare, never `.md`. **Display text must match the target file's H1**, so read it before writing the alias.

```markdown
[[industries/payment-processors|Payment Processors]]
[[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
[[origins/retail-banking/profile|Retail Banking]]
[[problems/payment-processors/high-impact|🔴 <real title>]]
[[niches/payment-processors/fee-and-interchange-optimisation/profile|Fee & Interchange Optimisation]]
```

Wave paths are **zero-padded** (`wave-01-…`), aliases are **not** (`1 — …`), and the alias dash is an em dash.

Origin links in the metadata block use `/profile`; body links may go deep to `/origin-story`, `/the-fight`, `/the-mechanism`, `/legacy` with the alias written as a noun phrase inside the sentence.

Problem emoji map, consistent across all 66 history notes: **🔴** high-impact · **🟡** low-impact-\* · **🟢** worker-life-\*.

`## What You Still Touch` **must** contain at least one `problems/` or `niches/` link. The verifier enforces it.

**Cross-links between lineage notes** are allowed only to files that already exist. Sequential execution makes this safe.

---

## 6. Order of work

Twelve stages, one per wave, chronological. Batching by wave because industries in a wave share ancestors and tooling, so research compounds within a batch — and per `_phase2-plan.md` §3, *"batches are thematic so an interrupted run leaves a coherent block."*

**Authoritative membership is `series/_state/wave-assignment.txt`** (250 rows, `slug|primary|secondary`), not `series/_eras.md`, which is rendered from it:

```bash
awk -F'|' -v n=1 '$2==n{print $1}' series/_state/wave-assignment.txt | sort
```

| Stage | Wave | Industries | Batches of 5 |
|---|---|---|---|
| 1 | W1 Mainframe & batch | 10 | 2 |
| 2 | W2 Departmental & item-level | 16 | 4 |
| 3 | W3 PC & spreadsheet | 16 | 4 |
| 4 | W4 Client–server & ERP | 18 | 4 |
| 5 | W5 The commercial web | 45 | 9 |
| 6 | W6 Cloud & SaaS | 83 | 17 |
| 7 | W7 Big data | 14 | 3 |
| 8 | W8 Mobile & GPS | 16 | 4 |
| 9 | W9 Programmatic | 6 | 2 |
| 10 | W10 Creator platform | 14 | 3 |
| 11 | W11 COVID dislocation | 4 | 1 |
| 12 | W12 Transformers | 8 | 2 |
| | **Total** | **250** | **~55** |

**Every stage ends with a stop-and-report to the owner.** Nothing proceeds to the next wave without a green light.

---

## 7. The rollup — `_builder-index.md`

Every note whose `**Builder in vault:**` is `ABSENT` contributes a row, aggregated across industries:

| # | Builder | Industries demanding it | Waves | First demanded | Nominated? |
|---|---|---|---|---|---|

**The nomination gate:** a builder named by **≥5 industries across ≥2 waves** becomes a candidate `origins/` entry. Below that it is logged and left alone. Deliberately high — nominate few, defend them. **Recalibrate at the Stage 1 gate.**

Regenerated from disk, never hand-incremented.

---

## 8. Files this workstream owns

Written **only** by the orchestrator (lead thread), never by a batch agent:

- `_lineage.md` (this file, incl. the CURSOR)
- `lineage/_bookmark.md`
- `_builder-index.md`
- `_state/verify-lineage.sh`, `_state/lineage_advance.py`

Written **only** by the assignment-holding batch agent, slug-disjoint:

- `lineage/<slug>.md`

Never touched by this workstream at all: `industries/`, `problems/`, `niches/`, `metadata/`, `plans/`, `history/`, `origins/`, `series/`.

> **One exception, logged.** `series/_state/verify-phase3.sh` was amended on 2026-09-21 to exclude `lineage/` from its protected-surface glob, with an in-script comment explaining why. Without it that verifier fails on every note this sweep writes.

---

## 9. Hard rules

- **Additive only.** Never edit `industries/`, `problems/`, `niches/`, `metadata/` or `plans/`.
- **Never parallelise across industries.** Shared files corrupt under concurrent writes, and the cursor is what makes the run resumable.
- **Sub-agents may research; only the assignment-holder writes.** From H4: nested delegation caused forks to race on the same paths and overwrite finished work.
- **Agent reports are not evidence of file state.** Verify from disk with `grep`/`wc`. H4 had an agent report content that was not on disk.
- **Research budget is shared and finite.** WebSearch hit a session-wide cap during H4 and later files are visibly thinner for it. Verify **dated claims only**; when budget runs out, say so in-file rather than guessing.
- **Citation provenance is explicit.** A lineage note citing another vault file must say so and must not present it as independent corroboration.
- **Never invent a builder.** See Rail 3.
- **Never run `_state/advance.py`.** Its bookmark regex is anchored to `\Z` and would delete everything in `niches/_bookmark.md` from the Pass 2 `## Completed` heading to EOF, including the whole Stage B log. This workstream keeps its bookmark in its own file for that reason.
- **Do not repeat the AWS "spare retail capacity" myth.** It is false — Werner Vogels on record; AWS would have exhausted Amazon.com's spare capacity within two months of launch, and the servers were customised and not shareable. The real trigger was the Merchant.com build around 2000 exposing the need for reusable internal services.

---

## 10. Verification

```bash
bash _state/verify-lineage.sh          # after every industry
bash series/_state/verify-phase3.sh    # at every stage boundary — content layers must print 13335
```

`_state/verify-lineage.sh` prints `LINEAGE-OK` on success and exits non-zero on failure. Quote the sentinel into `lineage/_bookmark.md` as evidence the check passed.

---

**Trackers:** `lineage/_bookmark.md` (build log) · CURSOR above (position) · `_builder-index.md` (rollup)
**Created:** 2026-09-21
