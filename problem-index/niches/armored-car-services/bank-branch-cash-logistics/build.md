# A Cash Network Plan for the Whole Footprint

**Niche:** [[niches/armored-car-services/bank-branch-cash-logistics/profile|Bank & Credit Union Branch Cash Logistics]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A bank decides how often each branch gets cash, from which vault and in what amounts one branch at a time, and nobody models the total cost of cash across the footprint.
**Tags:** #optimization-fundamentals #time-series-forecasting #gradient-boosting #monte-carlo-methods #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to fill a bank's branch and vault cash orders on the next scheduled stop across its whole footprint, and whoever has a vault close enough to every branch to make same-day emergency deliveries takes the account.

## The Problem
A regional bank's cash costs come from several bills that nobody adds up. Carrier fees per scheduled stop and per emergency run; vault inventory fees; the funding cost of cash in branches, ATMs and the carrier's vault; Federal Reserve recirculation fees when fit notes are deposited and reordered in the same week; and the cost of branches running short. Delivery frequencies were set years ago, branch by branch, and rarely revisited as branches closed or moved to recyclers.

## Why Nobody Has Built This
Carriers optimise their routes, not the bank's network, and earn more from more stops. Forecasting vendors forecast each location's demand but do not choose vault assignments, frequencies or inventory policy. Bank cash teams are small and sit in operations, not in the treasury or analytics functions that build models.

## What to Build
A planning model for the bank's whole cash network: demand forecasts by branch, ATM and denomination; candidate carrier vaults and their cut-offs; delivery frequency options and contract prices; recirculation fee exposure; and the service level the bank wants. Stochastic simulation tests each plan against payday, holiday and disruption scenarios. The output is a recommended frequency and inventory policy per location and a footprint view of which branches no vault can serve same-day — the bank's actual negotiating position with its carrier.

## Target Customer
Heads of cash operations and treasury services at banks with ~50–500 branches (estimate) and at large credit unions, renegotiating carrier contracts.

## Impact If Built
Cutting even one weekly delivery at a few hundred branches, and the idle cash that rides with it, saves a bank ~hundreds of thousands to low millions of dollars a year (estimate), and turns the carrier renegotiation from a price argument into a design conversation.
