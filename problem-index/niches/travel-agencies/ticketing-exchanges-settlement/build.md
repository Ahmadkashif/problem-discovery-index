# Refunds Run Against the DOT Clock

**Niche:** [[niches/travel-agencies/ticketing-exchanges-settlement/profile|Air Ticketing, Exchanges & ARC Settlement]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Agencies that are merchant of record must refund within 7 business days, but learn of cancellations late, depend on airlines to return the money, and track it all by hand.
**Tags:** #gradient-boosting #logistic-regression #large-language-models #compliance #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to process exchanges, refunds and voids without manual rework, and whoever generates the fewest agency debit memos per thousand tickets takes the account.

## The Problem
When an airline cancels a flight or changes it significantly, a passenger who declines the alternative is owed a refund. If the agency charged the card, 14 CFR 260 puts the refund duty on the agency: 7 business days for card purchases, 20 calendar days otherwise. The agency often learns of the change from the traveller, not the airline, and the airline's funds arrive on their own schedule.

## Why Nobody Has Built This
Schedule-change notifications reach agencies through GDS queues in inconsistent formats; eligibility depends on fare, change type and the passenger's response; and the rule is recent, contested by ASTA, and not yet reflected in back-office products.

## What to Build
A refund engine that reads schedule-change queues and NDC order notifications, classifies each change against the significance rules, detects passenger declines, computes the refund, issues it through ARC or the card processor, tracks the deadline per ticket, and chases the airline's transfer of funds. A model predicts which changes will be declined so the agency is ready before the clock starts.

## Target Customer
Operations and compliance leads at TMCs, online agencies and consolidators that act as merchant of record.

## Impact If Built
Refunds issued inside the deadline with an audit trail, fewer consumer complaints to DOT, and visibility of how much refund cash the agency is fronting for airlines.
