# Contract Testing From Software Integration

**Niche:** [[niches/technical-content-agencies/content-drift/profile|Content Drift]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software verifies that consumers' assumptions still hold when a provider changes, and documentation is a consumer nobody tests.
**Tags:** #automation #workflow-orchestration #compliance #evaluation-metrics #data-integration #change-point-detection #sets-and-logic #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to keep prose true about software that ships weekly, and whoever detects the drift automatically takes the account.

## The Problem
Software integration solved the problem of a provider changing under its consumers: contract testing verifies that what a consumer expects still holds, runs in the provider's pipeline, and fails the build when a change would break somebody. The consumer's expectations are explicit and executable. Documentation is a consumer of the product's interface — it asserts that methods exist, parameters are named thus, defaults are these — and nothing verifies any of it.

## What Already Exists
Executable consumer expectations; verification in the provider's pipeline; build failure on breaking change; versioned contracts; and consumer-driven change notification.

## The Customization Gap
The adaptation is to a consumer whose expectations are expressed in prose. It requires: (1) assertions embedded in human-readable text rather than in a test file, so the contract must be extracted from the documentation rather than written alongside it — this is the substantive difference and is the interesting technical problem; (2) assertions about behaviour and defaults as well as about signatures; (3) a consumer maintained by writers rather than engineers, so the failures must be actionable by them; (4) screenshots and interface descriptions with no executable analogue; and (5) a provider team that does not currently consider documentation a consumer at all.

## Target Customer
Documentation teams and agencies, engineering and developer experience leadership, documentation and testing tooling vendors, and platform teams.

## Impact If Solved
Contract testing verifies that consumers' expectations still hold and fails the build when they do not. Extracting an executable contract from prose is the interesting problem, and documentation is a consumer nobody has treated as one.
