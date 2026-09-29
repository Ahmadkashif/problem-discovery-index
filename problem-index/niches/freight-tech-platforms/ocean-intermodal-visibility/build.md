# One Reconciled Container Timeline From Contradictory Sources

**Niche:** [[niches/freight-tech-platforms/ocean-intermodal-visibility/profile|Ocean & Intermodal — Milestone Reconciliation]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A container's discharge is reported by the carrier on Tuesday, by the terminal on Wednesday, and by the drayage provider as not yet available on Thursday, and the importer has to decide which to believe.
**Tags:** #hidden-markov-models #bayesian-inference #graph-theory #evaluation-metrics #confidence-intervals #data-integration #automation #time-series-forecasting
**Contested on:** Every serious competitor in ocean and intermodal visibility is fighting to reconcile milestones reported by carriers, terminals, customs brokers and drayage providers into one true container timeline — and whoever produces the earliest correct availability and pickup signal takes the account.

## The Problem
An importer tracking forty containers has, for each one, a carrier status portal, a terminal website, a customs broker's update and a drayage provider's opinion. They disagree routinely. The carrier says discharged; the terminal says not yet available; the customs status says released but the terminal has not reflected it; the drayage provider says no appointments. The importer's logistics coordinator opens four browser tabs per container and forms a judgement. Demurrage accrues while this happens, and the charges are large.

## Why Nobody Has Built This
The sources do not agree and have no obligation to. Ocean carriers report on their own schedules with their own event vocabularies; terminals publish through websites built for gate operations rather than for integration; customs status flows through brokers. Reconciling them requires treating the true container state as latent and the reports as noisy, delayed observations of it — a modelling posture the category has not adopted, preferring to display each source's version and let the customer choose. Building it also requires per-source knowledge of each party's reporting lag and reliability, which accumulates slowly and is exactly the moat a serious entrant would want.

## What to Build
A latent state model of the container. The true state — where it is, whether it has cleared, whether it is physically available — is inferred from the reports, each weighted by that source's measured reliability and lag for that event type at that terminal. The output is one timeline with a confidence per milestone and an explicit statement when sources disagree materially, because a disagreement is itself actionable information. Availability prediction is the commercial core: given discharge, customs status, terminal congestion and appointment availability, when will this container actually be collectable, with enough lead time to book drayage before free time expires. Source reliability is measured continuously and is the asset — knowing that a particular carrier's discharge event leads the terminal's by eighteen hours at a specific port is worth more than any individual feed.

## Target Customer
Importers with meaningful container volume, freight forwarders and customs brokers, drayage providers scheduling against availability, and the visibility platforms currently displaying four contradictory sources.

## Impact If Built
Demurrage and detention charges on international containers are a large, avoidable and growing cost, and nearly all of it comes from not knowing early enough when a container will be collectable. A reconciled timeline with a predicted availability window converts reactive drayage scheduling into planned scheduling, which is where the charges disappear.
