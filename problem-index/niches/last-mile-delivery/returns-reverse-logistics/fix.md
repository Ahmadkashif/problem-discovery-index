# Return Pickup Scheduling Window

**Niche:** [[niches/last-mile-delivery/returns-reverse-logistics/profile|Returns & Reverse Logistics Pickup]]
**Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Type:** Fix (Pain Point)
**One-liner:** Customers requesting a return pickup receive a 3-5 day scheduling window with no specific time slot — forcing them to stay home for an entire day or risk missing the pickup, which restarts the scheduling cycle and delays the refund by another week.
**Tags:** #automation #gradient-boosting #worker-facing #quick-win

## The Problem
A customer initiates a return and requests home pickup. The carrier schedules pickup for "sometime between Monday and Friday" or "between 9am and 6pm on Thursday." The customer must be home during this window with the package ready. If the driver arrives and the customer is out, the pickup fails — requiring rescheduling for the following week. The customer's refund is delayed by the return transit time plus processing, and each failed pickup adds another 3-5 days. For customers who work outside the home, the broad scheduling window effectively requires taking a day off to return a package. This friction drives customers to drop-off locations (UPS Store, Kohl's) instead, where the return processing is slower and the carrier loses the pickup revenue.

## Why It's Still Broken
Return pickups are low-priority for carrier route planning. Forward deliveries have committed delivery windows and contractual obligations; return pickups are squeezed into whatever remaining capacity the route has. Giving return pickup customers a specific 2-hour window requires pre-planning the pickup into the route — which route optimization tools don't support for ad-hoc pickups.

## What a Fix Looks Like
A return pickup scheduling system that: (1) offers the customer a specific 2-hour pickup window based on the delivery driver's planned route for that day; (2) integrates the pickup into the driver's route as a confirmed stop; (3) sends the customer a notification when the driver is 15-20 minutes away; (4) allows the customer to reschedule to a different 2-hour window if the offered time doesn't work.

## Who Feels the Pain
Customers who can't stay home all day for a return pickup and end up driving to a drop-off location — defeating the purpose of doorstep pickup service. Working parents and elderly recipients are disproportionately affected by broad pickup windows.

## Impact If Fixed
Specific 2-hour windows improve first-attempt pickup success from 70% to 90%+. Each avoided failed pickup saves $8-$12 in rescheduling and re-dispatch costs. Customer satisfaction with the returns process — a key loyalty driver — improves measurably.
