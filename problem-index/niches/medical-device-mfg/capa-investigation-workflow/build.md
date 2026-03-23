# ML-Assisted CAPA Root Cause Hypothesis Engine

**Niche:** [[niches/medical-device-mfg/capa-investigation-workflow/profile|CAPA Investigation Workflow]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product analyzes a new CAPA's complaint/nonconformance description and automatically surfaces the most probable root cause hypotheses based on similar historical CAPAs, correlated production parameters, and supplier quality trends — cutting investigation time from weeks to days.
**Tags:** #bert #gradient-boosting #tacit-knowledge-ml #compliance #automation

## The Problem
When a quality engineer opens a new CAPA (triggered by a complaint, nonconformance, or audit finding), the first task is generating root cause hypotheses — informed guesses about what went wrong, which the investigation will then confirm or eliminate. An experienced quality engineer does this by recognizing patterns: "this complaint description sounds like the failure mode we saw in CAPA-2023-047, which turned out to be supplier X's lot variability." A junior quality engineer lacks this pattern recognition and pursues root cause analysis blindly, taking 2-3x longer to reach the same conclusion. This tacit knowledge — the ability to read a complaint and immediately narrow the investigation to 2-3 probable root causes — is the highest-value skill in quality engineering and leaves with each departing quality engineer.

## Why Nobody Has Built This
Root cause analysis for medical devices requires correlating unstructured text (complaint narratives, investigation notes) with structured production data (process parameters, component lots, supplier metrics) across systems with different data models. NLP for complaint text analysis is tractable, but the correlation with production data requires data integration that is specific to each manufacturer's system architecture. Additionally, the output must be defensible in an FDA audit — the model's hypotheses must be traceable to evidence, not a black-box prediction.

## What to Build
A root cause hypothesis engine that (1) ingests the new CAPA's complaint/nonconformance description, (2) uses NLP to find similar historical CAPAs and their confirmed root causes, (3) queries production data for correlated parameters (component lots, process deviations, supplier changes) within the relevant time window, (4) generates ranked root cause hypotheses with supporting evidence links, and (5) presents the hypotheses as starting points for the quality engineer's investigation — not as conclusions. Each hypothesis includes the evidence trail that generated it, making it auditable.

## Target Customer
Quality Directors and CAPA Managers at device manufacturers with 50+ CAPAs per year. Approximately 500-700 US medical device manufacturers at this scale. Average contract value: $50-100K/year.

## Impact If Built
CAPA investigation time decreases from 45-90 days to 15-30 days. Quality engineer productivity doubles (manage 20-30 CAPAs simultaneously instead of 10-15). FDA 483 citations for inadequate CAPA investigation decrease by reducing the frequency of superficial root cause analyses.
