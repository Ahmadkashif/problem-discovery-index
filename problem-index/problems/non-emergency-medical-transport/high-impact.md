# Multi-Constraint Trip Scheduling and Route Optimization

**Industry:** [[non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** High Impact
**One-liner:** Every vehicle runs the right patients in the right order, honoring appointment windows, mobility constraints, and Medicaid authorization rules — without a dispatcher manually building each route.
**Tags:** #reinforcement-learning #gradient-boosting #regression #tabular-ml #workflow-orchestration #compliance #revenue-impact

## The Problem
NEMT operators receive 50-500 trip requests per day from Medicaid brokers, healthcare facilities, and direct patients. Each trip carries hard constraints: appointment time windows (often 15-minute pickup precision required by brokers), vehicle type compatibility (wheelchair van vs. stretcher vs. ambulatory sedan), patient-specific load/unload times that vary from 2 minutes for an ambulatory patient to 20 minutes for a bariatric stretcher patient, attendant requirements, and geographic clustering across metro and rural areas. Dispatchers currently build routes manually or with basic routing tools that treat all passengers identically, resulting in 15-25% of trips arriving outside the broker's on-time window — triggering financial penalties, lost contracts, and patient harm when dialysis or chemotherapy appointments are missed.

## Why It's Unsolved
Standard vehicle routing solvers (CVRP variants) optimize distance and time but cannot natively encode the heterogeneous constraints of NEMT: a single route may mix wheelchair and ambulatory patients, each with different dwell times at pickup and dropoff, and the vehicle's effective capacity changes mid-route as equipment configurations shift. Patient no-show rates of 15-20% require real-time re-optimization, not just static morning route plans. Medicaid authorization rules vary by state and broker, adding compliance constraints (e.g., maximum shared-ride time, allowable detour miles) that generic routing engines do not model. The data needed to accurately predict per-patient dwell time — mobility level, facility layout, time of day, weather — lives in dispatcher knowledge, not in structured databases.

## What a Solution Looks Like
A scheduling engine ingests trip requests with patient profiles, predicts per-trip time requirements using a gradient-boosted model trained on historical trip data (actual vs. scheduled times by patient mobility category, facility, and time of day), then feeds these predictions into a reinforcement-learning-based route optimizer that jointly minimizes fleet miles, maximizes on-time performance, and respects all Medicaid compliance constraints. The system re-optimizes in real time as no-shows, cancellations, and add-on trips arrive throughout the day, pushing updated routes to driver tablets. Dispatchers shift from route builders to exception handlers.

## Impact If Solved
On-time performance improves from 75-85% to 95%+, directly protecting broker contracts worth $500K-$5M annually per operator. Fleet utilization increases 20-30% by eliminating dead miles and fitting more trips per vehicle per day, translating to $200K-$800K in annual revenue lift for a 30-vehicle fleet without adding vehicles.
