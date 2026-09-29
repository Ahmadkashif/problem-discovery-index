# Running a Monetary Policy Without Admitting It

**Industry:** [[virtual-economy-operators|Virtual Economy Operators]]
**Type:** High Impact
**One-liner:** Drop rates are money supply, sinks are withdrawal, and a rarity change is a revaluation — decided by designers optimising engagement with no forecast of what happens to prices people pay real money at.
**Tags:** #monte-carlo-methods #time-series-forecasting #markov-chains #bayesian-inference #confidence-intervals #causal-inference #evaluation-metrics #revenue-impact

## The Problem
When an operator issues items that trade for real money, every supply decision has a monetary consequence. Increasing a drop rate expands supply and depresses prices. A limited release creates scarcity that persists for years. Introducing a sink withdraws items and supports prices. Changing the rarity tier of an existing item revalues every unit in circulation. Adding a new item that supersedes an old one devalues the old one.

Those decisions are made by designers, on design grounds. The meeting considers engagement, progression pacing and monetisation; it does not consider the price path of items already held by players, because nobody in the room has a model of it and frequently nobody is even looking at the secondary market.

The consequences land on players as real financial outcomes. Communities in item-trading economies track prices closely, and a supply change that halves the value of a widely-held item is experienced as a loss of money. Operators generally respond that items have no real-world value under the terms of service, which is a legal position rather than a description of what happened.

The reverse error is equally common. Runaway scarcity in items that remain functionally necessary produces prices that exclude ordinary players and concentrate holdings, and the operator notices when the community complains rather than when the supply-demand balance turned.

And the internal effect is unmeasured. Item prices feed back into player behaviour — what is worth acquiring, whether opening a randomised container is rational, whether to keep playing — so monetary policy conducted blindly is also engagement policy conducted blindly.

## Why It's Unsolved
Acknowledging the monetary role creates obligations the operator would rather avoid. An operator that publishes a supply policy, forecasts price effects, and considers holders' positions is behaving like an issuer, and that framing attracts regulatory attention in a domain where operators have worked hard to maintain that items are licences rather than property.

Organisationally the secondary market is nobody's. Item design sits with game teams, the marketplace sits with platform engineering, fraud sits with trust and safety, and the aggregate economic state has no owner. In several large economies the trading happens largely on third-party sites the operator does not run and does not measure.

The modelling is also genuinely non-trivial. Item prices depend on supply, on utility that changes with balance patches, on aesthetic fashion, on speculative holding, and on the behaviour of a market with a substantial speculative component. Forecasting them is closer to asset pricing than to inventory planning, and game economy teams are not staffed for it.

And the short-run incentive points the other way. Supply events that flood the market generate immediate revenue from the sales that accompany them, and the price damage lands on holders over the following months, which is the same delayed-cost structure that runs through every industry in this segment.

## What a Solution Looks Like
Model the economy as an asset market. Circulating supply per item, issuance and sink rates, holder concentration, trade volume and price history are all observable to the operator, and a forecast of the price response to a proposed supply change is achievable — not precisely, but well enough to distinguish a change that will halve a widely-held item's value from one that will not.

Put the forecast in the design review. The specific intervention is that a supply decision arrives with its projected effect on circulating supply and on prices of existing holdings, so the trade is made deliberately. That single change would prevent the category of incident that reliably produces community crises.

Watch the aggregate. Concentration of holdings, the share of items held speculatively rather than used, the price level relative to what an ordinary player can reach, and the rate of new-player acquisition of basic items are diagnostic and are on nobody's dashboard.

Measure the behavioural feedback. Price levels change what players do — whether they open containers, whether they trade, whether they keep playing — and estimating that link makes the economic decisions legible in the terms the design team already cares about, which is how this gets adopted rather than ignored.

And include the third-party layer. In several of the largest item economies most trading happens off the operator's own marketplace, and an operator measuring only its own venue is looking at a minority of its economy.

## Impact If Solved
These operators run economies with real monetary stakes for millions of participants and manage them with none of the instrumentation that any other issuer would consider mandatory. Forecasting price effects before supply decisions ship, monitoring the aggregate state, and measuring the behavioural feedback would prevent the recurring community crises that follow unmodelled supply changes — and would give the operator a defensible account of its own decisions at a moment when regulators in several jurisdictions are taking an increasing interest in exactly this.
