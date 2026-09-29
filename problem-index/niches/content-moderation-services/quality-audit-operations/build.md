# Build: Risk-Weighted Audit Sampling

**Niche:** Quality Audit Operations
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An audit sampler that spends its budget on the decisions most likely to be wrong or most consequential if wrong, instead of drawing uniformly from a queue that is mostly obvious.
**Tags:** #gradient-boosting #bayesian-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #monte-carlo-methods #automation #workflow-orchestration
**Contested on:** Whether audit effort is spent where it would change a judgement, or spread uniformly across a sample drawn at a rate the contract specified.

## The Problem

An audit programme samples a fixed percentage of every reviewer's decisions at random and re-reviews them. On a queue where the overwhelming majority of items are unambiguous, this means auditors spend most of their time agreeing with decisions that were never in doubt.

The waste is large and quantifiable. If eighty-five per cent of a queue is obvious, then the same fraction of the audit budget produces a confirmation that carries almost no information. The disagreements — which are the entire point of auditing, since they are where either the reviewer erred, the auditor erred, or the policy is inadequate — are concentrated in a small, identifiable minority of items that uniform sampling reaches only by chance.

Worse, the uniform sample is statistically inadequate for what it is used for. Individual reviewer accuracy is computed from a few dozen items a month and then used to rank people, coach them and in some operations affect their pay. At that sample size, the confidence interval around an individual's accuracy is wide enough that most of the differences being acted on are not distinguishable from noise. Nobody computes the interval, so nobody knows.

Both problems have the same fix, and it is a sampling design rather than a new capability.

## Why Nobody Has Built This

**The sampling rate is a contractual term.** Agreements specify a percentage sampled, which is easy to audit and easy to argue about. Risk-weighted sampling produces a different and better estimate from the same effort, but it is harder for a client to verify and looks like the supplier choosing which of its own work to examine.

**Uniform random sampling has an appearance of fairness.** Weighting toward likely errors can be presented as targeting particular reviewers, which is a difficult conversation with a workforce and in some jurisdictions with a works council. The design has to handle that explicitly — a guaranteed uniform base layer plus a risk-weighted supplement, with the weighting based on item characteristics rather than on the person.

**Predicting which decisions are wrong requires a model of correctness.** Estimating error likelihood needs disagreement history, item difficulty and reviewer-item interaction, which means building the difficulty model first. It is a modest project and it is a project, whereas uniform sampling requires nothing.

**Quality operations is a cost centre.** It is staffed to the contractual rate and measured on completing the sample. Nobody in it is rewarded for extracting more information from the same budget.

**The statistical inadequacy is uncomfortable.** Computing confidence intervals on individual accuracy would show that a large share of current performance management is acting on noise, which implicates years of decisions about people.

## What to Build

**A two-layer sample.** A uniform base layer at a reduced rate, preserving unbiased estimates and the fairness property that every reviewer's work is sampled without regard to prediction. On top of it, a risk-weighted layer targeting items by predicted disagreement probability and by consequence. The base layer keeps the programme defensible; the supplement is where the information comes from.

**Predict disagreement, not error.** The tractable target is the probability that a second qualified reviewer would decide differently, learned from historical audit outcomes, item features, category, policy version recency and the difficulty model. Items near a policy boundary, in recently-changed categories, or of a type with high historical disagreement are where auditing pays.

**Weight by consequence as well as by uncertainty.** A likely-wrong decision on a low-harm item is worth less to catch than a moderately-uncertain one on a high-harm item. The sampler should optimise expected value of information, which is a standard formulation and entirely absent here.

**Report intervals, always.** Every accuracy figure with its confidence interval and the sample size required to detect a difference that matters. Where the sample cannot distinguish two reviewers, the report should say so rather than ranking them. This single change would stop a great deal of performance management from acting on noise.

**Adaptive allocation.** Concentrate additional sampling where uncertainty is highest — a new reviewer, a category that just changed, a site whose distributions have shifted — and reduce it where a reviewer's performance is already well established. Sequential allocation of this kind is well understood and would substantially improve what the same budget buys.

**Route disagreements to adjudication, not to scoring.** Items where auditor and reviewer disagree in good faith should go to a panel rather than straight into an accuracy figure, feeding the policy and the difficulty model. This connects the audit programme to the case library in [[niches/content-moderation-services/policy-training/profile|🟠 Policy Training & Consistency]] and turns auditing into something that improves the operation rather than only grading it.

## Target Customer

Vendor quality operations, where the change is internal, needs no client permission for the risk-weighted supplement if the contractual base rate is preserved, and pays back quickly in audit capacity.

Platform audit teams running their own parallel sampling, who have the same inefficiency and additionally need to reconcile their findings with the vendor's — a reconciliation that difficulty adjustment and interval reporting would make far less contentious.

## Impact If Built

The same audit budget produces several times the information, because it stops being spent on confirming the obvious. That is a straightforward efficiency gain in a function that is several per cent of headcount.

Confidence intervals on individual accuracy would end the management of people on differences that are not measurable, which is quietly one of the more consequential fairness problems in the industry.

And routing genuine disagreements to adjudication converts the audit programme from a grading exercise into the operation's main source of information about where its policy and its training are failing.
