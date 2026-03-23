# Multi-Unit Infestation Mapping & Treatment Orchestration

**Niche:** [[niches/pest-control/bed-bug-remediation/profile|Bed Bug Remediation]]
**Industry:** [[industries/pest-control|Pest Control]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool maps bed bug infestations across multi-unit buildings, tracks which adjacent units need inspection, or orchestrates building-wide treatment sequences.
**Tags:** #graph-ml #data-integration #workflow-orchestration #tacit-knowledge-ml

## The Problem
In apartment buildings and hotels, bed bugs spread between adjacent units through wall voids, shared plumbing, and electrical conduits. Experienced technicians know that treating Unit 305 requires inspecting 205, 405, 304, and 306 — and that the infestation likely originated from the unit with the heaviest activity, not the one that reported first. This spatial reasoning about infestation spread patterns is tacit knowledge that junior techs lack. Without systematic mapping, companies treat individual units reactively, only to return 4-6 weeks later when bugs re-emerge from an untreated adjacent unit.

## Why Nobody Has Built This
Building-wide infestation management requires a spatial data model (unit layouts, adjacency relationships, shared infrastructure paths) that no pest control platform has. Treatment history must be tracked per-unit with temporal sequencing (which units were treated in what order, with what results). The graph structure of "which units are connected to which through what pathways" is unique to each building and must be built from floor plans or discovery.

## What to Build
A building-level infestation management platform: input a building's floor plan (or construct a unit adjacency graph), log inspections and treatments per unit with timestamps, and the system identifies high-risk adjacent units requiring proactive inspection. The platform recommends treatment sequencing (treat from the periphery inward to prevent escape), tracks reinfestation patterns, and provides property managers with a building-wide status dashboard. Over time, the system learns which building characteristics (age, construction type, shared infrastructure) predict spread patterns.

## Target Customer
Bed bug remediation companies working with property management firms that manage 500+ unit apartment buildings and experience recurring reinfestation from incomplete building-wide treatment.

## Impact If Built
Reduces reinfestation callbacks by 40-60% (each callback costs $500-$1,500 in re-treatment), improves property manager relationships, and enables building-wide treatment contracts worth $10,000-$50,000 per building.
