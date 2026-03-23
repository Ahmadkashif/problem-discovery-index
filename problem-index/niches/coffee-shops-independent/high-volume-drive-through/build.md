# Drive-Through Speed-of-Service Analytics

**Niche:** [[niches/coffee-shops-independent/high-volume-drive-through/profile|High-Volume Drive-Through Independents]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Independent drive-through owners have no data on how long each car waits, where the bottleneck is, or how speed changes by staffing level — chain competitors measure this to the second.
**Tags:** #cnn #object-detection #computer-vision #time-series-forecasting #revenue-impact

## The Problem
Chain drive-throughs (Starbucks, McDonald's, Dutch Bros) use proprietary timer systems, computer vision, and queue sensors to measure every step: order time, payment time, handoff time, total window time. They staff and design menus to optimize these metrics. Independent drive-through owners have zero visibility into their throughput — they know the morning rush felt busy, but they don't know that their average window time is 68 seconds (vs. 45 for Dutch Bros) or that their bottleneck is payment processing, not drink making.

## Why Nobody Has Built This
The hardware solutions (HME, Delphi) are chain-focused with enterprise pricing and installation. A camera-based or POS-timestamp-based alternative would be cheaper, but the market of independent drive-through coffee shops (~5,000-8,000 locations) hasn't attracted dedicated product investment. Building computer vision that works across different drive-through layouts, lighting conditions, and camera angles requires meaningful CV engineering.

## What to Build
A camera-mounted (or POS-timestamp-based) system that measures: queue length by time of day, order-to-handoff time per car, and identifies which stage (ordering, making, payment, handoff) is the bottleneck during peak hours. Dashboard shows daily/weekly throughput trends and correlates speed-of-service with staffing levels. Alerts fire when queue backs up past a configurable threshold (e.g., 6+ cars = risk of drive-away).

## Target Customer
Independent drive-through coffee shop owners processing 200-600 cars/day who compete directly with chain drive-throughs on speed.

## Impact If Built
A 10-second improvement in average service time during the 2-hour morning peak means 30-50 additional cars served per day, worth $150-$350 in incremental daily revenue ($55K-$125K annually).
