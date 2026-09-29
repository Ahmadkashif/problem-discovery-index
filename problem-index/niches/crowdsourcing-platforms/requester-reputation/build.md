# Build: Requester Statistics From the Platform's Own Record

**Niche:** [[niches/crowdsourcing-platforms/requester-reputation/profile|Requester Reputation & Trust]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Publish each requester's rejection rate, approval speed, responsiveness and realised pay rate on the task listing, computed from the platform's own data.
**Tags:** #descriptive-statistics #confidence-intervals #evaluation-metrics #hypothesis-testing #bayesian-inference #workflow-orchestration #worker-facing #revenue-impact
**Contested on:** Whether the platform will publish behavioural statistics about the party that pays it.

## The Problem

A worker decides whether to accept a task knowing the reward, the time limit and the requester's name. They do not know whether this requester approves within hours or within twenty-eight days, rejects one percent or forty percent, answers questions, or has a history of posting broken batches.

Every one of those is a completed measurement in the platform's database. Not an estimate, not a survey — a count.

The consequence of not publishing it is that workers use external, incomplete, unverified substitutes, and that requesters who behave well get no credit for it while requesters who reject indiscriminately face no consequence. A market where one side's conduct is entirely unobservable does not discipline that conduct.

## Why Nobody Has Built This

Requesters pay. Publishing statistics about their conduct is a service to the side that does not, and it exposes some paying customers unflatteringly.

There is a legitimate secondary concern: a requester with a legitimately high rejection rate — because their task genuinely attracts automated junk — would be penalised by a raw number, and workers might avoid them. That argues for normalisation by task type, not for publishing nothing.

And there is a self-reinforcing element: because nothing is published, workers use forums, and because workers use forums, the platform can point at the forums as evidence the need is met.

## What to Build

A requester statistics panel on every listing, computed and normalised.

**Publish the counts.** Rejection rate, median time to approval, payment reliability, question response rate, batch completion rate, and total volume — per requester, over a recent window, with the sample size shown.

**Normalise by task type.** A transcription task and an open-ended writing task have different natural rejection rates. Percentile against comparable tasks is far more informative than a raw rate and removes most of the legitimate objection.

**Report with uncertainty.** A requester with two batches has a noisy rate. Bayesian shrinkage toward the task-type mean, with the interval shown, is both fairer and more useful than a bare percentage.

**Include the realised hourly rate.** From the duration measurement: what this requester's previous batches actually paid per hour. This is the single most decision-relevant number for a worker and the one most likely to change requester behaviour, because a requester whose realised rate is published will raise it.

**Make it prominent on the listing**, not buried in a profile. The decision is made at the listing, in seconds.

**Give requesters the same view of themselves first.** A requester who sees their own percentiles before anyone else does will frequently correct, and launching with a private period is both fairer and a better way to get adoption than publishing cold.

**Act on the outliers.** A requester whose rejection rate is many times the task-type median should be reviewed, and their rejections should not count against approval rates while under review. Publishing without any consequence is half a fix.

## Target Customer

Platforms wanting to differentiate on worker treatment, particularly in the academic and enterprise segments where requesters are institutions with reputations of their own and where behaving well is already the norm. Also worker organisations, and the requesters who pay properly and currently get no benefit from it.

## Impact If Built

The asymmetry at the centre of this market closes: both sides become observable. Workers can avoid requesters who reject indiscriminately or pay in four weeks. Requesters who behave well get credit and fill their batches faster. And the conduct that is currently invisible acquires a consequence.
