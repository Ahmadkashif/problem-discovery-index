# Connector Depth Is Invisible Until You Need It

**Niche:** [[niches/no-code-app-builders/integration-and-connectors/profile|Integration & Connectors]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Fix (Pain Point)
**One-liner:** A connector exists, so the builder designs around it, and discovers three days in that it supports reading records and not updating them.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #graph-theory #data-integration #quick-win #automation
**Contested on:** Every serious competitor here is fighting to make the connection to whatever system the customer actually has work and keep working — and that contest splits between getting connected and staying connected, which is why this niche is not terminal and is decomposed below.

## The Problem
The marketplace lists a connector for the CRM. The builder plans their app around it: read the accounts, update the status field, trigger on new records. Two of those three work. The update operation is not supported, the trigger polls every fifteen minutes rather than firing on change, and neither fact is stated anywhere on the connector's listing page. Three days of design is wasted and the builder falls back to the generic HTTP block for one operation, which means the app now has two integration mechanisms to the same system, one of which nobody knows about.

## Why It's Still Broken
Connector listings are marketing surfaces that assert existence, and existence is binary in the marketplace's data model while capability is not. Capability metadata would be a maintenance burden and would make partial connectors look bad, which is a commercial disincentive against exactly the transparency builders need. Community connectors vary enormously in completeness and are listed identically to first-party ones. And a builder's wasted three days is not a support ticket, so the cost never reaches the vendor as a signal.

## What a Fix Looks Like
Publish capability, which requires no new technology at all. For every connector, list the operations supported against the operations the underlying API offers — a coverage percentage and an explicit list, which is computable by comparing the connector's implemented operations to the API's specification wherever one exists. State trigger mechanics plainly: event-driven or polling, and at what interval, since this single fact changes what can be built. Show reliability from the platform's own execution data — success rate, error classes, recent incidents — which the vendor has and never publishes. Distinguish first-party, partner and community connectors clearly, along with when each was last updated, since a community connector untouched for two years is a specific risk. Warn at design time rather than at runtime, when a builder references an operation the connector does not support. And feed the gaps into the roadmap, because the operations builders most often need and cannot find is a ranked list nobody has assembled.

## Who Feels the Pain
Builders designing around capabilities that do not exist; platform teams supporting apps with mixed integration mechanisms; and vendors whose marketplace size is undermined by depth complaints they cannot see.

## Impact If Fixed
Coverage and reliability metadata are computable from data every vendor holds, and publishing them turns a three-day discovery into a three-second one. The most-requested-missing-operation list is the roadmap output and currently exists nowhere.
