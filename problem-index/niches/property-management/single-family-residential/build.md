# Scattered-Site Maintenance Route Optimizer

**Niche:** [[niches/property-management/single-family-residential/profile|Single-Family Residential]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A routing and scheduling optimizer that takes the week's maintenance work orders across hundreds of scattered properties, groups them by geography and trade, assigns vendors by proximity and availability, and produces optimized daily routes — reducing the 30-40% of vendor time spent driving between properties that currently makes SFR maintenance 2-3x more expensive per unit than multifamily.
**Tags:** #reinforcement-learning #workflow-orchestration #automation #revenue-impact #gradient-boosting

## The Problem
SFR maintenance is expensive because properties are scattered: a plumber dispatched to fix a leaky faucet at 123 Oak Street drives 25 minutes, spends 30 minutes on the repair, drives 35 minutes to the next property at 456 Elm Avenue for a toilet replacement, and repeats. This vendor spends 40-50% of their billable day driving, and the property management company pays for travel time (either directly through hourly rates or indirectly through higher per-job pricing). A PM company managing 500 scattered homes generates 200-400 maintenance work orders per month across 5-10 trade categories (plumbing, electrical, HVAC, general handyman, appliance, locksmith, landscaping). Currently, the maintenance coordinator assigns vendors to work orders individually, without optimizing for geographic clustering. The same plumber visits properties 20 miles apart while another plumber is available 2 miles from the first property.

## Why Nobody Has Built This
The optimization requires solving a multi-vendor vehicle routing problem with time windows, skill matching, and tenant coordination constraints. Standard route optimization (used by delivery companies) assumes fungible drivers and fixed delivery windows. SFR maintenance adds complexity: work orders require specific trades (can't send a plumber for electrical work), tenants have availability windows, job durations are variable and uncertain, and work orders arrive continuously throughout the week (the route must be re-optimized daily as new requests arrive). The market (SFR PM companies) is fragmented — most manage 100-500 properties and can't individually justify enterprise route optimization software.

## What to Build
A maintenance scheduling and routing platform that: (1) ingests work orders from AppFolio or Propertyware via API, with property address, trade required, priority level, tenant availability, and estimated job duration; (2) groups work orders by geography and trade, identifying geographic clusters where multiple jobs of the same trade can be completed in a single vendor visit (3 plumbing jobs within 2 miles = one plumber visit instead of three separate dispatches); (3) assigns vendors based on trade certification, geographic proximity to the cluster, availability, and price/rating; (4) produces optimized daily vendor routes with turn-by-turn directions and appointment confirmations sent to both the vendor and the tenant; and (5) re-optimizes daily as new work orders arrive, emergency requests override existing schedules, and completed jobs free up vendor capacity.

## Target Customer
SFR property management companies managing 200+ scattered-site properties across a metro area, currently spending $50K-200K annually on maintenance vendor costs with 30-40% attributable to travel time.

## Impact If Built
Reduces maintenance vendor travel time by 30-50% through geographic clustering and route optimization. Saves $15K-60K annually per PM company in reduced vendor costs. Decreases average maintenance response time by 20-30% by matching work orders to the nearest available qualified vendor. Could be priced at $3-5 per managed unit per month.
