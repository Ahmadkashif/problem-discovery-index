# The Detail the Classifier Already Has

**Niche:** [[niches/ugc-video-platforms/decision-explanation/profile|Decision Explanation]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The internal record contains the segment, the score and the model that fired, and the creator's notification contains a policy name.
**Tags:** #quick-win #compliance #evaluation-metrics #confidence-intervals #automation #worker-facing #workflow-orchestration #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to make a classifier state which passage of a video triggered its decision and how confident it was — and whoever does it turns an unaccountable determination into one a person can act on.

## The Problem
The enforcement record inside the platform is far richer than the notification sent out. It contains the model, the segment, the score, the threshold and often the reviewer's disposition. None of it reaches the creator, and much of it does not reach the appeal reviewer either, who frequently re-decides the case with no more information than the creator has. The gap is a boundary decision rather than a data gap.

## Why It's Still Broken
The notification schema was defined once for a policy notice, so anything not in that schema is dropped at the boundary — a message format designed to state an outcome cannot carry a rationale that was never part of it. Widening it was never prioritised. The adversarial concern is applied uniformly rather than by category. And nobody asked what the appeal reviewer sees.

## What a Fix Looks Like
Widen the boundary, starting internally. Give the appeal reviewer the full internal record, which is the fix's cheapest and most consequential step and requires no external disclosure at all. Add the timestamp and the modality to the creator notification, since those are the two most useful facts and are the least adversarially sensitive. Say whether a human reviewed it, as that single flag changes what the creator should do next. Show the confidence band rather than a binary, because a marginal decision deserves a different response. Categorise which policy categories warrant reduced detail rather than applying the strictest standard everywhere. Retain the record long enough for a later review, as appeals and regulatory requests arrive after retention periods sometimes expire. Surface the same detail in the creator's own dashboard rather than only in a notification that gets lost. Test the expanded notification on a category with low adversarial risk and measure the effect, since the objection is empirical and has never been tested. Report how often appeals succeed with and without the detail. And extend it category by category rather than waiting for a complete policy.

## Who Feels the Pain
Creators appealing without knowing what to address; reviewers re-deciding with no more information; support staff explaining nothing; and platforms whose appeal process cannot function on the information it is given.

## Impact If Fixed
A message format designed to state an outcome cannot carry a rationale that was never part of it. Giving the appeal reviewer the full internal record requires no external disclosure and is the cheapest improvement available.
