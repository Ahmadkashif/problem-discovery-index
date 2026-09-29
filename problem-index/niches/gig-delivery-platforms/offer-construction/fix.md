# Fix: The Estimate That Omits the Waiting

**Niche:** [[niches/gig-delivery-platforms/offer-construction/profile|Offer Construction & the Accept Decision]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The time estimate on an offer covers the driving and excludes the twenty minutes in the restaurant lobby, which is the part that determines whether the job was worth taking.
**Tags:** #time-series-forecasting #descriptive-statistics #confidence-intervals #evaluation-metrics #change-point-detection #worker-facing #quick-win #automation
**Contested on:** Whether the platform will add to the estimate the one component it measures most precisely.

## The Problem

An offer says eighteen minutes. The courier drives seven minutes to the merchant, waits twenty-two in a lobby for an order promised before they arrived, drives nine minutes to the customer, and parks. Forty-one minutes, of which the estimate anticipated eighteen.

The wait is not unpredictable. The platform knows, for that merchant, at that hour, with that current order backlog, what the wait distribution looks like — it has millions of observations of exactly this, because it timestamps courier arrival and order pickup on every delivery. It uses that data to decide when to dispatch. It does not put it in the estimate the courier sees.

The consequence is that the offers with the worst realised economics are the ones whose estimates are most optimistic, because a long merchant wait raises total time without raising pay. The courier's accept decision is systematically biased against them in exactly the cases that matter.

## Why It's Still Broken

Because the estimate's function is to get the offer accepted, and adding twenty minutes to it reduces acceptance. That is the honest answer and it accounts for most of the persistence.

There are contributing reasons that are real but not sufficient. The wait prediction sits in the dispatch and merchant-operations systems, and the offer is constructed by the pay model team; the join between them is an organisational one that nobody's roadmap owns. And there is a stated concern about setting merchant expectations — a platform displaying "this restaurant typically runs eighteen minutes late" to couriers is making a claim about a business partner, which the merchant team will resist.

That concern is about disclosure of a merchant-attributed number, though, not about the estimate itself. Nothing prevents the total time estimate from simply being correct without naming why.

## What a Fix Looks Like

Put the expected wait into the estimate. It is one term, from data the platform already computes.

Predict merchant wait at offer time from store, hour, day, current backlog at that store, order size and the platform's own dispatch timing — a routine forecasting problem with abundant labels, and one most platforms already solve internally for dispatch. Add it to the driving estimate so the displayed number is total engaged time. The offer need say nothing about the merchant; it just has to stop being wrong.

Show the variance where it is high. A merchant whose wait is reliably four minutes and one whose wait ranges from two to thirty-five are different propositions, and a range on the estimate is more honest than a point that will be wrong either way.

Pay for waiting beyond a threshold, automatically. Several platforms have some version of this and it is typically opt-in, manually claimed, or capped in ways that defeat it. Wait time is measured to the second by the app itself — geofenced arrival to pickup scan — so automatic compensation past a threshold requires no new data and no courier action. It also puts the cost of merchant lateness on the party that can influence it, which is the only way that lateness ever improves.

Report calibration back to the courier and the merchant both. Estimated versus realised total time, per offer, aggregated weekly. A courier who can see that their market's estimates run twelve minutes short knows how to adjust; a merchant who can see their wait distribution against the market's has something to act on.

Retrospectively, tell the courier what happened. After the delivery, the app knows exactly how long it took and what it netted. Showing the realised rate against the estimated one, per delivery, costs nothing and is the feedback that lets someone learn which offers to decline.

## Who Feels the Pain

Couriers, who absorb every minute of merchant lateness unpaid and who make accept decisions on an estimate that is biased in a known direction. Full-time couriers most of all, for whom the accumulated unpaid waiting across a week is a substantial fraction of their working hours. And the platform, which is quietly funding its delivery promise out of the courier's unpaid time and does not carry the cost anywhere it can see.

## Impact If Fixed

The estimate becomes correct, which is a low bar the category currently does not clear. Merchant lateness stops being free to everyone except the person standing in the lobby, which is the only mechanism by which it will ever be reduced. And couriers making a hundred accept decisions a week make them on a number that means what it says.
