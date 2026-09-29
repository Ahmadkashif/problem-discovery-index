# The Baseline Feature That Does Not Work

**Niche:** [[niches/dropshipping-suppliers/catalogue-and-stock-sync/profile|Catalogue & Stock Synchronisation]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Catalogue import and stock sync are the baseline feature of every platform in the category, and merchants still oversell items their supplier stopped carrying weeks ago.
**Tags:** #data-integration #workflow-orchestration #automation #evaluation-metrics #change-point-detection #revenue-impact #confidence-intervals #compliance
**Contested on:** This niche is not terminal — knowing whether the item still exists and making the listing worth buying are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Every platform in the category lists catalogue import and inventory synchronisation as a core capability, and every merchant in the category has sold something that was not there. The feed is polled on a schedule, the schedule is a compromise, the supplier's own stock system is approximate, the mapping between their identifiers and the storefront's drifts, and discontinuations arrive as an absence rather than as an event. The merchant discovers all of this from a customer. The feature is present, widely marketed, and does not deliver the guarantee its name implies.

## Why Nobody Has Built This
Integration was built to be broad rather than reliable, because the competitive pressure was on how many suppliers and storefronts were supported. Polling is cheap and its failures are diffuse. Suppliers have no obligation to publish changes and no incentive to publish discontinuations. And the cost of an oversell lands on the merchant and their customer, never on the platform, which removes the pressure that would otherwise fix it.

## What to Build
Rebuild synchronisation around correctness rather than coverage. Treat stock as a probabilistic statement with an age and a confidence rather than as a number, which is the honest representation and the foundation for every decision downstream — the current model asserts certainty the data has never supported. Poll adaptively by volatility and by sales velocity, since a fast-moving item needs minutes and a slow one needs a day, and a single global schedule is wrong for both. Detect a discontinuation as an event, because it arrives as a silent absence from a feed and is the single most damaging change type. Reconcile disagreements between the supplier's feed, the order outcomes and the merchant's storefront, which is where the real drift lives and which no platform does. Feed order rejections back into stock state immediately, as a failed fulfilment is the strongest possible evidence that something is gone. Handle variants and substitutions explicitly, since suppliers change pack sizes and components without changing identifiers. Give merchants a stated confidence per listing so they can decide what to advertise against, which turns an invisible risk into a managed one. Gate high-spend advertising on stock confidence, which is the mechanism that stops the most expensive failures. And publish oversell rate as a platform metric, because the feature has never been measured against the outcome it exists to prevent.

## Target Customer
Dropshipping platforms, sourcing marketplaces, merchants carrying oversell risk, and the storefront platforms absorbing the customer complaints.

## Impact If Built
The feature is universal, marketed, and does not deliver the guarantee its name implies, because the cost lands on the merchant rather than the platform. Treating stock as a statement with an age and confidence is the honest model, and it is what lets advertising spend be gated on it.
