# The Stair-Step Missed by Two Units

**Niche:** [[niches/franchised-car-dealers/oem-incentive-reconciliation/profile|OEM Incentive & Stair-Step Reconciliation]]
**Industry:** [[industries/franchised-car-dealers|Franchised Car Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** A store finishes the month two retail units short of a stair-step tier and loses the per-unit bonus on every car it sold, because nobody had an accurate count on the 25th.
**Tags:** #time-series-forecasting #gradient-boosting #data-integration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to claim every programme dollar each sale qualifies for and keep it through OEM audit, and whoever recovers the most incentive dollars per retail unit net of chargebacks takes the account.

## The Problem
Stair-step programmes pay a per-unit amount only if the store reaches a retail target, so the last few units of the month decide the bonus on all of them. The count that matters is the OEM's (reported retail deliveries that pass its rules), and it often differs from the sales board.

## Why It's Still Broken
The OEM count, unwound deals, unreported deliveries and fleet sales excluded from the target sit in different places; the general manager sees the gap late.

## What a Fix Looks Like
A daily projection reconciling DMS deliveries to OEM-reported retail units, excluding ineligible sales, with a month-end forecast and the number of retail units still needed, sent to the general manager from mid-month.

## Who Feels the Pain
General managers and sales managers; controllers explaining the missed bonus.

## Impact If Fixed
Hitting a tier the store would have missed by a few units can be worth tens of thousands in a month at a mid-size store (estimate); knowing the gap on the 15th rather than the 31st is the whole fix.
