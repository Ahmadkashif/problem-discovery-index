# Rebuilding the Same Dashboard Set

**Niche:** [[niches/revops-consultancies/funnel-model-reuse/profile|Funnel Model & Reporting Reuse]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Fix (Pain Point)
**One-liner:** The consultant is building the manager dashboard again, from memory, in a different platform.
**Tags:** #quick-win #automation #workflow-orchestration #evaluation-metrics #data-integration #descriptive-statistics #worker-facing #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to stop rebuilding the same funnel model, stage definitions and dashboard set for the twentieth time, and whoever packages it takes the account.

## The Problem
Dashboard building consumes days on every engagement and produces something very close to what the consultant built last time. The metrics are the same, the layout is the same, the filters are the same. The rebuild happens because the previous version lives in a client's system, the documentation of it is a screenshot, and nobody has written down what the standard set actually is.

## Why It's Still Broken
The standard was never written down — a set of reports that exists only as instances inside client systems cannot be reused, because there is nothing to reuse. Screenshots are not specifications. Platform differences discourage a single artefact. And rebuilding is quick enough per dashboard to never become a project.

## What a Fix Looks Like
Write the standard set down before trying to automate it. Document the standard dashboard set as specifications — metrics, filters, layout, audience — which is the fix and is a document rather than a product. Capture the definition of every metric precisely, since that is what actually gets debated on every engagement. Keep a per-platform build note so the specification translates. Export and store the configuration from each build where the platform permits, which accumulates into reusable artefacts. Record which dashboards clients actually used afterwards, as some of the standard set is always ignored. Trim the standard set to what gets used rather than what is impressive. Share the specification across the consultancy rather than per consultant. Adapt the wording per client while keeping the structure, which is the real variation. Update the specification when a better version emerges on an engagement. And use the documented set in proposals, which signals maturity and shortens the design discussion.

## Who Feels the Pain
Consultants rebuilding from memory; clients paying for a standard artefact at bespoke rates; engagements whose schedule is consumed by configuration; and the consultancy, whose repeated work never becomes an asset.

## Impact If Fixed
A set of reports that exists only as instances inside client systems cannot be reused, because there is nothing to reuse. A written specification of the standard set is the artefact everything else can be built from.
