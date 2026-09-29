# A Reference Price Worth Relying On

**Niche:** [[niches/virtual-economy-operators/price-discovery-and-market-data/profile|Price Discovery & Market Data]]
**Industry:** [[industries/virtual-economy-operators|Virtual Economy Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** People buy goods with real money at prices nobody publishes properly.
**Tags:** #descriptive-statistics #time-series-forecasting #evaluation-metrics #confidence-intervals #automation #data-integration #revenue-impact #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to publish a reference price people can rely on for goods they buy with real money — and whoever publishes it credibly takes the account.

## The Problem
A participant deciding whether a price is fair has a last-sale figure that may be a single manipulated trade, a third-party estimate of unknown provenance, or nothing. The operator holds every trade, every price and every quantity. Publishing a proper reference price with volume and depth is arithmetic. Its absence means every participant transacts on worse information than the operator could trivially provide, and the information gap is exploited by people who have assembled it themselves.

## Why Nobody Has Built This
Publishing reference prices acknowledges that this is a market with prices. It also makes manipulation visible and creates an expectation of accuracy the operator would be held to. The current asymmetry is not commercially harmful to the operator. And nobody has asked.

## What to Build
Publish an honest index and say how it is computed. Compute a volume-weighted reference price per item over a defined window, which is the core and is immediately more reliable than any last-sale figure. Exclude detected manipulation from the calculation, since including it publishes the manipulator's price as the truth. Publish volume, depth and spread alongside the price, as a price without liquidity context is misleading for thin items. Maintain a historical series from day one, which is what lets anyone see a trend or a break. Mark thin markets explicitly rather than publishing a confident figure from three trades. State the methodology publicly, which is what makes the number citable. Update at a stated frequency rather than opportunistically. Publish through an interface third parties can consume, since they will otherwise continue inventing their own. Show the price in real currency terms where an exchange rate exists, which is what participants actually think in. And treat the published price as a commitment to accuracy, because a reference price that is wrong is worse than none.

## Target Customer
Virtual economy operators, third-party marketplaces and price trackers, participants and trading communities, and market data vendors.

## Impact If Built
Every participant transacts on worse information than the operator could trivially provide, and the gap is exploited by those who assembled it themselves. A volume-weighted index with manipulation excluded and a published method is arithmetic with real consequences.
