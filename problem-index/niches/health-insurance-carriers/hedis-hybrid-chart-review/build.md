# Predicting Which Office Holds the Qualifying Record

**Niche:** [[niches/health-insurance-carriers/hedis-hybrid-chart-review/profile|HEDIS Hybrid Chart Review & Stars Measurement]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Chase lists send each sampled member's chart request to the attributed primary care office, when the qualifying blood pressure or screening is often documented somewhere else.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to retrieve and abstract every sampled chart for the hybrid measures before the June HEDIS submission, and whoever closes the most numerator hits that pass the auditor's medical record review validation takes the account.

## The Problem
A retrieved record that holds no qualifying evidence costs a retrieval fee, an abstractor's time and, worst of all, weeks of the season. The evidence for a diabetic member's HbA1c may be at the endocrinologist; a blood pressure may be in an urgent care visit; a cervical screening may be at a women's health clinic. Plans have years of history showing where hits were found, and rarely use it to route requests.

## Why Nobody Has Built This
Retrieval vendors are paid per chart retrieved, not per hit. Plans' abstraction results are stored as measure outcomes, not as "evidence found at provider X". And the season is too compressed to experiment.

## What to Build
A model trained on prior seasons' abstraction results and claims. For each sampled member and measure, it ranks the providers most likely to hold qualifying evidence, using visit types, specialties, lab claims, the timing of visits in the measurement year and each office's historical response time. Requests go to the top-ranked sources first, and a second request is triggered automatically when the first record comes back empty.

## Target Customer
HEDIS operations directors at MA, Medicaid and Marketplace plans, and the retrieval vendors serving them.

## Impact If Built
Higher hit rates per retrieved chart, earlier completion and ~20%–30% fewer wasted retrievals (estimate), with the chase finished weeks before the deadline.
