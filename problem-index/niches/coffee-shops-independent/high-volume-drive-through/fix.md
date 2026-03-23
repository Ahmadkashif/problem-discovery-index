# Peak Rush Staffing Mismatch

**Niche:** [[niches/coffee-shops-independent/high-volume-drive-through/profile|High-Volume Drive-Through Independents]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Drive-through owners schedule by habit, not throughput data — overstaffing the afternoon lull by 2 people while understaffing the 7am crush by 1.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #quick-win #worker-facing

## The Problem
A drive-through shop's revenue concentrates into two 90-minute windows (morning rush 6:30-8:00, afternoon pickup 2:30-4:00), but scheduling tools don't model this bimodal demand curve. Owners schedule flat shifts (7am-2pm, 2pm-close) that over-staff transitions and under-staff peaks. During peak, each barista handles $80-$120/hour in revenue; during lulls, that drops to $20-$30/hour. The mismatch costs money in both directions — labor waste during slow periods and lost throughput (drive-aways) during peaks.

## Why It's Still Broken
Generic scheduling tools (7shifts, Homebase) let owners set labor targets per hour, but the owner must manually specify those targets based on gut feel. Drive-through-specific demand patterns — where a 15-minute difference in shift start time can add or lose $500 in morning revenue — require granular demand forecasting that no scheduling tool provides for independents. The data (POS timestamps by minute) exists but is never analyzed at the throughput level.

## What a Fix Looks Like
A scheduling overlay that analyzes 90 days of POS timestamp data to identify the shop's actual demand curve at 15-minute resolution, then recommends shift start/end times and staffing levels that match throughput targets. Shows the owner: "Your 7:15-7:45 window averages 42 transactions but you only have 2 staff — adding a third barista at 7:00 would capture an estimated 12 additional transactions worth $72."

## Who Feels the Pain
The owner who watches the morning line back up to the street while knowing they have two baristas coming in at 8am — 45 minutes after the peak starts — and the baristas who endure a frantic 90-minute rush that could be manageable with one more set of hands.

## Impact If Fixed
Right-sizing staffing to the drive-through demand curve saves 8-12% of labor cost while increasing peak throughput by 15-25%, a combined impact of $3,000-$6,000/month for a shop doing $50K+ monthly.
