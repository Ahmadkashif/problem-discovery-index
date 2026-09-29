# The Connection That Breaks Silently

**Niche:** [[niches/b2b-commerce-platforms/procurement-integration/profile|Procurement Integration]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A working punchout connection breaks when either side changes something, and nobody notices until the customer mentions that they have not been able to order for a fortnight.
**Tags:** #change-point-detection #automation #evaluation-metrics #data-integration #confidence-intervals #revenue-impact #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to connect to a large customer's purchasing system in hours rather than weeks — and whoever does that takes the account, because the connection is the condition of the relationship and its cost decides which customers are worth having.

## The Problem
A customer's procurement platform is upgraded. The session handshake now sends a field in a different format and the punchout fails. The customer's buyers see an error, assume the supplier's site is down, and order from an alternative supplier who is also in their catalogue. Two weeks later somebody mentions it. The distributor's monitoring covers their own storefront, which is up. Nobody was watching the connection, nobody was watching the customer's order volume, and the revenue went elsewhere for a fortnight with no signal on either side.

## Why It's Still Broken
The integration is treated as delivered once it works, and the project team moves on. Monitoring a connection requires exercising it, which nobody set up. The customer's buyers experience an error and route around it rather than reporting it, which is the rational response. And the volume drop is invisible in an aggregate that contains hundreds of accounts.

## What a Fix Looks Like
Monitor the connection and the volume. Exercise every punchout connection synthetically on a schedule and alert on failure, which is straightforward, cheap, and detects the break within the hour instead of within a fortnight — this is the fix. Monitor order volume per connected customer against their own baseline, since a connection can degrade rather than fail and a volume drop is the symptom that matters. Alert the customer as well as the distributor, since their buyers are experiencing an error they will not report and the customer's own team will want to know. Version and change-notify the integration on both sides, so an upgrade on either is a known event rather than a surprise. Validate incoming orders against the profile continuously, since a partial break shows up as malformed orders being handled by an operator rather than as an outage. Test connections after any platform release on either side, which requires knowing when those happen and is a procurement term worth having. Maintain a named contact on the customer's side for the connection, since resolving one requires somebody there and the project contact has usually moved. And report connection uptime per customer, because a connected customer with a broken connection is worse than an unconnected one and neither party currently measures it.

## Who Feels the Pain
Customers whose buyers cannot order and route to an alternative supplier; distributors losing a fortnight of an account's volume silently; and integration teams rediscovering a connection they thought was finished.

## Impact If Fixed
Synthetic exercise of every connection detects the break within the hour instead of within a fortnight, and it is cheap. Monitoring per-customer order volume against their own baseline catches the degradations that do not present as an outage.
