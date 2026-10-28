# Post-Sale Transport & Gate Release

**Parent Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to move a sold unit from the auction lot to the buyer without a damage or wrong-pickup dispute, and whoever has the lowest transit claim rate per thousand deliveries takes the account.

## Profile
**Market Size:** ~$800M a year in auction-arranged transport margin, dispatch, gate release and lot logistics for sold units (estimate), within a much larger car-hauling market
**Share of Parent Industry:** ~11% of auction, service and floorplan revenue (estimate)
**Digital Adoption:** Medium — loads are posted and dispatched through apps and load boards, but release at the gate and condition at pickup still run on paper passes, phone calls and the driver's own photos
**Target Buyer:** Auction transportation director; buyers who choose auction-arranged transport at checkout
**Automation Potential:** High for carrier matching, release verification and condition matching at pickup

## What Makes This a Distinct Niche
Digital sales made transport part of the auction's product. A dealer who buys a car 600 miles away clicks "ship it" at checkout. ACV Transportation dispatches through a network of third-party carriers, and Cox owns the Central Dispatch load board. OPENLANE runs transport out of operations including Mesa, Arizona, where it was hiring a software engineer on 2026-10-26. Manheim's digital arbitration window runs from delivery when transport is long, so transit time and transit damage feed straight into claims. Two disputes recur. Was the scratch there at the sale or done on the truck? And did the right carrier collect the car? Release fraud, where a fictitious carrier collects a sold unit, is a known car-hauling problem (recalled; not checked). Competitors include the auctions' own transport arms, load boards and dispatch platforms (Central Dispatch, Super Dispatch, RunBuggy, named from recall) and large haulers. The dealer's own transport arranging is a fix at [[niches/auto-dealers-independent/wholesale-auction-flippers/profile|Wholesale & Auction Flippers]], and a repossession agency's lot is [[niches/repossession-services/post-recovery-storage-transport/profile|Post-Recovery Storage, Transport & Release]].

## Current Tools & Gaps
Auction transport modules, load boards and carrier apps with electronic bills of lading, gate-pass printers and lot management systems. Gaps: no automatic comparison of pickup photos with the condition report, release by paper pass checked by eye, and storage days after sale not tied to anyone's decision.

## Problems
- [[niches/wholesale-auto-auctions/post-sale-transport-release/build|🔨 Build: Condition at Hand-Off Matched to the Condition Report]]
- [[niches/wholesale-auto-auctions/post-sale-transport-release/buy|🛒 Buy: Freight Load-Board Vetting Adapted to Single-Car Releases]]
- [[niches/wholesale-auto-auctions/post-sale-transport-release/fix|🔧 Fix: The Gate Pass Handed to the Wrong Carrier]]
