# A Thousand Shapes of the Same Entity

**Niche:** [[niches/web-data-extraction-firms/cross-source-normalisation/profile|Cross-Source Normalisation]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Extraction from a thousand sites produces a thousand shapes of the same entity, and reconciling them into one usable dataset is the work customers assume they are buying and are not.
**Tags:** #graph-theory #k-nearest-neighbors #large-language-models #evaluation-metrics #data-integration #bayesian-inference #hypothesis-testing #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a thousand sites' worth of the same entity into one coherent dataset — and whoever does that takes the account, because that reconciliation is the work customers assume they are buying.

## The Problem
A customer collects product listings from eight hundred retailers. They receive eight hundred feeds. Prices are sometimes inclusive of tax and sometimes not, in six currencies, occasionally as a range. Availability is a boolean at one site, a stock count at another, an estimated delivery date at a third. Every retailer has its own category tree. The same product appears under eight hundred different identifiers and four hundred spellings. The customer's data team spends six months building normalisation and product matching, which is the actual project, and the extraction firm — which sees all eight hundred sites and could have built it once — delivered raw.

## Why Nobody Has Built This
Normalisation requires domain opinions the firms have avoided taking, since a canonical product schema is a commitment and delivering raw is not. Customers ask for fields rather than for a dataset, so the requirement is never stated at purchase. Building it per domain is real investment against a business model priced per request. And the work happening at the customer is invisible to the firm, which sees a successful delivery.

## What to Build
Normalise once, for everyone. Publish a canonical schema per domain — products, listings, companies, places, jobs — with explicit semantics for each field, since every customer invents one and they converge, which makes this the reusable core rather than the bespoke part. Build and maintain per-site mappings into it, which is the firm's natural asset because they already parse every site and the mapping is a small addition to work they do anyway. Normalise units, currencies, tax treatment and date semantics explicitly, recording what was assumed, since a silently normalised price is worse than a raw one. Build taxonomy crosswalks from each site's categories into a canonical one, which is a large accumulating asset that no single customer could justify and every customer needs. Resolve entity identity across sites where possible, offering a stable identifier, which is the hardest and most valuable piece. Deliver both raw and normalised, so a customer who disagrees with a normalisation decision can override it rather than being stuck. Report normalisation confidence per field, since some mappings are certain and some are judgement. And reuse mappings across customers collecting from the same sites, which is what makes the economics work.

## Target Customer
Data teams consuming multi-source extraction, and the firms whose customers are all independently building the same reconciliation layer.

## Impact If Built
Reconciliation is the customer's actual project and the firm parses every site already. Per-site mappings into a published canonical schema, plus taxonomy crosswalks, are assets that accumulate across customers and that no individual customer could justify building.
