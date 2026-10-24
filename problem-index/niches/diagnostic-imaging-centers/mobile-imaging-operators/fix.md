# The Authorization That Expires Before the Trailer Returns

**Niche:** [[niches/diagnostic-imaging-centers/mobile-imaging-operators/profile|Mobile Imaging Operators & Rural Shared Units]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Fix (Pain Point)
**One-liner:** A rural patient's MRI is approved for 30 days, the unit visits every two weeks, and one missed visit means a new authorization and a month's delay.
**Tags:** #gradient-boosting #automation #quick-win #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to keep each mobile MRI, CT or PET unit scanning on the days it is parked at a host site, and whoever fills the highest share of booked unit-days with completed, paid scans takes the account.

## The Problem
Host schedulers book patients into the next unit visit without checking the authorization window against the rotation. A cancellation or breakdown pushes the patient past expiry.

## Why It's Still Broken
The host books, the operator runs the unit, and the ordering practice holds the authorization. Nobody sees all three dates together.

## What a Fix Looks Like
At booking, show each patient's authorization expiry against the next two unit visits, and flag those at risk. Request extensions automatically when a visit is cancelled.

## Who Feels the Pain
Rural patients waiting weeks for a scan; host radiology managers; operators losing paid scans to paperwork.

## Impact If Fixed
Avoiding a handful of expired authorizations per unit per month keeps those scans on the schedule. Each is a full paid exam (estimate).
