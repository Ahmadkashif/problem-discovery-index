# Fix: The Model Was Retrained and the Threshold Was Not

**Niche:** Threshold Optimisation
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A new model ships with better reported accuracy, the customer's threshold is carried over unchanged, and the operating point moves overnight with nothing to indicate it.
**Tags:** #change-point-detection #evaluation-metrics #confidence-intervals #probability-distributions #automation #compliance
**Contested on:** Whether the operating point is computed from the score distribution and the stated costs, and maintained as both drift.

## The Problem

The vendor ships an improved model. Better reported accuracy, better handling of a category that had been weak, released through the normal update process.

The customer's threshold is a configuration value. It does not change, because nothing in the release changes it.

But the new model's scores are distributed differently. A score of 0.85 from the old model and 0.85 from the new one do not represent the same confidence, because calibration is a property of a trained model and retraining changes it. So the threshold that was catching a certain proportion is now catching a different one.

The move can be substantial and can go either way. A model with better separation may push more content above the threshold, increasing both actioning and false positives. Or it may compress scores downward, silently letting more through.

Nobody is told. The configuration is unchanged, the model is improved, and the operating point has shifted. The customer finds out when their review queue volume changes, or when a complaint pattern emerges, or not at all.

The fix is a standard deployment step everywhere else in machine learning. It has not been applied because the threshold belongs to the customer and the model belongs to the vendor.

## Why It's Still Broken

**The threshold is on the customer's side of the boundary.** The vendor ships a model; the customer configures a threshold. Neither owns the reconciliation between them.

**Improved accuracy sounds unambiguously good.** A release note saying the model is better does not suggest that the customer's operating point has moved.

**Calibration is rarely established or communicated.** If neither party treats the score as a calibrated probability, the fact that its meaning changed is not obviously a problem.

**The effect is invisible without outcome measurement.** A shifted operating point changes error rates, which nobody measures, so the change produces no signal.

**Customers cannot easily test it.** Comparing the new model's behaviour against the old at their threshold requires running both, which the update process does not support.

**Queue volume changes are attributed elsewhere.** A shift in review volume after an update is frequently attributed to content changes rather than to the model, because nobody looked.

## What a Fix Looks Like

**Recalibrate and publish the equivalent threshold on every model release.** The vendor computes, for each existing customer threshold, the value on the new model that produces the equivalent operating point, and ships it with the release. This is the fix and it is a release step.

**Report the expected effect of the update.** At your current threshold, this update will action approximately this much more or less content, with this projected effect on error rates. This is computable on the vendor's own data and is not communicated anywhere.

**Support shadow running.** Let the customer run the new model alongside the old for a period and compare, before switching. This is standard deployment practice and would remove the risk entirely.

**Calibrate the scores and say so.** A score that is a calibrated probability has a stable meaning across model versions, which makes the threshold portable. Uncalibrated scores are why the problem exists.

**Alert on queue volume shift after a release.** A simple monitor comparing actioning volume before and after would catch the effect within days rather than never.

**Never carry a threshold across a model version silently.** A release requiring explicit threshold confirmation is a small friction that prevents a substantial and invisible change.

**Measure the realised error rates around updates.** A sampled review before and after a model update would establish what actually changed, which is currently unknown at every deployment.

## Who Feels the Pain

Users on the platform, who experience a changed moderation posture with nobody having decided to change it.

The trust and safety engineer, who receives an improved model, keeps their configuration, and has unknowingly altered how much content is actioned.

The platform, whose regulatory reporting describes a moderation approach that shifted at a model release nobody recorded as a policy change.

And the vendor, whose genuine model improvement may have produced a worse outcome at the customer's operating point and who has no way to know.

## Impact If Fixed

Shipping an equivalent threshold with every model release is a release step borrowed directly from standard practice and prevents a substantial silent change in what billions of people see.

Reporting the expected effect of an update at the customer's current threshold is computable on the vendor's own data and is not offered anywhere.

And calibrating the scores properly would make thresholds portable across model versions, which removes the underlying cause rather than managing its symptom.
