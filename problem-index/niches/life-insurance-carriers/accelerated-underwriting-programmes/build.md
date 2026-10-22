# Continuous Slippage Monitor for Accelerated Programmes

**Niche:** [[niches/life-insurance-carriers/accelerated-underwriting-programmes/profile|Accelerated Underwriting Programmes]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Accelerated programmes are re-priced on a slippage estimate made once a year from a few hundred audited cases, while the applicant mix and data feeds change monthly.
**Tags:** #survival-analysis #causal-inference #change-point-detection #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to issue more applicants without fluids, exams or an APS while keeping audited mortality slippage inside the pricing load, and whoever proves the highest straight-through rate at a slippage the reinsurer will sign off takes the account.

## The Problem
Slippage is the extra mortality from cases the accelerated path places in a better class than full underwriting would. It is estimated from random holdouts and post-issue audits, which are small per segment, and the estimate is refreshed annually. Meanwhile marketing shifts the channel mix, a data vendor changes a score version, and producers learn which answers pass triage. The SOA's 2019 survey found carriers assuming ~1%–10% higher mortality where requirements were waived, a wide range for a number that prices a whole book.

## Why Nobody Has Built This
Data vendors monitor their own scores, reinsurers monitor treaties annually, and carriers' actuarial teams are busy with valuation. The audited sample is the bottleneck, and nobody has designed the sampling to support continuous inference.

## What to Build
A monitor that treats each audited case as evidence on a class-shift matrix by segment, updates slippage with credible intervals monthly, and projects the mortality load through class-specific survival curves. It watches triage inputs and pass rates for change points (a score version, a channel launch, producer gaming) and recommends holdout sample sizes where uncertainty is widest.

## Target Customer
Heads of accelerated underwriting and their reinsurers' programme actuaries.

## Impact If Built
Programmes can widen eligibility with evidence and pull back within weeks when something drifts, instead of discovering a slipped cohort in a claims study years later.
