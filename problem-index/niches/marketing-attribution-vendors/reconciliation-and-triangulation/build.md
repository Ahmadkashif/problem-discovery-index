# Triangulation Is Not a Method

**Niche:** [[niches/marketing-attribution-vendors/reconciliation-and-triangulation/profile|Reconciliation & Triangulation]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Three methods with unknown biases disagree and the client is told to triangulate, which is a word standing in for the absence of a method.
**Tags:** #bayesian-inference #causal-inference #confidence-intervals #monte-carlo-methods #hypothesis-testing #evaluation-metrics #probability-distributions #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to combine three methods with unknown biases into one defensible number — and whoever does that properly replaces an instruction to triangulate that nobody can execute.

## The Problem
The client has a path-based number, a mix model number and an occasional experiment. They disagree. Each vendor explains why theirs is right. The advice everyone gives is to triangulate, which in practice means a measurement lead looks at three numbers and decides, or averages them, or picks the one that fits the plan. There is no method being applied. The combination is the step where the actual budget decision is made, it is the least rigorous step in the entire chain, and it is performed by the person with the least methodological support and the most organisational pressure.

## Why Nobody Has Built This
No vendor sells combination because every vendor's commercial interest is in their own estimate being the answer — the step that matters most is the one nobody is paid for. Combining estimates properly requires knowing their biases and correlations, which nobody has measured. The client lacks the capability. And the word triangulate is comfortable enough to prevent anyone noticing that nothing is happening.

## What to Build
Build the combination as a real method. Combine estimates with explicit weights derived from each method's demonstrated reliability in this context, which is the core and requires the validation record the category does not keep — which is why this niche depends on the validation one. Model the correlation between methods, since two methods sharing a data source or an assumption are not independent evidence and averaging them overstates the confidence substantially. Use experiments as the anchor, weighting the models by how well each has predicted past experimental results, which is the only defensible basis for a weight. Report the combined estimate with an interval that reflects method disagreement rather than within-method uncertainty, because the disagreement is the larger term and is currently discarded. Identify where the methods agree, since a decision that is the same under all of them needs no resolution and identifying those cases is immediately useful. Escalate genuine disagreements to an experiment rather than to a judgement, which turns an argument into a question. Make the combination reproducible and auditable, so it is a method rather than a preference. Sell it as an independent function, since a party with no stake in any one estimate is the only one who can credibly perform this. Give the client the decision rather than the number, because the number is an input and the allocation is the deliverable. And record the combined estimates and their outcomes, so the weights improve.

## Target Customer
Client measurement and finance leadership, independent measurement advisors, and the vendors who would rather compete on a validated weight than on an unfalsifiable claim.

## Impact If Built
The step where the budget decision is made is the least rigorous in the chain and nobody is paid for it. Weighting by demonstrated predictive performance against experiments, and modelling the correlation between methods, replaces a word that stands in for the absence of a method.
