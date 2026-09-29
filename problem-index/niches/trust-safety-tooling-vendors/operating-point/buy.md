# Buy: Decision Analysis and Screening Practice

**Niche:** Operating Point & Threshold Setting
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Medical screening and decision analysis have spent decades formalising exactly this trade, with elicitation methods for incommensurable harms and a framework for setting the cut-off.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #probability-distributions #hypothesis-testing #compliance #descriptive-statistics
**Contested on:** Whether the number that decides how much harm is missed and how much legitimate speech is removed is chosen with a framework.

## The Problem

Choosing a threshold on a test where the two errors cause different kinds of harm is a problem medicine confronted directly and formalised.

Screening programmes must decide where to set a cut-off. Too sensitive and healthy people are subjected to unnecessary investigation, anxiety and occasionally harm from the follow-up. Too specific and disease is missed. The harms are of different kinds and cannot be traded off arithmetically without someone deciding the exchange rate.

The response was decision analysis. Utility elicitation methods — standard gamble, time trade-off, paired comparison — make people state their preferences over outcomes they cannot naturally quantify. Expected utility frameworks then compute the cut-off that follows. Sensitivity analysis shows how much the answer depends on the elicited values. And screening programme evaluation weighs benefits against harms explicitly, at population scale, as a matter of routine.

Content moderation faces the same structure with the same incommensurability and sets the cut-off by typing a number into a field.

## What Already Exists

Decision analysis: expected utility frameworks, utility elicitation methodology, decision curve analysis and sensitivity analysis, developed substantially in medical and policy contexts.

Screening evaluation: the frameworks for assessing whether a screening programme does more good than harm, including explicit accounting for false positive harms.

Diagnostic threshold setting: ROC analysis with cost-weighted optimal cut-off selection, standard practice in clinical test evaluation.

Machine learning: cost-sensitive learning and threshold optimisation, which handles the computation side well and assumes the costs are given.

Trust and safety: confidence scores and configurable thresholds.

## The Customization Gap

**Elicitation methods exist and have never been applied here.** Standard gamble and paired comparison are designed for exactly this — making someone state preferences over incommensurable outcomes — and no vendor or platform uses them.

**The affected party is not consulted.** Medical utility elicitation asks the patient. Content moderation thresholds are set by the platform, and the users on both sides of the error — those harmed by missed content and those wrongly removed — have no input, which is a meaningful difference.

**False positive harm is well studied there and unmeasured here.** Screening evaluation quantifies the harm of a false positive carefully. Trust and safety does not measure over-removal at all, which means half the trade has no magnitude.

**The costs vary by category and by community.** A single elicitation would be wrong. The framework needs to be applied per category and ideally per affected population, which is more work than the source discipline usually requires.

**Cost-sensitive learning solves the computation and assumes the input.** The machine learning literature handles threshold optimisation given costs, and the costs are precisely what does not exist.

**Sensitivity analysis is the most useful and least used element.** Showing how much the threshold depends on the elicited values would tell a platform whether their judgement even matters, and in some cases it barely does.

## Target Customer

Platform policy teams, who make the values judgement implicitly and would recognise the elicitation framing as giving structure to something they already do badly.

Vendors offering decision support, for whom an elicitation and optimisation capability is a differentiator that does not depend on unverifiable accuracy claims.

Regulators and civil society, for whom a documented elicitation would make a platform's values judgement inspectable rather than embedded in a configuration file.

## Impact If Solved

A formal apparatus for exactly this trade exists in medicine and policy analysis and has never been pointed at the decision that governs what billions of people see.

Utility elicitation would make the platform's values explicit, which is uncomfortable and is the precondition for the decision being reviewable by anyone.

And sensitivity analysis would show how much the threshold actually depends on the elicited values, which in some categories would reveal that the judgement matters less than the review capacity — a finding worth having.
