# Distributed Crawling and Politeness

**Niche:** [[niches/web-data-extraction-firms/collection-infrastructure/profile|Collection Infrastructure]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Search engine crawling solved scheduling, freshness prediction, politeness and duplicate detection at web scale decades ago, and extraction fleets re-fetch on a cron.
**Tags:** #time-series-forecasting #graph-theory #evaluation-metrics #convex-optimization #automation #workflow-orchestration #descriptive-statistics #change-point-detection
**Contested on:** Not terminal — the contest differs by whether the problem is reaching the page or reading it, and the decomposition is recorded in the profile.

## The Problem
Deciding what to fetch, how often, and how hard to hit a host is the founding engineering problem of web search, with mature answers: change frequency estimation per page, crawl scheduling that allocates budget by expected value, per-host politeness with adaptive rate limiting, duplicate and near-duplicate detection, and frontier management. Extraction fleets mostly fetch everything on a fixed schedule and back off when blocked.

## What Already Exists
Crawl scheduling with change frequency estimation and freshness objectives; per-host politeness and adaptive rate limiting; duplicate and near-duplicate detection at scale; URL frontier management and prioritisation; sitemap and feed consumption for change signals; and conditional request mechanisms that avoid re-fetching unchanged content.

## The Customization Gap
The adaptation is to a fleet whose targets have not invited it. It requires: (1) change frequency estimation per page driving the schedule, since most re-fetches return unchanged content and predicting change would cut both cost and load substantially — this is the largest available efficiency gain and is standard practice in search; (2) politeness as a governance property rather than a blocking-avoidance tactic, because the current behaviour is calibrated to what a target will tolerate and the defensible posture is calibrated to what is reasonable, which matters when intent is evidence; (3) conditional requests and change signals used properly, which reduce load on the target and cost for the firm simultaneously and are widely ignored; (4) freshness objectives stated per customer, so the schedule serves a stated requirement rather than a default interval; and (5) frontier prioritisation by customer value, since crawl budget is finite and is currently allocated by schedule rather than by what anybody needs.

## Target Customer
Extraction firms, their customers, target site operators experiencing the load, and the crawling and information retrieval community.

## Impact If Solved
Search solved crawl scheduling and extraction fleets fetch on a cron. Change frequency estimation is the largest efficiency gain available and reduces cost and target load together; politeness calibrated to what is reasonable rather than to what is tolerated is the defensible posture when intent is evidence.
