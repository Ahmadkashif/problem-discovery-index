# Anomaly Ranking Across a Test Campaign

**Niche:** [[niches/defense-systems-manufacturers/test-data-reduction-reporting/profile|Test Data Reduction & Test Reporting]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Test engineers review each event's thousands of channels by eye, with no model of what each channel did in every earlier event of the campaign.
**Tags:** #autoencoders #lstms-and-grus #change-point-detection #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to turn every test event's telemetry into findings before the next event, and whoever catches the most anomalies before the next test is run takes the account.

## The Problem
A qualification campaign for a motor or a spacecraft runs dozens of events. In each, engineers plot channels against predicted envelopes and look for anything out of family. Subtle anomalies (a slowly growing oscillation, a sensor that reads slightly differently after a thermal cycle) only show against the article's own history, which no one has time to review.

## Why Nobody Has Built This
Each programme's data formats, channel lists and analysis scripts are bespoke, and the data are ITAR-controlled or classified, so general analytics vendors haven't built for it. Anomaly detection models need per-article history, which only arrives as the campaign runs.

## What to Build
A campaign memory: every event's telemetry stored with configuration and test conditions, a per-channel model of normal behaviour learned across events and articles of the family, and a ranked list of out-of-family segments for each new event, each with its closest past traces and their resolutions. Anomalies are tracked to closure so recurring ones surface.

## Target Customer
Test engineering directors at motor, missile, vehicle and spacecraft makers running qualification and acceptance campaigns.

## Impact If Built
Catching an anomaly one event earlier can save a repeat test costing hundreds of thousands to millions of dollars (estimate) and avoid carrying a hidden fault into flight.
