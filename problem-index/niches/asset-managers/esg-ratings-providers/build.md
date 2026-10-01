# Ratings That Disagree and Are Never Tested

**Niche:** [[niches/asset-managers/esg-ratings-providers/profile|ESG Ratings & Sustainability Research Providers]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** ESG ratings of the same company from different providers correlate weakly, and no provider maintains a standing record of what its own ratings predict.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance
**Contested on:** Every serious competitor in this pocket is fighting to show that its ratings measure something real and are produced by a documented, consistently applied method — and whoever can evidence that, issuer by issuer, keeps its asset-manager clients through the EU authorisation regime and the political backlash against ESG labels.

## The Problem
Academic work — most prominently the "Aggregate Confusion" study by Berg, Kölbel and Rigobon — has documented that ESG ratings from major providers diverge substantially for the same company, driven by differences in scope, measurement and weighting. Asset managers building funds on one provider's ratings are therefore building on one provider's methodology choices. The provider holds years of its own ratings and can observe what happened afterwards to every rated company — controversies, regulatory penalties, downgrades, drawdowns, emissions trajectories — but rarely reports systematically whether its ratings anticipated any of it.

## Why Nobody Has Built This
Ratings are positioned as risk assessments rather than forecasts, which is a fair methodological point that has been allowed to block testing in the form users actually rely on. A published validation record that shows weak predictive power is commercially uncomfortable. And outcomes are heterogeneous — financial, operational, reputational — which makes a single scorecard hard to define.

## What to Build
A validation system built from the provider's own archive: every rating and component score as issued, joined to subsequent controversies, enforcement, credit events and returns. Survival models for time-to-controversy by rating band; event studies around rating changes; decomposition of which pillar and which indicators carry information; and a divergence map against other public ratings that explains disagreements by methodology choice. The EU regime's methodology-transparency requirements make the documented version of this an asset at authorisation, not only a research project.

## Target Customer
Chief methodology officers and heads of ESG research at ratings providers seeking EU authorisation and defending their product to sceptical asset-manager clients.

## Impact If Built
The provider can state, with evidence, what its ratings measure and how well — the strongest available answer to both the regulator and the backlash.
