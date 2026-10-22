# A Graded Archive of Every Cost-per-Hour Projection

**Niche:** [[niches/self-insured-benefit-pools/hw-fund-cost-projection/profile|Health & Welfare Fund Cost Projection & Bargaining Allocation]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Health funds commit members' wages to a projection every bargaining cycle and never check how good past projections were.
**Tags:** #time-series-forecasting #gaussian-processes #bayesian-inference #monte-carlo-methods #evaluation-metrics #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to project a health fund's cost per hour worked across a three-to-five-year bargaining agreement, and whoever's projection keeps the fund's reserve inside the trustees' target band without a mid-contract benefit cut or emergency reallocation takes the account.

## The Problem
Every three to five years the trustees adopt a cost-per-hour projection that fixes the health allocation for the next agreement. The projection carries a trend assumption, a large-claim load, an hours forecast and plan-design adjustments. When the agreement ends, nobody lays the projection beside the cost that actually emerged and asks which assumption missed and by how much. The next projection is built the same way, with the same blind spots.

## Why Nobody Has Built This
Projections live in consultants' workbooks and board minutes, not in a database. Consultants have little incentive to publish their own error rates. Each fund is too small to learn from its own few cycles, and pooling across funds raises data-ownership and HIPAA questions that nobody has resolved.

## What to Build
A projection ledger: every projection stored as its components and assumptions with a date, then automatically compared each quarter with emerged cost per hour and hours. Decompose the miss into trend, large claims, hours and design. Fit Bayesian forecasts that combine the fund's own history with de-identified peer experience, and produce probability bands for the reserve trajectory under each allocation, not a single line.

## Target Customer
Consulting actuaries who want to show trustees a track record, and fund administrators of mid-size and large construction, entertainment and service-trade funds.

## Impact If Built
Trustees would know how far to trust a projection before they take wages to cover it, and the profession would have its first evidence on which assumptions fail.
