# Measured Risk Reduction per Span Worked

**Niche:** [[niches/electric-utilities/vegetation-wildfire-mitigation-programs/profile|Vegetation Management & Wildfire Mitigation Programmes]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Utilities spend heavily on trimming and hardening and report modelled risk reduction, because nobody has joined work completed to outages and ignitions avoided.
**Tags:** #causal-inference #survival-analysis #gradient-boosting #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to show regulators that each trimming and hardening dollar removed measurable ignition and outage risk, and whoever ties completed work to risk reduced, span by span, takes the account.

## The Problem
A mitigation plan claims that trimming cycles, enhanced clearances, covered conductor and undergrounding will cut ignition risk by some percentage. Regulators and intervenors increasingly ask whether past work achieved what earlier plans promised. The utility has the data to answer: work completion by span, vegetation-caused outages and ignitions by location and date. But it sits in separate systems, and the comparison has never been done properly.

## Why Nobody Has Built This
Work is not randomised. The worst spans get treated first, which makes naive before-and-after comparisons misleading. Outage and ignition events are rare per span, and data systems differ across contractors and years.

## What to Build
A span-level panel of treatment history, vegetation and weather exposure, and outcomes. On it run survival models of time to vegetation-caused outage or ignition, with causal designs (matched spans, staggered-adoption comparisons) that estimate the effect of each treatment type and clearance level. The output is measured effectiveness by treatment, region and cost, fed back into the next plan's prioritisation.

## Target Customer
Wildfire mitigation and vegetation management leaders at western IOUs, public power systems and co-ops filing plans, and their regulatory teams.

## Impact If Built
If even ~10%–20% of mitigation spend moves from the least to the most effective treatments (estimate), the same budget removes measurably more risk, and plans survive review on evidence rather than assumptions.
