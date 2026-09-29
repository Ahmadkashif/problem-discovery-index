# Imputation Practice

**Niche:** [[niches/customer-data-platforms/profile-completeness-and-enrichment/profile|Profile Completeness & Enrichment]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistics has a rigorous theory of filling in missing values with honest uncertainty, and marketing fills them in by purchase.
**Tags:** #bayesian-inference #expectation-maximization #confidence-intervals #gradient-boosting #evaluation-metrics #monte-carlo-methods #probability-distributions #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to say what is missing from a profile and what can be inferred rather than bought — and whoever does that replaces a third-party data purchase with the organisation's own observations.

## The Problem
Filling in missing values is a solved statistical problem with a substantial literature. Multiple imputation preserves uncertainty rather than pretending a filled value is observed, model-based approaches use the full covariance structure, and the consequences of ignoring the distinction between observed and imputed are well documented. Survey research and clinical studies apply this routinely. Customer data enrichment fills gaps by purchasing values from a third party and storing them indistinguishably from observed ones.

## What Already Exists
Multiple imputation with uncertainty propagation; model-based and machine-learning imputation; missingness mechanism analysis; imputation diagnostics and validation; and conventions for reporting imputed data.

## The Customization Gap
The adaptation is to an operational database consumed by marketing systems. It requires: (1) a single stored value rather than multiple imputations, since downstream systems read a profile field and cannot consume a distribution — collapsing to a point while preserving the confidence alongside it is the practical compromise and the design problem; (2) imputation quality that varies enormously by customer, so the confidence must be per record rather than per field; (3) purchased values as an alternative source to compare against, which statistical imputation never has and which makes validation unusually tractable here; (4) privacy constraints on what may be inferred and used, which is a governance layer the statistical practice does not include; and (5) continuous rather than one-time imputation, since behaviour accumulates and an inference should improve every week.

## Target Customer
Data science and marketing teams, customer data platform vendors, and statistical practitioners for whom operational profile enrichment is unserved.

## Impact If Solved
Imputation theory insists on preserving uncertainty and marketing stores purchased values as facts. Collapsing to a point while carrying per-record confidence is the design compromise operational systems require, and purchased values give validation a benchmark statistics never has.
