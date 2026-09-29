# Platforms Built Without Knowing What Developers Do

**Industry:** [[internal-developer-platforms|Internal Developer Platforms]]
**Type:** High Impact
**One-liner:** Platform teams build paved paths, developers route around them, and nobody measures where the abandonment happens — because the team thinks it is building infrastructure rather than a product with users.
**Tags:** #gradient-boosting #survival-analysis #k-means-clustering #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #workflow-orchestration

## The Problem
The pattern repeats across the industry. A platform team is formed, surveys a few friendly teams, and builds paved paths: a service template, a deployment pipeline, a standard observability setup, a portal.

Adoption stalls. Some teams use it, usually those consulted during design. Others use part of it and drop out at a specific point. Others build their own. The platform team knows adoption is disappointing and does not know why, so they build more features, which is the response available to them.

The information that would explain it is entirely obtainable. Which developers opened the portal and what they did next. Where in the golden path they stopped and what they did instead. Which template steps produce a support request. How long it actually takes to get a new service to production, and where that time goes. Which platform capabilities are used once and never again.

A consumer product team would consider these table stakes. Platform teams collect almost none of them, because measuring your colleagues feels like surveillance and because the team's self-conception is infrastructure rather than product.

The consequence is a platform shaped by the assumptions of the people who built it, which is exactly the failure mode product measurement exists to prevent.

## Why It's Unsolved
The category error is the root cause. Infrastructure is measured by uptime and capacity; a product is measured by whether people use it and why they stop. Platform teams are staffed with infrastructure engineers who have not been asked to think in the second frame, and the tooling they buy reflects that.

Measuring developers is genuinely uncomfortable. Any instrumentation of engineering activity can become a performance surveillance tool, engineers are rightly alert to that, and a platform team that got it wrong would destroy the trust its adoption depends on. That is a real constraint and it rules out individual-level measurement entirely.

Adoption is also hard to attribute. A team using the platform may do so because it is genuinely better or because it was mandated, and those are very different outcomes that look identical in a usage chart.

And there is no counterfactual. Whether the platform made engineering faster requires comparing against not having it, and platform teams rarely stage rollouts in a way that would permit the comparison.

## What a Solution Looks Like
Product analytics for the platform, aggregated at team level and never at individual level, with that boundary architectural rather than promised. Activation, funnel completion, feature retention and time-to-first-deployment are the metrics, and they are the same ones any product team would use.

Drop-off analysis on the golden path specifically, since a path that developers abandon at step four is telling you precisely what to fix, and the abandonment is invisible today.

Route-around detection. Teams that built their own deployment pipeline, their own observability configuration, or their own service template are the most informative users the platform has, and identifying them from infrastructure and repository signals is straightforward.

Time-to-production as the headline outcome, measured end to end from repository creation to serving traffic, decomposed into the steps that consume it.

And staged rollouts designed to permit comparison, so the platform's effect on delivery outcomes is estimable rather than asserted — which is also the only way a platform team ever defends its headcount with evidence.

## Impact If Solved
Internal platforms fail at a rate the industry openly acknowledges, and the cause is consistently that they were built without knowing what developers actually do. Product measurement is the correction, it requires instrumentation nobody has to invent, and the team-level boundary is what makes it acceptable to the engineers being measured.
