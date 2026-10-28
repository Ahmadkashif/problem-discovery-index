# First-Run Sale Probability on the Run List

**Niche:** [[niches/wholesale-auto-auctions/dealer-consignment-conversion/profile|Dealer Consignment & Sale-Day Conversion]]
**Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The auction decides each car's lane, slot and floor advice by habit, when the run list already holds everything needed to predict which cars will no-sell.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to sell a dealer's wholesale unit on its first run, and whoever posts the highest first-run conversion rate on dealer consignments takes the account.

## The Problem
On a physical sale day a lane runs hundreds of cars, and slot position matters. Cars late in a long lane meet thinner online attention, and some cars sell only in lanes known for their segment. On digital platforms the same choice is when to launch and how long to run. Dealer-sales staff advise sellers on floors from MMR and memory. The result is visible only afterwards: around four cars in ten offered in-lane do not sell.

## Why Nobody Has Built This
The data sits inside each auction's lane system and has been used for reporting, not prediction. Seller floors are the seller's decision, and auctions are wary of advice that looks like price-setting. Online bidder behaviour is new enough that historical lane rules have not been revisited.

## What to Build
A model scoring every consigned unit's first-run sale probability from condition grade, floor against MMR, segment, mileage, lane, slot, day, the bidders who have viewed or watched it, and the seller's history. A survival model of runs-to-sale estimates the cost of a no-sale in depreciation and fees. The output drives three actions: suggested lane and slot, a floor message to the seller ("at this floor, 35% chance; at MMR minus $400, 70%"), and targeted notifications to the bidders most likely to bid.

## Target Customer
Auction general managers and dealer-sales directors at chains and large independents; digital platforms' marketplace product teams.

## Impact If Built
Each point of first-run conversion on 700,000 dealer-consigned units a year, OPENLANE's scale, is 7,000 fewer reruns. At ~$150–300 in fees, transport and depreciation per rerun, that saves dealers $1–2M a year (estimate).
