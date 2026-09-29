# Spend Classification & Supplier Master

**Parent Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Category:** High Market Share
**Contested on:** Every serious competitor in spend analytics is fighting to classify at the line item rather than the supplier and to resolve the supplier master into real entities — and whoever gets those two layers right takes every analysis built on them.

## Profile
**Market Size:** ~$2.3B US spend analytics, classification and supplier master data management
**Share of Parent Industry:** ~26% of procurement software revenue, and a precondition for the rest
**Digital Adoption:** Medium — every suite reports spend by category and the categories are approximations
**Target Buyer:** Procurement analytics, category management and master data leaders
**Automation Potential:** Very High — this is text classification and entity resolution with abundant labelled data

## What Makes This a Distinct Niche
Everything procurement claims to do rests on knowing what a company buys and from whom. Both are wrong in most implementations. Classification is typically performed at the supplier level — a supplier is assigned a category and all their spend inherits it — which means a large distributor selling office supplies, safety equipment, packaging and janitorial products appears as a single category, and the consolidation opportunity across the four real categories is invisible. The supplier master, meanwhile, contains the same vendor multiple times under name variants, legal entities, acquired brands and regional subsidiaries, so negotiation leverage is understated, concentration risk is underestimated, and the largest supplier by actual spend is frequently not the largest supplier in the report. Every downstream number — savings, consolidation opportunity, tail spend, category coverage — inherits both errors, and the errors run in a consistent direction: they make the estimate of leverage smaller than reality.

## Current Tools & Gaps
Coupa, SAP Ariba, Jaggaer and Oracle all ship spend classification; specialist providers offer classification as a service, typically with a human-in-the-loop component; enrichment vendors supply supplier firmographics and corporate linkage. The gaps: line-item classification is offered by few and adopted by fewer, because the line description is messy and the suites default to supplier-level assignment; supplier resolution relies on name matching and manual merges, which are destructive and recreate the duplicates repeatedly; corporate hierarchy — which determines true concentration and negotiation position — is a field rather than a maintained structure, exactly as in the CRM account hygiene niche; and nobody measures classification accuracy, so a procurement organisation cannot say how much of its own spend report is right.

## Problems
- [[niches/procurement-spend-platforms/spend-classification-supplier-master/build|🔨 Build: Line-Item Classification and a Resolved Supplier Graph]]
- [[niches/procurement-spend-platforms/spend-classification-supplier-master/buy|🛒 Buy: Product Classification and Entity Resolution Off the Shelf]]
- [[niches/procurement-spend-platforms/spend-classification-supplier-master/fix|🔧 Fix: Nobody Measures Classification Accuracy]]
