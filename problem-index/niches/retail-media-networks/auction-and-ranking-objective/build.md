# Bid Times Predicted Click Is Not the Objective

**Niche:** [[niches/retail-media-networks/auction-and-ranking-objective/profile|Auction & Ranking Objective]]
**Industry:** [[industries/retail-media-networks|Retail Media Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every network licenses the same auction technology and ranks on bid times predicted click, while the retailer's actual objective is a mix of relevance, margin, inventory, private label and long-run basket that no vendor platform expresses.
**Tags:** #convex-optimization #gradient-boosting #loss-functions #evaluation-metrics #revenue-impact #confidence-intervals #optimization-fundamentals #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to rank a sponsored slot by the retailer's real economics rather than by bid times predicted click — and whoever expresses that objective properly earns more from the same inventory while giving the shopper a better page.

## The Problem
The top slot goes to whoever bids most times their predicted click rate. That product may be the retailer's lowest-margin item, may be out of stock at the shopper's store, may be displacing a private label product the retailer makes far more on, and may be less relevant than the organic result beneath it. The auction is indifferent to all of it, because the objective was written for a publisher who sells attention and has no stake in what is purchased. A retailer has a stake in everything about what is purchased — the margin, the stock position, the basket it sits in, the trip it triggers — and prices its most valuable inventory with a function that ignores every one of them.

## Why Nobody Has Built This
The auction came from web publishing where the seller has no interest in the outcome, and nobody rewrote the objective when the model moved into retail — the inherited assumption is invisible precisely because it is inherited. A shared vendor platform cannot encode any one retailer's margin strategy without conflict. Margin, stock and basket data live in merchandising systems the media stack does not touch. And short-term media revenue is what the network is measured on.

## What to Build
Write the objective the retailer actually has. Rank on expected retailer value rather than expected advertiser payment, combining the advertisement revenue, the gross margin of what is likely to be bought, the displacement of an organic sale, and the shopper experience cost — this is the core and it is a straightforward reformulation once the data is connected. Bring margin and inventory into decisioning, which requires joining the media stack to merchandising and is the practical engineering work that has kept this undone. Model long-run basket and trip value, since the shopper who finds what they wanted returns, and a ranking that ignores that optimises a week and costs a year. Handle private label explicitly as an economic term rather than as a manual carve-out, because it is currently managed by exclusions that nobody can justify numerically. Account for local stock position, which is the fix note's subject and produces the most visible failures. Price the shopper experience cost into the auction so it is a stated trade-off rather than an unexamined one, connecting to the ad load work. Keep the auction incentive-compatible, since a ranking that advertisers cannot understand or trust invites gaming and complaint — this constraint is what makes the reformulation non-trivial. Let merchandising set constraints in their own terms, which is what gives the category merchant standing. Validate through experiments on yield, margin and return visits together, since any one of the three can be improved at the others' expense. And report the difference against the bid-times-click baseline, because that comparison is the whole business case.

## Target Customer
Retail media networks of any size, retailers with meaningful private label or margin variation, and platform vendors whose objective function is a liability.

## Impact If Built
The auction came from a publisher who has no stake in what is purchased, and a retailer has a stake in all of it. Ranking on expected retailer value — advertisement revenue plus margin minus displacement and experience cost — is a straightforward reformulation once merchandising data is connected.
