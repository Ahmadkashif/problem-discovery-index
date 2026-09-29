# Cache Analysis Is a Solved Discipline

**Niche:** [[niches/edge-cdn-providers/cache-configuration/profile|Cache Configuration]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Cache replacement, admission and sizing have a sixty-year literature with optimal offline baselines, and content delivery caching is configured with a rule and a time-to-live somebody guessed.
**Tags:** #dynamic-programming #optimization-fundamentals #monte-carlo-methods #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to derive what is genuinely cacheable from the traffic rather than from a rule somebody wrote in 2019 — and whoever does that takes the account, because caching decisions determine both performance and origin cost and are the category's oldest unsolved problem.

## The Problem
Caching is among the most studied problems in computing: replacement policies, admission policies, optimal offline baselines against which any policy can be measured, and a large body of work on content delivery caching specifically. A CDN's own internal replacement policy reflects some of this. The customer-facing configuration — which objects are cacheable and for how long — is set by rules written in a configuration language and is not connected to any of it.

## What Already Exists
Cache replacement and admission policy research including learned approaches; the optimal offline policy as an evaluation baseline; hierarchical and cooperative caching research developed for content delivery networks specifically; reuse distance analysis; and simulation frameworks for evaluating policies against a trace. All published and much of it open.

## The Customization Gap
The adaptation is from the provider's internal policy to the customer's configuration. It requires: (1) treating the customer's configuration as the object to optimise rather than the eviction policy, since the provider has tuned its own caching well and the customer's rules are what determines what reaches it — which is the reframing that matters; (2) counterfactual evaluation against the traffic trace, so that a proposed configuration can be scored on what it would have achieved on last week's traffic, which is simulation over a trace and is the only way a customer will accept a change to caching; (3) correctness as a hard constraint, because serving a stale or wrongly-shared response is a serious incident and the optimisation must never produce one — which means conservative treatment of anything that might be personalised; (4) an objective spanning both hit rate and origin cost, since those diverge when large objects are involved and optimising the first alone can increase the second; and (5) per-resource-class treatment, because a site's assets, API responses and documents have entirely different characteristics and a single policy is wrong for all of them.

## Target Customer
CDN and edge providers, platform engineering teams, and the performance consultancies who currently do this analysis by hand for large customers.

## Impact If Solved
A deep literature exists and is applied to the provider's internal policy rather than to the customer's configuration, which is where the actual losses are. Counterfactual evaluation against the traffic trace is what makes a proposed change acceptable, and correctness-as-a-constraint is non-negotiable.
