# Deprecation Practice From Platform Engineering

**Niche:** [[niches/data-platform-integrators/retirement-and-rationalisation/profile|Retirement & Rationalisation]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software platforms deprecate and remove interfaces routinely with notice and monitoring, and data assets are never removed at all.
**Tags:** #compliance #workflow-orchestration #graph-theory #automation #evaluation-metrics #data-integration #sets-and-logic #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to actually remove an unused asset, which requires proving nothing depends on it and finding someone willing to say so — and whoever makes deletion safe takes the account.

## The Problem
Software platforms remove interfaces all the time and have a practice for it: mark as deprecated, notify consumers, publish a sunset date, monitor remaining usage, and remove. The practice exists because an interface that can never be removed accumulates into an unmaintainable surface. It works because deprecation is a staged process with monitoring rather than a single decision. Data estates have no deprecation practice at all and consequently never shrink.

## What Already Exists
Deprecation marking and consumer notification; published sunset timelines; usage monitoring during the deprecation window; staged removal with rollback; and breaking-change communication norms.

## The Customization Gap
The adaptation is to assets whose consumers are people and spreadsheets rather than registered clients. It requires: (1) consumers who are unregistered and often unknown — an analyst's saved query or a finance spreadsheet pulling an extract — so notification must reach people rather than integrations, which is the substantive difference; (2) lineage that stops at the platform boundary while the dependencies do not; (3) assets whose removal may break a report someone runs quarterly, so the monitoring window must be long; (4) no versioning concept for a table, so there is no deprecated-but-available state natively; and (5) data retention and audit requirements that may prohibit removal entirely.

## Target Customer
Data platform teams and leadership, integrators, catalogue and lineage vendors, and governance providers.

## Impact If Solved
Software deprecates routinely because an unremovable interface accumulates into an unmaintainable surface, and the staged process is what makes it safe. Unregistered human consumers and quarterly readers are what the data version must notify and wait for.
