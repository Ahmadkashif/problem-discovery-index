# LTL Accessorial Cost Predictor

**Niche:** [[niches/freight-brokerage/ltl-consolidation/profile|LTL Consolidation Brokerages]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** LTL carrier rate APIs return base rates but don't predict which accessorial charges (liftgate, inside delivery, reweigh, reclassification) will actually be applied on delivery — charges that routinely add 15-30% to the quoted rate and surprise the shipper.
**Tags:** #gradient-boosting #tacit-knowledge-ml #revenue-impact #data-integration

## The Problem
LTL shipments frequently incur accessorial charges that weren't in the original quote: liftgate delivery ($75-150), inside delivery ($100-200), limited access delivery ($100-250), reweigh charges when actual weight exceeds billed weight, and reclassification charges when the carrier disputes the freight class. These charges appear on the carrier invoice 2-4 weeks after delivery, creating margin erosion and shipper disputes. Experienced LTL brokers anticipate which shipments will incur accessorials based on the delivery address type and commodity, but this judgment isn't embedded in quoting tools.

## What Already Exists
SMC3 and Banyan Technology provide LTL rate comparison with optional accessorial add-ons that the broker can manually select. Carrier Connect provides carrier-specific accessorial rate schedules. No tool predicts which accessorials will actually be charged based on delivery address and shipment characteristics.

## The Customization Gap
An accessorial prediction tool needs: (1) historical accessorial charge data by delivery address and shipment type from the broker's own carrier invoices; (2) delivery address classification (commercial dock vs. commercial no-dock vs. residential vs. limited access location) from geocoding and prior delivery experience; (3) predicted accessorial charges at quoting time, added to the base rate for accurate all-in pricing to the shipper. The broker's own historical accessorial data is the training signal no external tool has.

## Target Customer
LTL pricing analysts and desk managers at brokerages where accessorial invoice surprises are a recurring source of margin erosion and shipper complaints.

## Impact If Solved
Eliminating accessorial margin surprises on a $5M LTL book where 25% of shipments incur unquoted accessorials averaging $150 each recovers $187K in annual margin leakage. Shipper satisfaction improves when quoted rates match invoiced rates.
