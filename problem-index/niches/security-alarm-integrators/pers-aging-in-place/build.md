# A Subscriber's Normal Day as the Alarm

**Niche:** [[niches/security-alarm-integrators/pers-aging-in-place/profile|Personal Emergency Response & Aging-in-Place Subscribers]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The surest sign an older adult living alone is in trouble is a broken routine, and PERS systems wait for a button press or a fall detection instead.
**Tags:** #hidden-markov-models #change-point-detection #gradient-boosting #evaluation-metrics #feature-engineering #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get the right responder to a fallen or unwell subscriber quickly while keeping unnecessary EMS dispatches down, and whoever shows the paying Medicaid programme or health plan the fewest missed emergencies per false dispatch takes the account.

## The Problem
Many falls are never reported by pendant because the subscriber wasn't wearing it, couldn't press it or didn't want to bother anyone. Fall detectors catch some and trigger on others when the device is dropped. A subscriber who hasn't left the bedroom by noon, hasn't opened the fridge in a day or is up every hour of the night is showing trouble no current system reports.

## Why Nobody Has Built This
PERS providers sell a device and monitoring, priced for payers who reimburse a fixed monthly fee. Home sensors exist in the alarm dealer's catalogue but are sold as security, and privacy concerns and false-alert fears have kept providers from treating routine as a signal.

## What to Build
Passive routine monitoring from the sensors many homes already have: door contacts, motion detectors, a fridge or medication-box sensor, with the pendant's wear and step data. A per-subscriber model of normal daily patterns flags deviations by severity. Mild ones go to a family check-in text, serious ones to the operator. Fall-detection events are re-scored using the surrounding activity before EMS is sent.

## Target Customer
Medical-alert providers and central stations holding Medicaid waiver and Medicare Advantage contracts, and the payer programme managers who want outcomes, not devices.

## Impact If Built
Problems are found before the fall, needless EMS dispatches drop, and providers can report outcomes that win payer contracts.
