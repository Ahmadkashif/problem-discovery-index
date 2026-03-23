# Specimen Viability Timer & Priority Dispatch

**Niche:** [[niches/last-mile-delivery/medical-courier-services/profile|Medical Courier Services]]
**Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Type:** Fix (Pain Point)
**One-liner:** Medical specimens have strict viability windows — some blood tests require delivery within 30 minutes, tissue samples within 2 hours — but dispatchers manage these deadlines mentally across 20-40 active pickups, inevitably miscalculating which specimen must be delivered next when multiple pickups queue simultaneously.
**Tags:** #automation #compliance #worker-facing #quick-win

## The Problem
A medical courier dispatcher manages 30 active specimen pickups across 8 drivers. Each specimen has a viability window: a CBC blood draw collected at 2:15pm must reach the lab by 4:15pm (2-hour window), while a coagulation study collected at 2:30pm must arrive by 3:00pm (30-minute window). The dispatcher assigns deliveries based on their mental model of which specimens are most urgent, but when 5 pickups queue simultaneously from different clinics, they miscalculate priority. A specimen that expires in 25 minutes sits on a driver's shelf while the driver delivers a less-urgent specimen first. Expired specimens must be recollected — an inconvenience for the patient and a cost to the clinic.

## Why It's Still Broken
No dispatch tool models specimen viability timers as a routing constraint. General delivery platforms optimize for distance or time windows (2-4pm delivery request), not for "this item expires in 22 minutes and must be routed above all other stops." Medical courier dispatchers track viability mentally or on paper sticky notes — a system that works for 10 active pickups but fails at 30+.

## What a Fix Looks Like
A dispatch overlay that: (1) captures specimen type and collection time at pickup (driver scans label or selects specimen type); (2) calculates the viability deadline based on specimen type; (3) displays a real-time countdown timer for each active specimen across the fleet; (4) auto-prioritizes delivery routing by viability urgency (shortest remaining window delivered first); (5) alerts the dispatcher when a specimen's viability timer drops below threshold and no driver is close enough to deliver in time — triggering a recollection alert to the clinic.

## Who Feels the Pain
Dispatchers who carry the cognitive burden of tracking 20-40 specimen deadlines simultaneously, and who bear responsibility when an expired specimen forces a patient to return for recollection.

## Impact If Fixed
Reducing specimen expiration rate from 3-5% to under 1% prevents recollection costs ($50-$200 per recollection) and maintains courier service quality ratings with hospital/lab clients. On 500 monthly specimens, eliminating 10-20 expirations saves $500-$4,000/month in direct recollection costs and protects contract renewal.
