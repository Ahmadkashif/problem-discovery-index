# Patient Financial Assistance Tools Adapted to the HRSA Schedule

**Niche:** [[niches/community-health-centers/sliding-fee-discount-program/profile|Sliding Fee Discount Programme & Income Documentation]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hospital financial assistance and presumptive-eligibility tools already estimate income and screen for charity care, but a health center needs them recast to its board's sliding fee schedule and HRSA's documentation rules.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to make every sliding-fee discount traceable to documented household income and size under the center's board-approved schedule, and whoever leaves the fewest sliding-fee conditions at HRSA's operational site visit takes the account.

## The Problem
Centers want less friction at the window. Hospitals solved part of this with financial assistance screening, but that is built around charity-care policies and propensity-to-pay scores, not a federally reviewed sliding fee.

## What Already Exists
Hospital presumptive-eligibility and propensity-to-pay tools, patient intake platforms (Phreesia, Clearwave, Luma) and EHR registration workflows.

## The Customization Gap
- the center's schedule: FPL bands, nominal charge and service-specific discounts (dental, pharmacy, lab);
- HRSA's household and income definitions, and the center's re-verification interval;
- estimates used only to prompt documentation, never to replace it, because the discount must rest on what the patient provides;
- bilingual intake and evidence storage that can be sampled for a site visit.

## Target Customer
Centers already licensing an intake platform that want sliding-fee capture moved off the front desk.

## Impact If Solved
Moving income questions to pre-visit intake for half of sliding-fee patients (estimate) cuts window time on discount conversations by ~50%, about 45 minutes a day per representative at ~12 checks a day (estimate).
