# A Condition Record at Every Valet Handoff

**Niche:** [[niches/parking-operators/valet-hospitality-parking/profile|Valet & Hospitality Parking]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The only evidence of a car's condition when it reaches the valet stand is a runner's memory of one car among four hundred.
**Tags:** #cnns #semantic-segmentation #contrastive-learning #transfer-learning #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to park and return every guest's car undamaged, and whoever has the lowest damage and lost-key claim cost per 1,000 cars parked takes the account.

## The Problem
Guests report damage after the car is returned. The operator cannot show the scratch was there at drop-off, so it pays, the client hears about it, and a runner is written up. Phone walkarounds take ~60–90 seconds a car (estimate) and are skipped when the stand is busy.

## Why Nobody Has Built This
Vehicle-scanning systems were designed for drive-through lanes at rental returns and auctions, with controlled lighting and slow, straight approaches. A hotel porte-cochère has awnings, headlights, rain and cars stopping at angles. Each stand is a small site, so hardware has to be cheap and installation quick, and no operator has pooled enough paired images to train on.

## What to Build
Two or three fixed cameras at the drop-off and return points, triggered by the claim-ticket scan. A segmentation model finds panels; a change-detection model compares drop-off and return images panel by panel and flags new damage with a confidence score, separating rain, reflections and dirt from scratches and dents. Every car gets a timestamped condition record linked to the ticket, the runner and the parking location. Claims are answered with the two images side by side.

## Target Customer
Hospitality valet operators running 50+ stands; hotel groups and hospital systems that self-operate valet.

## Impact If Built
A stand parking 100,000 cars a year at 1–3 claims per 10,000 that resolves half of its contested claims from images avoids ~5–15 payouts at ~$500–2,500 each (estimate). Across 200 stands that is ~$0.5–7M a year, before the retention value of a hotel client that stops hearing complaints.
