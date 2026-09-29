# Priced on Volume, Measured on Agreement, Blind to Outcome

**Industry:** [[content-moderation-services|Content Moderation Services]]
**Type:** High Impact
**One-liner:** A vendor makes hundreds of millions of decisions a year and its only quality signal is whether a sampled few matched an auditor applying the policy literally.
**Tags:** #evaluation-metrics #confidence-intervals #bayesian-inference #gradient-boosting #hypothesis-testing #compliance #data-integration #worker-facing

## The Problem
Content moderation contracts are priced on volume — decisions per hour, cost per decision — with a quality threshold defined as agreement with an internal audit. An auditor reviews a small sample of a reviewer's decisions and marks each correct or incorrect against the policy document. Reviewer performance, team performance and frequently contract renewal depend on that number.

The metric has a specific and well-understood failure. An auditor working from a policy applies it as written; a reviewer facing a genuinely ambiguous case — satire, journalism about violence, reclaimed speech, medical content, a cultural reference the policy did not anticipate — must interpret. When the interpretation is correct and the literal reading is not, the reviewer is marked wrong. The rational response is to stop interpreting, and that is the response the industry gets.

The sample is also small. A reviewer making hundreds of decisions a day is audited on a handful, which means their quality score carries sampling error large enough that ordinary variation looks like performance difference — and people are managed on it.

The outcome never returns. Whether a decision was upheld on appeal, whether the removed content was actually harmful, whether the enforcement was proportionate, whether the platform got safer — the platform holds all of it and shares essentially none. So the vendor optimises the only signal it has, which is internal agreement, and the entire industry competes on price and throughput because quality cannot be demonstrated.

The consequence is visible downstream. The enforcement errors that creators and users experience as inexplicable — the wrongly removed journalism, the misread reclaimed speech — are produced in part by a measurement system that penalises the judgement that would have prevented them.

## Why It's Unsolved
The outcome data belongs to the platform and sharing it exposes the platform's own error rates, which is information no major platform publishes. A vendor asking for appeal outcomes is asking a client to hand over evidence about the quality of its own enforcement regime.

The audit-agreement metric is also genuinely convenient. It is cheap, it is auditable, it produces a number for a contract, and it can be computed without any information from outside the review operation. Replacing it requires agreeing a harder measure with a client who has no obligation to.

There is a real measurement difficulty underneath. Contextual correctness is not straightforwardly gradeable — two experienced reviewers will disagree on hard cases, which is the definition of a hard case — and any metric must handle that rather than pretending a single right answer exists. Inter-rater agreement among experts is the honest ceiling and it is well below one.

And the commercial structure rewards nobody for fixing it. The vendor is paid for volume, the platform gets a number it can report, and the cost of the resulting enforcement errors falls on users and creators who are not party to the contract.

## What a Solution Looks Like
Measure against a panel, not an auditor. Hard cases should be adjudicated by several experienced reviewers, with agreement among them establishing the ceiling and disagreement identifying genuine ambiguity rather than reviewer error. A reviewer whose decision falls within the range experts disagree over should not be marked wrong.

Separate the easy from the hard and score them differently. Most decisions are unambiguous and agreement is the right measure. A small share are genuinely difficult, carry most of the consequential errors, and need a different treatment — including permission to escalate rather than decide.

Negotiate the outcome return. Appeal outcomes at aggregate level, per policy category and per language, would let a vendor measure something real. The argument that works with a platform is that the vendor can then identify which policy areas produce systematic error, which is information the platform wants and currently generates only through public controversy.

Report uncertainty on reviewer scores. A quality score from a small sample has an interval, and managing people on a point estimate that ordinary variation could produce is both unfair and uninformative. Stating the interval changes how the number is used.

## Impact If Solved
This metric governs how hundreds of thousands of people do work that determines what billions of users see, and it currently trains them away from the judgement the hard cases require. Panel-based adjudication with honest agreement ceilings, separate treatment for ambiguous cases, and a negotiated outcome return would let a vendor compete on demonstrated decision quality rather than on price — and would remove one of the identifiable causes of the enforcement errors that the whole content ecosystem experiences as arbitrary.
