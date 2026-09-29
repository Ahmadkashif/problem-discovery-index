# The Reward Table Typed in Twice

**Niche:** [[niches/game-liveops-services/live-content-production/profile|Live Content Production]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Fix (Pain Point)
**One-liner:** The reward value was right in the design document, wrong in the config, and correct nowhere by the time it shipped.
**Tags:** #quick-win #automation #workflow-orchestration #data-integration #compliance #evaluation-metrics #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to cut the cost of producing and shipping each event in a calendar that never has a gap — and whoever cuts it takes the account.

## The Problem
Event values are authored in one place and entered in another. A designer sets reward amounts in a spreadsheet, someone transcribes them into the configuration console, and the two drift — a decimal point, a currency type, a tier mismatch. The result is a live event granting the wrong amount, discovered by players, mitigated at speed, and followed by compensation. It is among the most common live incidents and it is a transcription error.

## Why It's Still Broken
Two systems hold the same numbers and neither is authoritative — a value that exists in two places with no link between them will diverge, and the only detection is a player noticing. The console has no validation. The design document is not machine-readable. And the check depends on whoever is available.

## What a Fix Looks Like
Make one source authoritative and validate before publish. Import reward tables directly from the design source rather than retyping them, which is the fix and removes the error class rather than catching it. Validate values against expected ranges before publish, since an order-of-magnitude error is trivially detectable. Check currency types and tier consistency automatically, as those are the other two recurring mistakes. Show a diff against the previous comparable event, which surfaces anomalies immediately to a human. Require a second confirmation only on values outside the normal band, so the friction is proportionate. Simulate the economy inflow the event will produce and flag outliers, which catches the errors ranges miss. Keep the design source and the live config linked so drift is visible. Log who published what, because reconstructing this during an incident wastes the first hour. Provide a fast corrective path including compensation, since some will still get through. And apply the same validation to every event automatically rather than to the ones someone remembered to check.

## Who Feels the Pain
Live teams handling an avoidable incident; designers whose event shipped wrong; players receiving wrong rewards and then compensation; and the on-call person who got the page.

## Impact If Fixed
A value that exists in two places with no link between them will diverge, and the only detection is a player noticing. Importing from the design source and validating ranges removes the error class rather than catching it.
