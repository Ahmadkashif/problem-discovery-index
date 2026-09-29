# Optimising Both Sides of the Wall

**Niche:** [[niches/digital-native-publishers/paywall-and-access-policy/profile|Paywall & Access Policy]]
**Industry:** [[industries/digital-native-publishers|Digital Native Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The paywall is tuned on the readers who converted and knows nothing about the ones who left.
**Tags:** #causal-inference #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #revenue-impact #hypothesis-testing #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to decide who sees what for free, when, and at what price — and whoever measures the readers a paywall turns away as well as the subscribers it converts optimises the whole thing rather than half of it.

## The Problem
A meter set at three articles converts some readers and loses others, and only the conversions are in the report. The readers who hit the wall, left, and never returned are a cost that appears nowhere — they were future subscribers, future newsletter readers, future returning visitors, and they are indistinguishable in the data from people who were never coming back anyway. The same rule is applied to a first-time search visitor and a reader of eight years' standing.

## Why Nobody Has Built This
The conversion metric is the one the subscription platform reports, so the policy is tuned on it — a control optimised against the only available number will always be tightened past the point that is good for the business. The cost of a turned-away reader is diffuse and delayed. Loyal readers hitting a wall is invisible because they do not complain. And access policy is owned by subscriptions, whose metric is conversions.

## What to Build
Make it a per-reader decision measured on both sides. Personalise access by predicted propensity and value rather than applying one meter, which is the core — a reader far from subscribing should be building a habit and a reader close to it should be asked. Measure the turned-away reader explicitly by tracking what happens after a wall encounter, since return behaviour is observable and is the missing half of the metric. Measure subscriber quality by paywall path, because a conversion forced at the wall retains differently from one chosen after months and the difference should determine the policy. Run experiments on meter settings, formats and pricing, as this is one of the easiest experimental surfaces in the business and it is barely used. Value the reader who does not subscribe, since they are advertising inventory, newsletter signups and future subscribers and the paywall currently treats them as nothing. Open the articles that build habits and gate the ones that do not, which connects to the causation work and is where the largest gain sits. Test pricing properly, as it is usually set once by intuition. Handle the search and social visitor differently, since a hard wall on a first visit wastes the acquisition entirely. Report conversions net of estimated reader loss, so the policy has a counterweight. And measure the whole thing on lifetime contribution rather than on conversion rate.

## Target Customer
Subscription and audience leadership, publisher executives, paywall and subscription platform vendors, and readers who hit a wall on their first visit.

## Impact If Built
A control optimised against the only available number is always tightened past the point that helps the business. Tracking what happens after a wall encounter supplies the missing half and turns a uniform rule into a per-reader decision.
