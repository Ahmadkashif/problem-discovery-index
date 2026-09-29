# Discovered in Week Five

**Niche:** [[niches/ap-automation-vendors/erp-and-dimension-mapping/profile|ERP & Dimension Mapping]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The customer uses a dimension in a way the connector does not support, and everyone finds out five weeks into the implementation.
**Tags:** #quick-win #data-integration #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #worker-facing #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to map a customer's chart of accounts, dimensions and custom fields without six weeks of a consultant — and whoever makes the integration cover the non-standard fields wins the deals that die in implementation.

## The Problem
Implementation proceeds on the assumption that the customer's ERP is configured in a supported way. In week five, testing reveals that their approval hierarchy depends on a custom field, or that their tax handling differs by entity in a way the connector does not express, or that they are on an ERP version with a different API. The project stalls, the scope changes, and the customer's confidence in the whole purchase drops. All of it was discoverable on day one by reading their configuration.

## Why It's Still Broken
Discovery is a questionnaire the customer fills in, so it captures what they know to mention rather than what the integration needs — and a finance team cannot describe configuration details they have never thought about. Reading the ERP configuration directly requires access granted later in the project. Implementation is measured on go-live rather than on slippage causes. And the same surprises recur without anyone cataloguing them.

## What a Fix Looks Like
Read the configuration before promising anything. Connect and inspect the ERP configuration at the start rather than midway, which is the fix and moves every surprise to week one. Run an automated compatibility check against known unsupported patterns, since the list of things that break is well known to the implementation team and written nowhere. Catalogue the surprises from past projects, as the same ten issues cause most of the slippage. Report expected complexity from the configuration, so scoping is based on evidence rather than on a questionnaire. Replace the questionnaire with inspection wherever possible, because customers cannot answer questions about configuration they inherited. Flag ERP version and edition differences immediately, as they are deterministic and are found by accident today. Tell the customer what will need to change on their side early, since some fixes are theirs and take time. Track slippage causes, which will confirm that a small set of issues dominates. Prepare the known workarounds rather than reinventing each time. And give sales a qualification check, so unsupported configurations are known before a contract rather than after.

## Who Feels the Pain
Implementation consultants explaining a slipped date; customers whose deployment stalls; sales teams whose references are damaged; and vendors whose service margin evaporates in rework.

## Impact If Fixed
Discovery is a questionnaire, so it captures what the customer knows to mention rather than what the integration needs. Inspecting the configuration on day one moves every surprise from week five to week one.
