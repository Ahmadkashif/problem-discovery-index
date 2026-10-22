# Commercial Lending Platform Data Teams

**Parent Industry:** [[industries/community-banks|Community Banks]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
The data and analytics groups at commercial loan origination and spreading platforms (nCino, Abrigo, Moody's lending tools, Baker Hill) build portfolio reporting, peer benchmarks and increasingly AI features on the spreads, memos, grades and approvals flowing through their systems from hundreds or thousands of banks. Core processors' equivalent teams are logged under Credit Unions as [[niches/credit-unions/core-banking-vendor-data/profile|🔍 Core Banking Platform Data Teams]] (41, kill switch).

## Insight Function
**Size:** ~50-300 data engineers, data scientists and product analysts per platform (estimate)
**Output:** In-product analytics, benchmarks and AI features sold as part of the platform licence
**Proprietary data:** Spreads, credit memos, risk grades, approvals and exceptions across many banks' commercial lending, the only cross-bank record of credit decisions as made
**Clock:** Software release cycles, internal
**Buyer:** VP of data and AI products

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 2 |
| Q2 Labor mass + repeatable | ×2 | 4 |
| Q3 Proprietary data moat | ×3 | 5 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **41/60** |

**Kill switches:** live — data isn't theirs. The batch test: client loan-level data held under a service agreement is a live kill switch unless checked evidence shows the agreement permits aggregate use. The checked evidence covers only opt-in operational data: nCino's peer benchmarking draws on its Data Community, which it describes as institutions sharing anonymized operational data (cycle times, volumes, win rates). Nothing checked permits aggregate use of the scored corpus (spreads, memos, risk grades, and guarantor records that are customer information under the Gramm-Leach-Bliley Act), so the kill switch stays live; scored consistently with the core platform pocket.
**Verdict:** Logged — kill switch
