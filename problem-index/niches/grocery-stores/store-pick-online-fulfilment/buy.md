# Warehouse Pick Optimisation Adapted to Shared Store Aisles

**Niche:** [[niches/grocery-stores/store-pick-online-fulfilment/profile|Store-Pick Online Order Fulfilment]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Warehouse systems already batch orders and sequence pick paths; a store needs the same optimisation in aisles shared with shoppers, with fresh and frozen on a clock.
**Tags:** #optimization-fundamentals #dynamic-programming #graph-theory #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to pick online orders from the store's own shelves, and whoever delivers the lowest labour cost per order at an unchanged fill rate takes the account.

## The Problem
Store pick apps batch orders by pick window and sort items by aisle number. That ignores aisle congestion at peak shopping hours, the walk to the back room for backstock, and the rule that frozen goes in last.

## What Already Exists
Warehouse management and pick optimisation (Manhattan, Blue Yonder, Körber, and order-batching modules) that cluster orders, sequence pick paths on a facility graph and balance zones.

## The Customization Gap
A store's graph changes by hour as shoppers fill aisles. Locations are uncertain, so paths must allow for search. Temperature zones need staged picking and holding. Totes per cart are limited and orders are split by temperature. Store staff are shared with stocking and front end, so pick labour must be scheduled with the store, not as a dedicated warehouse crew.

## Target Customer
Chains with in-house pick apps, and store-pick software vendors.

## Impact If Solved
Cutting walking distance per batch by ~15% (estimate) on ~1,500 picker-hours a month per busy store saves ~225 hours a month.
