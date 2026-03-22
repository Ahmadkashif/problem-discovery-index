# PMS Inventory Module Adapted for Limited Wholesaler Delivery Schedules

**Niche:** [[niches/pharmacy-independents/rural-pharmacy/profile|Rural Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** PioneerRx and QS/1 inventory modules assume daily wholesaler delivery — they trigger reorders when stock drops below a par level without considering that the next delivery may be 2-3 days away, causing stockouts that are catastrophic for the only pharmacy within 20 miles.
**Tags:** #feature-engineering #optimization-fundamentals #data-integration #quick-win #revenue-impact

## The Problem
Standard PMS inventory modules use a simple par level system: when on-hand quantity for an NDC drops below the minimum threshold, the system adds it to the next wholesaler order. This works when delivery arrives daily — a one-day gap is manageable. But rural pharmacies receiving deliveries 2-3 times per week face a different math: if the par level triggers a reorder on Wednesday morning and the next delivery isn't until Friday, the pharmacy needs enough stock to cover Wednesday, Thursday, and Friday dispensing. The PMS doesn't know the delivery schedule and can't calculate coverage duration. The pharmacist compensates by mentally inflating par levels (ordering more than needed "just in case"), which ties up working capital, or by manually checking the delivery calendar before confirming orders — a 20-30 minute daily task that adds no value.

## What Already Exists
PioneerRx's auto-reorder module, QS/1's inventory management, and Liberty Software's ordering interface all generate purchase orders based on par levels and dispensing history. McKesson, Cardinal Health, and AmerisourceBergen offer electronic ordering with delivery schedule confirmation. The dispensing data and delivery schedule data both exist — they're just not connected in the reorder logic.

## The Customization Gap
The gap is delivery-schedule-aware reorder logic: (1) the PMS needs to know the pharmacy's wholesaler delivery schedule (e.g., Monday/Wednesday/Friday), (2) reorder calculations must account for demand-days-until-next-delivery rather than a static par level, (3) the system should flag "will stock out before next delivery" situations at order cutoff time (typically 4-6pm the day before delivery) rather than at dispensing time when it's too late, and (4) emergency order recommendations when a critical medication will stockout before the next scheduled delivery — suggesting patient transfer, same-day courier add-on, or therapeutic alternative. This requires modest customization of existing PMS reorder logic — adding a delivery calendar input and changing the reorder trigger from "below par" to "below coverage-until-next-delivery." A PMS plugin or configuration module priced at $49-99/month fills this gap.

## Target Customer
Rural pharmacies with 2-3x/week wholesaler delivery schedules who currently manage reorder timing manually by cross-referencing the delivery calendar with on-hand inventory every afternoon.

## Impact If Solved
Eliminates 20-30 minutes of daily manual delivery-schedule-aware ordering, reduces stockout-before-delivery events by 60-80%, and right-sizes safety stock to match actual delivery frequency rather than inflated par levels — freeing $1,500-4,000 in excess inventory per pharmacy.
