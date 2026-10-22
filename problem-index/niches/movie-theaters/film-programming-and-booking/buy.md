# Retail Assortment Planning Adapted to Screen Time

**Niche:** [[niches/movie-theaters/film-programming-and-booking/profile|Film Programming & Booking]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retailers have allocated scarce shelf space across stores by local demand for decades; exhibitors allocate scarce screen time the same way by phone and memory.
**Tags:** #gradient-boosting #time-series-forecasting #optimization-fundamentals #feature-engineering #revenue-impact #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn each week's screen time into the most theatre margin, but that produces two contests with different winners: the weekly allocation of screens and showtimes, won by whoever forecasts each theatre's demand best, and the terms and settlement negotiated with each distributor, won by whoever keeps the best record of what was agreed and how each sales office settles. Decomposed into contested sub-niches below.

## The Problem
A circuit's film department decides each week how a fixed number of screens and showtimes is split across a changing set of films in dozens of theatres with different audiences. It is an assortment problem with a one-week shelf life and a supplier price that falls as the product ages.

## What Already Exists
Retail assortment and space-planning suites (Blue Yonder, RELEX, Oracle Retail) forecast store-level demand by item and allocate shelf space under supplier constraints, with clustering of stores by local behaviour.

## The Customization Gap
The adaptation needs: products with a life of four to eight weeks and no history before launch, so forecasts rest on comparable titles and presales; a supplier cost that slides by week of run rather than a fixed price; auditorium capacities and formats as the "shelves", with showtimes as the unit; distributor commitments on minimum run and screen count as hard constraints; concession spend as a co-product that depends on the audience the film draws; and a weekly decision deadline before tickets go on sale.

## Target Customer
Film departments at circuits of 20+ theatres with a programming analyst on staff.

## Impact If Solved
A proven allocation engine, re-pointed at screen time, gives a mid-size circuit a forecast-backed booking sheet without a data science team.
