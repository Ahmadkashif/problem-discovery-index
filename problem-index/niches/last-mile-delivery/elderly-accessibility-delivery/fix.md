# Failed Delivery Rate for Elderly Recipients

**Niche:** [[niches/last-mile-delivery/elderly-accessibility-delivery/profile|Elderly & Accessibility-Focused Delivery]]
**Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Type:** Fix (Pain Point)
**One-liner:** Elderly recipients have 2-3x the failed first-attempt delivery rate of the general population — driven by slow door response, inaccessible package placement, and inability to use digital signature pads — but delivery operations treat all stops identically, applying the same 30-second wait time and standard procedures regardless of recipient demographics.
**Tags:** #gradient-boosting #automation #worker-facing #data-integration

## The Problem
Standard delivery procedure: ring doorbell, wait 30 seconds, leave package or "sorry we missed you" notice. For elderly recipients, 30 seconds isn't enough — they may need 60-90 seconds to reach the door from another room, especially with mobility aids. Drivers following the standard protocol mark the delivery as "attempted" and leave before the recipient reaches the door. The recipient then calls customer service, a redelivery is scheduled, and the cycle repeats. Signature-required deliveries (medications, high-value items) are worse: the elderly recipient arrives at the door after 45 seconds, but the driver is already walking to the van.

## Why It's Still Broken
Delivery operations optimize for stops-per-hour. Adding 30-60 seconds to elderly recipient stops reduces the driver's daily capacity by 10-15 stops — a material productivity hit. No delivery platform flags addresses as elderly/accessibility to adjust wait time expectations. The economic incentive (faster delivery = more stops = more revenue) directly conflicts with the elderly recipient's physical ability to respond.

## What a Fix Looks Like
An address-level configuration that: (1) flags addresses with elderly or mobility-impaired recipients (from recipient profile or delivery history patterns); (2) adjusts the expected wait time at flagged addresses (90-120 seconds instead of 30); (3) accounts for the extended wait time in route planning (so the driver isn't penalized for "slow stops"); (4) prompts the driver to knock/ring a second time after 60 seconds at flagged addresses before marking attempted.

## Who Feels the Pain
Elderly recipients who repeatedly miss deliveries despite being home, and who must navigate redelivery scheduling through phone systems designed for tech-savvy users.

## Impact If Fixed
Extending wait time at elderly-flagged addresses from 30 to 90 seconds reduces failed first attempts by 40-60% for this population. The 30-second per-stop productivity cost is offset by eliminated redelivery costs ($6-10 per redelivery) and reduced customer service call volume.
