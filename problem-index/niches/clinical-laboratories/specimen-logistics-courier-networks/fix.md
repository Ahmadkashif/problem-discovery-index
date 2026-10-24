# The Lockbox Pickup Nobody Logged

**Niche:** [[niches/clinical-laboratories/specimen-logistics-courier-networks/profile|Specimen Logistics & Courier Networks]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** A specimen left in a practice's lockbox at 5 p.m. arrives at the lab at 11 p.m. with a potassium that is no longer the patient's, and nobody can say when it was picked up.
**Tags:** #descriptive-statistics #data-integration #automation #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get specimens from practices and patient service centres to the bench inside their stability windows, and whoever delivers the lowest rate of rejected or recollected specimens per thousand picked up takes the account.

## The Problem
Practices drop specimens in outdoor lockboxes after hours. Drivers collect them on a loop, sign a sheet, and the specimens are logged only when they reach accessioning. In summer and winter, temperature extremes and long dwell times alter results without any visible sign.

## Why It's Still Broken
Lockboxes are dumb boxes, driver sheets are paper, and the LIS records receipt, not pickup. Without pickup times, dwell and transit cannot be measured, so the rejections never point back to a route or a box.

## What a Fix Looks Like
Scan specimen bags at pickup with the driver's phone, recording time, location and box temperature from a cheap sensor. Flag specimens whose dwell plus transit exceeds the test's limit before accessioning, so the technologist knows to suspect the result. Report dwell time by lockbox to reschedule pickups where it is worst.

## Who Feels the Pain
Technologists releasing altered results unknowingly, patients recalled for recollection, and drivers blamed without evidence.

## Impact If Fixed
For a few dollars per box and a scan per stop, the lab measures the stage of the process it has never seen. Moving the worst 10% of lockbox pickups earlier could prevent most heat- and dwell-related rejections, ~1,000 a year (estimate) for a mid-size lab.
