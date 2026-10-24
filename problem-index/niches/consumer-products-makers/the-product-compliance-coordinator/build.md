# One Compliance File per SKU, Filed at the Border

**Niche:** [[niches/consumer-products-makers/the-product-compliance-coordinator/profile|The Product Compliance Coordinator]]
**Industry:** [[industries/consumer-products-makers|Consumer Products Makers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** CPSC eFiling made certificate data a per-shipment obligation, and most makers keep that data in PDFs on a shared drive.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #compliance #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to have every SKU's certificate, test report and warning ready before listing and import, and whoever clears the most SKUs to listing without a compliance hold takes the account.

## The Problem
For each import entry the broker needs the product identifier, the rules certified, the certifier, the lab and dates. For each new listing the retailer needs test reports and warnings. The coordinator assembles both by hand from scattered documents.

## Why Nobody Has Built This
Compliance software targets large manufacturers with many components; small makers were not asked to file certificate data per shipment until July 2026.

## What to Build
A per-SKU file that extracts recipe and component data, maps each SKU to the rules that apply (lead-wick ban, lighter child-resistance, art-material labelling, Prop 65), links test reports and drafts certificates, exports the eFiling data elements to the broker, and checks labels against the required wording. Supplier formula changes re-open the affected files.

## Target Customer
Compliance coordinators at importing makers with a few hundred to a few thousand SKUs.

## Impact If Built
File-building time falls from ~2–4 hours to ~30 minutes per new SKU (estimate), listing holds for missing documents fall by about half (estimate), and an enforcement question is answered from one record.
