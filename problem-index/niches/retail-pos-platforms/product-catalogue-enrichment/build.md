# A Shared Specialty Catalogue Built From Merchant Entries

**Niche:** [[niches/retail-pos-platforms/product-catalogue-enrichment/profile|Product Catalogue Enrichment]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Two thousand merchants buy the same vendor's line and each of them types the same attributes for the same products, and the platform that holds all two thousand entries treats each as private configuration.
**Tags:** #bert #word-embeddings #contrastive-learning #k-nearest-neighbors #evaluation-metrics #confidence-intervals #transfer-learning #automation
**Contested on:** Every serious competitor in retail catalogue is fighting to populate a specialty item's attributes without the merchant typing them — and whoever holds attribute completeness highest at zero merchant effort takes the account.

## The Problem
A boutique receives a spring order from a vendor: sixty styles, each in several colours and sizes. The owner enters them — style name, colour, size, fabric, category, season, cost, retail — over two evenings. The same vendor shipped the same styles to hundreds of other boutiques on the same platform, each of which is doing the same thing this week. The platform holds every one of those entries and treats them as unrelated rows in unrelated tenants.

## Why Nobody Has Built This
Catalogue data has been treated as merchant-private configuration, which is a defensible default and has never been examined — a vendor's style name, fabric and colourway are not commercially sensitive to the merchant in any meaningful sense, though the cost and retail price are. Matching entries across merchants is also genuinely non-trivial, because merchants name things differently, use different category vocabularies and enter partial data, so the same item appears in a hundred slightly different forms. Solving that is exactly the entity resolution problem that recurs throughout this vault, and it has the same answer.

## What to Build
A shared catalogue assembled from merchant entries, with commercially sensitive fields excluded structurally. Entries are matched across merchants by vendor, style identifier, name similarity, attribute overlap and image similarity, resolving to canonical items. Attributes are consolidated with confidence, so a field entered consistently by forty merchants is high-confidence and one entered by two is not. A merchant entering a new item is offered the canonical record — type three characters of the style name and the rest arrives — with their own cost and price entered privately. Corrections flow back and improve the canonical record. Vendors can claim and enrich their own items, which is in their interest and costs them nothing, and is the mechanism that makes the catalogue authoritative rather than crowdsourced. The design commitment that makes this acceptable is explicit: descriptive attributes are shared and commercial terms never are, stated plainly to merchants rather than buried.

## Target Customer
POS platforms with large specialty merchant bases, wholesale platforms holding vendor catalogues, and the brands themselves, who benefit from their products being described consistently.

## Impact If Built
Catalogue entry is among the most-complained-about tasks in independent retail and is almost entirely duplicated effort. Beyond the hours, consistent attributes are the precondition for the size curve analysis, markdown modelling and cross-merchant learning that the merchandising niche depends on — which makes this the quiet foundation of the most valuable capability in the industry.
