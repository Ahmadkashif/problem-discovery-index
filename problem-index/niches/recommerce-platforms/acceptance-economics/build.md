# The Cost Is Spent Before the Revenue Is Known

**Niche:** [[niches/recommerce-platforms/acceptance-economics/profile|Acceptance Economics]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Intake cost is fixed per item and the revenue is not, so the decision that determines profitability is whether to accept the item at all — and it is made by a category rule.
**Tags:** #gradient-boosting #confidence-intervals #survival-analysis #revenue-impact #evaluation-metrics #convex-optimization #hypothesis-testing #cnns
**Contested on:** Every serious competitor in this niche is fighting to decide which items are worth accepting before the processing cost is spent — and whoever does that fixes the unit economics, because the cost is incurred at intake and the revenue is not.

## The Problem
A bag of thirty items arrives from a seller. Twenty-two are accepted by the category rules, processed at full cost, listed, and stored. Eleven of those eventually sell for less than they cost to process, four never sell at all and are donated or disposed of after months of storage, and the remaining seven carry the whole batch. The platform spent processing cost on fifteen items it should have declined, and it could have predicted most of that from the photograph the seller uploaded before the bag was ever posted. The category rule that let them through knows the brand and the category and nothing about the item.

## Why Nobody Has Built This
Acceptance is treated as a supply acquisition problem rather than as an underwriting decision, and a broad acceptance policy brings in more sellers. Rejecting items is a difficult seller conversation nobody wants to design. The per-item economics are visible only in aggregate, so the loss-making tail is not obvious. And the prediction that would support the decision is built for pricing at intake, which is one step after the point where it would be worth most.

## What to Build
Underwrite the item before accepting it. Predict expected realised value and time-to-sell from the seller's own photographs and description before the item is shipped, which is the same model the pricing work builds applied earlier, and is where its value is greatest — a decision to decline saves the entire processing cost, where a better price saves a margin. Compare that prediction to the fully loaded processing cost including storage and the probability of never selling, and accept only where the expected contribution is positive with a stated confidence. Offer sellers a clear pre-acceptance decision, so they know before posting rather than after, which is a better experience than a rejection on arrival and is the fix's customer-facing half. Handle the marginal items differently rather than binarily: a reduced-processing tier, a direct-to-outlet route, or an offer to the seller rather than a consignment, which turns a decline into an option. Design the rejection so it is cheap and does not damage the relationship, since the seller who is declined well returns with better items. Report the share of accepted items that failed to cover their cost, which is the number this whole build exists to reduce and which nobody currently produces. Feed outcomes back so the acceptance model improves with every item. And measure acceptance policy changes on contribution rather than on volume, since volume is what the current policy optimises.

## Target Customer
Managed platform operations and finance, resale-as-a-service providers, and the sellers who would rather know before posting.

## Impact If Built
The same prediction is worth far more one step earlier, because declining saves the entire processing cost where better pricing saves a margin. Reporting the share of accepted items that failed to cover their cost is the number the sector's unit-economics problem is made of and nobody produces it.
