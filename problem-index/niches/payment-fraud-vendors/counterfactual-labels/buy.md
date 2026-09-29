# Experimentation and Bandit Practice

**Niche:** [[niches/payment-fraud-vendors/counterfactual-labels/profile|Counterfactual Label Acquisition]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Exploration under uncertainty is a solved field with bandits, off-policy evaluation and explore-exploit tuning, and fraud decisioning explores not at all.
**Tags:** #causal-inference #monte-carlo-methods #hypothesis-testing #confidence-intervals #evaluation-metrics #markov-decision-processes #gradient-boosting #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to obtain honest outcomes for the transactions the model declines — and whoever pays the visible short-term cost of that experiment first can say something about its own accuracy that no competitor can contradict or match.

## The Problem
Learning a policy whose outcomes are observed only where the policy acted is a well-developed area: contextual bandits, exploration schedules, off-policy evaluation with importance weighting, and doubly robust estimators that extract more from limited exploration. Recommendation, advertising and pricing systems all use it routinely. Fraud decisioning is a textbook instance — a policy that censors its own feedback — and runs a pure exploit strategy.

## What Already Exists
Contextual bandit algorithms and exploration schedules; off-policy evaluation and importance weighting; doubly robust estimation; propensity logging infrastructure; and regret analysis frameworks.

## The Customization Gap
The adaptation is to exploration with real, attributable financial loss and an adversary. It requires: (1) exploration cost that is a direct loss rather than a foregone click, which changes the acceptable exploration rate and is the substantive difference; (2) an adversary who will detect and exploit a predictable exploration policy, so randomisation must be unpredictable and bounded; (3) propensity logging that most fraud platforms do not do, without which off-policy evaluation is impossible and which is a cheap prerequisite; (4) delayed and noisy rewards, since chargebacks arrive over months and mean several things; and (5) exploration cost borne by a merchant or guarantor rather than by the learner, requiring a commercial arrangement.

## Target Customer
Risk and data leadership, merchants and guarantors, and machine learning platform vendors whose bandit tooling has no fraud presence.

## Impact If Solved
This is a textbook censored-feedback policy problem and the field's methods apply directly. Propensity logging alone — a cheap prerequisite most platforms skip — would make off-policy evaluation possible before any exploration begins.
