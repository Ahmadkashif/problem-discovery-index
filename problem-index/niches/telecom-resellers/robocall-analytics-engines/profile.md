# Robocall Analytics & Call-Labelling Engines

**Parent Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Call-analytics firms such as Hiya, TNS and First Orion score inbound calls in real time and decide whether a handset shows "spam likely", blocks the call, or displays a verified brand. The main buyers are the national wireless carriers, profiled under [[industries/wireless-carriers|Wireless Carriers]], which run the scoring behind their own call-protection apps; MVNOs inherit their host's labels, and VoIP and wholesale providers buy smaller deployments to meet FCC call-blocking expectations. Enterprises buy branded calling and remediation when their legitimate numbers are mislabelled. This is the vault's one profile of these engines.

## Insight Function
**Size:** ~20-80 data scientists, labelling analysts and remediation staff per firm (estimate)
**Output:** Call risk scores and labels, blocking decisions, caller remediation and branded-calling services
**Proprietary data:** Cross-network call outcomes, user spam reports from apps, and labelling history per number, part of it processed from carriers' signalling data under contract
**Clock:** Continuous. FCC rules require blocking providers to offer redress for wrongly blocked calls, but set no dated deliverable.
**Buyer:** Chief product or analytics officer at the analytics firm; its own customers are a few national carriers

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 4 |
| Q2 Labor mass + repeatable | ×2 | 2 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **38/60** |

**Kill switches:** none — carriers supply their signalling data under contracts written for exactly this cross-network scoring, so carrier-sourced inputs reduce the moat score rather than void it, consistent with [[niches/collections-agencies/phone-number-reputation-consent-data/profile|Phone Number Reputation & Consent Data]] (46), the caller-side view of the same labels.
**Verdict:** Logged — below threshold. Scoring is mostly automated, so analyst work grows slowly with volume, and the market is a handful of engines selling to a handful of large carriers.
