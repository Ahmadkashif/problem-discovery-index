# Modelling an Adversary That Moves

**Niche:** [[niches/payment-fraud-vendors/decision-modelling/profile|Decision Modelling]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The model is trained as though the data-generating process were stable, and the data-generating process is a person trying to defeat it.
**Tags:** #gradient-boosting #graph-neural-networks #change-point-detection #evaluation-metrics #confidence-intervals #transfer-learning #contrastive-learning #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to build the best decision from device, behavioural, network and consortium signals against an adversary who adapts — and whoever models best on the labels that exist wins the transactions everybody else gets wrong.

## The Problem
Fraud models are built with the standard supervised apparatus: features, training data, cross-validation, a retraining cadence. The assumption underneath is that tomorrow's data resembles today's. It does not, because an intelligent adversary is probing the decision boundary, discovering which signals matter, and changing behaviour specifically to defeat what works. A model that performs beautifully on held-out historical data can be systematically defeated within weeks and the metrics will not show it until the chargebacks arrive months later.

## Why Nobody Has Built This
The modelling toolkit came from general supervised learning, so adaptation was handled by retraining more often — increasing the cadence is the obvious response and it substitutes for modelling the adversary at all. Adversarial behaviour is hard to represent and harder to validate. Feedback delay means degradation is detected late. And competitive pressure rewards adding features rather than rethinking the frame.

## What to Build
Model the adversary rather than only the transactions. Represent attack campaigns as entities rather than treating transactions independently, which is the core and is what makes adaptation visible — an attacker's probing is a pattern across attempts, not a property of any one. Detect boundary probing explicitly, since a series of transactions systematically varying one attribute is the signature of someone learning the model. Monitor for drift in the feature-outcome relationship continuously rather than waiting for chargebacks, because the delay is what makes the adversary's advantage durable. Use graph structure as the most adaptation-resistant signal, as connections between entities are harder to fabricate than any individual attribute. Build models that degrade gracefully, since a model that fails catastrophically when one signal is defeated is fragile by design. Encode the asymmetric cost of errors in the objective rather than applying a threshold afterwards, because the two errors have very different prices and the model should know. Calibrate per merchant segment, as a score meaning different things across verticals makes thresholds unmanageable. Explain decisions well enough for an analyst to use, which connects to the review function. Red-team the model deliberately, since an adversary will and the vendor may as well go first. And evaluate on time-forward splits rather than random ones, because random cross-validation systematically overstates performance against a moving adversary.

## Target Customer
Data science and risk leadership, merchants exposed to attack campaigns, and fraud platform vendors competing on model quality.

## Impact If Built
Increasing the retraining cadence is the obvious response to drift and it substitutes for modelling the adversary at all. Representing campaigns as entities and detecting boundary probing makes adaptation visible before the chargebacks arrive.
