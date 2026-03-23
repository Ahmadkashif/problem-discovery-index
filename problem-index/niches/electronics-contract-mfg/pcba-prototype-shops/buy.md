# Prototype-Specific Order Management System

**Niche:** [[niches/electronics-contract-mfg/pcba-prototype-shops/profile|PCBA Prototype & Quick-Turn Shops]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic MES and ERP systems model repeating production work orders, but a prototype shop processes 20-50 unique, one-time jobs per week where each job is a different board design — and no commercial system handles the unique-job-per-order workflow without creating excessive overhead per job.
**Tags:** #workflow-orchestration #automation #quick-win

## The Problem
Each prototype order is a unique job: unique BOM, unique Gerber, unique assembly requirements. A prototype shop running 20-50 such jobs per week would need to create 20-50 unique work orders, BOMs, and routings in a traditional MES — overhead that exceeds the value of tracking for a 5-board prototype run. Most prototype shops therefore track orders via email threads, whiteboard scheduling, and informal verbal handoffs between stations. This works until the shop reaches 30+ simultaneous orders, at which point jobs get lost, components get mixed between orders, and promised ship dates are missed.

## What Already Exists
MES platforms (Aegis, Cogiscan) handle production tracking for repeat-production EMS. Project management tools (Monday.com, Asana) handle task tracking. CRM tools handle customer communication. None integrate the prototype-specific workflow: receive files → DFM review → procure components → kit components → assemble → test → ship, where each step has a different turnaround time expectation based on the order's priority tier.

## The Customization Gap
A prototype order management system must handle: rapid job creation from uploaded Gerber/BOM files (not manual BOM entry), component procurement tracking integrated with distributor order APIs, station-level tracking with priority-based sequencing (expedite orders jump the queue), automated customer status notifications at each stage, and consolidated end-of-day shipping manifests. The data model is one-job-per-order rather than one-product-many-orders, requiring a fundamentally different workflow than production MES.

## Target Customer
Owners and production managers at prototype shops processing 15+ orders per week. Approximately 300-500 US prototype shops.

## Impact If Solved
Order visibility goes from "ask someone" to real-time dashboard. Missed ship dates decrease by 40-60%. Customer satisfaction improves with automated status updates, reducing the 5-10 "where's my order?" calls per day that the owner currently fields personally.
