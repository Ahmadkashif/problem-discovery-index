# Payout-Partner Prefunding by Corridor-Day

**Niche:** [[niches/money-service-businesses/treasury-prefunding-settlement/profile|Treasury, Prefunding & Settlement Reconciliation]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Treasury prefunds each payout partner with a buffer set by habit, so some corridors run dry before holidays while others hold idle cash for weeks.
**Tags:** #time-series-forecasting #temporal-fusion-transformers #exponential-smoothing #optimization-fundamentals #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to prefund each payout partner and currency just enough each morning — no failed payouts, no cash idle abroad — and whoever forecasts payout demand by partner-day most accurately takes the account.

## The Problem
Payout demand by partner swings with US paydays, receiving-country holidays, school-fee seasons, FX moves and one-off shocks such as a devaluation or a tax change. A treasury analyst sets each morning's prefunding from yesterday's balance and a buffer, and tops up when a partner warns it is running low.

## Why Nobody Has Built This
Treasury systems forecast corporate cash, not hundreds of partner-currency balances driven by consumer behaviour. Transmitters' data teams work on growth and risk, and treasury is a small, conservative team.

## What to Build
Probabilistic forecasts of payout demand per partner, currency and day, using the send pipeline, paydays and holiday calendars on both sides, FX moves and past shortfalls, feeding an optimiser that sets prefunding against the cost of shortfalls and idle balances and respects each partner's cut-off times.

## Target Customer
Treasurers at transmitters with dozens of payout partners and currencies.

## Impact If Built
Fewer failed or delayed payouts, lower average balances held abroad, and capital released for growth or permissible-investment headroom.
