# Incentives Priced on Forecast Pickup

**Niche:** [[niches/visitors-bureaus/citywide-convention-bids/profile|Citywide Convention Bids & Incentives]]
**Industry:** [[industries/visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Bureaus offer citywide incentives against the block a group asks for, when what the city gains depends on the rooms the group will actually fill.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #tacit-knowledge-ml #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to forecast, before the incentive is offered, how many of a citywide convention's contracted room nights will actually be occupied, and whoever's forecast holds up against the post-event housing report takes the account.

## The Problem
An association asks for 2,000 peak rooms across eight hotels. Three cities are competing. The bureau's director decides on an incentive package worth several hundred thousand dollars (estimate), on the strength of their read of the group. If the group picks up 75% of its block, the city has paid for stays it did not get and the group may owe hotels attrition. If the director misjudges which groups book around the block, the incentive fund goes to the wrong bids year after year.

## Why Nobody Has Built This
No single bureau books enough citywides a year to train a model, and pickup data sits with housing companies and hotels. The meeting-history vendors record where a group met, not how well it filled its block.

## What to Build
A pooled pickup model across bureaus: each group's realised pickup in past cities, drive-in share, rate gap to nearby non-contracted hotels and rentals, competing events, and block structure, predicting realised pickup with an interval. Incentive offers are then priced per forecast realised room night, and the bid record captures the director's own forecast so the two can be compared. Outcome-based incentives (paid per realised room night) become easier to offer because both sides share the forecast.

## Target Customer
Chief sales officers at the top ~100 convention destinations (estimate), and groups of bureaus willing to pool data through their CRM vendor or a state association.

## Impact If Built
Incentive money buys realised stays, groups get blocks sized to avoid penalties, and the city's bid record shows which wins paid back.
