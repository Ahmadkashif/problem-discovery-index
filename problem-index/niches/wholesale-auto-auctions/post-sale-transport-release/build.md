# Condition at Hand-Off Matched to the Condition Report

**Niche:** [[niches/wholesale-auto-auctions/post-sale-transport-release/profile|Post-Sale Transport & Gate Release]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The car is photographed by the inspector before the sale, by the carrier at pickup and by the buyer on arrival, and nobody compares the three sets until there is a dispute.
**Tags:** #cnns #object-detection #transfer-learning #evaluation-metrics #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to move a sold unit from the auction lot to the buyer without a damage or wrong-pickup dispute, and whoever has the lowest transit claim rate per thousand deliveries takes the account.

## The Problem
A buyer reports a new dent on delivery. The carrier says it was on the car at pickup. The auction points to its condition report, whose photos were taken in different light from different angles. Each party's photographs exist. Nobody has compared them, and the dispute is settled by argument or split.

## Why Nobody Has Built This
The three photo sets live in three systems (the auction's report, the carrier's electronic bill of lading app and the buyer's phone). Damage detection was built for condition reports, not for change detection between two shoots of the same car.

## What to Build
At pickup, the carrier's app guides a fixed shot list and the system aligns those photos with the condition-report photos panel by panel. A damage-detection model flags differences above a threshold and asks the driver to annotate them before the car leaves. The buyer's arrival photos are matched the same way. The result is a timestamped record of where each mark first appears, which settles who is liable.

## Target Customer
Auction transport directors; carrier networks that want fewer disputed claims; buyers using auction-arranged transport.

## Impact If Built
If 1–2% of deliveries draw a damage dispute (estimate) and half are settled by splitting the cost, a clear record settles most of them at once. At 300,000 auction-arranged deliveries a year at a national auction (estimate), that removes 1,500–3,000 split settlements at a few hundred dollars each.
