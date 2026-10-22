# Pocket Productivity Model for the Renewal Line Review

**Niche:** [[niches/greeting-card-publishers/mass-channel-card-departments/profile|Mass, Drug & Grocery Card Departments]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A publisher defending or attacking a card department contract argues from department averages, when the case that wins is what each pocket earns, why, and what it would earn after a refresh.
**Tags:** #time-series-forecasting #bayesian-inference #causal-inference #k-means-clustering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to win the retailer's whole card department at the multi-year contract renewal by proving, pocket by pocket in the retailer's own scan data, more sales per linear foot net of shrink than the incumbent publisher, and whoever proves it takes the department.

## The Problem
A card department contract runs for years and carries upfront incentives the publisher earns back only through purchases. At renewal the retailer's buyer compares the incumbent's department productivity with what the challenger promises. Both sides argue from averages: sales per linear foot by store, by occasion, year on year. Pocket-level reality is messier. Eye-level pockets outsell bottom rows by a wide margin, some pockets are empty for weeks because no merchandiser filled them, some carry designs three years past their prime, and shrink varies sharply by store.

## Why Nobody Has Built This
The scan data belongs to the retailer and is shared with the incumbent under the supply agreement, so only the incumbent can model pockets, and incumbents have historically used the data to defend rather than to diagnose. Space planning tools optimise SKUs that sell many units a week; card pockets sell a few, so their statistics need pooling across stores. The market is two or three publishers, too small for analytics vendors to build for.

## What to Build
A pocket productivity model that decomposes each pocket's sales into fixture position, design age, store cluster, shrink and out-of-stock effects, estimates each design's underlying rate with partial pooling across stores, and simulates department sales per linear foot under a proposed refresh. Its output is the renewal case: which pockets are dead and why, what the refresh plan earns with confidence intervals, and what share of the gap is execution (empty pockets) rather than assortment.

## Target Customer
VP of Category Management at a large card publisher preparing a department renewal or a conversion pitch; secondarily, retailer category managers evaluating the bids.

## Impact If Built
Turns the most consequential negotiation in the business, a department worth millions a year over a multi-year term (estimate), from a deck of averages into a quantified plan, and tells the publisher where execution rather than design is losing it money.
