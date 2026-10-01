# The Stop-Loss That Cannot Tell Bad Luck From Lost Edge

**Niche:** [[niches/hedge-funds/multi-manager-pod-platforms/profile|Multi-Manager Pod Platforms]]
**Industry:** [[industries/hedge-funds|Hedge Funds]]
**Type:** Fix (Pain Point)
**One-liner:** A fixed drawdown limit cuts a pod's capital the same way whether its PM was unlucky or has stopped being right.
**Tags:** #change-point-detection #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to separate a pod's skill from its factor and crowding exposure fast enough to move capital before the drawdown — and whoever measures pod skill first decides how the platform's risk budget is allocated.

## The Problem
Platforms enforce drawdown rules — commonly a cut to capital at one threshold and termination at a second — because they are simple, credible to investors and prevent catastrophe. They also treat every drawdown identically. A PM whose stock picks are still working but who was hit by a factor rotation and a PM whose hit rate has collapsed receive the same treatment. The platform loses good PMs to noise and keeps funding some bad ones until the threshold is reached.

## Why It's Still Broken
Drawdown limits are a contractual and cultural foundation of the model; replacing them looks like loosening risk control. Diagnostic analysis that could distinguish the two cases is not delivered at the speed decisions are made.

## What a Fix Looks Like
Keep the hard limits, and run a change-point diagnostic alongside them: has the PM's decision-level hit rate or sizing informativeness shifted, or is the drawdown explained by factor and crowding exposure? Surface the diagnostic to the allocation committee before the threshold binds, with an interval on the estimate, so a capital decision near the line is informed rather than mechanical.

## Who Feels the Pain
PMs cut for factor moves they did not cause; analysts in those pods who lose their jobs with them; and platforms that replace skilled teams at high recruiting cost.

## Impact If Fixed
Fewer skilled pods lost to noise and earlier action on genuine edge decay, without weakening the risk discipline investors rely on.
