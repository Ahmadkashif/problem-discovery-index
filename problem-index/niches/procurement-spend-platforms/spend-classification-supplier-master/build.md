# Line-Item Classification and a Resolved Supplier Graph

**Niche:** [[niches/procurement-spend-platforms/spend-classification-supplier-master/profile|Spend Classification & Supplier Master]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Spend is classified by reading a supplier name and suppliers are deduplicated by matching one, and every negotiation, consolidation and savings figure in procurement is computed on top of those two approximations.
**Tags:** #bert #word-embeddings #graph-theory #contrastive-learning #k-nearest-neighbors #evaluation-metrics #confidence-intervals #data-integration
**Contested on:** Every serious competitor in spend analytics is fighting to classify at the line item rather than the supplier and to resolve the supplier master into real entities — and whoever gets those two layers right takes every analysis built on them.

## The Problem
A category manager is preparing to negotiate with a safety equipment supplier and needs to know total spend. The report shows four million dollars. The actual figure is closer to seven, because two million is buying safety products through a general distributor classified as office supplies, and another million is with a subsidiary recorded as a separate supplier under a different name. The manager negotiates from four. This is not an unusual case; it is the ordinary condition of enterprise spend data, and it systematically understates the buyer's position in every negotiation it informs.

## Why Nobody Has Built This
Supplier-level classification is vastly cheaper to implement — one decision per supplier rather than per line — and produces a report that looks complete, so the shortcut was taken early and has been inherited. Line-item classification requires handling descriptions that are abbreviated, inconsistent, frequently supplier-specific and sometimes absent, which is genuinely harder and is exactly the entity-resolution-shaped problem this vault keeps encountering. Supplier resolution has the same obstacle as the CRM case: merges are destructive, negative decisions are not retained, and the duplicates regenerate from every new invoice.

## What to Build
Classification at the line and resolution as a graph. Line-item classification uses the description, the unit of measure, the price point, the supplier's own catalogue where available, the requisition context and the general ledger account, combined — since any one of them alone is weak and together they are strong. Confidence is returned per line, with the uncertain minority routed to a human whose decisions become training data, so accuracy improves with use rather than being fixed at implementation. Supplier resolution produces a graph with typed edges — legal parent, subsidiary, acquired brand, duplicate record — maintained against corporate linkage data and corporate event feeds, with merges non-destructive and negative decisions retained so a considered non-match is never reconsidered from scratch. Across a platform's customer base the same suppliers and the same items recur constantly, which means a pooled classification and resolution corpus makes each customer's data better than any of them could achieve alone — and is the capability no single enterprise can replicate.

## Target Customer
Procurement platform vendors, spend analytics specialists, and the large enterprises whose category strategies rest on a spend cube nobody has validated.

## Impact If Built
Correcting classification and resolution typically increases measured spend concentration substantially, which directly improves negotiating position in every affected category — the buyer discovers they are a larger customer than they thought. Consolidation opportunities that were invisible become visible, and the tail spend analysis that every procurement function performs becomes something other than an artefact of misclassification.
