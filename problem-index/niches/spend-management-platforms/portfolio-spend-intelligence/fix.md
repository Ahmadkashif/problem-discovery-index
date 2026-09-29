# The Benchmark Every Customer Asks For

**Niche:** [[niches/spend-management-platforms/portfolio-spend-intelligence/profile|Portfolio Spend Intelligence]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every finance leader wants to know whether their spending is normal for a company like theirs, and the platform that could tell them shows them only themselves.
**Tags:** #descriptive-statistics #quick-win #evaluation-metrics #automation #confidence-intervals #compliance #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn line-item purchasing across thousands of companies joined to their bank balances into answers nobody else can produce — and whoever organises it holds a real-time read on how businesses spend and how that relates to their survival.

## The Problem
A CFO asks whether their software spend per employee is high. Whether their travel budget is out of line. Whether they are paying more for a particular vendor than comparable companies. These are the most common questions finance leaders have and the platform can answer all of them from data it already holds. Instead it shows the customer their own numbers over time, which answers none of them, and the CFO goes to a peer group or a consultant for a worse version of the answer.

## Why It's Still Broken
The product was built as a system of record, so every view is scoped to the customer's own data — the tenancy model became the analytical boundary without anyone deciding it should be. Cross-customer aggregation needs a governance answer nobody has written. Nobody counted how often customers ask. And it is seen as a data product rather than as a feature.

## What a Fix Looks Like
Ship the benchmark. Produce aggregate benchmarks by size, sector and stage for the most-requested categories, which is the fix and is straightforward aggregation over data already held. Start with the questions customers actually ask — spend per employee by category, vendor pricing, headline ratios — rather than building a general analytics surface. Set aggregation thresholds so no individual company is identifiable, which is the governance minimum and is well understood. Write the consent and use basis explicitly, because doing this without one is the way it goes wrong. Show the customer their position in the distribution rather than a single average, since the spread is the useful part. Refresh continuously, as the data arrives daily and a stale benchmark is a report. Let customers choose their comparison set within limits, because relevance is what makes a benchmark persuasive. Flag the categories where the customer is a notable outlier, which is the insight and is what a consultant would charge for. Measure how often benchmarks are viewed, since it will justify further investment. And ask customers which comparisons they want, as they have been asking informally for years.

## Who Feels the Pain
Finance leaders guessing whether their spend is reasonable; controllers asked questions they cannot answer; platforms leaving their clearest differentiator unbuilt; and customers paying consultants for a worse version.

## Impact If Fixed
The tenancy model became the analytical boundary without anyone deciding it should be. Aggregated benchmarks answer the questions finance leaders actually ask, from data already held, and no competitor without the portfolio can copy them.
