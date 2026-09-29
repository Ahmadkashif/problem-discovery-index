# Markdown Optimisation for Merchants Who Cannot Employ a Planner

**Niche:** [[niches/retail-pos-platforms/specialty-retail-merchandising/profile|Specialty Retail Merchandising]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Enterprise retail has optimised markdowns for twenty years with methods that are published and a data requirement the POS platforms already satisfy, and an independent retailer decides by looking at the rack.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #bayesian-inference #confidence-intervals #evaluation-metrics #optimization-fundamentals #revenue-impact
**Contested on:** Every serious competitor in specialty retail software is fighting to tell an independent retailer what to mark down, when, and by how much — and whoever moves end-of-season sell-through and margin most takes the account.

## The Problem
Week nine of a fourteen-week season. A style has sold 40% of its units. The owner does not know whether that is on pace, because "on pace" depends on the sell-through curve for that kind of item in that season at that price point, which she has never seen quantified. She waits two more weeks, gets nervous, and takes 30% off everything — which gives away margin on the sizes that were selling fine and is not enough to clear the sizes that were not. At the end of the season she carries goods she will liquidate at a loss and tells herself she bought badly. Some of it was buying; much of it was markdown timing.

## Why Nobody Has Built This
The capability was gated on analysts rather than on technology, and the vertical SaaS vendors serving independents grew out of payments and transaction processing rather than out of retail planning — so nobody in these companies has the retail planning background, and the customers cannot articulate a request for something they have never seen. Item-level forecasting for a single small store is also genuinely hard: a style in five colours and six sizes at one location generates very thin data, which is precisely the case where a single merchant cannot do it and a platform holding hundreds of thousands of merchants can.

## What to Build
Sell-through curves learned across the platform's merchant base, specialised to the merchant. A style's expected sell-through trajectory is estimated from comparable items across comparable stores — category, price point, season, region, store type — and the merchant's own history refines it as data accumulates. Against that curve, a style's actual sell-through at week nine is either on pace or not, which is the statement no independent can currently make. From there, markdown recommendations follow as an optimisation: the depth and timing that maximise expected margin given remaining weeks, remaining units, size and colour distribution, and the residual value of unsold goods. Recommendations are per item rather than per rack, which is the entire advantage over the current practice. Results are reported honestly against what would have happened otherwise, because a merchant will extend trust only in proportion to a track record they can see.

## Target Customer
Retail POS platforms with large specialty merchant bases, and directly the multi-store independents and small chains for whom a season's markdown error is a large number.

## Impact If Built
Markdown timing is the largest controllable margin lever in specialty retail and is currently exercised by instinct. Enterprise retailers adopted this technology because it moved margin by points, and independents have exactly the same problem with less slack. For the platform, cross-merchant sell-through curves are a capability no competitor can copy without an equivalent merchant base — the strongest defensible position available in a category otherwise competing on payment rates.
