# Violation-to-Crash Outcome Linkage as a Scoring Foundation

**Niche:** [[niches/charter-bus-operators/driver-risk-data-providers/profile|Commercial Driver Risk Data Providers]]
**Industry:** [[industries/charter-bus-operators|Charter Bus Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The scores sold to insurers rest on how violations are weighted, the weights were set by judgment and convention years ago, and the firm holds the outcome data that would settle whether they are right.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #cross-validation #confidence-intervals #causal-inference #data-integration #revenue-impact

## The Problem
A driver risk score converts a record of violations into a prediction about future crashes. The conversion is a set of weights: how much a speeding citation counts against a following-too-close, how quickly a violation should decay, how a suspension compares to three moving violations. Those weights came from a mix of actuarial convention, regulatory scoring frameworks, and expert judgment, and they have largely stayed put. Meanwhile the firm has been monitoring the same drivers for years and observing what happened to them. The dataset that would tell it which violation types actually predict crashes, at what horizon, and for which populations sits in its own systems, joined to nothing. The product's central claim — that this score is predictive — is defended by construction rather than by evidence.

## Why Nobody Has Built This
Crash outcomes are the hard half. They arrive from different sources than violations, with different identifiers and reporting lags, and reportable crash definitions vary by state, so building a reliable outcome label is a substantial data engineering problem before any modelling starts. There are also legitimate constraints on how driving record data may be used, which vary by state agreement and by permissible purpose, and nobody has systematically mapped which analyses each agreement allows — so the safe default has been to use the data only for the monitoring it was licensed for. And a scoring change ripples into insurance pricing and employment decisions, which makes any recalibration a governance event rather than a model update.

## What to Build
An outcome-linked scoring foundation. Violation histories are joined to crash and claim outcomes wherever the linkage is obtainable, with the join quality itself measured rather than assumed, and every record carrying the use terms of the agreement it came from so any analysis can state what it is entitled to use. On that base, the weights become empirical: which violation types predict crashes and over what horizon, how predictive power decays with time since violation, where the current weighting is materially miscalibrated, and how all of that differs between passenger carriage, long-haul freight, and local delivery — populations the industry currently scores with substantially the same model. Calibration is the priority over discrimination, because an insurer pricing on the score needs the stated risk to mean what it says. And because scoring changes are governance events, the system's output is evidence for a recalibration decision, with the effect on the existing book quantified before anything ships.

## Target Customer
Chief data officers and VPs of risk products at driver monitoring bureaus running 100-500 staff, and the underwriting leaders at insurer clients who price on these scores and currently have no independent validation of them.

## Impact If Built
Replaces the product's core assertion with a measured one, in a market where competitors sell substantially the same raw monitoring and differentiate only on the score. Demonstrated predictive validity, by segment and horizon, is the strongest available commercial claim and the one no competitor without the same longitudinal record can match. It also derisks the firm's exposure to the fairness scrutiny that scoring products in employment-adjacent uses increasingly attract.
