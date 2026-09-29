# Bidding Against an Outcome Nobody Returns

**Industry:** [[programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** High Impact
**One-liner:** The bid is priced in ten milliseconds against a click, because the sale it was supposed to cause is observed by the advertiser a month later and never joined back to the impression.
**Tags:** #survival-analysis #causal-inference #gradient-boosting #bayesian-inference #evaluation-metrics #confidence-intervals #data-integration #revenue-impact

## The Problem
A demand-side platform receives a bid request, has roughly ten milliseconds to decide what the impression is worth, and prices it using a model that predicts the probability of a click or a post-click visit. Both are observable within seconds, which is why they are the label. The thing the advertiser is actually buying — an incremental sale, a subscription, a lifetime-value cohort — is observed inside the advertiser's own systems, days or weeks later, and comes back to the platform as a conversion pixel fire with whatever identity survived the journey, or as a weekly aggregate from a mobile measurement partner, or as a quarterly brand lift study, or not at all.

The consequences compound. Conversions are censored: a campaign running for two weeks has not yet seen most of the purchases it caused, so models trained on observed conversions systematically undervalue slow-converting inventory and overvalue whatever converts fast, which is usually retargeting the buyer would have got for free. Identity loss means the conversions that do return match to only a fraction of impressions, and the matched fraction is not random — it skews to logged-in, desktop, cookie-accepting users. And nothing in the loop distinguishes a conversion the ad caused from one that would have happened anyway, so the optimiser's most reliable strategy is to find people already about to buy.

Everyone in the chain knows this. Advertisers respond by demanding incrementality tests they run annually at best; platforms respond by publishing attributed ROAS figures they know are inflated; the ANA and large advertisers periodically commission studies that say so out loud. The market clears anyway, because there is no better number available at bid time.

## Why It's Unsolved
The data sits on two sides of a company boundary and the incentives point away from joining it. The platform cannot see the advertiser's CRM; the advertiser will not hand over customer-level purchase data to a vendor that also sells to their competitors, and increasingly cannot under GDPR, CPRA and their own privacy commitments. Clean rooms were built for exactly this and are used almost entirely for retrospective measurement — they answer questions in hours, not in the ten milliseconds a bid needs.

The technical problem underneath is genuinely hard and not just political. Delayed feedback with heavy right-censoring breaks ordinary supervised training; the conversion delay distribution differs by advertiser, product price and channel; and the causal question — would this person have bought anyway — cannot be answered from observational bid logs at all, because the platform chose who to show the ad to based on exactly the signals that predict purchase. Randomised holdouts answer it, but they cost money that someone has to agree not to spend, and at the granularity a bid model needs there is never enough holdout power.

There is also an uncomfortable equilibrium. A platform that switched from attributed conversions to incremental ones would report dramatically lower numbers than its competitors for the same real performance. The first mover is punished by its own honesty, which is why the category has spent fifteen years discussing it and shipping proxies.

## What a Solution Looks Like
Model the delay explicitly rather than pretending it away. A survival model over time-to-conversion, fit per advertiser vertical and price point, turns a censored observation into a calibrated expectation — an impression seven days old with no conversion carries information, and how much depends on how long conversions normally take for that product. Bid values become expected outcome under the delay distribution rather than observed-so-far counts, which stops the systematic bias against considered purchases.

Treat identity loss as a measurement model, not a matching failure. The matched fraction is observable and its skew is characterisable; a platform that estimates conversion rate on the matched population and corrects for the selection into that population gets a better number than one that quietly reports matched-only performance as if it were the whole.

Build incrementality into the bidder rather than beside it. Continuous, cheap, small-scale randomised holdouts — a percentage of eligible auctions withheld by design, rotating across segments — produce a stream of unbiased causal estimates that can be pooled hierarchically to give segment-level incrementality with honest intervals. That is not a study; it is a permanent instrument, and it is the only way to learn which inventory does anything.

Then make the join possible without moving the data. Federated or clean-room-resident training, where the advertiser's outcome labels never leave their environment and only gradients or aggregate sufficient statistics return, is the shape that survives both the legal and the commercial objection. It is slower than a pixel and it is the only version an advertiser will actually sign.

## Impact If Solved
This is the number the entire $150B flow is priced against. A bid valuation that reflects expected incremental outcome rather than observed early clicks reallocates spend away from inventory that converts people who had already decided, which is where a large and unmeasured share of programmatic budget currently goes. For a platform, it is the only durable differentiation left in a category where auction mechanics and supply access have converged — and the one that would let it survive the next identity shock, because a model that already treats identity as partial and outcomes as censored does not break when the cookie does.
