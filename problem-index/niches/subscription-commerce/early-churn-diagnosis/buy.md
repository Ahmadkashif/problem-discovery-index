# Survival Analysis and Onboarding Practice

**Niche:** [[niches/subscription-commerce/early-churn-diagnosis/profile|Early Churn Diagnosis]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Survival analysis handles time-to-event data with covariates and censoring, and subscription commerce uses a monthly percentage.
**Tags:** #survival-analysis #hypothesis-testing #confidence-intervals #gradient-boosting #evaluation-metrics #probability-distributions #cross-validation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to know why the first three deliveries fail — and whoever does that takes the economics, because that is where nearly all the churn happens and the reasons are specific and fixable.

## The Problem
Analysing when an event happens, what predicts it and how covariates change the hazard, with proper treatment of subjects who have not yet experienced it, is what survival analysis does. It is taught everywhere, implemented in every statistical library, and is the correct tool for subscription churn — which is time-to-event data with censoring and covariates. The category uses a monthly percentage, which discards the timing structure that contains the entire finding.

## What Already Exists
Survival and hazard modelling with covariates; competing risks methods for distinguishing cancellation types; discrete-time hazard models suited to a cyclical delivery structure; activation and onboarding practice from consumer software; and cohort retention curve analysis with statistical comparison.

## The Customization Gap
The adaptation is to a hazard concentrated in the first few discrete events. It requires: (1) discrete-time hazard modelling on delivery number rather than continuous time, since the risk attaches to the delivery event rather than to elapsed days — this framing is what makes the front-loading legible and is not how the platforms report; (2) competing risks separating voluntary cancellation from payment failure and from pause, since these have different causes and remedies and are pooled in every churn figure; (3) covariates from operational events — delivery condition, timing, contents, skips — which are available here and which conventional churn modelling in software does not have; (4) intervention evaluated causally rather than by comparing treated and untreated groups that differ by selection, which is where most retention programmes overstate themselves; and (5) activation defined as reaching the delivery at which the hazard drops, which gives onboarding a concrete target that the software framing supplies and this category has not adopted.

## Target Customer
Subscription operators, subscription platform vendors, and the applied statistics community for whom this is an unusually clean time-to-event problem being handled with a percentage.

## Impact If Solved
Churn here is time-to-event data with censoring and covariates, handled with a monthly percentage that discards the timing structure containing the finding. Discrete-time hazard on delivery number is the framing that makes the front-loading legible.
