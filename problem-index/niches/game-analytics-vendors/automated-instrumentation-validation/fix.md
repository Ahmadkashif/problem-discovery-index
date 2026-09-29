# The Event That Stopped Firing in March

**Niche:** [[niches/game-analytics-vendors/automated-instrumentation-validation/profile|Automated Instrumentation Validation]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Nobody noticed the event stopped arriving until June, and three months of reporting used a number that was missing a third of its input.
**Tags:** #quick-win #automation #change-point-detection #descriptive-statistics #evaluation-metrics #data-integration #confidence-intervals #compliance
**Contested on:** Every serious competitor in this niche is fighting to catch broken instrumentation when it breaks rather than when a metric looks wrong weeks later — and whoever automates that check takes the account.

## The Problem
An event stops arriving — removed in a refactor, broken on one platform, gated behind a condition that changed. Nothing alerts, because nothing is watching for absence. The metrics built on it drift downward, the drift looks like a product problem, and weeks or months of investigation and decision-making happen before somebody checks the raw event counts and finds the real cause.

## Why It's Still Broken
Nothing watches for absence — a pipeline that only processes what arrives cannot notice what stopped arriving, and an event going to zero looks exactly like a pipeline with nothing to do. Nobody owns event health. The drift is attributed to the product. And the discovery is accidental.

## What a Fix Looks Like
Watch the event counts, which is the cheapest monitoring available. Alert when any event's volume drops sharply or goes to zero, which is the fix and takes an afternoon to implement. Segment by platform and client version, since breaks are frequently version-specific and invisible in the total. Compare against player counts rather than absolute volume, so a quiet week does not fire an alert. Check on every build release specifically, which is when most breaks occur. Maintain a simple event health dashboard anyone can look at, which is the first thing to check when a number looks odd. List the metrics each event feeds, so an alert states what is affected. Annotate historical reports when a break is found rather than silently correcting them. Check for the opposite failure too, where an event starts firing far more than expected. Assign event health to a named owner. And review the alert list periodically so it stays meaningful rather than becoming noise.

## Who Feels the Pain
Studios that investigated a product problem that was a data problem; analysts whose numbers were wrong for months; decisions made on incomplete data; and the engineer who eventually found it.

## Impact If Fixed
A pipeline that only processes what arrives cannot notice what stopped arriving, and an event going to zero looks exactly like nothing to do. A volume alert per event is an afternoon of work against months of wrong numbers.
