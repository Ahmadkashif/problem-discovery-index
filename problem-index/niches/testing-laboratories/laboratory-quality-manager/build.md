# Measurement Uncertainty That Recalculates Itself From QC Data

**Niche:** [[niches/testing-laboratories/laboratory-quality-manager/profile|The Laboratory Quality Manager]]
**Industry:** [[industries/testing-laboratories|Testing Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Accredited labs must estimate the uncertainty of their results, and most do it once a year in a spreadsheet from data the LIMS collects every day.
**Tags:** #bayesian-inference #expectation-variance-covariance #confidence-intervals #change-point-detection #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep a lab continuously assessment-ready — corrective actions closed, uncertainty budgets current, every proficiency result answered — without the quality manager rebuilding the evidence before each visit, and whoever makes readiness continuous wins the quality budget.

## The Problem
Uncertainty estimates matter more than they used to: ISO/IEC 17025 requires labs to state the decision rule when they issue a pass or fail statement, and the rule depends on the uncertainty. Estimates are usually built from control-sample data, duplicates and proficiency results, but recalculated rarely, so a method whose precision has degraded since a column change carries last year's uncertainty on today's certificates.

## Why Nobody Has Built This
The inputs sit in the LIMS, the proficiency provider's portal and the quality manager's spreadsheet; the methods (top-down from QC data, bottom-up budgets) differ by sector; and quality managers are cautious about numbers they cannot reproduce by hand.

## What to Build
A service that pulls control-sample, duplicate and proficiency data per method and matrix, computes uncertainty by the lab's chosen approach, detects shifts in precision or bias since the last estimate, shows the calculation step by step for the quality manager to approve, and pushes approved values to report templates and decision rules.

## Target Customer
Quality managers at labs issuing statements of conformity — product, materials, food and environmental compliance testing.

## Impact If Built
Uncertainty that reflects the method as it performs today, defensible decision rules, and one of the most common assessment findings closed permanently.
