# The System Records Every Rejection and Learns From None of Them

**Industry:** [[recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** High Impact
**One-liner:** A rejected candidate produces no outcome data, so any model trained on this record learns which people recruiters chose rather than which people would have done the job.
**Tags:** #causal-inference #gradient-boosting #confidence-intervals #hypothesis-testing #bayesian-inference #evaluation-metrics #compliance #cross-validation

## The Problem
An applicant tracking system records the full funnel: applications, screens, interviews, offers, rejections and hires, at enormous volume across every employer using it. It is the most complete record of hiring decisions that has ever existed.

It contains no information about whether the decisions were right. The people who were hired generate performance data; the people who were rejected generate nothing, ever. That asymmetry is not a data collection oversight, it is structural — the counterfactual is unobservable by construction.

The consequence for any model built on this data is decisive. A model trained to predict which candidates advance is predicting recruiter behaviour. It will reproduce whatever those decisions contained, including preferences for particular backgrounds, institutions, career shapes and phrasings, and it will present that as a fit score. Amazon's abandoned resume-screening tool is the canonical public instance and the condition that produced it — training on historical selection because that is the only labelled data available — is present in every system in this category.

Vendors describe these features in terms that blur the distinction. A model is said to identify strong candidates when what it does is identify candidates resembling those previously advanced, and the two are the same thing only if past selection was accurate and unbiased, which is exactly what nobody has established.

The volume pressure makes this worse rather than better. Applications per opening have risen sharply, generative tooling has made tailored applications cheap, and the response has been more automated screening — which means more decisions made by models of past recruiter behaviour, at greater scale, with less human review.

## Why It's Unsolved
The missing counterfactual is genuine and not solvable by better data engineering. Without hiring someone there is no way to know how they would have performed, and no observational technique recovers it.

Performance data on the hired side is itself weak. Manager ratings are noisy, compressed and carry their own biases, so even the half of the problem that is observable has a contaminated criterion — which means a model validated against performance ratings may be validating against the same bias it inherited.

The partial solutions all have costs somebody must accept. Auditing rejections by expert re-review costs time and produces a measure of agreement with a different human rather than of performance. Randomising at the margin of a screening threshold — advancing a small random subset of borderline rejections — produces genuine causal evidence and requires an employer to deliberately interview people the system screened out, which is operationally and politically awkward even though the cost is small.

And the commercial incentive is to ship the feature. Matching and ranking are what customers ask for, the validation is expensive and would qualify the claim, and no regulator has yet required evidence that a ranking feature predicts anything.

## What a Solution Looks Like
Say what the model is. A ranking model trained on advancement decisions should be described as predicting recruiter agreement, because that is what it does, and the labelling difference is the most consequential honesty available in this market.

Audit the rejections. Re-reviewing a random sample of rejected applications with expert reviewers, blind to the original decision, measures the disagreement rate and its demographic distribution. It does not measure performance and it does detect systematic false rejection, which is the failure that matters most and is currently invisible.

Randomise at the margin. Advancing a small random subset of candidates who fall just below a screening threshold produces the only genuine evidence available about false rejection, and at the margin the expected cost is low because those candidates are near the boundary by definition. A programme running over two years across a large employer would answer questions the field has argued about indefinitely.

Validate against better criteria on the hired side. Tenure, promotion and involuntary exit are less contaminated than performance ratings, and reporting against several separately is more honest than a composite.

And monitor for the pattern that matters. Whether a ranking feature's output correlates with demographic characteristics conditional on qualifications is measurable, and it is the specific check that would have caught the canonical failure before deployment rather than after.

## Impact If Solved
This sector makes an enormous number of consequential decisions about people's access to work using models trained on the only labels available, which are past human decisions, and describes the result as fit. Accurate labelling of what these models predict is free and would change how they are bought. Rejection auditing detects systematic false rejection that is otherwise invisible, and marginal randomisation is the only route to genuine evidence — expensive in awkwardness and cheap in money, which is the opposite of how it is usually described.
