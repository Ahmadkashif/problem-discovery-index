# Underwriting That Learns From Its Own Declines

**Niche:** [[niches/retail-pos-platforms/merchant-underwriting-risk/profile|Merchant Underwriting & Risk]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An underwriting model trained only on approved merchants learns the shape of the existing policy rather than the shape of risk, and every payments platform trains on approved merchants because the declined ones have no outcome.
**Tags:** #logistic-regression #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #cross-validation #causal-inference #compliance
**Contested on:** Every serious competitor in merchant onboarding is fighting to approve a merchant in minutes at the same loss rate a week of manual review would produce — and whoever holds that trade-off best takes the volume.

## The Problem
A platform declines merchants in certain categories, with certain business ages, in certain geographies, because its policy says so. Those merchants never process, so no loss data exists for them, so the model that replaces the policy is trained exclusively on the population the policy already allowed. It reproduces the policy, including whatever the policy gets wrong, and reports excellent performance on the only population it can evaluate. The platform's actual question — which of the merchants we are declining would have been fine — is structurally unanswerable with the data it collects, and almost nobody does anything about it.

## Why Nobody Has Built This
Deliberately approving merchants the policy would decline means accepting known expected losses to learn, which requires someone senior to authorise a budget for losses — an unusual conversation in a risk function whose entire measurement is loss reduction. The statistical framing, that this is a selection problem requiring exploration, is well understood in credit and less commonly applied in payments risk, where the teams are frequently built from fraud operations rather than from credit modelling. And the incremental approach — tighten when losses rise, loosen when growth is needed — feels responsive and lets the question stay unasked.

## What to Build
An underwriting system with an explicit exploration allocation. A small, bounded, deliberately chosen slice of applications that the current policy would decline is approved with controlled exposure — low limits, extended reserves, closer monitoring — specifically to generate outcome data on the decline population. That population is chosen to be informative rather than random, concentrating near the decision boundary where the policy's correctness is most uncertain. Losses from exploration are budgeted and tracked as a cost of information rather than as failures. The model is then trained on a population that includes both sides of the boundary, with the selection handled properly, and the approval threshold is set against a stated expected-loss target rather than inherited. Fairness review belongs here explicitly: an underwriting model trained on historical decisions can encode geographic and demographic patterns that have nothing to do with risk, and a platform declining small businesses should be testing for that rather than assuming its absence.

## Target Customer
POS platforms, acquirers and ISOs whose growth is bounded by approval rate and whose losses are bounded by policy, and the risk functions inside them.

## Impact If Built
Exploration is the only mechanism that answers what a decline policy costs in foregone merchants, and platforms that run it typically discover that specific declined segments perform acceptably — which is growth available at a known loss rate rather than at an unknown one. The fairness testing is a second-order benefit that is hard to justify on its own and easy to include once the evaluation infrastructure exists.
