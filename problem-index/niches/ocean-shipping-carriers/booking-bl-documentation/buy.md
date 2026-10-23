# Document Extraction Adapted to the DCSA eBL Schema

**Niche:** [[niches/ocean-shipping-carriers/booking-bl-documentation/profile|Booking, Shipping Instruction & B/L Documentation]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Intelligent document processing platforms extract invoices and forms well; a bill of lading needs carrier, cargo and destination logic layered on top.
**Tags:** #transformers #large-language-models #evaluation-metrics #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn shipping instructions into a correct bill of lading before the SI cut-off, and whoever issues the highest share of bills of lading with no post-issue amendment takes the account.

## The Problem
Carriers that buy a general extraction platform get fields out of SIs but still need agents to reconcile, validate and correct them.

## What Already Exists
Cloud document AI services and IDP vendors (ABBYY, Rossum, Hyperscience) with configurable extraction and human-in-the-loop review.

## The Customization Gap
Mapping to the DCSA booking and eBL data model; reconciliation with the booking's equipment, routing and cut-offs; dangerous-goods, reefer and out-of-gauge checks; manifest rules for US and EU filings; party matching against the carrier's customer master; and learning from each shipper's past amendments. The issued B/L gives a free label for every SI, which generic platforms do not exploit.

## Target Customer
Carriers already licensing an IDP platform for finance documents.

## Impact If Solved
Straight-through processing on ~50–70% of clean SIs (estimate) cuts keying time per bill from ~10–15 minutes to ~2 (estimate), without a separate maritime-specific vendor.
