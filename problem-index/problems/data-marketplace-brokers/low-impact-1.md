# Cross-Provider Schema Harmonisation

**Industry:** [[data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every data integration tool on the market will map one schema to another, and a buyer combining four providers covering the same entities still writes four bespoke pipelines and an entity resolution layer nobody sells.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #dbscan #graph-neural-networks #evaluation-metrics #data-integration #feature-engineering

## The Problem
A buyer rarely uses one dataset. They combine several: firmographics from one provider, contact data from another, technographics from a third, intent signals from a fourth. Each covers overlapping entities with different identifiers, different field definitions, different taxonomies and different update cadences.

Combining them requires two things. Schema mapping — this provider's `emp_range` is that provider's `employee_count` bucketed differently — which is tedious and tractable. And entity resolution — establishing that this company record and that one refer to the same business — which is genuinely hard and is where all the effort goes.

Neither is provided. The marketplace delivers files or shares. The buyer's data engineering team builds the pipeline, the crosswalks and the matching, and maintains them as each provider changes its schema unilaterally.

The same work is done by every buyer of the same combination of providers, independently, at every company.

## What Already Exists
Data integration and transformation tools (Fivetran, dbt, Airbyte) handle movement and transformation competently. Master data management platforms perform entity resolution at enterprise scale. Identity resolution vendors specialise in it commercially. Cloud marketplaces deliver data without physical movement. Some providers publish crosswalks to common identifiers such as DUNS numbers or LEIs. Schema registries exist for streaming contexts.

## The Customisation Gap
Integration tools move data and do not know what it means. Mapping requires understanding that two differently named fields represent the same concept with different definitions — one counts full-time employees, the other counts all staff — and that difference matters and is documented in prose if at all.

Entity resolution across commercial datasets is the specific gap. Companies appear under legal names, trading names and abbreviations, at different addresses, with subsidiaries and acquisitions changing the picture. Standard identifiers exist and are inconsistently populated, precisely because populating them is the expensive part.

The marketplace is positioned to solve this once for everyone and does not. It sees the same provider combinations purchased repeatedly, and the mapping between any two providers in a category is largely fixed — so the crosswalk built by one buyer would serve every subsequent one.

Schema drift is the maintenance burden. Providers change fields without notice, downstream pipelines break silently, and nothing monitors for it — which is straightforward to detect at the marketplace layer and is not.

## Impact If Solved
Integration cost is a substantial and invisible tax on every data purchase, and it is duplicated across every buyer of the same combination. Maintaining crosswalks and resolution at the marketplace layer converts a recurring engineering project into a delivered capability, and drift monitoring prevents the silent breakages that make buyers distrust purchased data.
