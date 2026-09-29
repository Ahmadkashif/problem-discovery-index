# Metric Definition Drift

**Industry:** [[bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** High Impact
**One-liner:** Detect when two dashboards compute the same-named metric differently, from the query logic itself, so the reconciliation happens before the meeting rather than during it.
**Tags:** #bert #word-embeddings #graph-neural-networks #dbscan #large-language-models #hypothesis-testing #feature-engineering #evaluation-metrics #data-integration

## The Problem
Every organisation past a certain size has several definitions of its most important metrics. Active users counted with a thirty-day window in one dashboard and a seven-day window in another. Revenue net of refunds here and gross there. Churn computed on accounts in one report and on seats in another. Each definition is defensible and was chosen by someone with a reason.

The problem is that nobody knows they diverge until two numbers appear in the same room. Then a meeting that was supposed to decide something spends itself reconciling, an analyst is dispatched to work out which is right, and the decision slips a week. This happens constantly and is accepted as a fact of organisational life.

The semantic layer exists to solve exactly this — define the metric once, centrally, and have everything compute from the definition. It works where it is adopted. Adoption is always partial, because the layer requires governance effort and because self-service analytics exists precisely so that people can build things without waiting for the data team. So a governed core is surrounded by a large ungoverned periphery, and the periphery is where the drift lives and where most dashboards are.

The platforms could detect this. Every dashboard's underlying query is stored. Two queries producing a field called active users with different filter logic are comparable programmatically. Nobody compares them.

## Why It's Unsolved
Governance was assumed to be the answer, so the problem was framed as an organisational discipline issue rather than a detection one. The category's response has been to build better modelling layers and to encourage adoption, which addresses new development and does nothing about the thousands of existing assets.

The comparison is also genuinely non-trivial. Two queries can compute the same thing with entirely different SQL and different-looking queries can be semantically identical. Determining equivalence properly is a hard problem, though determining likely divergence for a human to check is much easier and is what is actually needed.

Ownership is the other obstacle. If drift is detected, someone has to decide which definition is right, and that is a business decision requiring authority that no data team has. Detecting a hundred divergences and being unable to resolve any of them is a worse position than not knowing, which is a rational reason teams have not looked.

Natural language querying makes it urgent. When a person writes SQL they at least see the definition. When a model generates the query from a question, the definition is chosen invisibly, and the drift becomes both faster and harder to see.

## What a Solution Looks Like
Metric fingerprinting across the asset estate. Extract from every dashboard and query the fields it computes, the tables and filters it uses, and the aggregation applied, and cluster by name and by semantics. Where the same business term maps to materially different logic, surface it with both definitions side by side and the usage volume of each.

Usage weighting is what makes it actionable. Two hundred divergences is noise; the four that appear in executive reporting are the ones that matter, and the platform knows which assets executives open.

Lineage-aware comparison catches the subtler case where two dashboards agree at the metric level and disagree upstream because one reads a table that filters differently.

And the resolution path has to be part of the product: a proposed canonical definition, an owner, and a migration list of the assets that would change and by how much — because the number changing is what makes people resist, and showing the delta in advance is what makes the change possible.

## Impact If Solved
Definition drift is the reason organisations do not trust their own dashboards, and distrust is why analysts spend their days answering questions that a dashboard already answers. Detecting it from query logic converts an unresolvable governance aspiration into a finite list, and the urgency is rising because natural language querying chooses definitions invisibly.
