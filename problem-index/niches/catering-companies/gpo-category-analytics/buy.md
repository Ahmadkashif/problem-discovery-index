# Spend Analytics Platforms Classify Invoices; They Do Not Know a Case of Chicken Thighs

**Niche:** [[niches/catering-companies/gpo-category-analytics/profile|Foodservice GPO Category Analytics]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Procurement suites, spend classification engines and contract lifecycle tools are all mature and all stop at the level of a supplier and a category, while every question here lives at the level of an item, a pack size and a usable yield.
**Tags:** #bert #k-means-clustering #feature-engineering #data-integration #evaluation-metrics

## The Problem
A GPO's analytical operation looks like enterprise procurement and is tooled as such. There is a spend analytics platform, a contract lifecycle management system, supplier performance dashboards, a data warehouse and a BI layer, and often a spend classification vendor to tidy the taxonomy.

Enterprise procurement software is built to answer: how much do we spend, with whom, in which category, and are we on contract. Those are the right questions for indirect spend across a corporation. They are the wrong resolution for food, where the entire economics turn on the difference between two items that classify identically.

## What Already Exists
Source-to-pay suites cover requisition, contract, invoice and payment. Spend classification engines map transactions to taxonomies with reasonable accuracy. Supplier risk and performance products track delivery and financial health. Distributor portals supply purchase data feeds. BI platforms deliver savings and compliance reporting. Commodity market data services publish futures and index prices.

## The Customization Gap
**The item master is the product and no platform normalises it.** The same chicken thigh arrives as a distributor-specific code, a manufacturer code, a brand item and a distributor equivalent, in three pack configurations, from four distributors, described inconsistently. Classification engines put all of them in "poultry" and consider the job done. Every analysis worth doing — price comparison, substitution, compliance, index construction — requires knowing that these six records are the same purchasable thing, and that is item-level entity resolution over a large, drifting, free-text catalogue. It is the single largest unsolved problem in the operation and no vendor sells it.

**Price per case is not price.** Comparing items requires normalising to a usable unit: pack size, count, drained weight, trim yield, cooked yield. Two items at the same case price can differ substantially in cost per portion. Procurement tooling compares unit price as invoiced, which is the number that misleads.

**Substitutes must be defined, and nothing defines them.** Category taxonomies are hierarchies. Substitution is a graph — which items operators actually switch between, revealed by behaviour and not by taxonomy. Building that graph from transaction data is the foundation of any price or elasticity work and there is no bought component for it.

**Rebate reconciliation is bespoke, everywhere.** GPO economics run on manufacturer rebate agreements with tiered volume terms, item eligibility rules and exclusions. Reconciling entitlement against actual purchases is a large, error-prone, high-stakes calculation that source-to-pay suites do not model, and it is generally run in spreadsheets by people who have done it for years.

**Compliance is reported, not diagnosed.** Platforms flag off-contract purchasing. They do not explain it — whether the operator did not know, the distributor substituted, the contracted item was unavailable, or the alternative was genuinely better. Each cause has a different remedy and the report says only that leakage occurred.

**Commodity feeds are the wrong series.** Futures and published indices track raw commodities. What an operator pays for a finished, processed, packed foodservice item is related to that but is not it, and the relationship differs by category. The GPO can measure the actual pass-through and instead references the commodity feed.

## Target Customer
Chief Procurement Officer or Head of Data at a GPO or contract caterer purchasing arm. The buy-and-build split is unusually clean: keep the source-to-pay, contract and BI layer entirely, and build the item resolution, unit normalisation and substitution graph that everything else in the business depends on and no vendor supplies.

## Impact If Solved
Every analysis the category organisation produces — savings, compliance, price movement, supply risk — rests on knowing which purchase records refer to the same food. That layer is built by hand, incompletely, and rebuilt every time a distributor changes a catalogue.
