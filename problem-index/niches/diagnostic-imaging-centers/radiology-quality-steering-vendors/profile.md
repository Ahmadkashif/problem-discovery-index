# Radiology Quality Measurement & Steering Vendors

**Parent Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Category:** Insight Layer
**Value-Chain Position:** Payer & intermediary layer

## What They Do
Firms that measure the diagnostic accuracy of imaging centres and radiologists for health plans and self-insured employers, and steer members toward the better ones. Covera Health is the clearest example. Independent radiologists re-review samples of studies that participating centres send, statistical models estimate error rates, and plans and employers use the ratings to build imaging Centers of Excellence and set cost sharing (Walmart from 2019, later Premera and Blue Cross Blue Shield of Michigan, search summary). The quality ranking is what plans pay for.

## Insight Function
**Size:** ~20-60 data scientists, clinical analysts and methodologists (estimate); radiologists re-reading sampled studies are production
**Output:** Centre- and radiologist-level diagnostic quality scores, Centers of Excellence designations, steering programmes
**Proprietary data:** Second-review discrepancy data across hundreds of centres, joined to plan claims
**Clock:** Plans' network and benefit-design cycles, which are the client's dates
**Buyer:** Health plan VP of network or employer benefits head; the vendor's chief medical officer as the pocket's own buyer

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 5 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **41/60** |

**Kill switches:** **Data isn't theirs**. The work runs on plan claims and on images and reports supplied by centres under service and business-associate agreements, and no checked term shows the vendor may reuse them beyond each client's programme (the vault's rule for client data held under a service agreement).
**Verdict:** Logged — kill switch. The one product in the value chain that grades radiologists' reads against a second opinion at scale. It sits on client-supplied PHI in a market of very few firms.
