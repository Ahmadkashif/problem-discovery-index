# Learning a Target Is Hostile by Being Blocked

**Niche:** [[niches/web-data-extraction-firms/request-log-intelligence/profile|Request Log Intelligence]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A target deploys new defences and the firm finds out when a collection stops working, after burning through addresses and a customer's data has already gone stale.
**Tags:** #change-point-detection #time-series-forecasting #evaluation-metrics #descriptive-statistics #confidence-intervals #automation #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to turn a complete record of every request the firm makes into knowledge about targets, cost and risk — and whoever does that operates on evidence while everyone else operates on the last incident.

## The Problem
A large retailer deploys a new detection system on a Tuesday. The firm's success rate against that host begins declining immediately, drifts down over three days, and crosses an alert threshold on Friday by which point a substantial portion of the address pool has been flagged at that host and is now useless there. Three customers' feeds have been degrading all week without anyone noticing, because the monitoring alerts on failure rather than on a trend. The signal was unambiguous from Tuesday afternoon and nobody was watching it.

## Why It's Still Broken
Monitoring is built around thresholds on current state rather than around change in a rate, which is a design choice that predates anyone asking for early warning. A gradual decline within tolerance produces no alert by construction. Address burn is not measured per host, so the cost of the delay is invisible. And the firm experiences the event as the target's action rather than as its own detection failure.

## What a Fix Looks Like
Watch the trend, not the threshold. Run change-point detection on success rate per host continuously, which detects a defensive deployment within hours rather than days and requires only data already streaming — this is the fix and it is a small build. Track address burn per host, so the cost of a slow response is visible and the pool can be protected by backing off rather than by continuing to spend into a wall. Back off automatically on a detected change rather than continuing at full rate, which preserves the pool and is also the more defensible behaviour. Alert customers early, since a degrading feed they know about is manageable and one they discover later is not. Correlate across customers and targets, because a detection vendor's new release affects many hosts simultaneously and recognising that is far more useful than treating each as its own incident. Retire flagged addresses from that host rather than globally, since an address burnt at one target is usually fine elsewhere and blanket retirement wastes the pool. Record every defensive change in the target profile, which builds the intelligence the build note describes. And report time-from-change-to-detection as a metric, because it is currently days and nobody has named it.

## Who Feels the Pain
Customers whose feeds degraded quietly for a week; operations teams rebuilding pools burnt while nobody was watching; and the firms whose response time to a target's action is measured in days for no technical reason.

## Impact If Fixed
The signal is unambiguous within hours and the alerting is built to fire on failure rather than on change. Change-point detection per host is a small build on data already streaming, and correlating across hosts identifies a detection vendor's release rather than a dozen separate incidents.
