# The Stale Estimate Sitting in Consensus

**Niche:** [[niches/sell-side-equity-research/estimates-consensus-data/profile|Analyst Estimates & Consensus Data Providers]]
**Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Fix (Pain Point)
**One-liner:** An analyst has not updated since the company changed guidance, and their old number still drags the consensus everyone measures against.
**Tags:** #gradient-boosting #survival-analysis #evaluation-metrics #feature-engineering #quick-win
**Contested on:** Every serious competitor in this pocket is fighting to deliver the most accurate expectation of each reported line item before the release — and whoever does that best becomes the benchmark every earnings surprise is measured against.

## The Problem
After a guidance change, covering analysts update over days or weeks. Until they do, their estimates sit in consensus. Vendors apply staleness filters by age, which drop estimates that are old but still correct and keep ones that are recent but pre-date the news.

## Why It's Still Broken
Staleness is defined by time since update rather than by whether material information has arrived since the estimate was made.

## What a Fix Looks Like
For each estimate, a modelled probability that it would be revised given the events since it was made — guidance changes, peer results, the analyst's own revision habits — with consensus shown both raw and adjusted, and the excluded estimates listed.

## Who Feels the Pain
Investors and IR teams reading a consensus that the market has already moved past; quant strategies trading on surprise against a stale benchmark.

## Impact If Fixed
A consensus that reflects current information, explained estimate by estimate.
