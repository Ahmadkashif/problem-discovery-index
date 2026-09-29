# Product Matching Adapted to Marketplace Listing Chaos

**Niche:** [[niches/ecommerce-sellers/ecommerce-share-measurement/profile|E-Commerce Share Measurement Providers]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Entity resolution products match records describing the same product; on marketplaces the same product appears as forty listings, a multipack, a variation child, and a bundle, and deciding which of those is the same product is the measurement.
**Tags:** #contrastive-learning #bert #transformers #cnns #word-embeddings #random-forests #evaluation-metrics #feature-engineering #automation #data-integration

## The Problem
Share depends on knowing which listings correspond to which product, and marketplace listing structure is designed for merchandising rather than measurement. One product appears under many sellers with different titles, in multipacks that must be unit-normalized, as variation children under a parent that may mix genuinely different products, and inside bundles that contain items from other categories. Analysts maintain the mapping by hand for high-value products and accept error elsewhere, which puts the measurement error precisely in the long tail where competitive surprises originate.

## What Already Exists
Product matching is a well-served problem. The entity resolution platforms, the retail-specific matching vendors, and the standard embedding-plus-blocking approaches all handle title and attribute similarity at scale, with human review queues and good tooling.

## The Customization Gap
Those tools resolve records to entities under the assumption that one record describes one product. Marketplace listings violate that constantly — a multipack is the same product at a different quantity, a bundle is several products, and a variation parent is a container rather than a thing. So the matching problem is really a decomposition problem: parse the listing into what it actually contains and at what quantity, then match. No general product matching product does that, because in most catalogues it never arises. The adaptation is listing decomposition as an explicit step — quantity and pack size extraction from titles and images, bundle component identification, variation structure interpretation — followed by matching on the decomposed units, with unit normalization so that share is computed on comparable quantities. Confidence must be per-listing, so unresolved and ambiguous listings are quantified rather than silently dropped, since dropping them is what quietly biases share toward well-structured sellers.

## Target Customer
Heads of data operations and taxonomy at share measurement providers, and the analysts who maintain product mappings by hand for the products that matter and guess at the rest.

## Impact If Solved
Removes the largest silent error source in the flagship metric and extends reliable measurement into the long tail, which is where a brand most wants early warning and where every competitor is equally weak.
