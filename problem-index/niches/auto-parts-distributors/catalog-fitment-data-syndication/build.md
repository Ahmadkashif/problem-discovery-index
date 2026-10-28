# Fitment Returns Fed Back Into the Supplier's ACES File

**Niche:** [[niches/auto-parts-distributors/catalog-fitment-data-syndication/profile|Catalog Data Ingestion & Fitment Syndication]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Catalog files are validated for format, never for truth; the only test of an application is whether the part stayed on the car, and that evidence sits at the returns desk.
**Tags:** #graph-neural-networks #graph-theory #gradient-boosting #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to deliver supplier catalog data that resolves each part to the vehicles it fits, and whoever ships the catalog with the fewest fitment returns per thousand lines sold takes the account.

## The Problem
A wrong application (a missing qualifier, a year range that runs one year too long, a production split one supplier ignores) produces wrong parts at every store that sells it, until enough returns accumulate for someone to investigate. Format validators pass these files because they are well formed.

## Why Nobody Has Built This
Returns are coded loosely and not linked to the application line; supplier files and the VCdb are licensed under terms that discourage sharing; and catalog teams are sized to process files, not investigate outcomes.

## What to Build
Link each fitment return to the vehicle configuration and the application line that produced the sale; score every application by its return rate against peers (other brands' interchangeable parts on the same configuration) and by graph anomalies on the vehicle-part bipartite graph; route the top suspects to the catalog team with the evidence, and send confirmed corrections to the supplier as a structured change request. Track fitment returns per thousand lines by supplier as the headline measure.

## Target Customer
Catalog and product data leaders at chains, warehouse distributors and programme groups; suppliers and catalog content vendors.

## Impact If Built
If fitment returns on corrected applications fell by ~half (estimate) and they make up ~20–35% of returns (vendor claims, search summary), a distributor with ~$10M of annual returns would cut ~$1–1.5M of them.
