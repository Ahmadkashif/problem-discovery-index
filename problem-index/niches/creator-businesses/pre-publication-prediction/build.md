# Ranking the Options Before Publishing

**Niche:** [[niches/creator-businesses/pre-publication-prediction/profile|Pre-Publication Prediction]]
**Industry:** [[industries/creator-businesses|Creator Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The creator has five titles and three thumbnails and picks by feel, with three hundred prior uploads sitting unused.
**Tags:** #gradient-boosting #cnns #word-embeddings #evaluation-metrics #confidence-intervals #transfer-learning #feature-engineering #contrastive-learning
**Contested on:** Every serious competitor in this niche is fighting to rank a creator's candidate titles, thumbnails, topics and formats before anything is published — and whoever predicts best against that creator's own audience changes what gets made.

## The Problem
The decision is made at the end of production, under time pressure, from a handful of options the creator generated themselves. It determines a large share of the outcome. There is no comparison against what has worked before on this channel, no model of this audience's preferences, and no way to know whether the preferred thumbnail resembles the ones that historically did well or the ones that did badly. The choice is made on taste, by someone whose taste was formed by an ambiguous feedback loop.

## Why Nobody Has Built This
Prediction requires representing the creative choices numerically, and nobody built the representation — a catalogue of videos is not a dataset until someone makes it one, and that step was never taken. Platform testing tools cover thumbnails narrowly and arrived late. A single channel's data is thin for anything subtle, which makes the pooled version necessary and harder to assemble. And the market has been served by advice rather than by tools.

## What to Build
Predict against the creator's own audience. Represent titles, thumbnails and topics numerically — text embeddings, image features, topic classification — which is the core and is the step that makes everything else a standard modelling problem. Rank candidate options by predicted performance for this specific channel, since generic best practice is what creators already have and it is not working. Use transfer from similar channels to handle thin own-data, because a creator with eighty uploads cannot model alone and channels in the same category behave similarly. Predict topic performance, as topic selection matters more than title and thumbnail combined and is completely unsupported. Give an interval rather than a point, since the confound and the sample size both make precision dishonest. Flag the option that resembles past failures, which is often more useful than identifying the winner. Explain the ranking in terms the creator can use, because an unexplained ranking will be overridden by intuition and should be. Support genuine testing where the platform allows it, and use those results to calibrate the model. Predict at the ideation stage as well as at publication, since the highest-value decision is what to make rather than how to package it. And measure prediction accuracy openly, as the category is full of confident claims and the differentiator is being checkable.

## Target Customer
Creators and channel managers, production teams choosing packaging, management companies, and creator tooling vendors selling templates and advice.

## Impact If Built
A catalogue of videos is not a dataset until someone makes it one, and that step was never taken. Representing titles, thumbnails and topics numerically turns the final decision of every production into a ranked choice against the creator's own history.
