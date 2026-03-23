# BOM Component Sourcing Bottleneck

**Niche:** [[niches/electronics-contract-mfg/pcba-prototype-shops/profile|PCBA Prototype & Quick-Turn Shops]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** Component sourcing for prototype orders — checking availability, finding alternatives for out-of-stock parts, and placing orders across 3-5 distributors per BOM — consumes 30-45 minutes per order and is the single largest delay in the quick-turn workflow.
**Tags:** #automation #data-integration #revenue-impact

## The Problem
A typical prototype BOM has 50-300 unique component line items. For each line item, the procurement person must check availability at Digi-Key, Mouser, Arrow, and potentially Newark and Avnet — verifying that the exact MPN is in stock in the required quantity, checking lead times for out-of-stock parts, and identifying acceptable alternatives (same package, same specifications, different manufacturer) for unavailable components. For a 200-line BOM, this process takes 30-45 minutes even for an experienced buyer. When 10-20% of components are unavailable (common during supply chain disruptions), each unavailable component requires a customer consultation to approve an alternative — adding hours or days to the order cycle.

## Why It's Still Broken
Distributor APIs exist (Octopart aggregates across distributors, Digi-Key and Mouser have direct APIs), but no tool integrates BOM-level availability checking with alternative part identification and customer approval workflow. The alternative part decision requires engineering judgment — is a different manufacturer's 100nF 0402 capacitor acceptable? Usually yes for a prototype. Is a different op-amp with similar specifications acceptable? Depends on the circuit. This engineering judgment is currently performed by the shop owner or lead engineer, one component at a time.

## What a Fix Looks Like
A BOM procurement tool that: (1) takes the full BOM, checks availability across all major distributors simultaneously via API, (2) flags unavailable components with ranked alternatives (same specifications, different manufacturer — scored by specification match percentage), (3) sends the customer a structured approval request for alternatives ("these 8 components are unavailable — here are recommended alternatives with spec comparison"), (4) once approved, places orders across distributors to minimize shipping cost and delivery time, and (5) tracks delivery of all components against the order's required-by date.

## Who Feels the Pain
Procurement staff (often the owner wearing another hat) who spend 4-6 hours per day on component sourcing. Customers who wait 1-3 extra days for their prototype because a single component was out of stock. Assembly technicians who wait idle while components trickle in.

## Impact If Fixed
Component sourcing time drops from 30-45 minutes to 5-10 minutes per BOM. Order-to-assembly time decreases by 0.5-1 day on average. The shop can process 30-50% more orders per day without additional procurement staff.
