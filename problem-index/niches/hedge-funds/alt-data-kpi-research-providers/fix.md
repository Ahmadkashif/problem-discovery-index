# The Analyst Who Maintains Thirty Panel-to-KPI Mappings by Hand

**Niche:** [[niches/hedge-funds/alt-data-kpi-research-providers/profile|Alternative Data KPI Research Providers]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Fix (Pain Point)
**One-liner:** Each covered ticker depends on a hand-maintained mapping of merchants and brands to reported segments, and when a company re-segments or acquires a brand, the analyst finds out from a bad estimate.
**Tags:** #word-embeddings #change-point-detection #feature-engineering #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this pocket is fighting to put the most accurate pre-earnings KPI estimate in front of a fund on the most tickers — and whoever can show a graded, calibrated track record per ticker takes the renewal.

## The Problem
Analysts at KPI vendors cover many tickers each, and every quarter re-check which merchant descriptors, apps or domains map to which reported segment. Corporate actions and re-segmentations break mappings silently.

## Why It's Still Broken
The mapping knowledge is held per analyst, and the vendor scales by adding analysts.

## What a Fix Looks Like
A shared, versioned mapping with suggested matches for new merchants, alerts on filings that announce acquisitions or re-segmentation for covered tickers, and change-point detection on each ticker's panel-to-reported ratio.

## Who Feels the Pain
Research analysts at KPI vendors in the weeks before each print.

## Impact If Fixed
Analysts cover more tickers with fewer errors, which is the vendor's main lever on margin.
