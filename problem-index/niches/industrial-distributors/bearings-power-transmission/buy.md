# CMMS Asset Records Linked to the Distributor's Catalogue

**Niche:** [[niches/industrial-distributors/bearings-power-transmission/profile|Bearings & Power Transmission Distribution]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Plants already keep asset and spare-parts lists in a maintenance system; the part numbers in it rarely resolve to anything the distributor can ship.
**Tags:** #large-language-models #k-nearest-neighbors #transformers #data-integration #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep the plant's rotating equipment turning, but that splits into two contests with different winners: putting the exact replacement on the machine inside the downtime window, and calling the failure before it stops the line. Decomposed into contested sub-niches below.

## The Problem
A maintenance planner's CMMS lists spare parts against assets with internal codes, OEM part numbers from the machine builder and free-text descriptions entered over decades. When a work order calls for a part, the planner still emails or calls the distributor, who identifies it again.

## What Already Exists
CMMS and enterprise asset management systems (IBM Maximo, SAP Plant Maintenance, Fiix, UpKeep and others) hold assets, work orders and spare-parts lists, and connect to e-procurement for ordering.

## The Customization Gap
The CMMS needs a distributor-side resolver: each spare-part record mapped to the distributor's SKU and approved interchanges, with OEM numbers translated to the underlying standard component (a machine builder's part number is often a stock bearing with a mark-up). It also needs stock and lead time shown inside the work order, and corrections from the counter written back. Generic CMMS integrations pass orders; they don't resolve identity.

## Target Customer
BPT distributors serving plants that run a maintained CMMS, and the plants' maintenance planners.

## Impact If Solved
If ~50% of CMMS spare-part records resolve to a distributor SKU (estimate), planners order ~2–4 times a week from the work order without a call, OEM mark-ups of ~20–50% on standard components become visible (estimate), and the distributor becomes the default source for every resolved part.
