# VIN-Based Recall Auto-Check on Vehicle Intake

**Niche:** [[niches/auto-repair-shops/warranty-compliance-tracking/profile|Warranty & Recall Compliance Tracking]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** NHTSA's free recall database exists, but no shop management system auto-queries it during vehicle intake — so open recalls go unmentioned on 30-40% of affected vehicles.
**Tags:** #data-integration #automation #quick-win #compliance

## The Problem
NHTSA maintains a comprehensive, free, VIN-specific recall lookup database. But checking it requires the service advisor to open a separate browser tab, type the VIN, and review results — a manual step that gets skipped on busy days. Industry data suggests 25-40% of vehicles in independent shop bays have at least one open recall that the shop doesn't mention. This is a missed opportunity: while independent shops can't perform recall work (dealers do), informing the customer builds trust and positions the shop as a thorough, customer-first operation.

## What Already Exists
NHTSA's recall API is free and well-documented. Carfax provides recall data in vehicle history reports. Some newer shop management systems (Tekmetric) have added basic recall lookup, but it requires manual action — it's a feature buried in a menu, not an automatic part of intake.

## The Customization Gap
The integration needs to be automatic and zero-effort: when a VIN is entered during vehicle intake (which already happens in every shop management system), the system auto-queries NHTSA and surfaces any open recalls as a prominent alert on the repair order. The alert should include a customer-ready explanation and a link to schedule the recall work at their dealer. This should be a default-on feature, not an optional menu item.

## Target Customer
Shop owners using any modern shop management system who want to build customer trust by proactively informing customers of open recalls.

## Impact If Solved
Adds a trust-building touchpoint on 25-40% of customer visits at zero cost to the shop. Shops that proactively notify customers of recalls see 15-20% higher retention rates — those customers perceive the shop as looking out for their interests, not just billing them.
