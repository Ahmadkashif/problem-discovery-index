# Route Stop Profitability Decay Detection

**Niche:** [[niches/food-trucks/weekday-office-lunch-route/profile|Weekday Office Lunch Route Trucks]]
**Industry:** [[industries/food-trucks|Food Trucks]]
**Type:** Fix (Pain Point)
**One-liner:** Operators keep serving stops that have quietly become unprofitable — they notice the decline only after months of eroding revenue because they have no per-stop trend data.
**Tags:** #change-point-detection #time-series-forecasting #tabular-ml #revenue-impact

## The Problem
A route stop that once generated $400/day can decay to $200/day over 3-6 months as tenants leave, competitors arrive, or WFH policies shift. Operators rarely notice gradual decline because they track total weekly revenue, not per-stop trends. By the time the stop is obviously dead, they have lost months of opportunity cost — they could have trialed a new location weeks ago.

## Why It's Still Broken
POS systems report daily totals but do not segment revenue by geotagged stop or flag declining trends. Operators would need to manually export data, split it by location, and plot time series to spot decay — a task no solo operator has time for. There is also a psychological factor: operators become attached to familiar stops and resist acknowledging decline until it is undeniable.

## What a Fix Looks Like
Automated per-stop revenue tracking (using POS geotagging or manual stop check-in) with a change-point detection algorithm that flags when a stop's rolling 4-week average drops 20%+ below its historical baseline. The alert includes the rate of decline, estimated weekly revenue loss, and a prompt to trial a replacement stop. The system also identifies the likely cause by correlating decline with nearby office closures, new competitor trucks, or seasonal patterns.

## Who Feels the Pain
Route operators with 4-8 stops who currently carry 1-2 unprofitable stops for months before dropping them, losing $3K-$8K in opportunity cost per decayed stop.

## Impact If Fixed
Detecting stop decay 6-8 weeks earlier and redeploying to a better location recovers $4K-$10K per year in revenue that would otherwise erode unnoticed.
