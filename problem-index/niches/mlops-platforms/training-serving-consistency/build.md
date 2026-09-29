# Both Computations Held and Never Compared

**Niche:** [[niches/mlops-platforms/training-serving-consistency/profile|Training–Serving Consistency]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The most common expensive failure in applied machine learning is a feature computed differently in production than in training, and the platforms that hold both computations do not compare them.
**Tags:** #hypothesis-testing #change-point-detection #evaluation-metrics #data-integration #descriptive-statistics #entropy-cross-entropy-kl-divergence #automation #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to prove that the feature values a model sees in production are the values it was trained on — and whoever does that takes the account, because it is the most common expensive failure in applied machine learning and nothing currently detects it.

## The Problem
A fraud model is trained on a feature defined as the customer's transaction count in the trailing thirty days, computed in a warehouse query. At serving time the same feature is computed by a streaming job written by a different team, whose window is thirty days from the start of the current day rather than from the current timestamp. The values differ for every customer, systematically, in a direction that matters. The model was evaluated at an accuracy it will never achieve. Nothing errors. Six weeks later an analyst notices the fraud catch rate is below forecast and a three-week investigation begins.

## Why Nobody Has Built This
The comparison requires the serving-time values to be logged, which many deployments do not do because it costs storage at request volume and nobody has articulated what it buys. Vendors are organised around training, where their integration and their customer relationship sit, and the serving path frequently belongs to a different team on different infrastructure. Feature stores were the category's answer and they solve it inside their own boundary, which lets everyone treat the problem as addressed. And the failure is invisible, so it generates no support tickets to prioritise against.

## What to Build
Log the serving values and diff them against training. Capture the feature vector the model actually received at inference time, for a sample of requests, which is the one prerequisite and is affordable at a sampling rate that still detects systematic skew within hours. Recompute the training-time definition for those same entities at those same timestamps and compare value by value, which is the direct test and is far more informative than comparing distributions — a distribution comparison passes when two features are swapped, and a value comparison does not. Report skew per feature with magnitude and direction, since an engineer needs to know which feature and by how much, not that something is wrong. Rank by the model's sensitivity to each feature, because a large skew on an unimportant feature matters less than a small skew on the dominant one, and the ranking is what makes the report actionable rather than a wall of warnings. Detect it at deployment rather than in production, by running the comparison as a pre-release gate on a shadow traffic sample, which is where this becomes prevention instead of diagnosis. Attribute the cause where the pattern allows — a constant offset, a window boundary, a null-handling difference and a type coercion all have recognisable signatures. And make consistency a standing contract on the model rather than a one-off check, since a feature definition that matches today drifts the next time either pipeline is edited.

## Target Customer
ML engineering and platform teams, the model owners accountable for production performance, and the MLOps and monitoring vendors on either side of the gap.

## Impact If Built
Both computations exist and nobody diffs them. Comparing values for the same entity rather than distributions is what catches the real failures, and ranking by model sensitivity is what makes the output something an engineer acts on.
