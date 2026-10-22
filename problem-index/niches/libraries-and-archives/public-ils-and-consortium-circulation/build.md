# Holds Routing Across Forty Branches

**Niche:** [[niches/libraries-and-archives/public-ils-and-consortium-circulation/profile|Public Library ILS & Consortium Circulation]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A consortium ILS fills each hold from a rule-picked copy, so items cross the county twice while an idle copy sits one branch away.
**Tags:** #optimization-fundamentals #dynamic-programming #time-series-forecasting #graph-theory #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to fill a patron's hold from any shelf in a shared consortium catalogue in the fewest days, without losing a hold or a patron record when the system changes, and whoever makes daily holds delivery and the migration least risky takes the consortium's shared contract.

## The Problem
When a patron places a hold in a shared catalogue, the ILS picks which library's copy to page using static rules: the patron's home library first, then a lender rotation or nearest-branch list. It does not know that the chosen copy is on a shelf whose staff page items twice a week, that tomorrow's van to the patron's branch is full, or that a returned copy will arrive at the right branch in two days anyway. Patrons wait longer than they need to, and delivery volume grows faster than circulation.

## Why Nobody Has Built This
Holds logic is a small part of an ILS that vendors rarely touch, and the data it needs — paging times, van routes and capacity, transit times — sits outside the ILS in spreadsheets and the delivery contractor's schedule.

## What to Build
An optimiser that, each morning, assigns holds to copies by minimising expected time to pickup and delivery load, using forecasts of returns in transit, branch paging rhythms, van routes and capacities. It writes paging lists back to the ILS and reports wait-time and transit savings per member library.

## Target Customer
Consortium executive directors and delivery coordinators at shared-catalogue consortia and large county systems.

## Impact If Built
Shorter average hold wait times and fewer items in transit — at a large consortium, plausibly a double-digit percentage cut in delivery volume (estimate) — without buying more copies.
