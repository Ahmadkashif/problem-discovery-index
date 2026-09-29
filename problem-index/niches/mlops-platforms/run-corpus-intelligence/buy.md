# Meta-Learning and Learning Curve Extrapolation

**Niche:** [[niches/mlops-platforms/run-corpus-intelligence/profile|Run Corpus Intelligence]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automated machine learning research produced learning curve extrapolation, multi-fidelity optimisation and meta-learning warm starts, and the platforms holding the ideal training corpus use none of them.
**Tags:** #bayesian-optimization #gaussian-processes #transfer-learning #gradient-boosting #time-series-forecasting #cross-validation #evaluation-metrics #feature-engineering
**Contested on:** Every serious competitor in this niche is fighting to turn millions of recorded training runs into answers the field currently gives as folklore — and whoever does that owns the empirical account of how machine learning actually works, which no individual product in the category can match.

## The Problem
Predicting where a learning curve will end from its first few epochs is a studied problem with published methods and benchmarks. Multi-fidelity optimisation formalises spending little compute on many candidates and more on survivors. Meta-learning warm-starts a search from what worked on similar datasets. All three are exactly what a run corpus enables, all three are published with implementations, and the vendors holding the largest corpora in existence have deployed none of them.

## What Already Exists
Learning curve extrapolation methods with parametric and Bayesian variants; successive halving and its asynchronous derivatives for multi-fidelity allocation; meta-learning warm starts from dataset meta-features; Bayesian optimisation with transfer across related tasks; and the automated ML benchmark suites that evaluated all of it.

## The Customization Gap
The adaptation is from an academic benchmark setting to a heterogeneous production corpus. It requires: (1) working across tasks, metrics and scales rather than within one benchmark, since the published methods assume comparability that a real corpus does not have and normalisation is the bulk of the engineering; (2) meta-features for real datasets that the platform can compute without seeing the data, which is both a privacy requirement and a practical one, and which the academic work does not consider; (3) calibrated uncertainty on the extrapolation, because a recommendation to kill a run must be conservative — the cost of stopping a run that would have won is much higher than the cost of continuing a loser, and the asymmetry has to be in the objective; (4) transfer across organisations without moving data, where meta-features and outcomes can be aggregated even when nothing else can, making federated aggregation unusually appropriate; and (5) delivering it as a suggestion the practitioner accepts rather than an automatic action, since trust has to be earned before anything is allowed to terminate somebody's run.

## Target Customer
Tracking and sweep vendors, ML platform teams, and the automated ML research community whose methods have an unserved corpus waiting for them.

## Impact If Solved
The methods are published, implemented and benchmarked, and the corpora that would make them work best are not using them. Building the asymmetric cost of a wrong stop into the objective is what makes an early-stopping recommendation acceptable to a practitioner.
