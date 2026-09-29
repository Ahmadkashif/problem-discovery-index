# One Calibration for Every Product

**Niche:** [[niches/embedded-finance-platforms/conduct-monitoring/profile|Conduct Monitoring]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The alert thresholds were calibrated for one programme and are applied to all of them, so a payroll product and a teen spending card generate alerts against the same rules.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #compliance #quick-win #hypothesis-testing #change-point-detection #automation
**Contested on:** Every serious competitor in this niche is fighting to infer how a programme treats its customers from the API calls it makes — and whoever detects a problem before the bank's examiner does defines what oversight from this layer can mean.

## The Problem
A payroll disbursement product moves large regular amounts to many recipients. A teen spending card moves small irregular amounts. A business expense product moves medium amounts between related parties. A gig platform's payout product moves variable amounts at unpredictable times. The monitoring applies one set of thresholds to all of them, calibrated against whichever programme was live when they were set. Three of the four generate constant alerts that are all normal for that product, the analysts learn to dismiss them, and the fourth generates none at all because its normal behaviour is below every threshold.

## Why It's Still Broken
Thresholds were set for the first programme and new programmes inherited them, because adding a programme is an onboarding task rather than a monitoring design exercise — the configuration follows the account setup and nobody treats calibration as part of it. Per-programme calibration requires baseline data a new programme does not have. Analysts absorb the noise. And a programme generating no alerts looks compliant rather than unmonitored.

## What a Fix Looks Like
Calibrate per programme and per archetype. Set thresholds from each programme's own observed behaviour rather than from a global default, which is the fix and immediately removes most of the noise and reveals the programmes generating nothing. Use archetype defaults for new programmes, since the twenty recurring programme shapes have known behavioural profiles and a payroll product should not start on a spending card's thresholds. Recalibrate as a programme's behaviour matures, because an early-stage programme and a scaled one are different and the thresholds set at launch decay. Report alert rate per programme, which makes both the noisy and the silent ones visible immediately and is a one-query diagnostic. Investigate the silent programmes specifically, since no alerts is a finding rather than a clean bill. Measure precision per rule per programme, so rules that fire only falsely for a given product can be suppressed there rather than everywhere. Compare against the archetype rather than against an absolute, which is the cross-programme instrument applied to alerting. Escalate on deviation from the programme's own norm as well as on absolute thresholds, since the change is more informative than the level. Involve the analysts in the calibration, since they know which alerts are noise and are never asked. And report alert quality as a function metric, because a monitoring function measured on alert volume will produce alert volume.

## Who Feels the Pain
Analysts dismissing alerts that are normal for the product; programmes generating no alerts because nobody calibrated for them; and banks relying on monitoring whose coverage nobody has examined.

## Impact If Fixed
The configuration follows account setup and calibration was never part of it, so thresholds set for the first programme apply to every one after. Per-programme calibration with archetype defaults removes the noise and reveals the programmes that were never being monitored at all.
