# Every Manufacturer Writes It Differently

**Niche:** [[niches/b2b-commerce-platforms/attribute-extraction/profile|Attribute Extraction]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** One manufacturer writes 1/2 inch, another writes 0.5", another writes 12.7mm, and the catalogue filter treats them as three different products.
**Tags:** #feature-engineering #word-embeddings #evaluation-metrics #k-nearest-neighbors #automation #quick-win #descriptive-statistics #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn manufacturer documents into catalogue attributes at an accuracy the distributor will publish without review — and whoever reaches that threshold replaces an entire manual function.

## The Problem
The attribute was extracted correctly from every document. It is still unusable, because across three thousand suppliers the same physical property is expressed in a dozen notations, a dozen units, a dozen vocabularies and a dozen orderings. Stainless steel, SS, 316SS and 316 Stainless are four values in the filter. A customer selecting half-inch sees a third of the half-inch products. The data is present and correct and the catalogue still does not work, which is the failure mode nobody anticipates because completeness was the metric.

## Why It's Still Broken
Normalisation is done at ingestion by whoever loaded the feed, inconsistently and without a record. There is no canonical vocabulary for most technical attributes outside a few standardised categories. Mapping rules are written per supplier and decay. And the symptom presents as poor search rather than as a data problem, so it is investigated in the wrong place.

## What a Fix Looks Like
Normalise as a defined, recorded, reversible step. Define a canonical form per attribute type with its unit and precision, which is the prerequisite and is usually absent — most catalogues have a field and no specification for it. Convert units at load while keeping the source value, so the original remains auditable and a manufacturer's own notation can still be displayed. Cluster raw values per attribute to expose the vocabulary actually present, which is a fast diagnostic that immediately shows where the filter is broken and needs no modelling. Build synonym maps semi-automatically from those clusters with review, rather than authoring them by hand per supplier. Handle ranges, tolerances and approximations explicitly instead of coercing them to a number, since silently dropping a tolerance is worse than leaving the field empty. Normalise at query time as well, so a customer typing half-inch matches 0.5 and 12.7mm regardless of how the catalogue stored it — which is where the customer-visible gain is. Report per-attribute normalisation coverage to the catalogue manager as part of the prioritised queue. And push the canonical form back to suppliers as the preferred submission format, which slowly reduces the problem at source.

## Who Feels the Pain
Customers whose filter selection silently hides two-thirds of the qualifying products; catalogue managers whose completed work does not improve findability; and distributors whose search performance is blamed on the search engine.

## Impact If Fixed
Completeness was the metric, so nobody anticipated correct data that still does not work. Clustering raw values per attribute is a modelling-free diagnostic that shows exactly where the filter is broken, and query-time normalisation is where the customer-visible gain lands.
