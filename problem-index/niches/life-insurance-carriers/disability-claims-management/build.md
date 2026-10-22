# Return-to-Work Uplift Targeting

**Niche:** [[niches/life-insurance-carriers/disability-claims-management/profile|Disability Income Claims Management]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carriers predict which disability claims will run long; what they need is to know which claimants a call, a nurse or a job accommodation would actually help.
**Tags:** #survival-analysis #causal-inference #gradient-boosting #large-language-models #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide each disability claim on a complete, organised medical file before its ERISA deadline and to return more claimants to work, and whoever shortens average claim duration without raising the appeal-overturn and litigation rate takes the account.

## The Problem
Duration models flag long claims, and resources go to them. But many flagged claimants would not recover with any intervention, and some unflagged ones would return quickly with modest help. Nurse case managers and vocational specialists are scarce, and assigning them by predicted duration wastes them.

## Why Nobody Has Built This
Uplift needs evidence about interventions, and carriers rarely randomise who gets one. Clinical and functional detail sits in unstructured records. Claims operations measure caseload throughput, not intervention effect.

## What to Build
Extraction of restrictions, limitations, treatment and prognosis from records into features; a survival model of duration; and an uplift model trained on natural variation and small randomised pilots, estimating the change in return-to-work probability from each intervention type. The output is a weekly intervention list for each examiner and case manager.

## Target Customer
VPs of disability claims and clinical/vocational resource leaders at group LTD writers.

## Impact If Built
The same intervention budget returns more claimants to work. That shortens durations, lowers reserves and improves claimants' lives, and the uplift test shows which part is real.
