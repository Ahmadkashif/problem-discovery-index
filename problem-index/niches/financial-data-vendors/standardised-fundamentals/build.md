# Learning the Senior Collector's Mapping

**Niche:** [[niches/financial-data-vendors/standardised-fundamentals/profile|Standardised Fundamentals]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The best collectors map ambiguous line items in a way they cannot fully articulate, and that judgement — the vendor's real moat — has never been learned by a model.
**Tags:** #tacit-knowledge-ml #transformers #large-language-models #k-nearest-neighbors #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to standardise a new filing correctly within hours and to show how each derived number was produced — and whoever does that best becomes the source every client's comp table and backtest silently trusts.

## The Problem
On routine items, XBRL plus rules are right. On the five or ten judgement items per filing — a gain buried in other income, a reclassified segment, compensation spread across lines — the outcome depends on who is collecting. Senior analysts are reliably better and slower to explain why.

## Why Nobody Has Built This
The decision path is unrecorded, the labels are noisy because experts disagree and policy drifts, and an assistant that must be double-checked is slower than no assistant. These are the three tacit-knowledge obstacles, and none is a modelling problem.

## What to Build
Instrument the collection tool to capture overrides with the source passage. Stamp history with policy versions and adjudicate a disagreement sample to measure the human ceiling. Train retrieval-plus-classification on the issuer's own history and peer precedents, with calibrated abstention. Ship it as pre-mapping with evidence so the routine majority is skipped and the ambiguous minority goes to seniors.

## Target Customer
Head of fundamentals content and content technology at standardisation vendors.

## Impact If Built
Turns the most valuable and most perishable expertise in the business into a versioned asset, and compresses time-to-standardised-data on earnings night.
