# Multi-Distributor Order Fragmentation

**Niche:** [[niches/electronics-contract-mfg/bom-procurement-operations/profile|BOM Procurement & Supply Chain Operations]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** A single production BOM requires purchasing components from 3-5 different distributors because no single distributor stocks the full BOM — creating 3-5 POs, 3-5 shipments, 3-5 receiving events, and 3-5 invoice reconciliations per BOM per production run.
**Tags:** #automation #workflow-orchestration #revenue-impact

## The Problem
A 500-line BOM might require ordering from Digi-Key (300 lines in stock), Mouser (100 lines), Arrow (50 lines), and a specialty distributor (50 lines). Each distributor requires a separate PO, ships separately, and invoices separately. The procurement team creates and manages 3-5 POs per production order. Receiving must check in 3-5 shipments and verify that all 500 lines are received before kitting can begin. If one distributor's shipment is delayed or short, production of the entire order is held. Invoice reconciliation across 3-5 invoices per order, multiplied by 20-50 production orders per month, consumes significant accounts payable time. The fragmentation is inherent — no single distributor carries everything — but the administrative overhead is multiplied by the number of distributors.

## Why It's Still Broken
ERP systems manage POs per distributor, but optimizing the split — which components to buy from which distributor to minimize total cost (unit price + shipping + minimum order quantity surplus) while ensuring all components arrive by the production date — is done manually by the procurement analyst. The optimization involves trade-offs: Digi-Key may have a component $0.02 cheaper but Mouser has it in stock for same-day ship, and ordering from Mouser consolidates the shipment with 50 other lines already being ordered there. This optimization is too complex for manual analysis across 500 lines and 4-5 distributors.

## What a Fix Looks Like
An order optimization engine that takes the full BOM with required quantities and production date, queries availability and pricing across all authorized distributors, optimizes the distributor allocation to minimize total procurement cost (unit price + shipping + surplus from MOQ) while meeting the production date, generates POs for each distributor with consolidated ordering, and tracks delivery status across all distributors against the kit-complete deadline. Alerts when a distributor is at risk of late delivery, with automatic re-sourcing recommendations.

## Who Feels the Pain
Procurement analysts managing 3-5 POs per production order across 20-50 orders per month. Receiving staff checking in fragmented shipments. Kit builders who cannot start kitting until the last distributor ships. Accounts payable reconciling 60-250 invoices per month from distributor orders alone.

## Impact If Fixed
Procurement administrative time decreases by 30-40%. Total component cost decreases by 2-5% through optimized distributor allocation. Kit-complete reliability improves by 15-25% through proactive delivery tracking and re-sourcing. Accounts payable workload for distributor invoices decreases by 40-50%.
