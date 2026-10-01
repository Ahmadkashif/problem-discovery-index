# The Stale Price Nobody Flagged

**Niche:** [[niches/financial-data-vendors/evaluated-pricing-desks/profile|Fixed-Income Evaluated Pricing]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** An evaluated price that has not moved for a week while its sector repriced is a stale price, and fund administrators find it before the provider does.
**Tags:** #change-point-detection #descriptive-statistics #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to price illiquid bonds defensibly every day and survive the client's price challenges — and whoever's evaluations hold up under challenge keeps the fund administrator's NAV process.

## The Problem
Unchanged evaluations are expected for some instruments and a defect for others. Administrators run stale-price reports and challenge; the provider responds after the fact.

## Why It's Still Broken
Staleness is checked with fixed thresholds that do not account for what the comparables did.

## What a Fix Looks Like
Flag evaluations that did not move when their comparable set or sector curve did, before release, routed to the responsible evaluator.

## Who Feels the Pain
Evaluators fielding avoidable challenges; administrators and fund boards relying on the prices.

## Impact If Fixed
Fewer challenges and fewer stale-price exceptions in NAV oversight.
