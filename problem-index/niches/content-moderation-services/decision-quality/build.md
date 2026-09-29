# Build: Quality Measured Against Outcomes

**Niche:** Decision Quality Measurement
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A quality system that grades moderation decisions against appeal outcomes, reversal rates and downstream harm rather than against whether a sampled few matched an auditor.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #causal-inference #logistic-regression #bayesian-inference #data-integration #compliance
**Contested on:** Whether decision quality means agreement with an auditor applying the policy literally, or linkage to what actually happened after the decision.

## The Problem

The industry's quality metric measures the wrong thing, and everyone in it knows.

Agreement with an auditor tells you whether two people reading the same policy reached the same conclusion. It does not tell you whether the conclusion was right. On the easy cases — the vast majority — agreement is high and the metric is uninformative. On the hard cases, where the policy language does not cleanly cover the situation, the auditor applies the literal reading because that is the defensible position for an auditor, and the reviewer who applied contextual judgement is marked wrong.

That is not a measurement failure at the margin; it is a training signal pointed in the wrong direction, delivered hundreds of times a day to tens of thousands of people. Reviewers optimise for it because their standing depends on it. The result is an operation that gets progressively better at literal policy application and progressively worse at the judgement calls that are the entire justification for using humans instead of classifiers.

Meanwhile the data that would actually grade a decision exists. Appeals are adjudicated and the outcome is recorded. Enforcements are reversed. Accounts go on to violate or do not. Content left up generates reports or does not. Every one of those is an external check on the original decision, and none of them come back to the vendor.

## Why Nobody Has Built This

**The outcome data is on the other side of the contract.** Appeals are handled by the platform, sometimes by a different vendor entirely. Reversal records, downstream account behaviour and harm reports all sit in platform systems. The vendor is not given them, and in most agreements has no right to ask.

**The contract specifies the metric.** Accuracy against a sampled audit is a written term with a service level and a penalty attached. A vendor cannot unilaterally substitute a different measure for the one it is paid against, and proposing a new one means reopening a commercial negotiation from a weak position.

**Outcome measurement would expose the policy.** A system that separates "the reviewer misapplied the policy" from "the policy gave the wrong answer" produces a running count of the second category. That is a finding about the client's policy team, delivered by a supplier, which is not a comfortable artefact to generate.

**Appeal outcomes are a biased signal and require care.** Only a small, self-selected fraction of decisions are appealed, skewed toward removals of content by people motivated to contest them, and appeal adjudication has its own error. Treating appeal reversal as ground truth naively would produce a metric as misleading as the one it replaces — correcting for the selection is real statistical work.

**Nobody is rewarded for it.** The vendor is paid on the existing metric, the platform is not asking for a better one, and the people harmed by the current metric are reviewers with no contractual voice.

## What to Build

**Start with what the vendor already holds.** Before any platform cooperation: proper inter-rater reliability on the existing audit programme. Multiple auditors on the same items, variance decomposed into reviewer effect, auditor effect and item difficulty. This alone reveals how much of each reviewer's reported accuracy is signal and how much is which auditor drew their sample — and in most operations the answer is shocking enough to force change on its own.

**Item difficulty as a first-class quantity.** Model each item's difficulty from disagreement patterns across reviewers and auditors. A reviewer graded on a hard sample and one graded on an easy sample are currently compared directly. Difficulty-adjusted accuracy is a fairer measure, computable entirely in-house, and immediately more useful to everyone.

**Separate policy failure from application failure.** When auditors disagree with each other on an item, or when a reviewer's contextual call is overturned and then reinstated on appeal, that is evidence the policy is inadequate rather than that the reviewer erred. Route those cases to a policy-feedback queue and count them separately. This converts the quality system into something that improves the policy instead of only grading people.

**Negotiate for appeal outcomes as the first external signal.** It is the most available, most interpretable and least sensitive of the outcome data, and platforms have a genuine interest in it because appeal volume is a cost to them. Correct for selection explicitly — model which decisions get appealed, and report reversal rates with that correction and with honest uncertainty.

**Then the harder signals.** Downstream account behaviour and subsequent harm reports, where they can be obtained, joined at the decision level. These are the signals that say whether the operation made the platform safer, which is the claim the industry sells and has never evidenced.

**Report quality as a distribution, not a number.** Accuracy by difficulty band, with confidence intervals, and the sample size actually needed to distinguish reviewers — which is usually far larger than what contracts specify. A great deal of current individual performance management is acting on noise.

## Target Customer

Vendor quality leadership, where the in-house components can be built without asking anyone's permission and produce immediate internal value.

Platforms are the buyer for the outcome-linked half, and the argument is direct: the current metric is degrading the judgement quality on the hard cases that constitute the platform's actual risk, and the data to fix it is sitting in their appeals system.

## Impact If Built

The training signal inverts. Reviewers currently learn that contextual judgement is punished; an outcome-linked measure would reward it, on exactly the cases where humans are the only reason the operation exists.

The policy starts learning. Separating policy failure from application failure produces a steady, evidenced stream of the places the document is inadequate — which is information the policy team currently receives only through escalation and anecdote.

And the vendor gets something to sell. A firm that can demonstrate better outcomes, rather than better agreement with its own auditors, has the first real quality differentiator in a market that competes on price.
