# The Floating Collection That Piles Up in One Branch

**Niche:** [[niches/libraries-and-archives/public-ils-and-consortium-circulation/profile|Public Library ILS & Consortium Circulation]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Fix (Pain Point)
**One-liner:** In a floating collection items stay wherever they are returned, so popular branches overflow while others empty out.
**Tags:** #time-series-forecasting #optimization-fundamentals #evaluation-metrics #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to fill a patron's hold from any shelf in a shared consortium catalogue in the fewest days, without losing a hold or a patron record when the system changes, and whoever makes daily holds delivery and the migration least risky takes the consortium's shared contract.

## The Problem
Floating collections save delivery cost by not returning items to an owning branch. Over months, items accumulate at branches near commuter routes or with generous return bins; shelves overflow there and thin out elsewhere.

## Why It's Still Broken
The ILS records item location but has no rule for rebalancing, so staff notice only when shelves are full and move items by hand.

## What a Fix Looks Like
A weekly balance report per branch and collection segment, comparing items on shelf with local demand, plus suggested transfer lists sized to van capacity, generated from the ILS.

## Who Feels the Pain
Branch staff shelving overflow; patrons at thin branches who find empty shelves.

## Impact If Fixed
Shelves matched to demand without abandoning the delivery savings that floating was adopted for.
