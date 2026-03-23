# Samsara Driver Scoring Calibrated for Stop-and-Go Delivery

**Niche:** [[niches/fleet-managers/last-mile-delivery-fleets/profile|Last-Mile Delivery Fleets]]
**Industry:** [[industries/fleet-managers|Fleet Managers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Samsara's driver safety scoring penalizes hard braking and rapid acceleration, but in stop-and-go delivery with 100+ stops, every driver triggers these events constantly — the scores are meaningless.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #worker-facing #automation

## The Problem
Samsara and Motive generate driver safety scores based on events: hard braking, rapid acceleration, sharp turns, and speeding. These thresholds were calibrated for highway trucking where a hard braking event is genuinely concerning. In last-mile delivery, a driver making 120 stops in 8 hours in city traffic legitimately brakes hard dozens of times (pedestrian crossings, delivery zone entries, parking maneuvers). Every driver scores "poor" on generic thresholds, making the scoring system useless for identifying actually dangerous drivers versus drivers doing their job in challenging urban conditions.

## What Already Exists
Samsara and Motive provide configurable driver scoring with adjustable thresholds. Some fleet managers manually adjust sensitivity, but the configuration options are one-size-fits-all — you can lower the hard-braking threshold, but then you miss genuinely dangerous events. There's no route-context-aware scoring that distinguishes "hard brake because of a pedestrian" from "hard brake because the driver was tailgating."

## The Customization Gap
Driver scoring needs to be contextualized against route characteristics: stop density, traffic patterns, speed limits, and historical event baselines for each route segment. A hard braking event on an open highway is concerning; the same deceleration at a known delivery stop is normal. The system should establish per-route-segment baselines and only flag events that exceed what's normal for that specific context. Truly dangerous behavior (distracted driving, running stops, aggressive passing) should score more heavily than delivery-related events.

## Target Customer
Delivery fleet safety managers who have abandoned telematics-based driver scoring because the generic algorithms produce too many false positives in stop-and-go environments.

## Impact If Solved
Makes driver scoring meaningful for delivery fleets, enabling identification of the 5-10% of drivers who are genuinely unsafe versus the 90% who are flagged by generic algorithms. Reduces at-fault accidents by 15-25% by focusing coaching on actual risk behaviors, saving $50K-$200K annually in accident-related costs for a 100-vehicle fleet.
