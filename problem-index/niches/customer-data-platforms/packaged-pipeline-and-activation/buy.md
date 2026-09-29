# Integration Platform Practice

**Niche:** [[niches/customer-data-platforms/packaged-pipeline-and-activation/profile|Packaged Pipeline & Activation]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Integration platforms solved connector maintenance, monitoring and error handling across hundreds of systems, and customer data pipelines rediscover it one destination at a time.
**Tags:** #data-integration #workflow-orchestration #automation #evaluation-metrics #compliance #descriptive-statistics #quick-win #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make customer data collected, unified and activated without the buyer having a data team — and whoever does that best owns the organisations that cannot build any of it themselves.

## The Problem
Maintaining hundreds of connectors to systems that change without notice is a solved operational problem. Integration platforms built connector frameworks, automated schema handling, monitoring with per-connector health, retry and dead-letter handling, and versioning that survives a partner's breaking change. They did it because the connector treadmill is the product's real cost. Customer data platforms maintain comparable destination catalogues and frequently handle the same problems less systematically, with failures surfacing as missing data downstream.

## What Already Exists
Connector frameworks with shared lifecycle management; schema evolution handling; per-connector monitoring and health; retry, backoff and dead-letter queues; and versioned connector releases with change notices.

## The Customization Gap
The adaptation is to destinations whose failures are invisible and whose payload is personal data. It requires: (1) failure detection based on downstream effect rather than on transport error, since a destination can accept records and do nothing with them — this silent acceptance is the characteristic failure and generic connector monitoring does not catch it; (2) consent and permitted-use travelling with every record, since different destinations may receive different subsets of the same profile and the filtering is a legal requirement; (3) identity mapping per destination, as each downstream tool keys on something different and the mapping is where profiles silently fragment; (4) real-time and batch paths with different guarantees, where the real-time path carries customer-facing consequences; and (5) operators who are marketers rather than integration engineers, which changes what monitoring can look like.

## Target Customer
Packaged platform vendors, marketing operations teams, and integration platform vendors for whom customer data activation is an adjacent market.

## Impact If Solved
Integration platforms solved the connector treadmill because it is the real cost, and customer data vendors rediscover it per destination. Detecting silent acceptance, and carrying consent per destination, are what generic connector monitoring does not do.
