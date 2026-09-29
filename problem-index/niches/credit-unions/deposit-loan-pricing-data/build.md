# Elasticity Estimates Validated Against What Actually Moved

**Niche:** [[niches/credit-unions/deposit-loan-pricing-data/profile|Deposit & Loan Pricing Benchmark Data]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The product tells an institution how much balance it will lose if it does not match a competitor's rate, and the balances then move — which nobody compares to what was predicted.
**Tags:** #causal-inference #gradient-boosting #time-series-forecasting #evaluation-metrics #cross-validation #confidence-intervals #feature-engineering #hypothesis-testing #data-integration #revenue-impact

## The Problem
Pricing benchmarks are useful; elasticity is where the money is. An institution setting a deposit rate wants to know what balances will do at each price point, and the vendor's models supply that. The models are estimated on historical contributed data and refreshed periodically. What is never done is the obvious test: the institution set a rate, balances moved, and both the decision and the outcome are in the contributed data stream. Comparing predicted to realized elasticity, by product, market, and institution type, is available and unperformed. So the models are validated on the sample they were fitted to, not on the decisions clients actually made using them — and rate cycles are exactly when clients scrutinize the advice hardest and when the models are least likely to hold.

## Why Nobody Has Built This
Contributed data arrives as periodic snapshots rather than as decisions with outcomes attached, so the causal structure — this institution changed this rate on this date and this happened — has to be reconstructed rather than read. The analysis is genuinely confounded: competitors move simultaneously, marketing campaigns coincide with rate changes, and a rate change that follows an outflow is a response rather than a cause. Doing it properly requires treating the rate change as an intervention with a comparison group, which is real methodological work. And there is the recurring disincentive — measured elasticity accuracy is a number that can be attacked in a competitive evaluation.

## What to Build
An elasticity validation layer built on the contributed stream. Rate changes are identified as events with their timing, magnitude, and competitive context; balance response is measured against a comparison group of institutions in similar markets that did not move, which is what separates the rate effect from the market-wide one. Predicted elasticity from the model in force at the time is scored against realized response, accumulating a calibration record by product, market structure, institution size, and rate environment. That produces three things the vendor cannot currently offer. Honest uncertainty around every elasticity estimate, which matters far more to a treasurer than a slightly better point estimate. Identification of the conditions where the models are systematically wrong — typically rate environments unlike the estimation period, which is precisely when clients need them. And a demonstrable accuracy claim, in a category where every competitor asserts model quality and none evidences it.

## Target Customer
Chief analytics officers and heads of research at pricing data providers running 100-500 staff, and the treasury and pricing executives at credit unions and banks who set rates against these models with no accuracy history available.

## Impact If Built
Converts the highest-value part of the product from an assertion into a measured capability. The validation record is also strictly proprietary — it can only be assembled by the party holding both the predictions and the contributed outcomes — and it compounds across every rate cycle it observes.
