# Marketplace Ranking From Commerce

**Niche:** [[niches/lending-marketplaces/borrower-routing/profile|Borrower Routing]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Commerce marketplaces learned that ranking on clicks destroys the marketplace and moved to post-purchase outcomes, and lending marketplaces are still on clicks.
**Tags:** #gradient-boosting #matrix-decompositions #evaluation-metrics #causal-inference #confidence-intervals #revenue-impact #hypothesis-testing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to send each borrower to the lender who will actually approve them on the best terms — and the contest splits cleanly enough that it is not terminal.

## The Problem
Commerce marketplaces went through this exactly. Early ranking optimised clicks, which favoured whatever looked appealing regardless of whether the transaction completed or the buyer was satisfied. The fix was to rank on downstream outcomes — completed purchases, returns, reviews, repeat behaviour — and to build the data pipelines and seller obligations that make those outcomes observable. Lending marketplaces face the same structure and have not made the move, because the equivalent of the completed purchase happens inside the lender.

## What Already Exists
Outcome-based marketplace ranking; seller quality scoring from post-transaction signals; auction designs that blend bid with quality; counterfactual evaluation of ranking policies; and the data obligations marketplaces impose on sellers.

## The Customization Gap
The adaptation is to a transaction that completes inside the counterparty. It requires: (1) outcome data that must be contractually obtained rather than natively observed, which is the substantive difference and makes this commercial before technical; (2) a regulated decision where the lender's criteria are proprietary and sometimes legally constrained from disclosure; (3) an outcome that unfolds over years, since loan performance is the real quality signal and arrives far too late for ranking; (4) borrower cost measured in credit inquiries and rates rather than in a return shipment; and (5) fair lending considerations in the ranking itself, which commerce ranking never has to weigh.

## Target Customer
Product and data leadership, lender partners, regulators examining marketplace practices, and ranking platform vendors from commerce.

## Impact If Solved
Commerce solved this by making outcomes observable and obligatory. The lending version requires winning the same data by contract, and the ranking machinery is otherwise directly transferable.
