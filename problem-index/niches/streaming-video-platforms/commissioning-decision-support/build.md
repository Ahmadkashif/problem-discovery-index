# Forecasting Something That Does Not Exist

**Niche:** [[niches/streaming-video-platforms/commissioning-decision-support/profile|Commissioning Decision Support]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The decision commits nine figures on the basis of a script, a cast list and a set of comparables somebody chose.
**Tags:** #gradient-boosting #large-language-models #k-nearest-neighbors #evaluation-metrics #confidence-intervals #transfer-learning #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to predict what an unmade title will be worth from a script, a cast, a comparable set and a gap in the catalogue — and whoever forecasts better than instinct changes which nine-figure commitments get made.

## The Problem
Commissioning happens before any of the data that makes streaming platforms sophisticated exists. What is available is a script or treatment, attached talent with their own track records, a genre and format, a budget, a production territory, and the platform's own knowledge of which segments it underserves. That is a real feature set with a real outcome variable — the platform has commissioned hundreds of titles and knows how each performed — and no platform has built a model on it.

## Why Nobody Has Built This
Commissioning is understood as a creative judgement, so a forecast reads as an attempt to replace taste — an activity defined by its practitioners as an art resists being modelled even where the inputs are structured. The outcome variable depends on the causal valuation work that does not exist either. Sample sizes are hundreds rather than millions. And a model that contradicts an executive is a political problem before it is a technical one.

## What to Build
Forecast from what exists before production, and be honest about the uncertainty. Structure the pre-production attributes — genre, format, talent history, budget, territory, source material, comparable set — which is the core and is the step that makes this a modelling problem at all. Model the outcome against the platform's own commissioning history, since hundreds of titles with known outcomes is a small but genuine dataset. Use talent track records properly, as they are the strongest available signal and are currently applied as reputation rather than as data. Model catalogue gaps and segment demand, because the platform knows which audiences it underserves and that is the most defensible argument for a narrow commission. Select comparables by measured similarity rather than by whoever is pitching, which removes a systematic bias in every greenlight meeting. Express the forecast as a wide interval, since the uncertainty is genuinely large and a false precision would be correctly rejected. Predict the range of outcomes rather than a point, as the portfolio question is about risk as much as expectation. Track every greenlight decision and its outcome, which is the dataset that makes the next model better and does not currently exist. Support the portfolio view — how much risk, how many narrow bets, how much breadth — because that is the decision above the individual title. And position it as evidence for the room rather than a verdict, since adoption depends entirely on that framing.

## Target Customer
Content leadership and commissioning executives, finance leadership approving slates, studios and producers pitching, and analytics vendors serving media.

## Impact If Built
An activity defined by its practitioners as an art resists being modelled even where the inputs are structured. Hundreds of commissioned titles with known outcomes and structured pre-production attributes is a small but real dataset nobody has assembled.
