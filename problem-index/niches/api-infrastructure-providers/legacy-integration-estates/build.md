# The Integrations Nobody Can Enumerate

**Niche:** [[niches/api-infrastructure-providers/legacy-integration-estates/profile|Legacy Integration Estates]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most enterprise data still moves by file transfer, message queue and SOAP, and the organisations running those flows cannot produce a list of them, let alone monitor them.
**Tags:** #graph-theory #descriptive-statistics #bert #change-point-detection #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor here is fighting to bring visibility and change safety to the file transfers, message queues and SOAP services that still move most enterprise data — and whoever does that takes the integration estate, because nobody can currently see it at all.

## The Problem
A bank is asked, for a regulatory exercise, to document every flow of customer data between its systems and to third parties. The modern APIs are documented. Beyond them are several hundred scheduled file transfers, a set of queues consumed by systems in three departments, a dozen SOAP services, and an unknown number of direct database connections. Some were built in the nineties. Several have no named owner. The exercise takes nine months, produces a spreadsheet, and is out of date before it is signed off, because nothing produced it from observation.

## Why Nobody Has Built This
The category's attention followed the new protocols, and the vendors serving the old ones are the incumbents who sold them, with limited incentive to make the estate legible enough to rationalise. Discovery across heterogeneous mechanisms — file transfer, queues, SOAP, direct database links — means integrating with several very different systems rather than terminating one protocol at a gateway, which is a less elegant product. And the estate is genuinely uncomfortable to look at: a complete inventory typically reveals flows nobody knew existed carrying data nobody knew was moving, which is a finding that creates work.

## What to Build
Discovery and monitoring across the whole estate, from observation rather than documentation. Discover flows from the evidence: transfer server logs, queue broker metadata, network connections between systems, scheduler jobs, and database link definitions — each of which is available and none of which is consulted. Resolve them into named integrations with source, destination, schedule, volume and data shape. Attach ownership, which will be unresolvable for a proportion of them and is a finding rather than a failure. Monitor end to end rather than per component, so a flow that leaves one system and does not arrive at the other is detected as one condition rather than as a gap in two dashboards. Baseline each flow's normal behaviour — timing, volume, record count, value distributions — and alert on deviation, which is where the real failures are and is the same observation the connector-drift niche makes about silent success. Map the dependency graph, so that the question of what depends on this file can be answered before it changes. And produce the inventory continuously, so the regulatory exercise becomes a query rather than a project.

## Target Customer
Enterprise integration and platform teams in banking, insurance, healthcare, government and manufacturing; and the integration and file transfer vendors whose products hold most of the evidence.

## Impact If Built
The highest-consequence integrations in most enterprises are the least visible, which is exactly the wrong way round, and the evidence to discover them exists in logs nobody reads. Continuous inventory turns a recurring nine-month exercise into a query, and end-to-end monitoring catches the failures that currently surface as missing data.
