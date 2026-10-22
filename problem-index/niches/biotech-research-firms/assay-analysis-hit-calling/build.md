# Curve Triage That Learns From Every Refit

**Niche:** [[niches/biotech-research-firms/assay-analysis-hit-calling/profile|Plate-Based Assay Analysis & Hit Calling]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Scientists review every dose-response curve by eye, though most are unambiguous and the registry already holds years of their own corrections to learn from.
**Tags:** #gradient-boosting #bayesian-inference #maximum-likelihood-estimation #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn plate-reader output into curve fits and hit calls scientists accept without re-checking, with every masking and refit decision recorded, and whoever makes analysis both same-day and auditable takes the account.

## The Problem
After each run a scientist opens every curve, masks wells, refits, rejects or flags, then uploads. The judgement is real for perhaps one curve in five (estimate); the rest are clear. Results wait for the scientist's time, and the design meeting may run on last week's data.

## Why Nobody Has Built This
Curve-fitting tools fit; they do not decide. The training signal — historical masks, refits and rejections — sits in registries without reasons, and vendors have treated review as the user's job.

## What to Build
A triage model trained on the organisation's own history: curve-shape classification, recommended masks with the reason (edge well, outlier against replicate, solubility limit), Bayesian fits with credible intervals, and auto-acceptance above a threshold set from measured overturn rates. Scientists review only the ambiguous fraction, and each decision becomes a new labelled example.

## Target Customer
Heads of biology and discovery informatics at biotechs running weekly assay cascades.

## Impact If Built
Same-day results for the design meeting and a logged analysis, with scientist review concentrated on the curves that need it.
