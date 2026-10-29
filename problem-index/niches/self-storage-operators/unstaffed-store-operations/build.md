# Which Stores Can Go Unstaffed

**Niche:** [[niches/self-storage-operators/unstaffed-store-operations/profile|Unstaffed Stores: Kiosks, Smart Access & Remote Rental]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators remove managers store by store on instinct, and learn months later whether the store earns more or less without one. The answer is estimable in advance from stores that already made the switch.
**Tags:** #causal-inference #gradient-boosting #time-series-forecasting #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to run a store with nobody on site without losing the rent a manager would have kept, and whoever delivers the highest net operating income per store run with nobody on site takes the account.

## The Problem
A manager costs a store ~$45,000–60,000 a year (estimate). Taking them out works at some stores and fails at others. Walk-in-heavy sites, stores with many elderly tenants, and sites with security problems lose move-ins, delinquency rises and audits stop. Operators decide from intuition and a pilot, and the result is muddied by season and market.

## Why Nobody Has Built This
Each operator has converted only a handful of stores, too few for a clean comparison, and vendors selling kiosks and locks have no incentive to say which stores should not convert. The data needed spans the facility system, the access system and the call centre.

## What to Build
A before-and-after model on every store that changed staffing. Synthetic-control comparisons match each converted store to staffed stores with similar markets, sizes and seasonality. The comparison is the proof method. They estimate the change in move-ins, occupancy, delinquency and protection attachment. A predictive model learns which store attributes moderated the effect: share of walk-in rentals, tenant age mix, unit mix, crime, competitor staffing. For a candidate store it forecasts net operating income run with nobody on site: rent kept, minus kiosk, lock, call-centre and maintenance costs, against the payroll saved.

## Target Customer
VPs of operations at operators and third-party managers planning staffing changes; vendors who want evidence their systems keep stores full.

## Impact If Built
If the model steers an operator away from converting the 20% of candidate stores where occupancy would fall ~3–5 points (estimate), each avoided mistake saves ~$20,000–35,000 a year of rent at a $700,000 store. At the stores it does convert, the ~$45,000–60,000 manager cost (estimate) becomes net operating income.
