# Fix: The Batch That Helps Everyone Except the Person Driving It

**Niche:** [[niches/gig-delivery-platforms/dispatch-and-batching/profile|Dispatch, Routing & Batching]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Batched orders and merchant wait times are optimised for platform throughput and customer promise, and the courier absorbs the cost of every miscalculation.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #gradient-boosting #worker-facing #quick-win #automation
**Contested on:** Whether the platform will count what a batch costs the courier when it decides whether to create one.

## The Problem

Two orders get combined. The platform's metrics improve: one courier trip instead of two, higher utilisation, lower cost per delivery, and if the timing works, both customers served acceptably.

The courier's experience is different. Two merchant waits instead of one. A route that serves both customers but is longer than either alone. Two handoffs, two buildings, two parking searches. Pay that under most pay models rises less than proportionally, because the second order's distance component is computed on an incremental basis. And if either merchant runs late, both deliveries are late, both customers are unhappy, and the ratings land on the courier.

The batch was a good decision by every number the system computes. Whether it was a good hour for the person driving it is not computed at all.

## Why It's Still Broken

Batching is measured by batch rate, delivery time impact and cost per delivery, all of which improve. There is no metric for what a batch does to the courier's realised rate, so there is nothing to trade against and no way for the question to enter a review.

The courier's ability to self-protect is also weaker than it appears. Declining batches is possible, but acceptance rate influences future offer quality on several platforms, and the courier cannot evaluate a batch quickly — the screen shows two merchants and two destinations and a combined amount, with no comparison to what the orders would have paid separately.

And there is an accounting subtlety that lets the harm hide. Batched deliveries usually do raise a courier's earnings per hour of *active driving*, because the alternative includes idle time between orders. They frequently lower earnings per hour of *engaged time* including waiting. Which of those two rates a platform quotes determines whether batching looks good or bad, and platforms quote the first.

## What a Fix Looks Like

Count the cost, then price it. Most of the first step is arithmetic on data already recorded.

Measure realised courier outcome on batched versus unbatched deliveries, in comparable conditions, per market. Engaged time, net pay, pay per engaged hour, and the rating consequence of late deliveries caused by the other order in the batch. This is a comparison the platform can run today over its own history, and its absence is why the question has never been settled internally.

Report batching's effect distributionally. Some batches are genuinely good for the courier — two orders from the same merchant to the same building is strictly better work. Others are bad. Aggregate reporting hides both. The useful output is the share of batches that improve and degrade courier outcome, with the features that distinguish them, which then tells the batching model what to stop doing.

Price the second order properly. Where a batch adds a merchant wait and a separate handoff, the pay model should reflect it, because the current incremental-distance treatment prices the second order as though it were a detour rather than a second job. This is the change that makes batching acceptable rather than merely measured.

Show the comparison on the offer. What the batch pays and what the orders would have paid separately, with the combined time estimate including both waits. A courier can then decide in the seconds available, which is currently impossible.

And stop counting acceptance rate against declined batches, or state clearly that it does not. If a courier cannot decline a batch without consequence, the accept decision is not one.

## Who Feels the Pain

Couriers, who absorb the coordination cost of every batch and the rating consequence when one order makes the other late. Customers whose order was the second in a batch and arrived cold. Merchants blamed for delays caused by a courier waiting at a different restaurant. And the platform, whose batch rate metric is improving against a cost it has chosen not to measure.

## Impact If Fixed

Batching gets evaluated on all of its consequences rather than the subset that flatters it, and the batches that are bad for everyone except the throughput metric stop being created. The second order gets priced as a second job. And the courier gets the one comparison they need — batched versus separate — at the moment they have to choose.
