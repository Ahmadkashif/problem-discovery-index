# Employment & Income Verification Databases

**Parent Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Category:** Insight Layer
**Value-Chain Position:** Data & benchmark vendors

## What They Do
Specialty consumer reporting agencies that hold payroll records contributed by employers and payroll processors and return instant verifications of employment and income to lenders, landlords, background screeners and government agencies. Equifax's The Work Number is the dominant database, with ~209 million active and ~813 million total records at end-2025; Experian Verify and consumer-permissioned connectors such as Truv and Argyle compete for coverage. Buyers pay per verification.

## Insight Function
**Size:** ~50-200 data scientists, data-quality and analytics staff at the leading database (estimate), far fewer at challengers
**Output:** Verification reports; income and employment attributes; contributor data-quality analysis
**Proprietary data:** Contributed payroll records across hundreds of millions of employment spells — a corpus no one else holds
**Clock:** Point-of-decision lookups on the buyer's timetable; the Medicaid work-verification requirement from 1 January 2027 binds state agencies, not the database
**Buyer:** Chief Data Officer / Head of Verification Products

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 3 |
| Q2 Labor mass + repeatable | ×2 | 2 |
| Q3 Proprietary data moat | ×3 | 5 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **36/60** |

**Kill switches:** lean live, unverified — data isn't theirs to use. The records are employers' payroll data supplied under service and contribution agreements (recalled, often bundled with employer services such as unemployment-claims handling) and released as consumer reports for a permissible purpose; the agreements' terms were not checked, so whether they grant the database rights beyond verification is unknown, and the switch is treated as live until they are.
**Verdict:** Logged — kill switch (36). The product is a point-of-decision lookup on an owned dataset run by a small analytical team (Q2 2, Q4 2, as for the deposit-screening, short-term lending and cash-flow pockets here), and one database dominates (Q5 2).
