# What This Load Is Actually Worth to This Truck

**Niche:** [[niches/freight-tech-platforms/small-carrier-tools/profile|Small Carrier Tools]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A small carrier decides several times a day whether a rate is good, using a number that ignores deadhead, this truck's actual cost, and how hard it will be to get out of the destination — and every product sold to them reports a lane average.
**Tags:** #gradient-boosting #time-series-forecasting #dynamic-programming #confidence-intervals #evaluation-metrics #optimization-fundamentals #revenue-impact #worker-facing
**Contested on:** Every serious competitor selling to small carriers is fighting to tell an owner what a load is actually worth to them, net of deadhead, fuel and the next load's prospects, before they accept it — and whoever answers that in one screen takes the segment.

## The Problem
A load board shows $2,400 for 620 miles. It looks acceptable. It requires 180 miles of deadhead to reach the pickup, the destination is a market where outbound freight is thin this week, fuel has moved, and the driver's remaining hours mean the delivery appointment will consume an extra day. The carrier accepts, and the week is worse than it looks. The alternative load at $2,150 with 20 miles of deadhead into a strong outbound market was better by a wide margin. Both numbers were on the same screen and neither was comparable to the other.

## Why Nobody Has Built This
The load boards' business is listings and subscriptions, and a tool that helps carriers decline loads is not obviously in their interest. Brokers, who post the loads, have even less reason to build it. The carrier cannot build it because the inputs — its own cost structure, current fuel prices along the route, destination market conditions — sit in different places and none of them are assembled. And the segment is fragmented, price-sensitive and hard to sell to, which has kept serious product investment away from the largest population of freight capacity in the country.

## What to Build
A net-value calculation per load for this specific truck at this specific moment. Revenue less deadhead cost, fuel at the current price along the actual route, tolls, and the driver's time, against this carrier's own measured cost per mile rather than an industry figure. Then the piece that matters most and is hardest: the destination's outbound market strength, expressed as the expected rate and wait for the next load out — which turns a per-load decision into a sequence decision and is where most of a small carrier's lost money actually goes. Multi-load lookahead makes it a planning tool rather than a calculator. Everything is presented as one number with the components visible, because an owner-operator sitting in a truck stop will use a comparison and will not use a model.

## Target Customer
Owner-operators and small fleets, dispatch services acting for them, and the load boards and factoring companies who could differentiate by serving the carrier's interest rather than only their own.

## Impact If Built
Load selection is the single largest determinant of a small carrier's income and is currently made on a rate and an instinct. Correcting it for deadhead and destination market conditions changes the composition of the week rather than the effort, which is the only lever available to a business whose capacity is fixed at one truck. It is also the clearest case in freight where a tool built for the weaker party would change outcomes substantially.
