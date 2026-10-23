# Second-Visit Predictions for a Two-Person Box Office

**Niche:** [[niches/ticketing-agencies/nonprofit-arts-box-offices/profile|Nonprofit Arts & Small-Venue Box Offices]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most first-time buyers at a small arts organisation never return, and the box office has no way to know which ones would with the right offer at the right time.
**Tags:** #gradient-boosting #survival-analysis #transfer-learning #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a first-time single-ticket buyer into a returning subscriber or donor using only the box office's own records, and whoever lifts the second-visit rate for a box office of two people takes the account.

## The Problem
A regional theatre sells several thousand first-time tickets a season (estimate). The experienced box office manager knows the patterns: buyers for the holiday show rarely come back for drama, a group of four who bought early for a new play are good subscription prospects. That knowledge is applied to the few patrons the manager happens to notice, and the email programme sends everyone the same season brochure.

## Why Nobody Has Built This
Each organisation's data is small, a few thousand patrons, too few to train a model alone. The vendors that hold many organisations' data host it for them under member or licence terms and have not built pooled models. Arts organisations rarely employ analysts.

## What to Build
A second-visit and subscription-conversion model trained across many organisations under explicit opt-in, transferred to each one's own records, scoring every first-time buyer after the performance. It suggests the next offer (a similar show, a flex pass, a post-show event) and timing, and reports what worked to the box office each month.

## Target Customer
Patron services directors at theatres, orchestras and presenting venues with budgets under ~$10M (estimate), through their ticketing platform.

## Impact If Built
A few points more of first-timers returning compounds into subscriptions and donations, the two revenue lines a small arts organisation lives on.
