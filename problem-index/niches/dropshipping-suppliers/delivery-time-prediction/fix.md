# The Parcel That Stopped Moving

**Niche:** [[niches/dropshipping-suppliers/delivery-time-prediction/profile|Delivery Time Prediction]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** The last tracking scan was nineteen days ago, the parcel is plainly lost, and nobody tells the merchant until the customer does.
**Tags:** #change-point-detection #survival-analysis #evaluation-metrics #automation #workflow-orchestration #quick-win #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to publish a delivery distribution for a specific supplier, service and destination that holds up — and whoever does that lets merchants make a promise instead of a guess.

## The Problem
A parcel scans into an international facility and then nothing. Day nine, nothing. Day nineteen, nothing. The tracking page faithfully displays the last known event and says in transit. The merchant, who is watching four hundred orders, has no idea. On day twenty-four the customer opens a dispute, and the merchant is now handling an angry conversation about a parcel that has been obviously lost for a fortnight, with the marketplace clock running against them. The evidence was sitting in the tracking feed the entire time and nothing was watching it.

## Why It's Still Broken
Tracking systems are built to display events, not to notice their absence — a gap produces nothing to display and therefore nothing to react to, which is the framing error at the centre. Normal transit gaps and abnormal ones look identical without a baseline per lane. Exception handling is a manual process nobody is staffed for at this order volume. And the loss surfaces as a dispute, where it is handled as a customer service event rather than a logistics one.

## What a Fix Looks Like
Watch for silence. Compute the expected gap between scans per lane and service, and alert when a parcel exceeds it, which is the whole fix and needs only the tracking history already held — the reason it does not exist is that nobody has framed absence as an event. Classify the stall by where it happened, since a customs hold, a carrier handoff failure and a lost parcel need different actions and are distinguishable by the last scan type. Tell the merchant proactively with a recommended action, because the merchant's advantage is entirely in acting before the customer does. Contact the customer first where the delay is confirmed, which converts a dispute into a service recovery and is the single highest-return action available. Open the carrier trace automatically rather than waiting for a manual claim, since claim windows expire and merchants routinely miss them. Decide reship or refund on the same economics as the returns work, rather than defaulting to refund. Aggregate stalls by lane and service to identify a broken route, which is usually a systemic problem affecting many merchants and is invisible one parcel at a time. Feed stall rates into supplier and service selection, so the choice of shipping method reflects its real failure rate. Track claim recovery, which most merchants never pursue and which is genuine recoverable money. And measure time-from-stall-to-merchant-notification, because that interval is the entire fix and is currently unbounded.

## Who Feels the Pain
Merchants finding out about lost parcels from angry customers; customers waiting weeks on a parcel that is gone; and platforms whose tracking product is technically accurate and operationally useless.

## Impact If Fixed
Tracking systems display events and a gap produces nothing to display, so absence is never noticed. Expected-gap thresholds per lane turn silence into an event, and reaching the customer before they complain converts a dispute into a recovery.
