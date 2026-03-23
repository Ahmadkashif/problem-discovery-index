# Condition-Based PM Scheduling Using Telematics Data

**Niche:** [[niches/fleet-managers/preventive-maintenance-scheduling/profile|Preventive Maintenance Scheduling]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No PM scheduling tool uses real-time telematics data (idle time, ambient temperature, load weight, driving behavior) to dynamically adjust maintenance intervals per vehicle — scheduling is still based on static mileage/time rules.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced fleet maintenance manager knows that Vehicle #12 (doing stop-and-go delivery in Phoenix) needs oil changes every 3,500 miles, while Vehicle #38 (doing highway routes in Oregon) can safely go 7,500 miles. This knowledge comes from years of correlating operating conditions with oil analysis results and engine wear patterns — it's tacit knowledge that adjusts OEM intervals based on actual duty cycle. Currently, the fleet either uses the conservative OEM interval for all vehicles (wasting money on over-maintenance) or uses the extended interval for all vehicles (risking under-maintenance on hard-duty vehicles).

## Why Nobody Has Built This
Condition-based maintenance requires a continuous feedback loop: telematics data (operating conditions) correlated with maintenance outcomes (what broke, when, at what condition). This correlation requires years of fleet data linking specific vehicles' operating conditions to their maintenance histories — data that exists in fleet systems but has never been analyzed at scale for interval optimization. The model must also account for OEM warranty requirements, which set minimum intervals regardless of condition.

## What to Build
A PM scheduling engine that ingests telematics data per vehicle (idle hours, ambient temperature, acceleration/deceleration patterns, load indicators, fuel economy trends), correlates these factors with historical maintenance outcomes for similar vehicles, and dynamically adjusts PM intervals per vehicle per service type. Vehicle #12 gets scheduled for oil change at 3,500 miles; Vehicle #38 at 7,000 miles. Each vehicle has a custom PM schedule based on its actual operating conditions, with adjustments every quarter as conditions change.

## Target Customer
Fleet maintenance managers overseeing 50+ vehicles with telematics installed who currently use static PM intervals and suspect they're over-maintaining some vehicles while under-maintaining others.

## Impact If Built
Optimizes PM intervals to reduce total maintenance cost by 15-25% while maintaining or improving fleet reliability. For a 100-vehicle fleet spending $400K/year on PM, this saves $60K-$100K annually. Simultaneously reduces unplanned breakdowns by 20-30% by catching under-maintained hard-duty vehicles earlier.
