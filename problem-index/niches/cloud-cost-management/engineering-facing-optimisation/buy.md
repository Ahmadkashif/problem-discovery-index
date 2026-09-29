# Selective Prediction and Safe Automation

**Niche:** [[niches/cloud-cost-management/engineering-facing-optimisation/profile|Engineering-Facing Optimisation]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Abstaining when uncertain is a developed area of machine learning, and cost recommendation engines emit every suggestion they can compute.
**Tags:** #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #evaluation-metrics #cross-validation #automation #revenue-impact
**Contested on:** Every serious competitor here is fighting to produce a recommendation an engineer will actually act on — specific, safe and verifiably right — and whoever does that takes engineering, because after two bad suggestions the feature is dead permanently.

## The Problem
When the cost of a wrong answer greatly exceeds the cost of no answer, the correct behaviour is to abstain, and selective prediction provides the framework: risk-coverage trade-offs, conformal guarantees, calibrated confidence. Cost recommendation engines compute a suggestion for every resource they can evaluate and present them all equally, in a setting where two wrong suggestions end the relationship.

## What Already Exists
Selective prediction and learning-to-defer methods; conformal prediction with distribution-free coverage guarantees; calibration techniques; anomaly detection for identifying resources whose behaviour is unusual and therefore risky to judge; and the safe automation patterns from infrastructure tooling — dry run, staged application, automatic revert.

## The Customization Gap
The adaptation is to infrastructure changes with asymmetric and heterogeneous risk. It requires: (1) a per-recommendation risk model rather than a global threshold, since downsizing a batch worker and downsizing a production database have entirely different downside, and the same confidence level is wrong for both; (2) explicit identification of the patterns that cause errors — standby roles, warm caches, periodic peaks, non-processor bottlenecks — as exclusion rules rather than relying on a model to learn them from thin evidence, because these are known and enumerable and a rule is more reliable than an inference here; (3) safe application mechanics borrowed from deployment practice, so a recommendation can be applied to one instance, observed, and reverted automatically — which converts a risky judgement into an experiment and is the strongest available route to trust; (4) coverage reported honestly, since a product that assesses a third of the estate confidently is more useful than one that guesses at all of it, and saying so is what distinguishes it; and (5) outcome tracking, because the record of recommendations that worked is what earns the right to make the next one.

## Target Customer
Cost management vendors, platform engineering teams, and the infrastructure automation vendors whose safe-change mechanics this depends on.

## Impact If Solved
The loss is extremely asymmetric and the products behave as though it were symmetric, which is why the feature is unread everywhere. Enumerated exclusion rules and revert-capable staged application are the two changes that most directly convert a distrusted list into an acted-on one.
