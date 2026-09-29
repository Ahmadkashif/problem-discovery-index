# Version Compatibility From API Platforms

**Niche:** [[niches/game-analytics-vendors/the-instrumentation-engineer/profile|The Instrumentation Engineer]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** API platforms made supporting many client versions a solved discipline, and game telemetry reconciles them by hand.
**Tags:** #data-integration #workflow-orchestration #compliance #automation #evaluation-metrics #sets-and-logic #worker-facing #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to let one engineer keep data consistent across six live client versions all sending slightly different schemas — and whoever supports that person takes the account.

## The Problem
Supporting many simultaneous client versions is a solved problem in API platform engineering. Versioned interfaces, translation layers mapping old shapes to current ones, deprecation policies with defined sunset dates, per-version usage monitoring, and compatibility testing across every supported version are all standard practice. Any platform with third-party clients runs this. Game telemetry has the identical structure and handles it as accumulated transformation code.

## What Already Exists
Explicit interface versioning; translation layers between versions; deprecation policies with sunset dates; per-version usage monitoring; and compatibility test suites.

## The Customization Gap
The adaptation is to clients that cannot be deprecated because they are games people are playing. It requires: (1) no ability to sunset an old version, since players on an old build are players and cutting them off is not an option — this is the substantive difference and removes the main mechanism for limiting complexity; (2) semantic rather than structural divergence, where the same event means something different because the game changed; (3) store review and console certification making client updates slow; (4) a data pipeline rather than a request-response interface, so validation happens after the fact; and (5) a single engineer rather than a platform team, requiring something far lighter than API governance.

## Target Customer
Studio data platform teams, game analytics vendors, publishers, and API and data platform tooling vendors.

## Impact If Solved
API platforms made multi-version support a discipline with translation layers and deprecation policy. Players on an old build cannot be sunset, which removes the main mechanism for limiting the complexity.
