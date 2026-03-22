# Refrigerant Tracking Compliance Gaps

**Niche:** [[niches/hvac-contractors/residential-service-repair/profile|Residential Service & Repair]]
**Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** EPA Section 608 requires tracking every pound of refrigerant from purchase to recovery, but residential HVAC shops track it on paper logs and partial spreadsheets — leaving them one audit away from fines of $44,539 per day per violation.
**Tags:** #automation #compliance #data-integration #worker-facing

## The Problem
Every residential HVAC service company handles refrigerants (R-410A, R-22, R-32, R-454B) daily, and EPA Section 608 requires complete chain-of-custody documentation: purchase records, cylinder tracking, pounds added to each system, pounds recovered, and proper disposal of recovered refrigerant. The AIM Act (2020) added HFC phase-down requirements that further tighten reporting obligations. In practice, technicians scribble refrigerant amounts on invoices ("added 2 lbs R-410A") but rarely record cylinder serial numbers, recovery amounts, or running totals. The office manager may maintain a spreadsheet of refrigerant purchases, but it doesn't reconcile with field usage. When the purchased pounds don't match the sum of added-to-systems plus recovered plus remaining-in-stock, there's a compliance gap. Most shops don't discover the gap until an EPA audit — at which point they face fines, mandatory reporting, and potential loss of EPA 608 certification for the entire company.

## Why It's Still Broken
Technicians are in attics and on rooftops in extreme temperatures with a goal of fixing the problem and moving to the next call. Recording cylinder serial numbers, recovery amounts, and detailed refrigerant data is friction that slows them down with no immediate benefit to the repair. ServiceTitan captures refrigerant as a pricebook line item ("R-410A per pound") for billing purposes, but doesn't track the compliance side: which cylinder the refrigerant came from, how much is left in that cylinder, or recovery amounts. The compliance data and the billing data live in separate systems (or more commonly, one is paper and one is digital), and nobody reconciles them until audit pressure forces it.

## What a Fix Looks Like
A refrigerant tracking module — either standalone or integrated with ServiceTitan via API — that captures the full chain: (1) Purchase entry with supplier, cylinder serial number, type, and weight; (2) Field usage logging where the technician scans a QR code on the cylinder, enters pounds added/recovered, and the system auto-deducts from cylinder inventory; (3) Recovery tracking with destination cylinder and eventual disposal documentation; (4) Dashboard showing real-time reconciliation of purchased vs. used vs. recovered vs. in-stock, flagging discrepancies before they become compliance violations. The technician interaction is: scan cylinder, enter pounds, confirm on tablet — 30 seconds per transaction, integrated into the existing service call workflow.

## Who Feels the Pain
Company owners who know their refrigerant tracking is inadequate but don't know how to fix it without adding 10 minutes of paperwork per service call, office managers spending hours monthly trying to reconcile purchase receipts with field invoices, and technicians who risk personal EPA certification violations because the company doesn't have a tracking system.

## Impact If Fixed
Eliminates EPA 608 compliance risk worth $44,539 per day in potential fines. Reduces office reconciliation time from 4-8 hours monthly to near-zero through automated tracking. Identifies refrigerant waste and theft — shops typically discover 10-15% of purchased refrigerant is unaccounted for once they implement tracking.
