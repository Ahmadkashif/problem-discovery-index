# A Blackout Cost Model from Past Disputes

**Niche:** [[niches/broadcast-stations/retrans-negotiation-leverage/profile|Retrans Negotiation & Blackout Leverage]]
**Industry:** [[industries/broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every group has been through blackouts, and none has a model of what each one actually cost both sides that it can bring to the next negotiation.
**Tags:** #causal-inference #survival-analysis #bayesian-inference #monte-carlo-methods #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche (distribution consultants, economic advisers and the groups' own distribution teams) is fighting to estimate, distributor by distributor, what a blackout would cost each side in lost subscribers, fees and ratings, and whoever estimates that blackout cost most accurately takes the account.

## The Problem
In a renewal the distributor claims subscribers will not notice and the group claims they will leave. Both sides cite anecdotes. The group's negotiator decides whether to accept an offer or go dark mostly on instinct about how long the distributor will hold out.

## Why Nobody Has Built This
Blackout outcomes are scattered across public subscriber disclosures, the station's own ratings, distributor churn that only the distributor sees, and the group's past fee and advertising effects. No outside party has the group's side of the data, and each group has only a handful of events.

## What to Build
A model of blackout cost for each side, built from the group's past disputes and public ones. On the distributor side: subscriber change around each event, adjusted for trend. On the station side: lost fees, ratings and advertising effects, and the time to resolution. Pooled across events, it estimates each side's daily cost and the likely duration, with uncertainty, for any proposed standoff. It feeds the renewal decision with a quantified walk-away point.

## Target Customer
Group EVPs of distribution and their CEOs and boards, who approve going dark.

## Impact If Built
Negotiators set walk-away points on evidence, avoid blackouts that cost more than the rate gained, and hold firm where the numbers favour the station.
