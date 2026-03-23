# Best Value Score Monitoring and Recovery

**Niche:** [[niches/moving-companies/military-pcs-relocation/profile|Military PCS Relocation Movers]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Fix (Pain Point)
**One-liner:** TSPs discover their Best Value Score has dropped only after losing volume allocation in the next cycle — by then it's too late to recover.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #anomaly-detection #revenue-impact

## The Problem
The DoD's Best Value Score (BVS) determines what percentage of military moves a TSP receives each cycle. BVS is calculated from customer satisfaction surveys, claims ratios, pickup/delivery performance, and cost competitiveness. TSPs currently have no real-time visibility into their evolving BVS — they see the final score after the evaluation period closes. A single bad month (late pickups during peak PCS season, a spike in damage claims) can tank a score that takes 6-12 months to rebuild, and the revenue impact is immediate: a 10-point BVS drop can mean 20-30% fewer move tenders next cycle.

## Why It's Still Broken
The BVS formula is published but the inputs are scattered across multiple systems — customer surveys in one portal, claims data in another, on-time performance in dispatch logs. No TSP has assembled these into a unified tracking view because each data source requires different access methods and the weighting formula changes periodically. TSPs treat BVS as a lagging indicator they react to rather than a leading metric they manage.

## What a Fix Looks Like
A dashboard that aggregates the known BVS input signals — survey scores, claims filed vs. resolved, pickup/delivery on-time rates, cost competitiveness vs. lane averages — and projects the TSP's likely BVS at the end of the current evaluation period. An anomaly detection layer flags when any single input metric is trending toward a threshold that would trigger a score drop, with enough lead time (4-6 weeks) to intervene: expedite open claims, prioritize on-time performance on remaining moves, or adjust pricing.

## Who Feels the Pain
TSP owners who have lost 20-40% of their government business overnight due to a BVS drop they didn't see coming, and operations managers who could have prevented it with 30 days of warning.

## Impact If Fixed
TSPs that maintain top-quartile BVS scores receive 2-3x the volume of bottom-quartile competitors. Preventing a single BVS cycle drop preserves $500K-2M in annual revenue for a mid-sized TSP.
