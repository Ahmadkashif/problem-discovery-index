# Phone Number Quality Degradation in Rural Skip Traces

**Niche:** [[niches/collections-agencies/rural-debtor-outreach/profile|Rural & Low-Connectivity Debtor Outreach]]
**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Skip trace vendors return phone numbers for rural debtors that are 40-60% more likely to be disconnected, reassigned, or wrong-party compared to urban results — but agencies pay the same per-query price and dial them with the same priority.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #data-integration #worker-facing

## The Problem
Rural phone numbers degrade faster than urban numbers: prepaid phone turnover is higher, landline-to-mobile transitions create reassignment gaps, and carrier coverage changes cause number abandonment. Skip trace vendors (LexisNexis, TLO, Accurint) return these numbers without a rural-specific quality adjustment — a number with a "high confidence" score from a vendor may have a 30% contact probability in an urban area but only a 12% probability in a rural area. Agents and dialers burn through Reg F contact attempt limits (7 per 7-day period per number) on numbers that are far less likely to reach the debtor.

## Why It's Still Broken
Skip trace vendors score number quality based on global models that do not account for rural-specific degradation patterns. Agencies accept vendor confidence scores at face value because they lack the data infrastructure to track and compare vendor accuracy by geography. The feedback loop from contact attempts back to vendor quality assessment does not exist — the agency knows a number was bad but does not systematically report this to adjust future scoring.

## What a Fix Looks Like
A post-skip-trace quality adjustment layer that re-scores phone numbers based on rural-specific factors: carrier coverage in the debtor's zip code, phone type (prepaid vs. postpaid), number age, number of other accounts in the database associated with this number, and historical contact rates in the debtor's geographic area. Numbers below a minimum quality threshold are deprioritized or skipped entirely, preserving Reg F attempt limits for higher-quality numbers.

## Who Feels the Pain
Collection agents who waste 30-40% of their call attempts on disconnected or wrong-party numbers in rural portfolios, and operations managers who see systematically lower productivity on rural account assignments.

## Impact If Fixed
Reduces non-productive call attempts on rural accounts by 25-35%, increasing right-party contact rate and improving agent productivity by 15-20% on rural portfolio segments. Preserves Reg F contact attempt limits for higher-probability numbers, increasing the effective reach per account.
