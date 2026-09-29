# A Policy Category and Nothing Else

**Niche:** [[niches/ugc-video-platforms/enforcement-and-governance/profile|Enforcement & Governance]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The notification names a policy the creator has read and does not say which forty seconds of their video breached it.
**Tags:** #compliance #quick-win #worker-facing #evaluation-metrics #automation #workflow-orchestration #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make an automated decision that changes someone's income explainable and contestable — and the contest splits cleanly enough that it is not terminal.

## The Problem
The creator receives a notice citing a policy category. Their video is twenty minutes long. They do not know whether the issue was a word, an image, a claim, a thumbnail, a title or something in a comment. They cannot correct it, cannot avoid it next time, and cannot appeal usefully because they do not know what they are appealing about. They re-upload with random changes, get the same result, and conclude the system is arbitrary — which, from where they are standing, is accurate.

## Why It's Still Broken
The notification was designed as a policy citation because that is what the compliance requirement was read to need, so the detail the system computed is discarded at the boundary — a notice built to record that a rule was applied does not carry what triggered it. Specificity is feared as adversarial guidance. Nobody measured re-upload and repeat-violation rates. And the creator has no route to insist.

## What a Fix Looks Like
Say where. Give the timestamp or element that triggered the decision, which is the fix and is information the classifier produced and discarded. State whether the decision was automated or reviewed, since the creator currently cannot tell and it changes what an appeal means. Say what would resolve it where that is knowable, because an enforcement with no remedy is a penalty rather than a correction. Report the confidence, as a marginal decision and a clear one are presented identically today. Distinguish removal, demonetisation and distribution reduction explicitly, since creators conflate them and the remedies differ. Show the creator their enforcement history in one place, which is currently scattered across notifications. Measure re-uploads and repeat violations after an enforcement, as a high rate is direct evidence that the notice taught nothing. Calibrate detail by risk category rather than withholding everywhere, since the adversarial argument applies to a minority of categories. Let the creator ask one clarifying question, which resolves many cases at low cost. And publish what the notices contain, because the current opacity is itself the reputational problem.

## Who Feels the Pain
Creators penalised without knowing why; partner managers who cannot explain it either; appeal reviewers receiving appeals that address nothing; and platforms whose enforcement is experienced as arbitrary regardless of its accuracy.

## Impact If Fixed
A notice built to record that a rule was applied does not carry what triggered it, though the classifier computed it. Giving the timestamp and stating whether a human reviewed it costs nothing and turns an arbitrary penalty into a correctable one.
