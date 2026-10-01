# Thematic Exposure Classified by Hand

**Niche:** [[niches/asset-managers/index-providers-research/profile|Index Providers' Research & Methodology Teams]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Deciding which companies belong in an AI, robotics or clean-energy index means analysts reading segment disclosures for thousands of companies, and the judgment calls are inconsistent and undocumented.
**Tags:** #tacit-knowledge-ml #large-language-models #bert #word-embeddings #evaluation-metrics #automation
**Contested on:** Every serious competitor in this pocket is fighting to design, test, document and govern custom and thematic indexes faster than rivals without compromising methodology integrity — and whoever does that wins the ETF, separate-account and direct-indexing launches that drive licensing revenue.

## The Problem
Thematic indexes select companies by exposure to a theme, often measured as share of revenue. Segment reporting rarely maps to themes, so analysts read filings, websites and transcripts and judge exposure. Experienced analysts develop a feel for where the boundaries sit; newer ones draw them differently. The theme definitions themselves drift as markets change.

## Why It's Still Broken
The task looks like simple classification but depends on judgment about ambiguous business lines, and the analysts' reasoning is recorded as a score without the evidence behind it.

## What a Fix Looks Like
Language-model extraction of theme-relevant revenue lines and evidence passages from filings, with a proposed exposure score and the passages cited; analysts confirm or adjust, and their adjustments become training labels. Inter-analyst agreement is measured on overlapping samples, which surfaces where the theme definition needs tightening.

## Who Feels the Pain
Thematic index analysts; asset managers whose ETF holdings are questioned by investors asking why a company is in the fund.

## Impact If Fixed
Classifications become faster, consistent and evidenced, and expert boundary judgment is preserved as labelled data.
