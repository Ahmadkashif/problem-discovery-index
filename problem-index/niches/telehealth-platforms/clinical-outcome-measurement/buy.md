# Buy: Quality Measurement Frameworks Adapted to Episodic Virtual Care

**Niche:** [[niches/telehealth-platforms/clinical-outcome-measurement/profile|Clinical Outcome Measurement]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Healthcare quality measurement is a mature, specified discipline built around a population attributed to a provider over a year; virtual care sees a patient once.
**Tags:** #descriptive-statistics #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance #bayesian-inference #data-integration #survival-analysis
**Contested on:** Whether quality measure specifications built for attributed populations can apply to a single episode.

## The Problem

Healthcare quality measurement has decades of infrastructure. HEDIS measures, CMS quality programmes, patient-reported outcome instruments, registry reporting and the specification bodies behind them provide standardised, validated, comparable measures that payers and regulators already recognise.

Nearly all of it assumes attribution: a patient is assigned to a provider or plan for a period, and the measure asks what happened to that population over the year. Telehealth sees a patient for an episode, often once, with no attribution, no panel and no denominator. The measures do not have a place to stand.

## What Already Exists

NCQA and the HEDIS measure set, CMS quality programme specifications, PROMIS and the validated patient-reported outcome instruments, condition-specific symptom scales, registry infrastructure, and the analytics vendors serving provider quality reporting. Payer claims feeds where contracts exist.

## The Customization Gap

**There is no attributed population.** Episode-based measurement needs its own denominator definition — encounters for a presentation rather than patients in a panel — which is a different measure construction than anything in the standard sets. Building the episode-level equivalents of the relevant measures is the substantive work and has no off-the-shelf answer.

**The window is days, not a year.** Standard measures look at annual screening and control. The clinically meaningful questions here resolve in one to three weeks: did the symptom settle, was the prescription filled, did the patient escalate. Short-window measures are largely unspecified and have to be defined and defended.

**PRO instruments have to fit a single message.** PROMIS and the condition-specific scales are validated and mostly designed for clinic administration. Deploying them as a one-tap follow-up message, with acceptable response rates and honest handling of non-response, is a delivery and psychometric adaptation rather than a licensing decision.

**Claims linkage is the enabling infrastructure and is contract-dependent.** Downstream escalation measurement requires claims or exchange data, available only for the payer-contracted subset. That subset becomes the calibration anchor for internal proxies used across the rest, and that two-tier design is not how any quality programme is structured.

**The comparison group is the hard part.** Quality measures are compared against national benchmarks for attributed populations. There is no benchmark for episodic virtual care, so the platform is comparing either to itself over time or to in-person ambulatory rates that describe a different population — and being explicit about which is what makes the reporting credible.

## Target Customer

Platforms building quality reporting for payer and employer contracts, who reach for HEDIS and find the denominators do not exist. Also the quality measurement bodies and analytics vendors, for whom episodic virtual care is an emerging measurement context with no specification set.

## Impact If Solved

The validated instruments, specification discipline and reporting infrastructure get reused, and the episode denominators, short windows, single-message PRO delivery, two-tier calibration and honest comparison framing get built. The practical result is outcome reporting a payer will accept, in a market that is starting to require it.
