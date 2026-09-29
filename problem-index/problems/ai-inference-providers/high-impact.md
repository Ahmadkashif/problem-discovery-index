# Capacity Economics Against Bursty Demand

**Industry:** [[ai-inference-providers|AI Inference Providers]]
**Type:** High Impact
**One-liner:** The business is renting depreciating accelerators against demand that arrives in unannounced spikes, and the entire margin sits in the gap between what is provisioned and what is used.
**Tags:** #time-series-forecasting #gradient-boosting #convex-optimization #optimization-fundamentals #confidence-intervals #evaluation-metrics #markov-decision-processes #revenue-impact

## The Problem
An inference provider commits to capacity in advance. Accelerators are procured on multi-year contracts, reserved cloud instances, or spot markets, and the cost of that commitment is fixed from the moment it is made. Hardware depreciates quickly in a market where each generation is substantially faster.

Demand does not cooperate. A customer launches a feature and their traffic multiplies overnight. Someone runs a large batch job at two in the morning with no warning. A model becomes briefly popular and every developer tries it in the same week. Traffic across the customer base is spiky, correlated in ways that are not obvious, and largely unannounced.

The provider must choose. Provision for peak and carry expensive idle hardware most of the time, which destroys the margin. Provision for the average and fail the latency guarantee during spikes, which is the one property customers are buying and the one failure they will leave over.

The usual mitigations each have limits. Autoscaling helps and is bounded by cold start — loading a large model into accelerator memory takes long enough that scaling reacts after the spike has already caused failures. Spot capacity is cheap and can be reclaimed exactly when demand is highest, because everyone's demand is correlated. Overselling reserved capacity works until two customers spike together.

Meanwhile customers have almost no incentive to communicate, because the current pricing structure charges them nothing for unpredictability.

## Why It's Unsolved
Forecasting is genuinely hard here. Demand is driven by the customers' own product events, which the provider does not see. There is little history for a new customer or a newly released model, and the spikes that matter are by definition rare, so the forecast is being asked to predict exactly the events it has fewest examples of.

Cold start is a physical constraint. Model weights must be resident in accelerator memory, loading tens of gigabytes takes real time, and no amount of scheduling sophistication removes it — it can only be anticipated.

The pricing structure works against everyone. Per-token pricing gives the customer no reason to signal an upcoming launch and no reward for predictable traffic, while the provider carries all the variance risk. A pricing model that shared it would change behaviour, and nobody has been willing to move first in a market competing hard on headline price.

And correlation is the quiet killer. Capacity planning that treats customers as independent is wrong, because product launches cluster, business hours overlap, and viral moments hit everyone at once.

## What a Solution Looks Like
Probabilistic demand forecasting per model and per customer, with correlation modelled explicitly across the base — the aggregate distribution matters far more than any individual forecast, and correlation is what makes the aggregate tail fat.

Capacity as a portfolio decision under uncertainty. The mix of committed, reserved and spot capacity is an optimisation against a demand distribution with a cost for failing the guarantee, and it is currently made with spreadsheets and instinct.

Predictive warm-up rather than reactive scaling. If a spike can be anticipated even ten minutes ahead, model weights can be staged and the cold start disappears — and many spikes are anticipable from leading indicators the provider can see, including a customer's own gradual ramp before a launch.

Pricing that shares the risk. Committed capacity at a discount, burst capacity at a premium, and a genuine reward for predictable traffic, which is standard in every other capacity-constrained utility business and absent here.

Placement that accounts for correlation. Co-locating customers whose demand peaks at different times raises effective utilisation without any new hardware.

## Impact If Solved
Utilisation is the entire margin in this business, and it is currently managed by overprovisioning against uncertainty nobody has quantified. Forecasting demand properly and treating capacity as a portfolio problem is worth a large fraction of the fleet in a category where competitors are pricing at or below cost.
