# Capacity for a Curve Nobody Can Forecast

**Industry:** [[game-hosting-providers|Game Hosting Providers]]
**Type:** High Impact
**One-liner:** Concurrency can multiply within an hour in a specific region, capacity has to be committed in advance, and being wrong costs either a large bill or the most public failure a multiplayer game can have.
**Tags:** #time-series-forecasting #recurrent-forecasting #bayesian-inference #confidence-intervals #convex-optimization #probability-distributions #evaluation-metrics #revenue-impact

## The Problem
Multiplayer demand is spiky, regional and driven by events. A launch produces a curve whose peak nobody knows in advance and whose shape differs by title and region. A seasonal event, a free weekend, a sale, a major patch, a streamer with a large audience playing at a particular hour, or a tournament all produce spikes of different magnitude and duration. Capacity must be in place before the spike, in the right regions, because allocating a server takes seconds and provisioning a fleet does not.

Both failure directions are expensive. Over-provisioning means paying for idle instances across dozens of regions on margins that are already thin, and in a business where compute is the dominant cost that is the difference between profitable and not. Under-provisioning means queues, failed matchmaking, disconnections and a launch that is publicly described as broken — which for a multiplayer title is close to unrecoverable, because the audience that leaves in the first week does not come back and the reputation persists.

Forecasting is done from the studio's own estimate, which is usually a wishlist number multiplied by a conversion assumption, adjusted by whoever has the most launch experience. Regional distribution is estimated from historical patterns of other titles that may not resemble this one. The uncertainty is not quantified, so the safety margin is a judgement rather than a calculation.

The event case is more tractable and equally unmodelled. A studio's own history of events produces a repeatable relationship between event type, promotion and concurrency, and most capacity planning still starts from last time's peak plus a margin.

## Why It's Unsolved
Launch is a single observation. A title launches once, so there is no within-title history to forecast from, and the cross-title relationship between pre-launch signals and realised concurrency has never been assembled — each provider sees its own customers and each studio sees its own game.

The cost asymmetry is severe and is not treated asymmetrically. Under-provisioning at launch is catastrophic and over-provisioning is merely expensive, which means the right answer is a deliberately asymmetric safety margin derived from the ratio of those costs. In practice the margin is a round number chosen by intuition, which is either too large all the time or too small once.

Regional allocation adds a dimension that intuition handles badly. Total capacity can be correct while the distribution is wrong, producing a queue in one region and idle fleets in another, and cross-region play is constrained by latency so the capacity is not fungible.

And the demand signals exist but are scattered. Wishlists and preorders sit with the storefront, streamer schedules are public, regional interest is visible in social and search data, and the provider sees none of it because the studio does not share it and nobody has asked for it in a structured way.

## What a Solution Looks Like
Forecast the launch from the signals that exist, pooled across titles. Wishlist volume and velocity, preorder counts, genre, platform mix, marketing spend, announced streamer participation and regional interest indicators relate to realised concurrency, and that relationship is estimable across many launches even though no single studio has more than a few. A provider hosting many titles is the natural party to build it.

Predict a distribution, not a peak. The capacity decision is a choice under an asymmetric loss function, and the correct input is the full predictive distribution of concurrency by region and hour. With the cost ratio stated explicitly — what a queued player costs versus what an idle instance costs — the provisioning level follows from the distribution rather than from a margin somebody picked.

Model events from the studio's own history. Event type, promotion, reward structure and timing produce a repeatable concurrency response, and that is a straightforward within-title forecasting problem that most teams approach as a lookup of the last comparable event.

Reduce the cost of being wrong. Faster provisioning, multi-region buffering, spot and preemptible capacity with graceful degradation, and a queue that manages expectations rather than failing all shorten the exposure window and change the asymmetry itself — which is often more valuable than a better forecast.

## Impact If Solved
Capacity is the dominant cost in this business and the source of its most damaging failure mode, and it is planned by multiplying a guess by a margin. A cross-title launch forecast with a proper predictive distribution, combined with an explicitly stated cost asymmetry, turns provisioning into a calculation — and the event-level version is achievable immediately from data every studio already has.
