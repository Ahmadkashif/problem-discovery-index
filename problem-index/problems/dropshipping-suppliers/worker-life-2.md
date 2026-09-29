# Dispute Resolution Agent

**Industry:** [[dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Worker Life Changing
**One-liner:** A dispute agent adjudicates between a merchant and a supplier over an item neither the agent nor the merchant has ever seen, with evidence consisting of a photograph and two conflicting accounts.
**Tags:** #cnns #large-language-models #bert #gradient-boosting #evaluation-metrics #confidence-intervals #compliance #worker-facing

## The Problem
An order goes wrong. The item arrived damaged, or was the wrong colour, or never arrived, or is not what the listing showed. The merchant refunded their customer and wants the supplier to bear the cost. The supplier says it shipped correctly.

A dispute agent decides. Their evidence is a photograph the customer sent to the merchant who forwarded it, tracking data showing delivery, the listing images, and two accounts that disagree.

Nobody in the chain has seen the item except the customer, who is not a party to the dispute. The agent cannot inspect it, cannot verify the photograph is of this order, and cannot determine whether damage occurred in transit or before it.

The decision allocates a small amount of money and carries larger consequences: a merchant who loses disputes repeatedly leaves the platform, and a supplier who loses repeatedly may too, and the platform needs both.

Volume is high because dropshipping's failure rate is structurally higher than warehoused retail — more handoffs, longer transit, less quality control, no one inspecting before it ships.

## Why It Matters to the Worker
Adjudicating without evidence is the core difficulty. The agent applies policy to facts that cannot be established, repeatedly, and knows that a meaningful share of decisions are wrong in one direction or the other.

Both parties are customers. Unlike a court, the agent has a commercial relationship with everyone in the room, and the platform needs the merchant's subscription and the supplier's catalogue. That is a genuinely uncomfortable position that policy does not resolve.

The volume is emotionally weighted. Merchants disputing are frequently small operators for whom the amount matters and who have already refunded a customer and absorbed a review, and their frustration is directed at the agent.

And the patterns go unused. An agent handling disputes daily knows which suppliers generate them, which products are chronically misdescribed, and which failure modes recur — and that observation typically has no route to sourcing or to catalogue.

## What a Solution Looks Like
Evidence assembly before adjudication. The order's full history — supplier, product, tracking events, this supplier's dispute rate for this product and destination, whether similar disputes have been upheld — turns a two-account standoff into a decision with base rates.

Image comparison against listing photographs. Whether the item received matches what was listed is a visual comparison the agent does by eye and that can be assisted, including detecting when a photograph does not correspond to the order at all.

Pattern-based resolution. A supplier with a high dispute rate on a specific product is evidence about this dispute, and consistent treatment across similar cases is both fairer and faster than case-by-case judgement.

Prevention through routing. Disputes cluster on identifiable supplier-product-destination combinations, and surfacing that to merchants before they list is worth more than resolving the dispute afterwards.

A feedback route to sourcing and catalogue, with dispute patterns aggregated by supplier and product, so the queue informs the platform rather than only absorbing its failures.

## Impact If Solved
Disputes are the visible symptom of the model's structural failure rate and are adjudicated without evidence between two parties the platform cannot afford to lose. Assembling base rates and comparing images makes decisions defensible, and routing the patterns upstream addresses the supplier and product combinations that generate them.
