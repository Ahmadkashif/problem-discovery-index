# Freight Class Misclassification Catch

**Niche:** [[niches/freight-brokerage/ltl-consolidation/profile|LTL Consolidation Brokerages]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Fix (Pain Point)
**One-liner:** Freight class errors — shippers declaring Class 70 when the product is actually Class 100 — trigger carrier reclassification charges and invoice disputes that consume 3-5 hours of billing staff time per week and erode 2-4% of LTL margin.
**Tags:** #bert #large-language-models #compliance #automation #quick-win

## The Problem
NMFC (National Motor Freight Classification) assigns freight classes (50-500) based on density, handling, stowability, and liability. Shippers frequently misclassify their products — often unintentionally, sometimes to get a lower base rate. When the carrier inspects the shipment and determines the actual class is higher, they apply a reclassification charge and re-rate the shipment at the higher class tariff. The broker is stuck between the shipper (who expected the original rate) and the carrier (who billed at the correct class). Resolving each reclassification dispute takes 30-60 minutes of back-and-forth documentation.

## Why It's Still Broken
NMFC classification requires matching the product description to the NMFC tariff — a 7,000+ item lookup that shippers rarely consult. Many shippers use the same freight class for all shipments regardless of product variation. Carrier rate APIs accept whatever class the shipper declares without validation. No tool validates the declared freight class against the product description at booking time, before the shipment moves.

## What a Fix Looks Like
A booking-time validation that: (1) takes the shipper's product description and declared freight class; (2) matches the description against NMFC commodity classifications using text similarity; (3) flags mismatches where the declared class doesn't align with the likely correct class; (4) alerts the broker before booking so they can confirm the correct class with the shipper and quote accurately. This prevents reclassification charges rather than resolving them after the fact.

## Who Feels the Pain
LTL billing coordinators who spend 3-5 hours per week resolving reclassification disputes, and brokers who absorb the margin hit when reclassification charges can't be recovered from the shipper.

## Impact If Fixed
Preventing 80% of freight class misclassifications on a desk handling 200 LTL shipments/week (where 8-10% get reclassified) eliminates 12-16 dispute resolutions per week, recovering 6-8 hours of billing staff time and 2-4% of LTL margin.
