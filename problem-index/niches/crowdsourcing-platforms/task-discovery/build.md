# Build: Matching, Alerting and Honest Previews

**Niche:** [[niches/crowdsourcing-platforms/task-discovery/profile|Task Discovery & Unpaid Search Time]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Learn which tasks a worker does well and quickly, alert them when matching batches appear, and show what a task involves before they open it.
**Tags:** #matrix-decompositions #gradient-boosting #word-embeddings #evaluation-metrics #confidence-intervals #k-nearest-neighbors #worker-facing #automation
**Contested on:** Whether task-worker fit can be learned from completion history in a market where workers do many task types.

## The Problem

A worker logs on to earn. Before any paid work happens they scan hundreds of listings, most of which they cannot do, do not qualify for, pay too little, or are from requesters they have learned to avoid. They open several to see what the task actually is, because the listing does not say. Good batches are gone within minutes, so the search is also a race.

On the larger platforms this unpaid search can be a substantial share of the session. It falls hardest on newer workers, who have not built the extensions, joined the forums or learned which requesters to watch, and who are therefore the least efficient at the one part of the job that pays nothing.

The platform holds every completion, every time, every rejection and every abandonment, by worker and by task type. It is a well-shaped matching dataset and it is used for filtering by keyword.

## Why Nobody Has Built This

Discovery serves the worker, and platform product investment has followed the requester, who pays. A better queue does not increase requester spend directly.

There is also a perverse interest: on platforms where the supply of workers scanning listings is what makes a batch fill quickly, a friction-laden queue produces an eager, attentive supply side. Nobody has said this out loud and the effect is real.

And workers built the tooling themselves, which reduced the pressure. The extensions and alert threads work well enough that the platform's gap is survivable, which is exactly why it persists.

## What to Build

A matching and alerting layer over the completion history.

**Learn worker-task fit from outcomes.** A latent-factor model over worker-task-type completions with outcome signals — completed, approved, abandoned, time taken relative to the median. The useful prediction is not what a worker will click but what they will complete successfully at a good effective rate. Task-type features and requester features handle the cold start.

**Rank by expected effective rate, not by reward.** A $2.00 task taking forty minutes is worse than a $0.40 task taking four. Ranking by predicted hourly rate for this worker, using the duration model, is the single most valuable change and is the number the worker is actually deciding on.

**Alert in real time.** Good batches are exhausted in minutes. A push notification when a batch matching a worker's profile and rate threshold appears is what workers built extensions to achieve, and it is trivial for the platform to provide properly.

**Show what the task actually is.** A preview — the interface, two sample items, the real instruction length, the qualification requirement, the predicted time — before the worker opens it. Opening tasks to find out what they are is a large share of the unpaid time and a preview removes nearly all of it.

**Surface requester history on the listing.** Rejection rate, payment speed and realised rate from previous batches. This is what workers currently look up on external sites, and putting it on the listing is both a discovery feature and a market-discipline mechanism.

**Measure the unpaid time.** Session time before first paid task, tasks opened and abandoned, search-to-accept ratio. Nobody reports this and it is the metric the whole niche is about.

## Target Customer

Platforms competing for worker supply, particularly those whose fill rates suffer because good workers cannot find their batches. The academic-focused platforms, which compete on participant quality and have the most to gain from workers who find suitable studies quickly. And worker-tooling builders, who have already demonstrated the demand.

## Impact If Built

The unpaid search that precedes every earning session shrinks substantially. Workers see the number they are actually deciding on — expected rate for them — instead of a reward figure. New workers stop being disadvantaged by not knowing which forum to read. And requesters' batches fill faster because the right workers are told about them.
