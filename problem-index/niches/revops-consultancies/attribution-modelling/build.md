# Attribution That Has Been Checked

**Niche:** [[niches/revops-consultancies/attribution-modelling/profile|Attribution Modelling]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Budget is allocated on a model whose correctness has never been tested against anything.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact #descriptive-statistics #data-integration #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to say which activities produced revenue, using a model whose output nobody has ever checked against a controlled test — and whoever validates it takes the account.

## The Problem
Attribution assigns revenue credit across touches. The rule that does the assigning is a choice, and different choices produce materially different answers about which channels work. Budget follows the answer. Nobody checks the answer against anything — not a holdout, not a geographic test, not a controlled experiment — so the model is a convention that determines spending, and its correctness is unestablished.

## Why Nobody Has Built This
Validation requires experiments that cost money and withhold activity from part of the market. The model's output is politically useful to whoever it flatters. Multi-touch attribution is sold as a solution rather than as a hypothesis. And nobody has asked for the check.

## What to Build
Validate the model against controlled tests and report what the model cannot know. Run holdout and geographic experiments to establish incremental contribution for the major channels, which is the core — attribution is an inference and an experiment is a measurement, and only the second can validate the first. Compare the attribution model's answer against the experimental result and report the gap, which is the finding that changes budget allocation. Show how much the allocation changes under different attribution rules, since that sensitivity is the honest statement of how much the model is really telling anyone. Model the unobserved touches explicitly rather than attributing only what was tracked, as the tracked set is systematically biased toward digital and measurable channels. Attach uncertainty to attributed figures, which are currently reported as exact. Handle long sales cycles where touches precede revenue by quarters, which breaks most standard models. Calibrate the model against experimental results where they exist, which is better than choosing between rules on principle. Report channel contribution as a range rather than a share. Re-validate periodically, as channel dynamics shift. And state plainly which channels the model cannot measure, rather than assigning them zero by omission.

## Target Customer
Marketing and revenue leadership, RevOps consultancies, attribution and marketing measurement vendors, and analytics providers.

## Impact If Built
Attribution is an inference and an experiment is a measurement, and only the second can validate the first. Running holdouts on the major channels and reporting the gap is what turns a convention into a measurement.
