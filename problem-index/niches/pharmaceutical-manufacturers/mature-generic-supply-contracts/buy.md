# Supply Planning Built for Branded Forecasts

**Niche:** [[niches/pharmaceutical-manufacturers/mature-generic-supply-contracts/profile|Mature Generic Supply & Shortage Exposure]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Planning suites forecast demand for brands with stable channels; generic demand is a sequence of contract awards won and lost overnight.
**Tags:** #time-series-forecasting #gradient-boosting #monte-carlo-methods #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to keep shipping a wholesaler's or GPO's awarded generic at an eroded price, and whoever ships the highest share of awarded volume in full takes the account.

## The Problem
A generic's volume jumps when a rival exits or a wholesaler awards the contract, and collapses when the award goes elsewhere. Planners run brand-style forecasts and then override them by hand after each award email.

## What Already Exists
SAP IBP, Kinaxis RapidResponse and o9 demand and supply planning, with statistical forecasting and scenario tools.

## The Customization Gap
Generic planning needs award-based demand: contract terms, award and loss probabilities by buyer, competitor supply status from shortage and inspection data, and the penalty exposure of each contract. It also needs batch-size and campaign constraints for shared trains, and API lead times by supplier. Scenario planning should ask "what if the second supplier exits" rather than "what if demand rises 10%".

## Target Customer
Supply planning leads at generic makers and generic CDMOs.

## Impact If Solved
Award-aware planning would lift fill rates on awarded contracts by two to five percentage points (estimate), cutting penalties and the lost awards that follow a short shipment.
