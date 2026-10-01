# Standardising Broker Models That Were Never Meant to Be Compared

**Niche:** [[niches/sell-side-equity-research/estimates-consensus-data/profile|Analyst Estimates & Consensus Data Providers]]
**Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every contributed broker model has its own rows, segment splits and definitions, and mapping them to a common line-item taxonomy is done by analysts.
**Tags:** #transformers #large-language-models #word-embeddings #feature-engineering #evaluation-metrics #data-integration
**Contested on:** Every serious competitor in this pocket is fighting to deliver the most accurate expectation of each reported line item before the release — and whoever does that best becomes the benchmark every earnings surprise is measured against.

## The Problem
Line-item consensus requires that "North America organic growth" in one broker's model means the same as a differently named row in another's. Model-level aggregators employ analysts to map each contributed model into a standard template per company, and redo it when models change.

## What Already Exists
Schema matching and entity resolution practice from data integration; embedding-based matching of labels and values; financial statement standardisation in Capital IQ, FactSet and Bloomberg.

## The Customization Gap
Broker models carry analyst-specific adjustments and non-GAAP definitions, use row labels that are abbreviations, change structure between versions, and must be matched using the numbers as well as the labels — a row is identified as much by how its history relates to reported figures as by its name. The mapping must be versioned, auditable and respect each contributor's entitlement terms.

## Target Customer
Head of model content at a line-item consensus provider.

## Impact If Solved
Deeper and faster line-item consensus with fewer mapping analysts per contributed model.
