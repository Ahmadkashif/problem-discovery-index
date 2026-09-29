# The Settlement File Nobody Joins

**Niche:** [[niches/payment-processors/network-outcome-intelligence/profile|Network Outcome Intelligence]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Fix (Pain Point)
**One-liner:** The authorisation decision is in one system and the settlement outcome is in another two days later, and joining them is nobody's job.
**Tags:** #data-integration #workflow-orchestration #evaluation-metrics #automation #quick-win #descriptive-statistics #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a network-scale record of approvals, declines and settlements into knowledge no issuer and no merchant can have — and whoever does that owns the empirical basis for questions the industry answers with folklore.

## The Problem
An authorisation is attempted and a decision is returned. Two days later a settlement file confirms what actually happened — settled, reversed, adjusted, disputed. The authorisation record lives in the processing platform. The settlement record lives in the finance and settlement systems. The two use different identifiers, arrive on different schedules and are owned by different teams. Joining them would produce a labelled record of every decision the processor has ever made, and it is not done, because the authorisation team does not need settlement and the settlement team does not need authorisation.

## Why It's Still Broken
Neither team needs the join for their own purpose, and a join that serves only a third purpose belongs to nobody — the organisational structure determines what data exists, and no team's requirements produced this one. The identifiers do not match cleanly, which makes it look like an engineering project rather than a pipeline. Nobody has costed what the missing dataset is worth. And the systems were designed separately at a time when the question did not exist.

## What a Fix Looks Like
Build the pipeline and give it an owner. Join authorisation to settlement continuously as infrastructure, which is the fix and is a modest engineering project with an enormous downstream payoff — everything in this analysis depends on it. Resolve the identifier mismatch explicitly, since it is the practical obstacle and is solvable with a mapping the two systems can both carry going forward. Carry a decision identifier through into settlement from now on, which makes the join exact for all future transactions rather than probabilistic. Handle the partial and adjusted settlements properly, since a reversal or an adjustment is an outcome and collapsing it loses the information. Retain the joined record as a first-class dataset with an owner and a service level, rather than as a reporting output. Make it available to the decisioning teams, which is the point and is currently blocked by the dataset not existing. Backfill where the historical join is feasible, since years of history become available immediately. Govern access properly, since the dataset is commercially sensitive and cross-merchant. Measure the join rate and completeness, because an incomplete join used as though it were complete produces biased conclusions. And name a team accountable for it, since the reason it does not exist is precisely that nobody is.

## Who Feels the Pain
Decisioning teams optimising against convention because the evidence is unassembled; merchants receiving authorisation performance nobody can improve systematically; and processors sitting on the industry's best dataset in two halves.

## Impact If Fixed
The organisational structure determined what data exists and no team's requirements produced this join. A continuous authorisation-to-settlement pipeline is a modest engineering project that unlocks every decisioning improvement in the category.
