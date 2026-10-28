# Three Channels, Three Prices

**Niche:** [[niches/parking-operators/rate-setting-yield-pricing/profile|Rate Setting & Yield Pricing]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Fix (Pain Point)
**One-liner:** The rate on the street board, the operator's app and the marketplace listing drift apart, so drivers book the cheapest one and the owner loses the difference.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to price every hour and every event at the rate that fills the facility without turning cars away, and whoever earns the highest revenue per available space against comparable nearby facilities takes the account.

## The Problem
An area manager raises the event rate on the board and in the PARCS but forgets one marketplace portal. Drivers booking ahead pay $25 while drive-ups pay $40, and the marketplace takes its commission on the lower price.

## Why It's Still Broken
Each channel has its own portal and login, and rate changes are typed into each by hand.

## What a Fix Looks Like
One rate calendar per facility that publishes to the PARCS, the operator's app and every marketplace through their APIs, with a daily parity check that scrapes the live listings and flags mismatches.

## Who Feels the Pain
Area managers, revenue analysts and owners reading lower average tickets on event nights.

## Impact If Fixed
If 10% of event bookings go through a stale lower rate at a $15 gap (estimate), a garage with 40 events a year and 200 booked cars an event recovers ~$12K a year.
