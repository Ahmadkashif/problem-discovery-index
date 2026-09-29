# Short-Term Rental Market Data & Analytics

**Parent Industry:** [[industries/short-term-rentals|Short-Term Rentals]]
**Category:** Insight Layer
**Value-Chain Position:** Data & benchmark vendors

## What They Do
Estimate occupancy, average daily rate and revenue for short-term rental supply at market, submarket and individual property level, and sell it to hosts, investors, lenders and municipalities — the only view of an accommodation market that publishes no operating data.

## Insight Function
**Size:** 60-300 data engineers, data scientists, and market analysts
**Output:** Market and submarket performance estimates, property-level revenue projections, investment screening, supply and demand tracking, custom research
**Proprietary data:** Longitudinal listing and calendar observations assembled over years, plus direct submissions from property managers where obtainable
**Clock:** Monthly reporting against investment and pricing decisions
**Buyer:** Chief Data Officer / Head of Research

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 5 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **45/60** |

**Kill switches:** **platform dependency** — occupancy is inferred from calendar availability observed on platforms that control access, change their interfaces, and have both the incentive and the means to stop it.
**Verdict:** Logged — below threshold and kill-switched. Occupancy is inferred rather than observed — a blocked calendar date may be a booking, an owner stay or a host taking a break — and the inference is never validated against the booking data the property managers who subscribe actually hold.
