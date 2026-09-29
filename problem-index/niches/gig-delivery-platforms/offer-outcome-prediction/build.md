# Build: Realised-Outcome Prediction at Offer Time

**Niche:** [[niches/gig-delivery-platforms/offer-outcome-prediction/profile|Offer Outcome Prediction]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict total engaged time, route cost and the probability of a bad outcome for each offer, from telemetry the platform already collects on every delivery.
**Tags:** #gradient-boosting #time-series-forecasting #survival-analysis #confidence-intervals #evaluation-metrics #feature-engineering #automation #worker-facing
**Contested on:** Whether the tail — the deliveries that go badly — can be predicted well enough to warn about in advance.

## The Problem

Delivery outcomes have a long right tail and the tail is where the courier's economics are destroyed. A typical delivery runs close to its estimate; a small share run two or three times over it, and those absorb the margin from a dozen ordinary ones. The distinguishing features are knowable: this merchant at this hour with this backlog runs late, this address has failed handoffs at four times the market rate, this apartment complex takes eleven minutes to navigate, this customer has been unreachable twice before.

The platform holds every one of these facts, at the moment the offer is generated, and uses none of them to warn the person about to accept it. The courier learns the same lessons the expensive way, repeatedly, and cannot share what they learn with anyone.

## Why Nobody Has Built This

The individual predictions exist — platforms forecast merchant readiness and predict ETAs well. What has not been built is the assembly of them into the courier-facing quantity, and that is a product priority question rather than a technical one: dispatch is optimised for the customer's promise and the platform's throughput, and the courier's realised experience is not a metric anyone owns.

The tail prediction specifically is harder and genuinely underinvested. Predicting the mean is easy and predicting the 90th percentile requires modelling the conditions that cause it, which means bringing in features from merchant operations, address history and customer behaviour that live in other systems. The payoff for dispatch is modest, so nobody built it.

And some of the most predictive features are uncomfortable. A per-address failure rate is a claim about a customer. A per-merchant delay distribution is a claim about a business partner. Platforms are cautious about computing things they would then have to decide whether to act on.

## What to Build

A per-offer outcome model producing three quantities and their uncertainty.

**Total engaged time.** Acceptance to drop-off completion, decomposed into drive-to-merchant, merchant wait, drive-to-customer, and handoff. The wait term is the one that is both largest and most neglected, and it is predictable from store, hour, backlog, order composition and the platform's own dispatch lead time. The handoff term matters more than it appears — apartment complexes, office buildings, gated communities and no-parking blocks have stable, learnable costs, and the platform has the GPS traces to learn them.

**Route cost.** Actual driving distance including the return to a viable waiting position, not straight-line or one-way distance, against a per-mile figure the courier can configure by vehicle. This is arithmetic on a routing call the platform already makes.

**Probability of a bad outcome.** Classification over the platform's own history: order not ready on arrival beyond a threshold, order cancelled after acceptance, customer unreachable, address problem, redelivery required. Features from merchant, address, customer history, time and current conditions. The right target is the tail rather than the mean — the useful statement is "one in seven offers like this runs over forty minutes", not an expected value that no individual delivery will match.

Calibrate all three continuously against outcomes that arrive within the hour, which makes this one of the best-instrumented prediction problems in the vault. Report reliability, not just error: when the model says 15%, is it 15%. Publish it per market.

Then use it in two directions. Show it to the courier as part of the offer, with the interval. And feed it back into dispatch, because an offer the model predicts will go badly is one the platform should reprice, route differently or not construct at all — which is the argument that gets this funded.

## Target Customer

Platform dispatch and marketplace engineering, where the internal case is abandoned-delivery reduction and courier retention. Also the courier-side tooling vendors who build this today from scraped offers and crowdsourced outcomes, and who would build a far better version with access to the underlying data — which is a licensing conversation some regional platforms would take.

## Impact If Built

The courier sees the tail risk before accepting rather than after, which is the difference between a bad shift and a bad decision. The platform gets a quantity it can optimise against — predicted courier-realised outcome — which is the missing objective in a system currently optimising only the customer's promise. And the conditions that produce bad deliveries become visible as a cost rather than absorbed silently by whoever accepted the offer.
