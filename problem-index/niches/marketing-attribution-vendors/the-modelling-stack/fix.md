# Two Vendors, Two Answers, One Business

**Niche:** [[niches/marketing-attribution-vendors/the-modelling-stack/profile|The Modelling Stack]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Two vendors model the same business over the same period and return materially different channel contributions, and the client is advised to triangulate.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #causal-inference #descriptive-statistics #quick-win #bayesian-inference #compliance
**Contested on:** This niche is not terminal — path-based attribution and mix modelling are different disciplines with different failure modes and different winners, and they are stated separately in the sub-niches.

## The Problem
A client runs two vendors in parallel. Same business, same data, same period. One says a channel contributed twice what the other says. Both present confident charts. The client asks each vendor about the other's number and receives an explanation of why the other method is limited. The advice is to triangulate. Triangulation between two estimates with unknown and possibly correlated biases is not a method — it produces a number between two numbers with no reason to think it is closer to the truth, and everybody involved knows it.

## Why It's Still Broken
Disagreement is embarrassing and each vendor's incentive is to explain it away rather than to investigate it, so nobody has ever done the comparison properly — the informative event is treated as a problem to manage. There is no shared standard for what is being estimated, so the two numbers may not even be answering the same question. Clients lack the capability to adjudicate. And the advice to triangulate lets everyone stop.

## What a Fix Looks Like
Treat disagreement as information. Establish first that both vendors are estimating the same quantity over the same period and population, which is the fix's precondition and frequently resolves a large part of the gap by itself — different windows, different conversion definitions and different channel groupings account for more disagreement than anyone assumes. Decompose the remaining difference into its sources: specification, priors, data coverage, identity assumptions. Run an experiment on the channel where they disagree most, which is the only adjudication available and is a highly efficient use of an experimental budget. Ask each vendor to predict the experiment's result before it runs, which is the single most revealing exercise a client can conduct and is almost never done. Report both estimates with their uncertainty rather than averaging them, since an average of two overconfident point estimates is worse than either with an honest interval. Require assumptions in writing from each, so the disagreement can be located rather than debated. Keep the comparison as a standing exercise rather than a one-off bake-off. Publish anonymised comparison findings, since the category will not develop standards until the disagreements are visible. Use the disagreement to bound the decision, because a decision that is the same under both estimates does not need resolving. And stop calling averaging triangulation, because the word conceals that no method is being applied.

## Who Feels the Pain
Clients paying two vendors and receiving two answers; vendors whose credibility rests on the comparison never being pursued; and the category, whose standard response to a falsification opportunity is to average it away.

## Impact If Fixed
Disagreement is the category's most informative event and is managed rather than investigated. Establishing that both are estimating the same quantity resolves much of the gap, and asking each vendor to predict an experiment before it runs is the most revealing exercise a client can do.
