# PM Scheduling Based on Static OEM Intervals Instead of Actual Wear

**Niche:** [[niches/fleet-managers/preventive-maintenance-scheduling/profile|Preventive Maintenance Scheduling]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Fleets follow OEM-recommended intervals designed for average consumer use, not commercial fleet duty cycles — resulting in either $50K+/year in wasted over-maintenance or preventable breakdowns from under-maintenance.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #worker-facing

## The Problem
Ford recommends oil changes every 7,500-10,000 miles for the Transit van under "normal" driving conditions and every 5,000 miles under "severe" conditions. A fleet's delivery vans operate exclusively in severe conditions (stop-and-go, high idle, heavy loads, extreme temperatures), but the fleet follows the 7,500-mile "normal" interval because that's what the OEM handbook says and what the shop management system is configured for. The result: engines accumulate excessive wear between services, and the fleet experiences 2-3x the expected engine failure rate. Meanwhile, the fleet's highway courier vehicles are getting the same 7,500-mile interval when they could safely go 10,000 miles — over-maintained by 33%.

## Why It's Still Broken
OEM intervals are legally conservative (designed to avoid warranty claims) and generalized (one interval for millions of diverse use cases). The fleet maintenance manager knows these intervals are wrong for their specific vehicles but has no data-driven basis for adjusting them. Oil analysis programs exist but are expensive ($30-$50 per sample), slow (3-5 day turnaround), and typically only done on a sample of vehicles. The maintenance manager defaults to OEM intervals because "nobody gets fired for following the manufacturer's recommendation."

## What a Fix Looks Like
A data-driven interval adjustment program that uses oil analysis sampling on a representative subset of vehicles (by route type and operating condition), correlates oil degradation rates with telematics-measured operating conditions, and generates fleet-specific PM intervals per vehicle group. The output replaces the generic "every 7,500 miles" with data-backed intervals: "Urban delivery vans: 4,500 miles. Suburban routes: 6,500 miles. Highway couriers: 9,000 miles." Updated quarterly based on ongoing oil analysis feedback.

## Who Feels the Pain
Fleet maintenance managers who suspect they're maintaining vehicles on wrong intervals but can't justify deviating from OEM recommendations without data, and fleet owners paying for either unnecessary maintenance or unnecessary engine replacements.

## Impact If Fixed
Reduces total PM costs by 15-25% through right-sized intervals while simultaneously reducing unplanned breakdowns by 20-30%. For a 75-vehicle fleet spending $300K/year on PM, this represents $45K-$75K in annual savings plus $30K-$60K in avoided breakdown-related costs.
