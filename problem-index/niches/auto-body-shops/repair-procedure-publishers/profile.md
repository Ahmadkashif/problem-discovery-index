# Repair Procedure & Service Information Publishers

**Parent Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Category:** Insight Layer
**Value-Chain Position:** Data & benchmark vendors

## What They Do
ALLDATA, Mitchell 1, Identifix, and MOTOR Information Systems take manufacturer service information — repair procedures, position statements, torque specifications, sectioning instructions, ADAS calibration requirements — and turn it into a structured, searchable, vehicle-indexed subscription. Shops cannot perform an OEM-compliant repair without it, and insurers increasingly require documented adherence to it.

## Insight Function
**Size:** 100-400 technical writers, automotive researchers, and data engineers
**Output:** The structured procedure database and technical bulletins — the subscription product
**Proprietary data:** The normalization layer over decades of heterogeneous OEM documentation, plus accumulated technician search and support-call history showing where procedures are ambiguous in practice
**Clock:** Model year releases, OEM position statement updates, recall and service bulletin issuance
**Buyer:** VP of Content / Director of Automotive Research

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 5 |
| Q2 Labor mass + repeatable | ×2 | 5 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 4 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **51/60** |

**Kill switches:** none live — the source documentation is OEM-licensed, which caps Q3, but the structuring layer and the usage history are the publisher's own
**Verdict:** Qualified — indexed
## Problems
- [[niches/auto-body-shops/repair-procedure-publishers/build|🔨 Build: Search Failure as a Map of Where Procedures Are Ambiguous]]
- [[niches/auto-body-shops/repair-procedure-publishers/buy|🛒 Buy: Document Ingestion Adapted to OEM Procedure Structure]]
- [[niches/auto-body-shops/repair-procedure-publishers/fix|🔧 Fix: Nobody Knows Which Procedures Changed Between Model Years]]
