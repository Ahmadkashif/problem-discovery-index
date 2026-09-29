# Impact Analysis From Compiler and Package Ecosystems

**Niche:** [[niches/api-infrastructure-providers/breaking-change-and-deprecation/profile|Breaking Change & Deprecation]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Package ecosystems built semantic versioning, deprecation tooling and automated migration to manage exactly this problem, and API providers manage it with an email.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #automation #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to tell a provider exactly which consumers a proposed change would break, before it ships — and whoever does that takes the platform, because the inability to answer it is why nothing is ever retired.

## The Problem
Library ecosystems face the same problem and have built machinery for it: semantic versioning as a contract, deprecation annotations that surface at compile time, automated migration tooling that rewrites consumer code, and dependency graphs that show who uses what. API providers, who have strictly more information — they can see the actual calls rather than inferring from static dependencies — manage change with a blog post and a sunset header.

## What Already Exists
Semantic versioning conventions and tooling; deprecation annotation and compile-time warning mechanisms; automated code migration and codemod tooling; package dependency graph analysis at ecosystem scale; and API diffing tools that classify a specification change as breaking or compatible. All mature and mostly open.

## The Customization Gap
The adaptation is to runtime consumers rather than compile-time dependents. It requires: (1) observed rather than declared usage, which is the fundamental advantage here — a library author infers who might break from static dependencies and an API provider can see who does break, and no product exploits that; (2) breaking-change classification that accounts for consumer tolerance, since whether removing a field breaks a consumer depends on their parser and not only on the change, and the same change is breaking for some consumers and not others; (3) consumer-side migration assistance, which is the analogue of a codemod and is harder because the provider does not have the consumer's code — but can supply a precise description of what to change and a test endpoint to verify against; (4) graduated rollout of the change itself, applying it to a small share of traffic or a subset of consumers first, which package ecosystems cannot do and API providers can, and almost none do; and (5) notification that reaches a human, since the deprecation header is read by nobody and the credential's registered owner is the person who needs to know.

## Target Customer
Gateway and API management vendors, developer platform teams, and the API product functions responsible for lifecycle.

## Impact If Solved
The library world's machinery transfers and the API provider's position is strictly better, since usage is observed rather than inferred. Graduated rollout of a breaking change is available here and nowhere else, and is the safest possible way to find out who breaks.
