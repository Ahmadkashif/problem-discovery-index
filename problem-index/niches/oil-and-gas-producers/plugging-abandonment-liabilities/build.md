# Plugging Cost Models Trained on Actual Invoices

**Niche:** [[niches/oil-and-gas-producers/plugging-abandonment-liabilities/profile|Plugging & Abandonment Liabilities]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators carry plugging liabilities at flat per-well estimates while states and contractors hold thousands of actual plugging costs that would let each well be priced.
**Tags:** #gradient-boosting #linear-regression #feature-engineering #confidence-intervals #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to estimate what each idle well will cost to plug and when the regulator will force it, and whoever's plugging estimates land closest to the final plugging invoices takes the account.

## The Problem
A shallow vertical well with intact casing can be plugged cheaply; a deep, old well with corroded casing, junk in the hole or no records can cost many times more. Operators book asset retirement obligations, and buyers of mature assets price them, using flat averages, so liabilities are misstated in both directions until the plugging rig finds out.

## Why Nobody Has Built This
Actual costs are scattered: operators' AFEs and invoices, contractors' bids, and state-funded plugging records, which are public in some states (recalled). No one has joined them to well attributes at scale.

## What to Build
A per-well cost model trained on actual plugging costs and attributes (depth, casing and cement records, age, well type, state rules, access, known problems), producing an estimate with an interval and the factors behind it. Add a timing model for when each idle well will be forced to plug under state inactive-well rules or bond conditions. Feed every new invoice back to recalibrate.

## Target Customer
Controllers and A&D teams at operators with large mature or idle well counts; buyers of legacy assets and their lenders.

## Impact If Built
For an operator with ~5,000 wells and liabilities in the hundreds of millions (estimate), narrowing per-well estimate error from ~±50% to ~±20% (estimate) changes how assets are priced and which wells are plugged first.
