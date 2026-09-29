# Psychometric Instrument Validation

**Niche:** [[niches/robo-advisors/risk-tolerance-measurement/profile|Risk Tolerance Measurement]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Psychometrics has a century of method for validating an instrument against an outcome, and risk tolerance questionnaires are largely exempt from it in practice.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #cross-validation #logistic-regression #compliance #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to predict how a client will actually behave in the next drawdown from the behaviour the platform already observes — and whoever predicts it best replaces the questionnaire as the input that sets the allocation.

## The Problem
Psychometrics developed rigorous practice for instrument design: construct validity, predictive validity against a criterion, reliability and test-retest stability, item analysis, differential item functioning across populations, and adaptive testing that asks fewer questions for more information. Risk tolerance instruments exist in this literature and the ones deployed in production are typically six items chosen for brevity, never validated against any criterion, and never revised.

## What Already Exists
Instrument validation methodology; item response theory and adaptive testing; reliability and stability measurement; differential item functioning analysis; and criterion validity study design.

## The Customization Gap
The adaptation is to an instrument whose criterion finally exists. It requires: (1) a behavioural criterion measured at scale, which is exactly what psychometrics usually lacks and what the platform supplies — this inverts the usual constraint and is the substantive opportunity; (2) a criterion that only materialises in a market event, so validation is episodic and regime-dependent in a way standard practice does not handle; (3) adaptive testing under an extreme brevity constraint, since onboarding will not tolerate thirty items; (4) an instrument that is also a regulatory record, which limits how freely it can be revised; and (5) a construct that may itself be unstable, since tolerance measured before and after a real loss may not be the same thing.

## Target Customer
Investment and product leadership, compliance functions relying on the instrument, academic researchers, and questionnaire vendors whose instruments have never met a criterion.

## Impact If Solved
Psychometrics usually cannot get a behavioural criterion at scale and this platform has one for millions of people. Validating and shortening the instrument against real drawdown behaviour is a textbook study nobody has run.
