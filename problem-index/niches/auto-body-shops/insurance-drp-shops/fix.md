# DRP KPI Threshold Violations Discovered Too Late to Correct

**Niche:** [[niches/auto-body-shops/insurance-drp-shops/profile|Insurance DRP Shops]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Shop owners discover they've breached a DRP KPI threshold when the insurer sends a warning letter — weeks after they could have corrected course.
**Tags:** #time-series-forecasting #anomaly-detection #tabular-ml #revenue-impact

## The Problem
Insurer DRP programs measure shop performance over rolling 30-90 day periods. A shop's cycle time creeps up due to a parts shortage one week, a technician calling in sick another week, and a complex repair extending beyond estimate — individually manageable events that cumulatively push the rolling average above threshold. The shop owner doesn't realize the trend until they check the insurer portal (which they might only do monthly) or receive a formal warning letter. By then, the rolling average is locked in and the shop faces a 90-day probation period or outright removal from the program.

## Why It's Still Broken
Insurer portals show current metrics but don't project trends or send proactive alerts when a metric is trending toward threshold. The data is backward-looking: it shows what happened, not what's about to happen. Shop owners who check metrics weekly can sometimes catch trends, but most only check monthly because the portals are slow and fragmented across multiple insurers.

## What a Fix Looks Like
A trend-monitoring system that continuously tracks each DRP metric's rolling average and projects where it will be in 1, 2, and 4 weeks based on current trajectory. When a metric is projected to breach threshold within the measurement period, the system sends an alert with specific corrective actions: "Your Progressive cycle time average is 6.2 days against a 6.0-day threshold. If your next 3 repairs complete in under 5 days, you'll recover to 5.8. Prioritize these 3 vehicles for delivery by Friday."

## Who Feels the Pain
DRP shop owners who lose insurer relationships worth $200K-$500K/year due to KPI violations they could have prevented with 2 weeks of advance warning.

## Impact If Fixed
Prevents 2-4 DRP relationship warnings per year per shop by providing early trend detection. For a shop with $1.5M in DRP revenue across 5 programs, preventing a single DRP loss protects $300K in annual revenue.
