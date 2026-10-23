# The Hosting Map Refreshed Once a Year

**Niche:** [[niches/electric-utilities/der-interconnection-hosting-capacity/profile|DER Interconnection & Hosting Capacity]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Fix (Pain Point)
**One-liner:** Hosting values go stale the moment the next batch of applications is approved, so applicants design against capacity that is already gone.
**Tags:** #feature-engineering #time-series-forecasting #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to clear rooftop, storage and EV-charger applications against a hosting-capacity number that later studies confirm, and whoever sends the fewest applications to full study without a later violation takes the account.

## The Problem
Many utilities recompute hosting capacity on a monthly or slower cycle (estimate) because the full analysis is a heavy batch run over every feeder. Between runs, approvals and queued applications consume capacity the map still shows as free, and switching or reconfiguration changes what each section can take.

## Why It's Still Broken
The full recomputation is expensive and nobody owns an incremental update. Queue positions live in the portal, network changes in GIS and the planning model, and the map in a third tool.

## What a Fix Looks Like
Decrement published capacity as applications are approved or queued ahead, flag sections where recent network changes make the value unreliable, and trigger targeted recomputation for those sections only. Show applicants the date and the queue position each value reflects.

## Who Feels the Pain
Installers and developers who redesign after failed screens; interconnection engineers fielding complaints; regulators who mandated the maps.

## Impact If Fixed
Maps that reflect the queue between full runs, ~10%–20% fewer doomed applications and a smaller supplemental-review backlog (estimate), without waiting for a new analysis engine.
