# Line-Time-Aware Concession Selling

**Niche:** [[niches/movie-theaters/concessions-and-food-and-beverage/profile|Concessions & Food and Beverage]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The theatre knows who bought a ticket for which show and when they will arrive, and still runs the counter as if each patron were a walk-in.
**Tags:** #gradient-boosting #time-series-forecasting #monte-carlo-methods #feature-engineering #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to raise food and beverage spend per patron in the few minutes between ticket scan and trailers without letting the line run past showtime, and whoever sells the most per head at the counter, kiosk, app or seat while holding service time takes the account.

## The Problem
On a peak night several shows start within minutes, the counter queue grows past the trailers, and patrons give up and walk into the auditorium empty-handed. Presales show exactly which shows will arrive when, but the counter isn't staffed or prepped against that curve, and pre-orders aren't pushed to the patrons most likely to walk away.

## Why Nobody Has Built This
Ticketing and point of sale are often the same vendor's modules but run as separate reports; mobile ordering was built as a convenience feature, not as queue control; and nobody measures walk-aways.

## What to Build
A model that forecasts arrivals and counter demand minute by minute from presales and showtimes, sets counter and kiosk staffing and popcorn batches for each peak, and targets pre-order offers in the app at patrons booked into the most congested start times. Measure walk-away rate from ticket scans without a concession transaction.

## Target Customer
VPs of food and beverage at circuits with 50+ theatres; operators of high-volume suburban multiplexes.

## Impact If Built
Recovering a fraction of walk-aways on peak nights could add ~$0.20–0.40 per patron at congested sites (estimate), at ~80% margin.
