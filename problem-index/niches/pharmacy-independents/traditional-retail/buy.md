# PioneerRx Analytics Module with Per-NDC Margin Visibility

**Niche:** [[niches/pharmacy-independents/traditional-retail/profile|Traditional Retail Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** PioneerRx shows adjudicated reimbursement but not true per-NDC margin after acquisition cost, dispensing fees, and estimated DIR impact — the analytics layer exists generically but needs pharmacy-specific financial logic layered on top.
**Tags:** #data-integration #feature-engineering #revenue-impact #quick-win

## The Problem
PioneerRx, QS/1, and Liberty Software all display the adjudicated price when a claim is processed, but none of them show the pharmacist true margin per prescription accounting for actual acquisition cost (which varies by wholesaler contract, GPO membership, and purchase timing), dispensing labor cost, and estimated DIR fee impact. The owner-pharmacist sees "$12.50 reimbursed" but doesn't know if the drug cost $8.00 or $11.50 from their wholesaler last week. Margin visibility requires merging PMS adjudication data with wholesaler invoice data and DIR projections — a data integration problem that no PMS vendor has prioritized because their revenue comes from subscription fees, not pharmacy profitability.

## What Already Exists
PioneerRx has a reporting module that generates standard reports: prescription volume by day, top dispensed drugs, payer mix breakdown. Third-party analytics tools like Datarithm and PharmaRite offer inventory-focused analytics (turns, deadstock, reorder optimization) but don't address per-prescription profitability. PSAO dashboards (e.g., from Innovatix or ProCare) show aggregate DIR assessments but not per-NDC attribution. The data exists across these systems but nobody merges it into a single per-prescription P&L view.

## The Customization Gap
The gap is a financial integration layer that pulls wholesaler invoice pricing (from McKesson, Cardinal Health, or AmerisourceBergen EDI files), matches it to each dispensed NDC in the PMS, overlays the adjudicated reimbursement, subtracts estimated dispensing cost ($2-4 per Rx in labor), and applies a DIR fee estimate based on current quality metric trajectory. This produces a true per-prescription margin that the pharmacist can sort, filter, and trend. The system needs to handle the complexity of pharmacy-specific pricing: the same NDC costs different amounts depending on whether it was purchased through the primary wholesaler, a secondary source, or a GPO deal. A curated analytics module built as a PioneerRx plugin or standalone connector — priced at $199-299/month — fills this gap without requiring a PMS switch.

## Target Customer
Independent pharmacy owners using PioneerRx, QS/1, or Liberty Software who suspect they are losing money on certain prescriptions but cannot identify which ones without manually cross-referencing wholesaler invoices and PBM remittances.

## Impact If Solved
Gives pharmacy owners per-prescription profitability visibility for the first time, enabling decisions like declining to stock chronically unprofitable NDCs, negotiating with alternative wholesalers for specific drugs, or steering patients toward therapeutically equivalent generics with better margin. Pharmacies using basic margin analysis tools report identifying $15,000-30,000/year in margin leakage within the first 90 days.
