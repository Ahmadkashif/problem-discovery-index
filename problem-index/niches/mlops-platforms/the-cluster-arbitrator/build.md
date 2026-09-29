# A Scheduler That Knows Nothing About the Work

**Niche:** [[niches/mlops-platforms/the-cluster-arbitrator/profile|The Cluster Arbitrator]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Platform engineers spend their days arbitrating between researchers who all need the cluster now, using a scheduler that knows nothing about how long anything will take or whether it will work.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #markov-decision-processes #confidence-intervals #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to schedule accelerators on what a job will actually need and be worth rather than on what its author requested — and whoever does that takes the account, because the cluster is the largest line in the budget and it is allocated by negotiation.

## The Problem
Eleven jobs are queued for sixteen free accelerators. The scheduler orders them by submission time and priority class, both of which are inputs the submitters control. Job three will run for six days and was submitted to hold capacity. Job seven will crash in four minutes on a configuration error its author has made twice this month. Job nine is a two-hour evaluation blocking a release. The platform engineer knows some of this and reorders the queue by hand, in a chat thread, several times a day. The history that would have predicted all three is in the tracking platform.

## Why Nobody Has Built This
Schedulers come from high performance computing, where a job's duration is declared by the submitter and enforced by a wall clock, and the ML world adopted the mechanism without the declaration culture. Duration prediction needs run history joined to scheduler state, and those are two different systems owned by two different teams. Killing a researcher's job on a prediction is politically fraught, which has prevented even the non-destructive uses from being built. And the scarcity is real, so every improvement is contested by someone who currently benefits from the arbitrary ordering.

## What to Build
Give the scheduler the information the organisation already has. Predict job duration from the run history — architecture, data volume, batch size, accelerator type, and the same author's previous jobs — which is a well-posed learning problem with abundant labels and immediately enables sensible queue ordering and honest start-time estimates. Predict failure-within-minutes, since a meaningful share of submissions die on configuration errors and catching them at submission rather than after a four-hour queue wait is pure gain with no political cost — which makes it the right thing to build first. Show every researcher a predicted start time, because most of the escalation is caused by not knowing, and visibility removes a large share of the arbitration without allocating anything differently. Detect over-reservation and report it, which the fix note develops. Support preemption with checkpoint awareness, so a long low-priority job can yield to a short urgent one and resume, which is where the real throughput gain is and which requires the checkpointing to be trustworthy. Offer value as an explicit input — a release blocker, an exploratory sweep, a scheduled retrain — so that priority is a stated policy rather than a negotiation. And report queue fairness and waiting time by team, since the current allocation's inequities are invisible and are the reason the arbitration is exhausting.

## Target Customer
Platform and ML infrastructure teams, the finance functions funding accelerator capacity, and the schedulers and cloud providers serving this workload.

## Impact If Built
The scheduler orders by inputs the submitter controls and ignores a history that predicts everything it needs. Failure-within-minutes prediction is the politically free place to start, and showing researchers a predicted start time removes most of the arbitration without changing a single allocation.
