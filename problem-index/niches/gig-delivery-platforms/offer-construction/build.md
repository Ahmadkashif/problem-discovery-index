# Build: An Offer That States What the Work Is Worth

**Niche:** [[niches/gig-delivery-platforms/offer-construction/profile|Offer Construction & the Accept Decision]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Construct the offer around net expected earnings per hour of total engaged time, with the uncertainty shown, instead of a gross amount and a driving estimate.
**Tags:** #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #survival-analysis #feature-engineering #worker-facing #revenue-impact
**Contested on:** Whether the platform will compute and show the number the courier is actually deciding on.

## The Problem

A courier decides in seconds whether to accept work, on a guaranteed amount whose composition is undisclosed, an estimated time that omits waiting, and no statement of what it will actually net after costs. The decision they need to make is whether this job beats the next one at an acceptable rate per hour of their time. The information they are given does not support that decision even approximately.

The gap is not small. A $9 offer estimated at eighteen minutes reads as $30 an hour. If the merchant runs twelve minutes late, the trip covers nine miles round, and vehicle cost is thirty cents a mile, the realised figure is closer to $12 — and which of those two worlds the offer belongs to is predictable from the platform's own data at the moment it is sent.

## Why Nobody Has Built This

Because the current construction works, for the platform. Acceptance rates are optimised against a number that reads better than the reality, and a courier who could see expected net per engaged hour would decline a meaningful share of offers that currently get accepted. That is not an oversight; it is the pricing model functioning as designed.

There is a second reason with more substance. Net earnings depend on the courier's vehicle, fuel efficiency, insurance and tax position, which the platform does not know, and any figure it publishes becomes a representation it has to defend. Publishing a range with clear assumptions handles this, but "we cannot compute it exactly" has served as a reason to compute nothing at all.

And there is a live legal complication: the more precisely a platform models and discloses a worker's realised hourly economics, the more it resembles an employer, which several platforms have been advised weighs against doing it.

## What to Build

An offer whose headline number is expected net earnings per hour of engaged time, with an interval.

The components are all predictable from platform data. Merchant wait by store, hour and current order backlog — the platforms have this to the minute and it is the largest unmodelled term. Total engaged time from acceptance to drop-off completion, including the pickup drive, the wait, the handoff and the parking, rather than the driving segment alone. Vehicle cost from the actual route distance against a courier-configurable per-mile figure, defaulted from vehicle class. Any promotional component with its own conditions. Together these give expected net per engaged hour, which is the quantity the decision turns on.

Show the uncertainty, because it is decision-relevant rather than decorative. An offer that is $22/hour with a tight interval and an offer that is $22/hour with a wide one are different propositions, and the wide ones are systematically the ones that go wrong. Predicting the probability that the offer lands materially below its estimate is straightforward classification over the platform's own historical offers and their realised outcomes, and it is the single most useful thing the platform could add.

Handle the tip complication honestly. Where an offer includes an estimated tip component that can change after delivery, that is a conditional quantity and should be shown as one, with the historical realisation rate for comparable orders. The industry's public controversy on this subject was about exactly this ambiguity, and stating it plainly is cheaper than the next round of it.

Calibrate publicly and continuously. Every offer generates ground truth within the hour — what the delivery actually took and actually paid. Reliability of the estimate against the outcome is measurable per market, per merchant and per hour, and the platform should report it. An estimate nobody has calibrated is a marketing number.

Then let the courier set their own filter. Given a stated minimum net rate, the app declines automatically and stops interrupting them. This is what acceptance-rate-preserving auto-decline should be, and it converts a stream of consequential snap decisions into a policy the courier sets once.

## Target Customer

Platforms in jurisdictions where minimum earnings standards have arrived, for whom the computation is now a compliance requirement rather than an option, and platforms competing for couriers in tight supply markets where earnings transparency is a genuine recruiting differentiator. Also the courier-side tooling market, which already builds weaker versions of this from screen-scraped offers.

## Impact If Built

The courier decides on the number their decision actually depends on. Offers that are systematically worse than they read stop being accepted, which forces the merchant-wait and route economics they conceal back into the platform's own optimisation. And a platform that calibrates and publishes its estimates has an answer when a regulator asks what its couriers actually earn — a question the industry currently cannot answer about itself.
