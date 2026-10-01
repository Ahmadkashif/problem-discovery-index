# Two Analysts, One Footnote, Two Answers

**Niche:** [[niches/financial-data-vendors/standardised-fundamentals/profile|Standardised Fundamentals]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Standardisation consistency across issuers and analysts is the property clients assume and the one no vendor measures.
**Tags:** #evaluation-metrics #hypothesis-testing #descriptive-statistics #tacit-knowledge-ml #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to standardise a new filing correctly within hours and to show how each derived number was produced — and whoever does that best becomes the source every client's comp table and backtest silently trusts.

## The Problem
A screen comparing EBIT margins across an industry is only meaningful if comparable items were treated the same way at each issuer. Different analysts covering different issuers make different calls on comparable footnotes, and nothing surfaces it. Sample QA checks each value against policy, not against what was done at the peer.

## Why It's Still Broken
Consistency is a cross-sectional property and QA is designed per filing. There is no structured record of which items were judged comparable. And measuring disagreement is uncomfortable because it quantifies something the vendor sells as a given.

## What a Fix Looks Like
Route a sample of ambiguous items to two analysts blind and measure agreement by item type. Cluster similar footnote language across issuers and report treatment divergence within clusters. Feed divergences to policy owners as candidate clarifications. Publish internal consistency metrics alongside error rates.

## Who Feels the Pain
Clients comparing companies on numbers that were standardised differently; analysts graded on errors against a policy that leaves the hard cases open.

## Impact If Fixed
Makes comparability — the reason standardised data exists — a measured property rather than an assumption.
