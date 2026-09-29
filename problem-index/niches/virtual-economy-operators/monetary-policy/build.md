# Treating Issuance as Issuance

**Niche:** [[niches/virtual-economy-operators/monetary-policy/profile|Monetary Policy & Supply Design]]
**Industry:** [[industries/virtual-economy-operators|Virtual Economy Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A designer changing a drop rate is changing a money supply and has no instrument that says so.
**Tags:** #time-series-forecasting #causal-inference #confidence-intervals #evaluation-metrics #optimization-fundamentals #monte-carlo-methods #revenue-impact #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to set drop rates, sinks and limited releases without a forecast of what they do to prices people pay real money at — and whoever supplies that forecast takes the account.

## The Problem
Every supply decision in these economies has a price consequence that real people pay in real money. Increasing a drop rate devalues existing holdings. A limited release creates a scarce asset whose price the operator determines by how many exist. Removing a sink inflates the currency. Designers make these calls on engagement grounds, in a tool that shows engagement, with no view of the secondary market and no forecast of the price effect.

## Why Nobody Has Built This
Modelling the price consequence makes the operator visibly responsible for an economy it prefers to describe as a game feature. The secondary market is often third-party and outside the operator's systems. Designers are not economists and have not asked for the instrument. And the losses fall on players rather than on the operator's reported numbers.

## What to Build
Give the designer the price consequence before the decision ships. Model the relationship between supply parameters and secondary market prices from the operator's own history, which is the core — every past change is a natural experiment and none has been analysed. Forecast the price effect of a proposed change before it ships, with an interval, since a point estimate on this is not credible and will be dismissed. Report a price index and a supply aggregate as standing metrics, as an economy with no measured price level is being run blind. Bring secondary market prices into the design tool, because a designer who cannot see the market cannot consider it. Model the distributional effect, as a supply change transfers value between holders and new entrants and the aggregate hides that entirely. Simulate limited releases before setting the quantity, which is the highest-leverage single decision in the category. Track every past parameter change against the realised price response so the model calibrates on the operator's own data. Warn when a change would devalue holdings by more than a threshold, which turns an invisible harm into a decision. Report the monetary effect alongside the engagement effect in the same review. And publish supply policy where it can be published, since predictability is itself valuable to a market.

## Target Customer
Virtual economy operators, platform economy designers, secondary marketplace operators, and games economics consultancies.

## Impact If Built
Every past supply change is a natural experiment in an economy with a complete transaction record, and none has been analysed. A forecast of the price effect before the change ships turns a design decision into a monetary one.
