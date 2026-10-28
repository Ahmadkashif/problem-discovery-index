# Retail Recommendation Engines Adapted to Matching Units to Bidders

**Niche:** [[niches/wholesale-auto-auctions/dealer-consignment-conversion/profile|Dealer Consignment & Sale-Day Conversion]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** E-commerce recommendation is solved; an auction still notifies dealers through saved searches that fire on every match and get muted.
**Tags:** #k-nearest-neighbors #matrix-decompositions #gradient-boosting #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to sell a dealer's wholesale unit on its first run, and whoever posts the highest first-run conversion rate on dealer consignments takes the account.

## The Problem
A unit sells on its first run when the right three or four dealers are bidding. Auctions reach them through saved searches, broad email blasts and the buyer's own app alerts. Busy buyers mute them, and a unit that would have drawn a bid from a dealer two states away runs to an empty lane.

## What Already Exists
Recommendation engines from retail and media (collaborative filtering, learning-to-rank, the personalisation services in the large cloud platforms) learn from views, clicks and purchases to rank items for each user.

## The Customization Gap
Wholesale needs:
- a one-off inventory, where every car is new and leaves after the sale, so content features (year, make, model, trim, grade, mileage, colour, location) must carry the cold start;
- buyer intent from purchase history, retail inventory gaps and floorplan headroom, not just clicks;
- transport cost from the car to the buyer inside the ranking;
- a timing constraint, since a notification after the car has run is worthless;
- a cap per buyer per day, so alerts stay trusted.

## Target Customer
Marketplace product teams at the national auctions and independent-auction software providers.

## Impact If Solved
If better matching adds one active bidder to each unit, a 2–3 point lift in first-run conversion is plausible (estimate). Across ~4 million dealer-consigned units a year industry-wide (estimate), that is 80,000–120,000 fewer reruns.
