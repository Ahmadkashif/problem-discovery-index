# Linear Regression — Learning Plan

## Why Start Here

Linear regression is the Rosetta Stone of machine learning. It is one equation — `y = w₁x₁ + w₂x₂ + ... + wₙxₙ + b` — and every concept you learn here (features, targets, loss functions, gradient descent, overfitting, regularization, evaluation metrics) transfers directly to neural networks, gradient boosting, and every model you will ever use. Master this, and everything else is an extension.

## Prerequisites

- Python: comfortable with functions, loops, lists, dicts
- Libraries to install: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- No prior ML or statistics knowledge required
- Math will be introduced as needed — every equation is explained symbol by symbol

## The Three Projects

| # | Problem | Domain | Data | Difficulty | What You Learn |
|---|---------|--------|------|-----------|---------------|
| 1 | [[plans/linear-regression/project-1\|Building Energy Consumption]] | Energy / Climate | NYC LL84 — 35K buildings, single CSV | Beginner | Core LR end-to-end: load data → train → evaluate → interpret coefficients |
| 2 | [[plans/linear-regression/project-2\|Restaurant Health Inspections]] | Public Health / Food Safety | Chicago Open Data — 250K inspections, single CSV | Intermediate | Temporal feature engineering, benchmarking against a real deployed model |
| 3 | [[plans/linear-regression/project-3\|Crop Yield Prediction]] | Agriculture / Food Security | USDA + NOAA + Satellite — multi-source | Advanced | Multi-source data integration, domain-driven feature engineering, features > algorithms |

## How to Use This Plan

1. **Read [[plans/linear-regression/foundations\|Foundations]]** — understand the math and intuition before touching code
2. **Work through projects in order** — each builds on concepts from the previous
3. **For each project, follow the 4 phases:** Exploration → Baseline → Primary Model → Iteration
4. **After completing all 3:** move to the logistic regression plan (classification)

## Estimated Timeline

- Foundations: 3-5 days of focused study
- Project 1: 3-5 days
- Project 2: 5-7 days
- Project 3: 7-10 days
- Total: 3-4 weeks at ~2 hours/day
