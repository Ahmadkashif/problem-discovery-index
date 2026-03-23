# Matched-Pair Adjustment Derivation from MLS Sales Data

**Niche:** [[niches/real-estate-appraisers/comp-selection-and-adjustment/profile|Comp Selection & Adjustment Workflow]]
**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Type:** Fix (Pain Point)
**One-liner:** USPAP expects market-supported adjustments derived from local sales data, but matched-pair analysis — finding two sales that differ in only one attribute to isolate that attribute's value — takes 1-2 hours per adjustment category and is so tedious that most appraisers skip it, using unsupported rule-of-thumb adjustments that CU increasingly flags.
**Tags:** #linear-regression #automation #compliance #data-integration

## The Problem
The gold standard for adjustment derivation is matched-pair analysis: find two recent sales in the same neighborhood that differ only in the attribute being valued (one has a garage, the other doesn't — everything else is identical) and the price difference is the adjustment amount. In practice, perfect matched pairs are rare. The appraiser searches the MLS for near-matches, identifies 2-3 pairs with "acceptable" differences, and manually calculates the implied adjustment — controlling for the other differences that aren't perfectly matched. This process takes 1-2 hours per adjustment category (GLA, garage, bathroom, condition) and must be repeated periodically as market conditions change. Most appraisers skip matched-pair analysis entirely, using adjustment tables from training or personal experience — which CU is now flagging as "unsupported adjustments."

## Why It's Still Broken
MLS data contains the information needed for matched-pair analysis, but extracting it requires systematic searching that MLS interfaces don't support. The appraiser needs to query: "show me all recent sales in this submarket where the only material difference between any two sales is the presence of a garage" — a query that requires comparing every pair of sales across multiple attributes simultaneously. This combinatorial search is trivial computationally but impossible through a standard MLS search interface.

## What a Fix Looks Like
An automated matched-pair extraction tool that: searches recent MLS sales in the subject's submarket; identifies pairs with minimal differences except for the target attribute; calculates the implied adjustment per pair; presents the median adjustment with confidence interval from multiple pairs; and generates a USPAP-compliant adjustment support addendum. The appraiser runs the tool for each adjustment category and gets market-supported values in 5-10 minutes instead of 1-2 hours.

## Who Feels the Pain
Every residential appraiser who needs market-supported adjustments — approximately 50,000-60,000 nationally, of whom 70%+ currently use unsupported adjustments that CU increasingly flags.

## Impact If Fixed
Adjustment derivation drops from 1-2 hours per category (or is skipped entirely) to 5-10 minutes. CU flags for unsupported adjustments decrease substantially. Appraisal defensibility improves in appeal and litigation because every adjustment is backed by identified market evidence.
