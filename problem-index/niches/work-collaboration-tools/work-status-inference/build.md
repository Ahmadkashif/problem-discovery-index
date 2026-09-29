# Status Estimated From What Actually Happened

**Niche:** [[niches/work-collaboration-tools/work-status-inference/profile|Work Status Inference]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A task's status is whatever somebody last typed, and the commits, edits, threads and reviews that show what is genuinely happening are captured by the same tools and used for an activity feed.
**Tags:** #hidden-markov-models #gradient-boosting #survival-analysis #change-point-detection #confidence-intervals #evaluation-metrics #causal-inference #automation
**Contested on:** Every serious competitor in work management is fighting to say what is actually happening from the activity the tools already captured rather than from what somebody typed — and whoever makes status observed rather than reported takes the category's founding promise.

## The Problem
A task is marked In Progress with a due date on Friday. In reality it has had no activity for nine days, the person assigned has been working on something else entirely, the document it depends on was last edited by someone who has since left, and a thread about it ended in an unanswered question three weeks ago. The status field says In Progress because that is what was set when it started. A project manager will discover the truth on Thursday by asking. Every signal that would have revealed it is in the same platform and is rendered as a list of recent activity nobody reads.

## Why Nobody Has Built This
The self-reported field is the product's own data model, and replacing it requires the vendor to assert that the customer's data is unreliable — which is commercially awkward for a company whose product is that data collection. Inference is also genuinely non-trivial: activity is a noisy proxy, work happens in tools the platform cannot see, and a task with no activity may be legitimately waiting. And the category's business model rewards engagement, so a feature that reduces the number of times people open the tool to update things is measured as a loss by the metrics the vendor runs on — which is the clearest case in this vault of a business model pointed against the product.

## What to Build
A state estimate per task with a confidence, from observed activity. The latent state — genuinely progressing, stalled, blocked on somebody, waiting on an external dependency, effectively abandoned — is inferred from the sequence of activity across the tools that can be observed: edits, commits, comments, review requests, message threads mentioning the work, and the activity of the people assigned. Slippage is predicted from the pattern rather than reported when a date passes, which is the difference between a warning and a record. Blocked work is detected by its signature — an unanswered request, a dependency with no activity, a person waiting on someone who has not responded — rather than by somebody marking it, since the people most blocked are the least likely to update a field. The estimate is presented alongside the reported status rather than replacing it, with the divergence visible, because the divergence is itself the most useful output: a task where the report and the evidence disagree is exactly what a programme review should discuss.

## Target Customer
Work management platform vendors, programme and portfolio functions in large organisations, and the project managers whose week is spent collecting what the system already knows.

## Impact If Built
The weekly status-gathering ritual is a large and universal cost in knowledge organisations and exists only because the reported field is untrustworthy. Inferred status with a visible divergence removes most of the collection while giving leadership something better than they had — and predicted slippage arrives while there is still time to act, which is the difference between programme management and programme reporting.
