# Real-Time Recommendation Practice

**Niche:** [[niches/live-commerce-platforms/stream-discovery/profile|Stream Discovery]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Real-time recommendation is a heavily engineered discipline in short-form video and news feeds, and live commerce imported it with its objective and its item model unchanged.
**Tags:** #transformers #matrix-decompositions #gradient-boosting #evaluation-metrics #transfer-learning #confidence-intervals #revenue-impact #automation
**Contested on:** This niche is not terminal — the fight over cold-start ranking and the fight over the ranking objective are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Serving a ranked feed to hundreds of millions of users in tens of milliseconds, with continuously updated features and online learning, is a solved and well-tooled engineering discipline. Live commerce inherited that machinery intact, which is why the infrastructure works and the matching does not: the borrowed system assumes a persistent item with accumulating history and an objective of watch time, and live commerce has neither. The engineering transferred and the problem definition did not.

## What Already Exists
Real-time feature stores and online serving infrastructure; two-stage retrieval and ranking architectures; multi-armed bandit exploration for new items; sequence models over user behaviour; and continuous online learning pipelines.

## The Customization Gap
The adaptation is from a persistent catalogue to perishable supply. It requires: (1) an item representation that expires and whose features change within its lifetime, which no feed architecture is built for and which is the structural change; (2) exploration budgeted against a deadline, since the usual approach of learning an item's value over days is unavailable when the item lasts two hours — this is where bandit practice needs genuine adaptation rather than tuning; (3) an objective built on purchase rather than dwell, which changes the labels, the training data and the evaluation together; (4) two-sided balance, because seller retention depends on audience and a pure viewer-value ranking starves new supply; and (5) in-stream state as a feature, which requires piping live audio-visual and transaction signal into the ranker at serving time — an input the borrowed stack has no path for.

## Target Customer
Live commerce platforms, marketplaces launching live formats, and recommendation infrastructure vendors whose products assume persistent items.

## Impact If Solved
The engineering transferred from short-form video and the problem definition did not. An item that expires and changes within its lifetime is the structural mismatch, and exploration under a two-hour deadline is where bandit practice needs real adaptation.
