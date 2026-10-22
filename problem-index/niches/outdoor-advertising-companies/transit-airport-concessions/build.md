# A Concession Bid Model With an Honest Downside

**Niche:** [[niches/outdoor-advertising-companies/transit-airport-concessions/profile|Transit, Airport & Street Furniture Concessions]]
**Industry:** [[industries/outdoor-advertising-companies|Outdoor Advertising Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Concession bids are won on a base-case revenue forecast, and the guarantee is owed in the bad case.
**Tags:** #monte-carlo-methods #bayesian-inference #time-series-forecasting #gradient-boosting #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to bid a minimum annual guarantee and revenue share that the concession's advertising will actually cover over a seven-to-ten-year term, and whoever forecasts concession revenue most honestly wins contracts without the write-downs that follow an overbid.

## The Problem
A concession bid commits the operator to a guarantee for seven to ten years and often to installing screens at its own cost. The forecast behind it is usually a single path: ridership or enplanements from the authority, a yield per passenger from a comparable system, a growth rate. When transit revenue fell short of forecast after 2020, guarantees that had looked prudent became losses; Outfront's 2023 impairments of $534.7M show the scale.

## Why Nobody Has Built This
Each operator bids a handful of large concessions a year, so the bid team rebuilds the model each time. The incentive inside the bid team is to win, and a model showing a high probability of shortfall is unwelcome. The comparable data (yield per rider or passenger by system, by year) is spread across the operator's own concessions and not organised for reuse.

## What to Build
A scenario engine that simulates concession revenue over the term from distributions of ridership or enplanement, advertiser demand by category, digital screen sell-through, and pricing, calibrated on the operator's historical yield across every concession it has run. It outputs the probability that revenue falls below the guarantee in each year, the expected shortfall, and the bid at which the concession breaks even at a chosen confidence. It also tracks each won bid against its simulated range so the model learns.

## Target Customer
Heads of transit and airport divisions and CFOs at the operators that bid national concessions; private equity owners evaluating concession-heavy portfolios.

## Impact If Built
Bids are priced on the downside the operator will actually carry. Avoiding one overbid on a major system is worth more than the whole tool costs over its life.
