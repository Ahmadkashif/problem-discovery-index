# Fix: The Wait Is Measured to the Second and Paid to Nobody

**Niche:** [[niches/gig-delivery-platforms/merchant-wait-and-handoff/profile|Merchant Wait & Handoff]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The app records geofenced arrival and pickup scan on every delivery, and the minutes between them are compensated only if the courier notices, claims, and qualifies.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance #worker-facing #quick-win #automation
**Contested on:** Whether an existing, precise, automatic measurement will be allowed to trigger an automatic payment.

## The Problem

Wait-time compensation exists at several platforms. It typically requires the courier to be aware of the programme, to notice that the threshold was crossed, to submit a claim through support or an in-app flow, and to fall within caps and conditions that vary by market and are not prominently documented.

Every element of that is unnecessary. The platform measures the wait automatically, to the second, on every pickup. It knows the threshold. It knows the market's rules. The claim adds nothing except attrition, which is its function: claim-based compensation pays the couriers who are informed and persistent, which is a minority, and the accounting works out far cheaper than paying everyone what the measurement says.

The courier standing in the lobby for twenty-two minutes experiences this as the platform knowing exactly what is happening to them and requiring them to ask.

## Why It's Still Broken

Cost. Automatic payment on a measured threshold multiplies the compensation spend by the reciprocal of the claim rate, which is a large multiple. That is the whole of it, and it is worth naming rather than dressing.

The supporting arguments are thin. Attribution — whether the wait was the merchant's fault or the platform's early dispatch — is genuinely relevant to who should *bear* the cost and not at all to whether the courier should be paid for the time. Fraud concerns about couriers sitting in geofences are addressed by the pickup scan and by the order's actual ready timestamp, both of which the platform has. And the operational cost of the claim process itself, in support handling, frequently exceeds the payments it suppresses for small waits.

## What a Fix Looks Like

Pay on the measurement.

Compensate automatically past a short grace period, per minute, at a rate tied to the market's earnings floor, with no claim, no cap and no courier action. The trigger is two timestamps the app already writes. The rules engine already knows the market. This is a settlement rule, and the engineering is days.

Show the clock while it runs. A courier waiting should see the elapsed time and the compensation accruing, live. This is the single most morale-relevant screen the app could have, it makes the policy real rather than theoretical, and it is a timer.

Separate attribution from payment. Pay the courier from the platform, then attribute internally — merchant lateness, dispatch timing, handoff failure — and settle with the merchant on the merchant-attributed share through the commercial relationship. The courier should never be part of that conversation, and today they effectively are, because the attribution argument is what the claim process makes them have.

Cap the exposure at the top of the distribution rather than at the bottom. If the concern is unbounded liability from pathological waits, handle it by releasing the courier from the order with full compensation past a long threshold — which is better for the customer too, since an order that is forty minutes from being ready should be reassigned.

Report it. Total courier-minutes waited, compensated and uncompensated, by market and merchant, monthly. This is the number that tells the platform whether the underlying problem is improving, and no platform currently produces it.

## Who Feels the Pain

Couriers, most acutely the newer ones and those working in their second language, who are least likely to know the compensation exists and least likely to claim. Full-time couriers, for whom accumulated uncompensated waiting is a substantial fraction of a working week. Support agents processing claims that a rule could settle. And customers waiting for orders held up by a system with no incentive to reduce the waiting.

## Impact If Fixed

The industry's largest unpaid time sink gets paid on a measurement that already exists, without anyone having to ask. The cost becomes visible on the platform's own books, which is the precondition for reducing it — an unpaid cost is invisible and therefore permanent. And the courier standing in the lobby watches a number go up instead of watching their hourly rate go down.
