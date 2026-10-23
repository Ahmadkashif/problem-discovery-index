# Electronic Prior Authorization Networks

**Parent Industry:** [[industries/physician-practices|Physician Practices]]
**Category:** Insight Layer
**Value-Chain Position:** Payer & intermediary layer

## What They Do
Electronic prior authorization networks route drug authorization requests between prescribers, pharmacies and payers, and increasingly medical-service requests too. CoverMyMeds (McKesson) and Surescripts are representative (named from recall). They see request, question set and determination for a large share of national drug authorizations. Some sell aggregate access insight to manufacturers. Claims clearinghouses with authorization products are logged as [[niches/medical-billing/healthcare-clearinghouses/profile|🔍 Healthcare Claims Clearinghouses]] (52).

## Insight Function
**Size:** ~20-100 analysts and data scientists per network (estimate)
**Output:** Network services paid per transaction; aggregate access analytics for manufacturers
**Proprietary data:** National stream of authorization requests and determinations by drug, payer and criterion
**Clock:** Payer decision clocks on each transaction, which bind the payer rather than the network's analysis
**Buyer:** Head of data and analytics at the network

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 2 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 5 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **37/60** |

**Kill switches:** **HIPAA**, and **data isn't theirs**, on the transaction-routing half. Identified requests are processed for prescribers and payers under network agreements, and reuse is limited to what those agreements permit. The aggregate access insight sold to manufacturers is a product the networks already license, so under the product-rights ruling that half carries no switch. Scored alone it is below threshold at ~36 (Q1 4, Q2 2, Q3 4, Q4 2, Q5 2): a small team licensing an owned dataset on its own calendar.
**Verdict:** Logged — kill switch. A unique view of what payers approve, collected as a utility and fenced by the agreements that make it one. The insight product alone sits below threshold.
