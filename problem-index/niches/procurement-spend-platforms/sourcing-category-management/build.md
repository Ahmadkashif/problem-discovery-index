# The Event Assembled From What the Organisation Already Knows

**Niche:** [[niches/procurement-spend-platforms/sourcing-category-management/profile|Sourcing & Category Management]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A category manager builds a specification and normalises bids by hand for an event whose category the organisation has sourced four times before, with the prior specifications, contracts and bid responses sitting in the same system.
**Tags:** #bert #large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor in sourcing software is fighting to remove the assembly work from a sourcing event so the category manager spends the time on negotiation — and whoever cuts specification and bid normalisation effort most takes the account.

## The Problem
A category manager runs a competitive event for facilities services across twelve sites. She writes a specification from a prior contract and a set of stakeholder conversations, builds a pricing template, invites seven suppliers, and receives seven responses in seven structures — one prices per square foot, one per visit, one as a bundled monthly fee with exclusions, two include consumables and two do not, and one has quoted a scope she did not ask for. Normalising them into a comparable basis takes three days. The negotiation that follows, which is where her expertise matters, gets a fraction of the time and none of the analytical support.

## Why Nobody Has Built This
Sourcing tools were built to collect structured bids, which works exactly as long as suppliers complete the structure — and suppliers deviate because their own cost structures differ and because deviating is frequently in their interest. Normalising a deviation requires understanding what was offered, which was not achievable automatically until recently. Specification reuse requires the organisation's prior events to be retrievable and comparable, which requires classification and which almost no procurement organisation has invested in. Both are now tractable and neither has been built.

## What to Build
Assembly from the organisation's own corpus and normalisation as an extraction problem. Specifications are proposed from prior events and contracts in the same category, with the differences between them surfaced — which is both a time saving and a quality improvement, since the variation between a company's own specifications for the same category is usually unintentional. Bid responses are normalised by extracting what was actually offered — scope, units, inclusions, exclusions, assumptions, price structure — and restating each on a common basis with the assumptions made explicit, since the assumptions are where comparability actually breaks and where a manual normalisation quietly loses information. Deviations are surfaced rather than flattened: a supplier offering a different structure may be offering something better, and the analysis should say so rather than forcing it into the template. Should-cost and benchmark references come from the platform's cross-customer data, which is the reference a category manager currently lacks and which no individual enterprise can produce.

## Target Customer
Sourcing platform vendors, category management functions at large enterprises, and the sourcing consultancies who perform this assembly as billable work.

## Impact If Built
Days of assembly per event, recovered, in a function whose value is concentrated in the negotiation that the assembly crowds out. The normalisation with explicit assumptions is also a quality improvement rather than only a time saving, because manual normalisation routinely discards the differences that matter and presents a comparison that is tidier than it is true.
