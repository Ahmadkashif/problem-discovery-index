# Route Intelligence for Jobber/LMN

**Niche:** [[niches/landscaping/crew-routing-scheduling/profile|Crew Routing & Scheduling]]
**Industry:** [[industries/landscaping|Landscaping]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Jobber and LMN have all the data needed for route optimization — property locations, service schedules, crew assignments, and job completion times — but use none of it for intelligent routing, leaving the operations manager to manually sequence 80-120 daily stops across 3-10 crews by looking at a map of pins.
**Tags:** #gradient-boosting #automation #data-integration #workflow-orchestration

## The Problem
A landscaping company on Jobber has years of data: every property address, every service visit with start/end times, every crew assignment, every cancellation, and every rain-day reschedule. This data contains the patterns needed for intelligent routing — which property clusters minimize drive time, which crew-to-property assignments produce the fastest service times, which day-of-week assignments balance crew workloads. But Jobber surfaces none of these patterns. The map view shows pins with no suggested sequence. The calendar view shows time blocks with no workload analysis. The reporting shows aggregate metrics (revenue per crew, jobs per day) with no route efficiency analysis. The operations manager looks at the same data through the Jobber interface every morning and manually performs the optimization that the platform could automate — because the platform was built as a scheduling tool, not a routing tool.

## What Already Exists
Jobber's map view displays scheduled jobs as pins color-coded by crew. Its mobile app provides turn-by-turn navigation to the next job but doesn't optimize the sequence. LMN's scheduling module allows drag-and-drop crew assignment on a calendar and tracks actual vs. estimated job times but has no routing component. Both platforms have API access that third-party route tools could plug into, but no third-party integration exists that models landscaping-specific constraints. Jobber recently added a "route optimization" button that reorders stops for a single crew using a basic TSP solver — but it doesn't consider property-specific time estimates, crew-equipment matching, or cross-crew rebalancing.

## The Customization Gap
Three intelligence layers are missing from Jobber and LMN. First, predictive service time: using the platform's own historical job completion data to predict how long each property will take for each crew on each day of the week, by season — replacing the uniform 30-minute default with property-specific estimates that enable realistic workload balancing. Second, cross-crew route optimization: reassigning properties between crews (not just reordering within a crew) to maximize geographic density per crew per day — the ops manager does this mentally but the platform doesn't even surface the geographic overlap between crews' current assignments. Third, schedule-level optimization: analyzing the full weekly schedule to identify whether moving Client A from Tuesday to Thursday and Client B from Thursday to Tuesday would save 25 minutes of drive time per day for both affected crews — a combinatorial analysis no human can perform across 400 properties but that an optimizer solves in seconds.

## Target Customer
Landscaping companies with 3-10 crews already on Jobber or LMN, where the platform manages the data but the ops manager performs the routing intelligence manually every morning.

## Impact If Solved
Unlocks the routing optimization value from data already sitting in Jobber/LMN databases, reducing average drive time per crew by 15-25% without any additional hardware or data collection. Converts the daily 30-60 minute route planning task into a 2-minute review-and-approve workflow. Enables data-driven crew workload balancing that reduces the perception of "unfair" route assignments driving crew turnover.
