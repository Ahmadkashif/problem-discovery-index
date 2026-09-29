# Build: Rental Pricing Against Modelled Driver Earnings

**Niche:** [[niches/rideshare-fleet-operators/rental-pricing/profile|Rental Pricing & Driver Economics]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Price the rental as a share of modelled driver earnings for that market and vehicle, and underwrite the fleet as the correlated book it actually is.
**Tags:** #gradient-boosting #time-series-forecasting #survival-analysis #confidence-intervals #evaluation-metrics #monte-carlo-methods #revenue-impact #feature-engineering
**Contested on:** Whether expected driver earnings can be modelled well enough from the operator's own data to price against.

## The Problem

A fleet's rate card is a set of fixed weekly numbers and its risk position is the sum of a few hundred identical bets on market conditions it does not model. The rate that works at $340 in a strong market becomes the reason a third of the fleet stops paying in a weak one, and the operator has no warning because the warning would come from earnings data they cannot see.

The consequence is not just default. It is that the operator cannot tell the difference between a driver who is struggling and a market that is softening, so they respond to a systemic problem with individual collections calls — which is the observed behaviour across this industry and which does not work.

## Why Nobody Has Built This

The obvious data — driver earnings — sits with the rideshare platform and is not shared. That fact has been treated as the end of the analysis, and it is not: the operator holds a great deal of evidence about earnings without ever seeing an earnings statement.

The second reason is that fleet operators are small businesses with capital tied up in vehicles and thin analytical capacity. The person who would build this is also the person doing collections and arranging repairs. And the software vendors serving the category sell fleet operations — tracking, contracts, maintenance — rather than underwriting, because underwriting is what lenders do and the fleet does not think of itself as a lender.

It is, though. A fleet is a secured lender with a depreciating collateral base and a borrower whose income depends on a third party's algorithm.

## What to Build

An earnings-and-exposure model that prices the rate card and monitors the book.

**Model expected driver earnings** from what the operator can observe. Telematics gives hours the vehicle moved, distance, trip patterns, time of day and geography — which for a rideshare driver is close to a direct observation of their working pattern. The operator's own payment history is the ground truth: drivers who paid reliably for months were earning enough, drivers who fell behind were not, and a fleet of a few hundred vehicles over a few years is a real dataset. Add observable market conditions — platform incentive announcements, local event calendars, seasonality, weather, driver supply proxies — and the model estimates what a driver in this market working these hours in this vehicle can clear.

**Price the rate as a share of that**, not as an absolute. A rental at 30% of modelled median weekly earnings for the market is a rate that stays payable as conditions move, and it is a defensible number to quote to a driver and to a lender. The rate card becomes a function rather than a table.

**Underwrite the correlation.** Simulate the book under market-wide earnings declines of varying severity — what share of the fleet becomes unable to pay at a 15% earnings drop, at 25%, at 40%. This is a Monte Carlo over the earnings model and it produces the number every fleet lender should be asking for and none currently does. It also tells the operator how much market concentration they can carry.

**Detect softening early.** Aggregate telematics across the fleet gives utilisation, hours worked per vehicle and trip density in near real time. A market softening shows up as drivers working longer hours for the same payment reliability, then as declining utilisation, weeks before the missed payments arrive. Change-point detection on fleet-level aggregates is cheap and is the leading indicator the industry lacks.

**Model default as a duration problem.** Time-to-default with the covariates — market, vehicle, rate as share of modelled earnings, driver tenure, utilisation trend — gives a survival model that supports both pricing and intervention timing, and it is fitted from the operator's own contract history.

## Target Customer

Fleet operators above roughly fifty vehicles, where the analytical investment pays and the correlated exposure is material. More directly, the lenders and lessors financing those fleets, who currently underwrite on vehicle collateral and operator track record with no model of the underlying driver economics — and who are the party most exposed when a market turns.

## Impact If Built

The rate stops being a guess that works until it does not. The operator can see a market softening in their own telematics weeks before the defaults, which converts a crisis into a pricing adjustment. And the fleet's real risk — a concentrated bet on one metro's driver earnings — becomes a number that can be managed rather than an exposure nobody had written down.
