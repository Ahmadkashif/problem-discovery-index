# ServiceTitan Pricebook Intelligence Layer

**Niche:** [[niches/electrical-contractors/residential-service-repair/profile|Residential Service & Repair]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ServiceTitan's pricebook is a static price list — residential electrical companies need a pricebook that learns from job outcomes, auto-updates material costs, and suggests bundled upsell packages based on the specific service call type.
**Tags:** #gradient-boosting #feature-engineering #automation #data-integration #revenue-impact #evaluation-metrics

## The Problem
ServiceTitan's pricebook is the industry standard for flat-rate pricing, but it functions as a static database — prices are manually entered and manually updated. When copper wire prices jump 20% in a quarter, the pricebook doesn't reflect it until someone manually recalculates every affected line item. When a new NEC code cycle adds AFCI protection requirements to more circuits, the pricebook doesn't auto-add the required materials. Technicians flip through hundreds of pricebook entries on a tablet to find the right service, often defaulting to the 10-15 items they've memorized rather than the full range of profitable services they could offer.

## What Already Exists
ServiceTitan's pricebook handles price display, technician tablet presentation, and invoice generation. Third-party pricebook consultants (George Brazil, Profit Rhino) sell pre-built electrical pricebooks with recommended pricing. Material distributors (Graybar, Rexel, WESCO) publish price sheets. These are all static — none learn from job outcomes or auto-adjust.

## The Customization Gap
Three layers are missing. First, material cost auto-tracking: connect to distributor pricing APIs (Graybar's B2B portal, electrical distributor EDI feeds) and auto-update material cost components of each pricebook entry when supplier prices change, flagging entries where margin has dropped below threshold. Second, intelligent bundling: when a technician selects "diagnose tripped breaker," the system should surface contextual upsell bundles based on the call type — "Panel inspection add-on ($295)" or "Whole-home surge protection ($450)" — ranked by historical close rate for that service-call-to-upsell combination using a gradient-boosted recommendation model. Third, NEC code compliance checking: when the current NEC cycle changes requirements (e.g., 2023 NEC expanded AFCI requirements), auto-flag pricebook entries that need material additions and generate updated pricing.

## Target Customer
Residential electrical shops with 3-15 technicians already on ServiceTitan, spending $5K-15K/year on the platform but leaving margin on the table through stale pricing and missed upsell opportunities.

## Impact If Solved
Eliminates the 2-4 week lag between material cost changes and pricebook updates, protecting 3-8% margin erosion during price spikes. Increases average upsell attachment rate from 15% to 30-40% through contextual recommendations, adding $500-1,500 per technician per week in incremental revenue.
