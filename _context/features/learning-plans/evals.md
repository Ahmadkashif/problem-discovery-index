# Learning Plans — Quality Gate

Run these checks after EVERY plan. ALL must pass. If ANY fails, fix before finalizing.

---

## Structural Checks

For each plan `{tag-id}`:

- [ ] All 7 files exist in `problem-index/plans/{tag-id}/`
- [ ] `_overview.md` — has prerequisites, 3-project summary table
- [ ] `foundations.md` — covers intuition, math, hyperparameters, pitfalls, limitations
- [ ] `project-1.md` through `project-3.md` — each has all required sections
- [ ] `deployment-guide.md` — practical production guidance
- [ ] `resources.md` — curated list of libraries, papers, datasets
- [ ] `_plans-index.md` updated with new plan entry

## Content Checks

### Project Files

| Criterion | PASS | FAIL |
|---|---|---|
| Sources from vault | Wiki-links to actual `ml-opportunity.md` entry | Generic problem not from vault |
| Dataset recommendations | "Kaggle: Home Credit Default Risk dataset (307,511 rows, 122 features)" | "Find a suitable dataset" |
| Progressive difficulty | Project 1 is clearly simpler than Project 3 | All similar complexity |
| Cross-industry | 3 projects from 3 different industries | Two from same industry |
| 4-phase implementation | Exploration → Baseline → Primary Model → Iteration | Missing phases |
| Evaluation thresholds | "Beginner: AUROC ≥ 0.70, Good: ≥ 0.80, Excellent: ≥ 0.88" | "Maximize accuracy" |
| Metric from source | Uses the evaluation metric defined in the vault's `ml-opportunity.md` | Invents a different metric |

### Foundations File

| Criterion | PASS | FAIL |
|---|---|---|
| Intuition before math | Explains concept conceptually, then formalizes | Starts with equations |
| Focused on 3 projects | Theory supports the specific problems chosen | Generic textbook coverage |
| Pitfalls included | Lists common mistakes with the technique | Only covers happy path |
| Limitations stated | "Don't use this when..." section present | Implies technique is universally applicable |

### Link Validation

- [ ] All project files link to real vault `ml-opportunity.md` entries
- [ ] Links resolve to existing files
- [ ] No reverse links added to vault files (plans only reference, never modify)

## Verification Commands

```bash
# Count plan files (expect 7)
ls problem-index/plans/{tag-id}/ | wc -l

# Verify vault links are valid
grep -o '\[\[problems/[^]]*\]\]' problem-index/plans/{tag-id}/project-*.md

# Check plans index was updated
grep "{tag-id}" problem-index/plans/_plans-index.md
```

## STOP GATE

Do NOT consider the plan complete until every check above passes. A plan with failing checks will mislead learners — fix it before publishing.
