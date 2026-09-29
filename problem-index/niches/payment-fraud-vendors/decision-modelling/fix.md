# Retrained on a Schedule

**Niche:** [[niches/payment-fraud-vendors/decision-modelling/profile|Decision Modelling]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The model retrains monthly whether anything has changed or not, and the attack that started on the fourth runs until the next cycle.
**Tags:** #change-point-detection #quick-win #evaluation-metrics #automation #confidence-intervals #descriptive-statistics #gradient-boosting #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to build the best decision from device, behavioural, network and consortium signals against an adversary who adapts — and whoever models best on the labels that exist wins the transactions everybody else gets wrong.

## The Problem
Retraining runs on a calendar. Between cycles, the model is static while the adversary is not. An attack campaign that begins shortly after a retrain has weeks of clear running, and the only thing that detects it is either a rule someone writes in response to a loss spike or a merchant complaint. Meanwhile a month with no meaningful change consumes the same retraining effort and validation cycle as a month with a major shift.

## Why It's Still Broken
Retraining was scheduled because scheduling is operationally simple, so cadence substituted for detection — a monthly job is easier to run and validate than a trigger nobody trusts. Drift detection on delayed labels is genuinely hard, and nobody built the leading indicators that do not need labels. Deploying a model outside the cycle requires validation nobody has streamlined. And the gap between attack onset and detection is not measured.

## What a Fix Looks Like
Detect the change rather than waiting for the calendar. Monitor feature distributions and score distributions continuously, which is the fix and detects a shift without needing any labels at all. Alert on a sudden change in the mix of approved traffic, since an attack that succeeds shows up as a population shift before it shows up as a chargeback. Track early proxies — authorisation behaviour, velocity patterns, new device and network clusters — because they move immediately and chargebacks do not. Trigger retraining on detected change as well as on the schedule, so the cadence becomes a floor rather than the mechanism. Streamline out-of-cycle deployment with a pre-agreed validation path, as the operational friction is what makes cadence the default. Measure time from attack onset to detection retrospectively for known campaigns, which quantifies the gap and is currently unmeasured. Compare across merchants, since a pattern appearing at several at once is a strong and immediate signal. Keep a challenger model running continuously, so a replacement is ready rather than trained under pressure. Record every intervention and its effect, because the current response is rules written under stress and forgotten. And report detection lag as a service metric, since it is the number that matters and nobody publishes it.

## Who Feels the Pain
Merchants absorbing weeks of a campaign; analysts drowning in the review queue an attack produces; data teams retraining on a calendar that does not match the threat; and vendors whose response time is invisible.

## Impact If Fixed
Scheduling is operationally simple, so cadence substituted for detection and a monthly job replaced a trigger nobody trusted. Distribution monitoring detects a shift without labels and turns the calendar into a floor rather than the mechanism.
