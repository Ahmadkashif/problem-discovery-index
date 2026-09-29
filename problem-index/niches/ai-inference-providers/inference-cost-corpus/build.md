# The Cost Record Used to Generate Invoices

**Niche:** [[niches/ai-inference-providers/inference-cost-corpus/profile|Inference Cost Corpus]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Providers hold request-level records of what inference actually costs across millions of requests and every accelerator generation, and use them to generate invoices.
**Tags:** #gradient-boosting #time-series-forecasting #convex-optimization #evaluation-metrics #confidence-intervals #revenue-impact #descriptive-statistics #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to turn request-level history into an empirical account of what inference actually costs — and whoever does that prices, provisions and optimises against evidence while everyone else guesses.

## The Problem
A provider decides what to charge per million tokens for a new model. The inputs available to that decision are what competitors charge and a rough sense of throughput on a benchmark. The inputs that exist are millions of served requests with their exact batch composition, memory pressure, accelerator utilisation and latency, from which the marginal cost of a request at a given concurrency on a given hardware generation is directly computable. Nobody has computed it. The same corpus would answer which models are worth keeping loaded, which fleet segments are unnecessary, and where the next optimisation should go. It runs a billing pipeline.

## Why Nobody Has Built This
The data was collected for billing, which means it is shaped for invoices and not for analysis, and reshaping it is unglamorous work. Cost analysis sits between finance and engineering, where neither owns it. The findings would show that some products are priced below cost and some customers are unprofitable, which is unwelcome information with immediate commercial consequences. And the whole industry is growing fast enough that unit economics feels like a problem for later.

## What to Build
Extract the cost model. Build a marginal cost model per request as a function of model, batch state, hardware generation and concurrency, which is a well-posed regression on abundant data and is the foundation everything else in this industry needs — capacity, pricing, scheduling and optimisation are all currently reasoning without it. Report profitability per customer and per model, which is where the uncomfortable and actionable findings are, and which no provider currently produces. Characterise serving efficiency by architecture empirically, so the next model's economics can be estimated before it is served rather than discovered afterwards. Analyse which fleet capacity was genuinely necessary, by replaying demand against counterfactual fleet sizes, which is the only honest way to size the insurance component and is directly computable from the history. Feed the cost model into scheduling and placement, so decisions are made against cost rather than against utilisation. Use it to target optimisation work at the models where efficiency gains are worth most, which is currently chosen by salience. Publish aggregate findings about serving efficiency by architecture, since the field has no reference and the provider who supplies it gains standing. And run the analysis continuously, because hardware generations and model mixes change and a one-off study ages immediately.

## Target Customer
Inference providers, their finance and pricing functions, their investors, and the customers who would benefit from prices grounded in cost.

## Impact If Built
Every other problem in this industry is being reasoned about without a marginal cost model, and the data to build one is in the billing pipeline. Replaying demand against counterfactual fleet sizes is the only honest way to size the insurance component of the fleet.
