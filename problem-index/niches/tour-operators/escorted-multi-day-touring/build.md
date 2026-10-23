# A Guarantee Decision With Its Odds Attached

**Niche:** [[niches/tour-operators/escorted-multi-day-touring/profile|Escorted Multi-Day Touring]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Escorted brands guarantee departures on a manager's read of the booking curve, and no system says how likely each date is to reach break-even or what guaranteeing it today is worth.
**Tags:** #survival-analysis #bayesian-inference #gradient-boosting #time-series-forecasting #tacit-knowledge-ml #revenue-impact #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to guarantee departures early enough for advisors to sell them without running them half empty, and whoever guarantees the most departures while holding load above break-even takes the account.

## The Problem
A brand with a few hundred itineraries and thousands of departures reviews each date at fixed checkpoints. Guaranteeing early helps advisors sell, which helps the date fill. Guaranteeing a date that then stalls means running a coach for twelve travellers, with hotel rooms, a tour director and guides all paid. The manager decides on pace against last year and on instinct. Some brands now guarantee most dates as a marketing promise, which moves the risk rather than removing it.

## Why Nobody Has Built This
Tour software vendors sell booking and inventory systems to an industry whose largest players build their own. The decision has no product category: it lives in a weekly meeting. Building it needs daily booking snapshots that most systems do not retain. The training labels are censored, because cancelled departures never show their outcome.

## What to Build
A departure-level forecasting service that sits on the operator's reservation data. It forecasts final load as a distribution and estimates the probability of reaching break-even. It also models the lift a guarantee gives to bookings, estimated from the brand's own history of guaranteeing dates at different points. Before each checkpoint, managers see a ranked list: dates safe to guarantee now, dates to watch, and dates where consolidation or cancellation is the cheaper outcome. Each recommendation carries its expected margin. Each decision is logged, and at season end the brand sees which guarantees paid.

## Target Customer
VPs of operations and heads of product at escorted brands with ~$50M+ in revenue (estimate), and the in-house platform teams that serve them.

## Impact If Built
Guaranteeing the right dates earlier lifts bookings on them, and avoiding guarantees on dates that stall saves a departure's loss each time. For a brand running thousands of departures, a point or more of margin is plausible (estimate).
