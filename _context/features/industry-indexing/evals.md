# Industry Indexing — Quality Gate

Run these checks after EVERY industry profile. ALL must pass. If ANY fails, fix before proceeding.

---

## Structural Checks

- [ ] File exists at `problem-index/industries/{id}.md`
- [ ] Contains all required sections: Profile, Key Pain Themes, Current Tech Landscape, Problems
- [ ] Profile has all 4 metadata fields: Category, Market Size, Tech Maturity, Workforce
- [ ] Problems section links to exactly 7 documents (high-impact, low-impact-1, low-impact-2, worker-life-1, worker-life-2, ml-opportunity, ai-agents-platforms)
- [ ] All wiki-links resolve to actual file paths

## Content Checks

| Criterion | PASS | FAIL |
|---|---|---|
| Workforce specificity | "Board-certified behavior analysts (BCBAs) supervising registered behavior technicians (RBTs)" | "Healthcare workers" |
| Pain theme specificity | "RBTs spend 30+ min/session on ABA data collection forms, reducing actual therapy time" | "Documentation is a burden" |
| Tech landscape | "Central Reach and CareCloud dominate but lack integrated ABA session data capture" | "Several EHR systems exist" |
| Market size | "$40B US behavioral health market" with source direction | "Large market" |
| Tech maturity calibration | "Medium — EHR adoption is high but interoperability between behavioral health and primary care systems is poor" | "Medium" with no explanation |

## Verification Commands

```bash
# Verify file exists and has correct structure
grep -c "## Profile" problem-index/industries/{id}.md          # expect 1
grep -c "## Key Pain Themes" problem-index/industries/{id}.md  # expect 1
grep -c "## Problems" problem-index/industries/{id}.md         # expect 1
grep -c "\[\[problems/" problem-index/industries/{id}.md       # expect 7
```

## STOP GATE

Do NOT proceed to the next industry until every check above passes.
