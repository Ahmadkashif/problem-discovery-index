# A Bid Forecast From the Doorway Photos

**Niche:** [[niches/self-storage-operators/lien-auction-execution/profile|Lien Auction Execution & Sale Proceeds]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An experienced auction buyer looks at three photos of a unit and knows within seconds whether it will fetch tens of dollars or more than a thousand. Nobody gives operators or marketplaces that read before the sale.
**Tags:** #cnns #transfer-learning #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to sell each lien unit for as much of the unpaid balance as its contents will fetch, and whoever recovers the highest share of the balance owed per auctioned unit takes the account.

## The Problem
Operators list every lien unit the same way, on the same weekday, with the same minimum bid. A unit with a motorcycle, tools and sealed furniture boxes sells for little in a quiet week with eight bidders. A unit of household trash still costs a cleanout. The operator cannot tell them apart before the sale and does not know how much of the balance it will recover.

## Why Nobody Has Built This
Marketplaces hold the photos and the winning bids but sell on bidder volume, not valuation. Photos are taken under rules that forbid entering or moving contents, so they are partial and dark. Each unit is unique, so the label (the hammer price) depends on bidder turnout as much as on the contents.

## What to Build
An image model fine-tuned on the marketplace's own archive of listing photos paired with final bids. It detects item categories visible from the doorway (vehicles, tools, appliances, furniture, boxes, bags) and estimates fill level. A second model predicts the hammer price from those features, the unit size, the region, the day and the number of registered bidders nearby. Operators get an estimated recovery per unit before scheduling. Marketplaces can time high-value units for weekends and alert the bidders who bought similar units before.

## Target Customer
Product leads at lien-auction marketplaces; VPs of operations at multi-state operators choosing a marketplace.

## Impact If Built
If better timing and bidder targeting lift average hammer prices by ~10–15% (estimate) on a few hundred dollars a unit, an operator selling 2,000 units a year recovers ~$50,000–100,000 more. Cleanouts are flagged before they waste a listing.
