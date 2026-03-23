# Output Standards

**After every unit of work, run these checks. If any check fails, fix it before proceeding. Do NOT move to the next industry or batch until every check passes.**

---

## File Count Verification

After completing an industry, VERIFY these exact file counts:

| Feature | Expected Count | Path Pattern |
|---|---|---|
| Industry indexing | 1 industry profile | `industries/{id}.md` |
| Problem identification | 7 problem files | `problems/{id}/{high-impact, low-impact-1, low-impact-2, worker-life-1, worker-life-2, ml-opportunity, ai-agents-platforms}.md` |
| Niche discovery | 33 files | `niches/{id}/_overview.md` + `niches/{id}/{niche-id}/{profile, build, buy, fix}.md` |
| Learning plans | 7 files per plan | `plans/{tag-id}/{_overview, foundations, project-1, project-2, project-3, deployment-guide, resources}.md` |

**Total per fully-indexed industry:** 1 + 7 + 33 = 41 files (excluding learning plans)

---

## Quality Checks — ALL Must Pass

### Content Quality

1. **Specificity** — every problem names the actual workflow, tool, person, and consequence. "Improves efficiency" = FAIL. "Reduces nurse documentation time from 60 to 15 minutes per home visit" = PASS.
2. **Distinctness** — the 5 problem cards within an industry cover different workflows. The 2 low-impacts target different gaps. The 2 worker-lifes target different pain points. Any overlap = FAIL.
3. **ML precision** — `ml-opportunity.md` entries include: input data, target, metric, scope, data availability. Missing any field = FAIL.
4. **Tacit knowledge coverage** — every industry's `ml-opportunity.md` has at least one `#tacit-knowledge-ml` entry listed first. Missing = FAIL. Not listed first = FAIL.

### Tag Validation

1. Tags use ONLY canonical forms from `problem-index/metadata/tags.md`. Deprecated tag = FAIL.
2. 2-5 tags per file, mixing algorithm + task + context tiers. Single-tier tagging = FAIL.

### Link Validation

1. All `[[wiki-links]]` resolve to actual files in the vault. Broken link = FAIL.
2. Industry profiles link to all 7 problem documents. Missing link = FAIL.
3. Problem cards link back to their industry. Missing backlink = FAIL.
4. Niche profiles link to their 3 problem files (build, buy, fix). Missing link = FAIL.
5. Niche problem files link back to both niche profile AND industry. Missing = FAIL.

---

## Bookmark Update — MANDATORY

After each batch, update the relevant `_bookmark.md`:

1. Move completed industries from "In Progress" to "Completed"
2. Set next industry/batch to "In Progress"
3. Update counts and timestamps

**If you skip the bookmark update, the next agent will reprocess your work.** Update immediately after completion — not at end of session.

---

## Verification Commands

Run these to confirm files were created correctly:

```bash
# Count files for an industry (problem identification)
ls problem-index/problems/{industry-id}/ | wc -l  # expect 7

# Count files for an industry (niche discovery)
find problem-index/niches/{industry-id}/ -name "*.md" | wc -l  # expect 33

# Verify no broken wiki-links (spot check)
grep -r '\[\[' problem-index/problems/{industry-id}/ | head -5
```

---

## Batch Size

| Feature | Default batch | Files per batch |
|---|---|---|
| Industry indexing + problem identification | 3-5 industries | 8 files per industry |
| Niche discovery | 4 industries (1 batch) | 132 files per batch |
| Learning plans | 1 plan | 7 files |
