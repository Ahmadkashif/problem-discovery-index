# Guest Screening & Damage Protection

**Parent Industry:** [[industries/short-term-rentals|Short-Term Rentals]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Screen guests before arrival for party risk, fraud and identity, and underwrite the damage protection products that pay when a stay goes wrong.

## Insight Function
**Size:** 40-200 data scientists, risk analysts, and claims staff
**Output:** Guest risk scoring and verification, booking approval recommendations, damage claim adjudication, incident analytics
**Proprietary data:** Booking attributes joined to incident and claim outcomes across many properties
**Clock:** Pre-arrival decision windows
**Buyer:** Head of Risk / Chief Product Officer

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 4 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **40/60** |

**Kill switches:** **platform dependency** — guest identity and history are held by the platform and exposed only partially.
**Verdict:** Logged — below threshold. Screens guests on the fragment of identity the platform chooses to expose, and never learns about the bookings it declined.
