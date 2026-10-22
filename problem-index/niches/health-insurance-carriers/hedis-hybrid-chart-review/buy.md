# Clinical Document Extraction Tuned to HEDIS Specifications

**Niche:** [[niches/health-insurance-carriers/hedis-hybrid-chart-review/profile|HEDIS Hybrid Chart Review & Stars Measurement]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** General clinical NLP services already extract vitals, labs and procedures from notes; HEDIS abstraction needs them filtered through each measure's exact rules on dates, settings and exclusions.
**Tags:** #bert #transformers #large-language-models #evaluation-metrics #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to retrieve and abstract every sampled chart for the hybrid measures before the June HEDIS submission, and whoever closes the most numerator hits that pass the auditor's medical record review validation takes the account.

## The Problem
An extraction service can find "BP 128/82" in a note. HEDIS needs the most recent reading in the measurement year, not from an acute inpatient or emergency setting, with both values present, and taken on the same date when several were recorded. Exclusions such as hospice or frailty must also be found. Generic extraction leaves the abstractor applying all of this by hand.

## What Already Exists
Cloud clinical NLP services and medical document AI, plus the abstraction modules of HEDIS engines.

## The Customization Gap
The plan needs measure logic layered over extraction: date windows, setting rules, value tests, most-recent selection and exclusion criteria, updated with each year's specifications. It also needs a confirmation interface showing the evidence with page and line, and capture of every confirmation and rejection for retraining. Finally, it needs output in the format the HEDIS engine and the auditor's over-read expect.

## Target Customer
Quality and HEDIS operations teams at plans that abstract in-house or supervise offshore abstraction.

## Impact If Solved
Abstractors confirm rather than search, throughput rises ~2–3× per abstractor (estimate), and every hit carries its evidence for the auditor.
