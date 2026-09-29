# Short-Term Rental Revenue Management

**Parent Industry:** [[industries/short-term-rentals|Short-Term Rentals]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Set nightly rates for individual listings — base pricing, seasonality, day-of-week, lead time curves, minimum stays and last-minute discounting — for hosts and property managers who otherwise price by intuition.

## Insight Function
**Size:** 60-300 data scientists, revenue analysts, and product staff
**Output:** Nightly rate recommendations, minimum stay and gap-night rules, market demand signals, portfolio revenue reporting
**Proprietary data:** Pricing decisions and booking outcomes across managed listings, plus observed market rates
**Clock:** Daily repricing against booking windows
**Buyer:** VP of Data Science / Head of Revenue Management

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 4 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **42/60** |

**Kill switches:** **platform dependency** — pricing is pushed through platform APIs whose terms and rate limits the platform sets and revises.
**Verdict:** Logged — below threshold and kill-switched. Prices are set and bookings observed for hundreds of thousands of listings, which is a genuine price-response experiment running continuously, and the counterfactual — what the listing would have earned at a different price — is never estimated.
