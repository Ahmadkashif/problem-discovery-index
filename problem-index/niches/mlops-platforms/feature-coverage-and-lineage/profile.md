# Feature Coverage & Lineage

**Parent Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to extend the consistency guarantee to the features that were never registered — and whoever does that takes the account, because the unregistered features are the majority and are where the failures are.

## Profile
**Market Size:** ~$290M US
**Share of Parent Industry:** ~10% of category revenue
**Digital Adoption:** Low — the guarantee is real and covers a minority
**Target Buyer:** Data and ML platform teams
**Automation Potential:** High — discovery and lineage are both mechanical

## What Makes This a Distinct Niche
Feature stores were built to guarantee that training and serving see the same values, and they deliver it — for features defined inside them. A real model's input vector is assembled from registered features, columns read directly from a warehouse table, values computed inline in the serving handler, fields pulled from an upstream service response, and constants somebody hard-coded. The store's guarantee covers the first category and says nothing about the rest, and no tool reports the ratio. The contest here is coverage: knowing what fraction of a model's inputs are actually governed, finding the ungoverned ones automatically, and extending lineage across the boundary so that a change to an upstream table is known to affect a specific model in production.

## Current Tools & Gaps
Feature stores with registration, offline and online serving, and point-in-time joins; data catalogues with column-level lineage that stops at the warehouse edge. The gaps: no measure of what share of a model's inputs are registered; no discovery of unregistered features from the serving path; lineage that does not cross from the data platform into the model, so an upstream schema change reaches production models undetected; and no ownership record for a feature, so when one breaks, nobody knows whose it is.

## Problems
- [[niches/mlops-platforms/feature-coverage-and-lineage/build|🔨 Build: A Guarantee That Covers a Minority of Features]]
- [[niches/mlops-platforms/feature-coverage-and-lineage/buy|🛒 Buy: Data Catalogues and Column-Level Lineage]]
- [[niches/mlops-platforms/feature-coverage-and-lineage/fix|🔧 Fix: The Upstream Schema Change Nobody Told the Model About]]
