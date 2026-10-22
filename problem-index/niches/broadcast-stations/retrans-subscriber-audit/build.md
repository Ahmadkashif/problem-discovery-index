# An Expected-Subscriber Model for Every System

**Niche:** [[niches/broadcast-stations/retrans-subscriber-audit/profile|Retrans Subscriber Reporting & Fee Audit]]
**Industry:** [[industries/broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Stations test each distributor's subscriber report against last month's; nobody tests it against what that system, given its own history and its peers, should have reported.
**Tags:** #bayesian-inference #exponential-smoothing #change-point-detection #hypothesis-testing #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche (contract audit firms, royalty-management vendors and in-house distribution finance teams) is fighting to test every distributor's reported subscribers, system by system, against an independent estimate of what each system should report, and whoever finds the shortfalls earliest and most completely takes the account.

## The Problem
A slow, steady decline looks like cord-cutting even when part of it is a dropped headend or a re-tiered package. Month-over-month checks catch sudden drops only, and contractual audits are expensive and limited.

## Why Nobody Has Built This
Each group sees only its own reports, under confidentiality. Audit firms work engagement by engagement on commission and have no standing model. The mapping of systems to markets changes constantly.

## What to Build
A hierarchical time-series model of subscribers by system, nested in distributor and DMA. It uses the system's own history, peer systems in the market, the distributor's public subscriber results and known events such as system sales. Each new report gets an expected range, and the model flags step changes that peers do not share. Flags are ranked by dollars at stake and by the remaining audit window, and each flag comes with an evidence pack for the distributor or the auditor.

## Target Customer
Distribution finance teams at TV groups, and audit firms that could run it across clients' portfolios with permission.

## Impact If Built
Audits target the systems where money is most likely missing, recoveries arrive within the limitation period, and the group goes into renewals knowing its true base.
