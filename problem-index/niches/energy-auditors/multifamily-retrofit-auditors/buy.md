# Unit Sampling Protocol and Extrapolation Engine

**Niche:** [[niches/energy-auditors/multifamily-retrofit-auditors/profile|Multifamily Retrofit Auditors]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistical sampling tools exist for survey research, but none are designed for multifamily energy audit unit sampling — determining which units to audit and how to extrapolate findings to the full building.
**Tags:** #bayesian-network #regression #tabular-ml #compliance

## The Problem
Auditing every unit in a 100-unit building is impractical — tenant access, time constraints, and cost make full-building audits prohibitive. Instead, auditors sample 10-20% of units, but the sampling methodology is ad hoc: some auditors choose units randomly, others pick the most accessible units, and others try to cover each floor plan type. The extrapolation from sampled units to building-wide energy characteristics is equally informal: if 3 of 10 sampled units had single-pane windows, the auditor assumes 30% of the building has single-pane windows — a statistically questionable conclusion that utility programs and building owners challenge. Programs like BPI Multifamily specify minimum sampling requirements but provide no computational tools to design the sample or calculate confidence intervals on extrapolated results.

## What Already Exists
Statistical sampling software (SAS, R packages, Qualtrics) designs survey samples with confidence intervals. Building stock assessment tools (DOE's Asset Score, CBECS) use sampling at the national level. Quality assurance sampling standards (ANSI Z1.4, MIL-STD-1916) define inspection sampling plans. None of these are adapted for the specific variables in multifamily energy audits (unit type, floor, orientation, occupancy pattern, in-unit equipment vintage).

## The Customization Gap
Multifamily auditors need a sampling protocol engine that: recommends which units to audit based on building characteristics (floor plan types, orientation exposure, floor level, renovation history), calculates the minimum sample size for desired confidence levels (e.g., "audit 15 units for 90% confidence on window condition"), generates stratified samples ensuring each unit type and orientation is represented, and extrapolates sampled findings to the full building with explicit confidence intervals that utility programs accept. The tool must integrate with the audit workflow — not be a separate statistical exercise.

## Target Customer
Multifamily energy auditors who currently design sampling plans informally and face utility program challenges to their building-wide extrapolations.

## Impact If Solved
Transforms multifamily sampling from ad hoc judgment to defensible methodology, reducing QA challenges by 40-60%. Auditors can justify smaller sample sizes (10-12% vs. 20%) with statistical rigor, saving 5-10 hours of field time per building without sacrificing accuracy.
