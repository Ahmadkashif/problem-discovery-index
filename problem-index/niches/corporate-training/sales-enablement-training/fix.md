# New Rep Ramp Time Inconsistency

**Niche:** [[niches/corporate-training/sales-enablement-training/profile|Sales Enablement & Revenue Training]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Fix (Pain Point)
**One-liner:** New sales reps take 4-9 months to reach full productivity, and the variance is driven by inconsistent onboarding quality across managers and regions — not by rep talent.
**Tags:** #gradient-boosting #regression #tabular-ml #worker-facing #revenue-impact

## The Problem
Sales organizations invest $15,000-$30,000 per new hire in onboarding and ramp training, but time-to-full-productivity varies wildly: some reps hit quota in month 4, others struggle until month 9. When enablement leaders investigate, they find that the onboarding experience differs dramatically by manager: one manager provides daily ride-alongs and call reviews, another assigns the new hire to self-paced e-learning and checks in monthly. The corporate onboarding curriculum exists, but local execution is inconsistent.

## Why It's Still Broken
Enablement teams design structured ramp programs with milestones (first demo, first proposal, first closed deal), but they have no visibility into whether managers are actually executing the prescribed activities. The LMS tracks course completion, but manager-led activities (ride-alongs, call reviews, pipeline coaching sessions) are untracked. Ramp time variation is attributed to "rep quality" because the data to blame inconsistent management coaching does not exist.

## What a Fix Looks Like
A ramp tracking system that: (1) defines the prescribed onboarding journey as a sequence of both self-paced and manager-led activities with target dates; (2) tracks completion of manager-led activities (logged by the manager or inferred from calendar events); (3) correlates ramp trajectory (weeks to first deal, quota attainment at 90/180/365 days) with onboarding activity completion patterns; and (4) alerts the enablement leader when a new rep's ramp trajectory deviates from the predicted path, along with which onboarding activities were missed or delayed.

## Who Feels the Pain
New sales reps who receive inconsistent onboarding depending on their assigned manager — some get structured coaching while others are left to figure it out alone, creating inequitable outcomes that feel like a talent problem but are actually a process problem.

## Impact If Fixed
Reducing median ramp time from 6 months to 4 months at a 100-rep organization yields approximately $2-5M in additional annual revenue from the incremental productive months, plus improved new hire retention (reps who ramp slowly are 2x more likely to quit within the first year).
