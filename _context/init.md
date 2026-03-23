# Agent Initialization Protocol

You are an agent working on the **Problem Discovery Index** project. Your job is to build a structured Obsidian knowledge graph of industry problems worth solving — with a focus on machine learning opportunities.

**Read this file before generating ANY output.** No exceptions.

---

## Your Onboarding Checklist

Follow this sequence exactly. Do NOT skip steps. Do NOT proceed past a gate until the condition is met.

### 1. Read all four feature directories

```
_context/features/
├── industry-indexing/       ← COMPLETE — 118 industry profiles
├── problem-identification/  ← COMPLETE — 826 problem files
├── niche-discovery/         ← IN PROGRESS — read session.md for current position
└── learning-plans/          ← NOT STARTED — read feature.md for spec
```

For each directory, read the 4 files in this order:
1. **`feature.md`** — your job assignment for this feature
2. **`session.md`** — where to pick up and what to do next
3. **`thinking-pattern.md`** — how to execute the work correctly
4. **`evals.md`** — quality gates your output must pass

**GATE 1:** Can you state what each feature produces, how many files, and which feature is currently active? If not, re-read. Do NOT proceed.

### 2. Read all four format files

```
_context/formats/
├── tags.md              ← canonical tags + deprecated mappings
├── wiki-links.md        ← exact link patterns for every file type
├── file-templates.md    ← every template — follow exactly
└── output-standards.md  ← file counts + quality checks
```

**GATE 2:** Can you list the deprecated tags that must NOT be used? Can you write a correct wiki-link for each file type? If not, re-read. Do NOT proceed.

### 3. Read the active bookmark file

Read the bookmark file referenced in the active feature's `session.md`. The bookmark is the crash-recovery mechanism — it tells you exactly what has been done and what comes next.

**GATE 3:** You know which industry/batch is next. You know exactly which files to produce. NOW you may begin generating output.

---

## Rules — Absolute, No Exceptions

1. **Every file you create MUST match the template in `formats/file-templates.md`.** Do not add sections. Do not remove sections. Do not rename sections. Do not reorder sections.

2. **Every tag you apply MUST be a canonical tag from `formats/tags.md`.** Check the deprecated list. If the tag you want is deprecated, use the replacement. If there is no replacement, the tag does not exist.

3. **Every wiki-link you write MUST follow the patterns in `formats/wiki-links.md`.** A link that does not resolve to an actual file is a broken vault. Verify before writing.

4. **Every file you produce MUST pass the evals in the relevant `evals.md`.** Output that fails an eval is output that must be rewritten.

5. **Tacit knowledge ML is the highest-priority concept in this project.** Every industry's `ml-opportunity.md` MUST have at least one `#tacit-knowledge-ml` entry listed first. This is not a suggestion.

6. **Update the bookmark after every completed unit of work.** An industry without a bookmark update is an industry that will be accidentally reprocessed. Update it immediately upon completion.

7. **Do not modify existing vault files unless explicitly instructed.** Your job is to generate new files and advance progress.

8. **Specificity is mandatory. Vagueness is failure.** "Improves efficiency" is wrong. "Reduces nurse documentation time from 60 to 15 minutes per home visit" is correct. Every problem names the actual workflow, the actual person, and the actual consequence.

---

## Quick Reference — What Am I Working On?

| Feature | Status | Bookmark Location | Your Action |
|---|---|---|---|
| Industry Indexing | **COMPLETE** | `problem-index/_bookmark.md` | None |
| Problem Identification | **COMPLETE** | `problem-index/_bookmark.md` | None |
| Niche Discovery | **IN PROGRESS** | `problem-index/niches/_bookmark.md` | Read bookmark, resume next batch |
| Learning Plans | **NOT STARTED** | `problem-index/plans/_plans-index.md` | Generate on request |

---

## When You Are Unsure

Read the `thinking-pattern.md` for the feature you are working on. It contains decision frameworks that resolve ambiguity. If the thinking pattern does not cover your case, ask the user. Do NOT guess. Do NOT improvise.
