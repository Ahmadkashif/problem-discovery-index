# Exposure Read Straight From the Cost Sheet

**Niche:** [[niches/tour-operators/tour-costing-currency-risk/profile|Tour Costing, Pricing & Currency Risk]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An operator's currency exposure exists only inside cost workbooks and the booking forecast, so nobody can say on any given day how many euros it is short, for which months, on which tours.
**Tags:** #monte-carlo-methods #time-series-forecasting #probability-distributions #confidence-intervals #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to publish a tour price a year or more ahead that still earns its target margin after the hotels, coaches and guides are paid in other currencies, and whoever lands closest to costed margin after currency moves takes the account.

## The Problem
Finance hedges a season-level guess (an illustrative "we'll need about €12M"), set before bookings arrive. As the season fills unevenly, the real exposure drifts away from the hedge. Popular itineraries add exposure; cancelled departures remove it; supplier payment dates move. Nobody recomputes it until the losses or windfalls show up.

## Why Nobody Has Built This
Cost sheets are idiosyncratic workbooks, and costs scale differently with load: per departure, per vehicle, per room, per traveller. Converting them into dated cash flows needs tour-specific logic that FX vendors do not write. Tour software vendors have not seen treasury as their problem.

## What to Build
A service that ingests cost sheets, tags each line by currency, payment date and cost driver, and combines them with departure-level booking forecasts. The result is a live exposure ladder by currency and month. On top, Monte Carlo simulation of exchange rates and bookings gives margin ranges by itinerary and departure, the hedge amount that brings margin variance within a target, and the price per itinerary that meets target margin at a stated confidence.

## Target Customer
CFOs and heads of product at outbound operators with ~$10M+ of non-dollar costs (estimate).

## Impact If Built
Hedges that follow bookings rather than a guess. Margin surprises caught months earlier. A defensible basis for price changes and surcharges (estimate: a point or more of margin protected in volatile years).
