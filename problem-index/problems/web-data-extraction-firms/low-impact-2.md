# Cross-Source Schema Normalisation

**Industry:** [[web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Extraction from a thousand sites produces a thousand shapes of the same entity, and reconciling them into one usable dataset is the work customers assume they are buying and are not.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #dbscan #large-language-models #evaluation-metrics #data-integration #feature-engineering

## The Problem
A customer wants product data across a category. Extraction runs against three hundred retailer sites and returns three hundred variations of the same entity.

Product names differ across every site. Sizes appear as "500ml", "0.5L" and "16.9 fl oz". Prices carry different currencies, tax treatments and units. Categories follow each retailer's own taxonomy. Availability is expressed as a badge, a phrase or an absence. The same physical product has a different identifier everywhere, and identifiers that should be universal are populated inconsistently.

Delivering a usable dataset means normalising units, reconciling taxonomies, and — the hard part — determining which records across which sites refer to the same product.

Firms deliver the raw extraction and leave this to the customer, or perform it as a bespoke professional services engagement per customer, per category, repeatedly.

## What Already Exists
Data transformation tools handle unit conversion and format normalisation once the mapping is specified. Entity resolution libraries and commercial matching services exist. Product identifier standards (GTIN, ASIN, MPN) exist and are populated inconsistently, particularly for own-brand and long-tail goods. Taxonomy mapping tools exist for structured catalogues. Model-based extraction can return normalised values directly when instructed.

## The Customisation Gap
Normalisation requires domain semantics that a generic tool does not have. Knowing that a pack of six units is comparable to a single unit at a sixth of the price, or that two retailers' size descriptors denote the same physical product, is category knowledge encoded nowhere.

Entity resolution across retail sites is genuinely hard where identifiers are absent, which is precisely for own-brand, long-tail and fast-moving goods — the products where competitive monitoring is most valuable.

The reusability failure is the notable one. The same normalisation is performed by every customer monitoring the same category from the same sites, and by the firm itself in every professional services engagement, and none of it accumulates. The firm sees more of this than any individual customer ever will and retains none of it as a shared asset.

Taxonomy reconciliation is the third gap: every retailer's category tree differs, mapping between them is stable once established, and it is re-established per engagement.

## Impact If Solved
Normalisation is the difference between a raw extraction feed and a usable dataset, and it is either dumped on the customer or rebuilt as services revenue. Accumulating category-level normalisation and entity resolution as a shared asset moves the firm from selling pages to selling data, which is where the margin is.
