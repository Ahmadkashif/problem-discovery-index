# State Medicaid Rule Engine

**Niche:** [[niches/estate-planning/elder-law-medicaid/profile|Elder Law & Medicaid Planning]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Benefits eligibility engines exist for social services programs — but none encode the specific Medicaid long-term-care eligibility rules that elder law attorneys need to advise clients on asset protection strategies.
**Tags:** #decision-trees #feature-engineering #evaluation-metrics #compliance #data-integration

## The Problem
Elder law attorneys must know their state's precise Medicaid long-term-care rules: countable vs. exempt asset categories, income methodologies (income-cap vs. medically needy), community spouse resource allowance calculations, home equity limits, look-back period penalty divisors, and transfer penalty calculation methods. These rules change annually (new income limits, updated penalty divisors, revised home equity caps) and vary dramatically between states. Attorneys track these changes through state bar publications, CLE courses, and NAELA (National Academy of Elder Law Attorneys) updates — a manual, error-prone process where missing a rule change can result in a client's Medicaid application being denied.

## What Already Exists
Benefits screening tools (BenefitsCheckUp, Single Stop) determine general program eligibility across dozens of social services programs but treat Medicaid as a yes/no eligibility check, not a planning tool. Healthcare.gov handles Medicaid income eligibility for non-long-term-care coverage. State Medicaid agency websites publish rules but in dense policy manual format, not in a queryable or calculable form. Legal research platforms (Westlaw, LexisNexis) provide case law and regulatory text but not computational rule engines.

## The Customization Gap
The missing layer transforms Medicaid long-term-care rules from regulatory text into a computational engine. For each state, it must encode: asset categorization rules (which assets count, which are exempt, with dollar thresholds), income methodology (gross income cap vs. net income with medical expense deductions), community spouse protections (minimum and maximum resource allowances, income allowances), transfer penalty calculations (look-back period, penalty divisor, undue hardship exceptions), and special rules (Miller trusts for income-cap states, pooled special needs trust provisions). The engine must update when rules change — ideally by monitoring state Medicaid agency publications and flagging changes for attorney review before automatic incorporation.

## Target Customer
Elder law attorneys who currently maintain personal reference materials (binders, spreadsheets, bookmarked state agency pages) for their state's Medicaid rules and must verify currency before every client consultation.

## Impact If Solved
Eliminates 30-60 minutes per case of rule verification and manual calculation. Prevents eligibility miscalculations from outdated rule references — a single error can delay Medicaid eligibility by months, costing families $8,000-$15,000/month in private-pay nursing home costs. Enables multi-state practices to handle cases across jurisdictions without maintaining separate rule libraries for each state.
