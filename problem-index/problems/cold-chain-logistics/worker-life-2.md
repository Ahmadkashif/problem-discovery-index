# Reefer Unit Pre-Cool Time Prediction for Load Planning

**Industry:** [[cold-chain-logistics|Cold Chain Logistics]]
**Type:** Worker Life
**One-liner:** Cold chain planners scheduling loads must know how long a reefer unit will take to reach setpoint temperature before loading — a number that varies with ambient temperature, unit age, unit model, and setpoint — but currently estimate from fixed tables that don't account for unit-specific performance degradation.
**Tags:** #gradient-boosting #regression #tabular-ml #worker-facing #automation

## The Problem

Before a refrigerated load can be picked up, the reefer unit must be pre-cooled to the cargo setpoint temperature. Pre-cool time varies: a new Carrier Transicold unit pulling down from 75°F ambient to 34°F setpoint takes 45-60 minutes; an older unit with compressor wear on the same pull-down takes 90-120 minutes. Getting the pre-cool timing wrong wastes driver time (driver arrives at shipper before the unit is ready) or delays loading (unit not at setpoint when driver arrives, extending dock time and creating dock congestion).

Planners currently estimate pre-cool time from manufacturer tables or rule-of-thumb experience. They don't account for the specific unit assigned to the load, that unit's recent performance history, or current ambient temperature at the origin facility. This creates unnecessary driver detention and shipper dock scheduling problems.

## The Solution

A regression model trained on historical reefer unit pre-cool logs (start temperature, target setpoint, ambient temperature at origin, unit model, engine hours, recent maintenance history, time-to-setpoint achieved) that predicts pre-cool time for a specific unit under specific conditions. At load planning time, the planner selects the assigned unit and origin, and receives a predicted pre-cool completion time that accounts for that unit's actual performance history. Driver departure is scheduled to arrive at the shipper 10 minutes after predicted pre-cool completion.

## Impact

Reduces driver detention at shipper docks — a direct cost center where carriers pay driver waiting time and may owe shipper detention fees. For a 100-driver fleet with current average 25 minutes of pre-cool-related detention per load, eliminating half of that detention recovers approximately $200,000 annually in driver time. Secondary benefit: improved shipper dock scheduling relationships.
