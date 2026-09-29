# Network Routing Practice

**Niche:** [[niches/payment-processors/routing-and-network-optimisation/profile|Routing & Network Optimisation]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Telecoms and internet routing optimise path selection against measured quality continuously, and payment routing applies a cost table.
**Tags:** #graph-theory #optimization-fundamentals #evaluation-metrics #confidence-intervals #convex-optimization #change-point-detection #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to present the transaction in the way most likely to be approved — route, network, token, authentication, data — and whoever does that prevents the declines everybody else is busy retrying.

## The Problem
Choosing a path through a network against measured quality is core practice in telecommunications and internet operations. Routes are monitored continuously for performance, traffic is shifted when a path degrades, least-cost routing is balanced against quality of service, and the measurement is continuous and automated. Payment routing has the same structure — several paths to the same destination with different cost and different quality — and selects on a cost table configured periodically, with quality measured only in aggregate if at all.

## What Already Exists
Quality-aware route selection; continuous path performance monitoring; automatic failover and traffic shifting; least-cost routing balanced against quality thresholds; and route-level performance reporting.

## The Customization Gap
The adaptation is to a route whose quality depends on the transaction being carried. It requires: (1) quality that varies by the payload rather than by the path, since a route's approval rate differs by issuer, card type, merchant category and amount — routing decisions must therefore be per-transaction rather than per-flow, which is the structural difference from network routing; (2) a two-day feedback delay before the outcome is known, where network quality is observable in milliseconds; (3) routes that require commercial licences and network agreements to exist at all, so the option set is a strategic investment rather than a configuration; (4) a destination that reacts to the sender's behaviour, since issuers form views of acquirers and merchants; and (5) cost differences that are small relative to quality differences, which inverts the usual least-cost priority.

## Target Customer
Processor infrastructure and network teams, payment orchestration vendors, and network operations practitioners for whom payment routing is an unrecognised analogue.

## Impact If Solved
Network routing balances cost against continuously measured quality and payment routing applies a cost table. Quality varying by payload rather than by path makes the decision per-transaction, and a two-day feedback delay is the constraint network operations never faces.
