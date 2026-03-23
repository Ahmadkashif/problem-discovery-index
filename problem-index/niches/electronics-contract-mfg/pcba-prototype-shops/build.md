# Instant DFM + Quotation Engine for Prototype PCBA

**Niche:** [[niches/electronics-contract-mfg/pcba-prototype-shops/profile|PCBA Prototype & Quick-Turn Shops]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product takes a customer's Gerber files and BOM, automatically performs DFM review against the specific prototype shop's equipment capabilities, checks component availability in real time, and generates a binding quote — all within minutes instead of the current 30-60 minute manual process.
**Tags:** #automation #revenue-impact #quick-win

## The Problem
A prototype shop receives 10-30 RFQs per day. Each requires the owner or lead estimator to: (1) review Gerber files for manufacturability (minimum trace/space, via sizes, pad geometries compatible with the shop's stencil printer, pick-and-place, and reflow oven), (2) review the BOM for component availability and pricing (checking Digi-Key, Mouser, Arrow in real time), (3) estimate assembly time based on component count, package complexity, and any manual assembly requirements, and (4) calculate a price. This process takes 30-60 minutes per quote, and the shop quotes 30-50% of inquiries (the rest are screened out as too complex or too large). The quoting bottleneck limits the shop's ability to capture revenue — inquiries that arrive at 4 PM may not be quoted until the next morning, by which time the customer has ordered from a competitor.

## Why Nobody Has Built This
Each prototype shop has different equipment capabilities (minimum component size, BGA capability, double-sided assembly, fine-pitch capability), different pricing models, and different lead time commitments. A generic quotation engine cannot account for shop-specific constraints without configuration. Additionally, DFM review requires parsing Gerber files and cross-referencing pad geometries against equipment specifications — a technical integration that few software companies have undertaken for the prototype market (MacroFab and Tempo Automation built this internally but do not sell it as a tool to other shops).

## What to Build
A web-based quotation platform that accepts Gerber files and BOM upload, performs automated DFM review against the shop's configured equipment capabilities, checks component availability and pricing via distributor APIs (Digi-Key, Mouser, Arrow, Octopart), estimates assembly time from component count and complexity, and generates an instant quote. The shop configures its equipment capabilities, pricing rules, and lead time tiers during onboarding. Customers receive a quote in minutes with DFM feedback, rather than waiting hours or days.

## Target Customer
Owners and production managers at prototype/quick-turn PCBA shops processing 10+ quotes per day. Approximately 500-700 US prototype shops. Average contract value: $15-30K/year.

## Impact If Built
Quote turnaround drops from 30-60 minutes to under 5 minutes. Quote volume capacity doubles without adding staff. Revenue capture rate improves by 15-25% by quoting inquiries that currently expire before the shop responds.
