# Alarm Fatigue on the Planner's Screen

**Niche:** [[niches/industrial-distributors/reliability-condition-monitoring/profile|Reliability & Condition Monitoring Services]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** When a condition-monitoring system cries wolf a few times, planners stop opening its alerts, and the one that matters is missed.
**Tags:** #gradient-boosting #change-point-detection #bayesian-inference #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this sub-niche is fighting to call a bearing, gearbox or coupling failure weeks before it stops the line, with few enough false alarms that planners keep acting on the alerts, and whoever posts the best caught-to-false-alarm record on the plant's own critical assets takes the account.

## The Problem
Generic thresholds fire on load changes, process upsets and sensor faults. A planner with dozens of open alerts and no way to tell which are real learns to ignore them, and the programme's value collapses.

## Why It's Still Broken
Vendors tune for recall because a missed failure is visible and a false alarm is not. Feedback from planners — "this was a process change, not a fault" — is rarely captured, so thresholds never adapt to each machine's normal behaviour.

## What a Fix Looks Like
Per-asset baselines that account for speed and load, one-click feedback on every alert (real, process change, sensor fault), and a published false-alarm rate per machine class that the vendor is measured on. Alerts arrive ranked, with the evidence and the confidence.

## Who Feels the Pain
Maintenance planners, reliability engineers defending the programme's budget, and distributors whose reliability contracts come up for renewal.

## Impact If Fixed
Halving false alarms, from an estimated ~30–50% of alerts to ~15–25% (estimate), keeps planners engaged, protects renewals, and makes the real warnings count.
