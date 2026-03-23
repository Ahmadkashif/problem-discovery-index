# Claims Data Portability on TPA Transitions

**Niche:** [[niches/insurance-tpa/self-insured-employers/profile|Self-Insured Employer Programs]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Fix (Pain Point)
**One-liner:** When self-insured employers switch TPAs, their historical claims data becomes trapped in proprietary formats, destroying continuity in analytics, stop-loss renewals, and care management programs.
**Tags:** #data-integration #compliance

## The Problem
Self-insured employers switch TPAs every 3-5 years due to service issues, cost, or M&A. When they do, their historical claims data must be extracted from the outgoing TPA and loaded into the incoming TPA's system. In practice, outgoing TPAs provide data in proprietary formats with inconsistent coding (procedure codes, diagnosis codes, provider identifiers), incomplete run-out claims, and missing member identifiers. The transition disrupts stop-loss renewals (carriers need prior-year claims data to quote), care management programs (disease management vendors lose patient history), and trend analysis (no apples-to-apples comparison across TPA eras).

## Why It's Still Broken
Outgoing TPAs have no economic incentive to make transitions smooth — they've lost the client. Data extraction is treated as a one-time project, not a product, and is often handled by IT staff pulling ad-hoc queries. There is no industry-standard claims data interchange format beyond the 835 (payment) and 837 (claim submission) EDI transactions, which don't capture adjudication history, accumulator balances, or care management notes. ERISA requires TPAs to provide claims records but doesn't specify format or completeness standards.

## What a Fix Looks Like
A standardized claims data export format — a defined schema covering claims history, member accumulators, authorization records, care management notes, and provider contracts — that every TPA can produce and consume. Paired with a transition management platform that validates completeness, maps coding differences, and reconciles run-out claims between old and new TPAs during the transition period.

## Who Feels the Pain
Employer HR and finance teams lose 3-6 months of analytical continuity during every TPA transition. Incoming TPAs spend 200-400 hours on data conversion for each new client.

## Impact If Fixed
Reduces TPA transition time from 6-9 months to 2-3 months and eliminates $100K-$300K in data conversion costs per transition. Enables employers to switch TPAs without losing analytical continuity, increasing competitive pressure on TPA service quality.
