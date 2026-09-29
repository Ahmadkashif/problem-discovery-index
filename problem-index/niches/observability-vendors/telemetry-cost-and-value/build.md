# Cutting by Volume Because Volume Is All You Can See

**Niche:** [[niches/observability-vendors/telemetry-cost-and-value/profile|Telemetry Cost & Value]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Observability spend rivals the infrastructure being observed, customers cut by volume because volume is the only attribute they can see, and nobody knows which signals have ever been read.
**Tags:** #gradient-boosting #k-means-clustering #logistic-regression #time-series-forecasting #confidence-intervals #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to tell an engineering organisation which telemetry is worth its cost — and whoever does that takes the budget conversation, because customers are currently cutting by volume, which is the only attribute they can see.

## The Problem
A platform team is told to reduce observability spend by a third. They sort by volume and start cutting: the noisiest service's debug logs, trace sampling reduced across the board, retention shortened globally from ninety days to thirty. Six weeks later an incident requires a trace that was sampled away and a log stream that was dropped, and diagnosis takes three hours longer than it should have. Some of what they cut had never been queried in a year; some of it was load-bearing. Nothing distinguished the two, and the platform that charged for all of it knew exactly which streams had been read and which had not.

## Why Nobody Has Built This
The commercial conflict is complete and explains the entire gap: an incumbent that tells customers what to stop paying for reduces its own revenue, and every incumbent prices by volume. The data required — query logs with the streams touched, alert definitions and their firing outcomes, investigation traces, ingestion cost per stream — is complete inside every platform. Investigation traces in particular, which record what an engineer actually looked at during an incident, are collected by some platforms and surfaced by none. The absence of the capability is a choice.

## What to Build
Value scoring per telemetry stream and the policy that follows. Score each stream on query frequency and recency, who queried it and in what context, whether it appeared in an incident investigation, and whether an alert built on it has ever fired usefully — then join to cost to produce a value-per-dollar ranking across the entire estate. Recommend retention and sampling per stream rather than globally: keep queried signals hot, preserve rare and unusual traces while dropping ordinary ones, and surface streams never read in a year for deletion with the evidence attached. Measure regret retrospectively, because the honest test is what proportion of dropped streams appear in subsequent investigations, and that number is directly measurable and is the one a customer will ask for. Summarise before dropping, so a discarded stream leaves aggregates and exemplars rather than nothing, which changes the risk of cutting. Report cost reduction achieved at a fixed regret rate, which is the summary metric this whole capability should be judged on. And build it at the collector layer, since the decision must be made before ingestion to save anything and that is exactly where the open standard has put the opportunity.

## Target Customer
Engineering and platform teams under cost pressure, which is most of them; the open collector ecosystem; and the cost management vendors for whom the incumbents' conflict of interest is the opportunity.

## Impact If Built
Customers are discarding the wrong data because the only visible attribute is the wrong one, and the value signal is complete and unexploited. Regret measurement is what makes the recommendation credible, and collector-layer implementation is what makes it commercially possible.
