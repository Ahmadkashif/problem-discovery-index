# A Channel Mapping Checker That Runs Before Every Change

**Niche:** [[niches/tour-operators/marketplace-channel-operations/profile|Experience Marketplace Channel Operations]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A new start time, a price change or a revised cancellation window is made once in the booking system and then appears differently, or not at all, on four marketplaces.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #automation #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep one live inventory of seats, prices and cancellation terms across the booking system and every marketplace, and whoever sells the last seat without an overbooking, a stale price or a mismatched refund takes the account.

## The Problem
Each marketplace models a product differently: options, ticket types, age bands, pickup points, time slots, inclusions, cancellation windows. Mapping is set up once and breaks silently when the operator changes something. Typical failures are a child price missing on one channel, a cancelled 4 p.m. slot still on sale on another, or a 24-hour cancellation policy displayed as 72 hours. Operators discover it from a traveller at the meeting point or a marketplace penalty.

## Why Nobody Has Built This
Each reservation vendor maintains its own connections and tests them technically, not semantically. They check that the API call succeeded, not that the product the traveller sees matches the operator's intent. Marketplaces police listings for their own rules, not the operator's.

## What to Build
A checker that reads the operator's product definitions and each marketplace's live listing via API or page content. It compares them field by field and semantically: times, prices by age band, inclusions, meeting point, cancellation terms. It runs after every change and nightly, and flags differences with a suggested fix before a booking goes wrong. Language models handle free-text inclusions and policy wording.

## Target Customer
Distribution leads at multi-product operators, and the reservation-system vendors themselves as an add-on.

## Impact If Built
Fewer overbookings, wrong-price bookings and policy disputes. Each one avoided saves a refund, a bad review and a ranking penalty (estimate).
