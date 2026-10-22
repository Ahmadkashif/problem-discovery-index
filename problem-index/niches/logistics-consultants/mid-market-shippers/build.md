# Shipment History Rebuilt From Freight Invoices

**Niche:** [[niches/logistics-consultants/mid-market-shippers/profile|Mid-Market Shippers Without Logistics Engineers]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mid-market shipper's freight history exists only as carrier invoices and ERP order lines that share no key, and every consultant rebuilds the shipment table from them by hand.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #feature-engineering #evaluation-metrics #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to reconstruct shipment-level history for a client with no TMS — freight invoices in PDFs, carrier portals, ERP order lines — and whoever can do it in days rather than weeks can deliver a study at a fee a mid-market CFO will approve.

## The Problem
The consultant asks for twelve months of shipments and receives a folder: parcel invoices from two carriers as PDFs and CSVs, LTL invoices from five carriers in five layouts, broker invoices for truckload, a carrier portal export covering four months, and an ERP sales order file keyed on order number. Invoices carry pro numbers, weights, consignee names and charges; orders carry customer numbers, items and quantities. The analyst spends weeks keying, matching and allocating before any analysis starts — on a study the client expects to cost ~$25K–$80K (estimate).

## Why Nobody Has Built This
Freight audit firms build shipment tables from invoices, but as a continuous service sold on payment processing, not as a one-off historical reconstruction. Network design vendors sell to enterprises that already have a TMS. The mid-market study is too small for either to design for.

## What to Build
An ingestion service that extracts line-level data from any carrier invoice format, normalises charges into linehaul, fuel and accessorial buckets, resolves consignee names into ship-to locations, and joins each shipment to ERP orders by date, destination and weight, with a confidence score per match. Output is the shipment table a network or procurement model needs, plus a coverage report showing what share of freight spend reconciled to orders.

## Target Customer
Solo and boutique logistics consultants serving mid-market manufacturers and distributors, and the regional accounting and advisory firms that resell their studies.

## Impact If Built
Weeks of reconstruction fall to days (estimate), which is the difference between a study a mid-market CFO approves and one the consultant cannot price profitably.
