# Calibration Borrowed From Alerting

**Niche:** [[niches/qa-test-automation-vendors/the-waiting-developer/profile|The Waiting Developer]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Operational alerting learned decades ago that an alert people ignore is worse than no alert, and developed the practice to fix it, and test results are still a binary nobody calibrates.
**Tags:** #logistic-regression #bayesian-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #cross-validation #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor that takes this seriously is fighting to make a test result mean something to the developer receiving it — and whoever does that takes the engineering organisation, because a suite that is disbelieved provides no value regardless of what it costs.

## The Problem
Operational alerting went through exactly this: alerts that fired constantly were muted, the muting spread to alerts that mattered, and the practice responded with alert quality measurement, precision as a first-class concern, and the four-class inventory of whether an alert ever led to action. The testing category is at the stage alerting was at before that, presenting a binary with no credibility attached and no measurement of whether anybody acts on it.

## What Already Exists
The alert quality practice with its precision-recall framing and outcome inventory; calibration methods for probabilistic outputs; flaky test detection research, which supplies the per-test reliability estimate; and the whole signal-detection framework for reasoning about a decision-maker facing a noisy indicator.

## The Customization Gap
The adaptation is to a per-test rather than per-alert reliability estimate. It requires: (1) reliability estimated per test rather than globally, since a suite contains both extremely reliable tests and known flaky ones and a single credibility number is useless — the per-test history is available and is the basis; (2) conditioning on the change, because a failure in a test unrelated to what was modified is more likely to be noise and one in a test directly exercising the change is more likely to be real, which is a strong signal and requires the change-to-test relationship; (3) calibration rather than ranking, since the developer's decision is whether to investigate and a calibrated probability supports that where a relative ranking does not; (4) the outcome inventory applied to tests — which tests have ever failed for a real reason, which fail constantly and are ignored, which have never failed, and which defects escaped a passing suite — which is the alerting practice's most useful artefact and translates directly; and (5) measuring the behavioural response, since the point is whether developers investigate rather than whether the model is accurate.

## Target Customer
Test tooling vendors, platform engineering teams, and the quality functions whose suites have lost credibility.

## Impact If Solved
Alerting learned this lesson decades ago and the testing category has not, despite an identical failure mode. Per-test reliability conditioned on the change is the adaptation, and the four-class outcome inventory translates directly and would let most teams prune in an afternoon.
