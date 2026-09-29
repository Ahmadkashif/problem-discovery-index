# Exploit Prediction and Risk Scoring That Exist

**Niche:** [[niches/software-supply-chain-security/finding-prioritisation/profile|Finding Prioritisation]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Exploit prediction scoring provides a probabilistic estimate of whether a vulnerability will actually be exploited, is published and free, and few tools use it well.
**Tags:** #gradient-boosting #logistic-regression #bayesian-inference #confidence-intervals #evaluation-metrics #cross-validation #hypothesis-testing #compliance
**Contested on:** Every serious competitor in this niche is fighting to turn thousands of findings into the handful that matter for this application — and whoever does that takes the account, because the ratio between what the category reports and what is worth acting on is its central unresolved problem.

## The Problem
A probabilistic exploit prediction score exists, is published, is free, and estimates the likelihood that a given vulnerability will be exploited — which is a far better prioritisation signal than a severity rating describing how bad exploitation would be if it happened. Published analyses consistently show that severity and exploitation are weakly related. The category's tools display the severity rating prominently and the exploitation estimate, where they show it at all, as a secondary field.

## What Already Exists
Exploit prediction scoring with published methodology and free access; known-exploited vulnerability catalogues maintained by national authorities; the severity scoring specification including its environmental and temporal components, which are designed for exactly this contextualisation and are almost never used; threat intelligence feeds; and the vulnerability management literature on risk-based prioritisation.

## The Customization Gap
The adaptation is to a specific application rather than to a vulnerability in general. It requires: (1) using the severity specification's contextual components, which exist precisely to adjust a base score for the environment and are omitted by nearly every tool — this is available immediately and is the cheapest available improvement; (2) combining exploitation likelihood with application-specific reachability, since a highly exploitable vulnerability in unreachable code is not a priority and the two signals are multiplicative rather than additive; (3) calibration against the organisation's own outcomes, since the general prediction is population-level and this organisation's exposure differs — and their own dismissal and incident history is the calibration set; (4) explicit decision support rather than a score, because a security engineer needs to know what to do this week and a ranked probability is an input to that rather than the answer; and (5) honest communication of uncertainty, since prioritisation means accepting risk on the deferred items and an organisation should know how much.

## Target Customer
Composition analysis and vulnerability management vendors, application security functions, and the threat intelligence providers whose data this uses.

## Impact If Solved
A better prioritisation signal is published and free and is used as a secondary field, while the severity specification's own contextual components are ignored. Using them is immediate, and multiplying exploitation likelihood by reachability is the combination that produces a short list.
