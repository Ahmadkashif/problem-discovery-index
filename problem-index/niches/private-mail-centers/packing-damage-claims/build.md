# A Packing Record With a Photograph and an Outcome

**Niche:** [[niches/private-mail-centers/packing-damage-claims/profile|Packing & Damage-Claim Liability]]
**Industry:** [[industries/private-mail-centers|Private Mail Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The store guarantees its packing and keeps no record of how any parcel was packed, so it can neither learn which methods fail nor prove a good pack when a claim is disputed.
**Tags:** #tacit-knowledge-ml #cnns #transfer-learning #gradient-boosting #survival-analysis #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to pack each walk-in item so it arrives intact at a price the customer accepts, and whoever can show a carrier or insurer how a damaged parcel was packed, and so wins the claim, takes the account.

## The Problem
A damaged-parcel claim is a dispute about something nobody saw. The carrier says it was packed badly; the store says it was packed well. The packer's method (double-boxed, two inches of foam, separate lamp shade) exists only in their memory, and the store's experienced packers' rules are taught by watching.

## Why Nobody Has Built This
Capture adds time at a busy counter; damage labels are rare and arrive through carrier and insurer channels the point-of-sale system does not see; and no single store ships enough fragile items to learn anything.

## What to Build
A fixed counter camera takes two photographs per parcel, item and finished pack, attached to the shipment record with box, materials, carrier and declared value. Claims and damage notices are joined back by tracking number. Across a franchise or point-of-sale vendor's stores, an image model classifies item handling class and a risk model estimates damage probability per method and box, learned from the methods experienced packers chose and how those parcels fared. The associate sees a recommendation and the photographs become claim evidence.

## Target Customer
Franchisors running packing guarantees; point-of-sale vendors; parcel insurers that would price store-packed parcels with evidence lower.

## Impact If Built
Fewer guarantee payouts, claims won with photographs instead of argument, and a new associate who packs to the network's learned standard in their first weeks (estimate).
