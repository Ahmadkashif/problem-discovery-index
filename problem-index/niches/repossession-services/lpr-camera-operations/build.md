# Hit Verification and Route Planning on the Agency's Own Scans

**Niche:** [[niches/repossession-services/lpr-camera-operations/profile|Licence-Plate Camera Operations & Hit Conversion]]
**Industry:** [[industries/repossession-services|Repossession Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Camera drivers choose routes by memory and confirm hits by squinting at a thumbnail, while the agency's own scan and hit history could tell them where to drive and whether the car matches.
**Tags:** #cnns #object-detection #time-series-forecasting #gaussian-processes #optimization-fundamentals #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn camera hours into confirmed hits on the hot list before the car moves, and whoever converts the most scans into verified, recoverable hits per driving hour takes the account.

## The Problem
An agency with four camera cars might log hundreds of thousands of scans a month and a few hundred confirmed hits (estimate). Drivers work the lots that paid last month. Some nights produce nothing; some hits are on the wrong car because a plate was misread or swapped and the driver confirmed too quickly. The scans that would show where hot-list cars actually park, and at what hours, sit unused in the camera vendor's system.

## Why Nobody Has Built This
The camera networks hold the full scan history and sell hits, not planning; agencies see their own data only through the vendor's app; and nobody has packaged hit verification for night-time infrared images.

## What to Build
Two modules over the agency's exportable scans and hits. A forecaster of hit intensity by area and hour from open assignments and past scans, with a route planner that maximises expected hits per hour and re-plans after each confirmed hit. And a verifier that classifies make, model, colour and body style from the hit image, compares them with the assignment, and asks the driver only when it is unsure. Both log outcomes so the agency learns which areas and drivers convert.

## Target Customer
Agencies running two or more camera cars; camera networks' affiliate programmes as a channel.

## Impact If Built
More confirmed hits per driving hour, fewer wrong-car alerts reaching a truck, and drivers whose nights pay more predictably.
