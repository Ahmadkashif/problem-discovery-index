# Logistics Estimation Practice

**Niche:** [[niches/dropshipping-suppliers/delivery-time-prediction/profile|Delivery Time Prediction]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Large retailers and carriers run serious estimated-delivery-date modelling because it moves conversion measurably, and dropshipping uses a number from a forum.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to publish a delivery distribution for a specific supplier, service and destination that holds up — and whoever does that lets merchants make a promise instead of a guess.

## The Problem
Estimated delivery date modelling is a well-developed capability at large retailers and carriers, built because a displayed date measurably changes conversion and a missed one measurably costs. The models account for origin, service, route, day of week, seasonality and network conditions, and they are evaluated on calibration rather than on average error. The methods are published and the technique is not exotic. Dropshipping, whose delivery variance is the largest in retail, has adopted none of it.

## What Already Exists
Estimated delivery date models with calibration measurement; carrier network transit modelling; seasonal and peak adjustment; promise-date optimisation against conversion; and in-flight estimate revision.

## The Customization Gap
The adaptation is from an owned network to a chain of parties nobody controls. It requires: (1) supplier handling time as a modelled random variable rather than a known constant, since it is the largest and most variable component and the retailer's version treats it as a fixed warehouse process — this is the central difference; (2) cross-border customs as a first-class stage with its own heavy-tailed distribution, which domestic models have no equivalent for and which produces most of the extreme outcomes; (3) sparse data per supplier-service-destination cell, requiring pooling and hierarchical structure rather than the dense per-lane data a carrier enjoys; (4) the estimate serving a merchant's promise decision rather than a retailer's own display, which means exposing the distribution and the trade-off rather than a single date; and (5) no operational control at all, so the model cannot assume any intervention is possible and must be purely predictive.

## Target Customer
Dropshipping and sourcing platforms, merchants and aggregators, and delivery estimation vendors for whom uncontrolled cross-border chains are unserved.

## Impact If Solved
Retail models treat handling as a fixed warehouse process, and here it is the largest random component. Customs is a heavy-tailed stage with no domestic equivalent, and sparse per-lane data demands hierarchical pooling a carrier never needs.
