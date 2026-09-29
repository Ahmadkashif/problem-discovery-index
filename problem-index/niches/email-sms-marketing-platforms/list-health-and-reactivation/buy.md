# Churn Modelling Practice

**Niche:** [[niches/email-sms-marketing-platforms/list-health-and-reactivation/profile|List Health & Reactivation]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Subscription businesses model churn and retention with real rigour, and email lists are managed with a rule about the last six months.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #bayesian-inference #causal-inference #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a brand which of its subscribers are still reachable and worth reaching — and whoever does that stops a list from being both a liability and an unworked asset at the same time.

## The Problem
Churn prediction and retention management are mature. Subscription businesses model the probability a customer lapses, segment by risk and value, target interventions at those where an intervention changes the outcome, and measure the uplift of doing so. The methods are well developed and the practice is standard. A marketing list has the same structure — subscribers who lapse, an intervention available, a value per retained subscriber — and is managed by a recency rule with no model behind it.

## What Already Exists
Churn prediction models with survival formulations; risk and value segmentation; uplift modelling for intervention targeting; retention campaign measurement; and win-back programme design.

## The Customization Gap
The adaptation is to a relationship with no contract and an ambiguous lapse event. It requires: (1) no clear churn event, since a subscriber who stops engaging has not cancelled and may return, so the target must be a continuous reachability-and-interest state rather than a binary — this ambiguity is the central modelling difference; (2) the possibility that the subscriber is reachable but filtered, which is a failure of the channel rather than of the relationship and has no subscription analogue; (3) intervention that itself causes harm, since messaging a fatigued subscriber accelerates the loss, making uplift modelling essential rather than optional; (4) very low value per subscriber, so the intervention must cost almost nothing and the modelling must be cheap at list scale; and (5) a deliverability consequence to keeping unreachable subscribers, which means the cost of inaction is collective rather than individual.

## Target Customer
Lifecycle and retention teams, messaging platforms, and churn modelling vendors for whom marketing lists are an unserved application.

## Impact If Solved
Subscription churn modelling assumes a clear lapse event and a contract, and a list has neither. Reachable-but-filtered has no subscription analogue, and an intervention that itself accelerates the loss makes uplift modelling essential rather than a refinement.
