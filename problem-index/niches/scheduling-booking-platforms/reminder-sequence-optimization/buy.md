# Experimentation Infrastructure, Applied to Messages

**Niche:** [[niches/scheduling-booking-platforms/reminder-sequence-optimization/profile|Reminder Sequence Optimisation]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Experimentation platforms, sequential testing and contextual bandits are standard equipment in consumer software, and an industry sending millions of messages a month runs none of it.
**Tags:** #hypothesis-testing #confidence-intervals #causal-inference #bayesian-inference #monte-carlo-methods #evaluation-metrics #cross-validation #automation
**Contested on:** Every serious competitor here is fighting to establish what a reminder should actually say, when, and through which channel, for whom — and whoever produces that evidence takes the category, because a feature deployed in every product has never been tested by anybody.

## The Problem
Randomised assignment, sequential monitoring, variance reduction and contextual allocation are solved engineering with open implementations and a large applied literature. A scheduling platform sends millions of reminders monthly against a clean binary outcome recorded hours later. It is close to an ideal experimental environment and no experiment has ever been run in it.

## What Already Exists
Open experimentation frameworks; sequential and always-valid testing methods that allow continuous monitoring without inflating error rates; variance reduction using pre-experiment covariates; multi-armed and contextual bandit libraries; and Bayesian approaches suited to many small strata. The statistical machinery is settled and free.

## The Customization Gap
The adaptation is to a multi-tenant estate of small operators. It requires: (1) randomisation at the appointment level within operators rather than across them, since operators differ enormously and between-operator assignment would confound everything — this is the central design decision; (2) hierarchical estimation, because each operator alone has too little volume and the pooled estimate is what makes per-sector and per-operator conclusions possible; (3) consent and transparency with operators, since these are messages sent in the operator's name to their clients, which makes unannounced experimentation a relationship problem rather than only an ethical one — the programme must be disclosed and opt-out must exist; (4) guardrails on harm, since a variant that reduces no-shows by irritating customers is not a win, and complaint rates, opt-outs and rebooking rates must be monitored alongside attendance; and (5) an outcome definition that is attendance rather than message engagement, because open and click rates measure the message and attendance measures the point.

## Target Customer
Scheduling and booking platform vendors, vertical platforms with reminder features, and the messaging providers who deliver these at volume.

## Impact If Solved
The infrastructure is commodity and the environment is unusually favourable, which makes the absence of any experimentation the notable fact. Within-operator randomisation and hierarchical pooling are the design adaptations, and the harm guardrails are what keep a winning variant from being a losing product.
