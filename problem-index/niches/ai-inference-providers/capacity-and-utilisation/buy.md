# Revenue Management and Capacity Markets

**Niche:** [[niches/ai-inference-providers/capacity-and-utilisation/profile|Capacity & Utilisation]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Airlines, hotels and electricity grids solved selling a perishable fixed capacity against volatile demand, and inference providers price per token at a flat rate.
**Tags:** #revenue-impact #time-series-forecasting #convex-optimization #markov-decision-processes #probability-distributions #confidence-intervals #dynamic-programming #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to hold its latency guarantees at the highest achievable utilisation of depreciating hardware — and whoever does that takes the market, because that single ratio is the entire margin.

## The Problem
Capacity that perishes if unused, demand that varies, and customers with different willingness to pay and different flexibility is the exact problem revenue management was invented for, and it has half a century of practice behind it. Electricity grids added demand response, interruptible tariffs and capacity markets for the same reason. Inference providers sell a flat rate per token to everyone, which leaves both the peak and the trough unmanaged.

## What Already Exists
Revenue management with demand forecasting, fare class allocation and overbooking models; dynamic pricing with willingness-to-pay segmentation; electricity demand response programmes with interruptible tariffs and capacity payments; commitment and option contracts from commodity markets; and the spot-versus-forward portfolio optimisation used across energy and shipping.

## The Customization Gap
The adaptation is to a resource sold in tokens and constrained by latency. It requires: (1) the capacity unit defined by concurrent latency-constrained throughput rather than by seats or megawatts, since an accelerator's usable capacity depends on the batch composition and the guarantee — which makes the capacity constraint itself workload-dependent and is the main modelling difference; (2) demand response adapted to compute: deferrable batch, interruptible sessions and notified spikes, which is the closest analogue and the least exploited, since the electricity world's experience is that paying customers to be flexible is far cheaper than building for the peak; (3) segmentation by flexibility rather than only by volume, so that a customer who can wait is priced differently from one who cannot; (4) overbooking models for guarantees, where the statistical machinery transfers but the consequence of a failure is a breached latency commitment rather than a denied boarding, and the cost function needs restating; and (5) very short horizons, since these markets clear over hours rather than months and the forecasting must run continuously.

## Target Customer
Inference providers, their pricing and finance functions, and the revenue management and energy market practitioners for whom this is an unclaimed application.

## Impact If Solved
Perishable capacity against volatile demand is a solved commercial discipline and this industry sells a flat rate. Demand response — paying customers to be flexible — is the electricity world's central lesson and the least exploited lever here.
