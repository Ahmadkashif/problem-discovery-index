# Nine in Ten With No Idea Which Ten

**Niche:** [[niches/ai-agent-platforms/task-reliability-prediction/profile|Task Reliability Prediction]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Agents report a success rate and not a per-task confidence, so an agent that knows nothing about its own likely failures proceeds identically on the cases it will handle well and the ones it will get wrong.
**Tags:** #confidence-intervals #evaluation-metrics #hypothesis-testing #logistic-regression #gradient-boosting #descriptive-statistics #quick-win #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to tell a buyer, before deployment, what fraction of their tasks the agent will complete correctly and which ones it will fail — and whoever does that takes the account, because no other claim in this market is checkable.

## The Problem
An agent handles a straightforward refund and an unusual one with identical apparent assurance. It has no representation of how likely it is to be right on this particular task, so it cannot defer the hard one, cannot flag it for review, and cannot tell the customer it is unsure. The deployment is therefore configured as a single policy for all tasks: either the agent runs freely and occasionally does something expensive, or a human reviews everything and the deployment saves nothing. Per-task confidence is the missing input that would let the policy be conditional, and nothing produces it.

## Why It's Still Broken
Confidence estimation over a multi-step trajectory is harder than over a single output, and the obvious signals — the model's own stated confidence — are poorly calibrated and known to be. Producing a confidence means sometimes declining, which reads as the product not working. The category's measurement is aggregate, so there has been no pressure toward the per-task view. And the trajectory data that would support a learned estimator is used for debugging rather than training.

## What a Fix Looks Like
Predict per-task success and act on it. Learn a success predictor from the trajectory corpus using features available before and during execution — task type, input characteristics, tool responses, retries, state anomalies — which is a well-posed supervised problem with abundant labels and is the whole fix. Calibrate it properly and report calibration, since an uncalibrated confidence is worse than none and calibration is measurable against the same corpus. Use it to route: proceed autonomously above a threshold, seek approval in the middle, decline at the bottom — which converts the binary deployment policy into a graduated one and is where most of the unrealised value sits. Detect mid-trajectory that a task is going wrong, since many failures announce themselves several steps before the damage and an early abort is far cheaper than a completed error. Let the buyer set thresholds against their own cost of error, which differs enormously and is currently not an input to anything. Report the confidence to the human in the loop, so their attention goes where it is needed. Explain the low-confidence cases in terms the buyer can act on, since a named pattern can be fixed or routed away. And measure the predictor's own accuracy continuously, because a confidence signal that drifts is worse than one that never existed.

## Who Feels the Pain
Buyers forced to choose between an unsupervised agent and a reviewed one that saves nothing; customers on the wrong end of a confident mistake; and vendors whose agents are reliable on most tasks and cannot prove which.

## Impact If Fixed
Per-task confidence is the missing input that turns a single deployment policy into a graduated one. It is a well-posed supervised problem with abundant labels in a corpus currently used only for debugging.
