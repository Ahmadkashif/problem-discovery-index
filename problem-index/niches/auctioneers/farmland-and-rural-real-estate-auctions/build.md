# A Land Auction Price Model the Heirs Can Read

**Niche:** [[niches/auctioneers/farmland-and-rural-real-estate-auctions/profile|Farmland & Rural Real Estate Auctions]]
**Industry:** [[industries/auctioneers|Auctioneers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A land auctioneer wins the listing on a price-per-acre call made from local memory, and the heirs have no way to see how that number was reached.
**Tags:** #gradient-boosting #gaussian-processes #confidence-intervals #feature-engineering #tacit-knowledge-ml #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to convince heirs or a retiring landowner that a public auction on a set date will beat a private listing, and whoever's price-per-acre call against soil productivity and recent county sales proves closest to the hammer takes the account.

## The Problem
Four siblings inherit 320 acres (illustrative). One wants to farm it, two want cash, one lives out of state. An auctioneer tells them it should bring a certain amount per acre at auction and proposes splitting it into three tracts. Whether that call holds depends on soil ratings, drainage tile, the neighbour who wants the middle tract, interest rates and the price of corn on sale day, and on knowledge of local buyers the auctioneer cannot fully explain.

## Why Nobody Has Built This
Valuation models exist for lenders and investors, but none is tuned to auction outcomes: tract splits, buyer's-choice formats and the presence of adjoining owners. Land auction firms hold their own results without the staff to model them.

## What to Build
A parcel-level forecast for auction format, combining soil productivity, tillable share, improvements, cash rents, recent county sales and auction results, rates and commodity prices, with spatial smoothing across neighbouring sales. It compares tract-split scenarios, shows the comparables, and records the firm's own call next to the model's for grading after the sale.

## Target Customer
Land auction and brokerage firms in the Corn Belt and Plains competing with private listings.

## Impact If Built
Listings won on a number the family can follow, tract plans that fit the buyer pool, and a record that shows heirs the firm's past calls were honest.
