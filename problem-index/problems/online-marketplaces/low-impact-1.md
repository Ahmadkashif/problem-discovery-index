# Category Taxonomy and Search Relevance

**Industry:** [[online-marketplaces|Online Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Search infrastructure and learned ranking are mature commodities, and marketplace search still fails because the inventory is described by amateurs against a taxonomy designed by someone else.
**Tags:** #bert #word-embeddings #transformers #k-means-clustering #evaluation-metrics #gradient-boosting #cnns #feature-engineering

## The Problem
A marketplace organises inventory into categories and lets buyers search. Both mechanisms depend on listings being described consistently, and they are not.

Sellers choose categories that feel right, which produces systematic misfiling — the vintage dress listed under costumes, the guitar pedal under accessories. Titles are written for humans or stuffed with keywords the seller believes help. Attributes are optional and frequently blank, because a seller listing from a phone will not fill in twelve fields.

The taxonomy itself is a permanent problem. It was designed once, it never fits the inventory that actually arrives, and updating it is disruptive because existing listings must be remapped. Marketplaces end up with categories that are enormous and useless alongside categories nobody uses.

The result is that search works well for buyers who know exactly what to type and badly for browsing, which is how most marketplace discovery actually happens — particularly for the unique inventory that defines these platforms.

## What Already Exists
Elasticsearch, OpenSearch and managed search services provide capable retrieval. Learned ranking is standard at any serious marketplace. Vector search over listing embeddings is increasingly deployed. Image understanding for category and attribute prediction is mature. Query understanding and spelling correction are well solved. Faceted navigation is a standard pattern.

## The Customisation Gap
Ranking improvements assume the underlying data is right, and the failure here is upstream in the listing. A perfectly ranked search over mis-categorised inventory with missing attributes returns the wrong things well.

Automatic categorisation and attribute extraction from images and text is where the leverage sits, and it is applied inconsistently — often as a suggestion the seller can ignore rather than as the system of record. Images are the richest signal, are always present, and are still secondary to seller-typed text at most platforms.

Taxonomy induction is the second unexploited path. What categories actually exist in the inventory is discoverable by clustering listings, and comparing that against the designed taxonomy shows exactly where the structure has diverged from reality. Nobody does this, so taxonomies are updated by committee.

Query intent for browse is the third gap. A short query on a marketplace expresses a fuzzy desire rather than a product lookup, and treating it as a lookup is why browse experiences are poor. Understanding a query as a region in attribute space rather than as a string to match is a different design.

## Impact If Solved
Search and browse are how every transaction begins, and their quality is bounded by listing data quality rather than by ranking sophistication. Extracting attributes automatically and inducing taxonomy from actual inventory fixes the input rather than tuning the output, which is where the remaining gains are.
