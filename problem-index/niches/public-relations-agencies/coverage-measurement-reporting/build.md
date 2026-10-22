# Client-Specific Message Coding With a Consistency Score

**Niche:** [[niches/public-relations-agencies/coverage-measurement-reporting/profile|Coverage Monitoring & Measurement Reporting]]
**Industry:** [[industries/public-relations-agencies|Public Relations Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether coverage carried a client's messages is the core claim of every PR report and is coded by whoever is free that afternoon.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #hypothesis-testing #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to produce a de-duplicated, message-coded coverage report that a chief communications officer will defend to the CFO without advertising value equivalents, and whoever does it with the least analyst time per client keeps the measurement line.

## The Problem
A client's message house has four messages: the product is secure, the company is growing, the chief executive is an industry voice, the company supports local jobs. Each month 300 articles are coded for which messages they carried. Two account executives coding the same article often disagree, and next month a different person codes. Message pull-through trends move with the coder, not the coverage.

## Why Nobody Has Built This
Monitoring vendors sell cross-client sentiment models, not per-client coding, and agencies lack the volume to train their own classifiers. Until few-shot language models, each client's frame meant a new model.

## What to Build
A coding engine that takes each client's message house with a handful of example sentences per message, codes every piece at passage level (carried fully, partially, not at all) with the supporting quote, and runs a monthly double-coded sample to report agreement between the model and humans and between humans. The report shows the consistency score next to the trend, so a shift in pull-through can be trusted or questioned.

## Target Customer
Insight and measurement leads at agencies of 30–500 staff; in-house communications teams with measurement mandates.

## Impact If Built
Most of the coding hours removed, and a message pull-through trend a chief communications officer can defend because its reliability is stated.
