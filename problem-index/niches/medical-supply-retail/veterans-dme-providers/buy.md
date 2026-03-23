# VA-to-Commercial Code Translation and Pricing Reconciliation

**Niche:** [[niches/medical-supply-retail/veterans-dme-providers/profile|Veterans DME Providers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** DME billing systems use HCPCS codes for commercial insurance, but VA orders use Federal Supply Schedule item numbers and VA-specific product codes — requiring manual translation for every order that no billing system handles natively.
**Tags:** #automation #data-integration #compliance #quick-win

## The Problem
When a VA prosthetics department orders a wheelchair, they reference VA product codes and Federal Supply Schedule (FSS) contract numbers. The DME supplier must translate these into HCPCS codes for their internal inventory and billing system, apply the VA-negotiated pricing (which differs from Medicare rates), and track the order in both their system and the VA's eCMS portal. This translation step is manual for every order: the billing specialist looks up the VA product code, finds the corresponding HCPCS code, verifies the FSS contract price, and enters the order in both systems. With 50-100 VA orders per month, this dual-entry and translation consumes 20-30 hours/month.

## What Already Exists
Brightree and other DME billing systems handle HCPCS-based commercial and Medicare billing. VA's eCMS portal handles VA-side order management. Federal Supply Schedule pricing is published but in formats not integrated with DME software.

## The Customization Gap
The missing capability is an automated code translation and pricing lookup layer: given a VA order with VA product codes, automatically map to the corresponding HCPCS codes, apply the FSS contract pricing, and sync the order between the DME billing system and the VA's eCMS. This eliminates dual data entry and prevents pricing errors (applying Medicare rates instead of VA rates, or vice versa — a compliance violation that can trigger contract penalties). The mapping table must be maintained as both HCPCS and VA codes are updated quarterly.

## Target Customer
DME billing specialists at VA-contracted suppliers who spend 20-30 hours/month on manual code translation and dual-system data entry for VA orders.

## Impact If Solved
Saves 15-25 hours/month of billing specialist time on code translation and dual entry. Eliminates pricing errors that average $50-200 per incorrect order and trigger VA audit flags. Reduces order processing time from 20-30 minutes per VA order to 5-10 minutes, enabling faster delivery and improved VA contract performance metrics.
