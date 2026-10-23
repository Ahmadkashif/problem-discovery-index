# Denomination-Level Loads Planned Against Route Days

**Niche:** [[niches/armored-car-services/atm-cash-forecasting-replenishment/profile|ATM Cash Forecasting & Replenishment]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Forecasts say how much cash a machine will dispense; nobody plans what to load on the route days that actually exist, cassette by cassette, under a truck's value limit.
**Tags:** #time-series-forecasting #temporal-fusion-transformers #markov-decision-processes #dynamic-programming #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to keep each ATM between a cash-out and idle cash with the fewest unscheduled visits, and whoever holds the least cash in machines at the contracted cash-out rate takes the account.

## The Problem
A machine with Tuesday and Friday service must carry enough of each denomination to last to the next visit, but a truck covering ~forty machines on Friday (illustrative) has a value limit, and a holiday Monday changes everything. Planners resolve these collisions by padding loads.

## Why Nobody Has Built This
Forecasting vendors sell to owners and do not see carriers' routes or limits; carriers' desks see routes but are paid per visit and are not rewarded for lower idle cash. Denomination-level data is often not exported from monitoring systems.

## What to Build
Quantile forecasts per machine, denomination and day, feeding a stochastic replenishment policy solved jointly across each route day: what to load in each cassette, which machines to bring forward or push back, and when an unscheduled visit is cheaper than the expected cash-out. Owners set their own costs for cash-outs, visits and funds; the plan reports the trade-off it made.

## Target Customer
Banks and deployers running a few thousand machines, and carriers' AMS teams competing on cash efficiency.

## Impact If Built
Lower idle cash and fewer emergency runs at the same time, and a defensible cash-in-machine figure for the owner's contract reviews.
