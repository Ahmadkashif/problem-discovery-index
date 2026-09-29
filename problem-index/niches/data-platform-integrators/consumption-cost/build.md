# Cost at Development Time

**Niche:** [[niches/data-platform-integrators/consumption-cost/profile|Consumption Cost Engineering]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every design decision in the transformation layer has a daily price and the engineer cannot see it.
**Tags:** #optimization-fundamentals #evaluation-metrics #data-integration #revenue-impact #descriptive-statistics #automation #change-point-detection #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make the cost consequences of a transformation layer visible during delivery rather than on a bill — and whoever surfaces that takes the account.

## The Problem
An analytics engineer chooses how to materialise a model, whether to make it incremental, how to partition it and how often to run it. Each choice has a recurring cost that compounds across the estate and appears only in a monthly bill attributed to a warehouse rather than to a decision. The engineer has no feedback, the reviewer has no basis to comment, and the cost is discovered by finance months later and addressed as an optimisation project.

## Why Nobody Has Built This
Cost data arrives late and aggregated, and nobody has joined it to the model layer. Development tooling shows correctness and not cost. The consumption model is recent enough that practice has not caught up. And the bill lands on the client after the integrator has left.

## What to Build
Put a price next to every model and every change. Attribute cost per model and per query continuously, which is the core and is the feedback loop the discipline is missing. Show the projected recurring cost of a model at development time, before it is merged, so the decision is informed rather than retrospective. Detect cost regressions on change and report them in review, which is where the decision can still be cheaply reversed. Recommend materialisation, incrementality and partitioning improvements from the actual query patterns rather than from general advice. Include the cost of everything a model depends on, since the true cost of an asset is its whole upstream chain and is never computed. Relate cost to use so the expensive-and-unused assets surface, which is where the largest savings are. Model the effect of schedule frequency, as many models run far more often than their consumers need. Set cost budgets per domain that a design is assessed against. Report cost per business outcome rather than per warehouse, which is what makes the conversation with finance productive. And make the cost visible to the engineer in their own tooling, because that is the only place the decision is actually made.

## Target Customer
Data platform teams and integrators, platform and finance leadership, cost management vendors, and platform providers.

## Impact If Built
Every materialisation and schedule decision has a recurring price and the engineer making it cannot see one. Cost attributed per model at development time turns an optimisation project into a design input.
