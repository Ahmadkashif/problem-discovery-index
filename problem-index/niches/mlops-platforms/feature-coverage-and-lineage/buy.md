# Data Catalogues and Column-Level Lineage

**Niche:** [[niches/mlops-platforms/feature-coverage-and-lineage/profile|Feature Coverage & Lineage]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The data governance world built column-level lineage, impact analysis and ownership registries, and the graph stops at the warehouse boundary where the models begin.
**Tags:** #graph-theory #data-integration #compliance #automation #workflow-orchestration #evaluation-metrics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to extend the consistency guarantee to the features that were never registered — and whoever does that takes the account, because the unregistered features are the majority and are where the failures are.

## The Problem
Data catalogues parse transformation code, build a column-level lineage graph, support impact analysis in both directions, hold ownership and classification, and notify downstream consumers of upstream changes. It is exactly the machinery a model needs. The graph ends at the last warehouse table, and the feature pipeline, the training job and the deployed model sit past the edge, invisible to it.

## What Already Exists
Data catalogue platforms with automated column-level lineage from query and transformation parsing; open lineage standards with a defined event model; impact analysis and downstream notification; data ownership and stewardship registries; classification and sensitivity tagging; and orchestrator integrations that emit lineage events natively.

## The Customization Gap
The adaptation is to extend the graph across the model boundary. It requires: (1) the model as a lineage node with typed inputs, so that a column change propagates to a named model in production rather than terminating at a table — this is a modest schema extension and the single highest-value piece; (2) the serving path as a lineage source, since the inline computations happen in application code that catalogue parsers do not read, which needs runtime instrumentation rather than static analysis and is where the unregistered features live; (3) training and serving as distinct edges from the same source, because the whole point is that the two paths can disagree and a single edge hides the divergence; (4) notification routed to a model owner in ML terms — this change affects three of your model's inputs, here is their importance — rather than as a generic schema alert that gets filtered; and (5) versioned lineage, since the question is frequently what the graph looked like when a given model version was trained, not what it looks like now.

## Target Customer
Data platform and governance teams, ML platform teams, catalogue and lineage vendors, and the feature store vendors whose boundary this crosses.

## Impact If Solved
The lineage machinery is mature and stops one node short of the models. Adding the model as a typed lineage node is a modest extension that turns an upstream schema change from a surprise into a notification.
