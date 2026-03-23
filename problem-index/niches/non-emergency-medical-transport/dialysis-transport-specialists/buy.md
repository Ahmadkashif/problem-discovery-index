# Standing Order Route Optimizer for Recurring Trips

**Niche:** [[niches/non-emergency-medical-transport/dialysis-transport-specialists/profile|Dialysis Transport Specialists]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Route optimization tools rebuild routes daily from scratch, but dialysis trips are 80% recurring standing orders that should be optimized once and adjusted incrementally.
**Tags:** #reinforcement-learning #gradient-boosting #regression #tabular-ml #workflow-orchestration

## The Problem
A 30-vehicle NEMT fleet transporting 200 dialysis patients 3x/week runs roughly 600 recurring trips per week to the same facilities at the same times. Yet dispatchers rebuild routes every morning using software that treats each day as independent, ignoring that Monday's optimal route structure is nearly identical to the previous Monday's. The daily rebuild takes 2-3 hours, produces inconsistent routes (the same patient gets different drivers each time, disrupting the relationship), and fails to account for the fact that the standing order schedule has inherent optimization patterns that a one-time master route design could capture.

## What Already Exists
RouteGenie, RoutingBox, and generic VRP solvers (Google OR-Tools, OptaPlanner) optimize daily routes. NEMT dispatch platforms (TripMaster, CTS) manage daily scheduling. Calendar-based scheduling tools handle recurring appointments. None of these specifically handle the standing-order structure of dialysis transport, where the goal is not daily re-optimization but master route optimization with daily exception handling (patient cancellation, substitute driver, vehicle breakdown).

## The Customization Gap
Dialysis transport routing needs a two-tier optimization: (1) a master route plan optimized for the recurring weekly schedule, assigning consistent driver-patient pairings and vehicle routes, and (2) a daily exception handler that adjusts the master plan for that day's changes (patient no-show, driver absence, add-on trips) without rebuilding from scratch. The master plan optimization runs weekly or when the patient roster changes; the daily handler runs in minutes. This structure preserves patient-driver relationships (critical for medically fragile patients), reduces dispatcher planning time, and produces more stable routes.

## Target Customer
NEMT dispatchers managing 100+ recurring dialysis trips per week who spend 2-3 hours daily rebuilding routes that are 80% identical to the previous day's.

## Impact If Solved
Cuts daily route planning time from 2-3 hours to 20-30 minutes of exception handling, improves patient-driver consistency from 40-50% to 85-90% same-driver rates, and reduces total fleet miles by 10-15% through master route optimization versus daily ad-hoc routing.
