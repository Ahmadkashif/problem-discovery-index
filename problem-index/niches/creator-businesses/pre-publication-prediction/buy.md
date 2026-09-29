# Headline and Creative Preference Testing

**Niche:** [[niches/creator-businesses/pre-publication-prediction/profile|Pre-Publication Prediction]]
**Industry:** [[industries/creator-businesses|Creator Businesses]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Digital publishing has tested headlines at scale for fifteen years and built models that predict them, and creators pick titles by feel.
**Tags:** #word-embeddings #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #transfer-learning #cnns #feature-engineering
**Contested on:** Every serious competitor in this niche is fighting to rank a creator's candidate titles, thumbnails, topics and formats before anything is published — and whoever predicts best against that creator's own audience changes what gets made.

## The Problem
News and digital publishing ran headline testing at industrial scale: multi-armed variants served to real traffic, models trained on the results, and libraries of what structures perform for which audiences. The practice is mature, the models are good, and the lessons are documented. Creators make the same decision — a short piece of text and an image that determine whether anyone clicks — with none of it.

## What Already Exists
Headline testing platforms with bandit allocation; click prediction models from text; image thumbnail testing; audience segment preference modelling; and documented pattern libraries.

## The Customization Gap
The adaptation is to one publication at a time in a recommendation feed. It requires: (1) a single item published at a time rather than parallel variants to a large traffic stream, which removes bandit allocation entirely and is the substantive difference; (2) distribution decided by a recommendation system rather than by placement on a page, so click-through is confounded with who was shown it; (3) a repeat audience that recognises the creator, where publishing headline models assume mostly new readers; (4) the thumbnail carrying as much weight as the title, which publishing models treat as secondary; and (5) a creator whose taste is part of the product, so a prediction that overrides voice is worse than useless.

## Target Customer
Creators and production teams, management companies, and headline optimisation vendors with no creator presence.

## Impact If Solved
Publishing's headline models assume parallel variants and placement-based distribution, and neither holds here. Predicting for a single publication into a recommendation feed, for a repeat audience, is the adaptation.
