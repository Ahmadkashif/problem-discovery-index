# Order Accuracy and Substitution Decisions

**Industry:** [[gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A shopper standing in an aisle has ninety seconds to decide what to substitute for an out-of-stock item, and the rating consequences of getting it wrong fall on them.
**Tags:** #contrastive-learning #bert #k-nearest-neighbors #gradient-boosting #word-embeddings #evaluation-metrics #worker-facing #k-means-clustering

## The Problem
In grocery and retail delivery the courier is also a shopper, and a substantial share of items on any given order are unavailable. The shopper must decide: substitute with what, refund, or message the customer and wait for a reply that may not come while the aisle time accumulates.

The substitution decision requires product knowledge the app does not supply. Whether a different brand of the same product is acceptable, whether a size difference matters, whether a dietary constraint applies, whether the customer will accept a more expensive alternative — the shopper is guessing, quickly, about a stranger's preferences.

The consequences are asymmetric. A wrong substitution produces a customer complaint, a rating hit and sometimes a refund that the platform may attribute to the shopper. The shopper carries the reputational cost of a decision made under time pressure with inadequate information about a stock situation the platform's own catalogue failed to predict.

Stock data is the underlying failure. The platform's inventory view is frequently wrong, so items are offered to customers that are not there, and the shopper absorbs the discrepancy in the aisle.

## What Already Exists
Platforms provide substitution suggestions from catalogue relationships, customer preference settings where customers configure them, and in-app messaging to the customer. Some have invested seriously in real-time inventory integration with retail partners, which is the structural fix where partners support it. Barcode scanning verifies item identity. Shopper ratings and order accuracy metrics track outcomes.

## The Customisation Gap
Substitution suggestions come from catalogue adjacency — same category, similar price — rather than from what customers in this situation have actually accepted. The platform has millions of substitution events with their outcomes: accepted silently, accepted with a complaint, refunded, rated poorly. That is a direct preference dataset and it would produce substantially better suggestions than a category tree.

Per-customer inference is the second gap. A customer's order history reveals brand loyalty, dietary patterns, size preferences and price sensitivity, and a substitution ranked for this specific customer rather than for the average is a materially different suggestion. Most customers will never configure preferences manually and their history states them anyway.

Stock prediction is the third and would prevent the decision arising. Out-of-stock probability by item, store and hour is forecastable from the platform's own shopper-reported availability, and flagging likely unavailability at the moment of ordering — with a pre-agreed substitution — moves the decision to the customer where it belongs.

And the attribution should be fixed. A substitution that followed the platform's own top suggestion should not count against the shopper's accuracy metric, and separating shopper judgement from platform recommendation in the outcome data is a fairness correction that costs nothing.

## Impact If Solved
Substitution is the most frequent judgement call in grocery delivery, is made under time pressure with no useful information, and its costs land on the shopper. Outcome-learned suggestions, per-customer ranking from order history, and upstream stock prediction that moves the decision to the customer address the problem at three levels — and correcting the attribution removes a penalty that shoppers currently absorb for following the platform's own advice.
