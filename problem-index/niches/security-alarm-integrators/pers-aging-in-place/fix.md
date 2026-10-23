# The Pendant on the Nightstand

**Niche:** [[niches/security-alarm-integrators/pers-aging-in-place/profile|Personal Emergency Response & Aging-in-Place Subscribers]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** The subscriber stopped wearing the pendant months ago, the monthly test signal still arrives, and the account looks healthy until the fall nobody hears about.
**Tags:** #change-point-detection #logistic-regression #feature-engineering #quick-win #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to get the right responder to a fallen or unwell subscriber quickly while keeping unnecessary EMS dispatches down, and whoever shows the paying Medicaid programme or health plan the fewest missed emergencies per false dispatch takes the account.

## The Problem
Pendants report a periodic test to show the device is alive, not that it's worn. Many subscribers take the pendant off to shower or sleep and don't put it back, or dislike how it looks. The provider is paid monthly either way, and the payer assumes protection that doesn't exist.

## Why It's Still Broken
Older pendants don't sense wear. Newer wearables do, through step counts and motion, but the data goes unused because no workflow follows from it and nobody bills for it.

## What a Fix Looks Like
For devices with accelerometers, flag subscribers whose movement shows the device hasn't been worn for set periods, and trigger a friendly check-in call or a family text. Report wear rates to payers as a quality measure.

## Who Feels the Pain
Subscribers who fall unprotected; families who believed they were covered; and providers whose contracts depend on outcomes they can't show.

## Impact If Fixed
Wear becomes a managed measure rather than an unknown, using data many current devices already send.
