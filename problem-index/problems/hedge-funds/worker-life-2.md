# The Data Scientist Serving Twenty PMs

**Industry:** [[hedge-funds|Hedge Funds]]
**Type:** Worker Life Changing
**One-liner:** A central data scientist at a multi-manager platform spends most of the week re-mapping tickers and re-cutting the same datasets for pods that each want a slightly different answer, and almost none of it on research.
**Tags:** #feature-engineering #k-nearest-neighbors #word-embeddings #time-series-forecasting #data-integration #worker-facing #automation

## The Problem
Multi-manager platforms run central data teams that license alternative data once and serve dozens of pods. A data scientist on such a team fields requests all day: this PM wants card spend for her retail names by week; that one wants the same panel re-weighted by region; a third wants web traffic mapped to a company that just acquired a competitor. Each request requires the same unglamorous steps — map merchant names to securities, handle the acquisition, rebuild point-in-time history, check the panel for a vendor-side methodology change — before any analysis begins.

The mapping is never finished. Brands are sold, companies re-segment, vendors change their merchant taxonomy, and every change breaks someone's series silently. The data scientist finds out when a PM asks why the number jumped.

## Why It Matters to the Worker
These are people hired for research ability who spend their time on symbology and plumbing, judged by pods who see only whether the number arrived on time. The work is invisible when it goes right and blamed when it goes wrong, and with twenty internal clients the priorities are set by whoever shouts loudest. Turnover in these roles is high, and each departure takes the undocumented mapping decisions with it.

## What a Solution Looks Like
A maintained, versioned entity map from merchant, brand and app identifiers to securities, with suggested matches ranked by similarity and confirmed once rather than per request. Automatic detection of vendor methodology breaks and panel composition shifts before a PM sees them. Self-service cuts of common datasets for pods, with the data scientist reviewing rather than building. And a request log that shows which datasets and analyses pods actually use, so the team's time follows value.

## Impact If Solved
Freeing a central data scientist from repeated mapping and re-cutting returns a large share of their week to actual research — new signal construction, evaluation of new datasets — and makes the role one a talented person stays in.
