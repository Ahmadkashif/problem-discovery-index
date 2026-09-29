# The Most Privileged Position and the Least Used

**Niche:** [[niches/api-infrastructure-providers/api-gateways-and-management/profile|API Gateways & Management]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The gateway sees every request and response between every system and uses that position to enforce rate limits and compute latency percentiles.
**Tags:** #graph-theory #descriptive-statistics #change-point-detection #evaluation-metrics #confidence-intervals #data-integration #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to be the layer every API call passes through — and that contest is fought twice, for internal traffic and for external consumers, which is why this niche is not terminal and is decomposed below.

## The Problem
An organisation runs a gateway in front of four hundred services. It handles authentication, rate limiting, routing and retries competently. It also observes the complete integration behaviour of the entire estate: which services call which, with what payloads, how that changes over time, where the coupling actually is as opposed to where the architecture diagram says it is. Asked which services depend on the customer service, the organisation draws a diagram from memory. The gateway could answer exactly and has never been asked.

## Why Nobody Has Built This
The gateway's product identity is policy enforcement, and the roadmap has followed policy features because that is what the category has always sold. Retaining and analysing payload-level traffic raises cost and privacy questions that are real and have been treated as prohibitive rather than as design constraints — sampling and structural extraction answer most questions at negligible cost. And the two customer types pull the roadmap in different directions simultaneously, which has produced a product that does policy well for both and the interesting work for neither.

## What to Build
The shared layer both sub-niches need: the traffic record as a first-class asset. Derive the actual service dependency graph continuously from observed calls, which is more accurate than any maintained diagram and is immediately useful for change management, incident diagnosis and architectural work. Extract structural behaviour by sampling — which fields are sent, which are returned, what value shapes occur, which combinations are used — with no retention of content, which makes the privacy position defensible and answers the questions that matter. Detect change in that behaviour, since a consumer whose request shape shifted or a service whose response distribution moved is a signal that currently surfaces as an incident. Attach identity throughout, resolving credentials to owning teams or organisations, because almost every useful question ends in who. And expose all of it as a queryable model rather than a dashboard, since the questions are open-ended and each sub-niche below builds different answers on the same foundation.

## Target Customer
Platform engineering and API product functions; and the gateway vendors themselves, for whom this is the differentiation available in a market where proxying has become commodity.

## Impact If Built
The gateway holds the only complete record of how an organisation's software actually integrates and reports almost none of it. Sampled structural extraction answers the important questions without retaining content, which removes the obstacle that has kept this position unexploited.
