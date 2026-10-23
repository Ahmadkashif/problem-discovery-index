# Vibration Software That Knows the Shelf

**Niche:** [[niches/industrial-distributors/reliability-condition-monitoring/profile|Reliability & Condition Monitoring Services]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Vibration and machine-health platforms diagnose the fault; they don't check whether the replacement part is in stock before the repair window.
**Tags:** #time-series-forecasting #gradient-boosting #feature-engineering #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this sub-niche is fighting to call a bearing, gearbox or coupling failure weeks before it stops the line, with few enough false alarms that planners keep acting on the alerts, and whoever posts the best caught-to-false-alarm record on the plant's own critical assets takes the account.

## The Problem
An alert gives the plant two to six weeks of warning (estimate), but the planner still has to identify the part, find it, and order it. Long-lead gearboxes and special bearings can take longer than the warning, so the advantage of early detection is lost in procurement.

## What Already Exists
Machine-health and vibration platforms from sensor vendors and manufacturers, route-based analysis software, and CMMS work-order systems that receive alerts.

## The Customization Gap
A distributor layer that maps each monitored position to its exact components, checks stock and lead time the moment an alert fires, stages a kit, and estimates whether the part will arrive before the predicted failure window. It should prioritise alerts by the combination of failure probability and supply risk, not by vibration severity alone.

## Target Customer
BPT distributors offering reliability services, and plants using condition monitoring without a supply link.

## Impact If Solved
If ~50–70% of alerts on monitored positions become planned repairs with the part staged before the failure window (estimate), each converted emergency saves the plant hours of downtime and expedite costs of ~$500–$5,000 per event (estimate), and the distributor that monitors becomes the obvious supplier.
