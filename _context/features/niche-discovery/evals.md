# Niche Discovery — Quality Gate

Run these checks after EVERY industry. ALL must pass. If ANY fails, fix before proceeding to the next industry.

---

## Structural Checks

For each industry `{id}`:

- [ ] `_overview.md` exists at `problem-index/niches/{id}/_overview.md`
- [ ] Overview contains table with exactly 8 niches
- [ ] Each niche has a directory with 4 files: `profile.md`, `build.md`, `buy.md`, `fix.md`
- [ ] Total file count: 33 per industry (1 overview + 8 × 4 niche files)

## Axis Coverage

- [ ] Exactly 2 niches categorized as **High Market Share** (🔵)
- [ ] Exactly 2 niches categorized as **Low Digitized** (🟠)
- [ ] Exactly 2 niches categorized as **Underserved Audience** (🟣)
- [ ] Exactly 2 niches categorized as **Highly Automatable** (⚡)

## Content Checks

### Overview Table

| Criterion | PASS | FAIL |
|---|---|---|
| Niche specificity | "Multi-Location DSOs with Centralized Billing" | "Large Practices" |
| Market size present | "$8B" or "~15% of parent industry" | Empty or "N/A" |
| Target buyer specific | "Regional DSO operations manager" | "Practice owner" |

### Profile Files

| Criterion | PASS | FAIL |
|---|---|---|
| Distinct from siblings | Clearly different buyer persona and workflow from other 7 niches | Could be merged with another niche |
| Digital adoption calibrated | "Low-Medium — most use paper intake forms and fax referrals" | "Low" with no explanation |
| Tools & gaps specific | "DrChrono handles scheduling but lacks integrated OASIS scoring" | "Current tools have gaps" |

### Build/Buy/Fix Files

| Criterion | PASS | FAIL |
|---|---|---|
| Niche-specific | Problem is unique to this niche, not a restatement of industry-level pain | Could apply to any niche in the industry |
| Build: genuinely greenfield | Product doesn't exist in any form | Feature request for existing product |
| Buy: names the generic tool | "HubSpot CRM lacks insurance-specific pipeline stages" | "CRM tools don't fit" |
| Fix: structural root cause | Explains why the workaround exists and what creates the structural issue | Just describes the symptom |
| Target customer present | Specific buyer persona with budget context | Missing |
| Impact quantified | "Saves 8 hours/week of manual reconciliation per location" | "Improves efficiency" |

### Link Validation

- [ ] Overview links to all 8 niche profiles
- [ ] Each profile links to its 3 problem files (build, buy, fix)
- [ ] Each problem file links back to niche profile AND parent industry
- [ ] Parent industry link format: `[[industries/{id}|{Industry Name}]]`

## Verification Commands

```bash
# Count niche directories (expect 8)
ls -d problem-index/niches/{id}/*/ | wc -l

# Count total files (expect 33)
find problem-index/niches/{id}/ -name "*.md" | wc -l

# Verify axis distribution in overview
grep -c "High Market Share" problem-index/niches/{id}/_overview.md    # expect 2
grep -c "Low Digitized" problem-index/niches/{id}/_overview.md       # expect 2
grep -c "Underserved Audience" problem-index/niches/{id}/_overview.md # expect 2
grep -c "Highly Automatable" problem-index/niches/{id}/_overview.md  # expect 2
```

## STOP GATE

Do NOT proceed to the next industry until every check above passes. A batch is only complete when all 4 industries pass all checks AND `_bookmark.md` is updated.
