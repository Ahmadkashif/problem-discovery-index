# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

An **Obsidian vault**, not a software project — there is no build system, no tests, no package manager, and it is not a git repository. It contains ~4,855 markdown notes forming a structured research index of business problems in 118 US SMB industries, tagged against a canonical math/ML topic registry, which then feeds project-based ML learning plans.

Work here is authoring and maintaining markdown under strict structural conventions. The conventions below are enforced by consistency across hundreds of files — deviating breaks the vault's queryability.

## The four content layers

```
industries/<slug>.md            118 files — one hub note per industry
problems/<slug>/                118 dirs × 7 files — industry-level problem analysis
niches/<slug>/                  118 dirs — _overview.md + exactly 8 niche subdirs
niches/<slug>/<niche>/          944 dirs × 4 files — niche-level opportunity analysis
metadata/                       tag registry + ML/math topic taxonomies
plans/                          project-based learning paths (self-contained)
```

`industries/`, `problems/`, and `niches/` are keyed by the **same slug** and are in exact 1:1:1 parity. Adding an industry means adding all three at once.

`industries/<slug>.md` is the hub: Profile / Key Pain Themes / Current Tech Landscape, then link lists into `problems/<slug>/`.

`problems/<slug>/` always contains exactly these 7 files:
- `high-impact.md`, `low-impact-1.md`, `low-impact-2.md`, `worker-life-1.md`, `worker-life-2.md` — the five problem notes
- `ml-opportunity.md` — numbered ML problem formulations derived from the five above
- `ai-agents-platforms.md` — numbered agent/platform concepts derived from the five above

`niches/<slug>/_overview.md` holds the four-axis niche selection table and rationale; each of its 8 subdirs contains `profile.md`, `build.md`, `buy.md`, `fix.md`.

**Pass 2 (`Category: Insight Layer`) is an active second sweep** — see `_direction.md` for the full method and cursor, and `_run.md` for the standing run order (a fresh agent is launched with just "Read `_run.md` and execute it"; `_scorecard-index.md` holds qualifying findings). Pass 2 niches sit alongside Pass 1 niches in the same industry directories and deliberately relax one invariant: they carry **1 file (profile only) or 4 files**, because build/buy/fix is written only for pockets that clear the scoring threshold. Do not "fix" a Pass 2 niche that has only a profile. Pass 1's 944 niches and every file under `problems/` and `industries/` are append-only from here — never edit them.

## Note templates

Each note type has a fixed heading set. Match it exactly when authoring.

| File | `## ` headings |
|---|---|
| `industries/<slug>.md` | Profile, Key Pain Themes, Current Tech Landscape, Problems, Analysis |
| `problems/*/high-impact.md` | The Problem, Why It's Unsolved, What a Solution Looks Like, Impact If Solved |
| `problems/*/low-impact-{1,2}.md` | The Problem, What Already Exists, The Customisation Gap, Impact If Solved |
| `problems/*/worker-life-{1,2}.md` | The Problem, Why It Matters to the Worker, What a Solution Looks Like, Impact If Solved |
| `problems/*/ml-opportunity.md` | numbered `## N. <Title>` sections |
| `problems/*/ai-agents-platforms.md` | numbered `## N. <Title>` sections |
| `niches/*/_overview.md` | Niche Selection (table), Why These Niches, Niches |
| `niches/*/*/profile.md` | Profile, What Makes This a Distinct Niche, Current Tools & Gaps, Problems |
| `niches/*/*/build.md` | The Problem, Why Nobody Has Built This, What to Build, Target Customer, Impact If Built |
| `niches/*/*/buy.md` | The Problem, What Already Exists, The Customization Gap, Target Customer, Impact If Solved |
| `niches/*/*/fix.md` | The Problem, Why It's Still Broken, What a Fix Looks Like, Who Feels the Pain, Impact If Fixed |

Note the deliberate spelling split: `low-impact-*.md` uses "Customi**s**ation Gap", `buy.md` uses "Customi**z**ation Gap".

### Metadata block

Bolded key-value lines sit directly under the H1, before the first `## `:

- Problem notes (`high-impact`, `low-impact-*`, `worker-life-*`): `**Industry:**`, `**Type:**`, `**One-liner:**`, `**Tags:**`
- Niche opportunity notes (`build`, `buy`, `fix`): `**Niche:**`, `**Industry:**`, `**Type:**`, `**One-liner:**`, `**Tags:**`
- `profile.md`: `**Parent Industry:**`, `**Category:**` — then a `## Profile` block of `**Market Size:**`, `**Share of Parent Industry:**`, `**Digital Adoption:**`, `**Target Buyer:**`, `**Automation Potential:**`. **No `**Tags:**` line** on profiles.
- `ml-opportunity.md` / `ai-agents-platforms.md`: `**Industry:**`, `**Derived from:**` (links to all five problem notes)

`**Type:**` values are fixed strings: `High Impact`, `Low Impact (Customisation Opportunity)`, `Worker Life Changing`, `Build (Greenfield Opportunity)`, `Buy & Customize (Vertical Adaptation)`, `Fix (Pain Point)`.

`profile.md`'s `**Category:**` is one of the four discovery axes: `High Market Share`, `Low Digitized`, `Underserved Audience`, `Highly Automatable`. Each industry's 8 niches are two per axis.

### Numbered-section notes

In `ml-opportunity.md`, each `## N.` section carries a tag line then: `**Problem statement:**`, `**ML task:**`, `**Input data:**`, `**Target:**`, `**Evaluation metric:**`, `**Scope:**`, `**Data availability:**`, separated by `---`.

In `ai-agents-platforms.md`: `**What it does:**`, `**Who uses it:**`, `**Decisions it makes/augments:**`, `**Why an agent:**`, `**Compounding value:**`.

## Tag discipline

`metadata/tags.md` is the single source of truth — a canonical registry where every tag maps 1:1 to a topic in `metadata/math-topics.md` (64 math topics) or `metadata/ml-roadmap.md` (15-level ML dependency graph). **Only registry tags may be used.** If a concept isn't listed, it gets no tag.

The registry ends with a "Deprecated (do not use)" section mapping old coarse tags to their replacements (`#cnn` → `#cnns`, `#llm` → `#large-language-models`, `#nlp` → use `#bert`/`#transformers`/`#large-language-models`). Never reintroduce a deprecated tag.

Context tags (`#quick-win`, `#tacit-knowledge-ml`, `#automation`, `#data-integration`, `#workflow-orchestration`, `#compliance`, `#worker-facing`, `#revenue-impact`, `#ai-agent`, `#ai-platform`) mix freely with technique tags.

The vault is currently 100% tag-clean. Verify after edits:

```bash
grep -rhoE '(^|\s)#[a-z][a-z0-9-]{2,}' problems niches --include='*.md' | tr -d ' ' | sort -u > /tmp/used.txt
grep -o '^#[a-z0-9-]\+' metadata/tags.md | sort -u > /tmp/canon.txt
comm -23 /tmp/used.txt /tmp/canon.txt   # should be empty
```

## Wikilink conventions

Link style varies **by source directory** — this is established, not accidental. Match the sibling files:

- From `industries/<slug>.md` → vault-root paths: `[[problems/dental-practices/high-impact|🔴 High Impact: ...]]`
- From `problems/<slug>/*.md` → bare industry slug: `[[dental-practices|Dental Practices]]`
- From `niches/**` → prefixed path: `[[industries/dental-practices|Dental Practices]]`

Emoji prefixes in link lists: 🔴 High Impact · 🟡 Low Impact · 🟢 Worker Life · 🧠 ML Opportunities · 🤖 AI Agents & Platforms · 🔵 High Market Share · 🟠 Low Digitized · 🟣 Underserved Audience · ⚡ Highly Automatable · 🔨 Build · 🛒 Buy · 🔧 Fix.

`plans/` deliberately does **not** wikilink into the industry/problem layers — plans are self-contained and reference source problems in prose only.

## Progress trackers

Two bookmark files must be updated when content is added — they are the vault's build log:

- `_bookmark.md` — industry-level coverage (Completed / In Progress / Queue), with a `Last updated:` ISO timestamp. Currently 118/118.
- `niches/_bookmark.md` — niche generation log by batch (4 industries × 8 niches × 4 files + 1 overview = 132 files per batch). Currently complete: 30 batches, 944 niches.

## plans/

A plan is a project-based learning path for one ML technique. `plans/_plans-index.md` is the registry, sectioned By Algorithm / By Task Type / By Domain. Only `linear-regression` exists so far; it establishes the shape:

```
plans/<technique>/_overview.md          why-start-here, prerequisites, project table, timeline
plans/<technique>/foundations.md        math + intuition before any code
plans/<technique>/project-{1,2,3}.md    beginner → advanced; each has The Problem, Dataset,
                                        ML Task, Evaluation Criteria, Implementation — 4 Phases
plans/<technique>/resources.md          libraries, sklearn classes, dataset links
plans/<technique>/deployment-guide.md   notebook → production
plans/<technique>/briefs/<file>.md      teaching-agent prompts, one per plan file
```

Projects draw their problems from the vault's industry/problem notes and follow a fixed 4-phase implementation arc: Exploration → Baseline → Primary Model → Iteration.

`briefs/` are second-person prompts written **for a teaching agent**, not for the learner — they address the vault owner ("Ahmad") by name and specify analogies, pacing, and what to reinforce. When editing a plan file, check whether its brief needs the matching update.

## Verification commands

There is nothing to build or test; these structural checks stand in for it.

```bash
# 1:1:1 parity across the three keyed layers (both should print nothing)
comm -3 <(ls industries | sed 's/\.md$//' | sort) <(ls problems | sort)
comm -3 <(ls industries | sed 's/\.md$//' | sort) <(ls niches | grep -v '_bookmark' | sort)

# every industry has exactly 7 problem files; every industry has exactly 8 niches
find problems -mindepth 1 -maxdepth 1 -type d | while read d; do echo "$(ls $d | wc -l) $d"; done | grep -v '^ *7 '
for d in niches/*/; do echo "$(ls -d $d*/ 2>/dev/null | wc -l) $d"; done | grep -v '^ *8 '

# every niche has exactly build/buy/fix/profile
find niches -mindepth 2 -maxdepth 2 -type d | while read d; do echo "$(ls $d | wc -l) $d"; done | grep -v '^ *4 '

# heading-set drift for a note type
grep -h '^## ' niches/*/*/fix.md | sort | uniq -c | sort -rn
```

The vault is small enough (~4,855 files, all prose markdown) that `grep -r` across everything is instant — prefer targeted greps over reading files wholesale.
