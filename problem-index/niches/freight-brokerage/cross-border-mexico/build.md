# Three-Leg Cross-Border Shipment Orchestration Platform

**Niche:** [[niches/freight-brokerage/cross-border-mexico/profile|Cross-Border Mexico Freight Brokerages]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No single platform orchestrates the full US-Mexico cross-border freight workflow — US domestic haul, border drayage, customs clearance, and Mexico domestic delivery — in one system, forcing brokers to coordinate three separate legs through phone calls, emails, and spreadsheets.
**Tags:** #workflow-orchestration #automation #data-integration #compliance

## The Problem
A northbound shipment from Monterrey to Chicago requires: (1) a Mexican carrier to haul from the shipper to the Laredo border transfer yard; (2) a drayage carrier to cross the load through the Laredo POE with customs clearance on both sides; (3) a US carrier to haul from Laredo to Chicago. Each leg has its own carrier, its own rate, its own scheduling, and its own documentation. The broker coordinates all three legs plus customs on both sides — typically through 15-20 phone calls and emails per shipment. A single delay on one leg cascades: if the Mexico carrier is late to the border, the drayage misses its customs appointment, the US carrier sits idle, and the Chicago delivery is missed.

## Why Nobody Has Built This
The three-leg workflow spans two countries with different technology ecosystems. US TMS platforms (McLeod, Mercury Gate) don't integrate with Mexican carrier dispatch or Mexican customs (SAT). Mexican logistics platforms don't integrate with US TMS or CBP. Building a unified platform requires bilingual development, dual-country customs API integration (ACE for US, VUCEM for Mexico), and carrier network coverage on both sides of the border — a multi-market challenge that software vendors avoid.

## What to Build
A cross-border shipment orchestration platform that: (1) manages all three legs in a single workflow with milestone tracking (pickup → border arrival → customs clearance → border crossing → US pickup → delivery); (2) integrates with ACE (US) and VUCEM (Mexico) for customs document submission; (3) alerts the broker when any leg is delayed and recommends contingency actions; (4) provides a bilingual interface for coordination with Mexican carriers and customs agents.

## Target Customer
Cross-border operations managers at US-Mexico freight brokerages handling 50+ cross-border shipments per week. Approximately 500-800 brokerages specialize in US-Mexico freight. Average contract value: $24-48K/year.

## Impact If Built
Reducing per-shipment coordination from 15-20 touchpoints to 5-7 (automated milestones + exception alerts) saves 2-3 hours of broker time per shipment. On 50 weekly shipments, this recovers 100-150 hours of broker capacity per week — equivalent to 3-4 FTE.
