# Conversion Decided in Someone Else's Codebase

**Niche:** [[niches/bnpl-providers/merchant-checkout-and-placement/profile|Merchant Checkout & Placement]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Conversion depends on where and how the offer appears in a merchant's checkout, every merchant's checkout is different, and the integration is tuned by account managers reading dashboards.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #gradient-boosting #revenue-impact #automation #workflow-orchestration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to make the offer appear at the right moment in a checkout the provider does not control — and whoever does that wins the conversion that decides which provider a merchant keeps.

## The Problem
Whether a consumer chooses to split the payment depends on whether they saw the option on the product page, how the instalment amount was expressed, whether eligibility was indicated before they committed to the basket, where in the payment step it appeared and what it looked like. All of those are decided by the merchant's developer during an integration, typically once, from a documentation example. The provider's conversion at that merchant follows from those choices, the merchant attributes the result to the provider, and the account manager's tool for changing it is a conversation.

## Why Nobody Has Built This
The integration lives in the merchant's code, which makes placement the merchant's decision and therefore outside the provider's product — the boundary of the codebase became the boundary of the responsibility. Experimenting across merchants requires a mechanism the provider does not have. Conversion differences between merchants are attributed to their customers rather than to their placement. And account management is a relationship function without an experimentation capability.

## What to Build
Own the placement even where you do not own the code. Deliver placement through a provider-controlled component that can be varied without a merchant deployment, which is the fix and is what makes everything else possible — placement that requires a merchant release will be set once and never changed. Experiment across merchants, since the provider can run a placement test across thousands of sites simultaneously and no individual merchant ever could, which is the structural advantage here. Learn what works by merchant type, basket value and category, because the answer differs and a single guideline is wrong for most. Show eligibility earlier where possible, since a consumer who knows they can split the payment shops differently and this is one of the largest effects available. Express the instalment amount in the way that converts, which is a messaging question with a testable answer and is currently set by convention. Give the merchant the evidence, since a merchant shown that a placement change adds conversion will make it and the conversation currently has no evidence in it. Diagnose underperforming integrations automatically, so the account manager arrives with a finding rather than a dashboard. Handle the platforms, since many merchants integrate through a commerce platform and the placement is set by that platform's template for all of them at once. Report conversion by placement rather than by merchant, which separates the provider's product from the merchant's implementation. And measure the aggregate conversion uplift of the placement programme, because it is a large number and it is currently nobody's metric.

## Target Customer
Commercial and merchant leadership at instalment providers, the merchants whose conversion depends on a decision they made once, and the commerce platforms whose templates set it for thousands.

## Impact If Built
The boundary of the merchant's codebase became the boundary of the provider's responsibility, so the decision determining conversion is made once from a documentation example. A provider-controlled component that can be varied without a merchant release is what makes cross-merchant experimentation possible at all.
