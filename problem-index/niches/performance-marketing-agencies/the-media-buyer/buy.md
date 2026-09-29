# Black Box Diagnostics Practice

**Niche:** [[niches/performance-marketing-agencies/the-media-buyer/profile|The Media Buyer After Automation]]
**Industry:** [[industries/performance-marketing-agencies|Performance Marketing Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Engineering has a mature practice for characterising systems you cannot open, and media buyers face one every day with no method at all.
**Tags:** #hypothesis-testing #causal-inference #confidence-intervals #gradient-boosting #evaluation-metrics #change-point-detection #monte-carlo-methods #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to give the buyer visibility and leverage inside a black box they are still accountable for — and whoever does that restores a profession the platforms hollowed out while keeping its responsibilities.

## The Problem
Characterising a system you cannot open is a real engineering discipline. System identification estimates a system's behaviour from its inputs and outputs; control theory designs interventions against an imperfectly known plant; sensitivity analysis establishes which inputs matter; and model-based testing probes behaviour systematically. These are taught, tooled and applied wherever a component's internals are unavailable. Media buyers face exactly this situation across billions of pounds of spend and approach it with intuition and forum posts.

## What Already Exists
System identification from input-output data; sensitivity analysis and design of experiments; control design under model uncertainty; change detection in system behaviour; and surrogate modelling of opaque components.

## The Customization Gap
The adaptation is to a system that is adversarial, non-stationary and shared. It requires: (1) a plant that is deliberately opaque and updated without notice by a party with different interests, so the identification must be continuous and robust to abrupt change — this non-stationarity is what makes the standard methods insufficient on their own; (2) experiments that cost real media spend, which sharply limits design of experiments and demands efficient sequential designs; (3) the same system serving thousands of advertisers simultaneously, which means cross-account observation is a legitimate and powerful identification channel unavailable in a single-plant setting; (4) an operator who is a marketer rather than an engineer, so the output must be a playbook rather than a transfer function; and (5) outcomes that are noisy and delayed, making the identification statistical rather than deterministic.

## Target Customer
Agency channel teams and media buyers, in-house performance teams, and analytics vendors for whom platform behaviour characterisation is an unserved product.

## Impact If Solved
The discipline exists for characterising systems you cannot open, and buyers face one daily with forum posts. Continuous identification robust to unannounced updates, and cross-account observation as an identification channel, are what the standard methods need here.
