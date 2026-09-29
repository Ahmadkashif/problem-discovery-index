# Designing Blind, Judged in Production

**Niche:** [[niches/headless-commerce-vendors/the-solutions-architect/profile|The Solutions Architect]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Solutions architects live inside multi-year replatforming programmes, designing compositions whose failure modes only appear in production, held responsible for outcomes that depend on a dozen parties.
**Tags:** #worker-facing #evaluation-metrics #confidence-intervals #graph-theory #workflow-orchestration #tacit-knowledge-ml #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to let an architect find out whether a composition works before the programme commits to it — and whoever does that takes the delivery quality, because the failure modes currently appear in production eighteen months later.

## The Problem
An architect designs a composition: this commerce platform, this search service, this content platform, this personalisation layer, with inventory here and pricing there and the front end rendering server-side. Each choice is defensible. The composition has a property nobody noticed — the personalisation call sits in the critical path of the product page and the vendor's response time at the ninety-ninth percentile is four hundred milliseconds — which becomes a conversion problem visible eighteen months later at peak. The architect is answerable for it and could not have known, because the only place that information exists is other retailers' production systems.

## Why Nobody Has Built This
Composition performance and failure modes are emergent and nobody produces the evidence. Vendors document intended behaviour and publish no operating characteristics under real load. Each implementation's learnings stay with the team that had them. Architects share informally at conferences, which is a slow and lossy channel. And the feedback loop from production to design spans eighteen months and two organisations.

## What to Build
Give the architect evidence before the commitment. Build a composition sandbox where a proposed stack can be assembled and load-tested against realistic traffic and catalogue before the programme commits, which is the artefact that does not exist and which would surface the critical-path and latency problems while they are still design decisions. Publish observed operating characteristics per vendor service — latency distributions, failure behaviour, rate limits, consistency windows — measured rather than documented, since the intended behaviour is not the useful information. Maintain a pattern library of compositions with their outcomes, which the pattern intelligence niche develops and which is the accumulated knowledge architects currently trade informally. Record architecture decisions with their reasoning and revisit them against production, so the loop closes within the organisation even if it does not across it. Model the critical path explicitly, since a service in it and a service out of it have completely different requirements and the distinction is frequently not made deliberately. Provide failure mode analysis for a proposed composition, naming what happens when each service degrades, which is a design exercise the architect can do with a prompt and mostly does not. Feed production outcomes back to the architects who designed them, which almost never happens across an integrator boundary. And give the role standing to say a composition will not work, since the commercial pressure in a replatform runs the other way.

## Target Customer
Vendor and integrator delivery organisations, the architects, and the retailers whose programmes depend on these decisions.

## Impact If Built
The information that would have prevented the failure exists only in other retailers' production systems. A composition sandbox surfaces latency and critical-path problems while they are still design decisions, and measured vendor operating characteristics replace documentation of intent.
