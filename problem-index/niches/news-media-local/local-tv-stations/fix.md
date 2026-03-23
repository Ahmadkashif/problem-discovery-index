# Ad Traffic Reconciliation Errors

**Niche:** [[niches/news-media-local/local-tv-stations/profile|Local TV News Stations]]
**Industry:** [[industries/news-media-local|Local News Media]]
**Type:** Fix (Pain Point)
**One-liner:** Local TV stations lose 3-8% of ad revenue annually to make-goods and credits caused by discrepancies between sold spots, traffic logs, and actual air verification — a reconciliation process still done manually in most mid-market stations.
**Tags:** #data-integration #automation #anomaly-detection #tabular-ml #revenue-impact

## The Problem
The ad revenue pipeline at a local TV station involves three separate systems: the sales system (WideOrbit or Matrix) where spots are sold, the traffic system where spots are scheduled into commercial breaks, and the air verification log that confirms what actually ran. Discrepancies between these three records — a spot sold but not scheduled, scheduled but preempted, aired but at the wrong time — trigger "make-goods" (free re-runs) or credits to advertisers. At mid-market stations, a traffic coordinator manually reconciles these logs daily, and errors slip through constantly because the systems don't automatically cross-reference.

## Why It's Still Broken
WideOrbit dominates traffic and billing but requires manual data entry at multiple stages. The air verification feed from the automation system (often Grass Valley or Imagine) outputs in proprietary formats that don't cleanly map to WideOrbit's expected inputs. Stations have built custom scripts and spreadsheet macros to bridge the gap, but these break whenever a system is updated. Corporate ownership groups mandate specific tools but don't invest in the integration layer between them, leaving each station to improvise.

## What a Fix Looks Like
An automated reconciliation engine that: (1) pulls sold orders from the sales system, (2) compares against the traffic log in real-time, (3) ingests the air verification feed and flags discrepancies within minutes of airing, and (4) auto-generates make-good recommendations with advertiser notification templates. The traffic coordinator reviews exceptions rather than manually cross-checking every spot.

## Who Feels the Pain
Traffic coordinators who spend 2-3 hours daily on manual reconciliation, and sales managers who lose commission revenue to avoidable make-goods.

## Impact If Fixed
Recovers 3-8% of annual ad revenue lost to undetected discrepancies — worth $150K-500K per station in mid-to-large markets — while reducing traffic coordinator workload by 50%.
