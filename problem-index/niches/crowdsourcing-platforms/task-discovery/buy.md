# Buy: Job Matching Infrastructure Adapted to Minutes-Long Work

**Niche:** [[niches/crowdsourcing-platforms/task-discovery/profile|Task Discovery & Unpaid Search Time]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Job boards and gig marketplaces have good matching and alerting; they are built for opportunities that last weeks, not batches that are exhausted in four minutes.
**Tags:** #matrix-decompositions #word-embeddings #gradient-boosting #evaluation-metrics #confidence-intervals #k-nearest-neighbors #automation #worker-facing
**Contested on:** Whether job-matching infrastructure can operate at the timescale of a batch that disappears in minutes.

## The Problem

Matching and recommendation infrastructure is abundant. Job boards, gig marketplaces and shift-work platforms all run personalised matching, saved searches, alerts and recommendation feeds, and the underlying technology — embeddings, collaborative filtering, real-time serving — is commodity.

The timescale is wrong by two orders of magnitude. A job posting is available for weeks; a good crowdsourcing batch is exhausted in minutes. A daily digest email, which is the standard alerting product, is useless. And the matching signal differs: job matching predicts application and hire, while here the useful prediction is completion at a good effective rate, which is known within the hour.

## What Already Exists

Job board matching and alerting. Gig marketplace recommendation. Shift-work platforms with real-time shift offers, which are the closest analogue in cadence. Embedding retrieval and recommendation infrastructure. Push notification services. Saved search and alerting patterns.

## The Customization Gap

**Alerting must be seconds, not hours.** The event is a batch appearing and the window is minutes. Real-time push with tight latency, rate limiting so a worker is not buried, and precision tuning so alerts are worth opening — a different product from a job alert digest.

**The feedback loop is minutes long and unusually rich.** Job matching waits weeks for a hire signal. Here a worker accepts, completes and is approved within an hour, so the model can learn continuously. That is an advantage the standard architecture does not exploit.

**Rank by effective rate, not by relevance or reward.** Job matching ranks by fit. Here the decision variable is money per hour for this specific worker, which requires a duration prediction joined to the reward — a composite target no matching product computes.

**The counterparty's history is a first-class ranking feature.** Requester rejection rate, payment speed and realised rate matter more to a worker's decision than the task's content. Surfacing counterparty reputation in the ranking and on the listing is central here and peripheral in job matching.

**Exhaustion and competition have to be modelled.** A batch shown to too many workers produces failed accepts and wasted time. Allocation-aware ranking — who is shown what, given that the supply is finite and disappearing — is closer to a real-time marketplace allocation problem than to a recommendation feed.

## Target Customer

Crowdsourcing platforms building a worker-facing discovery experience. Also shift-work and real-time gig platform vendors, whose alerting and allocation infrastructure is the closest existing fit, and worker-tooling builders who have proven the demand with extensions.

## Impact If Solved

The embedding, recommendation, alerting and push infrastructure gets reused, and the seconds-scale alerting, continuous learning, effective-rate ranking, counterparty reputation and allocation awareness get built. Concretely: a worker is told about a suitable batch while it still exists, which is what the extensions exist to approximate.
