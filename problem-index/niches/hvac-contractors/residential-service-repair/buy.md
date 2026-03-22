# ServiceTitan Pricebook Without Diagnostic Guidance

**Niche:** [[niches/hvac-contractors/residential-service-repair/profile|Residential Service & Repair]]
**Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ServiceTitan handles scheduling, dispatching, and flat-rate pricing for residential HVAC — but the pricebook is a static price list with no connection to diagnostic workflow, leaving technicians to flip through hundreds of entries while standing in a homeowner's attic trying to figure out what's actually wrong.
**Tags:** #gradient-boosting #automation #data-integration #revenue-impact

## The Problem
ServiceTitan's pricebook presents residential HVAC technicians with a flat-rate menu — "Replace run capacitor: $285," "Add 1 lb R-410A refrigerant: $125," "Replace contactor: $310" — but it has no diagnostic intelligence connecting symptoms to the correct pricebook entries. A technician who has diagnosed a failed capacitor can find the pricebook entry and present it to the homeowner, but the pricebook cannot help a technician who knows the outdoor unit is humming but not starting figure out whether the problem is the capacitor, contactor, compressor, or wiring. The pricebook also doesn't suggest related repairs: if the capacitor failed because the contactor is pitted and pulling excessive amperage, an experienced technician knows to recommend replacing both — the pricebook just shows them as separate line items with no relationship.

## What Already Exists
ServiceTitan's pricebook handles price display, technician tablet presentation, and invoice generation. Coolfront provides a mobile flat-rate pricing app with HVAC-specific categories. National Comfort Institute sells pre-built HVAC pricebooks with recommended pricing tiers. All three are static price lists organized by equipment category, not by diagnostic workflow. None connect the technician's diagnosis to the appropriate repair options, and none suggest related repairs or maintenance bundles based on the primary diagnosis.

## The Customization Gap
Two layers are missing. First, diagnostic-to-pricebook mapping: when a technician enters a diagnosis (or uses a diagnostic tool to identify the problem), the pricebook should surface the specific repair options, including related repairs that experienced technicians would bundle. "Capacitor failure" should surface not just "Replace run capacitor: $285" but also "Inspect/replace contactor: $310" (because contactor issues cause capacitor failures) and "Electrical safety inspection: $195" (because electrical component failures warrant a full check). This mapping requires a recommendation model trained on historical job data — which repairs are commonly performed together, and which bundles have the highest close rates. Second, seasonal pricing intelligence: a pricebook entry for "AC tune-up" should price differently in March (pre-season, competitive, drive volume) than in July (peak demand, pricing power, capacity constrained), but current pricebooks use year-round static pricing.

## Target Customer
Residential HVAC shops with 5-20 technicians on ServiceTitan or Coolfront, generating $2-10M in annual revenue, frustrated by junior technicians who can't navigate the pricebook effectively and miss bundled upsell opportunities that experienced techs identify automatically.

## Impact If Solved
Increases average ticket by 15-25% through diagnostic-driven bundled recommendations, adding $300-750K in annual revenue for a 10-truck shop. Reduces pricebook lookup time by 60% by surfacing relevant entries based on diagnosis rather than requiring manual search through category trees.
