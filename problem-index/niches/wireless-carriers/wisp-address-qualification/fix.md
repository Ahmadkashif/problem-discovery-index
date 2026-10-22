# The Summer Leaf-Out Cancellation

**Niche:** [[niches/wireless-carriers/wisp-address-qualification/profile|WISP Address Qualification & Installs]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** An install that tested fine in March fails in June when the trees leaf out, and the customer cancels before anyone connects the two.
**Tags:** #change-point-detection #time-series-forecasting #feature-engineering #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche (coverage-prediction tools, LiDAR heat-map vendors and radio makers' planning software) is fighting to tell, before the truck rolls, whether a specific roofline can hold the advertised speed from a specific sector, and whoever qualifies addresses most accurately takes the account.

## The Problem
Foliage attenuates fixed wireless signals, especially at higher frequencies. Installs done in winter on marginal paths degrade every spring. The customer sees slower speeds and calls support, which resets the radio, and eventually cancels.

## Why It's Still Broken
Install records don't capture the season or the margin, and signal history isn't watched for seasonal decline. Support treats each call as a new problem.

## What a Fix Looks Like
Flag winter installs with thin margins at install time. Watch each customer's signal level for the seasonal step change, and schedule a proactive visit to raise or re-aim the antenna before the customer calls.

## Who Feels the Pain
Installers sent back to the same houses, support staff, and customers who think the service is just bad.

## Impact If Fixed
A predictable wave of spring cancellations becomes a scheduled maintenance list.
