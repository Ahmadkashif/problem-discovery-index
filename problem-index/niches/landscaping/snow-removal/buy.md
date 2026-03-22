# Snow Operations Module for Landscaping Platforms

**Niche:** [[niches/landscaping/snow-removal/profile|Snow Removal]]
**Industry:** [[industries/landscaping|Landscaping]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** LMN and Aspire handle snow as an afterthought — their scheduling models assume predictable recurring service, but snow events are weather-triggered, variable-duration, and require per-event documentation that recurring service scheduling was never designed to capture.
**Tags:** #data-integration #automation #workflow-orchestration #compliance

## The Problem
Landscaping companies that add snow removal use the same platform (LMN, Aspire, Jobber) for both services, but the operational model is fundamentally different. Landscape maintenance is predictable: mow 40 properties every Tuesday, same route, same crew. Snow removal is stochastic: service is triggered by weather events of unpredictable timing, duration, and severity, with per-event pricing that varies by accumulation depth and service type (plowing vs. salting vs. both). When a contractor creates a "snow service" in LMN, the system treats it like a scheduled landscape job — but there's no way to link it to a weather trigger, no way to track multiple service events per property per storm (initial push at 2am, re-push at 6am, salting at 8am), and no way to generate per-event invoices based on actual accumulation thresholds. The contractor ends up tracking snow operations in a parallel Excel spreadsheet because the landscaping platform can't model the workflow.

## What Already Exists
LMN includes a snow module that lets companies create snow contracts and log service events, but it functions as a time-tracking overlay — the contractor manually logs arrival time, departure time, and service type per property per event. Aspire handles snow contracts similarly with manual event logging. Jobber has no snow-specific features. All three generate invoices based on logged events but require manual entry of which accumulation tier applies (2-4", 4-6", 6+") and which pricing level that triggers. None integrate with weather data to auto-detect events or auto-determine trigger thresholds.

## The Customization Gap
Three capabilities are missing from landscaping platforms for snow operations. First, weather-triggered event detection: when official weather station data shows accumulation exceeding a contract's trigger threshold in the contract's geographic zone, automatically create a service event, notify assigned crews, and begin tracking response time against the SLA clock. Second, multi-visit event tracking: a single storm can require 2-4 service visits to the same property (initial plow, re-plow, de-ice, post-storm cleanup) — each visit is a billable event that must be tracked separately with its own timestamp, material usage (salt/sand quantities), and photographic documentation. Third, accumulation-tiered invoicing: per-push contracts have different rates for different accumulation ranges (e.g., $350 for 2-4", $500 for 4-6", $750 for 6+") — the system should auto-determine the applicable rate based on the weather data for that location during that event, not require the contractor to manually select the tier.

## Target Customer
Landscaping companies with $1-10M in revenue that add $200K-2M in seasonal snow revenue, already using LMN, Aspire, or Jobber for their landscape operations, and currently tracking snow operations in a parallel spreadsheet because their platform can't model the workflow.

## Impact If Solved
Eliminates the parallel Excel tracking system, saving 3-5 hours per storm event in manual documentation and invoicing. Reduces billing disputes by 60-80% through weather-verified accumulation data linked to each service event. Enables accurate per-event profitability analysis that most snow contractors have never been able to calculate.
