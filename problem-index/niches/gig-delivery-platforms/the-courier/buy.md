# Buy: Mileage and Expense Tools Adapted to Multi-App Gig Work

**Niche:** [[niches/gig-delivery-platforms/the-courier/profile|The Courier]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mileage and expense apps were built for a salesperson claiming a deduction; a courier needs the same trace attributed to deliveries, platforms and zones so it can guide decisions rather than file a return.
**Tags:** #descriptive-statistics #gradient-boosting #data-integration #evaluation-metrics #confidence-intervals #feature-engineering #worker-facing #automation
**Contested on:** Whether deduction-oriented mileage tracking can be turned into trip-level economics without rebuilding the capture layer.

## The Problem

Mileage and expense tracking is a solved consumer category. Automatic drive detection, classification into business and personal, IRS-compliant logs, expense capture and tax export are all available in polished apps that couriers already use in large numbers.

They are built for a deduction. The output is a total annual mileage figure and a compliant log. What a courier needs is the same underlying trace attributed to individual deliveries, platforms and zones, joined to earnings, so that it answers where their time is worth the most rather than what they can deduct. The capture is 80% of the way there and the attribution — the part that makes it a decision tool — is entirely absent.

## What Already Exists

Everlance, Stride, MileIQ, Hurdlr and the mileage-tracking category, several with gig-specific positioning. Automatic drive detection with reasonable battery behaviour. Expense categorisation. Quarterly tax estimation. Some earnings import from the major platforms via receipt parsing. Gridwise and Solo attempt the multi-app earnings side with partial zone guidance.

## The Customization Gap

**Trips need attributing to deliveries, not classifying as business.** The existing capture segments driving into trips and labels them. A courier's economics require knowing which platform, which delivery, which zone and which segment type — deadhead to merchant, wait, delivery leg, repositioning. That is a different segmentation over the same trace, driven by platform notifications and receipts rather than by start-stop detection.

**Deadhead is the whole point and is invisible in a deduction log.** For tax purposes all business miles are equivalent. For decisions, the miles driven while unpaid are the cost that distinguishes a good zone from a bad one, and no existing tool separates them.

**Earnings and mileage have to be joined at the delivery, not at the period.** Current tools sum both over a month. The useful object is a per-delivery record with amount, engaged time and attributed distance, which is what supports comparison across zones, hours and platforms. Building it means holding a delivery-level data model these apps do not have.

**Multi-app is the normal case and the integrations are hostile.** Most serious couriers run two or three platforms. Platform APIs are limited or absent, receipt parsing is fragile, and screen-based capture sits uneasily with terms of service. A durable ingestion strategy — user-permitted export, email parsing, and graceful degradation when a platform changes — is the hardest sustained engineering in this product and is not a feature of the existing apps.

**The output has to be prospective.** Deduction tools look backward by design. The value here is in next week: which hours and zones to work. That requires forecasting, aggregation across users and confidence reporting, none of which exists in an expense app's architecture.

## Target Customer

The existing mileage and gig-tooling vendors, for whom this is the obvious move from tax utility to decision tool and the defence against being commoditised. Also platform-agnostic courier apps looking for a wedge, where mileage capture is the install reason and the economics layer is the retention reason.

## Impact If Solved

The capture layer that already runs on hundreds of thousands of phones starts producing decision-grade economics instead of an annual total. Concretely: a courier sees net per engaged hour by zone and platform, deadhead separated from paid miles, and gets their tax log as a side effect rather than as the product.
