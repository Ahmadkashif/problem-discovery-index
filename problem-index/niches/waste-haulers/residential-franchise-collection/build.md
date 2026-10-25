# Bid Assumptions Graded Against the Contract's Real Cost

**Niche:** [[niches/waste-haulers/residential-franchise-collection/profile|Residential Franchise & Municipal Contract Collection]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A franchise bid rests on assumptions about homes per route-hour, set-out rates and tons per home, and no hauler systematically checks those assumptions against the first year of the contract it won.
**Tags:** #gradient-boosting #monte-carlo-methods #linear-regression #confidence-intervals #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to price a multi-year franchise bid against routes it has never run, and whoever's bid lands closest to the realised cost per home over the contract term takes the account.

## The Problem
The bid analyst estimates routes from parcel counts and the hauler's experience in similar towns, adds disposal at the nearest site's gate rate, carts, overhead and margin, and submits. If the contract is won, operations runs it and finance reports its margin, but nobody returns to the bid workbook to see which assumption was wrong. The next bid repeats the error.

## Why Nobody Has Built This
Bids are infrequent per hauler and owned by individuals; won contracts are measured in accounting categories that do not match bid assumptions; and losing bids produce no cost data at all.

## What to Build
A bid model whose inputs are the drivers that operations later measures: homes per route-hour by density band, set-out rate, pounds per home by stream, travel time to disposal, cart replacement rate. After award, the system pulls actuals from route telemetry and scale tickets and grades each assumption. Monte Carlo ranges over fuel, wage and disposal-fee paths give the bid team a priced uncertainty band.

## Target Customer
Bid managers and municipal sales directors at regional haulers bidding 5–20 franchises a year.

## Impact If Built
A 3% error in cost per home on a 20,000-home, seven-year franchise at ~$25 per home per month is ~$1.3M over the term (estimate); halving that error on every bid compounds across the portfolio.
