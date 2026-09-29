# Replenishment and Workflow Practice

**Niche:** [[niches/b2b-commerce-platforms/reorder-and-account-purchasing/profile|Reorder & Account Purchasing]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Vendor-managed inventory and business process workflow are both mature, and B2B reordering is a list of past orders with an add button.
**Tags:** #time-series-forecasting #workflow-orchestration #probability-distributions #convex-optimization #evaluation-metrics #automation #confidence-intervals #compliance
**Contested on:** Every serious competitor in this sub-niche is fighting to make a repeat order faster and more certain than phoning the rep — and whoever does that takes the volume, because the buyer knows what they want and is choosing between channels rather than between products.

## The Problem
A supplier managing a customer's stock levels and replenishing before they run out is vendor-managed inventory, a practice with decades of use in industrial distribution and demonstrated benefits on both sides. Routing an approval through an organisation's rules is business process workflow, equally mature. A B2B storefront has the consumption history that would support the first and a rudimentary version of the second, and offers a reorder button.

## What Already Exists
Vendor-managed inventory practice with consumption-based replenishment; min-max and reorder point models; business process workflow engines with delegation, escalation and audit; approval matrices driven by value, category and cost centre; and scheduled and standing order mechanisms.

## The Customization Gap
The adaptation is to a supplier who sees orders rather than stock levels. It requires: (1) consumption inferred from order history rather than observed from a customer's inventory, which is the standard vendor-managed inventory precondition and is unavailable here — inferring the cycle from the ordering pattern is the substitution and is tractable because these patterns are unusually regular; (2) workflow that spans two organisations, since the approver is the customer's employee and the platform is the supplier's, which no internal workflow engine assumes; (3) approval rules configured by the customer rather than by the supplier, which means the platform must expose configuration to a customer administrator; (4) integration with the customer's own procurement controls where they exist, since an approval in two places is worse than one; and (5) trust, since a supplier proposing what a customer should buy is commercially delicate and the proposal must be evidently in the customer's interest to be accepted.

## Target Customer
Distributors, their account buyers and approvers, and the industrial distribution practitioners whose replenishment methods transfer with an inference step.

## Impact If Solved
Vendor-managed inventory is proven in this industry and assumes visibility of the customer's stock. Inferring the consumption cycle from an unusually regular ordering pattern is the substitution that makes it available from the supplier's side alone.
