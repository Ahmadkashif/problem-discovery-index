# Tare Weights That Drift

**Niche:** [[niches/landfill-operators/scale-house-ticketing-fees/profile|Scale-House Ticketing, Tonnage & Fee Reporting]]
**Industry:** [[industries/landfill-operators|Landfill Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Route trucks are often weighed in only, against a stored empty weight that goes stale as bodies, fuel loads and equipment change, so every ticket is off by the drift.
**Tags:** #change-point-detection #descriptive-statistics #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to turn every load across the scale into a ticket that bills, reports and pays fees correctly the first time, and whoever has the smallest share of tickets corrected after invoicing takes the account.

## The Problem
To keep lines moving, frequent customers' trucks use stored tare weights instead of weighing out. A body rebuild, a new lift or seasonal differences shift the true tare by hundreds of pounds.

## Why It's Still Broken
Re-taring is manual and periodic, and nobody watches the occasional outbound weights for drift.

## What a Fix Looks Like
Automatic comparison of every outbound weight with the stored tare, drift detection per vehicle, and a re-tare prompt when the gap passes a threshold, with an audit log for disputes.

## Who Feels the Pain
Finance teams and customers disputing invoices; attendants caught in the middle.

## Impact If Fixed
A 300-lb average drift across 200 trucks making ~1,000 loads a day (estimate) is ~150 tons a day mis-billed, ~$9,000 a day at ~$60 a ton, in one direction or the other.
