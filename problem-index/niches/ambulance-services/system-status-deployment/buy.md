# Field Service Optimisation Taught 911 Coverage

**Niche:** [[niches/ambulance-services/system-status-deployment/profile|System Status Management & 911 Unit Deployment]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Field service scheduling optimises routes to known jobs; ambulance deployment positions idle units for jobs that have not happened yet, so that no zone is left without one.
**Tags:** #optimization-fundamentals #time-series-forecasting #dynamic-programming #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to keep an available ambulance within reach of every zone of a county 911 contract around the clock, with the unit-hours the contract funds, and whoever has the fewest priority-1 calls arriving when the zone has no available unit (level-zero calls) per 1,000 priority-1 responses takes the account.

## The Problem
Operators want optimisation they can trust, but most optimisation software assumes the jobs are known in advance.

## What Already Exists
Field service management and routing platforms (Salesforce Field Service, ServiceTitan's dispatch board, OptimoRoute), CAD posting modules from public safety vendors, and drive-time mapping tools.

## The Customization Gap
Ambulance deployment needs availability optimisation: keeping an unassigned unit within reach of each zone given forecast demand, and counting the level-zero calls when it fails. It also needs the contract's rules (zones, priority definitions, response standards), hospital wall time as a stochastic delay, crew shift and meal-break rules, and the scheduled interfacility runs sharing the fleet. Moves must be recommended in seconds, inside CAD, with drive times under lights and sirens.

## Target Customer
Operators' communications and operations directors, and the CAD vendors that would embed the logic.

## Impact If Solved
Moving a static operator to dynamic deployment is where Medicare's cost survey found the gap: $1,524 against $636 mean cost per transport, in 2022 dollars (MedPAC, June 2026). Closing even a tenth of that gap on 50,000 transports a year is worth ~$4.4M, money an operator can spend on the unit-hours that keep zones out of level zero.
