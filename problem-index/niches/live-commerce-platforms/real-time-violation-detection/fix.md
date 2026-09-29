# The Model That Cries Wolf at Scissors

**Niche:** [[niches/live-commerce-platforms/real-time-violation-detection/profile|Real-Time Violation Detection]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The weapons classifier fires every time a craft seller picks up scissors, moderators learn to dismiss it, and the one real case arrives into a queue nobody trusts.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #descriptive-statistics #quick-win #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to catch a violation while it is still airing rather than after it has been broadcast — and whoever closes that gap defines what the platform can safely allow to go live.

## The Problem
A craft seller holds up shears. A kitchenware seller shows a knife set. A collectibles seller displays a replica prop. The weapons classifier fires on all of them, dozens of times a night, and a moderator dismisses every one. Within a week the team treats that flag class as noise. The classifier is not broken — it is doing exactly what it was trained to do on a distribution that does not include commerce. The consequence is not the wasted clicks; it is that the flag has been rendered meaningless, so when a real case fires it is dismissed with the others.

## Why It's Still Broken
Thresholds are set globally on a generic taxonomy and never conditioned on the category the seller is in. False positive rates are measured in aggregate, where a flag class that is ninety-eight percent noise is invisible behind overall precision. Nobody owns per-class health. And moderator dismissals are recorded as actions rather than treated as labels, so the loop that would fix it is open.

## What a Fix Looks Like
Treat flag credibility as the thing being managed. Report precision per flag class per category, which is a single query and almost always reveals two or three classes doing all the damage — this is the diagnostic and it needs no modelling. Condition thresholds on seller category and history, since a knife in a kitchenware stream and a knife in an unclassified stream are not the same event and treating them identically is the root cause. Use the moderator's dismissal as a label and retrain on it, which closes the loop and is the mechanism by which the problem stops recurring. Suppress flag classes whose precision falls below a stated floor, and say so openly, rather than continuing to emit them and relying on humans to absorb the noise. Require corroboration for low-precision classes — an object detection plus a spoken cue plus a chat reaction — which raises precision sharply at a small latency cost. Show the moderator why it fired, since a flag with no evidence cannot be evaluated and is dismissed by default. Track dismissal rate per class as an operational health metric with an alert, so degradation is caught rather than absorbed. Separate high-harm classes and hold them to different rules, because suppressing a noisy low-harm class is prudent and suppressing a noisy high-harm one is not. And audit for the case this all exists to prevent: a real violation dismissed because its flag class had been discredited.

## Who Feels the Pain
Moderators trained by experience to ignore the system; sellers repeatedly flagged for their ordinary merchandise; and platforms whose real detections arrive in a queue nobody believes.

## Impact If Fixed
The damage is not the wasted clicks but a flag class rendered meaningless, so the real case is dismissed with the noise. Per-class precision by category is a single query, and conditioning thresholds on seller category addresses the root cause directly.
