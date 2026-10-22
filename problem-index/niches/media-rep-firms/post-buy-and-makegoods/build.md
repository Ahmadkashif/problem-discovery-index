# Continuous Posting With Makegoods Planned Mid-Flight

**Niche:** [[niches/media-rep-firms/post-buy-and-makegoods/profile|Post-Buy Posting, Makegoods & Reconciliation]]
**Industry:** [[industries/media-rep-firms|Media Representative Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Delivery against a ratings guarantee is computed after the flight, when the only fix left is giving away future inventory; computed weekly, it can be fixed inside the flight.
**Tags:** #gradient-boosting #time-series-forecasting #dynamic-programming #optimization-fundamentals #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to settle each flight (ratings posted against the guarantee, preempted spots made good, invoice matched to affidavit and order) before the agency's payment cycle closes, and whoever settles cleanest gets the station paid first and keeps audience-deficiency liability from piling up.

## The Problem
A station guarantees a buyer a number of rating points in a demo over a flight. The research analyst posts actual delivery after the flight ends. If the station fell short, it owes audience-deficiency units in a later period, often a busier one, giving away inventory it could have sold.

## Why Nobody Has Built This
Ratings used to arrive slowly and in sweeps, so posting was naturally a post-flight exercise. Faster big-data ratings now arrive, but the workflow hasn't changed.

## What to Build
A weekly posting engine per buy. As ratings arrive it compares delivery to date with the guarantee, forecasts remaining delivery spot by spot, and proposes in-flight adjustments (adding units, shifting dayparts) from unsold inventory while the flight is still running. It produces a makegood plan for preemptions that minimises inventory value given away.

## Target Customer
Research and sales operations leaders at rep firms and station groups.

## Impact If Built
Shortfalls are corrected inside the flight from unsold inventory instead of repaid later from inventory that could have been sold, and buys settle on time.
