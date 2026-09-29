# Client Reporting and Metric Definitions

**Industry:** [[performance-marketing-agencies|Performance Marketing Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Pipeline vendors solved getting the data into a dashboard, and left untouched the part that consumes the week — agreeing what the numbers mean and writing what happened.
**Tags:** #large-language-models #time-series-forecasting #change-point-detection #gradient-boosting #evaluation-metrics #data-integration #workflow-orchestration #automation

## The Problem
Every agency builds and rebuilds client reporting. The data extraction is a solved problem, and the remaining work is not extraction at all. It is that each client defines their metrics differently — this one counts a lead at form fill, that one at qualification, a third at opportunity; one uses gross revenue, another net of returns, another contribution margin after shipping. Those definitions live in a strategist's memory and a spreadsheet formula, and they diverge quietly until a number in a deck disagrees with a number in the client's board pack.

Then there is the writing. A weekly report is charts plus a narrative explaining what moved and why. The charts assemble themselves; the narrative is written by an account manager on Thursday, from scratch, for every client, and is the part the client actually reads. A quarterly business review is the same at four times the length with a strategy section.

The recurring failure is silent: a tracking break, a feed outage, a platform changing an attribution default, a conversion event misfiring after a site release. These corrupt the numbers upstream of everything, and are typically discovered when a figure looks wrong in a meeting.

## What Already Exists
Supermetrics, Funnel, Fivetran and Adverity move platform data into warehouses and dashboards reliably. Looker Studio, Tableau and Power BI visualise it. Agency-specific platforms — TapClicks, AgencyAnalytics, Swydo — package the whole loop for smaller shops. Larger agencies run their own warehouse with dbt models encoding client metric logic, which is the right architecture and is built from scratch at every agency independently.

## The Customisation Gap
Metric definitions are the actual product of a reporting system and are treated as configuration. What a client's business calls a conversion, how returns and cancellations are handled, what margin assumptions apply, which spend is in scope — these are semantic decisions made once, recorded inconsistently, and silently broken when someone edits a formula. A definition layer with versioning, provenance and a record of who agreed what, reconciled against the client's own finance numbers, is what would actually stop the disagreements, and it is a different thing from a dashboard.

Data quality monitoring is the second gap and the one that costs the most credibility. A tracking break is detectable the day it happens: conversion volume departing from its own forecast, a platform feed arriving with a different schema, a conversion rate stepping at a deployment. The tooling reports what arrived, not whether what arrived is plausible.

The narrative is the third. Explaining what moved is a decomposition problem — spend, efficiency, mix, seasonality, a platform change — and the decomposition is computable from the same data the charts use. A drafted narrative grounded in the actual decomposition leaves the account manager to add the judgement and the recommendation, which is the part that needs a person.

## Impact If Solved
Reporting is the largest unbillable time sink in an agency and the most common source of client friction, because every disputed number costs trust disproportionately. A versioned definition layer ends the disputes, quality monitoring turns silent corruption into an alert, and drafted narratives return the single largest block of recurring hours in the account team's week — all without touching the part of reporting clients actually value, which is somebody thinking about their business.
