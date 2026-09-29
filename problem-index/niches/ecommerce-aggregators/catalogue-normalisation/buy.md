# Product Data Management and Entity Resolution

**Niche:** [[niches/ecommerce-aggregators/catalogue-normalisation/profile|Catalogue Normalisation]]
**Industry:** [[industries/ecommerce-aggregators|Ecommerce Aggregators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product information management and entity resolution are mature product categories built for exactly this, and aggregators maintain forty spreadsheets.
**Tags:** #data-integration #k-nearest-neighbors #bayesian-inference #large-language-models #evaluation-metrics #automation #graph-theory #word-embeddings
**Contested on:** Every serious competitor in this niche is fighting to describe forty acquired brands' products in one vocabulary — and whoever does that unlocks the synergy, because every portfolio-level decision requires comparability the catalogues do not have.

## The Problem
Bringing product data from many sources into one governed schema is what product information management systems do, and deciding whether two records describe the same thing is entity resolution. Both are mature product categories with vendors, implementations and a large body of practice, used routinely by distributors and retailers who assemble catalogues from many suppliers. An aggregator's problem is that exact shape, assembled by acquisition rather than by supply agreement, and the sector runs it on spreadsheets.

## What Already Exists
Product information management platforms with schema governance and attribute validation; entity resolution and record linkage tooling; attribute extraction from unstructured product content; data quality rules for units and value normalisation; and taxonomy mapping between source and target classifications.

## The Customization Gap
The adaptation is to source data that is a marketplace listing rather than a supplier feed. It requires: (1) extraction from listing content and images rather than from structured feeds, since the acquired brands have no supplier feeds and the best available description is the consumer-facing listing — which is what language and vision models now handle and what made this tractable; (2) supplier correspondence as a data source, since the specification frequently exists only in an email thread and nobody has treated that as ingestible content; (3) resolution across brands with no shared identifier scheme, where the match is on physical characteristics rather than on a code; (4) manufacturability grouping as an output, since the sourcing question is which products could be made together and standard product classification does not express it; and (5) an implementation scoped for a mid-sized operator, since the enterprise platforms are priced and scoped for far larger catalogues.

## Target Customer
Aggregator sourcing and operations teams, product information vendors for whom this is an adjacent market, and the entity resolution community.

## Impact If Solved
The mature tooling assumes supplier feeds and the only description here is a consumer listing, which vision and language models now handle. Treating supplier correspondence as an ingestible source recovers the specifications that exist nowhere else.
