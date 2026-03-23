# ML-Calibrated Estimating from Historical Job Data

**Niche:** [[niches/printing-shops/print-estimating-departments/profile|Print Estimating Departments]]
**Industry:** [[industries/printing-shops|Printing Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No estimating tool learns from the shop's actual production data to improve future estimates — MIS systems use static production standards that the estimator adjusts by feel, while historical job data (quoted cost vs. actual cost) sits unused in the database.
**Tags:** #gradient-boosting #linear-regression #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced print estimator carries a mental model of how their specific shop performs: "our 4-color makeready on the 40-inch press actually takes 35 minutes, not the 25 minutes in the standard, because our pressman takes extra time on color matching" or "folding jobs on the Stahl take 15% longer than standard because the feeder is temperamental." This calibrated knowledge — the gap between MIS production standards and actual shop performance — takes 5-10 years to develop and is the difference between accurate and inaccurate pricing. When the estimator retires, the successor uses the same MIS standards but lacks the calibration, producing estimates that are systematically off by 5-15%.

## Why Nobody Has Built This
MIS vendors view estimating as a configuration problem (set the right production standards) rather than a learning problem (calibrate standards from actual production data). The historical data — quoted time versus actual time, quoted cost versus actual cost, by job type — exists in MIS databases but is rarely analyzed systematically. Building a calibration model requires joining estimating data (quoted standards by cost category) with actual production data (actual time and material consumption by job) and computing the systematic variance by job type, press, and operation. MIS vendors have this data but have not built the feedback loop.

## What to Build
A calibration engine that connects to the shop's MIS, analyzes 1-2 years of historical job data (estimated versus actual by cost category — press time, makeready time, finishing time, material consumption), identifies systematic estimation errors by job type/press/operation, and adjusts the estimating standards used for future quotes. The estimator sees calibrated standards ("our 4-color makeready on Press 2 averages 33 minutes, not the 25-minute default") and confidence ranges ("this job type has high variance — quote conservatively"). The system updates continuously as new actual data flows in.

## Target Customer
Lead estimators and owners at commercial print shops with 1+ years of job history in their MIS (actual production tracking enabled). Approximately 3,000-5,000 US shops running EFI Pace or Avanti with actual tracking. Average contract value: $15-30K/year.

## Impact If Built
Estimating accuracy improves by 5-10% of total job cost. Margin protection improves — the shop stops systematically under-pricing the job types where actual cost exceeds the standard. New estimator ramp time decreases from 5-10 years to 6-12 months because the calibrated standards encode the previous estimator's knowledge.
