# Cache and Retention Policy Is a Solved Optimisation

**Niche:** [[niches/observability-vendors/telemetry-cost-and-value/profile|Telemetry Cost & Value]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Deciding what to keep in expensive storage given access patterns and a budget is cache replacement, studied since the sixties, and telemetry retention is set as a single number in a settings page.
**Tags:** #dynamic-programming #optimization-fundamentals #gradient-boosting #time-series-forecasting #evaluation-metrics #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to tell an engineering organisation which telemetry is worth its cost — and whoever does that takes the budget conversation, because customers are currently cutting by volume, which is the only attribute they can see.

## The Problem
Choosing what to hold in fast storage under a budget, given observed and predicted access, is cache replacement — one of the oldest studied problems in computing, with optimal offline solutions, good online policies and a large literature including learned approaches. Telemetry retention is a number of days applied to everything, or at best per index, chosen by whoever configured the platform.

## What Already Exists
Cache replacement policies from the classical to the learned; tiered storage management in databases and file systems; access prediction from historical patterns; knapsack and budgeted selection formulations; and value-density ranking, which is the elementary version of the whole idea. Every platform has the access log the policies need.

## The Customization Gap
The adaptation is to data whose value is investigative rather than transactional. It requires: (1) a value model that includes future investigative use, not just past access frequency, since a stream nobody has queried may be the one that explains the next incident — which means weighting by the stream's role in the dependency graph and its history in past investigations, not only by hit rate; (2) asymmetric loss, because the cost of dropping something needed during an incident is far higher than the storage saved and a symmetric optimisation will cut too aggressively; (3) correlated value, since telemetry is useful in combination — a trace without its logs is worth much less than either suggests — and evaluating streams independently produces incoherent policies; (4) summarisation as a third option alongside keep and drop, which no cache formulation has and which dominates both for many streams; and (5) explainability, since a platform team must justify each cut to the service owner and an unexplained policy will be overridden everywhere.

## Target Customer
Observability and cost management vendors, the collector ecosystem, and large platform teams managing telemetry budgets directly.

## Impact If Solved
A sixty-year-old optimisation literature addresses precisely this decision and the category implements a global number. Asymmetric loss and summarisation-as-a-third-option are the two adaptations that make the policy safe enough to adopt.
