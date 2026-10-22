# Carrier-Data Identity & SIM-Swap Signal Vendors

**Parent Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Category:** Insight Layer
**Value-Chain Position:** Payer & intermediary layer

## What They Do
Firms that license carriers' subscriber and network signals (phone possession, tenure, recent SIM change or port, line type) and resell checks built on them to banks, fintechs and marketplaces for account opening and payment authentication. Prove and TeleSign are the best-known US examples; buyers pay per API call. The output feeds the identity checks analysed under [[industries/identity-verification-vendors|Identity Verification Vendors]].

## Insight Function
**Size:** ~20-80 risk analysts and data scientists per vendor (estimate)
**Output:** Identity verification results, SIM-swap and port risk signals, fraud scores
**Proprietary data:** None of their own at source; carriers' data under licence plus the vendor's record of past checks and outcomes
**Clock:** Customers' real-time transaction flows; no third-party deadline on the analysis
**Buyer:** Chief risk or data officer at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 3 |
| Q2 Labor mass + repeatable | ×2 | 2 |
| Q3 Proprietary data moat | ×3 | 2 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **29/60** |

**Kill switches:** live — the underlying data is carrier customer information licensed under consent and customer-data rules, revocable by the carriers and not the vendor's to reuse.
**Verdict:** Logged — kill switch. An automated API product on licensed data; the analysts tune models rather than produce billable analysis. The line-type, activity and reassignment checks sold to list compilers from the same carrier-derived signals are logged as [[niches/directory-and-list-publishers/phone-number-intelligence/profile|Phone Number Intelligence & Reassigned-Number Data]] (32, kill switch) under directory and list publishers, ruled the same way.
