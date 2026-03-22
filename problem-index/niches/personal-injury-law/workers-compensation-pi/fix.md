# State-Specific Benefit Calculation Errors

**Niche:** [[niches/personal-injury-law/workers-compensation-pi/profile|Workers' Compensation PI]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Fix (Pain Point)
**One-liner:** Workers' comp attorneys stop miscalculating indemnity benefits — automated state-specific formulas replace the manual spreadsheet calculations where a wrong overtime inclusion rule or an outdated rate cap costs the client thousands.
**Tags:** #logistic-regression #decision-trees #feature-engineering #evaluation-metrics #compliance #worker-facing

## The Problem
Workers' comp benefit calculations are deceptively complex. Computing the Average Weekly Wage (AWW) in New York requires the higher of: (a) average weekly earnings over the prior 52 weeks, or (b) the daily wage multiplied by the number of days worked per week — and the "daily wage" for seasonal workers uses a different formula. In Pennsylvania, overtime is included in the AWW if regularly worked. In California, it's excluded. The compensation rate (typically 66.7% of AWW) is then subject to state-specific maximums that change annually — Pennsylvania's 2025 maximum is different from its 2024 maximum. PPD benefits multiply the compensation rate by a body-part-specific number of weeks from the state schedule. Attorneys perform these calculations manually, using state-published rate tables, and make errors at every step. A 2019 study found that approximately 15% of WC benefit calculations contain at least one error. Each error can cost the client $3,000-$20,000 in underpaid benefits.

## Why It's Still Broken
State WC agencies publish rate tables as PDFs or static web pages, not as API-accessible data. The formulas change with legislative updates, sometimes mid-year. No single reference source covers all 50 states. The AMA Guides (used for impairment ratings that feed PPD calculations) require medical interpretation — the same injury can produce different ratings depending on which edition is used and how the physician applies the rating criteria. Existing practice management tools have no concept of WC benefit formulas — they store the attorney's manually calculated numbers without any validation. There is no "spell check" equivalent for benefit calculations.

## What a Fix Looks Like
A benefit calculation engine with continuously updated state-specific rules. Input: state, date of injury, pay stubs (or manual AWW entry), body part, impairment rating, injury type (occupational disease vs. accident). The engine computes: AWW using the correct state formula, compensation rate with applicable min/max caps for the injury date year, TTD benefit amount and duration, PPD benefit amount using the state's body-part schedule, and total projected benefit entitlement. Output includes a calculation audit trail showing each step and the statutory basis, so the attorney can verify the logic and present it to the WC judge. Alerts flag when the attorney's manual entry differs from the computed amount by more than 5%.

## Who Feels the Pain
Workers' comp attorneys who discover calculation errors when the opposing insurer challenges their numbers at hearing — resulting in credibility damage and delayed benefits for the injured worker. Paralegals who spend hours double-checking calculations against state rate tables that may not be the current version.

## Impact If Fixed
Eliminates the estimated 15% calculation error rate in WC benefit computations. Prevents client financial harm from underpaid benefits — a single corrected AWW calculation can recover $5,000-$15,000 in additional benefits. Reduces calculation time from 30-60 minutes per case to under 5 minutes with validated output.
