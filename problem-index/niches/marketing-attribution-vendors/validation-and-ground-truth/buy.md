# Forecast Verification Practice

**Niche:** [[niches/marketing-attribution-vendors/validation-and-ground-truth/profile|Validation & Experimental Ground Truth]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Weather forecasting built a whole science of verifying its own predictions and publishes its skill scores, and attribution vendors report how well their model fits its own training data.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #bayesian-inference #probability-distributions #monte-carlo-methods #descriptive-statistics #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to make experiments the ground truth and every model an interpolator between them — and whoever does that credibly makes their own error rate visible and resets the terms the whole category competes on.

## The Problem
Forecast verification is a mature science. Meteorology developed skill scores, calibration and sharpness measures, proper scoring rules and reliability diagrams, and publishes them — a forecaster's performance is a matter of public record and the field improved substantially because of it. The same practice exists in clinical prediction, credit risk and sports forecasting. Marketing measurement produces predictions that move budgets and reports in-sample fit, which is not verification in any sense the forecasting community would recognise.

## What Already Exists
Proper scoring rules and skill scores; calibration and reliability assessment; sharpness and resolution decomposition; verification against reference forecasts; and published performance records as a field norm.

## The Customization Gap
The adaptation is to a causal estimand with scarce ground truth. It requires: (1) verifying a causal quantity rather than a predicted observable, since the truth is a counterfactual that only an experiment reveals — this makes the verification set small and expensive where meteorology gets a new observation every day; (2) ground truth that is itself an estimate with its own uncertainty, so the comparison is between two uncertain quantities and naive error metrics overstate the model's failure; (3) no reference forecast equivalent to climatology, so a skill baseline must be constructed — last year's allocation is the honest candidate; (4) verification pooled across clients to reach usable sample sizes, which raises confidentiality questions meteorology never faces; and (5) commercial reluctance, since a published record invites comparison and the field norm that made meteorology honest does not exist here.

## Target Customer
Measurement vendors, client measurement functions, and industry bodies who could establish a verification norm.

## Impact If Solved
Meteorology improved because its skill scores are public, and attribution reports in-sample fit. Verifying a causal estimand against uncertain experimental ground truth is the adaptation, along with constructing the skill baseline the field has never defined.
