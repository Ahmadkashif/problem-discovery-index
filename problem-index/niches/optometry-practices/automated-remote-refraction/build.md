# Final-Prescription Model from Objective Measurements

**Niche:** [[niches/optometry-practices/automated-remote-refraction/profile|Automated & Remote Refraction]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A model that predicts the final prescription an experienced optometrist would write from autorefraction, aberrometry, the old glasses and the patient's age and task, and learns from remakes.
**Tags:** #tacit-knowledge-ml #gradient-boosting #random-forests #feature-engineering #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to produce final spectacle prescriptions without the optometrist's full manual refraction, and whoever has the fewest prescription-related remakes per hundred refractions takes the account.

## The Problem
Objective measurements get close to the right prescription but not close enough. The experienced OD makes adjustments for adaptation, comfort and task, and those adjustments are what prevent remakes. Automated systems lack them.

## Why Nobody Has Built This
The adjustments are tacit and vary by doctor. Remake data sits with the optical lab or the practice's dispensing records and is rarely linked to the refraction that produced it. Device makers sell hardware and do not see outcomes.

## What to Build
A gradient-boosted model per prescription component trained on paired objective measurements, prior glasses and the OD's final prescription, weighted by whether the glasses were remade. The model proposes a final prescription and a confidence, and routes low-confidence patients to a full subjective refraction. It is retrained on each practice's remakes.

## Target Customer
Rollups and groups short of optometrists, and automated refraction device makers looking for a software edge.

## Impact If Built
If technician-led refraction with the model saves ~5 OD minutes per routine exam without raising remakes, a practice doing ~4,000 refractions a year frees ~330 OD hours (estimate).
