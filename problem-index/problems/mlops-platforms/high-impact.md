# Training-Serving Skew and Silent Degradation

**Industry:** [[mlops-platforms|MLOps Platforms]]
**Type:** High Impact
**One-liner:** The most common expensive failure in applied machine learning is a feature computed differently in production than in training, and the platforms that hold both computations do not compare them.
**Tags:** #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #entropy-cross-entropy-kl-divergence #feature-engineering #gradient-boosting #data-integration #revenue-impact

## The Problem
A model is trained on features computed by a batch pipeline over historical data. It is served on features computed by a different pipeline, in a different language, under latency constraints, over live data. The two are supposed to produce the same values and frequently do not.

The causes are mundane. A null handled as zero in one path and as a missing indicator in the other. A timezone difference in a timestamp feature. An aggregation window defined as the last thirty days in training and as the last thirty days excluding today at serving. A categorical encoding built from the training vocabulary that silently maps unseen values to a default. A unit change upstream that the batch job normalises and the streaming path does not.

Each produces a model that performs well in evaluation and worse in production, by an amount nobody measures, for as long as nobody notices. There is no error, no alert, no failed job. The model returns predictions with the same confidence and they are simply worse.

Alongside it runs the slower version: the world changes, the input distribution moves, and the model degrades gradually. Same symptom, different cause, same detection gap.

The signal is usually a business metric — conversion, fraud loss, churn — moving weeks or months later, at which point the model is one of twenty candidate explanations.

## Why It's Unsolved
The category grew up around training and never crossed into serving. Experiment tracking platforms instrument the training loop, which is where their users lived when the products were designed. The serving path is owned by a different team, runs on different infrastructure, and emits different telemetry. The organisational boundary became a product boundary.

Model monitoring exists as a separate category for exactly this reason, and its separateness is the problem: a monitoring product sees production inputs and predictions but not the training distribution, the feature definitions or the evaluation set, so it can detect that something moved without saying what it should have been.

Ground truth latency is the deeper obstacle. Whether a prediction was right often arrives weeks later — a loan defaults, a customer churns, a transaction is charged back — and sometimes never arrives for the predictions that mattered. Direct performance monitoring is therefore impossible in the window where intervention would help, which forces reliance on input-side proxies that are noisy and easy to dismiss.

And alert fatigue has poisoned the ground. Naive drift detection on high-dimensional feature vectors fires constantly, teams turn it off, and the next proposal is met with justified scepticism.

## What a Solution Looks Like
Direct comparison of the two computations rather than statistical drift detection on one of them. The training platform holds the feature values used to train; the serving path holds the values used to predict. Logging serving features and comparing their distributions against the training set, feature by feature, is a direct measurement of skew and is far more actionable than an abstract drift score.

Better still, replay: recompute a sample of production requests through the training pipeline and compare values exactly. Discrepancies become specific and attributable rather than distributional.

Drift detection that reports impact rather than movement. A feature that shifted and that the model barely uses is noise; a shift in a high-importance feature is the alert. Weighting by model attribution is what makes drift monitoring survivable.

Proxy performance where labels are late: prediction distribution shifts, confidence changes, and agreement with a champion model all move before the outcome arrives.

## Impact If Solved
Silent degradation is the dominant failure mode of deployed machine learning and it is currently discovered by finance. Comparing the two computations directly — which requires only that both platforms log what they already compute — converts a months-long mystery into a specific, attributable defect.
