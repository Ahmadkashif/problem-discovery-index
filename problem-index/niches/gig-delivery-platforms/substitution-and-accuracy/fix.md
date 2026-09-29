# Fix: The Rating Lands on the Person Who Guessed

**Niche:** [[niches/gig-delivery-platforms/substitution-and-accuracy/profile|Substitution & Order Accuracy]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The item was out of stock because the retailer's inventory was wrong, the customer did not answer the chat, and the shopper's rating pays for both.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #causal-inference #worker-facing #quick-win #workflow-orchestration
**Contested on:** Whether the rating consequence of a substitution can be attributed to the party whose information or absence caused it.

## The Problem

A customer orders an item the platform showed as in stock. It is not on the shelf, because grocery inventory feeds are frequently wrong. The shopper messages the customer, who does not reply — most do not, within the window. The shopper substitutes, using a list built on catalogue similarity. The customer receives the wrong thing and rates the order down.

The rating attaches to the shopper. It affects their standing, their access to batches, and in aggregate their deactivation risk. The causes — a bad inventory feed and an absent customer — attach to nobody.

This repeats several times per shift for a grocery shopper. It is the defining feature of the role and the primary source of its rating volatility.

## Why It's Still Broken

Ratings are collected per order and attributed to the shopper because the shopper is the identifiable party. The system has no concept of attributing an outcome to an inventory feed or to a non-responsive customer, and adding one requires deciding what to do with the attributed share — which means telling a retailer their data is bad, or telling a customer their rating will not count.

Inventory accuracy specifically is a retailer responsibility that the platform has little leverage over and considerable incentive not to press, since retailer relationships are the supply of the grocery business. So the cost of bad inventory data flows downhill to the only party with no leverage at all.

And nobody has measured the attribution. The platform could determine, today, what share of low ratings follow a substitution, what share of substitutions follow an out-of-stock on an item the feed showed available, and how those rates vary by store. None of it is computed, so the problem has no size and therefore no owner.

## What a Fix Looks Like

Measure the attribution, then act on it in the ratings arithmetic.

Compute the chain from existing data: orders containing a substitution, substitutions caused by a stock discrepancy against the feed, customer responsiveness during the substitution window, and the rating outcome. Aggregate by store, by retailer, by item category and by time. This is descriptive statistics over the order log and it produces the first honest picture of where substitution failures originate — which on most platforms will point overwhelmingly at a subset of stores with bad feeds.

Exclude or discount ratings where the causal chain is clear. An order whose only complaint relates to a substitution forced by a feed error, with a customer who did not respond to the chat, should not count against the shopper's standing. This requires no judgement about the shopper's choice — it is a lookup on whether the item was shown available and whether the customer was reachable. Ratings stay visible; they simply stop driving consequences the shopper could not control.

Ask the customer the right question. Rating an order lumps delivery speed, item quality, substitution acceptability and packing into one number. Item-level substitution feedback — was this substitution acceptable — is a single tap, gives a clean label for the substitution model, and separates the shopper's performance from the substitution outcome.

Report inventory accuracy to retailers, per store, against peers, with the substitution and refund cost attached. Retailers largely do not know their feed accuracy at shelf level, and this is the report that makes it actionable. It is also the only mechanism by which the root cause improves.

Make unreachability an expected path, not a failure. A customer who does not respond within the window should have a pre-stated preference — substitute freely, refund instead, or a per-category rule — captured at order time when they are present and attentive, rather than solicited in the aisle when they are not.

## Who Feels the Pain

Grocery shoppers, whose standing is set substantially by decisions forced on them by other parties' errors, and who carry deactivation risk from it. Customers who receive wrong items and blame a person who did their best with a bad list. Retailers who never learn their feeds are wrong. And the platform, which absorbs refunds and churn from a cause it has never quantified.

## Impact If Fixed

The rating consequence lands where the cause is, which is the minimum condition for the shopper's score to mean anything. Inventory accuracy gets reported to the party who can fix it, with a cost attached. And the substitution decision gets a clean item-level label, which is what the preference model needs to be built at all.
