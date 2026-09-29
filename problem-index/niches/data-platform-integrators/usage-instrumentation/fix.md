# The Query Log Nobody Has Opened

**Niche:** [[niches/data-platform-integrators/usage-instrumentation/profile|Usage Instrumentation]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** The platform has retained every query for a year and the team has never looked at it as anything but a troubleshooting tool.
**Tags:** #quick-win #data-integration #descriptive-statistics #evaluation-metrics #automation #workflow-orchestration #revenue-impact #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to turn query logs, lineage and cost data into a standing account of what each asset is worth — and whoever produces that takes the account.

## The Problem
The query log is treated as an operational artefact: consulted when something is slow or expensive, ignored otherwise. It is simultaneously a complete record of what the organisation's data estate is for — who asks what, how often, about which subject. Nobody reads it that way, so the platform team's understanding of its own users comes from tickets and requests rather than from what they actually do.

## Why It's Still Broken
The log is classified as telemetry — a record filed under troubleshooting is never read as evidence about the business, however completely it describes it. The queries are verbose and hard to read in bulk. Nobody has framed the question. And there is no report anyone expects.

## What a Fix Looks Like
Read the log as a description of the business, not as telemetry. Produce a monthly summary of the most-queried objects, the most active consumers and the least-touched assets, which is the fix and is three queries. Group queries by the objects they touch rather than by their text, which makes bulk reading possible. Identify the consumers who query most and ask them what they are doing, since that is the fastest route to understanding demand. Find the objects queried once and never again, which is the abandonment signal. Look at query failures and long-running queries by object, as those indicate assets that are hard to use rather than unused. Report the concentration — what share of queries touch the top twenty objects — which is usually striking. Share the summary with the team, so understanding of the estate is collective rather than anecdotal. Use it to prioritise documentation and optimisation, which is immediately actionable. Keep the summary as a standing artefact rather than a one-off. And retain the log for longer if the platform's default is short, because the history is the asset.

## Who Feels the Pain
Platform teams prioritising from tickets rather than behaviour; users whose actual patterns nobody knows; assets optimised because somebody complained rather than because they matter; and the log itself, holding an answer nobody asked for.

## Impact If Fixed
A record filed under troubleshooting is never read as evidence about the business, however completely it describes it. Three queries a month turn the log into an account of what the estate is for.
