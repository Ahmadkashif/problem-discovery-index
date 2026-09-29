# Every Case Is Ambiguous and the Metric Is Throughput

**Niche:** [[niches/online-marketplaces/the-trust-and-safety-reviewer/profile|The Trust & Safety Reviewer]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Trust and safety reviewers make consequential judgement calls at high volume on the cases automation could not decide, which means every case they see is genuinely ambiguous and the metrics treat them as interchangeable units of throughput.
**Tags:** #worker-facing #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #compliance #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to support a reviewer whose every case is genuinely ambiguous — and whoever does that takes the quality, because these are the decisions automation could not make and they are being timed like data entry.

## The Problem
A reviewer's queue holds a listing that might be a counterfeit or might be an authentic item photographed badly, a message that might be an attempt to move the transaction off-platform or might be a legitimate question, and an account that shows three of the seven patterns associated with fraud. Each requires reading, context-gathering and a decision that will materially affect somebody's income. Their target is a number of cases per hour, set by dividing the queue by the headcount. The measurement system assumes the cases are comparable and none of them are, and the reviewer's only lever for hitting the target is to think less.

## Why Nobody Has Built This
Throughput metrics came with the outsourced review model and were designed for a queue that included easy cases. As automation improved and took the easy cases, the metric stayed and the queue got harder — a change nobody adjusted for because nobody was measuring case difficulty. Weighting cases requires a complexity measure that does not exist. And the reviewers are frequently contracted staff with no channel to raise it.

## What to Build
Measure the work rather than the volume. Score case complexity from the signals that reached review — how close the automated score was to the threshold, how many policy areas are implicated, how much context is required — and weight targets by it, which is computable from data the queue already carries and is the change that makes the metric honest. Give reviewers the context automatically: the account history, the related cases, the seller's prior decisions, the similar cases and how they were decided, which is most of what a careful reviewer gathers by hand. Surface precedent, since consistency is the quality that matters most in this work and a reviewer currently has no way to see how the same situation was decided last month. Report agreement between reviewers on the same case rather than against a single reviewer's answer, since disagreement on a genuinely ambiguous case is information about the policy and not error by the reviewer. Separate quality measurement from throughput so they are not traded against each other implicitly. Let a reviewer mark a case as genuinely undecidable and route it to a policy owner, which the fix note develops. Report the decision's downstream outcome — appealed, overturned, upheld — back to the reviewer, since they currently decide into silence. And staff to the difficulty of the queue rather than to its length, because the queue's composition has changed and the staffing model has not.

## Target Customer
Trust and safety organisations and their leadership, the reviewers, and the sellers and buyers on the wrong end of a rushed decision.

## Impact If Built
Automation took the easy cases and the throughput metric stayed, leaving a queue of only hard cases measured as though it were data entry. Complexity weighting is computable from signals the queue already carries, and precedent access is what makes consistency possible at all.
