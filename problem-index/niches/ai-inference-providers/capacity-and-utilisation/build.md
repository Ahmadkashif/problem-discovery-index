# The Margin Is the Gap Between Provisioned and Used

**Niche:** [[niches/ai-inference-providers/capacity-and-utilisation/profile|Capacity & Utilisation]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The business is renting depreciating accelerators against demand that arrives in unannounced spikes, and the entire margin sits in the gap between what is provisioned and what is used.
**Tags:** #time-series-forecasting #markov-decision-processes #convex-optimization #confidence-intervals #gradient-boosting #revenue-impact #evaluation-metrics #dynamic-programming
**Contested on:** Every serious competitor in this niche is fighting to hold its latency guarantees at the highest achievable utilisation of depreciating hardware — and whoever does that takes the market, because that single ratio is the entire margin.

## The Problem
A provider holds a fleet sized for the peak it experienced two months ago plus a margin for safety. Average utilisation is well under half. The finance team sees a hardware amortisation line that dwarfs revenue growth; the engineering team sees a fleet that was fully saturated twice last quarter and cannot be cut. Both are right. The gap between them is the entire profit of the business, it is managed by a capacity planner's judgement in a spreadsheet, and the request-level history that would let it be forecast, priced and arbitrated is sitting in the billing system.

## Why Nobody Has Built This
Capacity was treated as a procurement function inherited from cloud operations, where demand is smoother and the assets depreciate more slowly, so the optimisation instinct never arrived. Hardware commitments are negotiated by a different team from the one serving requests, on a different time horizon. Spikes are experienced as incidents rather than as a distribution to be modelled. And the forecast that would justify a smaller fleet is the forecast that gets blamed when a guarantee fails, which makes headroom the politically safe choice at every review.

## What to Build
Forecast demand, then optimise the portfolio against it. Build per-customer demand forecasting, because aggregate demand is the sum of a small number of customers whose individual patterns are far more predictable than the total — and the launches, batch schedules and weekly cycles that drive spikes are per-customer facts the provider can see. Model the capacity portfolio explicitly across committed, reserved, on-demand and spot tiers, since the spread between them is where the margin lives and it is currently exploited by instinct rather than by an allocation model. Price the guarantee rather than the token: a customer requiring low tail latency at unpredictable volume consumes headroom that a flexible customer does not, and charging identically for both is a cross-subsidy nobody has quantified. Offer flexibility discounts explicitly — commitment, advance notice of spikes, interruptibility, deferrable batch — which reshapes demand rather than merely absorbing it and is the most underused lever in the business. Compute the fleet's necessary size against a stated service level and report the insurance component, since nobody currently knows what fraction of the fleet is insurance. Optimise hardware refresh against depreciation and performance per watt, which is a capital allocation problem being made by intuition. And measure realised utilisation against forecast continuously, so the forecast earns the trust required to shrink the headroom.

## Target Customer
Inference providers, their finance and capacity functions, their investors, and the accelerator lessors on the other side of the commitments.

## Impact If Built
The industry's entire margin is a ratio managed in a spreadsheet. Per-customer forecasting is tractable where aggregate forecasting is not, and pricing the guarantee rather than the token exposes a cross-subsidy every provider currently absorbs silently.
