# Patient Outcome Tracking and Treatment Plan Optimization

**Industry:** [[chiropractic-practices|Chiropractic Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic outcome tracking tools can administer patient surveys, but they don't know that a chiropractic treatment plan for lumbar radiculopathy should show measurable Oswestry Disability Index improvement by visit 6 — and that if it doesn't, the treatment approach needs to change, not just continue for another 12 visits.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #linear-regression #descriptive-statistics #expectation-variance-covariance #bias-variance-tradeoff

## The Problem
Chiropractic treatment plans are typically set at the initial exam (e.g., "3x/week for 4 weeks, then 2x/week for 4 weeks, then 1x/week for 4 weeks") and followed without systematic outcome monitoring. The DC asks "how are you feeling?" at each visit, but subjective patient responses don't provide the objective data needed to determine whether the treatment approach is working, needs modification, or should be discontinued. Validated outcome measures (Oswestry Disability Index for low back, Neck Disability Index for cervical, PROMIS-29 for general function) exist but are rarely administered systematically. Without outcome data, treatment plans either continue too long (patient plateaus but keeps coming because they feel incrementally better) or end too early (patient is discharged at the end of the predetermined plan without verifying goal achievement).

## What Already Exists
PatientIQ, FOTO, and CareConnections provide outcome measurement platforms for physical therapy and rehabilitation. ChiroTouch and Jane App offer basic outcome forms. No system integrates chiropractic-specific outcome measures into the treatment workflow with decision support — alerting the DC when a patient is not responding as expected for their condition and demographics, and suggesting treatment plan modifications based on outcomes data from similar patients.

## The Customisation Gap
A chiropractic outcome system needs to: (1) administer condition-specific validated outcome measures at protocol-defined intervals (initial, visit 6, visit 12, discharge), (2) benchmark patient progress against expected recovery curves for their condition, age, chronicity, and presentation severity, (3) alert the DC when a patient is significantly below expected progress — triggering a re-examination or treatment approach modification, (4) generate progress reports formatted for insurance medical necessity documentation, and (5) provide practice-level analytics showing which treatment approaches produce the best outcomes for which conditions.

## Impact If Solved
Reduces average treatment course length by 15-20% by identifying non-responders earlier and modifying treatment. Improves patient outcomes by 10-15% through data-driven treatment plan adjustments. Generates objective progress data that supports insurance medical necessity documentation, reducing denial rates. Provides the practice-level outcomes data needed to participate in value-based care contracts.
