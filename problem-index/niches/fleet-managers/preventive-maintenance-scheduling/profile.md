# Preventive Maintenance Scheduling

**Parent Industry:** [[industries/fleet-managers|Fleet Managers]]
**Category:** Highly Automatable

## Profile
**Market Size:** $7B
**Share of Parent Industry:** 10%
**Digital Adoption:** Medium — Many fleets have maintenance scheduling tools, but they use static mileage/time intervals rather than condition-based or usage-aware scheduling.
**Target Buyer:** Fleet maintenance manager or shop foreman responsible for scheduling and executing preventive maintenance
**Automation Potential:** High — PM scheduling is inherently rule-based (interval-driven), but the rules should be dynamic (condition-based), which current tools don't support.

## What Makes This a Distinct Niche
Preventive maintenance (PM) scheduling determines 60-70% of total fleet maintenance cost — get the intervals right and vehicles last longer with fewer breakdowns; get them wrong (too frequent = waste, too infrequent = failures) and costs spiral. Current PM scheduling uses static OEM intervals (oil every 5,000 miles, brakes every 30,000 miles) regardless of actual operating conditions. A vehicle doing stop-and-go delivery in Phoenix summer heat needs oil changes twice as often as one doing highway runs in Seattle. The gap between static scheduling and condition-based scheduling represents billions in wasted maintenance spending and preventable breakdowns.

## Current Tools & Gaps
Fleetio, RTA Fleet Management, and Fleet Complete all provide mileage-based and time-based PM scheduling. Telematics platforms (Samsara, Geotab) provide operating condition data (idle time, ambient temperature, driving behavior). But the PM scheduler doesn't consume telematics data to adjust intervals. The maintenance manager manually overrides OEM intervals based on experience — "these Transit vans in Phoenix need oil every 3,500 miles, not 5,000" — but this tacit knowledge isn't systematized.

## Problems
- [[niches/fleet-managers/preventive-maintenance-scheduling/build|🔨 Build: Condition-Based PM Scheduling Using Telematics Data]]
- [[niches/fleet-managers/preventive-maintenance-scheduling/buy|🛒 Buy: Fleetio PM Schedules Adjusted for Operating Conditions]]
- [[niches/fleet-managers/preventive-maintenance-scheduling/fix|🔧 Fix: PM Scheduling Based on Static OEM Intervals Instead of Actual Wear]]
