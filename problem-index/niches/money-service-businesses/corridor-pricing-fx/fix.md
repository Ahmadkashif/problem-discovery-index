# Competitor Scrapes Nobody Joins to Volume

**Niche:** [[niches/money-service-businesses/corridor-pricing-fx/profile|Corridor Pricing & FX Margin]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Fix (Pain Point)
**One-liner:** Transmitters pay for daily competitor pricing data and look at it as a table, never as an input to their own volume.
**Tags:** #linear-regression #time-series-forecasting #descriptive-statistics #data-integration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set each corridor's fee and FX spread so the landed amount wins the sender's comparison while still paying back acquisition cost, and whoever prices each corridor-day most precisely takes the account.

## The Problem
Competitor prices arrive daily from a vendor feed or a scraper. Volume arrives daily from the transfer ledger. They are reviewed in separate meetings, so a lost week in a corridor is explained after the fact, if at all.

## Why It's Still Broken
The pricing feed is licensed by strategy or treasury and the ledger belongs to finance; the two use different corridor, amount-band and timestamp definitions, and nobody owns the join.

## What a Fix Looks Like
A daily corridor table aligning own landed amount, the best and median competitor landed amounts, and own volume and new senders by amount band, with alerts when the price gap and volume move together beyond normal ranges.

## Who Feels the Pain
Pricing managers explaining volume drops, corridor managers, and finance teams forecasting revenue.

## Impact If Fixed
Pricing reacts in days rather than weeks to a competitor move, from data the transmitter already pays for.
