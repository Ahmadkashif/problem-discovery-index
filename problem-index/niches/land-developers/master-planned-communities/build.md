# Lot Price and Release Pacing Model

**Niche:** [[niches/land-developers/master-planned-communities/profile|Master-Planned Communities]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An MPC sets lot prices and release timing for each builder and product from a spreadsheet, when it holds the sales history that could show how price and supply move its pace.
**Tags:** #gradient-boosting #causal-inference #time-series-forecasting #bayesian-inference #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep its builders selling homes faster than the competing new-home communities around it, and whoever posts the most new-home sales a year in its submarket takes the account.

## The Problem
Each year an MPC decides how many lots to develop and release, in which widths and price bands, to which builders, at what base price and escalator. Release too many and builders compete each other's prices down; release too few and buyers go to the next community. Price too high and builders slow their takedowns; too low and the developer leaves money in a multi-decade asset. The decision is made by experienced executives reading builder reports and competitor data.

## Why Nobody Has Built This
The decision is rare (annual or per phase), the data is spread across builders' reports, the MPC's contracts and licensed competitor data, and each MPC is a small, idiosyncratic market. Data vendors sell the market view; nobody models the MPC's own lever.

## What to Build
A model of the community's sales pace by product and price band against competing communities, mortgage rates and the MPC's own supply. It estimates the effect of release size and lot price on builder sales and takedowns, using the MPC's phase history as natural experiments. It recommends release plans and lot prices with their expected pace and revenue, and grades each recommendation against what followed.

## Target Customer
Presidents and VPs of builder sales at MPC developers selling to five or more builders.

## Impact If Built
Better-timed releases and prices keep builders selling at the top of the submarket, which is what keeps the next lot contract and the community's ranking. On an MPC selling ~500 lots a year, a 2% better lot price is ~$1.1M a year, using Forestar's $108,400 average lot as a proxy (estimate).
