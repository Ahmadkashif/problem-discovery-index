# Criticality Scoring That Already Exists

**Niche:** [[niches/open-source-commercial-vendors/long-tail-critical-dependencies/profile|Long-Tail Critical Dependencies]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Criticality scoring for open-source projects exists as published open methodology, and funding allocation does not use it.
**Tags:** #graph-theory #spectral-graph-theory #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #descriptive-statistics #compliance
**Contested on:** Every serious competitor here is fighting to identify which unfunded projects the software economy actually depends on and get resources to them before they fail — and whoever does that takes the funding function, because the current allocation is driven by visibility rather than by dependence.

## The Problem
Several open projects publish criticality scores for open-source software, computed from dependents, contribution activity and other public signals, with documented methodology. Dependency graph data is published by the package ecosystems. Network centrality has a deep literature. The analysis that would identify the industry's fragile load-bearing dependencies is available and the funding decisions are made from a different set of inputs entirely.

## What Already Exists
Published criticality scoring methodologies with open implementations; ecosystem-wide dependency graph datasets; network centrality measures including the eigenvector and PageRank family, which are the right shape for weighted dependence; project health metrics frameworks from the open-source community; and vulnerability and incident histories.

## The Customization Gap
The adaptation is from a score to a funding and risk decision. It requires: (1) dependence weighted by the importance of the dependent rather than counted, since being depended on by ten critical systems differs from being depended on by ten thousand hobby projects, and centrality measures over the weighted graph capture this directly; (2) fragility as a separate axis rather than folded into one score, because the actionable target is high dependence and high fragility, and a single composite hides exactly that combination; (3) succession risk as an explicit factor — single maintainer, single publication credential, no documented handover — since these are the realised failure modes and generic health metrics do not capture them; (4) organisation-specific views, because a global list is a public good that nobody owns and an enterprise's own exposure list has an owner with a budget; and (5) an outcome measure, since the point is to prevent failures and a scoring system nobody validates against subsequent abandonments and compromises is an opinion with arithmetic.

## Target Customer
Foundations and funding programmes, corporate open-source offices, security and risk functions, and the software composition analysis vendors for whom this is an adjacent capability.

## Impact If Solved
The scoring methodology is published and open and is not used by the funders, which leaves a solved analytical problem disconnected from the decision it should inform. Separating fragility from dependence and producing organisation-specific views are the two adaptations that turn a public good into something with an owner.
