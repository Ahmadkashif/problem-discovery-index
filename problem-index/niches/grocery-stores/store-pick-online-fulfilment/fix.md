# The Cost per Order Nobody Measures

**Niche:** [[niches/grocery-stores/store-pick-online-fulfilment/profile|Store-Pick Online Order Fulfilment]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Fix (Pain Point)
**One-liner:** Stores measure pickers in items per hour, which hides the minutes lost to searching, staging, substitutions and handoff that decide whether an online order makes money.
**Tags:** #descriptive-statistics #feature-engineering #evaluation-metrics #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to pick online orders from the store's own shelves, and whoever delivers the lowest labour cost per order at an unchanged fill rate takes the account.

## The Problem
The pick app reports items per hour per picker. The real cost of an order also includes batch set-up, searching for missing items, substitution calls, staging in coolers, re-picks after customer changes, and handoff to a driver or a curbside customer. Most of that is invisible, so improvements target the picker's speed rather than the order's cost.

## Why It's Still Broken
Each step happens in a different tool or none, and e-commerce P&Ls are kept at chain level, not per order.

## What a Fix Looks Like
Timestamp every step from the existing scans (batch start, each pick, not-found, staging, handoff) and compute labour minutes per order by store, hour and order size. Show the top three causes of minutes lost each week, and track fill rate beside it so cost cuts do not come from dropped items.

## Who Feels the Pain
E-commerce leaders asked whether online orders make money; store managers staffing pick shifts; and pickers judged on a rate that ignores the store's errors.

## Impact If Fixed
If a store learns that ~25% of order minutes are search and staging (estimate), halving them cuts ~4 minutes off a ~30-minute order, ~13 hours a day at 200 orders.
