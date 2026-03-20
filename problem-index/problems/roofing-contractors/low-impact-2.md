# Material Takeoff and Waste Factor Calculation from Aerial Measurement Reports

**Industry:** [[roofing-contractors|Roofing Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** EagleView and Nearmap provide accurate roof geometry measurements, but converting those measurements into a materials order with correct waste factors for each plane, hip, ridge, and valley configuration — accounting for the contractor's specific installation method and shingle product — requires a roofing-specific calculation layer that general estimating tools don't provide.
**Tags:** #arithmetic-and-basic-algebra #feature-engineering #automation #compliance #workflow-orchestration

## The Problem

Roofing material estimation is a precise calculation problem: each roof plane's area, plus waste factor for cuts at hips and rakes, plus ridge cap coverage, plus starter strip linear feet, plus underlayment overlap, plus ice-and-water shield area in applicable climate zones. An experienced estimator can perform this calculation accurately from an EagleView report in 15-20 minutes. A junior estimator makes errors — over-ordering (waste cost) or under-ordering (requiring mid-job material delivery that delays the crew). Material errors on a $20,000 job can cost $1,500–$3,000.

The waste factor calculation is non-trivial: a hip roof has different waste factors than a gable roof; a roof with multiple penetrations (skylights, chimneys, pipes) requires additional material for flashing and cuts; different shingle products have different exposure dimensions that affect coverage calculations.

## What Already Exists

EagleView ProContractor and Nearmap Property provide measurement reports with total area and facet-level breakdown. GAF's QuickMeasure integrates with AccuLynx for basic material calculation. None of these account for contractor-specific installation practices (e.g., a contractor who uses 4" vs. 6" overlap for ice-and-water shield, or who orders 15% vs. 12% waste factor depending on roof complexity score).

## The Customisation Gap

A roofing-specific takeoff tool needs: (1) input of the EagleView/Nearmap report geometry (facet areas, ridge/hip/valley linear feet, pitch by plane); (2) contractor-configured waste factor table by roof complexity tier; (3) product-specific coverage calculations (shingle product chosen → specific squares per bundle, starter strip → specific linear feet per bundle); (4) climate zone overlay (ice-and-water shield required by slope in applicable IRC climate zones). Output: a ready-to-submit material order with per-item quantities and current distributor pricing from the contractor's preferred supplier.

## Impact If Solved

Reduces material takeoff time from 15-20 minutes to under 3 minutes. Eliminates estimator-level errors in waste factor calculation — the most common source of mid-job material shortfalls. Enables apprentice estimators to produce accurate takeoffs on their first independent jobs.
