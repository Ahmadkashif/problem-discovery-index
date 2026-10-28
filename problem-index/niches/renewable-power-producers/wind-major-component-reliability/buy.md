# Aircraft Engine Health Monitoring for Wind Drivetrains

**Niche:** [[niches/renewable-power-producers/wind-major-component-reliability/profile|Wind Turbine Major Component Reliability]]
**Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Aircraft engine makers and airlines have trended engine parameters against fleet baselines for decades to schedule removals before failure; a wind drivetrain is a rotating machine with the same problem and far less instrumentation.
**Tags:** #autoencoders #survival-analysis #time-series-forecasting #feature-engineering #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to catch drivetrain and main-bearing damage early enough to repair it uptower, and whoever has the fewest crane-dependent major component replacements per 100 turbines takes the account.

## The Problem
Wind owners need early, trusted warnings of drivetrain failure across mixed fleets, and current alerts are noisy.

## What Already Exists
Engine health monitoring in aviation compares each engine's gas temperatures, vibration and fuel flow with a fleet baseline adjusted for flight conditions, ranks deterioration, and plans shop visits around it, with removal records feeding back as labels.

## The Customization Gap
The adaptation needs: wind speed, turbulence and yaw as the operating conditions to adjust for; ten-minute SCADA instead of continuous high-rate engine data on most turbines; main bearings, gearbox stages and generator bearings as the components; crane availability, weather windows and uptower repair options in the action plan; and work orders, which are far less structured than aviation removal records, as labels.

## Target Customer
Reliability engineering teams at IPPs and independent service providers.

## Impact If Solved
Raising the share of drivetrain failures caught with more than 30 days' warning from ~40% to ~70% (estimate) turns several crane jobs a year per 1,000 turbines into planned uptower work.
