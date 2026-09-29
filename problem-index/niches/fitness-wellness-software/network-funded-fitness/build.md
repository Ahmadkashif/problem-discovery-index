# Network Revenue Reconciled and Valued Per Visit

**Niche:** [[niches/fitness-wellness-software/network-funded-fitness/profile|Network-Funded Fitness]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A studio's network statement is a monthly total it takes on faith, in a relationship where the studio has no leverage, no itemisation and no way to check whether the visits it hosted match the visits it was paid for.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #data-integration #revenue-impact #compliance #automation
**Contested on:** Every serious competitor serving network-participating studios is fighting to let a small studio see, verify and reconcile what a fitness network actually owes it — and whoever makes network revenue legible takes those studios.

## The Problem
A studio hosted, by its own check-in records, 412 network visits last month across three networks. The statements total an amount that corresponds to somewhere between 380 and 400 visits at rates that vary by network, by class type and sometimes by the member's own plan tier in ways the studio does not fully understand. Reconciling would mean matching check-in records against statement lines, which the statements do not itemise in a form that permits it. The studio accepts the number. Whether it is correct, and whether the rate applied was the rate agreed, are unknown — as is, more fundamentally, whether the whole arrangement is profitable.

## Why Nobody Has Built This
The information asymmetry favours the network and there is no commercial pressure to close it: the studios are small, individually replaceable, and have no collective mechanism. Studio software vendors have integrated with networks to deliver check-in, which is what the network wanted, and have not built the reconciliation, which is what the studio would want. And the terms of network participation frequently discourage the studio from treating network members as its own, which has a chilling effect on building any capability around them.

## What to Build
A reconciliation and valuation layer on the studio's side. Every network check-in is recorded against the class, the instructor, the time and the member's network and tier, from the studio's own system. Statements are ingested and matched line by line, with unmatched visits and rate discrepancies itemised — which is the artefact that makes a conversation with a network possible at all. Beyond reconciliation, value each network visit properly: revenue per visit against the marginal cost of the spot and against what the spot would otherwise have earned, which is the calculation that determines whether participation is filling capacity or giving it away. Report by class and by hour, because the answer almost always differs — network visits into an empty Tuesday afternoon are pure gain and network visits into a full Saturday morning are not. That breakdown is what lets a studio manage its participation deliberately rather than accept it wholesale.

## Target Customer
Independent studios and small operators participating in employer, insurer and aggregator networks, and the studio platform vendors who could serve their side of the relationship.

## Impact If Built
Reconciliation recovers unpaid visits and rate errors that are currently invisible, which is immediate money. The larger effect is strategic: a studio that can see which hours network participation helps and which it harms can manage its allocation rather than accept the network's, which is the first negotiating position any of these studios has ever had.
