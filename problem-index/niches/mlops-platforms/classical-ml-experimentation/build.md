# Four Hundred Runs and No Conclusion

**Niche:** [[niches/mlops-platforms/classical-ml-experimentation/profile|Classical ML Experimentation]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A team finishes a month of experimentation with four hundred tracked runs and no statement of what it learned, because the platform records runs and does not attribute differences to causes.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #bayesian-optimization #evaluation-metrics #gradient-boosting #cross-validation #descriptive-statistics
**Contested on:** Every serious competitor in this sub-niche is fighting to make a large population of cheap runs genuinely comparable — so that a team can say what changed, what it was worth, and where the next run should go — and whoever does that takes the account, because comparability is the only thing a tracking tool is bought for at this scale.

## The Problem
The quarter's experimentation is over. The dashboard shows four hundred runs, the best one at an area under the curve of 0.847, and a parallel coordinates plot nobody can read. The question the team lead has to answer is what was learned: did the new feature set help, was it worth its pipeline cost, does the regularisation change matter, is the gain over last quarter's model real or within noise. None of that is in the tool. Somebody spends two days in a notebook reconstructing it by hand from the run export, and the reconstruction is not repeated next quarter.

## Why Nobody Has Built This
Attribution requires knowing what differed between runs in a structured way, and the platforms record configuration as an unstructured dictionary where a feature set change and a learning rate change look identical. Most real comparisons are observational rather than designed — runs were launched as a person thought of them, not as a factorial design — so naive comparison is confounded and doing it properly requires care the vendors have not invested. And recording is a feature that demos well while concluding is a feature that demos as a paragraph of text.

## What to Build
Turn the run population into findings. Structure the configuration space so that a change is typed — feature set, hyperparameter, data version, preprocessing, code revision — which is the precondition for attributing anything and is a schema decision rather than a modelling one. Attribute metric differences to the changes that plausibly caused them, handling the confounding that observational run populations always carry, and state the uncertainty rather than presenting a point estimate as a finding. Produce a standing summary of what the population supports: which changes have evidence behind them, which are within noise, which were tried and abandoned and by whom. Detect repeated investigation, since the most common waste at this scale is a new team member spending a week establishing something a colleague established in March and did not write down — and the runs are right there. Recommend where the next runs should go, using the whole prior population rather than the current sweep, because search restarted from scratch on every sweep is the default and is straightforwardly wasteful. Report cost alongside gain, so a feature set worth a tenth of a point and a nightly pipeline can be judged on both. And write the summary automatically at the end of a sweep, since the two days of reconstruction is exactly the work that gets skipped under deadline.

## Target Customer
Data science organisations, their engineering leads, and the tracking vendors whose product currently ends at the run table.

## Impact If Built
Recording is solved and concluding is absent. Typing the configuration space is the schema change that makes attribution possible at all, and detecting re-investigation addresses the largest silent waste at this scale.
