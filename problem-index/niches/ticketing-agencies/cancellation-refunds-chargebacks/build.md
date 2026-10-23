# Chargeback Forecasts the Day a Show Moves

**Niche:** [[niches/ticketing-agencies/cancellation-refunds-chargebacks/profile|Event Cancellation Refunds & Chargebacks]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Which buyers of a postponed show will file a chargeback is predictable on the day of the announcement, and ticketers find out when the disputes arrive.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to refund, credit or reissue every affected order within the organiser's policy and the card network's dispute window when an event is cancelled or moved, and whoever loses the fewest dollars to chargebacks per cancelled show takes the account.

## The Problem
A postponement affects tens of thousands of orders. Some buyers will happily keep tickets for the new date; others cannot attend and will dispute with their card issuer if a refund is not quick. The ticketer treats all orders alike and handles disputes one by one as they arrive.

## Why Nobody Has Built This
Chargeback tools are built for fraud, where the buyer is a criminal; here the buyer is a customer with a reasonable complaint. The useful signals (distance from the venue, the new date's day of week, resale purchase versus primary, past dispute behaviour) are scattered across systems.

## What to Build
A model scored on every order the moment an event status changes, estimating the probability of a chargeback within the dispute window. High-risk buyers get proactive refund or exchange offers, card-network alerts are worked first for them, and evidence packs are pre-built for the disputes that still arrive.

## Target Customer
Payments and customer operations heads at primary ticketers and resale marketplaces.

## Impact If Built
Fewer chargebacks and dispute fees per cancelled show, and a dispute ratio kept clear of card-network monitoring thresholds in a bad season (estimate).
