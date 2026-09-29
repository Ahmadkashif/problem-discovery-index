# Substitution & Order Accuracy

**Parent Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Category:** Low Digitized
**Contested on:** Whether the substitution decision made in an aisle in ninety seconds can be informed by anything other than the shopper's guess about a stranger's preferences.

## Profile
**Market Size:** ~$9B — 10% of US gross order value
**Share of Parent Industry:** ~10%
**Digital Adoption:** Low — a chat message, a photo, and a shopper deciding alone
**Target Buyer:** Platform grocery operations; retailers; shoppers
**Automation Potential:** High — the preference signal is in the platform's order history and unused

## What Makes This a Distinct Niche

A shopper standing in an aisle has ninety seconds to decide what to substitute for an out-of-stock item, and the rating consequences of getting it wrong fall on them. The customer is frequently unreachable. The app offers a list of loosely related products ranked by something that is not the customer's preference. The shopper picks, and finds out whether it was right when the rating arrives.

The niche is distinct because the decision is a genuine preference inference problem — which alternative would this specific customer accept for this specific item — and because the consequences are misallocated. The platform owns the preference data, the retailer owns the inventory accuracy, and the shopper owns the rating outcome.

It separates from order accuracy generally because substitution is the hard case: a missing item is a known failure, and a wrong substitution is a decision that was made badly. The rest of accuracy — picked the wrong size, missed an item, damaged produce — is a quality problem with ordinary solutions.

## Current Tools & Gaps

Platforms provide substitution suggestion lists, customer-set preferences at order time, and in-app chat to ask the customer. Retailers supply inventory feeds of varying quality, and real-time stock accuracy in grocery is notoriously poor — the item shown as available is frequently not on the shelf. Some platforms let customers pre-approve categories of substitution.

The gaps are that suggestions are catalogue-similarity rather than preference-learned, that the customer's own order history across months is not consulted, that unreachability is treated as an edge case when it is the common case, and that the rating consequence sits with the shopper rather than with whoever's information was wrong. Inventory accuracy, which causes the whole situation, is a retailer problem that the shopper absorbs.

## Problems
- [[niches/gig-delivery-platforms/substitution-and-accuracy/build|🔨 Build: Preference-Learned Substitution from Order History]]
- [[niches/gig-delivery-platforms/substitution-and-accuracy/buy|🛒 Buy: Retail Recommendation Engines Adapted to a Forced Choice]]
- [[niches/gig-delivery-platforms/substitution-and-accuracy/fix|🔧 Fix: The Rating Lands on the Person Who Guessed]]
