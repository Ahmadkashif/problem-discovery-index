# On-Site Visit Scheduling and Route Optimization

**Niche:** [[niches/it-managed-services/rural-small-town/profile|Rural & Small-Town MSPs]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Fix (Pain Point)
**One-liner:** Rural MSP technicians drive 200-400 miles per week visiting clients scattered across a wide geographic area, and there is no system that batches on-site visits by geography and urgency to minimize windshield time.
**Tags:** #automation #workflow-orchestration #worker-facing #quick-win

## The Problem
A rural MSP serving 40 clients across a 100-mile radius may have 10-15 on-site visits per week for hardware replacements, network projects, and issues that cannot be resolved remotely. Technicians schedule visits based on urgency and client requests, not geography — driving 45 minutes to a client in the morning, returning to the office, then driving 40 minutes in the same direction for a different client in the afternoon. The drive time is unbillable: at an average of 1.5 hours of driving per on-site visit, a technician making 3 on-site visits per day spends 4.5 hours driving and 4 hours working. Geographic batching (combining all visits in the same direction into a single trip) could save 30-50% of drive time, but the scheduling is done ad-hoc in the technician's head or on a calendar with no geographic awareness.

## Why It's Still Broken
PSA platforms schedule tickets by priority and technician availability without geographic context. Route optimization tools (Google Maps, Route4Me) optimize delivery routes but do not integrate with a PSA's ticket queue. The missing connection is between "which on-site tickets need to be addressed this week" (PSA data) and "what is the most efficient route to cover them" (geographic optimization). Additionally, some visits are time-sensitive (server down) while others can be batched (hardware swap, quarterly maintenance visit), and the scheduling system must distinguish between these.

## What a Fix Looks Like
A geographically-aware scheduling layer on top of the PSA that: plots all pending on-site tickets on a map, identifies geographic clusters, suggests daily routes that minimize drive time while respecting ticket priority (urgent tickets are visited first regardless of location, non-urgent tickets are batched by geography), estimates travel time between stops, and provides the technician with a daily route plan. The system also identifies opportunities to schedule proactive maintenance visits when the technician is already in the area ("you're driving past ABC Accounting tomorrow — their quarterly firewall maintenance is due this week").

## Who Feels the Pain
Technicians who spend 20-30 hours per week driving instead of doing billable work, and MSP owners who see 40-50% of technician capacity consumed by windshield time.

## Impact If Fixed
Reduces weekly drive time by 30-50% (6-15 hours per technician per week), enabling 1-2 additional billable visits per day. For a 3-technician MSP, this recovers $50K-$100K annually in previously unbillable time.
