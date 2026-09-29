# Build: A Maintained Operating Point

**Niche:** Threshold Optimisation
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Compute the threshold from the customer's live score distribution and their stated error costs, monitor the realised error rates, and recompute whenever the model or the content changes.
**Tags:** #bayesian-inference #convex-optimization #evaluation-metrics #confidence-intervals #probability-distributions #change-point-detection #automation #data-integration
**Contested on:** Whether the operating point is computed from the score distribution and the stated costs, and maintained as both drift.

## The Problem

A threshold is a number set once and then treated as constant. It is not constant in effect.

The score distribution shifts continuously. The content on a platform changes with events, seasons, user growth and product changes. A category that was rare becomes common. A community with different language patterns joins. Each moves the distribution, and a fixed threshold sitting on a moving distribution is a moving operating point.

Model updates are worse. A retrained model's scores are differently calibrated, sometimes substantially, and the threshold is frequently carried over unchanged because it is a configuration value and the deployment was a model change. The operating point can move dramatically at that moment, in either direction, with no alert.

And the realised error rates at the current threshold are not monitored anywhere. A platform can tell you the threshold and cannot tell you what proportion of actioned content was wrongly actioned or what proportion of harmful content is passing.

The computation is straightforward. Given a cost ratio and a score distribution, the threshold minimising expected cost is elementary. Given monitoring, drift is detectable. Given both, the operating point can be maintained.

## Why Nobody Has Built This

**It needs the costs, which do not exist.** Optimisation requires the error costs as an input, which is the elicitation problem. A vendor can work around this with a stated target error rate instead, and few do.

**The threshold is the customer's configuration.** Vendors ship a field and consider the choice the customer's, which makes maintaining it feel like overstepping.

**Model updates are deployed as model updates.** The release process treats the model as the artefact and the threshold as customer configuration, so they are not reconciled.

**Error rate monitoring requires labelled outcomes.** Knowing the realised false positive rate needs sampled review of actioned content, which is review capacity nobody has allocated.

**Automatic threshold changes are alarming.** A system that moves a moderation threshold by itself is a system that could move it badly, so the safe default is to leave it static.

**Nobody has noticed the drift.** Because the configuration value does not change, nothing signals that the operating point has, and the effect is invisible.

## What to Build

**Compute from the customer's live distribution.** The vendor's precision-recall curve is computed on their test set; the customer's operating point depends on their content. Computing the curve on the customer's own score distribution is the first step and it is straightforward.

**Optimise against the stated costs, or a stated target.** Where costs are elicited, minimise expected cost. Where they are not, let the customer state a target error rate on one side and compute the threshold that achieves it — which is a workable substitute and is not offered anywhere.

**Monitor drift in the score distribution.** Alert when the distribution moves enough that the current threshold represents a materially different operating point. This is change detection on a distribution and is entirely standard.

**Reconcile thresholds on model update.** A model change should trigger recalibration of every threshold, with the equivalent operating point computed on the new scale. This is the single largest silent failure in the category and it is a release process change.

**Measure the realised error rates.** Sampled review of actioned and unactioned content, producing the actual precision and recall at the operating point. Small samples, run regularly, and it tells a platform where it actually is.

**Recommend rather than change automatically.** Alert and propose a new threshold with its projected effect, and let a human approve. This addresses the reasonable objection to automatic movement while still keeping the operating point current.

**Show the effect before the change.** How many more items would be actioned, how many fewer, and the projected error rates. A threshold change with no visible consequence is why nobody adjusts them.

## Target Customer

Trust and safety engineering teams, who set these thresholds, know they are stale, and have no instrument for maintaining them.

Vendors, for whom threshold maintenance is a differentiating capability that does not depend on unverifiable accuracy claims and addresses a failure their customers experience.

Platforms under regulatory reporting obligations, who must describe their moderation performance and currently cannot state what their operating point actually achieves.

## Impact If Built

The operating point stops drifting silently, which is a failure mode that changes what billions of people see and is currently invisible because the configuration value stays the same.

Reconciling thresholds on model update addresses the largest single unremarked failure in the category — a retrained model with a carried-over threshold can move the operating point substantially overnight.

And measuring the realised error rates would tell a platform where it actually operates, which neither the vendor's test-set curve nor the configuration value currently reveals.
