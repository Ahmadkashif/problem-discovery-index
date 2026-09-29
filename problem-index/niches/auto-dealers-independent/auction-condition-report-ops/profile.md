# Wholesale Auction Condition Report Operations

**Parent Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Category:** Insight Layer
**Value-Chain Position:** Payer & intermediary layer

## What They Do
Manheim, ADESA, and the digital wholesale platforms employ large inspection workforces that produce a condition report on every vehicle crossing the block — panel-by-panel damage, mechanical findings, tyre and glass condition, announcements, and a composite grade. Independent dealers buy sight-unseen on the strength of that report, and arbitration decides who pays when it was wrong.

## Insight Function
**Size:** 1,000-5,000 inspectors, condition report writers, and arbitration staff
**Output:** Condition reports and grades, plus market analytics derived from them
**Proprietary data:** Millions of structured condition reports joined to realized sale price and to arbitration outcomes — the only dataset that records both what a vehicle's condition was said to be and whether that turned out to be true
**Clock:** Sale day; the report must exist before the vehicle runs
**Buyer:** VP of Inspection Services / Chief Operating Officer

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 3 |
| Q2 Labor mass + repeatable | ×2 | 5 |
| Q3 Proprietary data moat | ×3 | 5 |
| Q4 External clock | ×2 | 4 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **48/60** |

**Kill switches:** none
**Verdict:** Logged — below threshold; the arbitration-outcome join is the best condition ground truth in used vehicles, but the report is bundled into a transaction fee rather than invoiced as insight

**Embedded-research fit:** 39/45 — qualifies on the delivery-gating rubric; see `_embedded-index.md`. The `/60` score above is unchanged.
## Problems
- [[niches/auto-dealers-independent/auction-condition-report-ops/build|🔨 Build: Arbitration Says Whether the Report Was True and Nobody Adds It Up]]
- [[niches/auto-dealers-independent/auction-condition-report-ops/buy|🛒 Buy: Every Vehicle Is Photographed From Every Angle and the Damage Is Typed by Hand]]
- [[niches/auto-dealers-independent/auction-condition-report-ops/fix|🔧 Fix: Two Inspectors, One Vehicle, Different Grades, Thousands of Dollars]]
