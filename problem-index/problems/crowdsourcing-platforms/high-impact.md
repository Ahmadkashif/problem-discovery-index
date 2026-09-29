# Pay Is Set Per Task by Someone Who Does Not Know How Long It Takes

**Industry:** [[crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** High Impact
**One-liner:** The requester estimates five minutes, the task takes fifteen, the platform knows this exactly, and neither party is told.
**Tags:** #gradient-boosting #confidence-intervals #probability-distributions #time-series-forecasting #evaluation-metrics #hypothesis-testing #worker-facing #compliance

## The Problem
A requester posts a batch of tasks with a per-task payment. They set the amount from an estimate of how long the task will take, usually made by doing one themselves or by guessing. The estimate is systematically low: the requester knows the task's purpose, wrote the instructions, and does not experience the cost of parsing an unfamiliar interface, reading ambiguous guidance, or handling the edge cases that make up a substantial share of real submissions.

The platform records exactly how long every submission actually takes. That number, divided into the payment, is the realised hourly rate, and it is computed by nobody and shown to neither party. Academic studies of these platforms have repeatedly found median effective hourly earnings well below relevant minimum wages, and the estimation gap is a large part of the mechanism — most requesters are not trying to underpay and have no feedback telling them they are.

The worker discovers the real rate by doing the work. Having discovered it, they can abandon the task — forfeiting the time already spent — or complete it at a rate they would not have accepted. Neither is a good option and both happen constantly.

Task discovery compounds it. On platforms with large open task pools, finding work that pays acceptably is itself unpaid labour, and workers have built extensions and forums specifically to solve a search problem the platform could solve trivially. That informal infrastructure is a direct measure of the gap between what the platform provides and what the work requires.

And the qualification tests, instruction reading and broken tasks that produce nothing are all unpaid, so time spent and time paid diverge before any task is even submitted.

## Why It's Unsolved
The platform's customer is the requester. Showing a requester that their pay implies a low hourly rate invites them to pay more, which raises their cost and — in a market where platforms compete for requester volume — is competitively unattractive for whoever does it first.

Contractor classification removes the legal floor. With workers classified as independent contractors across jurisdictions and platforms positioned as intermediaries rather than employers, minimum wage obligations do not attach, and the platforms' terms are written to maintain that position.

Time measurement has genuine complications. A worker may be multitasking, may have a task open while doing something else, and self-reported duration is unreliable — so a naive time measure overstates. But the distribution of completion times across many workers on the same task is highly informative regardless, and the platforms have it.

And the market is international and fragmented, with workers who have limited collective capacity and no representation, which means there has been little external pressure — except in the academic segment, where ethics review boards and journal expectations have pushed toward pay floors, and where the norms have visibly shifted as a result.

## What a Solution Looks Like
Show the requester the realised rate before they post. Estimating completion time from comparable historical tasks and displaying the implied hourly rate at the moment of setting payment is a straightforward computation, and the evidence from platforms that have adopted pay guidance suggests most requesters adjust upward when told. The estimation gap is mostly ignorance rather than intent.

Show the worker the same number before they accept. Median and interquartile completion time for this task, and the implied rate, turns an accept decision made blind into an informed one — and it is the single change workers themselves have built tooling to approximate.

Compensate the unpaid categories. Qualification tests, instruction reading for long tasks, and tasks that turn out to be broken are all identifiable, and paying for them — even at a low rate — removes the largest source of the divergence between time worked and time paid.

Publish platform-level earnings distributions. Effective hourly earnings by task category, honestly computed, is the accountability mechanism that does not currently exist, and it would let requesters and research ethics reviewers make informed choices about where to place work.

And solve task discovery, which the platform is uniquely placed to do and workers currently do with extensions. Ranking available tasks by the worker's expected rate given their own speed is an ordinary recommendation problem.

## Impact If Solved
This market allocates work at rates neither party intended, through an estimation gap the platform measures precisely and reports to nobody. Showing the implied rate at posting time is a small feature with a large effect, compensating the unpaid categories closes the gap between hours worked and hours paid, and published earnings distributions create the external accountability that has already shifted norms in the academic segment of this same market.
