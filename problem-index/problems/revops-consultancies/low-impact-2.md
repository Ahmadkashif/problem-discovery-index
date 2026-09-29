# Territory and Quota Design

**Industry:** [[revops-consultancies|RevOps Consultancies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Territories and quotas are set annually in a spreadsheet by splitting last year's number, and the resulting inequity is the single largest driver of sales attrition nobody models.
**Tags:** #convex-optimization #gradient-boosting #confidence-intervals #k-means-clustering #causal-inference #evaluation-metrics #optimization-fundamentals #revenue-impact

## The Problem
Annual planning allocates accounts to representatives and attaches a quota to each. The method at most organisations is a spreadsheet: take last year's attainment, apply a growth factor, adjust for headcount changes, and balance territories by a proxy like account count or total addressable revenue.

The result is systematically unequal in ways that are visible afterwards and not modelled beforehand. Two representatives with nominally equivalent territories face very different realistic potential, because potential depends on account propensity, existing penetration, competitive presence, renewal timing and the quality of the installed base rather than on account count. One representative hits quota comfortably and one cannot reach it however they perform.

The consequences are well documented in practice. Attainment distribution is bimodal rather than centred. Attrition concentrates among representatives with unwinnable territories, and the organisation loses people who were performing well against a bad allocation. Mid-year territory changes to fix it disrupt customer relationships and reset pipeline.

Quota setting has the same structure. A number derived from last year's performance plus a growth expectation, applied uniformly, ignores that territories differ in how much growth is actually available.

## What Already Exists
Territory and quota planning software exists — Varicent, Xactly, Anaplan, Salesforce Maps — and handles the mechanics of allocation, hierarchy and crediting well. Incentive compensation management is mature. Data enrichment provides firmographic attributes for account scoring. Some revenue intelligence platforms surface attainment distribution. Most mid-market organisations do this in a spreadsheet regardless of what they own.

## The Customisation Gap
The tooling allocates against a proxy and the problem is estimating potential. What a territory is actually worth depends on each account's propensity to buy, expand or churn given its characteristics and history with this vendor — which is a modelling problem the organisation has the data for and solves nowhere.

With account-level potential estimated, allocation becomes a constrained optimisation with a clear objective: balance expected potential across representatives subject to geography, industry specialisation, relationship continuity and workload constraints. That is a well-understood problem shape and it is currently approximated by sorting a spreadsheet.

The essential output is the equity measurement. Showing the distribution of expected attainment across the proposed allocation — and how much of the variance is territory rather than performance — is the artefact that changes the planning conversation, because it makes visible the thing everyone suspects and nobody can demonstrate.

And the customisation is per-business: what predicts account potential differs completely between a vendor selling to enterprises through long cycles and one selling transactionally, so the potential model must be fitted to this organisation's own history rather than to firmographic scores bought off the shelf.

## Impact If Solved
Territory inequity drives attrition among people who were performing, and replacing a productive representative costs a year of ramp. Modelled potential with optimised, equity-measured allocation addresses a problem that every sales organisation knows it has, that is revisited annually under time pressure in a spreadsheet, and that has a clean mathematical shape once the potential estimate exists.
