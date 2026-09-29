# Statistical Process Control and Sequential Monitoring

**Niche:** [[niches/mlops-platforms/drift-and-degradation-detection/profile|Drift & Degradation Detection]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Manufacturing has monitored processes for drift since the 1920s with control charts and change-point methods calibrated to a false alarm budget, and model monitoring reinvented it badly.
**Tags:** #change-point-detection #hypothesis-testing #confidence-intervals #time-series-forecasting #descriptive-statistics #evaluation-metrics #monte-carlo-methods #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to tell a model owner that their model has stopped working before a business metric does — and whoever does that takes the account, because that is the question the whole category was bought to answer.

## The Problem
Detecting when a process has shifted, with a controlled false alarm rate and a quantified detection delay, is exactly what statistical process control was built for, and it has a century of practice behind it. Sequential change-point detection has strong theory with optimality results. Model monitoring products instead compute a distribution distance, compare it to a threshold somebody picked, and fire — which is the approach the quality control discipline abandoned before most of these vendors existed.

## What Already Exists
Control charts including cumulative sum and exponentially weighted variants with established design procedures; sequential change-point detection with quantified average run length to false alarm; multivariate process monitoring for correlated measurements; false discovery rate control for many simultaneous tests; and the whole quality engineering practice around out-of-control action plans.

## The Customization Gap
The adaptation is to hundreds of correlated features monitored simultaneously against a reference that may itself be stale. It requires: (1) multiplicity control, since monitoring three hundred features at a five percent threshold produces fifteen false alarms a day by construction and this single fix removes most of the noise the category complains about — it is the cheapest and most consequential adaptation available; (2) thresholds designed against an explicit false alarm budget rather than chosen by convention, which is the standard procedure in process control and is simply not done here; (3) accounting for correlation between features, because a single upstream change moves forty features and reporting forty alerts is the difference between a signal and a flood; (4) seasonal and cyclical structure, since a control chart on a metric with strong weekly seasonality fires every Monday, and the process control literature handles this and the ML tooling does not; and (5) distinguishing detection of a shift from a judgement that it matters, which in process control is handled by an action plan attached to each chart and here is left entirely to the recipient.

## Target Customer
Monitoring vendors, model owners drowning in drift alerts, and the quality engineering community whose methods have a direct unserved application here.

## Impact If Solved
A century of process control methodology addresses exactly this and the category reinvented a worse version. Multiplicity control alone removes most of the false alarms, and designing thresholds against a stated false alarm budget is standard practice everywhere else.
