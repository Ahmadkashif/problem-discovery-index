# A Booking Record That Joins the Call to the Settlement

**Niche:** [[niches/movie-theaters/film-programming-and-booking/profile|Film Programming & Booking]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The decision to give a film three screens and the terms paid for those screens live in different systems, so no exhibitor can say what a booking actually earned.
**Tags:** #large-language-models #gradient-boosting #causal-inference #feature-engineering #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn each week's screen time into the most theatre margin, but that produces two contests with different winners: the weekly allocation of screens and showtimes, won by whoever forecasts each theatre's demand best, and the terms and settlement negotiated with each distributor, won by whoever keeps the best record of what was agreed and how each sales office settles. Decomposed into contested sub-niches below.

## The Problem
A booking has two halves. The allocation (screens, auditoriums, showtimes, holdover or drop) is in the ticketing system. The price of that allocation (the sliding scale, any floor, any concession the distributor won in exchange for the big house) is in an email, and the final settled rent is in the general ledger weeks later. The buyer who made the call never sees its net result.

## Why Nobody Has Built This
Ticketing vendors stop at the gross, and accounting vendors start at the invoice. Terms are private and negotiated by phone, so no vendor holds them in structured form. Circuits large enough to build this treat their buying data as a trade secret, and small ones can't fund it.

## What to Build
A booking record per film per theatre per week that holds the allocation, the agreed terms extracted from confirmations, the buyer's expectation, the weekly grosses and concession sales, and the settled rent. On top of it: net margin per screen-week by film, distributor and buyer, and a report of the bookings whose settled terms made a "successful" film a loss.

## Target Customer
Heads of film and CFOs at regional circuits of 10–60 theatres; booking agencies that want to show owners what their bookings earned.

## Impact If Built
A circuit that sees net margin per booking can shift screens toward the films and distributors that pay, worth perhaps a point of film margin (~1% of admissions, estimate), and gives its buyers evidence for the next negotiation.
