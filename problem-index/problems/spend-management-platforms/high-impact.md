# Policy That Never Learns From Its Own Exceptions

**Industry:** [[spend-management-platforms|Spend Management Platforms]]
**Type:** High Impact
**One-liner:** Every out-of-policy transaction is routed to a human who approves it, and thousands of those judgements a month are stored as audit trail and used to improve nothing.
**Tags:** #gradient-boosting #logistic-regression #bert #large-language-models #k-means-clustering #evaluation-metrics #feature-engineering #automation #revenue-impact

## The Problem
Spend policy is a rule set. Meals under a threshold, no alcohol, software purchases require approval above an amount, travel must be booked in the tool, certain merchant categories blocked outright, receipts required above twenty-five dollars.

Reality does not fit. A team dinner with a customer exceeds the per-head limit. An engineer buys a tool the policy has never heard of because it did not exist last quarter. A sales trip books outside the tool because the customer moved the meeting. A conference registration exceeds the software limit because it was categorised as software.

Each becomes an exception, routed to a manager or a controller. They look at it, understand the context in about four seconds, and approve. The approval rate on exceptions is very high across the category — the overwhelming majority of flagged spend is legitimate spend that a rule could not anticipate.

That approval is a judgement with the full context attached: who spent, at which merchant, for how much, in what business circumstance, and a human decided it was fine. It happens thousands of times a month in a mid-sized company and far more across a platform's customer base. It is recorded, timestamped and attributed, and it is used only as audit evidence.

Nothing flows back. The rule that produced the exception is unchanged next month and produces the same exception. The manager approves it again. Over time managers approve faster and less carefully, which is rational given the base rate and which erodes the control the whole system exists to provide. The exceptions that genuinely deserve attention arrive in the same queue at the same pace as the hundred that do not.

The rules themselves came from somewhere unexamined — a template the platform ships, a policy the CFO wrote at a prior company, a threshold set in a currency and an era that no longer apply. Nobody can say which rules earn their keep.

## Why It's Unsolved
Policy is a governance artefact and changing it feels like a governance act. Adjusting a threshold requires the CFO's agreement, sometimes the audit committee's, and the meeting to justify it is more expensive than living with the exceptions. So policy ossifies while the business changes around it.

The platforms sell control, and control is legible as rules. A product that said "we learned that your $75 meal limit generates four hundred exceptions a month and every one is approved, so it should be $110" is selling something harder to describe in a procurement document than a policy engine, even though it is obviously better.

Measurement is absent because nobody has defined the outcome. There is no agreed metric for whether a policy is good. Exception volume is measured, approval rate is measured, and neither says whether the policy prevented anything. The counterfactual — what would have been spent without the rule — is unobservable without deliberate variation that no finance team will run.

And the genuinely bad spend is rare, which makes the signal faint. Actual misuse is a small fraction of exceptions, so a classifier trained naively on approval outcomes learns to approve everything, which is what the humans already do.

## What a Solution Looks Like
Grade every rule against its own exception history. Volume generated, approval rate, and the manager-seconds consumed are all directly measurable. A rule with a ninety-nine percent approval rate and four hundred monthly exceptions is not a control; it is a tax, and identifying those is arithmetic rather than modelling.

Recommend thresholds from the observed distribution. Where a limit is approved through constantly, the empirical distribution of approved spend says what the limit should be. Presenting that as a recommendation with the evidence attached gives the CFO the justification that currently makes the change too expensive to bother with.

Route by novelty rather than by rule breach. The exception that deserves human attention is the one unlike previous approved exceptions — a new merchant, an unusual pattern, a combination not seen before. Everything resembling a thousand prior approvals can be auto-approved with post-hoc sampling, which is how every other mature control function works.

Detect genuine misuse as a rare-event problem in its own right, rather than expecting it to fall out of exception review. Duplicate submissions, personal spend patterns, vendor relationships that look unusual, splitting to stay under thresholds — these are specific, detectable patterns and none of them is what the current rule set is looking for.

Learn policy across customers. The platform sees thousands of companies' policies alongside their exception and approval behaviour. What a fifty-person software company's meal limit should be is an empirical question the platform can answer and each customer currently guesses at.

## Impact If Solved
The category sells control and delivers an exception queue that trains its reviewers to stop reading. Grading rules against their own outcomes, recommending thresholds from observed distributions and routing by novelty converts rubber-stamping into actual oversight, and it runs entirely on decisions the platform is already recording.
