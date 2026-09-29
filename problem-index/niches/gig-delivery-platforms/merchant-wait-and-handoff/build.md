# Build: Wait Attribution, Automatic Compensation and Merchant Feedback

**Niche:** [[niches/gig-delivery-platforms/merchant-wait-and-handoff/profile|Merchant Wait & Handoff]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Attribute every minute of courier waiting to its cause, pay for it automatically, and report each merchant's wait distribution against its peers.
**Tags:** #time-series-forecasting #gradient-boosting #causal-inference #evaluation-metrics #confidence-intervals #descriptive-statistics #worker-facing #automation
**Contested on:** Whether a wait can be attributed between the merchant, the platform's dispatch timing and the courier's own arrival reliably enough to pay on it.

## The Problem

Courier waiting is measured precisely and acted on by nobody. The platform records geofenced arrival and pickup scan on every delivery, which gives it a wait duration per pickup, per merchant, per hour, across years — probably the largest dataset on restaurant fulfilment timing in existence.

It uses that data to time dispatch, which reduces platform-side cost, and does not use it to compensate the courier, to inform the offer, or to tell the merchant how they compare. So a merchant that runs fifteen minutes late every Friday evening imposes that cost on a different courier each time, none of whom can do anything about it, and never learns that they do.

## Why Nobody Has Built This

Attribution is the stated obstacle and it has some substance. A courier who arrives eight minutes before the order was ever going to be ready has waited eight minutes, and whether that is the merchant's lateness or the platform's early dispatch depends on what readiness was promised and when the dispatch was made. Without attribution, paying for all waiting means paying for the platform's own dispatch timing errors, which is expensive and rewards nothing.

But the attribution is entirely computable — promised ready time, actual ready time, dispatch time and arrival time are four timestamps the platform holds — and the difficulty has functioned as a reason not to start.

The real obstacle is that merchants are the customer. Reporting a merchant's wait performance, or charging them for it, is a commercial action against the party paying commission, in a competitive market where merchants can list on a rival. Platforms have consistently chosen merchant acquisition over courier cost, and the courier's unpaid time is what funds that choice.

## What to Build

An attribution and settlement layer over the timestamps that already exist.

**Attribute the wait.** Decompose each wait into: courier arrived before promised ready time (platform dispatch timing), order not ready at promised time (merchant), order ready but handoff delayed (merchant operations or courier). The four timestamps give this directly, with modelling needed only to establish what the promised readiness should have been for the order's composition — which is the merchant's own prep-time model, calibrated against their actual history rather than their stated times.

**Pay automatically on the merchant-attributed portion** past a short grace threshold, without a claim, at a per-minute rate tied to the market's earnings floor. No courier action, no support ticket, no cap. This is a settlement rule over an attributed measurement and requires no new data whatsoever.

**Report to the merchant.** Wait distribution by daypart against anonymised peers in their category and market, with the cost attributed — this many courier-minutes, this much in compensation, this much in delayed deliveries and the resulting customer rating impact. Merchants overwhelmingly do not know their own lateness distribution, because they experience each late order individually and never see the aggregate. This report alone changes behaviour at a meaningful share of merchants, and it is a dashboard over existing data.

**Predict readiness properly and feed it to dispatch and to the offer.** Per merchant, per hour, by order composition and current backlog, as a distribution rather than a point. Dispatch already consumes a version of this; the offer does not, and the estimate is wrong because of it.

**Then price it.** A merchant whose wait cost exceeds a threshold should face it — a commission adjustment, a placement consequence, or at minimum a required prep-time correction. This is the step platforms avoid and it is the only one that makes the rest self-sustaining, because measurement and reporting without consequence decays.

## Target Customer

Platform merchant operations, where the internal case is delivery-time improvement and courier retention, and the external case is the wait-time compensation requirements appearing in jurisdictional earnings standards. The merchant-facing benchmark report is also a genuinely wanted product — operators ask for it — which makes it the easiest piece to fund.

## Impact If Built

The industry's largest pool of unpaid working time gets attributed and settled automatically. Merchants find out how they compare and a meaningful share improve, which reduces the underlying cost rather than redistributing it. And the readiness prediction that makes offers honest gets built as a by-product of the attribution.
