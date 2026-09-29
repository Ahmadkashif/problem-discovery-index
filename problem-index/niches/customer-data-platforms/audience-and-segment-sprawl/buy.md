# Asset Lifecycle Practice

**Niche:** [[niches/customer-data-platforms/audience-and-segment-sprawl/profile|Audience & Segment Sprawl]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every mature software discipline manages proliferating artefacts with ownership, usage tracking and deprecation, and audience builders ship none of it.
**Tags:** #workflow-orchestration #descriptive-statistics #evaluation-metrics #automation #compliance #graph-theory #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to tell an organisation which of its two thousand segments overlap, are stale or are the same idea three times — and whoever does that makes an unmanageable artefact governable.

## The Problem
Artefact proliferation is a known condition with known remedies. Dashboards, reports, feature flags, API endpoints and data models all accumulate, and mature organisations manage them with ownership metadata, usage instrumentation, deprecation processes, duplicate detection and periodic review. The tooling exists across several categories and the practice is unremarkable. Audience builders produce the same kind of artefact at greater volume with none of the management.

## What Already Exists
Asset catalogues with ownership and metadata; usage instrumentation and unused-asset detection; deprecation workflows with consumer notification; duplicate and similarity detection; and periodic review processes.

## The Customization Gap
The adaptation is to an artefact whose definition is a query and whose consumers are customer-facing. It requires: (1) similarity measured over both logic and membership, since two definitions can be textually different and semantically identical or textually similar and behaviourally opposite — this dual comparison has no analogue in dashboard catalogues; (2) deletion that risks a live customer-facing failure, such as a suppression list disappearing, which raises the stakes far beyond an unused dashboard; (3) consumers that span advertising platforms and messaging tools outside the system, so dependency tracking crosses a boundary; (4) a cost per artefact that is ongoing computation rather than storage, which makes the financial argument for cleanup unusually concrete; and (5) creators who are marketers rather than engineers, so the governance must be nearly invisible to be followed.

## Target Customer
Marketing operations teams, customer data platform vendors, and data catalogue vendors for whom audience artefacts are unserved.

## Impact If Solved
Every discipline with proliferating artefacts developed lifecycle management and audience builders shipped none. Comparing both logic and membership is the dual similarity check dashboard catalogues never needed, and ongoing computation cost makes the cleanup argument concrete.
