# The Upstream Schema Change Nobody Told the Model About

**Niche:** [[niches/mlops-platforms/feature-coverage-and-lineage/profile|Feature Coverage & Lineage]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A data engineer renames a column, changes a unit, or alters how nulls are encoded, and a model in production degrades with nobody connecting the two for weeks.
**Tags:** #data-integration #change-point-detection #evaluation-metrics #automation #compliance #descriptive-statistics #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to extend the consistency guarantee to the features that were never registered — and whoever does that takes the account, because the unregistered features are the majority and are where the failures are.

## The Problem
An upstream team changes a currency field from cents to dollars and updates their own consumers correctly. A recommendation model reads that column through a feature pipeline nobody on the upstream team knows exists. The model's inputs become a hundredth of what they were, the model continues serving without error, conversion drops four percent, and the marketing team opens an investigation into seasonality. Three weeks later somebody joins the deploy log to the metric and finds it. The upstream team did nothing wrong; there was no mechanism by which they could have known.

## Why It's Still Broken
The dependency is invisible from the upstream side, and a team cannot notify consumers it cannot enumerate. Model inputs degrade rather than fail, so there is no error to trace back. The two teams sit in different organisations with different on-call rotations and no shared surface. And the investigation always starts from the business metric, which is the furthest possible point from the cause.

## What a Fix Looks Like
Make the dependency visible to the person making the change. Publish model consumption upstream, so that a data engineer editing a column sees which models depend on it before they merge — which is the fix, and the rest is refinement. Gate breaking changes behind acknowledgement from the model owner rather than merely notifying, since a notification into a busy channel is not a control. Monitor input distributions per feature at serving time and alert on step changes, because that catches the cases where no schema change was recorded at all — a semantic change, a backfill, an upstream job silently failing — which are as common as the declared ones. Include the deploy and data-change event stream in the model's own incident timeline, so an investigation starts with what changed rather than reconstructing it. Report the model's sensitivity to each input, so a change to a dominant feature escalates differently from a change to a marginal one. Detect unit and encoding changes specifically, since a hundredfold shift in a numeric column is trivially detectable and is a recurring and expensive case. And measure time from upstream change to detection as the metric the fix is judged on, because it is currently weeks and nobody is tracking it.

## Who Feels the Pain
Model owners debugging a degradation whose cause is in another team's merge; data engineers who broke something they had no way to see; and the business functions running investigations into a seasonality that was a unit conversion.

## Impact If Fixed
The upstream engineer cannot see the dependency, so no notification is possible. Publishing model consumption at the point of change is the fix; distribution monitoring at serving time covers the semantic changes no schema diff would catch.
