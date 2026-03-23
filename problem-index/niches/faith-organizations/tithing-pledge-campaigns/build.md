# Giving Health Intelligence Dashboard

**Niche:** [[niches/faith-organizations/tithing-pledge-campaigns/profile|Tithing & Pledge Campaigns]]
**Industry:** [[industries/faith-organizations|Faith Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can analyze a church's giving data and surface actionable intelligence — giving concentration risk (what if our top 5 donors leave?), seasonal patterns, new-giver-to-regular-giver conversion rates, and early indicators of household financial distress that predict giving drops.
**Tags:** #gradient-boosting #time-series-forecasting #anomaly-detection #tabular-ml #revenue-impact

## The Problem
Churches know their total giving but lack the analytical tools to understand giving health. A church receiving $1.5M/year may not realize that 35% comes from 8 households (concentration risk), that summer giving drops 25% (seasonal pattern requiring reserves), that 70% of first-time givers never give a second time (conversion problem), or that a faithful family's giving just dropped 40% (possible job loss or health crisis requiring pastoral care). Finance committees review monthly totals in a spreadsheet but miss the story underneath the numbers. When giving declines, they discover the cause 6 months too late.

## Why Nobody Has Built This
Church giving data is sensitive — analyzing individual household giving patterns feels intrusive to many church leaders. The church software industry has been cautious about building analytical tools that might make pastors feel like they're profiling donors. Additionally, the analytical sophistication required (time-series decomposition, cohort analysis, concentration metrics) exceeds what most church software developers build. Nonprofit fundraising tools (Bloomerang, DonorPerfect) provide similar analytics, but churches resist using "fundraising" tools for theological reasons.

## What to Build
A giving health dashboard that ingests transaction data from any giving platform (Pushpay, Tithe.ly, Planning Center Giving) and surfaces: giving concentration (top donor dependency), giving velocity (trend by cohort — new, regular, declining, lapsed), seasonal patterns with 12-month forecast, pledge fulfillment rate with at-risk pledges flagged, new-giver retention curve, and pastoral care alerts (sudden giving drops that may indicate household distress). All analytics use church-appropriate language — "stewardship health" not "donor retention."

## Target Customer
Executive pastors and finance committee chairs at churches with $500K+ annual giving who make budget decisions based on incomplete giving data.

## Impact If Built
Provides 6-month giving forecasts that improve budget planning accuracy from ±20% to ±5%, identifies at-risk donor households 3 months earlier for pastoral intervention, and reduces giving concentration risk by surfacing dependency on top givers.
