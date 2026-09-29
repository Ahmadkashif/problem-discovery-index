# Valuation Explainability Adapted to Regulatory Defence

**Niche:** [[niches/auto-body-shops/total-loss-valuation-providers/profile|Total Loss Valuation Providers]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Model explainability tooling produces feature attributions for data scientists; what a market conduct examiner needs is a narrative reconstruction of why these six vehicles were chosen and those four were not, three years after the settlement.
**Tags:** #evaluation-metrics #feature-engineering #gradient-boosting #logistic-regression #large-language-models #transformers #compliance #data-integration #workflow-orchestration #automation

## The Problem
A valuation is a regulated determination that must remain defensible long after it is issued. The obligation is not "which features mattered" but "why this specific set of comparables, with these adjustments, under the methodology in force on that date." Answering it today means reconstructing the state of the system as it was — the listing inventory available that week, the rule configuration then deployed, the adjustment tables then in effect — from logs and deployment records, by hand, for one claim at a time. Under a market conduct examination covering a sample of hundreds of claims, this becomes the dominant cost of the exam, and the reconstruction is slow enough that the answer is sometimes a reasonable approximation rather than the actual record.

## What Already Exists
Model governance is a well-supplied market. SHAP and LIME cover attribution; Fiddler, Arthur, and Arize provide monitoring, drift detection, and explanation serving; the MLOps platforms handle model registries, lineage, and versioned artifacts; the model risk management suites built for banking cover documentation and validation workflow comprehensively. Every component of the technical answer exists as a product.

## The Customization Gap
All of it is built to explain a model, and a valuation is not produced by a model alone. It is produced by a pipeline: an inventory of available listings at a point in time, a rule-based eligibility filter, a selection step, an adjustment table, and analyst overrides. The most consequential question an examiner asks — which candidate vehicles were excluded and on what basis — concerns the filter, not the model, and no explainability product addresses it because filters are considered plumbing. The adaptation needed is determination-level reproducibility across the whole pipeline: every valuation pinned to the exact inventory snapshot, rule version, adjustment table, and override that produced it, replayable on demand. On top of that, explanation rendered in the register the audience uses — a written account naming the excluded candidates and the exclusion reason, the adjustments applied and their source, expressed in the terms of the state regulation governing that settlement. And retention on a regulatory horizon of years rather than the weeks typical of monitoring tools.

## Target Customer
Chief compliance officers and heads of valuation at total loss providers, and the regulatory affairs teams at insurer clients who field examinations on determinations they did not compute.

## Impact If Solved
Turns examination response from a project into a query, which matters most in the states with the most aggressive market conduct programs. It also removes a quiet constraint on the product: methodology improvements are currently slowed by the difficulty of explaining any additional complexity to a regulator, and reproducibility infrastructure raises the ceiling on how sophisticated the valuation can defensibly become.
