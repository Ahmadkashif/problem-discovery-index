# Rare Event Modelling From Fraud and Medicine

**Niche:** [[niches/game-user-acquisition-firms/heavy-tail-estimation/profile|Heavy-Tail Estimation]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fraud detection and medical screening solved finding rare cases in vast populations, and UA models average over everyone.
**Tags:** #logistic-regression #gradient-boosting #confidence-intervals #evaluation-metrics #cross-validation #probability-distributions #maximum-likelihood-estimation #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to identify, from a few days of behaviour, the small fraction of players who will produce most of a cohort's value — and whoever does it takes the account.

## The Problem
Fraud detection and medical screening are built on finding a rare positive class in a large population. The methods handle extreme imbalance, calibrate probabilities for rare events, evaluate on precision at low recall rather than on accuracy, and are explicit that overall accuracy is meaningless when the base rate is tiny. The practice is mature and widely taught. UA models predicting a quantity dominated by a rare class use regression on the whole population.

## What Already Exists
Extreme class imbalance handling; rare-event probability calibration; precision-at-threshold evaluation; cost-sensitive learning; and screening pipeline design with staged thresholds.

## The Customization Gap
The adaptation is to a rare class defined by future behaviour rather than by a present state. It requires: (1) a positive class that has not happened yet at prediction time and is defined by cumulative future spending, so the label is censored and threshold-dependent — this is the substantive difference from any detection problem; (2) value that is continuous within the positive class rather than binary, so identification alone is not enough; (3) a decision made per cohort rather than per case, aggregating many uncertain individual predictions; (4) a base rate that varies by source, game and season; and (5) no confirming ground truth for months.

## Target Customer
UA data science teams, mobile publishers, bidding platforms, and predictive modelling vendors.

## Impact If Solved
Fraud and screening are explicit that overall accuracy is meaningless at a tiny base rate, and the methods are mature. A positive class that has not happened yet, with continuous value inside it, is what the transfer has to handle.
