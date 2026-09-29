# Corporate Linkage and Event Data Already Sold

**Niche:** [[niches/crm-platforms/account-data-hygiene/profile|Account Data Hygiene]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Corporate family trees, registration identifiers and acquisition event feeds are commercially available and have been for decades, and most CRM account hierarchies are maintained by a representative typing a parent account name.
**Tags:** #graph-theory #bert #word-embeddings #evaluation-metrics #confidence-intervals #data-integration #change-point-detection #automation
**Contested on:** Every serious competitor in account data is fighting to keep the relationships between accounts correct — parent, subsidiary, duplicate, acquired — rather than the fields inside them, and whoever holds the hierarchy right takes the account.

## The Problem
An organisation buys enrichment and receives excellent firmographics attached to records whose relationships to one another are wrong. It also, frequently, already subscribes to a data source that carries corporate linkage — the family tree, the parent and ultimate parent, the registration identifiers — and uses it for none of that, because the integration populates fields rather than structure. The linkage data has existed commercially since long before CRM did.

## What Already Exists
Dun & Bradstreet's corporate linkage and the equivalent products from the major business information providers maintain global family trees with stable identifiers. Company registries publish authoritative entity and ownership data in many jurisdictions. Acquisition and corporate event feeds are available commercially and from news sources. Entity resolution tooling is mature. Every component required to maintain a structure rather than a field is purchasable, and much of it is already licensed inside the companies that need it.

## The Customization Gap
The adaptation is to a customer's own view of the account rather than to the legal truth. It requires: (1) multiple coexisting hierarchies — legal ownership, contracting relationship, service or support structure, and the go-to-market view the sales organisation actually runs on — since forcing one tree is what makes the field useless and is the reason it decays; (2) reconciliation between the purchased legal tree and the organisation's own operating view, with the differences surfaced rather than overwritten, because the legal parent is frequently not the buying centre and the sales organisation is right about that; (3) event-driven update with human confirmation on the consequential changes, since an acquisition that moves an account between territories has compensation implications and should not happen silently; (4) confidence and provenance on every edge, so a structure inferred from a name similarity is distinguishable from one sourced from a registry; and (5) a merge path that preserves history, which is the fix note's subject and is what makes structural change safe to perform at all.

## Target Customer
Enterprise sales and revenue operations, master data management functions, and the enrichment vendors whose linkage data is under-used inside their own customers.

## Impact If Solved
The linkage data exists, is frequently already paid for, and is discarded into a field. Modelling several coexisting hierarchies is the specific adaptation that makes the structure survive contact with a sales organisation, and event-driven maintenance is what stops it decaying the week after it is built.
