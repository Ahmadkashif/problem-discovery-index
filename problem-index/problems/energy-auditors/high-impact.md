# Building Energy Model Calibration from Audit Data

**Industry:** [[energy-auditors|Energy Auditors]]
**Type:** High Impact
**One-liner:** Savings projections become trustworthy enough that homeowners, contractors, and utility programs can fund retrofits with confidence instead of guesswork.
**Tags:** #gradient-boosting #gaussian-process #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Energy auditors collect field measurements — blower door results, insulation R-values, duct leakage, HVAC efficiency ratings, window specs — and feed them into modeling software (TREAT, Ekotrope, REM/Rate) to predict energy savings from proposed retrofits. The models routinely over-predict savings by 30-50% because they cannot account for occupant behavior, micro-climate effects, building geometry nuances, and the dozens of judgment calls an experienced auditor makes but never records. Experienced auditors mentally adjust their recommendations based on patterns they have seen across hundreds of buildings — noticing that a particular 1960s ranch floor plan always leaks more than the model predicts, or that a certain furnace brand degrades faster than its rated efficiency — but this calibration knowledge lives entirely in their heads and retires when they do.

## Why It's Unsolved
The core difficulty is data collection: capturing what an expert auditor *actually notices* during a walkthrough requires pairing audit outcomes (actual utility bill reductions post-retrofit) with the full context of the auditor's field observations, including the informal ones they never write down. Labeling is inherently noisy — actual savings depend on weather normalization, occupant behavior changes, and rate structure shifts that confound the signal. The few datasets that exist (DOE Weatherization Assistance Program evaluations, utility program measurement & verification data) are siloed across hundreds of local agencies with inconsistent schemas. Deployment is also challenging: the model must be faster and more transparent than the auditor's gut feel, or experienced auditors will ignore it and new auditors will not trust it.

## What a Solution Looks Like
A calibration layer that sits between raw audit data and the energy model, ingesting the standard field measurements plus historical performance data from completed retrofits. The model learns building-archetype-specific correction factors — effectively encoding the experienced auditor's mental adjustments — and outputs calibrated savings predictions with uncertainty bands. For each proposed retrofit measure, it provides a probability distribution of expected savings rather than a single point estimate, enabling risk-adjusted financing decisions.

## Impact If Solved
Retrofit close rates could increase 20-40% when savings projections are trusted enough to underwrite performance guarantees. The $5B weatherization market is currently bottlenecked not by demand but by credibility — accurate predictions unlock pay-for-performance contracts, green mortgage products, and utility program expansion.
