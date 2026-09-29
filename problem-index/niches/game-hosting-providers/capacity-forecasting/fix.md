# The Studio's Estimate Everyone Knew Was Wrong

**Niche:** [[niches/game-hosting-providers/capacity-forecasting/profile|Capacity Forecasting & Allocation]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The capacity plan was built on a concurrency number the studio supplied, the provider doubted it, and nobody wrote the doubt down.
**Tags:** #quick-win #descriptive-statistics #confidence-intervals #evaluation-metrics #time-series-forecasting #revenue-impact #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to commit capacity in specific regions hours before a demand curve that can multiply within an hour, where being wrong costs either a large bill or the most public failure a multiplayer game can have — and whoever forecasts it takes the account.

## The Problem
Capacity planning for a launch usually begins with a concurrency estimate from the studio. The studio's estimate reflects hope, marketing's projections and no forecasting method. The provider's engineers often believe it is wrong — in either direction — and have no mechanism for saying so that survives the meeting. Capacity is committed against it. When the launch goes badly, the post-mortem discovers that several people had private doubts and none were recorded.

## Why It's Still Broken
The estimate arrives as a fact rather than as a forecast — a number supplied without a range or a method cannot be challenged, only accepted or disbelieved, and there is no process for the second. The provider does not want to contradict the customer. Nobody tracks estimate accuracy across launches. And the asymmetry of the two failure modes is never stated.

## What a Fix Looks Like
Ask for a range and keep the record. Require the estimate as a range with stated assumptions rather than a single number, which is the fix and immediately changes what the planning conversation is about. Supply the provider's own comparable-title view alongside it, since the provider has seen dozens of launches and the studio has seen one. Record both estimates and the eventual actual, as the accuracy history across launches is the asset that ends this argument permanently. State the asymmetry explicitly in the plan, because everyone weighs the two errors differently until it is written down. Plan the pre-warm against the upper end and the steady state against the middle, which is the standard remedy and is often not applied. Agree a rapid-scale trigger and who may pull it before the day, which is what turns a shortfall into a delay rather than a failure. Write down the dissent when engineers disagree, which is the cheapest institutional improvement available. Review the estimate against live signals in the final days, since wishlist and preorder movement is informative. Share the accuracy record with the studio, which improves the next estimate more than any argument. And treat the estimate as the provider's forecast rather than as the studio's instruction.

## Who Feels the Pain
Providers absorbing the blame for a shortfall they predicted; studios with a failed launch; engineers whose doubts were never recorded; and the finance function holding an overprovisioned bill.

## Impact If Fixed
A number supplied without a range or a method cannot be challenged, only accepted or disbelieved, and there is no process for the second. Requiring a range and recording both estimates against the actual builds the accuracy history that settles it.
