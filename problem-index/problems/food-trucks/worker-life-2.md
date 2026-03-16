# Heat Exposure & Physical Toll Monitoring

**Industry:** [[food-trucks|Food Trucks]]
**Type:** Worker Life Changing
**One-liner:** Workers trapped in a 100-120°F steel box for 6-8 hours get an early warning before heat exhaustion sets in, instead of discovering it when they collapse.
**Tags:** #lstm #anomaly-detection #signal-processing #worker-facing

## The Problem
Food truck interiors routinely reach 100-120°F during summer service, combining radiant heat from grills and fryers with minimal ventilation in a 7x14-foot steel enclosure. Operators and staff work through progressive heat stress symptoms — dizziness, confusion, slowed reaction time — because stopping service means losing revenue. Heat-related incidents cause burns (impaired coordination near hot oil), falls, and occasional hospitalizations. There is no objective monitoring: operators self-assess, and by the time they feel "really bad," they are already in early heat exhaustion.

## Why It Matters to the Worker
Food truck workers have no HR department, no OSHA compliance officer, and no coworker who can take over while they cool down. The owner-operator in particular cannot afford to stop — every minute off the line is lost revenue. This creates a perverse incentive to push through dangerous heat exposure. Cumulative heat stress over a season contributes to chronic kidney issues, cardiovascular strain, and accelerated physical aging that shortens careers.

## What a Solution Looks Like
A low-cost wearable (wristband or clip-on) tracks skin temperature, heart rate, and heart-rate variability. An LSTM anomaly-detection model trained on the operator's personal baseline identifies deviation patterns that precede heat exhaustion 15-20 minutes before subjective symptoms. The device sends a vibration alert and a phone notification: "Core temp rising — take a 10-minute break with water now." A dashboard logs cumulative heat exposure per shift and per week, giving operators data to justify schedule adjustments (e.g., skipping the 2-4 PM dead window on 95°F+ days).

## Impact If Solved
Prevents 1-3 heat-related incidents per operator per summer season, reduces burn risk from impaired coordination, and gives operators objective data to make rational stop/continue decisions instead of pushing through dangerous conditions.
