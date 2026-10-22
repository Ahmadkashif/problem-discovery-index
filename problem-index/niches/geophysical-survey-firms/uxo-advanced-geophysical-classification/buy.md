# Model Registries Adapted to Classification Evidence

**Niche:** [[niches/geophysical-survey-firms/uxo-advanced-geophysical-classification/profile|UXO Advanced Geophysical Classification]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine-learning teams already version every model, dataset and decision in tools like MLflow; munitions classification teams reconstruct the same lineage for QAPP reviewers by hand.
**Tags:** #evaluation-metrics #hypothesis-testing #data-integration #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to cut digs of harmless debris while holding DoD's zero-missed-target line, and whoever delivers the shortest defensible dig list under DAGCAP accreditation takes the munitions response task order.

## The Problem
A classification decision must be defensible: which sensor data, which inversion settings, which library version, which classifier and threshold, which QC seeds passed. Reviewers and DAGCAP assessors ask for it; teams assemble it from processing logs and spreadsheets.

## What Already Exists
MLflow, Weights & Biases and similar experiment trackers record model versions, parameters and metrics; UX-Analyze records inversion results within its database.

## The Customization Gap
The adaptation needs: lineage from each dig-list row back to the raw sensor file, inversion parameters, library version and classifier; QC seed results attached to the data they validate; threshold decisions recorded with their justification; formatted outputs matching DAGCAP and QAPP deliverable tables; and immutable records for long-term DoD retention.

## Target Customer
Quality managers and classification leads at accredited contractors.

## Impact If Solved
Review cycles shortened and assessments passed with records produced as a by-product of the work.
