# Three Hundred Models Delivered and Nobody Counts Which Are Queried

**Industry:** [[data-platform-integrators|Data Platform Integrators]]
**Type:** High Impact
**One-liner:** The query log records every access to every asset the firm has ever built, and no integrator has ever joined it to their own delivery record to find out what proportion of their work is used.
**Tags:** #gradient-boosting #graph-neural-networks #k-means-clustering #causal-inference #confidence-intervals #evaluation-metrics #data-integration #revenue-impact

## The Problem
A data platform engagement produces assets: ingestion pipelines, staging and intermediate models, marts, metric definitions, dashboards and reverse ETL syncs. A substantial project delivers hundreds of them. Delivery is measured by whether they were built, tested and documented, and the engagement ends.

Whether anyone uses them is recorded in the client's query history and dashboard access logs, in complete detail. Practitioners' shared experience — expressed openly in the analytics engineering community — is that usage is extremely concentrated: a small fraction of models and dashboards serve nearly all the queries, and the remainder is inventory that costs money to refresh and complexity to maintain. Nobody has quantified it systematically, so the estimate remains folklore and the build rate never changes.

The consequences are concrete. Clients pay to build assets nobody opens and then pay again, in compute, to refresh them daily forever. The model layer's complexity — which is what makes change risky and slow — is driven largely by assets that provide no value. And when a client eventually asks what they can delete, nobody can answer confidently, because deletion requires knowing that nothing downstream depends on it and that knowledge is scattered across lineage, query logs and someone's memory.

For the firm, the loss is the evidence. An integrator that could say which kinds of asset actually get used, in which kinds of organisation, would deliver a materially better platform in half the models. Instead, every engagement builds the full set because the full set is what was scoped and because nobody has ever measured the alternative.

## Why It's Unsolved
The usage data belongs to the client and accumulates after the engagement. There is no standard mechanism by which an integrator sees a platform's consumption six months after go-live, and no clause in a typical statement of work that would grant it.

The commercial incentive is unfavourable in an obvious way. A firm billing by delivery volume has no reason to demonstrate that half its output is unused. The finding would be genuinely valuable to clients and genuinely awkward to publish, which is the same dynamic that appears everywhere in this cluster and is sharper here because the evidence is so unambiguous — a table with zero queries in a year is not a matter of interpretation.

The analysis also requires joining three things that live in different places: delivery records at the firm, query and access logs at the client, and lineage from a catalogue that may or may not be deployed. Each is available; nobody owns the join.

And there is a genuine subtlety about what usage means. A model queried once a quarter for a regulatory report is essential; one queried daily by an automated refresh that feeds an unopened dashboard is not. Access counts alone mislead in both directions, and a naive pruning exercise driven by query volume will delete something important — which is the objection that has stopped several attempts and is the reason the analysis has to be done with lineage and purpose attached rather than as a leaderboard.

## What a Solution Looks Like
Instrument consumption as a deliverable. A post-go-live reporting window covering query and access logs, agreed at contracting, gives both parties the answer. Clients want it — every mature platform owner knows their estate is mostly inventory and cannot prove which part — and it costs the integrator nothing but candour.

Classify by purpose, not by count. Combining access frequency with lineage depth, downstream consumer type — a human dashboard, a machine sync, a regulatory extract — and the seasonality of use separates the rare-but-essential from the automatically-refreshed-and-unread. That distinction is what makes a pruning recommendation safe enough to act on.

Attach cost. In consumption-priced platforms every model has a running cost that is directly attributable, and an asset's value-per-dollar ranking is computable. That converts an abstract complexity argument into a monthly number, which is what actually gets a deletion approved.

Feed it back into scoping. Across enough engagements, an integrator can learn which asset types earn their keep in which organisational contexts, and scope the next project to build what gets used. That is the version of this that changes the firm's product rather than just its reporting.

## Impact If Solved
Every mature data platform is carrying an estate whose majority is unused and whose owners cannot identify which part, paying for it in compute, complexity and change risk. Purpose-aware usage analysis with cost attached makes pruning safe and fundable. For the integrator it is the only credible route from selling model counts to selling a platform that works — and the first firm to publish its own usage data would have a positioning argument nobody in the category can answer.
