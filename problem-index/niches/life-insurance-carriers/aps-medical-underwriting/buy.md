# Clinical Chart-Abstraction Tools Mapped to an Underwriting Manual

**Niche:** [[niches/life-insurance-carriers/aps-medical-underwriting/profile|Full Medical Underwriting & APS Review]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Health plans already pay for NLP that reads medical charts to find coded conditions; life underwriting needs the same reading with a different rulebook at the end.
**Tags:** #large-language-models #bert #transformers #feature-engineering #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to turn an attending physician statement into a defensible risk class in days rather than weeks, and whoever cuts APS-to-decision time without moving class agreement on blind re-underwriting takes the account.

## The Problem
Underwriters read whole files to find the handful of findings the manual cares about. Clinical abstraction is a solved category elsewhere: health plans and their vendors run chart-review NLP at scale for risk adjustment and quality measures.

## What Already Exists
Chart-abstraction and risk-adjustment coding tools that extract diagnoses, labs and medications from clinical documents and map them to HCC and ICD codes, with coder review queues.

## The Customization Gap
Life underwriting needs: mapping to the underwriting manual's impairments and debits rather than payment codes; trend extraction across serial results (blood pressure, A1c, ejection fraction); detection of follow-up gaps and non-adherence; handling of faxed, handwritten and out-of-order pages; a worksheet output the workbench accepts; and audit trails suitable for model-governance reviews under New York and Colorado rules.

## Target Customer
Underwriting operations leaders who want a proven document engine rather than a pilot from scratch.

## Impact If Solved
Reading time per APS falls substantially (estimate: by half on long files), with a reviewable extraction underwriters can trust.
