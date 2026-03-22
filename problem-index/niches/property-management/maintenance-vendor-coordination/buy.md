# AppFolio with Vendor Intelligence

**Niche:** [[niches/property-management/maintenance-vendor-coordination/profile|Maintenance & Vendor Coordination]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** AppFolio's maintenance module stores vendor records and work order history but doesn't use this data to recommend vendors — integrating a vendor scoring and recommendation layer would transform vendor selection from a Rolodex lookup into a data-driven decision.
**Tags:** #gradient-boosting #data-integration #automation #quick-win

## The Problem
An AppFolio user creating a work order sees a dropdown list of vendors sorted alphabetically or by trade. They select a vendor based on memory ("John handles plumbing well") or habit (always sending the same vendor regardless of location or workload). AppFolio has the data to make better vendor recommendations — it stores every historical work order, including which vendor was assigned, completion time, invoice amount, and whether a callback was required — but this data is stored as historical records, not as vendor performance intelligence.

## What Already Exists
AppFolio stores: vendor profiles (trade, contact info, insurance), work order history (every job assigned, completion status, invoice), and property locations (geocoded addresses). The data needed for vendor scoring exists. What's missing is the analytical layer that transforms this data into actionable vendor recommendations.

## The Customization Gap
A vendor intelligence module that: (1) calculates vendor performance scores from historical work order data — average completion time, callback rate (how often the same issue requires a second visit), average cost per job type, tenant satisfaction (from follow-up surveys if collected); (2) recommends vendors per work order based on trade match, proximity to the property, current availability (self-reported or inferred from recent workload), performance score, and pricing relative to other vendors for the same job type; (3) flags vendor performance trends — "Plumber A's callback rate has increased from 5% to 15% over the last 3 months" or "HVAC vendor B's average invoice has increased 20% without corresponding scope changes"; and (4) benchmarks vendor pricing against market rates for common maintenance tasks, identifying vendors charging significantly above market.

## Target Customer
AppFolio users managing 200+ units with 5+ active vendors, currently selecting vendors by memory or habit. AppFolio seeking to differentiate through AI-powered operations features.

## Impact If Solved
Reduces vendor selection time from 3-5 minutes to 15 seconds through data-driven recommendation. Improves maintenance quality by routing work orders to higher-performing vendors. Reduces maintenance costs by 5-15% through price-aware vendor matching and identification of overcharging vendors. Creates a competitive moat for AppFolio through vendor intelligence that requires historical work order data competitors don't have.
