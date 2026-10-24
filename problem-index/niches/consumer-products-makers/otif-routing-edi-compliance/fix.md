# The Ship Notice Sent After the Truck Arrived

**Niche:** [[niches/consumer-products-makers/otif-routing-edi-compliance/profile|OTIF, Routing-Guide & EDI Compliance]]
**Industry:** [[industries/consumer-products-makers|Consumer Products Makers]]
**Type:** Fix (Pain Point)
**One-liner:** The advance ship notice goes out in an end-of-day batch, the truck reaches the distribution centre first, and the load is fined.
**Tags:** #quick-win #workflow-orchestration #automation #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep a maker's shipments inside each retailer's routing guide and on-time, in-full targets, and whoever keeps the maker's compliance fines lowest as a share of shipments takes the account.

## The Problem
Advance ship notices are generated when someone closes the shipment in the system, which at a busy dock happens hours after the truck leaves, often in an end-of-day batch. The truck reaches the retailer's distribution centre before the notice, and the load is fined or received late.

## Why It's Still Broken
The batch job was set up years ago, nobody connected it to the fines, and the fines arrive weeks later in finance under a code the dock never sees.

## What a Fix Looks Like
Trigger the notice from the carrier's pickup scan, check it against each retailer's timing rule, and alert the dock lead when it is late or the quantities do not match the pick. Report the fine code back to the dock weekly so the fix sticks.

## Who Feels the Pain
Shipping leads, EDI coordinators and the AR clerk disputing the fine.

## Impact If Fixed
A recurring fine category disappears, worth ~$10K–$40K a year at a mid-sized maker (estimate), for a small change to one integration.
