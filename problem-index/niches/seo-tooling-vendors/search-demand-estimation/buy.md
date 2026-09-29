# Panel Estimation Practice

**Niche:** [[niches/seo-tooling-vendors/search-demand-estimation/profile|Search Demand Estimation]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Media measurement has run panel-based estimation with published error properties for decades, and search tooling extrapolates a panel and prints an integer.
**Tags:** #confidence-intervals #bayesian-inference #descriptive-statistics #hypothesis-testing #monte-carlo-methods #evaluation-metrics #probability-distributions #law-of-large-numbers-and-clt
**Contested on:** Every serious competitor in this niche is fighting to produce demand and difficulty numbers that are honest about their own error — and whoever does that displaces a market built on extrapolations displayed as integers.

## The Problem
Panel-based audience measurement is an old and rigorous discipline. Television and radio ratings, readership surveys and retail panels all extrapolate from samples, and the practice includes published sampling methodology, weighting, minimum reporting thresholds below which a figure is suppressed, and stated error properties. Industry bodies audit it. Search tooling runs exactly this kind of panel extrapolation and reports every figure as an exact number with no threshold, no weighting disclosure and no error.

## What Already Exists
Panel design, recruitment and weighting methodology; minimum reporting thresholds and suppression rules; published error and reliability properties; independent audit of measurement methodology; and industry currency standards.

## The Customization Gap
The adaptation is to a population of queries rather than of people, at enormous cardinality. It requires: (1) millions of distinct estimands rather than a few hundred programmes, which makes per-item reporting thresholds the central design question — media measurement suppresses below a threshold and search tooling reports everything, which is the specific discipline to import; (2) an extremely long tail where most items have almost no panel observations, so hierarchical pooling across semantically related queries is necessary rather than optional; (3) panel composition biased toward users who install measurement software, which needs correction and is currently unaddressed; (4) customers who are individual marketers rather than an industry body, so there is no institution to enforce a standard and the vendor must self-impose it; and (5) no audited currency, which is the gap an industry body could fill and which nobody has convened.

## Target Customer
SEO tooling vendors, marketing measurement teams, and audience measurement bodies for whom search demand is an unstandardised currency.

## Impact If Solved
Media measurement suppresses figures below a reporting threshold and search tooling reports everything as an integer. Per-item thresholds and hierarchical pooling across related queries are the two disciplines that would make the tail honest.
