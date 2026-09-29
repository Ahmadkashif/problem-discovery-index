# A Pooled Mapping of Distributor Items to Ingredients

**Niche:** [[niches/restaurant-tech-platforms/invoice-to-recipe-costing/profile|Invoice-to-Recipe Costing]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same distributor item appears on thousands of a vendor's customers' invoices and has been mapped to the right ingredient hundreds of times already, and every new customer maps it again from scratch.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #gradient-boosting #evaluation-metrics #confidence-intervals #transfer-learning #automation
**Contested on:** Every serious competitor in restaurant back office is fighting to map a distributor invoice line to the recipe ingredient it actually is, at a cost per usable unit — and whoever holds the automatic match rate highest takes the account.

## The Problem
A restaurant onboards onto a back-office product. Its last three months of invoices contain nine hundred distinct line items across four distributors, each an abbreviated description with a pack size and a code. Somebody — usually the chef, in the evening — maps them to the restaurant's ingredient list. It takes days. Then the distributor changes a product code, substitutes a brand, or the restaurant switches suppliers, and the mapping decays. Within a year a meaningful fraction of the plate costs the product reports are computed from unmapped or mis-mapped items, and the operator has stopped believing the numbers.

## Why Nobody Has Built This
Cross-customer pooling is the obvious answer and requires a decision that the mapping corpus is a vendor asset rather than a per-customer configuration, which nobody has made — partly from a vague sense that customer data should stay siloed, even though a mapping from a distributor's public item code to a generic ingredient discloses nothing about any restaurant. Beyond that, the matching problem has genuine difficulty: descriptions are heavily abbreviated in inconsistent ways, the same product appears under different codes across distributors, and the correct target depends on the restaurant's own ingredient taxonomy, which differs between customers. Yield factors add a second layer that nobody has attempted at all.

## What to Build
A pooled mapping service: every confirmed customer mapping becomes an observation linking a distributor item code and description to a canonical ingredient, and new invoice lines are matched against that corpus first, the canonical ingredient list second, and the customer's own history third. Confidence-gated, so high-confidence matches apply silently and the remainder is presented as a ranked choice rather than a blank. Pack size and unit conversion are handled explicitly and are where most silent errors originate. Yield factors are the second half of the product and the more valuable one: a canonical library of trim and cooking yields by product and preparation, seeded from published references and refined from customers' own theoretical-versus-actual usage variance, which is a signal every one of these products already computes and none uses this way. The match rate is the headline metric and should be reported to customers per period.

## Target Customer
Restaurant back-office and inventory vendors, the distributors themselves, and the multi-unit operators for whom stale plate costs across forty units is a real financial exposure.

## Impact If Built
Onboarding drops from days of a chef's evenings to a review session, which removes the single largest friction in selling this category of product. Ongoing mapping decay — the reason operators stop trusting their own plate costs — largely disappears. And a yield library is the first correction to a number that has been confidently wrong across the entire industry for as long as it has been computed.
