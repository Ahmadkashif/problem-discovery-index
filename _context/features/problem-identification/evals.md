# Problem Identification — Quality Gate

Run these checks after EVERY industry. ALL must pass. If ANY fails, fix before proceeding.

---

## Structural Checks

For each industry `{id}`:

- [ ] All 7 files exist in `problem-index/problems/{id}/`
- [ ] `high-impact.md` — has Type: High Impact, all 4 sections
- [ ] `low-impact-1.md` — has Type: Low Impact (Customisation Opportunity), all 4 sections
- [ ] `low-impact-2.md` — has Type: Low Impact (Customisation Opportunity), all 4 sections, different workflow from low-impact-1
- [ ] `worker-life-1.md` — has Type: Worker Life Changing, all 4 sections
- [ ] `worker-life-2.md` — has Type: Worker Life Changing, all 4 sections, different pain point from worker-life-1
- [ ] `ml-opportunity.md` — has 4-5 entries, tacit knowledge entry listed first
- [ ] `ai-agents-platforms.md` — has 3-4 entries

## Content Checks

### Problem Cards (high-impact, low-impact, worker-life)

| Criterion | PASS | FAIL |
|---|---|---|
| Problem specificity | "OASIS assessments require nurses to answer 100+ items per visit, taking 45-60 minutes of documentation after each home visit" | "Documentation takes too long" |
| Tags present | `**Tags:** #gradient-boosting #time-series-forecasting #tacit-knowledge-ml #worker-facing` | No Tags line, or vague tags |
| Industry link | `**Industry:** [[home-health-agencies\|Home Health Agencies]]` | Missing or broken link |
| Impact quantified | "Reduces documentation time from 60 to 15 minutes per visit, reclaiming 3+ hours per nurse per day" | "Saves time" |

### ML Opportunity Entries

| Criterion | PASS | FAIL |
|---|---|---|
| ML task specified | "Binary classification: will this patient require hospital readmission within 30 days?" | "Predicts patient outcomes" |
| Input data defined | "Structured EHR fields (vitals, medications, diagnoses) + free-text nursing notes from past 6 visits" | "Patient data" |
| Target explicit | "Binary label: readmitted (1) vs. not readmitted (0) within 30 days of discharge" | "Readmission risk" |
| Metric justified | "AUROC with emphasis on recall ≥ 0.85 — false negatives (missed readmissions) cost $15K+ each" | "Accuracy" |
| Scope honest | "2-person team, 3 months. Requires partnership with 1+ home health agency for retrospective data access" | "Easy to build" |
| Data availability assessed | "CMS OASIS dataset publicly available. Agency-specific data requires BAA. Labeling: readmission events are recorded in claims data" | Not mentioned |

### Tacit Knowledge ML

- [ ] At least one entry in `ml-opportunity.md` carries `#tacit-knowledge-ml`
- [ ] That entry is listed FIRST
- [ ] For HIGH-potential industries: tacit knowledge IS the `high-impact.md` problem
- [ ] Tacit knowledge entries explain: data collection challenge, labeling challenge, deployment challenge

### Distinctness Check

- [ ] 5 problem cards cover 5 different workflows (no overlap)
- [ ] 2 low-impact problems address different customization gaps
- [ ] 2 worker-life problems address different individual pain points
- [ ] ML opportunities span at least 3 different techniques/approaches

## Verification Commands

```bash
# Count problem files
ls problem-index/problems/{id}/ | wc -l  # expect 7

# Check for Tags line in all problem cards
grep -l "Tags:" problem-index/problems/{id}/*.md | wc -l  # expect at least 5

# Check tacit knowledge present in ml-opportunity
grep -c "tacit-knowledge-ml" problem-index/problems/{id}/ml-opportunity.md  # expect ≥ 1
```

## STOP GATE

Do NOT proceed to the next industry until every check above passes. An industry with failing checks is an industry that must be rewritten.
