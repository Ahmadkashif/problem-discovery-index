# Prioritising by Intuition

**Niche:** [[niches/b2b-commerce-platforms/the-catalogue-manager/profile|The Catalogue Manager]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A catalogue manager keys attributes from manufacturer PDFs all day with no way to know which of the hundred thousand gaps are actually costing sales.
**Tags:** #worker-facing #revenue-impact #evaluation-metrics #descriptive-statistics #gradient-boosting #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to tell the catalogue manager which gaps are costing sales — and whoever ranks the work by revenue at risk turns an endless backlog into a finite prioritised queue.

## The Problem
The catalogue has four hundred thousand products. Perhaps a third have complete technical attributes. The manager works through a category because a merchandiser asked, or because a supplier sent a new file, or because it seemed important. Meanwhile customers are searching for a thread size that is not populated on eleven thousand products, filtering to zero results, and calling a rep or buying elsewhere. That search is recorded. The connection between the missing attribute and the lost order has never been made, so the person whose entire job is closing those gaps works essentially at random.

## Why Nobody Has Built This
Product information management systems are built to store and govern attributes, not to value them — completeness is reported as a percentage, which treats every attribute on every product as equally worth having, and that is the flaw the whole problem rests on. Search analytics live in the storefront and never reach the catalogue team. Nobody owns the join. And catalogue work is a cost centre nobody has asked to justify, so the absence of a prioritisation is not felt as a failure.

## What to Build
Rank the catalogue backlog by revenue at risk. Join search and browse behaviour to catalogue gaps — every zero-result search, every filter that eliminates products that should have qualified, every session that ended at a specification the customer could not confirm — which is the core of it and converts an unbounded backlog into a ranked queue. Weight gaps by the product's actual and potential revenue, since an incomplete attribute on a part nobody buys costs nothing. Detect gaps the customer cannot report, such as products excluded from a filter because the attribute is empty rather than because they do not qualify, which is silent and is the largest hidden loss. Measure completeness against what customers search on rather than against the full attribute schema, which is the honest denominator and typically makes the true figure both worse and far more actionable. Estimate the value of each enrichment before it is done and measure it after, which is how the function finally justifies its headcount. Queue the work as a ranked list with the evidence attached rather than as a category assignment. Feed extraction candidates from the attribute extraction work so the manager is reviewing rather than keying. And track which manufacturers supply usable data, which is a supplier-management fact the merchandising team can act on.

## Target Customer
Catalogue and product information managers, ecommerce leadership at distributors, and product information vendors whose completeness reporting is not decision-useful.

## Impact If Built
The person whose job is closing catalogue gaps works at random while the platform records exactly which gaps lose orders. Ranking by revenue at risk converts an unbounded backlog into a finite queue and finally lets the function justify its headcount.
