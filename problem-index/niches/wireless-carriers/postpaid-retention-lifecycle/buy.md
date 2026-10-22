# Next-Best-Action Engines Taught Port-Out Signals

**Niche:** [[niches/wireless-carriers/postpaid-retention-lifecycle/profile|Postpaid Phone Retention & Upgrade Lifecycle]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Carriers already license decisioning engines that pick an offer for every interaction, and those engines don't know what a promo-credit end date or a bad sector means.
**Tags:** #gradient-boosting #causal-inference #feature-engineering #data-integration #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche (decisioning platforms, retention analytics vendors and the carriers' own lifecycle teams) is fighting to pick, line by line, the cheapest save offer that actually changes a postpaid customer's decision to port out, and whoever measures save-offer uplift most accurately takes the account.

## The Problem
Next-best-action engines decide what each customer sees in the app, on the bill, in the store and on a care call. They run on generic propensity models and business rules written by marketing, so a carrier-specific risk shows up late, after the customer has already called a competitor.

## What Already Exists
Pega Customer Decision Hub, Salesforce, Adobe and similar decisioning platforms, fed by carrier data warehouses and in-house churn scores.

## The Customization Gap
The adaptation needs carrier-native features and rules. Features include device payment and promo-credit end dates, upgrade eligibility, network experience on the sectors where the customer lives and works, port-out PIN requests and account-change patterns that often precede a switch, and household line structure. Offer rules must encode promotion term versions and eligibility so the engine never offers something billing will reject. Arbitration has to choose by estimated uplift, not by propensity. And measurement must keep holdouts per channel so the engine's lift is known.

## Target Customer
Customer lifecycle and decisioning teams at carriers that already run one of these platforms and want it to reflect wireless realities.

## Impact If Solved
Port-out risk is caught weeks earlier and acted on with offers billing can honour, using an engine the carrier already pays for.
