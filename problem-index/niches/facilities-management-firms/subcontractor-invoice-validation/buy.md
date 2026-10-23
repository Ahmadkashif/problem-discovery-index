# Three-Way Match Rebuilt for Not-to-Exceed Work Orders

**Niche:** [[niches/facilities-management-firms/subcontractor-invoice-validation/profile|Subcontractor Invoice Validation & Pass-Through Billing]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** AP automation matches invoices to purchase orders and receipts; a facilities job has a ceiling, a rate card and a work order instead.
**Tags:** #large-language-models #transformers #data-integration #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to validate every subcontractor invoice against its work order, rate card and not-to-exceed before it is rebilled to the client, and whoever catches the overbilling before the client's audit does takes the account.

## The Problem
Providers run AP suites built for purchase-order businesses. Facilities invoices fail their matching rules or are forced through them with blanket POs, and the real validation happens by hand outside the system.

## What Already Exists
AP automation and procure-to-pay suites (Coupa, SAP Ariba, OCR capture and three-way matching), which match invoice lines to PO lines and goods receipts and route exceptions.

## The Customization Gap
Facilities matching needs: the work order as the "PO," with an NTE ceiling rather than line prices; the completion record as the "receipt"; rate cards by subcontractor, trade, region and hour band as the price reference; warranty and service-contract registers by asset; per-client rebilling rules (markup, approval thresholds, excluded categories); and an exception workflow that sends a correction request to the subcontractor rather than an internal approver.

## Target Customer
IFM provider finance and AP teams already licensing a procure-to-pay suite.

## Impact If Solved
Facilities invoices flow through the AP system the provider already owns, with exceptions that mean something.
