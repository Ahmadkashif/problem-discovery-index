# It Costs More to Send Back Than It Is Worth

**Niche:** [[niches/dropshipping-suppliers/cross-border-returns/profile|Cross-Border Returns & After-Sales]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The item shipped from another continent, the customer wants to return it, return shipping exceeds its value, and every merchant in the category improvises the same bad policy alone.
**Tags:** #convex-optimization #gradient-boosting #evaluation-metrics #revenue-impact #workflow-orchestration #confidence-intervals #automation #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to resolve a return on an item that cannot economically go back where it came from — and whoever makes that decision correctly per order captures the margin the whole category currently writes off.

## The Problem
A customer says the item is the wrong size. The merchant's options are: refund and let them keep it, losing the full cost; refuse, and take a dispute and a negative review; or ask them to ship it back at a cost exceeding the item's value. Most merchants pick the first, for everything, forever. That policy is right for an eleven-dollar item and catastrophic for a ninety-dollar one, right for a change of mind and wrong for a supplier defect that should be charged back, and it is applied uniformly because making the decision properly per order requires information and effort no merchant has. Across the category this is a very large number nobody has added up.

## Why Nobody Has Built This
Returns are the merchant's problem by the platform's construction, so no platform has built the capability. The decision requires per-item economics, supplier terms and resale options that are all scattered or unknown. Reverse logistics for many merchants with a few items each has no obvious operator. And the cost hides inside refunds, where it is never separated from ordinary cost of goods.

## What to Build
Make the return decision per order, economically. Compute the correct action for each case from the item's value, the return reason, the customer's history, the supplier's terms and the available disposition options — which is a small optimisation that merchants currently replace with one blanket rule, and it is the core of the product. Distinguish supplier fault from customer change of mind, since the first should be recovered from the supplier and the second should not, and conflating them is why nothing is ever recovered. Offer graduated resolutions — partial refund, keep-and-replace, discount on a future order — because the binary of full refund or full return is the wrong choice set and the middle options are frequently better for both sides. Provide a local return address with consolidation across merchants, which is the piece that makes physical return viable at all and which no individual merchant can arrange. Route returned goods to resale, liquidation or disposal based on condition and value, so a returned item stops being a total loss. Charge back supplier-caused returns automatically with the evidence attached, which is the fix note's subject. Detect products whose return rate makes them unprofitable regardless of sales, since merchants routinely scale a product that loses money on returns. Give the customer a fast, clear resolution, since the slow improvised process is itself a major source of disputes and chargebacks. And report return cost per product and per supplier as a line merchants can see, because it is currently invisible and therefore unmanaged.

## Target Customer
Dropshipping merchants and aggregators, dropshipping platforms, and the reverse logistics operators who could serve them.

## Impact If Built
One blanket policy is right for an eleven-dollar item and catastrophic for a ninety-dollar one, and it is applied uniformly because the per-order decision is too much work. Consolidated local return addresses make physical returns viable at all, and separating supplier fault from change of mind is what makes recovery possible.
