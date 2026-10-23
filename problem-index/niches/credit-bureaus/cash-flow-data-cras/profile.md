# Consumer-Permissioned Cash-Flow Data CRAs

**Parent Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Category:** Insight Layer
**Value-Chain Position:** Data & benchmark vendors

## What They Do
Consumer reporting agencies that build underwriting reports and scores from bank-account data the consumer permissions at application. Plaid set up Plaid Check as a separate FCRA agency whose Consumer Report bundles income, cash-flow attributes and Prism Data's CashScore, used mainly for second looks at declined applicants and better pricing for marginal approvals; Nova Credit and Experian Boost are other examples (named from recall). Lenders pay per report.

## Insight Function
**Size:** ~15-60 data scientists and attribute developers per firm (estimate)
**Output:** Cash-flow consumer reports, income and obligation attributes, cash-flow risk scores
**Proprietary data:** Attribute definitions and performance history on permissioned transactions; the transactions themselves are the consumer's and reachable by any aggregator
**Clock:** Point-of-application decisions; no third-party deadline on the output
**Buyer:** Head of Data Science / Chief Product Officer

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 3 |
| Q2 Labor mass + repeatable | ×2 | 2 |
| Q3 Proprietary data moat | ×3 | 3 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **32/60** |

**Kill switches:** live — data isn't theirs to use. Each consumer authorises access for the credit decision they applied for; reuse of their transactions for model development or analytics beyond that service depends on the consent terms, not on the agency.
**Verdict:** Logged — kill switch (32). A software product over data the consumer controls; the operating contest is covered in [[niches/credit-bureaus/thin-file-consumers/profile|Thin-File & Credit-Invisible Consumers]].
