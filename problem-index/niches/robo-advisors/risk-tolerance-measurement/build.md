# Tolerance Inferred From Behaviour

**Niche:** [[niches/robo-advisors/risk-tolerance-measurement/profile|Risk Tolerance Measurement]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every past drawdown labelled every client, and the platform still asks them how they think they would feel.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #confidence-intervals #evaluation-metrics #hypothesis-testing #cross-validation #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to predict how a client will actually behave in the next drawdown from the behaviour the platform already observes — and whoever predicts it best replaces the questionnaire as the input that sets the allocation.

## The Problem
Risk tolerance is treated as a trait the client can report. What actually matters is a prediction: will this person sell when their portfolio is down thirty percent? That is a question with observed answers — every client who has been through a drawdown has one — and with abundant predictive features in login behaviour, allocation fiddling, funding continuity, prior reactions and portfolio composition. The platform has the labels, has the features, and asks the question instead.

## Why Nobody Has Built This
The self-report satisfied the suitability requirement, so it was never treated as a measurement to be validated — a compliant instrument is not obliged to be an accurate one. Behaviour as a signal requires modelling that the investment team is not staffed for and the data team is not pointed at. New clients have no drawdown history, which makes the cold-start case look like a blocker for the whole idea. And nobody measured the questionnaire's predictive power, so its weakness is undocumented.

## What to Build
Predict the behaviour rather than asking about the feeling. Label every client with their observed drawdown behaviour, which is the core and exists for every client who has been through one. Build features from what the platform already logs — login frequency and timing in falling markets, allocation changes, funding pauses, goal edits, balance checks — since these are the behavioural traces that precede a sale. Predict the probability of a panic sale at a given drawdown depth, because that is the operationally useful form and can be acted on before the event. Attach a confidence to every estimate, as a prediction for a two-year client and a two-month client are not comparable. Handle the cold start explicitly with a prior from similar clients, which turns the new-client case from a blocker into a straightforward hierarchical problem. Measure the questionnaire's incremental predictive power, since it may add real information or almost none and nobody knows which. Validate out of sample across different market regimes, because a model fitted to one drawdown may not transfer to a differently shaped one. Segment by predicted behaviour rather than by stated tolerance, which is what changes the product. Keep the inferred estimate separate from the suitability record, so the supervision question does not block the modelling. And recalibrate after every market event, since each one supplies a fresh set of labels.

## Target Customer
Investment and product leadership, chief investment officers setting allocation policy, supervision functions assessing suitability evidence, and advice platform vendors whose risk models are a lookup table.

## Impact If Built
A compliant instrument was never obliged to be an accurate one, so nobody validated it. Every past drawdown labelled every client, which makes this a conventional supervised problem the category has simply never framed.
