# The Tag That Stopped Firing After the Release

**Niche:** [[niches/marketing-attribution-vendors/conversion-data-plumbing/profile|Conversion Data Plumbing]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A checkout change broke the conversion event for one payment method in March, the model has been fitted to incomplete data since, and nobody noticed because the total still looked plausible.
**Tags:** #change-point-detection #data-integration #evaluation-metrics #automation #quick-win #compliance #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to build the conversion record once instead of rebuilding it at every client — and whoever does that owns the input every model in the category depends on.

## The Problem
The client shipped a checkout change. One payment path stopped firing the conversion event. That path is a minority of orders, so the total fell by an amount that looked like ordinary variation. The measurement model has been fitted to this data for four months. Its channel contributions have shifted, the shift has been explained as a genuine change in channel performance, and budget has moved on the basis of a broken tag. The error is invisible in the model's own diagnostics because the model has no way to know what it was not told.

## Why It's Still Broken
Conversion pipelines are monitored for failure rather than for correctness, and a partial loss is not a failure — a pipeline that runs and returns fewer rows looks healthy in every operational check. Nobody reconciles conversions against the financial record routinely. The client's engineering team does not know which releases affect measurement. And the model absorbs the change and produces a plausible explanation for it, which is the most dangerous property of the whole arrangement.

## What a Fix Looks Like
Reconcile and monitor for silence. Compare conversion counts and values against the client's financial record daily, which is the fix, is the strongest available check, and catches partial losses that no pipeline monitor can see. Monitor by segment — payment method, device, geography, product line — because a partial loss is concentrated and an aggregate comparison can miss it. Alert on composition shifts as well as on totals, since the total may be held up by growth elsewhere while a segment has gone to zero. Connect to the client's release process so measurement-affecting changes are flagged before they ship, which is the preventive version and requires a relationship rather than a technology. Run synthetic conversions through each path periodically, which verifies end to end and catches what comparison cannot. Version the pipeline and correlate breaks with changes, so diagnosis is minutes rather than days. Mark affected periods in the data so models can exclude or adjust them, which prevents the silent corruption of every downstream estimate. Refit and restate after a correction, since leaving the contaminated period in is how a one-month break becomes a permanent distortion. Report data completeness alongside every model output, so a client knows what the estimate was fitted to. And measure time from break to detection, because the current answer is months and everything downstream depends on it.

## Who Feels the Pain
Clients reallocating budget on models fitted to broken data; vendors whose estimates were corrupted by an input they could not see; and analysts who explained a channel shift that was a tag.

## Impact If Fixed
A pipeline that runs and returns fewer rows looks healthy in every operational check, and the model produces a plausible explanation for the loss. Daily reconciliation against the financial record, segmented, is the strongest available check and catches what no pipeline monitor can.
