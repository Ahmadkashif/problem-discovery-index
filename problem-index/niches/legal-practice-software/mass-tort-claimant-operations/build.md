# Claimant Qualification as a Measured Production Line

**Niche:** [[niches/legal-practice-software/mass-tort-claimant-operations/profile|Mass Tort — Claimant Operations at Scale]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mass tort firm's profitability is decided by cost per claimant per stage, and no system in the category measures it, so firms scale operations they cannot see and discover the cost structure after the litigation resolves.
**Tags:** #survival-analysis #gradient-boosting #evaluation-metrics #confidence-intervals #descriptive-statistics #optimization-fundamentals #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in mass tort software is fighting to move forty thousand claimants through record retrieval, proof of exposure and lien resolution without an operation that collapses under its own headcount — and whoever holds throughput per claimant lowest takes the account.

## The Problem
A firm signs 40,000 claimants. Two years later it has spent an amount it can total and cannot decompose. It does not know what a claimant costs to qualify, which stage consumes the money, how long each stage takes, or what share of claimants who enter a stage ever leave it. It cannot answer the operationally decisive question — should the next 10,000 claimants be acquired at all, given what the last 10,000 cost to process — because it has no unit economics. The firm is running a factory and reading a bank balance.

## Why Nobody Has Built This
Case management systems were designed around the matter as the unit of legal work, not the claimant as a unit of production, so cost, time and yield per stage are not concepts the data model holds. The work is also distributed across vendors and contract teams whose invoices arrive aggregated and monthly, so attributing cost to a claimant means pushing measurement into suppliers who have no reason to cooperate. And the litigations are episodic: a firm builds an operation for one product, the litigation resolves, and the institutional learning disperses before anyone generalises it.

## What to Build
A claimant pipeline with explicit stages, per-stage cost and cycle time attributed at the claimant level, and yield measured as the share advancing versus dropping at each gate. Every external vendor cost — record retrieval, review labour, expert screening, lien resolution — is attributed per claimant rather than booked monthly, which is a billing integration question more than a modelling one. On top of that sits the decision layer: predicted probability that a given claimant qualifies, given what is already known, so that expensive retrieval is sequenced toward claimants likely to clear and away from those who will not, and so that a firm can set an acquisition budget against a measured cost-to-qualify instead of a guess. Bottleneck analysis is the daily output — which stage is accumulating claimants, and what it is costing to hold them there.

## Target Customer
Mass tort firms running 10,000+ claimant inventories, the litigation support vendors serving them, and the claims administrators who could extend upstream from settlement into qualification.

## Impact If Built
Firms that instrument per-claimant economics for the first time routinely discover that one or two stages consume the majority of the cost and that a large share of that spend is applied to claimants who never qualify. Sequencing retrieval by qualification probability addresses both at once. The measurement also converts a firm's operational knowledge from something that disperses at the end of a litigation into something it carries into the next one.
