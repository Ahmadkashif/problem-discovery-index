# The Redesign That Slowly Reverted

**Niche:** [[niches/product-design-studios/design-system-durability/profile|Design System Durability]]
**Industry:** [[industries/product-design-studios|Product Design Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Eighteen months after launch the product looks like it did before, one reasonable exception at a time.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #automation #workflow-orchestration #compliance #data-integration #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to deliver a design system that does not begin drifting from the client's production code the week the studio leaves — and whoever makes it durable takes the account.

## The Problem
Nobody reverts a redesign deliberately. It happens one exception at a time: a team ships a page that does not use the system because the deadline was tight, a component is copied and modified, a new feature invents its own pattern. Each decision is defensible. Eighteen months later the product is inconsistent again, the client concludes the redesign did not hold, and the studio — which has not seen the product since handover — is judged accordingly.

## Why It's Still Broken
Nobody counts the exceptions — a system eroded by individually reasonable decisions has no moment at which anyone notices, because the erosion is only visible in aggregate and nothing aggregates it. There is no owner after handover. Each exception is small. And the reversion is discovered when it is complete.

## What a Fix Looks Like
Count the exceptions and give them an owner. Measure what share of the live product uses the system, reported on a schedule, which is the fix and turns invisible erosion into a visible trend. Name an owner on the client side before the studio leaves, since the absence of one is the root cause. Record every deliberate exception with its reason, which converts erosion into a backlog. Review the exceptions periodically to absorb the good ones into the system, as a system that never changes is one people route around. Make using the system easier than not using it, which is the only durable enforcement. Report the trend to the person who commissioned the work, because they care and currently never hear. Check the system's coverage against the product's new surfaces, which is where most exceptions originate. Offer a light check-in at three and twelve months, which is cheap and frequently becomes a follow-on engagement. Flag components that have diverged in code rather than waiting for a redesign to discover it. And treat coverage as the measure of the system's success rather than its completeness at delivery.

## Who Feels the Pain
Clients whose redesign did not hold; studios judged on a decay they did not see; developers making reasonable local decisions with no visibility of the aggregate; and the next redesign, which starts from the same place.

## Impact If Fixed
A system eroded by individually reasonable decisions has no moment at which anyone notices, because the erosion is only visible in aggregate and nothing aggregates it. A scheduled coverage number with an owner makes it a trend somebody manages.
