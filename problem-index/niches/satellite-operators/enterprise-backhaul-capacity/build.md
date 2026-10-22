# A Multi-Orbit Network Designer for Every Bid

**Niche:** [[niches/satellite-operators/enterprise-backhaul-capacity/profile|Enterprise, Backhaul & Government Data Capacity]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each enterprise or backhaul bid needs an engineer to design which sites ride which orbit and beam, at what availability and cost, and the week that takes loses deals to a competitor with a price list.
**Tags:** #convex-optimization #monte-carlo-methods #gradient-boosting #feature-engineering #revenue-impact #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to sell guaranteed throughput across GEO, MEO and partner LEO capacity at a price per megabit that survives comparison with Starlink, and whoever can design, quote and prove a multi-orbit service level fastest takes the carrier or enterprise contract.

## The Problem
A mobile operator asks for backhaul to 400 rural cell sites; a mining company for 30 remote sites with failover. The solutions engineer must choose for each site a GEO beam, MEO coverage or partner LEO service, size the terminal and capacity, run link budgets with local rain statistics, and price it so the bid wins and the margin survives. The same analysis is redone by hand for every bid and every revision.

## Why Nobody Has Built This
Multi-orbit offers are new, partner LEO capacity terms are bespoke, and each operator's capacity, pricing rules and terminal catalogue are confidential. Ground equipment vendors design for their own hubs, not the operator's whole portfolio.

## What to Build
A designer that takes a site list and service requirements and returns an optimised network: orbit and beam per site, terminal, capacity, predicted availability from rain and congestion models, failover paths, and cost and price, with sensitivity to the customer's priorities. Win and loss data from past bids feeds a price-response model.

## Target Customer
Heads of solutions engineering and enterprise sales at multi-orbit operators.

## Impact If Built
Bids answered in a day instead of a week, consistent margins, and an SLA prediction the operator can stand behind.
