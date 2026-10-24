# Inventory Truth Learned From Pickers' Scans

**Niche:** [[niches/grocery-stores/store-pick-online-fulfilment/profile|Store-Pick Online Order Fulfilment]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Pickers scan every item they find and flag every one they cannot, and that stream is the best live inventory signal in the store, yet it rarely updates locations or on-hand counts.
**Tags:** #bayesian-inference #hidden-markov-models #gradient-boosting #feature-engineering #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to pick online orders from the store's own shelves, and whoever delivers the lowest labour cost per order at an unchanged fill rate takes the account.

## The Problem
The pick app sends a picker to aisle 7 for an item the system shows twelve of. It was moved in last week's reset and the shelf is empty. The picker searches, marks it not found, and the customer gets a substitution. Tomorrow the system sends the next picker to the same place.

## Why Nobody Has Built This
Pick apps belong to the e-commerce team or a platform; inventory and planograms belong to store operations and merchandising. Pickers' "not found" events are treated as fulfilment metrics, not inventory evidence.

## What to Build
A probabilistic model of each item's location and on-shelf availability, updated from every picker scan, not-found event, store sale, delivery and reset. Before a batch, it predicts which items will be missing and routes the picker to backstock or proposes substitutes upfront. It sends location fixes to the reset team and suspected count errors to inventory control as a daily list.

## Target Customer
E-commerce operations leaders at chains picking in-store with their own staff, and platforms that pick for them.

## Impact If Built
At ~200 orders a day per store and ~2 minutes of search saved per order (estimate), a store saves ~6.5 picker-hours a day, ~2,400 hours a year.
