# The Back Catalogue as an Experiment

**Niche:** [[niches/creator-businesses/content-performance/profile|Content Performance]]
**Industry:** [[industries/creator-businesses|Creator Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of deliberate creative decisions with measured outcomes is an experimental record, and every creator has one and nobody reads it.
**Tags:** #causal-inference #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #time-series-forecasting #feature-engineering #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to tell a creator which choices will work and which choices caused what happened — and the contest splits cleanly enough that it is not terminal.

## The Problem
A creator with three hundred uploads has made thousands of deliberate choices — topic, framing, title structure, thumbnail composition, video length, opening seconds, posting day — each followed by a measured result. That is an experimental record, and it is sitting in a platform's analytics export. The treatment effect is entangled with a distribution decision, which makes the analysis harder, not impossible. What creators have instead is a dashboard, a set of heuristics from other people's channels, and a strong intuition they cannot check.

## Why Nobody Has Built This
The analytics were built to report, so the product's job ended at describing what happened — a reporting surface has no reason to develop a theory of why. The confound is real and discouraged serious attempts. The advice industry sells anecdote because anecdote is cheaper to produce. And no creator has the volume alone to resolve small effects, which is why the cross-creator version matters.

## What to Build
Treat the catalogue as the experiment it is. Extract structured features from every upload — topic, title structure, thumbnail composition, length, pacing, opening, format — which is the core and is the step that turns a video library into a dataset. Model performance against those features while controlling for what can be controlled: channel trajectory, subscriber base at publication, seasonality, and the platform's own early impression allocation. Separate prediction from attribution, since a creator needs one before publishing and the other after, and they are the decomposition below. Pool across creators in similar categories to resolve effects no single channel has the volume for, because that is the only way to get past the small-sample problem. Run genuine tests where the platform allows them, as thumbnail and title testing is real experimentation and is underused. Express every finding with uncertainty, since the confound means confident claims are usually wrong and creators have been burned by confident advice. Distinguish what the creator controls from what they do not, because effort spent on the latter is wasted. Detect the channel's own patterns rather than applying general rules, as every audience differs and generic advice is the current product. Validate findings prospectively on the next uploads, which is what separates this from the existing advice industry. And make the output a decision rather than a chart, because creators need to choose and dashboards do not choose.

## Target Customer
Creators and channel managers, creator agencies and management, analytics and education vendors selling anecdote, and platforms whose analytics report without explaining.

## Impact If Built
A reporting surface has no reason to develop a theory of why, so the analytics describe and stop. Every creator with a few hundred uploads holds an experimental record, and nobody has read one as the dataset it is.
