# The Derived Table Nobody Tagged

**Niche:** [[niches/data-marketplace-brokers/licence-term-enforcement/profile|Licence Term Enforcement]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Licensed data is joined, aggregated and copied into dozens of downstream tables that carry no marking, so the restrictions apply to a source nobody uses and not to the derivatives everybody does.
**Tags:** #graph-theory #data-integration #compliance #automation #evaluation-metrics #descriptive-statistics #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to make permitted-use terms something the delivery path can read and enforce rather than prose somebody has to remember — and whoever does that takes the account, because compliance currently depends on institutional memory.

## The Problem
A licensed dataset lands in a raw zone, correctly labelled. A pipeline joins it with internal data into a curated table. Another aggregates that into a mart. A dashboard reads the mart, a training set is assembled from it, and an export goes to a partner. None of the four downstream assets carries any indication that licensed data is inside them. The governance team's inventory shows one restricted table, carefully controlled and barely queried. The actual exposure is four assets nobody has classified, used daily, by people who have never heard of the provider.

## Why It's Still Broken
Classification is applied at ingestion and does not propagate, because propagation requires lineage that many organisations have only partially. Tagging derived assets manually does not scale and is nobody's task. Pipelines are written by people who are not thinking about licences. And the inventory looks correct, which is worse than looking wrong.

## What a Fix Looks Like
Propagate the marking automatically. Derive classification from lineage, so any asset containing licensed data inherits its restrictions without anybody tagging it — this is mechanical wherever column-level lineage exists and is the fix; where lineage is partial, the gaps are exactly the places to invest. Compose restrictions from multiple sources, taking the most restrictive applicable term, since a derived table combining three licensed sources is bound by all three. Report the true footprint — how many assets contain licensed data and who uses them — which is usually an order of magnitude larger than the governance inventory and is the number that makes this fundable. Warn at pipeline authoring time when a job is about to propagate licensed data into a less-controlled zone, which is the cheapest intervention and catches it before it exists. Handle aggregation thresholds explicitly, since many licences permit publishing aggregates above a threshold and that distinction is currently lost entirely. Flag exports and model training paths specifically, because those are where the consequential breaches happen. Re-evaluate the whole graph when a licence changes or expires. And show the provenance to the user at query time, so somebody about to publish a chart knows what is underneath it.

## Who Feels the Pain
Governance teams whose inventory is accurate and irrelevant; analysts unknowingly breaching terms in tables they inherited; and the companies whose exposure is an order of magnitude larger than their register shows.

## Impact If Fixed
Classification applied at ingestion and not propagated leaves an inventory that is accurate and irrelevant. Deriving classification from lineage is mechanical wherever lineage exists, and reporting the true footprint is usually an order-of-magnitude correction.
