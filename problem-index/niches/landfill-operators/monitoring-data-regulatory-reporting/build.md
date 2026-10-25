# Groundwater Statistics That Explain Themselves

**Niche:** [[niches/landfill-operators/monitoring-data-regulatory-reporting/profile|Environmental Monitoring Data & Regulatory Reporting]]
**Industry:** [[industries/landfill-operators|Landfill Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every sampling event runs dozens of wells and constituents through statistical tests, and the false positives that follow cost months of resampling and alternate-source demonstrations.
**Tags:** #hypothesis-testing #bayesian-inference #large-language-models #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a landfill's monitoring data into regulatory reports that survive agency review, and whoever has the fewest deficiencies found by the agency per report takes the account.

## The Problem
Detection monitoring compares each well and constituent against background with statistical limits; with many comparisons, some exceed by chance, and each statistically significant increase triggers notification, resampling or a demonstration that another source caused it.

## Why Nobody Has Built This
Statistics software computes limits; consultants interpret them by hand; and the reasoning for alternate sources (seasonality, sampling artefacts, upgradient trends) is rewritten for each event.

## What to Build
A system that runs the permit's statistical method, controls the site-wide false-positive rate, screens each exceedance against seasonality, field parameters, lab qualifiers and upgradient trends, and drafts the notification or alternate-source demonstration with the evidence attached.

## Target Customer
Compliance directors at multi-site owners and the consultancies filing for public landfills.

## Impact If Built
Avoiding two false triggers a year at a site where each costs ~$25K in resampling and reports (estimate) saves ~$50K a year and keeps the site out of unnecessary assessment monitoring.
