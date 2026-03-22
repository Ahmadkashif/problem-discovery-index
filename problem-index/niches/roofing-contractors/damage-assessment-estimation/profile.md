# Damage Assessment & Estimation

**Parent Industry:** [[industries/roofing-contractors|Roofing Contractors]]
**Category:** Highly Automatable

## Profile
**Market Size:** $3-5B (embedded across roofing segments)
**Share of Parent Industry:** Embedded function — damage assessment and estimation are performed on every roofing job, but the tools and services supporting these functions represent $3-5B in annual spend across measurement services (EagleView), estimation software (Xactimate), drone equipment, and inspection labor.
**Digital Adoption:** Medium — EagleView and Xactimate are widely adopted, but the critical step between measurement (automated) and estimate (manual Xactimate entry) involves human judgment that remains entirely manual. Drone usage is growing but standardized capture protocols and automated analysis are absent.
**Target Buyer:** Roofing company estimator, damage inspector, or operations manager responsible for drone program and estimation accuracy
**Automation Potential:** Very High — Damage classification from imagery is a well-defined computer vision problem, material estimation from measurements is algorithmic, and waste calculation can be optimized beyond human heuristics

## What Makes This a Distinct Niche
Damage assessment and estimation is the function that converts a lead into a priced job, and its accuracy determines both close rate and profitability. The workflow: measure the roof (solved by EagleView), assess the condition (unsolved — human judgment), price the repair or replacement (partially automated by Xactimate pricing data, but scope determination is manual), and calculate materials with waste factors (manual heuristics). The damage assessment step is where the most value and the most error live. An experienced inspector classifies damage type (hail, wind, aging, foot traffic, mechanical), determines severity (cosmetic, functional, replacement-required), maps affected areas, and translates findings into Xactimate line items — all in 20-40 minutes on the roof. This is pure tacit knowledge: the inspector has seen thousands of roofs and can distinguish a 1-inch hail hit from a blister from a manufacturing defect in seconds. Material waste calculation is another judgment call — experienced estimators know that a complex hip roof with 12 facets and 6 valleys needs 18-20% waste factor while a simple gable needs 10-12%, but these numbers come from experience, not calculation.

## Current Tools & Gaps
EagleView dominates measurement with satellite and aerial imagery delivering accurate dimensions, pitch, and facet geometry. Xactimate provides pricing data for insurance-scope estimating. CompanyCam handles photo documentation. DJI and Skydio drones are increasingly used for roof-level imagery. The gap is between EagleView's measurement output and Xactimate's scope input — no tool bridges this gap with automated damage classification, severity scoring, or intelligent waste factor calculation. Material estimation from scope is partially handled by supplier ordering systems but without optimization. The industry has measurement, has pricing, but lacks automated assessment.

## Problems
- [[niches/roofing-contractors/damage-assessment-estimation/build|🔨 Build: AI Damage Classifier with Severity Scoring]]
- [[niches/roofing-contractors/damage-assessment-estimation/buy|🛒 Buy: EagleView Condition Assessment Integration]]
- [[niches/roofing-contractors/damage-assessment-estimation/fix|🔧 Fix: Material Waste Calculation Accuracy]]
