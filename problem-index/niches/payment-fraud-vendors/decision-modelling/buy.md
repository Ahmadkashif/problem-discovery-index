# Adversarial Machine Learning

**Niche:** [[niches/payment-fraud-vendors/decision-modelling/profile|Decision Modelling]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Adversarial machine learning is a developed research field about models under attack, and fraud decisioning — the largest real-world instance — barely references it.
**Tags:** #contrastive-learning #gradient-boosting #evaluation-metrics #confidence-intervals #graph-neural-networks #hypothesis-testing #change-point-detection #transfer-learning
**Contested on:** Every serious competitor in this niche is fighting to build the best decision from device, behavioural, network and consortium signals against an adversary who adapts — and whoever models best on the labels that exist wins the transactions everybody else gets wrong.

## The Problem
There is a substantial literature on machine learning under adversarial conditions: evasion attacks, model extraction through querying, robustness guarantees, and the analysis of what an attacker can learn from a model's responses. Most of it was developed on image classifiers and academic benchmarks. Payment fraud is the largest continuously running adversarial machine learning system in commercial use, and the two bodies of practice barely touch.

## What Already Exists
Evasion and model extraction attack literature; robustness certification methods; adversarial training techniques; query-based extraction defences; and red-teaming methodology for models.

## The Customization Gap
The adaptation is from a perturbation-based threat model to an economic one. It requires: (1) an attacker constrained by cost and payoff rather than by a perturbation budget, which changes what robustness means and is the substantive translation; (2) queries that are real transactions with real cost to the attacker, so extraction is bounded economically rather than mathematically; (3) tabular and graph data rather than images, where most robustness results do not transfer; (4) many attackers of very different sophistication simultaneously, rather than a single worst-case adversary; and (5) a decision that must remain fast and explainable, which rules out many robustness techniques outright.

## Target Customer
Data science and risk leadership, security research teams, and machine learning platform vendors serving adversarial domains.

## Impact If Solved
The research field developed on image classifiers and the largest real adversarial system is commercial fraud. Translating robustness from a perturbation budget to an economic constraint is the adaptation and would inform both sides.
