# Ambient Capture That Writes Flowsheet Rows, Not Notes

**Niche:** [[niches/general-hospitals/bedside-nurses-med-surg/profile|Bedside Nurses on Med-Surg Units]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Nursing documentation is hundreds of structured flowsheet values per shift, and speech-to-note tools built for physicians produce prose nobody can chart from.
**Tags:** #transformers #large-language-models #seq2seq #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to cut the bedside nurse's documentation time without degrading the flowsheet data that quality measures, audits and billing depend on, and whoever gives back the most charting minutes per shift with audit-clean flowsheets takes the account.

## The Problem
During a head-to-toe assessment a nurse observes dozens of values: neuro checks, lung sounds, skin integrity, pain score, IV site, drain output, fall-risk factors. Each belongs in a specific flowsheet row with allowed values, timed and attributed. She charts them later by clicking through screens.

## Why Nobody Has Built This
Mapping speech to a hospital's own flowsheet build (thousands of rows, local value lists) is a structured-extraction problem, not summarisation. Errors land in measures (falls, pressure injuries, pain reassessment) that are audited, and each hospital's build differs.

## What to Build
Capture that listens during care and proposes flowsheet entries mapped to the hospital's row identifiers and value lists, with timestamps and confidence. The nurse confirms each block with one tap. It learns each unit's build and the nurse's phrasing, and refuses to fill rows it did not hear. Accuracy is reported by row against a nurse-verified sample. Every entry keeps the time it was observed at the bedside, separate from the time it was confirmed. Ambient capture changes when charting happens, and deterioration models that read nurses' documentation timing (the industry's [[problems/general-hospitals/high-impact|high-impact problem]]) would otherwise lose their signal and need retraining.

## Target Customer
CNIOs at Epic and Oracle hospitals with nurse-retention programmes funded by contract-labour savings.

## Impact If Built
Saving ~30 minutes per nurse per shift (estimate) across 1,000 nurses returns ~180,000 hours a year to care or to going home on time.
