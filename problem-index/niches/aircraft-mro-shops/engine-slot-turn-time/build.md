# A Release Date With a Range

**Niche:** [[niches/aircraft-mro-shops/engine-slot-turn-time/profile|Engine Shop Slot & Turn-Time Commitments]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Engine shops quote a single release date at induction and revise it in steps as each delay lands, when they could quote and track a forecast with a range.
**Tags:** #survival-analysis #gradient-boosting #monte-carlo-methods #time-series-forecasting #feature-engineering #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to quote an engine's release date at induction and hit it while parts and repair vendors slip, and whoever keeps the most engines inside their quoted turn time takes the account.

## The Problem
Owners plan fleets around engine release dates: spare-engine leases, aircraft swaps, lease returns. Shops quote a contractual turn time and then report slips as they happen, often late in the visit, when the owner can do little about them. Neither side has a probability attached to the date.

## Why Nobody Has Built This
Shop data needed for a forecast (part-level waits, repair-vendor loop times, test-cell queues) is spread across stores, purchasing and planners' spreadsheets, and rarely timestamped consistently. Contract turn times are commercial promises, and shops have been wary of quoting ranges that show uncertainty to customers.

## What to Build
A forecasting layer over the shop's systems. At induction, a survival model trained on past visits of the same engine type and workscope level gives a release-date distribution. During the visit, a Monte Carlo simulation of open items (parts on order with supplier lead-time history, pieces out at repair vendors with their loop histories, test-cell queue) updates it daily and names which items drive the tail. The customer view shows the median, the 80% date and the three items most likely to move it.

## Target Customer
Production directors and customer programme managers at independent and airline engine shops; powerplant managers at operators planning spare-engine cover.

## Impact If Built
If honest ranges and earlier warnings let owners cut spare-engine lease overlap by ~2 weeks per visit (estimate), that is worth ~$50,000–$100,000 per visit at ~$100,000–$200,000 a month. For the shop, the payoff is a delivery record it can sell.
