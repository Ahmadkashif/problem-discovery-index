# Observational Causal Inference

**Niche:** [[niches/creator-businesses/post-publication-attribution/profile|Post-Publication Attribution]]
**Industry:** [[industries/creator-businesses|Creator Businesses]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Social science built a whole methodology for estimating effects when randomisation is impossible, and creator analytics reports raw outcomes.
**Tags:** #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #monte-carlo-methods #descriptive-statistics #k-nearest-neighbors #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to separate what the creator did from what the recommendation system decided — and whoever can say what a video was actually responsible for replaces a decade of anecdote with evidence.

## The Problem
Estimating a causal effect when you cannot randomise is a solved methodological area: matching, difference-in-differences, synthetic controls, instrumental variables, sensitivity analysis for unmeasured confounding, and honest reporting of what the design can and cannot support. Economists and epidemiologists do this routinely on messier data than a creator's analytics export. Creator analytics reports raw outcomes and leaves the inference to intuition.

## What Already Exists
Matching and weighting methods; difference-in-differences and synthetic control; instrumental variable designs; sensitivity analysis for unmeasured confounders; and reporting standards for observational claims.

## The Customization Gap
The adaptation is to a confounder that is an adaptive system. It requires: (1) a confounder that responds to the treatment itself, since the algorithm's allocation depends on early response to the content — which violates most standard designs and is the substantive difficulty; (2) small samples, as a channel has hundreds of observations rather than thousands, making precision limited and honesty essential; (3) a non-technical user, so the method must produce a plain statement rather than a coefficient; (4) a confounder that changes over time as the platform updates, which breaks long historical comparisons; and (5) decisions made weekly, so the analysis must be automatic rather than a study.

## Target Customer
Creators and channel managers, creator analytics vendors, management companies, and researchers studying algorithmic distribution.

## Impact If Solved
The methodology for inference without randomisation is mature and has never been pointed here. The genuinely hard part is a confounder that responds to the treatment, and naming that honestly is already better than the current silence.
