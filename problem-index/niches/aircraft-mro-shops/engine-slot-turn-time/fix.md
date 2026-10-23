# Repair-Vendor Status Chased by Phone

**Niche:** [[niches/aircraft-mro-shops/engine-slot-turn-time/profile|Engine Shop Slot & Turn-Time Commitments]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Expediters spend their mornings calling blade and case repair vendors to learn whether parts that left three weeks ago will be back in time.
**Tags:** #large-language-models #time-series-forecasting #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to quote an engine's release date at induction and hit it while parts and repair vendors slip, and whoever keeps the most engines inside their quoted turn time takes the account.

## The Problem
Repair vendors report status in different ways: a portal for one, a weekly spreadsheet for another, nothing until the part ships for most. The shop's expediters call and email for updates on the parts that matter this week, and the answers end up in a planner's spreadsheet. Late parts are discovered when they fail to arrive.

## Why It's Still Broken
Repair vendors are small specialists without integration budgets, and each shop uses many of them. Nobody has made status capture cheap enough for the vendor or valuable enough to share, so the phone remains the integration layer.

## What a Fix Looks Like
An agent that reads vendor emails, spreadsheets and portal exports and keeps a single status per part out for repair. It requests updates automatically on a schedule tied to each part's due date, flags parts whose vendor history says they'll run late, and feeds the release-date forecast.

## Who Feels the Pain
Expediters and buyers at engine and component shops; planners re-planning around late parts; repair vendors fielding the same calls from many customers.

## Impact If Fixed
Freeing ~2–3 hours a day per expediter (estimate) and spotting late repair loops a week earlier could pull a few days of slip out of each affected visit. Across ~150 visits a year, that is hundreds of spare-engine days.
