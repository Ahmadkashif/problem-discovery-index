# Early-Tenure Port-Out Prediction

**Niche:** [[niches/telecom-resellers/independent-digital-mvnos/profile|Independent Digital MVNOs]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An independent MVNO learns that a new subscriber was unprofitable when the port-out notice arrives, though the signs were in the first weeks of network use, care contacts and payment behaviour.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in this sub-niche (MVNE retention modules, lifecycle-messaging platforms and churn-analytics vendors) is fighting to tell, within a new subscriber's first billing cycles, who will port out before repaying their acquisition cost, and whoever predicts and keeps the most of those subscribers takes the account.

## The Problem
New subscribers leave early for reasons the MVNO could see. Coverage is weak at their home or office, data is throttled on a plan they misunderstood, the first port-in took days, a payment failed, or they joined for a promotion and will chase the next one. Acquisition cost is paid on day one and recovered over months, so each early leaver is a loss. Churn models built for big carriers use contract and device-financing features these brands don't have.

## Why Nobody Has Built This
Independent MVNOs are small, and their data is split between the MVNE's BSS, the app analytics tool and the host's usage files. Retention vendors sell engagement scores. They don't use network experience or porting signals, which are the ones that matter on a host network the brand doesn't control.

## What to Build
A time-to-port-out model over the first 120 days of tenure. Its features cover acquisition channel and promotion, port-in experience, coverage quality inferred from usage and dropped sessions at the subscriber's frequent locations, throttling events, care contacts and their topics, payment failures and plan changes. It feeds a few concrete actions: a coverage check-in with Wi-Fi calling set-up, a plan correction, a payment-method nudge, or an honest exit that avoids a chargeback.

## Target Customer
Heads of growth and retention at independent MVNOs, and MVNEs offering retention as a service to their brands.

## Impact If Built
Fewer subscribers leave before payback, and acquisition spend moves toward channels whose subscribers stay. Each avoided early port-out is roughly one acquisition cost saved.
