# Provider Float Pool Scheduling Across Locations

**Niche:** [[niches/urgent-care/multi-site-chains/profile|Multi-Site Urgent Care Chains]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Multi-site chains stop managing provider assignments across locations with spreadsheets and group texts — getting an intelligent scheduling system that matches provider availability, credentials, and site-specific demand in real time.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #optimization-fundamentals #automation #workflow-orchestration

## The Problem
Urgent care chains maintain a "float pool" of providers (physicians, NPs, PAs) who rotate across locations based on demand. Scheduling these providers is a constraint satisfaction nightmare: each provider has credential requirements per state/location, preferred sites, maximum shift lengths, minimum hours guarantees, and varying compensation rates by location. Meanwhile, patient demand fluctuates unpredictably — a flu surge hits one site while another is overstaffed. The operations coordinator managing this for 20+ locations uses a shared Google Sheet, a group text thread, and 2-3 hours daily of phone calls to fill gaps and balance coverage.

## What Already Exists
General physician scheduling tools (QGenda, Heuristic Solutions/Lightning Bolt) handle multi-provider scheduling for hospitals and large medical groups. Urgent care-specific platforms (Experity) manage per-site provider schedules but have no cross-site float pool concept. Shift-filling platforms (ShiftMed, IntelyCare) provide per-diem staffing but not internal float pool optimization. None combine UC-specific constraints (provider must be comfortable reading X-rays at sites with imaging, state licensure for multi-state chains, walk-in volume forecasting) with cross-location optimization.

## The Customization Gap
A float pool scheduler for UC chains needs to ingest: per-provider credential sets (state license, DEA, site-specific privileges), shift preferences and contractual hour guarantees, historical patient volume by site and day-of-week, real-time staffing levels across all locations, and provider performance data (patients per hour, patient satisfaction scores by site). The system should auto-generate weekly float assignments that minimize travel time while maximizing coverage alignment with predicted demand, and handle same-day rebalancing when a site spikes or a provider calls out. This requires UC-specific demand forecasting (urgent care volume is weather-sensitive, flu-season-sensitive, and day-of-week-sensitive in ways distinct from primary care or ED patterns).

## Target Customer
Operations coordinators, regional directors, and scheduling managers at urgent care chains with 10+ locations and a float pool of 15+ providers currently managed through spreadsheets and manual coordination.

## Impact If Solved
Eliminates 10-15 hours per week of manual scheduling coordination. Reduces provider overtime costs by 8-12% through better demand-matching. Decreases site understaffing events (which cause LWBS and extended wait times) by 30-40% through predictive allocation rather than reactive gap-filling.
