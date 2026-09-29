# Finding the Right Model in Minutes

**Niche:** [[niches/data-platform-integrators/the-analytics-engineer/profile|The Analytics Engineer]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A request to add a column costs a day of archaeology in an estate the team built themselves.
**Tags:** #worker-facing #graph-theory #large-language-models #data-integration #evaluation-metrics #workflow-orchestration #automation #word-embeddings
**Contested on:** Every serious competitor in this niche is fighting to let an engineer answer "can you add a column" without spending the day working out which of four similarly-named models is the right one — and whoever removes that takes the account.

## The Problem
An analytics engineer receives a small request and cannot find where to make the change. Four models have similar names; two are derived from the third; the fourth is a legacy version somebody left. The lineage graph shows structure and not meaning. Reading the transformations takes hours, the correct answer is a judgement, and the fastest safe option is often to add a new model — which makes the next person's version of this problem worse.

## Why Nobody Has Built This
Lineage tooling shows dependencies and stops there. Naming conventions decay. Nobody records which model is authoritative for a concept. And adding a model is always faster than understanding the estate, so the estate grows and the problem compounds.

## What to Build
Answer the business question rather than displaying the graph. Let an engineer find the right model from a business question in plain language rather than from a name, which is the core and is where the day actually goes. Mark which model is authoritative for each business concept, since ambiguity about that is the root of both the search cost and the duplication. Show impact before a change — what depends on this, who queries it, which reports move — which is the question asked constantly and answered by hand. Surface usage alongside lineage, as the heavily-queried model is usually the one that matters and the graph does not say so. Recover intent from commit history, ticket references and comments where it exists, because the why is what the engineer is actually reconstructing. Warn when a proposed new model closely resembles an existing one, which is the only realistic brake on proliferation. Show the model's cost and refresh schedule in the same place, so the change is made with full context. Make all of it available in the engineer's own tooling rather than a separate catalogue. Keep the context updated as changes are made, so the next engineer inherits more. And measure how long requests take to locate, which is the number that justifies the whole thing.

## Target Customer
Data platform teams and integrators, analytics engineering leads, catalogue and lineage vendors, and developer tooling providers.

## Impact If Built
The fastest safe option is usually to add another model, which makes the next person's problem worse. Finding the authoritative model from a business question, with impact shown before the change, breaks that cycle.
