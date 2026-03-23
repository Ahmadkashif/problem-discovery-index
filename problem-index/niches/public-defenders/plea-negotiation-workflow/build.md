# Plea Outcome Predictor and Benchmarking Engine

**Niche:** [[niches/public-defenders/plea-negotiation-workflow/profile|Plea Negotiation Workflow]]
**Industry:** [[industries/public-defenders|Public Defenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool tells a public defender whether the plea offer on the table is good, bad, or typical for this charge, this judge, this prosecutor, and this defendant profile — they rely entirely on gut feel and memory.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A public defender receives a plea offer: plead to a reduced charge, 18 months probation, $500 fine. Is this a good offer? The defender has no data to evaluate it. They can't look up what similarly-situated defendants received from this prosecutor, in front of this judge, for this charge, in this jurisdiction. They rely on their own experience — how many similar cases they've handled and what they remember about outcomes. A new defender with 6 months of experience has almost no basis for evaluation. A veteran with 15 years has intuition but no data. Neither can give their client an evidence-based recommendation.

## Why Nobody Has Built This
Plea offer data doesn't exist in structured form. Offers are made verbally, counter-offers are verbal, and the only recorded outcome is the final disposition. Building a predictor requires first building the data infrastructure — recording offers, defendant characteristics, charge details, judge, prosecutor, and outcomes across thousands of cases. No single office has done this systematically. Court administrative records capture dispositions but not the negotiation process. The chicken-and-egg problem (need data to build the tool, need the tool to collect the data) has prevented any progress.

## What to Build
A plea benchmarking system with two phases. Phase 1 (data collection): a lightweight input form where defenders record each plea offer received — charge, offer terms, defendant profile (age, criminal history, employment, housing), judge, prosecutor. Takes 60 seconds per entry. Phase 2 (prediction): after accumulating 12-18 months of data, a prediction model that takes a new case's characteristics and outputs: expected plea offer range, expected sentence range if convicted at trial, and a "deal quality" score comparing the current offer to the distribution of offers in comparable cases. Includes judge-specific and prosecutor-specific adjustment factors.

## Target Customer
Public defender offices with 20+ attorneys in jurisdictions with sufficient case volume (10,000+ annual dispositions) to generate statistically meaningful benchmarks.

## Impact If Built
Transforms plea negotiation from intuition-based to data-informed. New defenders immediately gain the benchmarking capability that currently takes 10+ years of experience to develop. Estimated 10-15% improvement in plea outcomes (sentence length, charge reduction) when defenders can identify and reject below-average offers with data support.
