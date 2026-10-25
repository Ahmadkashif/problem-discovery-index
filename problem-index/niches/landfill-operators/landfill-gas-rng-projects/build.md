# A Collection-Efficiency Ledger by Area

**Niche:** [[niches/landfill-operators/landfill-gas-rng-projects/profile|Landfill Gas Collection & RNG Projects]]
**Industry:** [[industries/landfill-operators|Landfill Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A landfill reports one collection-efficiency number for the whole site, so neither owner nor developer can say which areas are losing gas, how much it is worth, or which fix pays first.
**Tags:** #bayesian-inference #gaussian-processes #time-series-forecasting #data-integration #revenue-impact #compliance
**Contested on:** Every serious competitor in this niche is fighting to pull more of the methane a landfill generates into the collection system and the RNG plant, and whoever delivers the most methane per ton of waste in place takes the account.

## The Problem
Generation is estimated from waste placed and its age with a first-order decay model; collection is measured at the blower and plant. The gap between them is lost gas, but it is a site-level number built on default assumptions, and aerial surveys measured emission rates averaging 1.4 times what landfills reported.

## Why Nobody Has Built This
Generation by area needs waste-placement history by cell, which sits in survey and ticket records; collection by area needs well flows, which many sites do not meter; and emissions by area need surface and aerial data that arrive from different vendors.

## What to Build
A ledger per cell or area: modelled generation from waste placed and age, calibrated to measured flows; collected gas from well flows and composition; estimated surface emissions from monitoring and aerial detections; and the gap valued at current gas, RIN and credit prices. Ranked actions — new wells, liquid removal, cover repair, vacuum changes — with the expected recovery for each.

## Target Customer
RNG developers' operations heads and landfill owners' renewable energy and engineering teams.

## Impact If Built
At a site sending ~3,000 scfm to an RNG plant (estimate), finding and recovering 5% of lost gas is ~40,000 MMBtu a year, ~$1M with D3 RINs near $2.45 (estimate).
