# Structural Analyses That Fail on Stale Mount Records

**Niche:** [[niches/wireless-carriers/site-modification-permitting/profile|Site Modifications, Leasing & Permitting]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Structural and mount analyses are run on the equipment the records say is on the tower, and when the records are wrong the analysis is redone after a site visit, costing weeks.
**Tags:** #cnns #object-detection #feature-engineering #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to compress the weeks between "this site needs new radios" and "on air" — tower-owner application, structural and mount analysis, landlord consent and municipal approval inside the FCC shot clock — and whoever gets the most sites through that chain fastest takes the deployment programme.

## The Problem
An engineer models the tower with existing and proposed loads. If the existing equipment list is out of date (old antennas never removed, a neighbour tenant's additions, a mount replaced), the analysis is wrong. The error surfaces when a crew arrives, or when a mapping visit is ordered after the fact, and the step starts again.

## Why It's Still Broken
Equipment records are updated by whoever remembers to, across the carrier, the tower owner and other tenants. Mount mapping visits cost money, so they are skipped when records look recent.

## What a Fix Looks Like
Use the photos and drone imagery already captured at site visits and audits to detect and count antennas, radios and mounts by position. Compare the result with the record, and flag sites for a mapping visit before the analysis is ordered.

## Who Feels the Pain
Site development managers whose schedules slip, structural engineers redoing work, and crews sent to sites that can't be built as designed.

## Impact If Fixed
Analyses are done once on accurate loads, saving weeks on the sites that would otherwise loop.
