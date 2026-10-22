# Incrementality Measurement for Discount Nights and Passes

**Niche:** [[niches/movie-theaters/ticket-pricing-and-subscriptions/profile|Ticket Pricing & Subscriptions]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Circuits know that discount Tuesdays and subscriptions fill seats, and can't say how many of those seats would have sold at full price anyway.
**Tags:** #causal-inference #hypothesis-testing #gradient-boosting #survival-analysis #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price each showtime, seat type and subscription so that discount nights and passes fill empty seats without cannibalising full-price weekend sales, and whoever measures that cannibalisation honestly takes the account.

## The Problem
A subscription that brings a member twice a month at an effective $6 a visit looks like growth until some of those visits turn out to be weekend visits the member would have paid $14 for. Discount nights shift demand as well as create it. The loyalty data to tell the difference exists, member by member.

## Why Nobody Has Built This
Loyalty platforms report activity, not causal effects; circuits run national changes with no control theatres; and the answer may be commercially uncomfortable.

## What to Build
A measurement system on the member-level visit history: matched comparisons of members before and after joining a pass, staggered rollouts across theatres as natural experiments, and visit-shift models that separate new visits from moved ones. It reports net margin per programme including the distributor's share and concession spend.

## Target Customer
Revenue management and loyalty leaders at circuits with 100+ theatres.

## Impact If Built
Knowing true incrementality lets a circuit reprice passes and discounts toward the members and showtimes where they create visits, a margin effect plausibly worth ~1–2% of admissions at a large circuit (estimate).
