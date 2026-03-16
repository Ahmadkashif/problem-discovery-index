# Mixed Fleet Preventive Maintenance Scheduling

**Industry:** [[non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Fleet maintenance tools exist for homogeneous trucking fleets — but NEMT operators run wheelchair vans, stretcher vehicles, sedans, and WAVs with different maintenance profiles, and a single vehicle down on a Monday morning means patients miss dialysis.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml

## The Problem
A typical 30-50 vehicle NEMT fleet includes wheelchair-accessible vans (with hydraulic lifts requiring separate maintenance cycles), stretcher vehicles (with locking mechanism inspections mandated by DOT), sedans for ambulatory patients, and sometimes bariatric-capable vehicles with reinforced suspension. Each vehicle type has different maintenance intervals, different failure modes, and different consequences when pulled from service. Operators schedule maintenance reactively or on crude mileage intervals, leading to breakdowns during service hours that strand patients and trigger broker penalties for missed trips. Lift and ramp failures alone account for 30-40% of roadside breakdowns in wheelchair fleets.

## What Already Exists
Fleet management platforms like Fleetio, Samsara, and Azuga offer maintenance scheduling based on mileage or calendar intervals, with telematics integration for engine diagnostics. These tools work well for homogeneous over-the-road trucking fleets but treat all vehicles identically and cannot model the specialized maintenance needs of wheelchair lifts, stretcher locking systems, or the patient-safety-critical nature of NEMT equipment.

## The Customisation Gap
NEMT maintenance scheduling must incorporate vehicle-type-specific failure models (hydraulic lift cycle counts, ramp actuator wear, stretcher lock engagement frequency), patient impact scoring (a wheelchair van serves 8-12 patients/day vs. a sedan serving 12-18, but the wheelchair patients have no alternative), and broker penalty exposure (vehicles assigned to high-value broker contracts should be prioritized for preventive maintenance). A forecasting model trained on historical repair data, telematics signals, lift cycle counters, and daily utilization patterns can predict failure windows per vehicle and schedule maintenance during lowest-impact time slots — typically weekends or mid-week afternoons when trip volume dips.

## Impact If Solved
In-service breakdowns drop 40-60%, eliminating 2-4 patient-stranding incidents per month for a 40-vehicle fleet. Maintenance costs decrease 15-20% by shifting from reactive to predictive scheduling, saving $30K-$60K annually. Broker on-time compliance improves as vehicles are available when scheduled.
