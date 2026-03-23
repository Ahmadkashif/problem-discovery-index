# PCBA Prototype & Quick-Turn Shops

**Parent Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Category:** Low Digitized

## Profile
**Market Size:** $3-5B
**Share of Parent Industry:** ~5%
**Digital Adoption:** Low-Medium — many run on spreadsheets, email-based order management, and manual quotation processes with no MES
**Target Buyer:** Owner or Production Manager at prototype shops (5-50 employees)
**Automation Potential:** Medium — quoting, DFM review, and order tracking are the primary automation targets

## What Makes This a Distinct Niche
PCBA prototype shops specialize in quick-turn assembly (24-72 hour turnaround) of 1-50 board quantities for hardware startups, R&D departments, and design engineers validating new designs. The business model is speed and flexibility, not cost efficiency — customers pay 5-10x per-board premium for rapid turnaround. The operational challenge is managing 20-50 simultaneous quick-turn orders, each with a unique BOM, unique board layout, and urgent timeline. Quoting is the revenue bottleneck: each inquiry requires BOM review, component availability check, assembly time estimation, and price calculation — a 30-60 minute process that the owner or lead estimator performs personally. Unlike production EMS, prototype shops rarely run the same board twice, so process optimization has minimal value — speed of setup and first-pass success are everything.

## Current Tools & Gaps
Most prototype shops run on QuickBooks for invoicing, email for order management, spreadsheets for quoting, and manually configured SMT machines. A few use MacroFab or Tempo Automation's digital front end for online ordering. No platform provides automated DFM review specific to the shop's equipment capabilities (will this BGA pitch work on our printer/placer?), BOM component availability integration with real-time pricing, or prototype-specific production tracking (where each board is a unique job, not a repeating work order).

## Problems
- [[niches/electronics-contract-mfg/pcba-prototype-shops/build|🔨 Build: Instant DFM + Quotation Engine for Prototype PCBA]]
- [[niches/electronics-contract-mfg/pcba-prototype-shops/buy|🛒 Buy: Prototype-Specific Order Management System]]
- [[niches/electronics-contract-mfg/pcba-prototype-shops/fix|🔧 Fix: BOM Component Sourcing Bottleneck]]
