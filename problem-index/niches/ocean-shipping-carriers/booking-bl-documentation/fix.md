# The Amendment Fee Nobody Wanted to Charge

**Niche:** [[niches/ocean-shipping-carriers/booking-bl-documentation/profile|Booking, Shipping Instruction & B/L Documentation]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** B/L amendments after issue cost the shipper a fee and the carrier a dispute, and most trace back to errors that were visible when the SI arrived.
**Tags:** #large-language-models #evaluation-metrics #quick-win #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn shipping instructions into a correct bill of lading before the SI cut-off, and whoever issues the highest share of bills of lading with no post-issue amendment takes the account.

## The Problem
A shipper finds a wrong consignee tax ID or cargo weight on the final B/L, asks for an amendment, and disputes the amendment fee (~$50–150, estimate) because the error was the agent's. Nobody can show whose error it was.

## Why It's Still Broken
SIs and drafts are not compared field by field, and the shipper's approval of the draft is often a reply email that does not say what was checked.

## What a Fix Looks Like
Diff every SI against the draft and the final B/L, show the shipper exactly which fields changed and who changed them, and flag fields that differ from the shipper's history before the draft goes out.

## Who Feels the Pain
Documentation agents, customer service staff handling fee disputes, and shippers paying for errors.

## Impact If Fixed
At amendment fees of ~$50–150 (estimate), a clear record of responsibility on ~100,000 amendments a year at a large carrier (estimate) settles ~$5–15M of fees without dispute.
