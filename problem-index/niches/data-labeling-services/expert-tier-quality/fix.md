# Agreement Reported as Quality

**Niche:** [[niches/data-labeling-services/expert-tier-quality/profile|Expert-Tier Quality]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Fix (Pain Point)
**One-liner:** A delivery report presents inter-annotator agreement as the quality figure, the customer reads disagreement as error, and on a genuinely ambiguous task the number is partly measuring the task.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #bayesian-inference #quick-win #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to establish whether an expert judgement is correct when no ground truth exists and reasonable experts disagree — and whoever does that takes the frontier contracts, because consensus arithmetic is the industry's only quality signal and it does not work here.

## The Problem
The report says inter-annotator agreement is seventy-one percent. The customer's model team reads this as a defect rate. The vendor's delivery manager defends it by explaining that the task is hard, which sounds like an excuse. Neither party knows what agreement should be expected on this task, because nobody has established the ceiling — the level the best available experts achieve among themselves — and without that number the reported figure has no interpretation at all. The conversation that follows is a negotiation rather than an assessment.

## Why It's Still Broken
Agreement is computed automatically and is the only quality number available, so it became the figure in the report. Establishing the ceiling requires a deliberate exercise — having the most qualified available assessors do a sample independently — which costs money and has never been treated as part of project setup. And a vendor volunteering that a task has an agreement ceiling of seventy-five percent is making a claim about their own output's limits, which is commercially uncomfortable even when it is true and is the honest framing.

## What a Fix Looks Like
Establish and report the ceiling. Run a calibration exercise at project start: the best available assessors, independently, on a sample, which produces the achievable agreement for this task and is the number every subsequent figure should be read against — and costs a small fraction of the project. Report delivered agreement relative to the ceiling rather than absolutely, which turns an uninterpretable percentage into a meaningful one. Decompose disagreement into annotator error, genuine ambiguity and guideline ambiguity, since only the first is a defect and the other two require different responses from the vendor and the customer respectively. Report per-item uncertainty in the delivered data, so the customer can weight or exclude the contested items rather than treating the whole set as uniform. Agree the quality definition at contract time rather than arguing about it at delivery, which is where these disputes actually originate. And track the ceiling over time, since guideline improvements should raise it and that is the measurable evidence that the vendor's quality work is doing anything.

## Who Feels the Pain
Delivery managers defending a number nobody can interpret; customers reading task ambiguity as vendor error; and vendors whose genuine quality improvements are invisible in a statistic dominated by the task.

## Impact If Fixed
A calibration exercise at project start costs little and makes every subsequent agreement figure interpretable, which is currently impossible. Decomposing disagreement into its three causes is what turns a dispute into an assessment with actions attached.
